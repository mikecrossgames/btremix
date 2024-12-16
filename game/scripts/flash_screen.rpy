init python:
    def flash_screen(wait=True):
        rgba = [255,255,255,170]
        frames = 60
        duration = frames / 120
        _window_hide()
        rgb_hex = '{:02x}{:02x}{:02x}{:02x}'.format(rgba[0], rgba[1], rgba[2], rgba[3])
        fadeflash = fadetoeasein(1.0, 0.0, duration)
        renpy.show("flash_screen", what=Solid(rgb_hex, xysize=(config.screen_width, config.screen_height)), at_list=[fadeflash], zorder=4000)
        if wait:
            renpy.pause(duration)
            renpy.hide("flash_screen")
