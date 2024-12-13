init python:
    def can_start():
        try:
            return mcap_authorized()
        except:
            return True

    def set_save_name():
        save_name = rpgm_display_name(current_map)

    def is_unknown(event):
        return False

    def get_rollback_enabled_for_map():
        return True

    def map_has_special_screen(map_name):
        return False

    def get_map_event_transform(event, person_image, enabled):
        if event["event"] in ["TownCorruptionFairy","Town2CorruptionFairy"]:
            return [figure_of_eight, fade_in_event]
        return None

    def get_extra_face(event):
        return None

    def adjust_event_xy(event, xypos):
        return xypos

    def is_faded_event(event):
        return False

    def get_map_event(event):
        return MapEvent(event)

    def get_event_zorder(event):
        if event in map_event_zorder:
            return map_event_zorder[event]
        base_zorder = 50 if event not in map_event_xy_fixed else map_event_xy_fixed[event][1]
        return base_zorder

    def image_screen_event_title(event_title):
        if event_title.endswith("."):
            return event_title[:-1]
        return event_title

    def pre_resolve_scene():
        return

    def post_resolve_scene(resolution):
        global pause_for_movement
        pause_for_movement = True
        return

    def adjust_backgrounds(backgrounds, background_type):
        global pause_for_movement
        pause_for_movement = False
        return backgrounds

    def setup_event_choices(map_name):
        global hover_text
        hover_text = None
        set_save_name()

    def autorun_hacks(map_name):
        conditions = [lambda event: True]
        return lambda event: all(map(lambda condition: condition(event), conditions))

    def event_in_list(event, event_list):
        return event in event_list

    def not_in_list(event_list):
        return lambda event: not event_in_list(event[0][0], event_list)

    def adjusted_coordinates_for_map(coordinates):
        return coordinates

    def event_screen_transition(map):
        return None
        # return Dissolve(FADE_DURATION)

    def map_hack_conditions(map_name, events):
        conditions = [lambda event: True]
        if map_name == "Town":
            if corruption == 3:
                event_result = event_call_result("TownToRiverEvent")
                if event_result != None and event_result == "TownToRiverEvent_0":
                    conditions.append(lambda event: event[0][0] != "TownToRiverEvent") # hack to prevent "pass" event preceding TownToRiver
        if map_name == "InnRooms":
            if "map_inn_rooms" in map_backgrounds[0]:
                conditions.append(lambda event: event[0][0] != "InnRoomsSleep") # prevent sleep from hallway
        if map_name == "InnRoomsNight":
            if "map_inn_rooms" in map_backgrounds[0]:
                conditions.append(lambda event: event[0][0] != "InnRoomsNightSleep") # prevent sleep from hallway
        if map_name == "TownFestivalNight" and hiding_place >= 3:
                conditions.append(lambda event: event[0][0] != "TownFestivalNightSouthEastToSouth") # prevent repeating glade hiding_place event
        return conditions

    def map_hacks(map_name, events):
        conditions = map_hack_conditions(map_name, events)
        return lambda event: all(map(lambda condition: condition(event), conditions))

    def event_is_enabled(event):
        return event["event"] not in [
            "PathNPCFestivalWorker2",
            "FoodStoreToolbag",
            "FestivalFinaleChef",
            "PoliceStationPrisoner",
            "PoliceStationBars",
            "AlexaBar",
            "FestivalFinaleHeyWhatsGoingOnHereDone",
        ]

    def hack_autoruns(autoruns):
        if current_map == "Path" and johan_dream == 2:
            autoruns = [*autoruns, "PathJohanDream"]
        if current_map == "Town2" and switch("erotic_photos_together"):
            autoruns = [*autoruns, "Town2LeynaJohanSexAutorun"]
        if current_map == "Town2":
            autoruns = [*autoruns, "Town2finalfiestafestivalAsAutorun"]                
        return autoruns

    def hack_parallels(parallels):
        return parallels

    def hack_events(map_name, events):
        new_events = []        
        for event in events:
            if event[0] == "Pathespacioentradafestival" and leyna_work >= 4 and leyna_work < 7:
                new_events.append(("Pathespacioentradafestival",_("Collect the flowers")))
            else:
                new_events.append(event)
        if map_name == "InnRooms":
            if "map_inn_rooms" not in map_backgrounds[0]:
                new_events = [
                    ("InnRoomsRoomToHallway", _("To hallway")),
                    ("InnRoomsSleep", _("Go to sleep")),
                ]
            else:
                new_events.append(("InnRoomsToInnRoom", _("To your room")))
        if map_name == "InnRoomsNight":
            if "map_inn_rooms" not in map_backgrounds[0]:
                new_events = [
                    ("InnRoomsRoomToHallway", _("To hallway")),
                    ("InnRoomsNightSleep", _("Go to sleep")),
                ]
            else:
                new_events.append(("InnRoomsToInnRoom", _("To your room")))
        if map_name == "HotSpringsExterior":
            new_events.append(("PathNPCFloat", _("Well")))
        if map_name == "InnNight":
            new_events.append(("InnJohanEndOfDay2", _("Johan")))
        if map_name == "Path":
            new_events.append(("PathNPCFestivalWorker2", _("Festival worker")))
        if map_name == "FoodStore":
            new_events.append(("FoodStoreToolbag", _("Toolbag")))
        if map_name == "FestivalFinale":
            new_events.append(("FestivalFinaleChef", _("Chef")))
            new_events.append(("FestivalFinaleHeyWhatsGoingOnHereDone", _("Talk to group")))
            event_locations["FestivalFinaleChef"] = (8, 6)
            event_locations["FestivalFinaleHeyWhatsGoingOnHereDone"] = (22, 19)
        if map_name == "TownNight":
            new_events.append(("TownNightBottleBoys", _("Talk to boys")))
            event_locations["TownNightBottleBoys"] = (41, 37)
        if map_name == "PoliceStation":
            new_events.append(("PoliceStationPrisoner", _("Prisoner")))
            new_events.append(("PoliceStationBars", _("Bars")))
        if map_name == "Bar2":
            new_events.append(("BarAlexa", _("Talk to Alexa")))
            
        player_location = get_player_location()
        locations = get_locations()
        if map_name in locations:
            if player_location in locations[map_name]:
                if "extra_events" in locations[map_name][player_location]:
                    for extra_event in locations[map_name][player_location]["extra_events"]:
                        event_locations[extra_event["event"]] = extra_event["pos"]
                        new_events.append((extra_event["event"], extra_event["title"]))
        return new_events

    def hack_no_events(map_name):
        return False

    def get_baked_event_image_map(map_name, pos=None):
        return "River" if map_name == "River2" else map_name

    def map_display_name(named_map):
        return "" # rpgm_display_name(named_map)

    def get_time_text(map_text):
        return ""

    def set_movement_script(called_from, character, moves):
        global last_move_direction
        for move in moves:
            if move[0] == "SCRIPT" and "find_path" in move[1] and len(move) == 3:
                perform_moves(character, move[2])
            if character == "player":
                if move == "U" or move == "D" or move == "L" or move == "R":
                    last_move_direction = move

label TransferPlayer(to_map, called_from, x, y, direction = 0, reset = True):
    if to_map == "TownFestivalNight" and called_from.startswith("TownFestivalNighteventoblackmail_0"):
        return # hack for move away
    if called_from.startswith("Glade") and to_map.startswith("Town"):
        $ y = 42
    if called_from.startswith("HouseInterior") and to_map.startswith("Town"):
        $ x = 7
        $ y = 22
    $ old_pos = (map_x, map_y)
    $ old_location = get_xy_location(current_map, map_x, map_y)
    $ new_location = get_xy_location(to_map, x, y)
    $ map_x = x
    $ map_y = y
    if direction != 0:
        $ map_direction = direction
    if to_map != current_map or old_location != new_location:
        $ map_event_xyposition = {}
        $ reset_pictures()
        if previous_map_background_map is None:
            $ previous_map_background_map = (current_map, old_pos)
            # "previous_map_background_map is [current_map] [old_pos]"
    call SwitchMap(to_map, called_from, reset) from _call_hacks_SwitchMap
    if to_map.startswith("Town") or to_map.startswith("Festival"):
        $ player_location = get_player_location()
        $ locations = get_locations()
        if current_map in locations:
            if player_location in locations[to_map]:
                if "start_event" in locations[to_map][player_location]:
                    $ renpy.call(locations[to_map][player_location]["start_event"])
    if to_map == "Glade" and called_from == "TownFestivalNighteventoescondite_0":
        $ set_transparency_backgrounds(["bg_glade_night"])
        $ set_map_backgrounds(["map_glade_night"])
    if to_map == "Mountains" and called_from.startswith("Festival"):
        $ set_transparency_backgrounds(["map_mountain4"])
        $ set_map_backgrounds(["map_mountain4"])
    if to_map == "Mountains" and called_from == "Pathespacioentradafestival_7":
        $ set_transparency_backgrounds(["map_mountain3"])
        $ set_map_backgrounds(["map_mountain3"])
    if to_map == "InnRooms" and called_from in ["Townfinaldelprimerdia_0", "InnNightentradaalaposadanoche_0"]:
        call InnRoomBG from _call_InnRoomBG_TransferPlayer
        $ scene_state = "dirty" if scene_state != "faded_out" else "faded_out"
        $ fade_in()
        $ resolve_scene()
    if to_map == "InnRooms" and called_from in ["Innposadero_3"]:
        call InnRoomBG from _call_InnRoomBG_TransferPlayer2
        $ resolve_scene()
    if to_map == "InnRooms" and called_from == "InnNightentradaalaposadanoche_0":
        $ fade_out()
        call EndOfDayPause from _call_EndOfDayPause_Day2
    if to_map == "Inn" and called_from == "Townfinaldelprimerdia_0":
        call EndOfDayPause from _call_EndOfDayPause_Day1
    if to_map == "Festival" and called_from == "FestivalButtPlugEvent_1":
        $ set_transparency_backgrounds(["bg_festival_night"])
        $ set_map_backgrounds(["map_festival_night"])
    if to_map == "Town" and called_from == "River2EVENTORIO2":
        pause 1.5
return

label EndOfDayPause():
    pause 1
    pause 1
    return

default call_text = ""
default previous_call_text = ""
default scene_unlocked = False
default followers_before_call = None
default map_of_called_event = None
default originating_event = None
default originating_trigger = None

label CallWithHacks(event, trigger):
    if not isinstance(event, str):
        $ typeof_event = type(event)
        "CallWithHacks ([typeof_event]) [event]"
        return
    $ previous_call_text = "(previous " + call_text + ")"
    $ call_text = trigger + ":" + event
    $ show_dialog_background()
    $ hide_shown_images()
    $ reset_choices()
    $ followers_before_call = followers
    $ originating_event = event
    $ originating_trigger = trigger
    if trigger == "event":
        $ move_player_to_event(event)
    $ map_of_called_event = current_map
    # hack before
    # end hacks
    if scene_state != "faded_out":
        $ resolve_scene("dirty")
    $ renpy.checkpoint(hard = False)
    $ renpy.call(event if not renpy.has_label(event + "Custom") else event + "Custom", trigger=trigger)
    $ call_result = _return
    if call_result != None:
        $ call_text = trigger + ":" + call_result[2]
        if trigger == "autorun":
            $ have_run.append(call_result[2])
    if followers_before_call != None:
        $ set_show_new_followers(followers_before_call, followers)
    if game_over:
        return call_result
    # hack after
    # end hacks
    return call_result

transform fade_in_event():
    alpha 0
    linear 2.0 alpha 1

transform figure_of_eight():
    ease 0.25 xpos -20 ypos -20
    easein 0.25 xpos -25 ypos -30
    ease 0.25 xpos 0 ypos -20
    easeout 0.25 xpos -3 ypos 3
    easeout 0.25 xpos -10 ypos 10
    ease 0.25 xpos -5 ypos 20
    easeout 0.25 xpos 5 ypos 10
    ease 0.25 xpos 0 ypos 0
    repeat

label PlayEvent(play_event, event, base_event):
    if play_event:
        if renpy.has_label(event + "Custom"):
            $ renpy.call(event + "Custom")
        else:
            $ renpy.call(event)
        if _return:
            $ erase_event_from_map(base_event)
    return

default pause_for_movement = True

label Movement(called_from, character, moves):
    if pause_for_movement:
        call PauseForMoves(moves) from _PauseForMovement_PauseForMoves
    call MovementHacks(called_from, character, moves) from _PauseForMovement_MovementHacks
    return

label ReturnToTitleScreen(called_from):
    $ game_over = True
    return
