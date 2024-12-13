init python:
    from math import sqrt

    def largest_square(coordinates):
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

    # | padding | 1/2 left size | left | 

    def x_to_px(x, pos_range):
        return round((x - pos_range[0] / (pos_range[1] - pos_range[0])) * config.screen_width)

    def y_to_px(y, pos_range):
        return round((y - pos_range[2] / (pos_range[3] - pos_range[3])) * config.screen_height)

screen position_choice_screen(events_with_priorities, extra_text = None):
    python:
        all_direction_events = ["TownGoNorth", "TownGoEast", "TownGoSouth", "TownGoWest"]
        direction_events = []
        image_events = []
        left_x = None
        right_x = None
        bottom_y = None
        top_y = None
        for event, priority in events_with_priorities:
            if event[0] in all_direction_events:
                direction_events.append((event, priority[0], priority[1]))
            else:
                image_events.append((event, priority[0], priority[1]))

    if left_x == None or right_x == None or bottom_y == None or top_y == None:
        use image_choice_screen(events_with_priorities, extra_text)
    else:
        use position_choices(direction_events, image_events, [left_x, right_x, bottom_y, top_y], extra_text)

screen position_choices(direction_events, image_events, pos_range, extra_text):
    python:
        if map_backgrounds != None and len(map_backgrounds) > 0:
            background_image = get_small_image_from_backgrounds(map_backgrounds)
        else:
            last_displayed = get_last_displayed_image_small()
            if last_displayed == None:
                if transparency_backgrounds != None and len(transparency_backgrounds) > 0:
                    background_image = get_small_image_from_backgrounds(transparency_backgrounds)
                else:
                    background_image = Solid("#000000", xysize=(204, 156))
            else:
                background_image = Composite((204, 156), (0, 0), last_displayed, (0, 0), "darkbg")

        coordinates = list(map(lambda event: event[3], image_events))
        square_size = largest_square(coordinates)
        square_size_rounded = round(square_size)

    modal True
    tag personchoice
    add background_image xsize config.screen_width ysize config.screen_height
    use direction_list(direction_events)

    fixed:
        xsize config.screen_width
        ysize config.screen_height

        text "PERSON CHOICE SCREEN" size 24 xalign 0.95 ypos 40 color "#FFFFFF"
        text str(pos_range[0]) size 24 xalign 0.95 ypos 80 color "#FFFFFF"
        text str(pos_range[1]) size 24 xalign 0.95 ypos 120 color "#FFFFFF"
        text str(square_size_rounded) size 24 xalign 0.95 ypos 160 color "#FFFFFF"

        vbox:
            for image_event in image_events:
                python:
                    text_for_event = image_event[0][0] + " x=" + str(image_event[3][0]) + " y=" + str(image_event[3][1])
                    event_xpos = round((image_event[3][0] / pos_range[1]) * (config.screen_width - square_size))
                    event_ypos = round((image_event[3][1] / pos_range[3]) * (config.screen_height - square_size))
                    text_for_event = text_for_event + " (" + str(event_xpos) + ", " + str(event_ypos) + ")"
                text text_for_event

        for image_event in image_events:
            python:
                event_text = image_event[0][0]
                event_xpos = round((image_event[3][0] / pos_range[1]) * (config.screen_width - square_size))
                event_ypos = round((image_event[3][1] / pos_range[3]) * (config.screen_height - square_size))

            # textbutton event_text:            
            #     action None
            #     xpos event_xpos
            #     ypos event_ypos

