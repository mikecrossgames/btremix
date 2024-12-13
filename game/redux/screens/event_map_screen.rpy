init python:
    from math import sqrt

    def do_nothing():
        pass

    def event_xysize(event, xysize):
        if is_person(event["event"], event["title"]):
            if get_person_image(event["event"], event["title"]) in large_face_images:
                return large_face_images[get_person_image(event["event"], event["title"])]
        if not is_unknown(event):
            return xysize
        return (round(xysize[0] / 2), round(xysize[1] / 2))

    def hover_title_for_location(location):
        locations = get_locations()
        def hover_title(e):
            if is_unknown(e):
                return hover_title_unknown + " " + e["title"]
            # return e["title"] + " " + str(e["xy"][0]) + "," + str(e["xy"][1])
            return get_event_title(e, location, locations)
        return hover_title

    def adjusted_square_size(square_size, bounds):
        bounds_h = bounds[1] - bounds[0]
        bounds_v = bounds[3] - bounds[2]
        if bounds_h == 0 or bounds_v == 0:
            return default_min_square_size
        while square_size / bounds_h > 0.25 or square_size / bounds_v > 0.25:
            square_size /= 2
        return square_size

    def get_bounds(coordinates, square_size, extra_coordinates, initial_bounds = None):
        if len(coordinates) == 0 and len(extra_coordinates) == 0:
            return (0, 0, 1, 1)
        min_x = float('inf') if initial_bounds is None else initial_bounds[0][0]
        max_x = -float('inf') if initial_bounds is None else initial_bounds[1][0]
        min_y = float('inf') if initial_bounds is None else initial_bounds[0][1]
        max_y = -float('inf') if initial_bounds is None else initial_bounds[1][1]
        for coord in coordinates:
            if coord[0] < min_x:
                min_x = coord[0]
            if coord[0] > max_x:
                max_x = coord[0]
            if coord[1] < min_y:
                min_y = coord[1]
            if coord[1] > max_y:
                max_y = coord[1]

        min_x -= (square_size / 2)
        max_x += (square_size / 2)
        min_y -= (square_size / 2)
        max_y += (square_size / 2)

        for coord in extra_coordinates:
            if coord[0] < min_x:
                min_x = coord[0]
                max_x += coord[0] - min_x
            if coord[0] > max_x:
                max_x = coord[0]
                min_x -= coord[0] - max_x
            if coord[1] < min_y:
                min_y = coord[1]
                max_y += coord[1] - min_y
            if coord[1] > max_y:
                max_y = coord[1]
                min_y -= coord[1] - max_y

        return (min_x, max_x, min_y, max_y)

    def largest_square(coordinates):
        if len(coordinates) < 2:
            return 1
        min_distance = float('inf')

        # Function to calculate the Euclidean distance between two points
        def distance(a, b):
            return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

        # Compare each coordinate with all other coordinates to find the minimum distance
        for i in range(len(coordinates)):
            for j in range(i + 1, len(coordinates)):
                dist = distance(coordinates[i], coordinates[j])
                if dist < min_distance:
                    min_distance = dist

        # Return the side length of the largest non-overlapping square
        # Half the minimum distance gives the radius of the largest square, so we multiply it by 2 to get the side length
        return min_distance / sqrt(2)

    def event_to_event_object(event):
        return {
            "priority": event[1][0],
            "label": event[1][1],
            "key": event[1][2],
            "event": event[0][0],
            "title": event[0][1],
            "xy": get_event_xy(event[0][0]),
            "zorder": get_event_zorder(event[0][0]),
        }

    def sortKey(area_size):
        def sortKeyArea(event):
            # priority * 25 * 25
            # quad = 25x25
            # inter = 100x100 / 10000
            area_square = 100 / area_size
            sort_score = 2 - event["priority"] * area_square * area_square
            x = event["xy"][0]
            y = event["xy"][1]
            x4 = round(x / area_size)
            y4 = round(y / area_size)
            sort_score += (y4 * area_square) + x4
            sort_score += ((x * 100) + y) / 10000
            return sort_score
        return sortKeyArea

    def to_event_objects(events, area_size=4):
        unsorted_list = list(map(event_to_event_object, events))        
        return sorted(unsorted_list, key=sortKey(area_size))

    def clear_drag_events():
        global map_event_xyposition
        map_event_xyposition = {}

    screen_padh = default_screen_padh
    screen_padtop = default_screen_padtop
    screen_padbottom = default_screen_padbottom
    width = config.screen_width - 2 * screen_padh
    height = config.screen_height - screen_padtop - screen_padbottom
    max_face_size = (default_max_face_size, default_max_face_size)

    def get_square_xy(bounds, square_size):
        if bounds[0] == bounds[1] or bounds[2] == bounds[3]:
            return (1, 1)
        square_x = round(square_size * (width / (bounds[1] - bounds[0])))
        square_y = round(square_size * (height / (bounds[3] - bounds[2])))
        return (square_x, square_y)

    def adjust_pos_for_event(event, xy):
        if is_person(event["event"], event["title"]):
            if get_person_image(event["event"], event["title"]) in large_face_images:
                image_dims = large_face_images[get_person_image(event["event"], event["title"])]
                return (xy[0] + image_dims[0], xy[1] + round(image_dims[1] / 2))
        return xy

    def event_box_xy(event, bounds, square_size):
        if event["event"] in map_event_xyposition:
            return adjust_pos_for_event(event, map_event_xyposition[event["event"]])
        if event["event"] in map_event_xy_fixed:
            return adjust_pos_for_event(event, map_event_xy_fixed[event["event"]])
        if bounds[0] == bounds[1] or bounds[2] == bounds[3]:
            return (0, 0)
        left_x = event["xy"][0]
        top_y = event["xy"][1]
        scalex = (left_x - bounds[0]) / (bounds[1] - bounds[0])
        scaley = (top_y - bounds[2]) / (bounds[3] - bounds[2])
        x = screen_padh + round(width * scalex)
        y = screen_padtop + round(height * scaley)
        return adjust_pos_for_event(event, adjust_event_xy(event, (x, y)))

    def get_event_screen_bg(event):
        if (get_person_image(event["event"], event["title"]) is not None and not drag_mode) or is_unknown(event):
            return None
        if is_faded_event(event["event"]):
            return Solid("#00000060")
        return Solid("#000000C0")

    def get_event_screen_hover_bg(event):
        if (get_person_image(event["event"], event["title"]) is not None and not drag_mode) or is_unknown(event):
            return None
        return Solid("#000000F0")

    def get_event_screen_image(event, xysize, enabled):
        if is_person(event["event"], event["title"]):
            person_image = get_person_image(event["event"], event["title"])
            if person_image == "":
                return []
            large_face_image = person_image in large_face_images
            if not large_face_image:
                face_dims = (144, 144)
                face_size = (xysize[0], xysize[0]) if xysize[0] < xysize[1] else (xysize[1], xysize[1])
                if (face_size[0] > max_face_size[0] or face_size[1] > max_face_size[1]):
                    scale_x = max_face_size[0] / face_size[0]
                    scale_y = max_face_size[1] / face_size[1]
                    scale = scale_x if scale_x < scale_y else scale_y
                    face_size = (round(face_size[0] * scale), round(face_size[1] * scale))
                filename = get_filename(person_image)
                event_face = Image(filename)
                tint = im.matrix.brightness(0.08) if "silho" in filename else im.matrix.tint(1.1, 1.1, 1.1)
                event_face_tint = im.MatrixColor(event_face, tint)
                if is_faded_event(event["event"]):
                    image2 = im.Alpha(event_face, 0.675)
                    image1 = im.Alpha(event_face_tint, 0.675)
                else:
                    image2 = event_face_tint
                    image1 = event_face
                if face_size[0] > 144:
                    face1 = Transform(image1, xysize=face_dims, pos=(round((face_size[0] - face_dims[0]) / 2), round((face_size[1] - face_dims[0]) / 2)))
                    face2 = Transform(image2, xysize=face_dims, pos=(round((face_size[0] - face_dims[1]) / 2), round((face_size[1] - face_dims[1]) / 2)))
                else:
                    face1 = Transform(image1, xysize=face_size)
                    face2 = Transform(image2, xysize=face_size)
                event_transform = get_map_event_transform(event, person_image, enabled)
                if event_transform is not None:
                    return (Transform(face1, xalign = 0.5, yalign = 0.5), Transform(face2, xalign = 0.5, yalign = 0.5), event_transform)
                extra_face = get_extra_face(event)
                if extra_face is not None:
                    map_face = extra_face[0]
                    if face_size[0] > 144:
                        map_image = Transform(map_face, xysize=face_dims, pos=(round((face_size[0] - face_dims[0]) / 2), round((face_size[1] - face_dims[0]) / 2)))
                    else:
                        map_image = Transform(map_face, xysize=face_size)
                    return (Transform(face1, xalign = 0.5, yalign = 0.5), Transform(face2, xalign = 0.5, yalign = 0.5), None, map_image, extra_face[1])
                return (Transform(face1, xalign = 0.5, yalign = 0.5), Transform(face2, xalign = 0.5, yalign = 0.5))
            face_dims_raw = large_face_images[person_image]
            actual_face_dims = face_sizes[person_image]
            face_scale = face_dims_raw[0] / actual_face_dims[0] if face_dims_raw[0] > face_dims_raw[1] else face_dims_raw[0] / actual_face_dims[0]
            scaled_dim = 20 * face_scale
            face_dims = (large_face_images[person_image][0] + round(scaled_dim), large_face_images[person_image][1] + round(scaled_dim))
            face_size = (xysize[0], xysize[0]) if xysize[0] < xysize[1] else (xysize[1], xysize[1])
            filename = get_filename(person_image)
            filename_outline = get_filename(person_image + "-outline")
            event_face = Image(filename)
            event_face_outline = Image(filename_outline)
            if is_faded_event(event["event"]):
                event_face = im.Alpha(event_face, 0.675)
                event_face_outline = im.Alpha(event_face_outline, 0.675 * 0.675)
            else:
                event_face_outline = im.Alpha(event_face_outline, 0.675)
            pos = (round((face_size[0] - face_dims[0] + scaled_dim) / 2), round((face_size[1] - face_dims[0] + scaled_dim) / 2))
            pos2 = (round((face_size[0] - face_dims[0]) / 2), round((face_size[1] - face_dims[0]) / 2))
            face = Transform(event_face, xysize=face_dims_raw, pos=pos)
            event_face_scaled = Transform(event_face, xysize=face_dims_raw)
            event_face_outline_scaled = Transform(event_face_outline, xysize=face_dims)
            original_pos = (math.floor(scaled_dim / 2), math.floor(scaled_dim / 2))
            if person_image in face_image_hack_offsets:
                original_pos = (original_pos[0] + face_image_hack_offsets[person_image][0], original_pos[1] + face_image_hack_offsets[person_image][1])
            face_outline_composite = Composite(face_dims, original_pos, event_face_scaled, (0, 0), event_face_outline_scaled)
            face_outline = Transform(face_outline_composite, pos=pos2)
            event_transform = get_map_event_transform(event, person_image, enabled)
            if event_transform is not None:
                return (Transform(face, xalign = 0.5, yalign = 0.5), Transform(face_outline, xalign = 0.5, yalign = 0.5), event_transform)
            extra_face = get_extra_face(event)
            if extra_face is not None:
                map_face = extra_face[0]
                map_image = Transform(map_face, xysize=face_dims, pos=(round((face_size[0] - face_dims[0] + scaled_dim) / 2), round((face_size[1] - face_dims[0] + scaled_dim) / 2)))
                return (Transform(face, xalign = 0.5, yalign = 0.5), Transform(face_outline, xalign = 0.5, yalign = 0.5), None, map_image, extra_face[1])
            return (Transform(face, xalign = 0.5, yalign = 0.5), Transform(face_outline, xalign = 0.5, yalign = 0.5))
        if is_unknown(event):
            return (Solid("#00000060", xysize=xysize), Solid("#00000060", xysize=xysize))
        if event["event"] in event_images:
            screen_ratio = config.screen_width / config.screen_height
            xy_ratio = xysize[0] / xysize[1]
            if xy_ratio > screen_ratio:
                y_size = config.screen_width / (xysize[0] / xysize[1])
                y_diff = round(config.screen_height - y_size)
                crop = (0, y_diff, config.screen_width, config.screen_height - y_diff)
            else:
                x_size = config.screen_height / (xysize[1] / xysize[0])
                x_diff = round(config.screen_width - x_size)
                crop = (x_diff / 2, 0, config.screen_width - x_diff, config.screen_height)
            filename = get_filename(event_images[event["event"]])
            image2 = im.Crop(Image(filename), crop)
            tint = im.matrix.brightness(0.08) if "silho" in filename else im.matrix.tint(0.8, 0.8, 0.8)
            image1 = im.MatrixColor(image2, tint)
            return (Transform(image1, xysize=xysize), Transform(image2, xysize=xysize))
        return (Solid("#808080", xysize=xysize), Solid("#AAAAAA", xysize=xysize))

    def event_dragged(event):
        def dragged_function(drags, drop):
            drag_debug_text = "drags (" + str(len(drags)) + ") drop (" + str(drop) + ") "
            if is_person(event["event"], event["title"]) and get_person_image(event["event"], event["title"]) in large_face_images:
                lfi = large_face_images[get_person_image(event["event"], event["title"])]
                map_event_xyposition[event["event"]] = (drags[0].x, drags[0].y)
            else:
                map_event_xyposition[event["event"]] = (drags[0].x + 48, drags[0].y + 24)
            with open(renpy.config.gamedir + "/events-xy.md","w") as egg:
                for map_event in map_event_xyposition:
                    if map_event.startswith(current_map):
                        egg.write("    \"" + map_event + "\": (" + str(map_event_xyposition[map_event][0]) + "+adjust_x," + str(map_event_xyposition[map_event][1]) + "+adjust_y),\n")
            egg.closed

            return None
        return dragged_function

    def sorted_by_zorder(event_objects):
        return sorted(event_objects, key=lambda event_object: event_object["zorder"])

    def get_hotspot_image(event_images):
        return event_images[1] if renpy.android or renpy.ios else event_images[0]

    def get_hotspot_transforms(transforms):
        if not renpy.android and not renpy.ios:
            return transforms
        if transforms is None:
            return [fadeinout]
        return [fadeinout] + transforms

transform fadeinout():
    alpha 1
    linear 0.4 alpha 0.8
    linear 0.4 alpha 1
    repeat

screen event_map_screen(events, new_quests):
    default viewed_quests = False

    python:
        initial_bounds = None
        player_location = get_player_location()
        locations = get_locations()
        if current_map in locations:
            if player_location in locations[current_map]:
                if "fit_to_map_bounds" in locations[current_map][player_location] and locations[current_map][player_location]["fit_to_map_bounds"]:
                    initial_bounds = locations[current_map][player_location]["bounds"]

    tag eventscreen
    modal True
    if len(events) == 0:
        text "No events available: " + map_display_name(current_map) + " " + str(map_x) + "," + str(map_y):
            xalign 0.5
            ypos 0.5
    else:
        use event_buttons(events, initial_bounds)
        use event_map_overlay
        use ui_icons(new_quests and not viewed_quests)
        if show_timer is not None:
            use timer_frame(show_timer, [Return("TimeoutEvent")], on_screen = timer_onscreen())

default hover_event = None
default hovered_name_event = None
default drag_mode = False
default show_all_events = False

default map_click_xy = (0, 0)

screen event_buttons(events, initial_bounds):
    python:
        event_objects = to_event_objects(events)
        non_face_event_objects = list(filter(lambda event_object: get_person_image(event_object["event"], event_object["title"]) is None and not is_unknown(event_object), event_objects))
        face_event_objects = list(filter(lambda event_object: get_person_image(event_object["event"], event_object["title"]) is not None or is_unknown(event_object), event_objects))
        coordinates = list(map(lambda event_object: event_object["xy"], non_face_event_objects))
        face_coordinates = list(map(lambda event_object: event_object["xy"], face_event_objects))
        coordinates = adjusted_coordinates_for_map(coordinates)
        square_size = largest_square(coordinates) if len(coordinates) > 0 else largest_square(face_coordinates)
        bounds = get_bounds(coordinates, square_size, face_coordinates, initial_bounds) if len(coordinates) > 0 else get_bounds(face_coordinates, square_size, [], initial_bounds)
        xysize = get_square_xy(bounds, square_size)
        if xysize[0] == 0 or xysize[1] == 0:
            xysize = (1, 1)

        max_aspect_ratio_x = (config.screen_height + (config.screen_width - config.screen_height) / 2) / config.screen_height if config.screen_width > config.screen_height else config.screen_width + (config.screen_height - config.screen_width) / 2 / config.screen_width
        max_aspect_ratio_y = 1

        if xysize[0] / xysize[1] > max_aspect_ratio_x or xysize[1] / xysize[0] > max_aspect_ratio_y:
            if xysize[0] > xysize[1]:
                xysize = (round(xysize[1] * max_aspect_ratio_x), xysize[1])
            else:
                xysize = (xysize[0], round(xysize[0] * max_aspect_ratio_y))         
        scale = 1
        min_square_size = default_min_square_size if current_map not in min_square_sizes else min_square_sizes[current_map]
        max_square_size = 32 if drag_mode else default_max_square_size
        if xysize[0] > max_square_size:
            scale = max_square_size / xysize[0]
            xysize = (max_square_size, round(xysize[1] * scale))
        if xysize[1] > max_square_size:
            scale2 = max_square_size / xysize[1]
            xysize = (round(xysize[0] * scale2), max_square_size)
            scale *= scale2
        if xysize[0] < min_square_size:
            scale = min_square_size / xysize[0]
            xysize = (min_square_size, round(xysize[1] * scale))
        if xysize[1] < min_square_size:
            scale2 = min_square_size / xysize[1]
            xysize = (round(xysize[0] * scale2), min_square_size)
            scale *= scale2
        if scale != 1:
            square_size *= scale
        square_size = adjusted_square_size(square_size, bounds)

        player_location = get_player_location()
        map_screen_hover_title = hover_title_for_location(player_location)
        bounds_text = ",".join(map(lambda b: "{:.2f}".format(b), bounds))
        map_text = map_display_name(current_map)
        time_text = get_time_text(map_text)
        drag_text = "Drag mode" if not drag_mode else "Cancel drag"
        show_all_text = "Show active only" if show_all_events else "Show all"

    fixed:
        ypos hover_title_ypos
        vbox:
            xalign 0.975
            text map_text:
                color help_button_text_color
                size location_text_size
                outlines [ (absolute(1), help_text_outline_color, absolute(0), absolute(0)) ]
                font "light.ttf"
                xalign 1.0
            text time_text:
                color help_button_text_color
                size location_small_size
                outlines [ (absolute(1), help_text_outline_color, absolute(0), absolute(0)) ]
                font "light.ttf"
                xalign 1.0
            if developer_mode():
                textbutton drag_text:
                    action ToggleVariable("drag_mode")
                    xpadding 5
                    background Solid("#000")
                textbutton show_all_text:
                    action [ToggleVariable("show_all_events"), Return("")]
                    xpadding 5
                    background Solid("#000")
                textbutton "Clear drag":
                    action [Function(clear_drag_events), Return("")]
                    xpadding 5
                    background Solid("#000")
                text "bounds [bounds_text]":
                    color help_button_text_color
                    size location_small_size
                    outlines [ (absolute(1), help_text_outline_color, absolute(0), absolute(0)) ]
                    font "light.ttf"
                if hovered_name_event is not None and "event" not in hovered_name_event:
                    text hovered_name_event[0]["event"]:
                        color help_button_text_color
                        size location_small_size
                        outlines [ (absolute(1), help_text_outline_color, absolute(0), absolute(0)) ]
                        font "light.ttf"
                    text str(hovered_name_event[0]["xy"][0]) + "," + str(hovered_name_event[0]["xy"][1]) + " @ " + str(hovered_name_event[1]) + ": " + str(hovered_name_event[2]):
                        color help_button_text_color
                        size location_small_size
                        outlines [ (absolute(1), help_text_outline_color, absolute(0), absolute(0)) ]
                        font "light.ttf"
            if developer_mode() and False:
                text (str(player_location) + " " + str(map_x) + "," + str(map_y)).strip():
                    color help_button_text_color
                    size location_text_size
                    outlines [ (absolute(1), help_text_outline_color, absolute(0), absolute(0)) ]
                    font "light.ttf"

    for event in sorted_by_zorder(face_event_objects):
        use event_hotspot(
            map_screen_hover_title,
            event,
            event_xysize(event, xysize),
            event_box_xy(event, bounds, square_size),
            event_is_enabled(event),
        )

    for index in range(len(non_face_event_objects)):
        use event_hotspot(
            map_screen_hover_title,
            non_face_event_objects[index],
            xysize,
            event_box_xy(
                non_face_event_objects[index], 
                bounds,
                square_size,
            ),
            event_is_enabled(non_face_event_objects[index]),
        )

    use hover_text()

screen event_hotspot(map_screen_hover_title, event, xysize, xypos, enabled=True):
    if drag_mode:
        use event_hotspot_drag(event, xysize, xypos, enabled)
    elif use_square_hotspots(event):
        use event_hotspot_square(map_screen_hover_title, event, xysize, xypos, enabled)
    else:
        use event_hotspot_name(map_screen_hover_title, event, xysize, xypos, enabled)

screen event_hotspot_drag(event, xysize, xypos, enabled=True):
    python:
        ysize = xysize[1] # if xysize[1] < 100 or xypos[1] < 550 else 100
        pos = xypos # adjust_pos_for_event(event, xypos)
    drag:
        as drag_event
        draggable True
        dragged event_dragged(event)
        xpos pos[0] - round(xysize[0])
        ypos pos[1] - round(ysize / 2)
        frame:
            xsize xysize[0]
            ysize ysize
            background get_event_screen_bg(event)

screen event_hotspot_square(map_screen_hover_title, event, xysize, xypos, enabled=True):
    python:
        event_images = get_event_screen_image(event, xysize, enabled)
        display_title = map_screen_hover_title(event)
        transforms = None if len(event_images) < 3 else event_images[2]
    if len(event_images) > 0:
        frame:
            xsize xysize[0] + (event_hotspot_padding * 2)
            ysize xysize[1] + (event_hotspot_padding * 2)
            xpos xypos[0] - event_hotspot_padding - round(xysize[0])
            ypos xypos[1] - event_hotspot_padding - round(xysize[1] / 2)
            background get_event_screen_bg(event)
            fixed:
                if len(event_images) > 4:
                    add event_images[3] at event_images[4]:
                        xysize xysize
                        xpos -event_hotspot_padding
                        ypos -event_hotspot_padding
            fixed:
                if not enabled or renpy.android or renpy.ios:
                    imagebutton:
                        action NullAction()
                        xysize xysize
                        xpos -event_hotspot_padding
                        ypos -event_hotspot_padding
                        idle event_images[0] at transforms
                        padding (0, 0)
                if enabled:
                    imagebutton:
                        action [SetVariable("hover_text", None), SetVariable("map_click_xy", xypos), Return(event["event"])]
                        xysize xysize
                        xpos -event_hotspot_padding
                        ypos -event_hotspot_padding
                        idle get_hotspot_image(event_images) at get_hotspot_transforms(transforms)
                        hover event_images[1]
                        hovered [SetVariable("hover_text", display_title), SetVariable("hovered_name_event", (event, xypos, xysize))]
                        unhovered [SetVariable("hover_text", None),SetVariable("hovered_name_event", None)]
                        padding (0, 0)
                        focus_mask True
                        mouse "action"

screen event_hotspot_name(map_screen_hover_title, event, xysize, xypos, enabled=True):
    python:
        display_title = map_screen_hover_title(event)
        color = gui.idle_color
        if is_faded_event(event["event"]):
            color = "#A8A8A860"
    frame:
        xalign xypos[0] / config.screen_width
        ypos xypos[1] - 60
        ysize 120
        background None
        if enabled:
            textbutton display_title action [SetVariable("map_click_xy", xypos), Return(event["event"])]:
                background get_event_screen_bg(event)
                hover_background get_event_screen_hover_bg(event)
                text_color color
                text_hover_color gui.hover_color
                text_outlines []
                xpadding 10
                yalign 0.5
                hovered SetVariable("hovered_name_event", (event, xypos, xysize))
                unhovered SetVariable("hovered_name_event", None)
        else:
            textbutton display_title action Function(do_nothing):
                text_color "#606060"
                text_hover_color "#606060"
                background "#30303050"
                xpadding 10
                yalign 0.5
                hovered SetVariable("hovered_name_event", (event, xypos, xysize))
                unhovered SetVariable("hovered_name_event", None)

