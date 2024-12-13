screen direction_list(events):
    fixed:
        xsize config.screen_width
        ysize config.screen_height
        for event in events:
            python:
                is_north = "North" in event[0][0]
                is_west = "West" in event[0][0]
                is_east = "East" in event[0][0]
                is_south = "South" in event[0][0]
                direction_image_size = 64
                event_xpos = 0 if is_west else config.screen_width - direction_image_size if is_east else round((config.screen_width - direction_image_size) / 2)
                event_ypos = 0 if is_north else config.screen_height - 128 if is_south else round((config.screen_height - 128) / 2)
            fixed:
                xpos event_xpos
                ypos event_ypos
                use image_button(event[0], event[2], image_size=direction_image_size, disabled=False)
