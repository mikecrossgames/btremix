label start:
    stop music fadeout 1.0
    scene black
    call TransferPlayer("Intro", "IntroStart", 0, 0, reset=True) from _call_IntroStart
    call PlayEntireGame from _call_PlayEntireGame 
    return

label ShowChoiceBackground(state):
    if state == "faded_out":
        $ fade_in()
    $ resolve_scene("dirty")
    # remove baked
    $ use_baked_images = False
    $ resolve_scene("dirty")
    $ use_baked_images = True
    return

label HideChoiceBackground(state):
    if state == "faded_out":
        $ fade_out()
    return

default no_advancement_events = 0
default last_done = 0 # TODO delete

label PlayEntireGame:
    $ reset_pictures()
    label GameLoop:
        pass
    $ set_save_name()
    $ in_game_loop = True
    if persistent.sfw_mode != redux_conf("sfw") or developer_mode():
        $ redux_config = get_redux_config()
    call RunParallels(current_map) from _call_PlayEntireGame_RunParallels
    $ resolve_scene()
    $ autoruns = get_autoruns_for_map(current_map)
    if len(autoruns) > 0:
        call PlayAutoruns(autoruns) from _call_PlayEntireGame_PlayAutoruns
    else:
        $ config.rollback_enabled = get_rollback_enabled_for_map()
        $ choice_scene_state = scene_state
        $ last_done = get_done_count()
        call ShowChoiceBackground(choice_scene_state) from _call_ShowChoiceBackground
        $ setup_event_choices(current_map)
        $ filtered_events = get_filtered_events_for_map(current_map, show_all_events)
        if map_has_special_screen(current_map):
            call screen map_special_screen(current_map) with event_screen_transition(current_map)
            pause 0.5
            $ chosen_event = _return
        elif events_have_image_choices(filtered_events) and not show_event_screen(current_map, []):
            call screen event_image_screen((filtered_events, get_new_quests_or_objectives())) with event_screen_transition(current_map)
            $ chosen_event = _return
        else:
            $ event_objects = to_event_objects(filtered_events)            
            $ player_location = get_xy_location(current_map, map_x, map_y)
            $ choices = list(map(get_choice_from_event(player_location), event_objects))
            if show_event_screen(current_map, choices):
                $ chosen_event = None
                while chosen_event is None:
                    call screen event_map_screen(filtered_events, get_new_quests_or_objectives()) with event_screen_transition(current_map)
                    if _return == "":
                        $ filtered_events = get_filtered_events_for_map(current_map, show_all_events)
                    else:
                        $ chosen_event = _return
            else:
                $ choices_in_order = sorted_choices(choices)
                $ stealth_events = get_stealth_events(choices_in_order)
                if len(stealth_events) > 0:
                    call StealthEvent(choices_in_order, stealth_events) from _call_PlayEntireGame_StealthEvent
                    $ chosen_event = _return
                else:
                    $ chosen_event = get_choice(choices_in_order)
        call HideChoiceBackground(choice_scene_state) from _call_HideChoiceBackground
        call CallWithHacks(chosen_event, trigger="event") from _call_PlayEntireGameLoop_chosen_event
        if get_done_count() > last_done:
            $ no_advancement_events = 0
        else:
            $ no_advancement_events += 1
            if no_advancement_events > 20 and not switch("fairy_on"):
                $ set_switch("fairy_on", True)
        $ config.rollback_enabled = True
    if scene_unlocked:
        $ renpy.notify("Scene unlocked")
        $ scene_unlocked = False
    if not game_over:
        jump GameLoop
    return