transform parallel_anim_transform(pos, xysize, opacity):
    pos pos
    xysize xysize
    alpha opacity

transform parallel_anim_blend_mode(blend_mode):
    blend BLEND_MODE_NAMES[blend_mode]

transform fadeat(new_alpha):
    alpha new_alpha

transform flipped():
    xzoom -1.0

transform fadeto(old_alpha, new_alpha, duration=1.0):
    alpha old_alpha
    linear duration alpha new_alpha

transform fadetoease(old_alpha, new_alpha, duration=1.0):
    alpha old_alpha
    ease duration alpha new_alpha

transform fadetoeasein(old_alpha, new_alpha, duration=1.0):
    alpha old_alpha
    easein duration alpha new_alpha

transform moveat(new_pos):
    pos new_pos

transform blendpic(blend_mode):
    blend BLEND_MODE_NAMES[blend_mode]

transform moveto(old_pos, new_pos, duration=1.0):
    pos old_pos
    linear duration pos new_pos

transform movetoease(old_pos, new_pos, duration=1.0):
    pos old_pos
    ease duration pos new_pos

transform sizeat(new_size):
    xysize new_size

transform sizeto(old_size, new_size, duration=1.0):
    xysize old_size
    linear duration xysize new_size

transform sizetoease(old_size, new_size, duration=1.0):
    xysize old_size
    ease duration xysize new_size

init python:
    def set_dialogue_size(size):
        style.say_dialogue.size = size

    def fadeattext(a):
        return "fadeat(" + str(a) + ")"

    def fadetotext(a, b, duration):
        return "fadeto(" + str(a) + ", " + str(b) + ", " + "{:.4f}".format(duration) + ")"

    def blendpictext(a):
        return "blend(" + BLEND_MODE_NAMES[a] + ")"

    def moveattext(a):
        return "moveat((" + str(a[0]) + ", " + str(a[1]) + "))"

    def flippedtext():
        return "flipped"

    def movetotext(a, b, duration):
        return "moveto((" + str(a[0]) + ", " + str(a[1]) + "), (" + str(b[0]) + ", " + str(b[1]) + "), " + "{:.4f}".format(duration) + ")"

    def sizeattext(a):
        return "sizeat((" + str(a[0]) + ", " + str(a[1]) + "))"

    def sizetotext(a, b, duration):
        return "sizeto((" + str(a[0]) + ", " + str(a[1]) + "), (" + str(b[0]) + ", " + str(b[1]) + "), " + "{:.4f}".format(duration) + ")"

    def shake_screen(power, speed, duration):
        size = power * speed
        delay = duration / 120
        renpy.with_statement(Move((size, 0), (-size, 0), 0.5 / power, repeat = True, bounce = True, delay=delay))

    def flash_screen(rgba, frames, wait):
        duration = frames / 120
        _window_hide()
        rgb_hex = '{:02x}{:02x}{:02x}{:02x}'.format(rgba[0], rgba[1], rgba[2], rgba[3])
        fadeflash = fadetoeasein(1.0, 0.0, duration)
        renpy.show("flash_screen", what=Solid(rgb_hex, xysize=(config.screen_width, config.screen_height)), at_list=[fadeflash], zorder=4000)
        if wait:
            renpy.pause(duration)
            renpy.hide("flash_screen")
        else:
            images_shown.append("flash_screen")

    def x_if_android():
        return "x-" if renpy.android else ""

    def get_filename(image):
        if image == None:
            return ""
        image_string = image if type(image) is str else image[0]
        if renpy.loadable("images/faces/" + image_string + ".png"):
            return "faces/" + image_string + ".png"
        if renpy.loadable("images/faces/" + image_string + ".webp"):
            return "faces/" + image_string + ".webp"
        if renpy.loadable("images/pictures/" + image_string + ".webp"):
            return "pictures/" + image_string + ".webp"
        if renpy.loadable("images/bg/" + image_string + ".webp"):
            return "bg/" + image_string + ".webp"
        if renpy.loadable("images/maps/" + image_string + ".webp"):
            return "maps/" + image_string + ".webp"
        if renpy.loadable("images/icons/" + image_string + ".webp"):
            return "icons/" + image_string + ".webp"
        if renpy.loadable("images/choices/" + image_string + ".webp"):
            return "choices/" + image_string + ".webp"
        if renpy.loadable("images/characters/" + image_string + ".webp"):
            return "characters/" + image_string + ".webp"
        if renpy.loadable("images/movielast/" + image_string + ".webp"):
            return "movielast/" + image_string + ".webp"
        if renpy.loadable("images/gallery/" + image_string + ".webp"):
            return "gallery/" + image_string + ".webp"
        return image_string + ".webp"

    MAX_IMAGES = 101
    MAX_VIDEOS = 8

    def get_o(filename):
        f = renpy.open_file("images/" + get_filename(filename))
        f.seek(4)
        return int.from_bytes(f.read(1), "big") + (int.from_bytes(f.read(1), "big") * 2) + (int.from_bytes(f.read(1), "big") * 3) + (int.from_bytes(f.read(1), "big") * 4)

    def hide_shown_images(leave_videos = False):
        global images_shown
        images_being_shown = []
        for shown_image in images_shown:
            if not leave_videos or (not shown_image.startswith("video_looping_") and not shown_image.startswith("video_once_") and shown_image != "final_video_image"):
                renpy.hide(shown_image)
            else:
                images_being_shown.append(shown_image)
        images_shown = images_being_shown

    def hide_shown_videos(except_for):
        global images_shown
        images_being_shown = []
        allowed_videos = []
        if except_for != None:
            allowed_videos.append("video_looping_" + except_for["name"])
            allowed_videos.append("video_looping_" + except_for["name"] + "bg")
            allowed_videos.append("video_once_" + except_for["name"])
            allowed_videos.append("video_once_" + except_for["name"] + "bg")
        for shown_image in images_shown:
            if not shown_image.startswith("video_looping_") and not shown_image.startswith("video_once_"):
                images_being_shown.append(shown_image)
            elif shown_image in allowed_videos:
                images_being_shown.append(shown_image)
            else:
                renpy.hide(shown_image)
        images_shown = images_being_shown

    def get_callback_function(function_name):
        if function_name in user_defined_callback_functions:
            return user_defined_callback_functions[function_name]
        return None

    def call_user_defined_callbacks():
        global user_defined_callbacks
        for id in user_defined_callbacks:
            for callback, parameters in user_defined_callbacks[id]:
                callback_function = get_callback_function(callback)
                callback_function(*parameters)
        user_defined_callbacks = {}

    def reset_pictures(hard = False):
        global pictures, moving_pictures, cached_moving_pictures, videos, playing_videos, obscured_videos, obscured_playing_videos, last_displayed_pictures, last_displayed_map, last_displayed_pictures_set, scene_state, final_video_image, user_defined_images
        
        user_defined_images = {}
        call_user_defined_callbacks()
        pictures = [None for _ in range(MAX_IMAGES)]
        moving_pictures = [None for _ in range(MAX_IMAGES)]
        cached_moving_pictures = []
        videos = [None for _ in range(MAX_VIDEOS)]
        playing_videos = []
        obscured_videos = [None for _ in range(MAX_VIDEOS)]
        obscured_playing_videos = []
        last_displayed_pictures = None
        last_displayed_map = None
        final_video_image = None
        hide_shown_images()
        if hard:
            scene_state = "dirty" if scene_state != "faded_out" else "faded_out"
            last_displayed_pictures_set = []

    def set_transparency_backgrounds(new_backgrounds = []):
        global next_transparency_backgrounds
        global raw_transparency_backgrounds
        global transparency_backgrounds_needs_fade
        adjusted_backgrounds = adjust_backgrounds([new_backgrounds] if type(new_backgrounds) is str else new_backgrounds, "transparency")
        if adjusted_backgrounds != transparency_backgrounds:
            raw_transparency_backgrounds = new_backgrounds
            next_transparency_backgrounds = adjusted_backgrounds
            transparency_backgrounds_needs_fade = scene_state == "resolved"

    def set_map_backgrounds(new_backgrounds = []):
        global next_map_backgrounds
        global raw_map_backgrounds
        global map_backgrounds_needs_fade
        adjusted_backgrounds = adjust_backgrounds([new_backgrounds] if type(new_backgrounds) is str else new_backgrounds, "map")
        if adjusted_backgrounds != map_backgrounds:
            raw_map_backgrounds = new_backgrounds
            next_map_backgrounds = adjusted_backgrounds
            map_backgrounds_needs_fade = scene_state == "resolved"

    def get_small_image_from_backgrounds(backgrounds):
        composite_values = []
        for background in backgrounds:
            composite_values.append((0, 0))
            composite_values.append(im.FactorScale(get_filename(day_to_night(background)), 0.25))
        return Composite((round(config.screen_width / 4), round(config.screen_height / 4)), *composite_values)

    def get_full_image_from_backgrounds(backgrounds):
        composite_values = []
        for background in backgrounds:
            composite_values.append((0, 0))
            composite_values.append(get_filename(day_to_night(background)))
        return Composite((config.screen_width, config.screen_height), *composite_values)

    video_order = -1

    def calculate_video_order():
        global video_order
        video_order = -1
        for id, picture in enumerate(pictures):
            if picture != None and picture_is_opaque(id):
                video_order = id

    def reset_obscured_video(id):
        global obscured_playing_videos
        obscured_videos[id] = None
        obscured_playing_videos = list(filter(lambda x: x != id, obscured_playing_videos))

    def add_video_to_scene(video_object):
        global scene_state, playing_videos
        if scene_state == "resolved":
            scene_state = "dirty"
        id = video_object["id"]
        reset_obscured_video(id)
        videos[id] = video_object
        playing_videos = [id]
        calculate_video_order()
        if (scene_state == "faded_out" or scene_state == "fade_out") and redux_conf("play_faded_out_videos"):
            fade_in()
            resolve_scene()

    def play_video_looped(id, name, filename, width=config.screen_width, height=config.screen_height):
        add_video_to_scene({
            "id": id,
            "name": name,
            "filename": filename,
            "looping": True,
            "movie": None,
            "no_pause": True,
            "width": width,
            "height": height,
        })

    def play_video_once(id, name, filename, duration, final_image, width, height, no_pause = False):
        add_video_to_scene({
            "id": id,
            "name": name,
            "filename": filename,
            "duration": duration,
            "final_image": final_image,
            "looping": False,
            "movie": None,
            "no_pause": no_pause,
            "width": width,
            "height": height,
        })

    def stop_video(id, but_keep_final_image = False):
        global scene_state, playing_videos, images_shown, final_video_image
        if scene_state == "resolved":
            scene_state = "dirty"
        the_video = videos[id]
        videos[id] = None
        if not but_keep_final_image:
            final_video_image = None
        playing_videos = list(filter(lambda x: x != id, playing_videos))
        reset_obscured_video(id)
        if the_video != None:
            new_images_shown = []
            video_names = ["video_looping_" + the_video["name"], "video_once_" + the_video["name"]]
            if not but_keep_final_image:
                video_names.append("final_video_image")
            for shown_image in images_shown:
                if shown_image in video_names:
                    renpy.hide(shown_image)
                else:
                    new_images_shown.append(shown_image)
            images_shown = new_images_shown

    def obscure_videos():
        global scene_state
        if scene_state == "resolved":
            scene_state = "dirty"
        global videos, playing_videos, obscured_videos, obscured_playing_videos
        obscured_videos = videos
        obscured_playing_videos = playing_videos
        videos = [None for _ in range(MAX_VIDEOS)]
        playing_videos = []

    def at_origin(pos, origin, width, height, scale):
        if origin != 1:
            return pos
        return (round(pos[0] - (width * scale[0] / 100) / 2), round(pos[1] - (height * scale[1] / 100) / 2))

    def show_picture(id, image, origin=0, designation=0, pos=(0, 0), scale=(100, 100), width=config.screen_width, height=config.screen_height, opacity=255, blend_mode=0, is_transparent=False, blink_image=False, breathe_image=False):
        global scene_state, user_defined_images
        if scene_state == "resolved":
            scene_state = "dirty"
        if opacity > 0 and not (is_transparent or image == "") and scene_state != "faded_out":
            obscure_videos()
        try:
            flipped = should_flip()
        except NameError:
            flipped = False
        pictures[id] = {
            "id": id,
            "image": image,
            "width": width,
            "height": height,
            "origin": origin,
            "designation": designation,
            "pos": at_origin(pos, origin, width, height, scale),
            "scale": scale,
            "opacity": opacity,
            "blend_mode": blend_mode,
            "is_transparent": is_transparent or image == "",
            "blink_image": blink_image,
            "breathe_image": breathe_image,
            "rotating": 0,
            "faded_out": False,
            "flipped": flipped,
        }
        moving_pictures[id] = None
        if id in user_defined_images:
            del user_defined_images[id]
        call_user_defined_callbacks()

    def recalculate_backgrounds_if_needed():
        global recalculate_backgrounds
        if recalculate_backgrounds:
            set_transparency_backgrounds(raw_transparency_backgrounds)
            set_map_backgrounds(raw_map_backgrounds)
            recalculate_backgrounds = False

    def show_transparent(id, image, origin=0, designation=0, pos=(0, 0), scale=(100, 100), opacity=255, blend_mode=0, width=config.screen_width, height=config.screen_height):
        show_picture(id, image, origin=origin, designation=designation, pos=pos, scale=scale, width=width, height=height, opacity=opacity, blend_mode=blend_mode, is_transparent=True)

    def spo(id, image, px, py, sx, sy, w, h, origin=0, designation=0, opacity=255, blend_mode=0, is_transparent=False, blink_image=False, breathe_image=False):
        show_picture(
            id=id,
            image=image,
            origin=origin,
            designation=designation,
            pos=(px ^ dex, py ^ dex),
            scale=(sx ^ dex, sy ^ dex),
            width=w ^ dex,
            height=h ^ dex,
            opacity=opacity,
            blend_mode=blend_mode,
            is_transparent=is_transparent,
            blink_image=blink_image,
            breathe_image=breathe_image
        )

    def sto(id, image, px, py, sx, sy, w, h, origin=0, designation=0, opacity=255, blend_mode=0):
        show_transparent(
            id=id,
            image=image,
            origin=origin,
            designation=designation,
            pos=(px ^ dex, py ^ dex),
            scale=(sx ^ dex, sy ^ dex),
            width=w ^ dex,
            height=h ^ dex,
            opacity=opacity,
            blend_mode=blend_mode,
        )

    def move_picture(id, frames=0, origin=0, designation=0, pos=(0, 0), scale=(100, 100), opacity=255, blend_mode=0):
        global scene_state
        if scene_state == "resolved":
            scene_state = "dirty"
        if moving_pictures[id] != None and pictures[id] != None:
            pictures[id] = get_moved_picture(pictures[id], moving_pictures[id])
        moving_pictures[id] = {
            "id": id,
            "frames": frames,
            "origin": origin,
            "designation": designation,
            "scale": scale,
            "opacity": opacity,
            "blend_mode": blend_mode,
            "width": 0,
            "height": 0,
        }
        if pictures[id] != None:
            if "width" in pictures[id] and "height" in pictures[id]:
                moving_pictures[id]["width"] = pictures[id]["width"]
                moving_pictures[id]["height"] = pictures[id]["height"]
            pictures[id]["faded_out"] = False
        if moving_pictures[id] is not None:
            moving_pictures[id]["pos"] = at_origin(pos, origin, moving_pictures[id]["width"], moving_pictures[id]["height"], scale)
        if pictures[id] != None and moving_pictures[id] is not None:
            if scene_state == "faded_out" or scene_state == "fade_out":
                if redux_conf("remove_faded_out_pictures"):
                    pictures[id] = get_moved_picture(pictures[id], moving_pictures[id])
                else:
                    cached_moving_pictures.append((id, moving_pictures[id]))
                    moving_pictures[id] = None

    def erase_picture(id):
        global user_defined_images, scene_state
        if scene_state == "resolved" and pictures[id] != None:
            scene_state = "dirty"
        pictures[id] = None
        if id in user_defined_images:
            del user_defined_images[id]        
        call_user_defined_callbacks()

    def rotate_picture(id, speed):
        pictures[id]["rotating"] = speed

    def apply_manipulators(image, picture):
        return image

    def get_blink_animation(visible, not_visible):
        return Animation(not_visible, 2 + renpy.random.random(), visible, 0.08, not_visible, 2 + renpy.random.random(), visible, 0.08)

    def get_picture_image(picture):
        if picture["opacity"] == 0 and not picture["blink_image"] and not picture["breathe_image"]:
            return None
        picture_width = picture["width"]
        picture_height = picture["height"]
        image = Image(get_filename(picture["image"]))
        if picture["width"] < config.screen_width and picture["height"] < config.screen_height:
            image = im.Composite((config.screen_width, config.screen_height), (0, 0) if not picture["flipped"] else (config.screen_width - picture["width"], 0), image)
            picture_width = config.screen_width
            picture_height = config.screen_height
        if picture["blink_image"]:
            not_visible = im.Alpha(image, 0)
            image = get_blink_animation(image, not_visible)
        elif not picture["breathe_image"] and picture["opacity"] != 255:
            image = im.Alpha(image, picture["opacity"] / 255)
        if is_message_background(picture) and persistent.say_window_alpha != 1.0:
            image = im.Alpha(image, persistent.say_window_alpha)
        if picture["flipped"]:
            image = Transform(image, xzoom=-1)
        if picture["scale"][0] != 100 or picture["scale"][1] != 100:
            image = Transform(image, xysize=(round(picture_width * picture["scale"][0] / 100), round(picture_height * picture["scale"][1] / 100)))
        if picture["blend_mode"] != 0:
            # 1 = add, 2 = multiply, 3 = screen (?)
            image = Transform(image, blend=BLEND_MODE_NAMES[picture["blend_mode"]])
        return image

    user_defined_images = {}
    user_defined_callbacks = {}

    def show_image(id, image_to_show, blend_mode=0):
        global scene_state, user_defined_images, pictures, moving_pictures
        if scene_state == "resolved":
            scene_state = "dirty"
        user_defined_images[id] = (image_to_show, blend_mode)
        if id < MAX_IMAGES:
            pictures[id] = None
            moving_pictures[id] = None

    def add_hide_callback(id, callback_name, *parameters):
        if id not in user_defined_callbacks:
            user_defined_callbacks[id] = []
        user_defined_callbacks[id].append((callback_name, parameters))

    def get_picture_image_small(picture):
        if picture["opacity"] == 0:
            return None
        if picture["width"] < config.screen_width:
            return None
        image = im.FactorScale(Image(get_filename(picture["image"])), 0.25)
        if picture["scale"][0] != 100 or picture["scale"][1] != 100:
            image = Transform(image, xysize=(round(picture["width"] * 0.25 * picture["scale"][0] / 100), round(picture["height"] * 0.25 * picture["scale"][1] / 100)))
        return image

    def get_breathe_in_animation(visible, not_visible):
        return Animation(visible, 2.0, not_visible, 2.5)

    def get_breathe_in_animation_transforms(image, picture):
        transforms = []
        delay = 2.0
        moveto_function = movetoease
        sizeto_function = sizetoease
        fadeto_function = fadetoease
        scale_was = 120
        scale_to = 122
        was_size = (round(scale_was * picture["width"] / 100), round(scale_was * picture["height"] / 100))
        new_size = (round(scale_to * picture["width"] / 100), round(scale_to * picture["height"] / 100))
        transforms.append(moveat(get_displayed_pos(picture)))
        transforms.append(sizeto_function(was_size, new_size, delay))
        transforms.append(fadeto_function(0.0, 1.0, delay))

        return transforms

    def get_fade_in_transform():
        return fadeto(1.0, 0.0, FADE_DURATION)

    def get_breathe_out_animation(visible, not_visible):
        return Animation(not_visible, 2.0, visible, 2.0)

    def get_breathe_out_animation_transforms(image, picture):
        transforms = []
        delay = 2.0
        moveto_function = movetoease
        sizeto_function = sizetoease
        fadeto_function = fadetoease
        scale_was = 122
        scale_to = 120
        was_size = (round(scale_was * picture["width"] / 100), round(scale_was * picture["height"] / 100))
        new_size = (round(scale_to * picture["width"] / 100), round(scale_to * picture["height"] / 100))
        transforms.append(moveat(get_displayed_pos(picture)))
        transforms.append(sizeto_function(was_size, new_size, delay))
        transforms.append(fadeto_function(1.0, 0.0, delay))
        return transforms

    def get_moving_image_transforms(picture, moving, as_text = False):
        transforms = []
        delay = moving["frames"] / (30 * redux_conf("scene_animation_speed", 1.0))
        if as_text:
            moveat_function = moveattext
            sizeat_function = sizeattext
            fadeat_function = fadeattext
            moveto_function = movetotext
            sizeto_function = sizetotext
            fadeto_function = fadetotext
            blend_function = blendpictext
        else:
            moveat_function = moveat
            sizeat_function = sizeat
            fadeat_function = fadeat
            moveto_function = moveto
            sizeto_function = sizeto
            fadeto_function = fadeto
            blend_function = blendpic
        if not picture["blink_image"] and not picture["breathe_image"]:
            alpha_scale = persistent.say_window_alpha if is_message_background(picture) else 1.0
            if moving["opacity"] != picture["opacity"]:
                transforms.append(fadeto_function(alpha_scale * (picture["opacity"] / 255), alpha_scale * (moving["opacity"] / 255), delay))
            elif picture["opacity"] != 255 or alpha_scale != 1.0:
                transforms.append(fadeat_function(alpha_scale * (picture["opacity"] / 255)))
        if moving["pos"][0] != picture["pos"][0] or moving["pos"][1] != picture["pos"][1]:
            moving_pos = get_displayed_pos(moving)
            transforms.append(moveto_function(picture["pos"], moving_pos, delay))
        elif picture["pos"][0] != 0 or picture["pos"][1] != 0:
            moving_pos = get_displayed_pos(picture)
            transforms.append(moveat_function(moving_pos))
        if moving["scale"][0] != picture["scale"][0] or moving["scale"][1] != picture["scale"][1]:
            was_size = (round(picture["scale"][0] * picture["width"] / 100), round(picture["scale"][1] * picture["height"] / 100))
            new_size = (round(moving["scale"][0] * picture["width"] / 100), round(moving["scale"][1] * picture["height"] / 100))
            transforms.append(sizeto_function(was_size, new_size, delay))
        elif picture["scale"][0] != 100 or picture["scale"][1] != 100:
            new_size = (round(picture["scale"][0] * picture["width"] / 100), round(picture["scale"][1] * picture["height"] / 100))
            transforms.append(sizeat_function(new_size))
        if moving["blend_mode"] != 0:
            transforms.append(blend_function(moving["blend_mode"]))
        if as_text:
            return ":".join(transforms)
        return transforms

    def get_moved_picture(from_picture, to_picture):
        new_picture = {}
        for key, value in from_picture.items():
            if key in to_picture:
                new_picture[key] = to_picture[key]
            else:
                new_picture[key] = from_picture[key]
        if "width" not in new_picture and "width" in to_picture:
            new_picture["width"] = to_picture["width"]
        if "height" not in new_picture and "height" in to_picture:
            new_picture["height"] = to_picture["height"]
        return new_picture

    def copy_of_picture(picture):
        if type(picture) is str:
            return picture
        new_picture = {}
        for key, value in picture.items():
            new_picture[key] = picture[key]
        return new_picture

    def get_displayed_pos(displayed_picture):
        the_pos = (displayed_picture["pos"][0], displayed_picture["pos"][1])
        if displayed_picture["designation"] == 1:
            the_pos = (variable_value(displayed_picture["pos"][0]), variable_value(displayed_picture["pos"][1]))
        return the_pos

    def get_last_displayed_image(exclude_small = False):
        global last_displayed_pictures
        composite_values = []
        if last_displayed_pictures != None:
            for displayed_picture in last_displayed_pictures:
                if type(displayed_picture) is str:
                    displayed_image = Image(get_filename(displayed_picture))
                    displayed_pos = (0, 0)
                else:
                    if displayed_picture["width"] < config.screen_width and exclude_small:
                        displayed_image = None
                        displayed_pos = None
                    else:
                        displayed_image = get_picture_image(displayed_picture)
                        displayed_pos = displayed_picture["pos"]
                if displayed_image != None:
                    composite_values.append(displayed_pos)
                    composite_values.append(displayed_image)

        if len(composite_values) > 0:
            return Composite((config.screen_width, config.screen_height), *composite_values)

        return None

    def get_last_displayed_image_small():
        composite_values = []
        for displayed_picture in last_displayed_pictures_set:
            if type(displayed_picture) is str:
                displayed_image = im.FactorScale(Image(get_filename(displayed_picture)), 0.25)
                displayed_pos = (0, 0)
            else:
                displayed_image = get_picture_image_small(displayed_picture)
                displayed_pos = displayed_picture["pos"]
            if displayed_image != None:
                composite_values.append(displayed_pos)
                composite_values.append(displayed_image)

        if len(composite_values) > 0:
            return Composite((round(config.screen_width / 4), round(config.screen_height / 4)), *composite_values)

        return None

    def say_displayed_pictures():
        global last_displayed_pictures
        renpy.say(None, "say_displayed_pictures() length = " + str(len(last_displayed_pictures)))
        for displayed_picture in last_displayed_pictures:
            if type(displayed_picture) is str:
                renpy.say(None, "transparency bg = " + displayed_picture)
            elif displayed_picture == None:
                renpy.say(None, "None :(")
            else:
                renpy.say(None, "picture=" + displayed_picture["image"] + ", opacity=" + str(displayed_picture["opacity"]))

    def get_image_from_backgrounds(backgrounds, extra_images=[]):
        composite_values = []
        for background in backgrounds:
            composite_values.append((0, 0))
            composite_values.append(get_filename(day_to_night(background)))
        for extra_image in extra_images:
            composite_values.append(extra_image[0])
            if len(extra_image) >= 3:
                composite_values.append(Transform(Image(get_filename(extra_image[1])), xysize=extra_image[2]))
            else:
                composite_values.append(get_filename(extra_image[1]))
        return Composite((config.screen_width, config.screen_height), *composite_values)

    def get_map_background(include_previous = False, baked_event_image_map = None):
        last_displayed_image = get_last_displayed_image(exclude_small = True)
        if (map_backgrounds != None and len(map_backgrounds) > 0) and (redux_conf("map_backgrounds_have_priority") or last_displayed_image == None):
            return get_image_from_backgrounds(map_backgrounds, get_baked_event_images(current_map) if baked_event_image_map is None else get_baked_event_images(baked_event_image_map[0], baked_event_image_map[1]))
        elif include_previous:
            if last_displayed_image != None:
                return last_displayed_image
            elif transparency_backgrounds != None and len(transparency_backgrounds) > 0:
                return get_image_from_backgrounds([*transparency_backgrounds, "darkbg"])
            else:
                return Solid("#000000", xysize=(config.screen_width, config.screen_height))
        return None

    def show_map_background(include_previous = False, baked_event_image_map = None):
        bg = get_map_background(include_previous, baked_event_image_map)
        if bg != None:
            renpy.show("map_background", what=bg)
            images_shown.append("map_background")

    def hide_map_background(include_previous = False):
        if last_displayed_map != current_map and map_backgrounds != None and len(map_backgrounds) > 0:
            renpy.hide("map_background")
        elif include_previous:
            renpy.hide("map_background")

    def get_pos_text(pos):
        if pos[0] == 0 and pos[1] == 0:
            return ""
        return " pos=(" + str(pos[0]) + ", " + str(pos[1]) + ")"

    def get_raw_pos_text(pos):
        if pos[0] == 0 and pos[1] == 0:
            return ""
        return " rawpos=(" + str(pos[0]) + ", " + str(pos[1]) + ")"

    def get_size_text(w, h):
        if w == config.screen_width and h == config.screen_height:
            return ""
        return " w/h=(" + str(w) + ", " + str(h) + ")"

    def get_opacity_text(opacity):
        if opacity == 255:
            return ""
        return " opacity=" + str(opacity) + " "

    def get_scale_text(scale):
        if scale[0] == 100 and scale[1] == 100:
            return ""
        return " scale=" + str(scale[0]) + "," + str(scale[1]) + " "

    def get_blend_text(blend):
        if blend == 0:
            return ""
        return " blend=" + BLEND_MODE_NAMES[blend]

    def get_flipped_text(flipped):
        if not flipped:
            return ""
        return " flipped"

    def get_origin_text(origin):
        if origin == 0:
            return ""
        return " origin=" + str(origin)

    def remove_faded_out():
        if redux_conf("remove_faded_out_pictures"):
            for id, picture in enumerate(pictures):
                if picture != None and picture["faded_out"]:
                    pictures[id]["opacity"] = 0
                    pictures[id]["faded_out"] = False

    def picture_is_opaque(id):
        if pictures[id]["is_transparent"]:
            return False
        if moving_pictures[id] != None:
            return pictures[id]["opacity"] == 255 and moving_pictures[id]["opacity"] == 255
        return pictures[id]["opacity"] == 255

    def picture_say_text(title = ""):
        return ""
        # text = title + "\n" if title != "" else ""
        # for id, moving_dict in enumerate(pictures):
        #     if moving_dict is not None:
        #         text = text + "Image " + str(id) + ": " + moving_dict["image"] + "\n"
        # return text

    def switch_to_next_backgrounds(no_fades = False):
        global map_backgrounds, transparency_backgrounds, next_map_backgrounds, next_transparency_backgrounds
        global transparency_backgrounds_needs_fade, map_backgrounds_needs_fade, scene_state
        if next_transparency_backgrounds is not None:
            transparency_backgrounds = next_transparency_backgrounds
            next_transparency_backgrounds = None
        if next_map_backgrounds is not None:
            map_backgrounds = next_map_backgrounds
            next_map_backgrounds = None
        if no_fades:
            transparency_backgrounds_needs_fade = False
            map_backgrounds_needs_fade = False

    def resolve_scene(set_state_to = None):
        global scene_state, scene_state_before_resolve, scene_say_text, user_defined_images, cached_moving_pictures, moving_pictures, transparency_backgrounds_needs_fade, map_backgrounds_needs_fade, movement_pauses, previous_map_background_map

        if set_state_to is not None and scene_state == "resolved":
            scene_state = set_state_to
        scene_state_before_resolve = scene_state
        extra_say = "scene_state_before_resolve=" + scene_state_before_resolve + "\n" 

        if scene_state == "resolved":
            return

        if scene_state == "faded_out":
            scene_say_text = "resolve_scene faded out: " +scene_state + "\n" + picture_say_text("Pictures")
            return

        if scene_state == "fade_out":
            renpy.scene()
            renpy.show("black")
            renpy.with_statement(Dissolve(FADE_DURATION))
            scene_state = "faded_out"
            hide_shown_images()
            user_defined_images = {}
            call_user_defined_callbacks()
            scene_say_text = "resolve_scene fade out: " +scene_state + "\n" + picture_say_text("Pictures")
            switch_to_next_backgrounds()
            return

        if scene_state == "fade_in_after_fade_out" or transparency_backgrounds_needs_fade or map_backgrounds_needs_fade:
            renpy.scene()
            if map_backgrounds_needs_fade:
                show_map_background(True, baked_event_image_map = previous_map_background_map)
                previous_map_background_map = None
            renpy.show("black_bg", what=Solid("#000000", xysize=(config.screen_width, config.screen_height)), at_list=[fadeto(0.0, 1.0, FADE_DURATION)], zorder=3002 + MAX_IMAGES)
            renpy.pause(FADE_DURATION)
            renpy.hide("black_bg")
            if map_backgrounds_needs_fade:
                hide_map_background()
            scene_state = "fade_in"
        elif scene_state == "fade_in":
            previous_map_background_map = None
            switch_to_next_backgrounds()

        if transparency_backgrounds_needs_fade or map_backgrounds_needs_fade:
            switch_to_next_backgrounds()

        if scene_state == "fade_in":
            for cached_moving_picture in cached_moving_pictures:
                if cached_moving_picture is not None:
                    moving_pictures[cached_moving_picture[0]] = cached_moving_picture[1]
            cached_moving_pictures = []

        def resolution_callback(resolution):
            try:
                post_resolve_scene(resolution)
            except NameError:
                pass

        try:
            pre_resolve_scene()
        except NameError:
            pass

        before_text = picture_say_text("Before")
        remove_faded_out()
        resolve_scene_render(resolution_callback)
        after_text = picture_say_text("After")
        scene_say_text = extra_say + before_text + scene_say_text + after_text
        movement_pauses = 0

        switch_to_next_backgrounds()

        if transparency_backgrounds_needs_fade or map_backgrounds_needs_fade:
            renpy.pause(FADE_DURATION)
            transparency_backgrounds_needs_fade = False
            map_backgrounds_needs_fade = False

    draw_list = []

    def reset_draw_list():
        global draw_list
        draw_list = []

    def add_to_draw_list(id, image, pos=(0, 0), transforms=[], extra_transforms=True):
        global draw_list
        if image != None:
            draw_list.append((image, id, pos, transforms, extra_transforms))

    def draw_scene(video_to_show):
        global draw_list, images_shown

        def renpy_show_video(video_to_show):
            if len(video_to_show[2]) > 0 and redux_conf("show_black_below_videos", False):
                renpy.show(video_to_show[0]+"bg", what=Solid("#000000", xysize=(config.screen_width, config.screen_height)))
                images_shown.append(video_to_show[0]+"bg")
            renpy.show(video_to_show[0], what=video_to_show[1], at_list=video_to_show[2])
            images_shown.append(video_to_show[0])

        shown_video = False
        if not redux_conf("sfw"):
            for image, id, initial_pos, initial_transforms, extra_transforms in draw_list:
                what = image
                pos = initial_pos
                transforms = initial_transforms[:]
                if len(transforms) == 0 and (pos[0] != 0 or pos[1] != 0):
                    what = Composite((config.screen_width, config.screen_height), pos, image)
                at_list = transforms if not extra_transforms else get_at_list(transforms)
                if video_to_show is None or redux_conf("always_show_video_obscured_pictures") or (video_to_show != None and not shown_video):
                    renpy.show("picture_" + str(id), what=what, at_list=at_list)
                    images_shown.append("picture_" + str(id))
                if video_to_show != None and not shown_video and id >= video_order:
                    renpy_show_video(video_to_show)
                    shown_video = True
            if video_to_show != None and not shown_video:
                renpy_show_video(video_to_show)

    def add_webm_suffix(filename):
        if ".webm" in filename:
            return filename
        return filename + ".webm"

    def get_video_at_list(video_being_played):
        if video_being_played == None:
            return []
        if video_being_played["width"] == config.screen_width and video_being_played["height"] == config.screen_height:
            return []
        scale_x = config.screen_width / video_being_played["width"]
        scale_y = config.screen_height / video_being_played["height"]
        if scale_x == scale_y:
            return [Transform(xsize=config.screen_width, ysize=config.screen_height)]
        if scale_y > scale_x:
            ysize = round(video_being_played["height"] * scale_x)
            return [Transform(xsize=config.screen_width, ysize=ysize, ypos=round((config.screen_height - ysize) / 2))]
        xsize = round(video_being_played["width"] * scale_y)
        return [Transform(xsize=xsize, ysize=config.screen_height, xpos=round((config.screen_width - xsize) / 2))]

    def get_playing_video(playing_these, these_videos):
        video_being_played = None
        video_to_show = None
        say_text = ""
        if (len(playing_these) > 0) and (these_videos[playing_these[len(playing_these) - 1]] == None):
            playing_these = []
        if len(playing_these) > 0:
            video_being_played = these_videos[playing_these[len(playing_these) - 1]]
            video_at_list = get_video_at_list(video_being_played)
            last_displayed = get_video_background(get_last_displayed_image())
            if video_being_played["looping"]:
                if video_being_played["movie"] == None:
                    video_being_played["movie"] = Movie(play="movies/" + add_webm_suffix(video_being_played["filename"]), channel="movie_dp", loop = True)
                    if scene_state != "fade_in" and last_displayed != None:
                        renpy.show("last_displayed_image", what=last_displayed)
                        images_shown.append("last_displayed_image")
                    say_text = say_text + "looping movie " + add_webm_suffix(video_being_played["filename"])
                    looping_name = "video_looping_" + video_being_played["name"]
                    video_to_show = (looping_name, video_being_played["movie"], video_at_list)
            else:
                if video_being_played["movie"] == None:
                    video_being_played["movie"] = Movie(play="movies/" + add_webm_suffix(video_being_played["filename"]), channel="movie_dp", loop = False)
                    say_text = say_text + "playing movie " + add_webm_suffix(video_being_played["filename"])
                    if scene_state != "fade_in" and last_displayed != None:
                        renpy.show("last_displayed_image", what=last_displayed)
                        images_shown.append("last_displayed_image")
                    once_name = "video_once_" + video_being_played["name"]
                    video_to_show = (once_name, video_being_played["movie"], video_at_list)
        return [video_being_played, video_to_show, say_text]

    def get_final_video_image(video):
        if video["final_image"] == None:
            return None
        renpy_image=Image(get_filename(video["final_image"]))
        transforms = [] if video["width"] == config.screen_width and video["height"] == config.screen_height else [sizeat((config.screen_width, config.screen_height))]
        return [renpy_image, transforms]

    def show_video_final_image(final_image):
        if final_image != None:
            renpy.show("final_video_image", what=final_image[0], at_list=final_image[1])

    def resolve_scene_render(resolution_callback):
        global scene_state, transparency_backgrounds, moving_pictures, last_displayed_pictures, last_displayed_pictures_set, playing_videos, last_displayed_map, images_shown, scene_say_text, final_video_image, user_defined_images
        hide_shown_images(leave_videos = True)
        video_result = get_playing_video(playing_videos, videos)
        video_being_played = video_result[0]
        video_to_show = video_result[1]
        say_text = video_result[2]
        obscured_video_result = get_playing_video(obscured_playing_videos, obscured_videos)
        obscured_video_being_played = obscured_video_result[0]
        obscured_video_to_show = obscured_video_result[1]
        obscured_say_text = obscured_video_result[2]
        if obscured_say_text != "":
            say_text = say_text + "OBSCURED: " + obscured_say_text
        duration_frames = 0
        wait = True
        some_opaque = False
        some_not_transparent = False
        picture_filenames = []
        actual_moving_pictures = {}
        highest_visible_moving_picture = 0
        for id, picture in enumerate(moving_pictures):
            actual_moving_pictures[id] = picture
            if picture != None and picture["opacity"] > 0 and pictures[id] != None and not pictures[id]["is_transparent"]:
                highest_visible_moving_picture = id

        for id, picture in enumerate(actual_moving_pictures):
            if picture != None and id < highest_visible_moving_picture:
                actual_moving_pictures[id] = None

        displayed_pictures = []
        for id, picture in enumerate(pictures):
            if picture != None and picture["image"] != "" and (picture["opacity"] > 0 or actual_moving_pictures[id] != None or picture["blink_image"] or picture["breathe_image"]):
                some_opaque = some_opaque or picture_is_opaque(id)
                some_not_transparent = some_not_transparent or not pictures[id]["is_transparent"]
                picture_filenames.append(picture["image"])
                if picture_is_opaque(id):
                    say_text = say_text + "opaque " + str(id) + ": " + picture["image"] + ", opacity " +  str(picture["opacity"]) +" "
                    if actual_moving_pictures[id] != None:
                        say_text = say_text + "(moving opacity " + str(actual_moving_pictures[id]["opacity"]) + ") "
                if actual_moving_pictures[id] != None:
                    if actual_moving_pictures[id]["frames"] > 2:
                        duration_frames = max(duration_frames, actual_moving_pictures[id]["frames"])
                    if actual_moving_pictures[id]["opacity"] != 0 or picture["opacity"] != 0 or picture["blink_image"] or picture["breathe_image"]:
                        displayed_pictures.append((picture, actual_moving_pictures[id], id))
                else:
                    displayed_pictures.append((picture, None, id))

        final_video_image_to_show = None
        if transparency_backgrounds != None and len(displayed_pictures) > 0 and not some_opaque and len(playing_videos) == 0 and len(obscured_playing_videos) == 0:
            if final_video_image != None:
                say_text = say_text + "\nsetting final_video_image_to_show"
                final_video_image_to_show = final_video_image
            else:
                say_text = say_text + "\nadding transparency_backgrounds"
                counter = -len(transparency_backgrounds)
                for background in reversed(transparency_backgrounds):
                    displayed_pictures.insert(0, (day_to_night(background), None, counter))
                    counter = counter + 1
        if some_opaque:
            say_text = say_text + "\nsome_opaque"
            final_video_image = None

        say_text = say_text + "\nnum_pictures=" + str(len(displayed_pictures)) + "\n"
        reset_draw_list()
        for displayed_picture in displayed_pictures:
            if type(displayed_picture[0]) is str:
                displayed_image = Image(get_filename(displayed_picture[0]))
                add_to_draw_list(displayed_picture[2], displayed_image)
                say_text = say_text + get_filename(displayed_picture[0]) + "\n"
            elif displayed_picture[0]["breathe_image"]:
                displayed_image = None
                displayed_pos = None
                displayed_moving_image = Image(get_filename(displayed_picture[0]["image"]))
                not_visible_image = im.Alpha(displayed_moving_image, 0)
                breathe_in_image = get_breathe_in_animation(displayed_moving_image, not_visible_image)
                breathe_out_image = get_breathe_out_animation(displayed_moving_image, not_visible_image)
                # moving_images.append((breathe_in_image, get_breathe_in_animation_transforms(displayed_moving_image, displayed_picture[0])))
                # moving_images.append((breathe_out_image, get_breathe_out_animation_transforms(displayed_moving_image, displayed_picture[0])))
            elif displayed_picture[1] == None:
                displayed_image = get_picture_image(displayed_picture[0])
                displayed_pos = get_displayed_pos(displayed_picture[0])
                add_to_draw_list(displayed_picture[2], displayed_image, displayed_pos, extra_transforms=not is_message_picture(displayed_picture[0]))
                say_text = say_text + str(displayed_picture[0]["id"]) + ":" + get_filename(displayed_picture[0]["image"]) + get_origin_text(displayed_picture[0]["origin"]) + get_size_text(displayed_picture[0]["width"], displayed_picture[0]["height"]) + get_pos_text(displayed_pos) + get_scale_text(displayed_picture[0]["scale"]) + get_opacity_text(displayed_picture[0]["opacity"]) + get_flipped_text(displayed_picture[0]["flipped"]) + get_blend_text(displayed_picture[0]["blend_mode"]) + "\n"
            elif displayed_picture[0]["opacity"] != 0 or displayed_picture[1]["opacity"] != 0 or displayed_picture[0]["blink_image"] or displayed_picture[0]["breathe_image"]:
                if displayed_picture[1]["frames"] <= 2 or (is_message_picture(displayed_picture[0]) and displayed_picture[1]["frames"] <= 5):
                    moved_picture = get_moved_picture(displayed_picture[0], displayed_picture[1])
                    displayed_image = get_picture_image(moved_picture)
                    displayed_pos = get_displayed_pos(moved_picture)
                    add_to_draw_list(displayed_picture[2], displayed_image, displayed_pos, extra_transforms=not is_message_picture(displayed_picture[0]))
                    say_text = say_text + str(displayed_picture[0]["id"]) + ":" + get_filename(displayed_picture[0]["image"]) + get_origin_text(displayed_picture[0]["origin"]) + get_size_text(displayed_picture[0]["width"], displayed_picture[0]["height"]) + get_pos_text(displayed_pos) + get_scale_text(displayed_picture[1]["scale"]) + get_opacity_text(displayed_picture[1]["opacity"]) + get_flipped_text(displayed_picture[0]["flipped"]) + get_blend_text(displayed_picture[1]["blend_mode"]) + "\n"
                else:
                    displayed_moving_image = Image(get_filename(displayed_picture[0]["image"]))
                    if displayed_picture[0]["blink_image"]:
                        not_visible = im.Alpha(displayed_moving_image, 0)
                        displayed_moving_image = get_blink_animation(displayed_moving_image, not_visible)
                    add_to_draw_list(
                        displayed_picture[2], 
                        displayed_moving_image, 
                        pos=get_displayed_pos(displayed_picture[0]),
                        transforms=get_moving_image_transforms(displayed_picture[0], displayed_picture[1]), 
                        extra_transforms=not is_message_picture(displayed_picture[0]),
                    )
                    say_text = say_text + str(displayed_picture[0]["id"]) + ":" + get_filename(displayed_picture[0]["image"]) + get_origin_text(displayed_picture[0]["origin"]) + get_size_text(displayed_picture[0]["width"], displayed_picture[0]["height"]) + get_raw_pos_text(displayed_picture[0]["pos"]) + get_scale_text(displayed_picture[0]["scale"]) + get_pos_text(get_displayed_pos(displayed_picture[0])) + " moving>" + get_moving_image_transforms(displayed_picture[0], displayed_picture[1], as_text=True) + "\n"

        if video_being_played != None:
            hide_map_background(True)
            hide_shown_videos(except_for=video_being_played)
        elif obscured_video_being_played != None:
            hide_map_background(True)
            hide_shown_videos(except_for=obscured_video_being_played)
        else:
            hide_shown_videos(except_for=None)
        if final_video_image_to_show != None:
            say_text = say_text + "draw_list show_video_final_image0\n"
            show_video_final_image(final_video_image_to_show)
        if len(draw_list) > 0:
            say_text = say_text + "draw_list len=" + str(len(draw_list)) + "\n"
            if len(playing_videos) == 0 and len(obscured_playing_videos) == 0 and final_video_image_to_show == None:
                renpy.scene()
                renpy.show("composite_background", what=Solid("#000000", xysize=(config.screen_width, config.screen_height)))
            video_drawn = video_to_show if video_to_show != None else obscured_video_to_show
            draw_scene(video_drawn)
            if video_drawn != None:
                say_text = say_text + "video_drawn=" + str(video_drawn[0]) + "\n"
            else:
                say_text = say_text + "video_drawn=None\n"
                
            last_displayed_pictures = []
            last_displayed_map = current_map
            for displayed_picture in displayed_pictures:
                if displayed_picture[1] == None:
                    last_displayed_pictures.append(copy_of_picture(displayed_picture[0]))
                else:
                    last_displayed_pictures.append(get_moved_picture(displayed_picture[0], displayed_picture[1]))
            if len(last_displayed_pictures) > 0:
                last_displayed_pictures_set = last_displayed_pictures
        elif len(playing_videos) != 0:
            say_text = say_text + "draw_list video_to_show\n"
            draw_scene(video_to_show)
        elif len(obscured_playing_videos) == 0:
            say_text = say_text + "draw_list obscured_playing_videos==0\n"
            if final_video_image_to_show == None:
                show_map_background(True)
                say_text = say_text + "showing map_background\n"
        else:
            say_text = say_text + "draw_list obscured_video_to_show\n"
            draw_scene(obscured_video_to_show)

        if len(user_defined_images) > 0:
            if some_opaque or video_being_played != None:
                user_defined_images = {}
                call_user_defined_callbacks()
            else:
                for id, image_details in user_defined_images.items():
                    transforms = [] if image_details[1] == 0 else [blendpic(image_details[1])]
                    renpy.show("user_defined_image_" + str(id), what=image_details[0], at_list=transforms)
                    images_shown.append("user_defined_image_" + str(id))
                    say_text = say_text + "user_defined_image_" + str(id) + "\n"
                    picture_filenames.append("user_defined_image_" + str(id))

        if scene_state == "fade_in":
            say_text = say_text + "fade_curtain\n"
            renpy.show("fade_curtain", what=Solid("#000000", xysize=(config.screen_width, config.screen_height)), at_list=[get_fade_in_transform()], zorder=3002 + MAX_IMAGES)
            images_shown.append("fade_curtain")

        _window_hide()

        resolution_callback({
            "some_opaque": some_opaque,
            "some_not_transparent": some_not_transparent,
            "picture_filenames": picture_filenames,
            "video_being_played": video_being_played is not None,
        })
        
        if video_being_played != None and not video_being_played["looping"]:
            if not video_being_played["no_pause"]:
                renpy.pause(video_being_played["duration"])
                renpy.scene()
                final_video_image = get_final_video_image(video_being_played)
                show_video_final_image(final_video_image)
                say_text = say_text + "final_video_image " + video_being_played["final_image"] + "\n"
                _window_hide()
                stop_video(video_being_played["id"], but_keep_final_image = True)
                images_shown.append("final_video_image")
        elif len(draw_list) > 0:
            transition_duration = duration_frames / (30 * redux_conf("scene_animation_speed", 1.0))
            if scene_state == "fade_in":
                transition_duration = transition_duration + FADE_DURATION
            if transition_duration > 0.05:
                renpy.pause(transition_duration)
        elif scene_state == "fade_in":
            renpy.pause(FADE_DURATION)

        for id, moving_dict in enumerate(moving_pictures):
            if moving_pictures[id] != None and pictures[id] != None:
                pictures[id] = get_moved_picture(pictures[id], moving_pictures[id])
                moving_pictures[id] = None

        scene_state = "resolved"
        scene_say_text = say_text

    def show_scene(image):
        erase_picture(1)
        show_picture(1, image)
        resolve_scene()

    def fade_in():
        global scene_state
        # scene_state = "resolved" if (scene_state == "resolved" and scene_state_before_resolve == "fade_in") else "fade_in" if scene_state != "fade_out" and scene_state != "fade_in_after_fade_out" else "fade_in_after_fade_out"
        scene_state = "resolved" if scene_state == "resolved" else "fade_in" if scene_state != "fade_out" and scene_state != "fade_in_after_fade_out" else "fade_in_after_fade_out"
        switch_to_next_backgrounds()
        for id, picture in enumerate(pictures):
            if picture != None and picture["faded_out"]:
                picture["faded_out"] = False

    def fade_out():
        global scene_state
        scene_state = "fade_out"
        for id, picture in enumerate(pictures):
            if picture != None:
                picture["faded_out"] = True
        if redux_conf("resolve_after_fade_out"):
            resolve_scene()

    def replace_last(source_string, old_string, new_string):
        reversed_string = source_string[::-1]  # Reverse the string
        replaced_string = reversed_string.replace(old_string[::-1], new_string[::-1], 1)  # Replace the first occurrence in reversed string
        return replaced_string[::-1]  # Reverse back to original

    screen_tint = (0,0,0,255)

    def tint_screen(rgba, duration, wait):
        screen_tint = rgba
        return

    def getPos(image):
        return (0, 0) if type(image) is str else image[1]

    def hide_dialog_background():
        global dialog_background_is_hidden
        dialog_background_is_hidden = True

    def show_dialog_background():
        global dialog_background_is_hidden
        dialog_background_is_hidden = False

    def open_save_screen():
        renpy.call_screen("save")

    def get_event_xy(event):
        if event == "player":
            return [map_x, map_y]
        if event in event_locations:
            return event_locations[event]
        if event in event_xys:
            return event_xys[event]
        for event_name_xy in event_xys:
            if event.startswith(event_name_xy):
                return event_xys[event_name_xy]
        return [-1, -1]

    class MapEvent:
        def __init__(self, event):
            self.event = event
            xy = get_event_xy(event)
            self.x = xy[0]
            self.y = xy[1]
            self.direction = 0

    def get_xy_locations(map_name, x, y):
        map_locations = []
        locations = get_locations()
        if map_name in locations:
            for location_name, location_details in locations[map_name].iteritems():
                location_pos = location_details["bounds"]
                if location_pos[0][0] <= x and location_pos[0][1] <= y and location_pos[1][0] >= x and location_pos[1][1] >= y:
                    map_locations.append(location_name)
                    if location_pos[0][0] == x or location_pos[0][1] == y or location_pos[1][0] == x or location_pos[1][1] == y:
                        if "" not in map_locations:
                            map_locations.append("")
        if len(map_locations) == 0:
            return [""]
        return map_locations

    def get_event_locations(map_name, event):
        locations = get_locations()
        if map_name in locations:
            for location_name, location_details in locations[map_name].iteritems():
                if "location_events" in location_details:
                    if event in location_details["location_events"]:
                        return [location_name]
        e_xy = get_event_xy(event)
        return get_xy_locations(map_name, e_xy[0], e_xy[1])

    def get_xy_location(map_name, x, y):
        return get_xy_locations(map_name, x, y)[0]

    def get_player_location():
        return get_xy_location(current_map, map_x, map_y)

    def get_called_from_move_direction(called_from):
        move_direction = "h" if map_direction == 4 or map_direction == 6 else "v"
        movement_direction = get_movement_direction()
        for event, direction in movement_direction.iteritems():
            if called_from.startswith(event):
                move_direction = direction
        return move_direction

    def move_player_to_event(event):
        global map_x, map_y, map_direction
        e_xy = get_event_xy(event)
        diff_x = abs(e_xy[0] - map_x)
        diff_y = abs(e_xy[1] - map_y)
        if diff_y > diff_x:
            if e_xy[1] > map_y:
                map_y = e_xy[1] - 1
                map_direction = 2
            else:
                map_y = e_xy[1] + 1
                map_direction = 8
        else:
            if e_xy[0] > map_x:
                map_x = e_xy[0] - 1
                map_direction = 6
            else:
                map_x = e_xy[0] + 1
                map_direction = 4

    from renpy.uguu import GL_FUNC_REVERSE_SUBTRACT, GL_ONE, GL_ZERO  # type: ignore

    def add_sub_blend_mode():
        renpy.config.gl_blend_func["sub"] = (GL_FUNC_REVERSE_SUBTRACT, GL_ONE, GL_ONE, GL_FUNC_REVERSE_SUBTRACT, GL_ZERO, GL_ONE)

    def get_starting_xy(called_from, character):
        if character == "player":
            e_xy = get_event_xy(called_from)
            player_location = get_player_location()
            e_locs = get_event_locations(current_map, called_from)
            event_locations_not_at_player = list(filter(lambda x: x != player_location and x != "", e_locs))
            if len(event_locations_not_at_player) > 0 and redux_conf("move_player_to_edge_of_location"):
                event_location = event_locations_not_at_player[0]
                # player is outside location so work out closest point outside location to event
                locations = get_locations()
                location_bounds = locations[current_map][event_location]["bounds"]
                location_min_x = location_bounds[0][0]
                location_min_y = location_bounds[0][1]
                location_max_x = location_bounds[1][0]
                location_max_y = location_bounds[1][1]
                diff_x1 = abs(e_xy[0] - location_min_x)
                diff_x2 = abs(location_max_x - e_xy[1])
                if diff_x1 < diff_x2:
                    new_x = location_min_x - 1
                else:
                    new_x = location_max_x + 1
                diff_y1 = abs(e_xy[1] - location_min_y)
                diff_y2 = abs(location_max_y - e_xy[1])
                if diff_y1 < diff_y2:
                    new_y = location_min_y - 1
                else:
                    new_y = location_max_y + 1
                return (new_x, new_y)
            return (map_x, map_y)
        return get_event_xy(character)

    def get_moved_xy(xy, e_xy, move_direction, moves):
        x = xy[0]
        y = xy[1]
        event_x = e_xy[0]
        event_y = e_xy[1]
        xplus = 0
        yplus = 0
        if move_direction == "h":
            if x < event_x:
                xplus = 1
            elif x > event_x:
                xplus = -1
        else:
            if y < event_y:
                yplus = 1
            elif y > event_y:
                yplus = -1
        if redux_conf("move_player_to_edge_of_location"):
            x = event_x
            y = event_y
        for move in moves:
            if move == "FORWARD":
                x = x + xplus
                y = y + yplus
            elif move == "BACKWARD":
                x = x + xplus
                y = y + yplus
            elif move == "L":
                x = x - 1
            elif move == "R":
                x = x + 1
            elif move == "U":
                y = y - 1
            elif move == "D":
                y = y + 1
        return (x, y)

    def perform_moves(character, xy):
        global map_x, map_y, event_locations
        if character == "player":
            map_x = xy[0]
            map_y = xy[1]
        else:
            event_locations[character] = xy

    def parallel_suffix(interval, waits):
        if interval > 0:
            return "_" + str(interval)
        return "_".join(map(str, waits))

    def hide_sound_callback(channel):
        def hide_sound():
            renpy.music.stop(channel=channel)
        return hide_sound

    def hide_image_n(n):
        def hide_image_value():
            global user_defined_images
            if n in user_defined_images:
                del user_defined_images[n]
            renpy.hide("user_defined_image_" + str(n))
        return hide_image_value

    show_flash_image = True
    accumulator = 0
    last_time = 0

    def get_parallel_anim_flash_image(st, at):
        global show_flash_image, accumulator, last_time
        if show_flash_image:
            show_flash_image = False
            last_time = st
            return (Solid(parallel_anim_flash_screen), 0.03)
        else:
            accumulator = accumulator + (st - last_time)
            last_time = st
            if accumulator > parallel_anim_flash_screen_interval:
                accumulator = 0
                show_flash_image = True
            return (Solid("#00000000"), 0.03)

    def get_parallel_anim_tint_image(st, at):
        return (Solid(parallel_anim_tint_screen), None)

define user_defined_callback_functions = {
    "hide_sound_callback": hide_sound_callback,
    "hide_image_n": hide_image_n,
}

default pictures = [None for _ in range(MAX_IMAGES)]
default moving_pictures = [None for _ in range(MAX_IMAGES)]
default cached_moving_pictures = []
default videos = [None for _ in range(MAX_VIDEOS)]
default obscured_videos = [None for _ in range(MAX_VIDEOS)]
default transparency_backgrounds = None
default map_backgrounds = None
default next_transparency_backgrounds = None
default transparency_backgrounds_needs_fade = False
default next_map_backgrounds = None
default raw_transparency_backgrounds = None
default raw_map_backgrounds = None
default map_backgrounds_needs_fade = False
default recalculate_backgrounds = False
default scene_state = "resolved"
default playing_videos = []
default obscured_playing_videos = []
default last_displayed_pictures = None
default last_displayed_pictures_set = []
default last_displayed_map = None
default images_shown = []
default event_locations = {}
default final_video_image = None
default movement_pauses = 0
define MAX_PAUSE = 0.8
define FADE_DURATION = 0.4

label PauseForMoves(moves):
    $ pause_length = 0.2 + (len(moves) * 0.02)
    $ movement_pauses += pause_length
    if movement_pauses < MAX_PAUSE:
        pause pause_length
    return

label PauseForMovementBase(called_from, character, moves):
    if current_map == map_of_called_event and originating_trigger == "event":
        $ start_at_xy = get_starting_xy(originating_event, character)
        $ e_xy = get_event_xy(originating_event)
        $ move_direction = get_called_from_move_direction(originating_event)
        $ new_xy = get_moved_xy(start_at_xy, e_xy, move_direction, moves)
        $ perform_moves(character, new_xy)
    call PauseForMoves(moves) from _call_PauseForMovementBase_PauseForMoves
    return

label SetEventLocation(called_from, event, x, y):
    $ event_locations[event] = (x, y)
    if renpy.has_label("SetEventLocationCustom"):
        call SetEventLocationCustom(called_from, event, x, y) from _call_SetEventLocation_SetEventLocationCustom
    return

label PauseForBalloon(called_from):
    pause 0.2
    return

label Assert(condition, message):
    if not condition:
        "ERROR: [message]"
        pause
    return

label ParallelAnimPlaySound(picture, sound, volume, channel, interval=0, waits=[]):
    $ filename = "audio/" + sound + parallel_suffix(interval, waits) + ".ogg"
    if renpy.loadable(filename):
        $ renpy.music.play(filename, channel=channel, loop=True, relative_volume=volume)
        $ add_hide_callback(picture, "hide_sound_callback", channel)
    else:
        if developer_mode():
            "Missing ParallelPlaySound: [filename]"
    return

label ParallelAnimPlaySE(picture, sound, volume, interval=0, waits=[]):
    call ParallelAnimPlaySound(picture, sound, volume, "sound", interval, waits) from _call_ParallelPlaySound_ParallelPlaySE
    return

label ParallelAnimPlayBGS(picture, sound, volume, interval=0, waits=[]):
    call ParallelAnimPlaySound(picture, sound, volume, "bgs", interval, waits) from _call_ParallelPlaySound_ParallelPlayBGS
    return

label ParallelAnimPlayBGM(picture, sound, volume, interval=0, waits=[]):
    call ParallelAnimPlaySound(picture, sound, volume, "music", interval, waits) from _call_ParallelPlaySound_ParallelPlayBGM
    return

default parallel_anim_flash_screen = '#00000000'
default parallel_anim_flash_screen_interval = 1.0
default parallel_anim_tint_screen = '#00000000' 
image parallel_anim_flash_image = DynamicDisplayable(get_parallel_anim_flash_image)
image parallel_anim_tint_image = DynamicDisplayable(get_parallel_anim_tint_image)

label ParallelAnimFlashScreen(picture, rgba, interval=0, waits=[]):
    if interval == 0:
        "ParallelAnimFlashScreen not implemented for waits"
    else:
        $ parallel_anim_flash_screen = '{:02x}{:02x}{:02x}{:02x}'.format(rgba[0], rgba[1], rgba[2], rgba[3])
        $ parallel_anim_flash_screen_interval = interval
        $ show_image(101, "parallel_anim_flash_image")
        $ add_hide_callback(picture, "hide_image_n", 101)
    return

label ParallelAnimTintScreen(picture, rgba, interval=0, waits=[]):
    if rgba[0] < 0 or rgba[1] < 0 or rgba[2] < 0:
        $ add_sub_blend_mode()
        $ blend_mode = 4
    else:
        $ blend_mode = 1
    $ parallel_anim_tint_screen = '{:02x}{:02x}{:02x}{:02x}'.format(abs(rgba[0]), abs(rgba[1]), abs(rgba[2]), abs(rgba[3]))
    $ show_image(100, "parallel_anim_tint_image", blend_mode=blend_mode)
    $ add_hide_callback(picture, "hide_image_n", 100)
    return

default dex = 0

label SO(n):
    $ dex = get_o(n)
    return

label PlaySound(channel, filename, volume, no_loop):
    if renpy.music.get_playing() != filename:
        $ renpy.music.play(filename, channel=channel, relative_volume=volume, loop=not no_loop)
    return
