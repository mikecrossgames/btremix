init python:
    import math

    global show_new_followers
    show_new_followers = False

    def set_show_new_followers(prev_followers, new_followers):
        global show_new_followers
        if len(prev_followers) != len(new_followers):
            show_new_followers = True
        else:
            for i in range(len(prev_followers)):
                if prev_followers[i] != new_followers[i]:
                    show_new_followers = True

screen image_choice_screen(events_with_priorities, new_quests = False, extra_text = None):
    default viewed_quests = False

    python:
        image_events = []
        person_events = []
        followers_to_show = list(filter(lambda follower: follower != "Stacy", followers))
        for event, priority in events_with_priorities:
            if is_custom_ui_event(event):
                continue
            if priority[1] != "" or not is_person(event[0], event[1]):
                image_events.append((event, priority[0], priority[1]))
            else:
                person_events.append((event, priority[0]))

        num_image_rows = 1 if len(image_events) < 4 else 2 if len(image_events) <= 6 else math.ceil(len(image_events) / 6)
        num_image_cols = math.ceil(len(image_events) / num_image_rows)

        frame_ysize = config.screen_height - 192

    modal True
    tag imagechoice

    if extra_text != None:
        text extra_text size image_choice_font_size xpos 40 ypos 40

    use custom_ui(events_with_priorities)

    if display_normal_ui():
        if len(followers_to_show) > 0 and show_new_followers:
            use follower_list(followers_to_show)
        use ui_icons(new_quests and not viewed_quests)

    use hover_text()

    if show_timer is not None:
        use timer_frame(show_timer, [Return("TimeoutEvent")], on_screen = timer_onscreen())

    vbox:
        yalign 0.5
        xalign 0.5

        null:
            height 16
        if len(image_events) > 24:
            side "c r":
                area (0, 0, config.screen_width, frame_ysize)
                viewport id "image_choices":
                    draggable True
                    mousewheel True
                    frame:
                        xsize config.screen_width - gui.bar_size
                        background None
                        use image_list(image_events, num_image_rows, num_image_cols, not persistent.tooltip1 or (not persistent.tooltip2 and len(person_events) > 0))
                vbar value YScrollValue("image_choices")
            null:
                height 16
        else:
            use image_list(image_events, num_image_rows, num_image_cols, not persistent.tooltip1 or (not persistent.tooltip2 and len(person_events) > 0))

        if len(person_events) > 0:
            use person_list(person_events, not persistent.tooltip2, 0 if len(image_events) > 18 else config.screen_height - 54)
            if not persistent.tooltip2 and persistent.tooltip1:
                imagebutton:
                    xpos 0
                    ypos 0
                    xsize config.screen_width
                    ysize config.screen_height
                    idle "verydarkbg.webp"
                    hover "verydarkbg.webp"
                    action SetField(persistent, "tooltip2", True)
                add "images/tooltip2.webp" xpos 0 ypos -10

    fixed:
        if not persistent.tooltip1:
            imagebutton:
                xpos 0
                ypos 0
                xsize config.screen_width
                ysize config.screen_height
                idle "verydarkbg.webp"
                hover "verydarkbg.webp"
                action SetField(persistent, "tooltip1", True)
            add "images/tooltip1.webp" xpos 0 ypos 0

screen person_list(events, disabled, list_ypos = config.screen_height - 54):
    python:
        list_spacing = 20 if len(events) < 12 else 8 if len(events) < 18 else 1 
    hbox:
        xalign 0.5
        ypos list_ypos
        spacing list_spacing
        for event in events:
            use person_button(event[0], disabled)

screen person_button(event, disabled):
    python:
        image_name = get_person_image(event[0], "")
        if image_name is None:
            person_image = Solid('#808080')
            hover_person_image = person_image if disabled else Solid('#AAAAAA')
        else:
            person_image = im.FactorScale(get_filename(image_name), 54 / 144)
            hover_person_image = person_image if disabled else im.MatrixColor(person_image, im.matrix.tint(1.4, 1.4, 1.4))
        click_action = NullAction() if disabled else Return(event[0])
    imagebutton:
        xsize 54
        ysize 54
        idle person_image      
        hover hover_person_image
        action click_action

screen image_list(events, num_rows, num_cols, disabled):
    python:
        image_size = get_image_list_size(len(events))        
        hspacing = image_size / 8

    hbox:
        xalign 0.5
        vbox:
            spacing hspacing
            for row in range(num_rows):
                hbox:
                    spacing hspacing
                    xalign 0.5
                    for col in range(num_cols):
                        if (row * num_cols) + col < len(events):
                            python:
                                event = events[(row * num_cols) + col][0]
                                priority = events[(row * num_cols) + col][2]
                            use image_button(event, priority, image_size, disabled)
                        else:
                            null

screen image_button_base(event, priority, image_size, disabled):
    python:
        image_name = get_event_choice_image(event[0], priority, text=event[1])
        if image_name is None:
            event_image = Solid('#808080')
            hover_event_image = Solid('#AAAAAA')
        else:
            if image_name.endswith("_choice"):
                raw_image = Image(get_filename(image_name)) if image_size == 256 else im.FactorScale(get_filename(image_name), image_size / 256)
            else:
                raw_image = im.FactorScale(im.Crop(get_filename(image_name), (config.screen_width - config.screen_height) / 2, 0, config.screen_height, config.screen_height), image_size / config.screen_height)
            event_image = im.MatrixColor(raw_image, im.matrix.tint(0.8, 0.8, 0.8))
            hover_event_image = event_image if disabled else raw_image
        event_title = image_screen_event_title(event[1])
        click_action = NullAction() if disabled else Return(event[0])
    vbox:
        frame:
            xsize image_size + 6
            ysize image_size + 6
            background Solid("#000000")
            frame:
                background Solid("#808080")
                xsize image_size
                ysize image_size
                xpos 0
                ypos 0
                imagebutton:
                    xsize image_size
                    ysize image_size
                    xpos -3
                    ypos -3
                    idle event_image
                    hover hover_event_image
                    action click_action
                    hovered SetVariable("hover_text", event_title)
                    unhovered SetVariable("hover_text", "")

screen image_button(event, priority, image_size, disabled):
    use image_button_base(event, priority, image_size, disabled)

screen image_button(event, priority, image_size, disabled):
    variant "touch"
    vbox:
        use image_button_base(event, priority, image_size, disabled)
        python:
            event_title = image_screen_event_title(event[1])
        text event_title:
            xalign 0.5
            size 18
            xsize image_size
            font image_choice_screen_font
            color gui.selected_color