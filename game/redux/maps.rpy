init python:
    def no_nones(event):
        return event != None

    def at_same_location(player_location):
        return lambda event: player_location in get_event_locations(current_map, event[0][0])

    def at_same_location_for_map(map):
        def at_same(player_location):
            return lambda event: player_location in get_event_locations(map, event[0][0])
        return at_same

    def not_excluded_by_preceding(preceding):
        if len(preceding) == 1 and preceding[0].startswith("!"):
            return lambda event: event[0][0] == preceding[0][1:]
        return lambda event: event[0][0] not in preceding

    def get_call_result(event, trigger):
        if renpy.has_label(event + "Custom"):
            return renpy.call_in_new_context(event + "Custom", play_event=False, trigger=trigger)
        return renpy.call_in_new_context(event, play_event=False, trigger=trigger)

    def event_call_result(event):
        call_result = get_call_result(event, trigger="event")
        return None if call_result is None else call_result[2]

    def event_result_tuple_include_none(event):
        call_result = get_call_result(event[0], trigger="event")
        return (event, (1, "", event[0] + "_0") if call_result == None else call_result)

    def event_result_tuple(event):
        call_result = get_call_result(event[0], trigger="event")
        if call_result == None:
            return None
        return (event, call_result)

    def autorun_call_result_with_multiple(event, multiple_triggers):
        call_result = get_call_result(event, trigger="autorun")
        if call_result == None:
            return None
        if event in multiple_triggers:
            call_result_any = get_call_result(event, trigger="any")
            if call_result_any == None:
                return None
            if call_result[2] != call_result_any[2]:
                return None
        return (event, call_result)

    def autorun_call_result_for_triggers(multiple_triggers):
        return lambda event: autorun_call_result_with_multiple(event, multiple_triggers)

    def parallel_call_result(event):
        call_result = get_call_result(event, trigger="parallel")
        if call_result == None:
            return None
        return (event, call_result)

    have_run = []

    def not_has_run(event):
        return event[1] == None or event[1][2] not in have_run

    def reset_map_runs():
        global have_run
        have_run = []


    def get_autoruns_for_map(map_name):
        autoruns = hack_autoruns(rpgm_autoruns_for_map(map_name))
        multiple_triggers = rpgm_multiple_triggers_for_map(map_name)
        autorun_call_result = autorun_call_result_for_triggers(multiple_triggers)
        filtered_autoruns = list(filter(no_nones, map(autorun_call_result, autoruns)))
        filtered_autoruns = list(filter(not_has_run, filtered_autoruns))
        return list(filter(autorun_hacks(map_name), filtered_autoruns))

    def get_event_to_run(filtered_autoruns):
        event_to_run = (None, (-1, ""))
        for autorun in filtered_autoruns:
            if autorun[1][0] > event_to_run[1][0]:
                event_to_run = autorun
        return event_to_run

    def get_filtered_events(map_name, allow_all = False, location = None):
        player_location = location if location is not None else get_player_location()
        at_same = at_same_location_for_map(map_name)
        preceding_events = get_preceding_events()
        events = hack_events(map_name, rpgm_events_for_map(map_name))
        if allow_all:
            filtered_events = list(map(event_result_tuple_include_none, events))
            filtered_events = list(filter(at_same(player_location), filtered_events))
        else:
            filtered_events = list(filter(no_nones, map(event_result_tuple, events)))
            filtered_events = list(filter(map_hacks(map_name, filtered_events), filtered_events))
            filtered_events = list(filter(at_same(player_location), filtered_events))
            preceding_map_events = []
            only_this_event = None
            for event in filtered_events:
                if event[0][0] in preceding_events:
                    if preceding_events[event[0][0]] == "*":
                        only_this_event = event
                    else:
                        preceding_map_events += preceding_events[event[0][0]]
            if only_this_event != None:
                filtered_events = [only_this_event]
            else:
                filtered_events = list(filter(not_excluded_by_preceding(preceding_map_events), filtered_events))
        return filtered_events

    def get_filtered_events_for_map(map_name, allow_all = False, location=None):
        filtered_events = get_filtered_events(map_name, allow_all, location=location)
        if len(filtered_events) == 0:
            hack_no_events(map_name)
            filtered_events = get_filtered_events(map_name, allow_all, location=location)
        return filtered_events

    def events_have_image_choices(filtered_events):
        if current_map.startswith("Halloween"):
            return False
        return any(map(lambda event: is_event_image(event[0][0]) or is_person(event[0][0], event[0][1]), filtered_events))

    def erase_event_from_map(event_name):
        global erased_events
        erased_events.append(event_name)

    def is_erased(event_name):
        global erased_events
        return event_name in erased_events

    def reset_event_erasures():
        global erased_events
        erased_events = []

default erased_events = []

label RunParallels(map_name):
    $ parallels = hack_parallels(rpgm_parallels_for_map(map_name))
    $ filtered_parallels = list(filter(not_has_run, filter(no_nones, map(parallel_call_result, parallels))))
    $ parallel_to_run = 0
    while parallel_to_run < len(filtered_parallels):
        $ parallel_event = filtered_parallels[parallel_to_run]
        call CallWithHacks(parallel_event[0], trigger="parallel") from _call_RunParallels_CallWithHacks_parallel_event
        $ parallel_to_run += 1
    return

label PlayAutoruns(filtered_autoruns):
    $ event_to_run = get_event_to_run(filtered_autoruns)
    call CallWithHacks(event_to_run[0], trigger="autorun") from _call_PlayAutoruns_CallWithHacks_event_to_run
    return

label StartMap(map_name):
    $ reset_map_runs()
    $ reset_event_erasures()
    $ has_start_function = renpy.has_label(map_name + "Start")
    if has_start_function:
        $ has_custom_start_function = renpy.has_label(map_name + "StartCustom")
        if has_custom_start_function:
            $ renpy.call(map_name + "StartCustom")
        else:
            $ renpy.call(map_name + "Start")
    return

label EndMap(map_name):
    $ has_end_function = renpy.has_label(map_name + "End")
    if has_end_function:
        $ has_custom_end_function = renpy.has_label(map_name + "EndCustom")
        if has_custom_end_function:
            $ renpy.call(map_name + "EndCustom")
        else:
            $ renpy.call(map_name + "End")
    return

label CallCustom(label_name, parameters = None):
    $ has_custom_function = renpy.has_label(label_name + "Custom")
    if has_custom_function:
        $ renpy.call(label_name + "Custom", parameters)
    else:
        $ renpy.call(label_name, parameters)
    return

label SwitchMap(new_map_name, called_from, reset = True):
    if new_map_name != current_map:
        if current_map != "":
            call CallCustom("EndMap", current_map) from _call_CallCustom
        $ current_map = new_map_name
        if new_map_name != "Special" and new_map_name != "Map36":
            call CallCustom("StartMap", current_map) from _call_CallCustom_1
    return
