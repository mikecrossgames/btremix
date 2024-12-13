screen event_image_screen(map_screen_details):
    tag map
    modal True
    if len(map_screen_details[0]) == 0:
        text "No events available: " + map_display_name(current_map):
            xalign 0.5
            ypos 0.5
    else:
        use image_choice_screen(map_screen_details[0], new_quests=map_screen_details[1])
