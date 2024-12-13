default scene_say_text = ""
default scene_state_before_resolve = ""

screen debug_info_screen():
    python:
        def coerce_var_value(value):
            if value == "True":
                return True
            elif value == "False":
                return False
            elif value.isdigit():
                return int(value)
            else:
                return value

    default variable_to_set = None
    default variable_set_value = ""
    tag menu
    style_prefix "debug_info"
    use game_menu(_("Debug info")):
        if variable_to_set != None:
            vbox:
                text variable_to_set[0] + "="
                input:
                    value ScreenVariableInputValue("variable_set_value", default=str(variable_to_set[1]))
                    focus True
                if variable_set_value != None:
                    textbutton "Update":
                        action [
                            SetVariable(variable_to_set[0], coerce_var_value(variable_set_value)),
                            SetScreenVariable("variable_to_set", None),
                            SetScreenVariable("variable_set_value", "")
                        ]
                textbutton "Cancel":
                    action [SetScreenVariable("variable_to_set", None), SetScreenVariable("variable_set_value", "")]
        else:
            viewport:
                draggable True 
                mousewheel True
                xsize 920
                vbox:
                    use debug_info_misc()
                    use debug_info_visuals()
                    use debug_info_game_vars()
                    hbox:
                        spacing 20
                        textbutton "Reset gallery scenes":
                            action SetField(persistent, "unlocked_scenes", ["Intro"])
                        textbutton "Reset tooltips":
                            action [SetField(persistent, "tooltip1", False), SetField(persistent, "tooltip2", False)]
                        textbutton "Clear auth":
                            action [Function(mcap_clear_auth), MainMenu(confirm=True)]

screen debug_info_misc():
    text "Misc"
    vbox:
        python:
            player_location = get_player_location()
            map_text = "map=" + current_map + " " + str(map_x) + "," + str(map_y) + " : " + player_location
            follower_text = "followers=" + ("(None)" if len(followers) == 0 else ", ".join(followers))
            have_run_text = "have_run=" + ("(None)" if len(have_run) == 0 else ", ".join(have_run))
            displayed_call_text = call_text + " " + previous_call_text
            seen_text = "seen_today (" + str(len(events_seen_today)) + ") =" + str(", ".join(events_seen_today)) + " " + ("No date" if events_seen_date is None else str(events_seen_date))
        text map_text size gui.text_size
        text displayed_call_text size gui.text_size
        text follower_text size gui.text_size
        text have_run_text size gui.text_size
        text seen_text size gui.text_size
        null height 20

screen debug_info_vars(var_name, variable_values):
    python:
        import math

        text_strings = []
        for key, value in variable_values.iteritems():
            if value != 0 and value != "0":
                text_strings.append((key, value))
        grid_rows = math.floor(len(text_strings) / 2) + 1
        if len(text_strings) % 2 != 0:
            range_val = 2 - (len(text_strings) % 2)
            for i in range(range_val):
                text_strings.append(None)

    if len(text_strings) > 0:
        text var_name
        grid 2 grid_rows:
            xsize 480
            for text_string in text_strings:
                if text_string is None:
                    null
                else:
                    textbutton text_string[0] + "=" + str(text_string[1]):
                        text_size gui.text_size
                        action SetScreenVariable("variable_to_set", text_string)
        null height 20

screen debug_info_game_vars():
    python:
        item_values = get_item_values()
        items_got = []
        switches_on = []
        self_switches_on = []
        quests = []
        for key, value in switches.iteritems():
            if value:
                switches_on.append(str(key))
        for key, value in item_values.iteritems():
            if value != "False":
                items_got.append(key)
        for key, value in self_switches.iteritems():
            for key2, value2 in value.iteritems():
                for key3, value3 in value2.iteritems():
                    if value3:
                        self_switches_on.append(str(key) + ":" + str(key2) + ":" + str(key3))
        self_switches_on.sort()
        for quest in get_active_quests():
            quests.append(quest["title"])
    use debug_info_vars("Game Vars", game_variable_values())
    use debug_info_vars("People Vars", game_people_values())
    use debug_info_vars("Message Vars", game_message_values())
    if len(switches_on) > 0:
        text "Switches"
        vbox:
            python:
                switch_to_display = ", ".join(sorted(switches_on))
            text switch_to_display size gui.text_size
            null height 20
    if len(self_switches_on) > 0:
        text "Self Switches"
        vbox:
            python:
                switch_to_display = ", ".join(self_switches_on)
            text switch_to_display size gui.text_size
            null height 20            
    if len(items_got) > 0:
        text "Items"
        vbox:
            python:
                item_to_display = ", ".join(sorted(items_got))
            text item_to_display size gui.text_size
            null height 20
    if len(quests) > 0:
        text "Quests"
        vbox:
            python:
                quest_to_display = ", ".join(sorted(quests))
            text quest_to_display size gui.text_size
            null height 20
    use quest_status

screen debug_info_visuals():
    text "Visuals"
    vbox:
        python:
            transparency_backgrounds_to_display = "Transparency Backgrounds=" + ("None" if transparency_backgrounds == None else ", ".join(list(map(lambda v: v if type(v) is str else "Composite", transparency_backgrounds))))
            map_backgrounds_to_display = "Map Backgrounds=" + ("None" if map_backgrounds == None else ", ".join(list(map(lambda v: v if type(v) is str else "Composite", map_backgrounds))))
            backgrounds_to_display = transparency_backgrounds_to_display + " " + map_backgrounds_to_display
            playing_videos_to_display = "Playing videos=" + ", ".join(list(map(lambda v: videos[v]["filename"], playing_videos))) +" obscured=" + ", ".join(list(map(lambda v: obscured_videos[v]["filename"], obscured_playing_videos)))
            last_image_set_to_display = "" if len(last_displayed_pictures_set) == 0 else ", ".join(list(map(lambda v: v if type(v) == str else "(none)" if v == None else v["image"], last_displayed_pictures_set)))
            last_image_to_display = "No last image (" + last_image_set_to_display + ")" if last_displayed_pictures == None else "Last image=" + ", ".join(list(map(lambda v: v if type(v) == str else "(none)" if v == None else v["image"], last_displayed_pictures)))
            images_shown_to_display = "Images shown=" + ", ".join(list(map(lambda v: v, images_shown)))
            # videos_to_display = "Videos = " + ", ".join(list(map(lambda v: "None" if v == None else "Video", videos)))
            # if len(playing_videos) > 0:
            #     video_extra = "len(playing_videos) > 0"
            #     video_extra2 = "None" if videos[playing_videos[len(playing_videos) - 1]] == None else "Video"
            # else:
            #     video_extra = "len(playing_videos) == 0"
            #     video_extra2 = "n/a"
            scene_state_text = "scene_state=" + scene_state_before_resolve
            tint_text = "tint=" + str(screen_tint)
        text scene_state_text size gui.text_size
        text tint_text size gui.text_size
        text backgrounds_to_display size gui.text_size
        text scene_say_text size gui.text_size
        text images_shown_to_display size gui.text_size
        text last_image_to_display size gui.text_size
        text playing_videos_to_display size gui.text_size
        # text videos_to_display size gui.text_size
        # text video_extra size gui.text_size
        # text video_extra2 size gui.text_size
        null height 20
                
style debug_info_label is gui_label
style debug_info_label_text is gui_label_text
style debug_info_text is gui_text

style debug_info_label_text:
    size gui.label_text_size

screen quest_status():
    python:
        def get_quest_details(dict):
            dets = ""
            for key, value in dict.iteritems():
                dets = dets + str(key) + "=" + ",".join(list(map(lambda v: str(v), list(value)))) + " "
            return dets

        qsr = get_quest_details(quest_steps_revealed)
        qsc = get_quest_details(quest_steps_complete)
        qsf = get_quest_details(quest_steps_failed)
        pqsr = get_quest_details(previous_quest_steps["revealed"])
        pqsc = get_quest_details(previous_quest_steps["complete"])
        pqsf = get_quest_details(previous_quest_steps["failed"])
    vbox:
        hbox:
            text "quest steps revealed"
            text qsr
        hbox:
            text "quest steps complete"
            text qsc
        hbox:
            text "quest steps failed"
            text qsf
        hbox:
            text "previous quest steps revealed"
            text pqsr
        hbox:
            text "previous quest steps complete"
            text pqsc
        hbox:
            text "previous quest steps failed"
            text pqsf
        null height 20
