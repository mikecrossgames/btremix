init python:
    def enact_timing(timing, j, i):
        if timing["flash_duration"] > 0:
            duration = timing["flash_duration"] / 120
            rgb_hex = '{:02x}{:02x}{:02x}{:02x}'.format(timing["flash_color"][0], timing["flash_color"][1], timing["flash_color"][2], timing["flash_color"][3])
            fadeflash = fadetoeasein(1.0, 0.0, duration)
            renpy.show("timing_flash" + str(j) + str(i), what=Solid(rgb_hex, xysize=(config.screen_width, config.screen_height)), at_list=[fadeflash], zorder=4000)
        if "se" in timing and timing["se"]["name"] != "":
            renpy.music.play("audio/" + timing["se"]["name"] + ".ogg", relative_volume=timing["se"]["volume"] / 100, channel="sound", loop=False)

    def end_timing(timing, j, i):
        if timing["flash_duration"] > 0:
            renpy.hide("timing_flash" + str(j) + str(i))

    def show_animation(id, x = round(config.screen_width / 2), y = round(config.screen_height / 2), frame_time = 0.05, end_pause = 0.24):
        animation = get_animation(id)
        if animation is not None:
            if len(animation["frames"]) > 0:
                crops = [None for _ in range(30)]
                for crop_x in range(5):
                    for crop_y in range(6):
                        crops[crop_x + crop_y * 5] = im.Crop("animations/" + animation["name"] + ".png", ((192*crop_x), (192*crop_y), 192, 192))
                _window_hide()
                for index, frame in enumerate(animation["frames"]):
                    timings_for_frame = list(filter(lambda t: t["frame"] == index, animation["timings"]))
                    for timing_index, timing in enumerate(timings_for_frame):
                        enact_timing(timing, index, timing_index)
                    composite_values = []
                    for raw_crop_id, xpos, ypos, scale, unknown2, unknown3, opacity, unknown4 in frame:
                        crop_id = abs(raw_crop_id)
                        if crop_id != -1 and crop_id < len(crops):
                            frame_scale = scale / 100
                            frame_xpos = round(192 - (192 * frame_scale * 0.5)) + xpos
                            frame_ypos = round(-200 - (192 * frame_scale * 0.5)) + ypos
                            composite_values.append((frame_xpos, frame_ypos))
                            composite_values.append(im.Alpha(im.FactorScale(crops[crop_id], frame_scale), opacity / 255))
                    animation_image = Composite((config.screen_width, config.screen_height), *composite_values)
                    renpy.show("animation_image", what=animation_image, at_list=[Transform(xpos=x - 192, ypos=y + 192)], zorder=5000)
                    renpy.pause(frame_time)
                renpy.hide("animation_image")
                renpy.with_statement(Dissolve(end_pause))
                _window_hide()
                renpy.pause(end_pause)
                for index, frame in enumerate(animation["frames"]):
                    timings_for_frame = list(filter(lambda t: t["frame"] == index, animation["timings"]))
                    for timing_index, timing in enumerate(timings_for_frame):
                        end_timing(timing, index, timing_index)

define fastdissolve = Dissolve(0.1)
define middissolve = Dissolve(0.25)
define slowdissolve = Dissolve(1.0)

label RemoveFromInventory(item):
    $ inventory.remove(item)
    return

label AddToInventory(item):
    $ inventory.append(item)
    return

style default:
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]

style youfound is text:
    size 30
    xpos 340
    ypos 95

style indented is text:
    xpos 312