label HotSpringsBathroomBG:
    $ set_transparency_backgrounds(["bg_hot_springs_bathroom"])
    $ set_map_backgrounds(["bg_hot_springs_bathroom"])
    return

label HotSpringsBathroomStart:
    call HotSpringsBathroomBG from _call_HotSpringsBathroomBG
    stop music
    stop bgs
    return

label HotSpringsBathroomEnd:
    return

label HotSpringsBathroomeventoenseatrabajoBase:
    Receptionist "This is the bathroom, as you can see when you came in, it's mixed baths so don't be surprised if people of all kinds come"
    Leyna "Yes... I remember..."
    call Movement("HotSpringsBathroomeventoenseatrabajo", "HotSpringsBathroomeventoenseatrabajo", ["D","L","L","TURN_R"]) from _call_HotSpringsBathroomeventoenseatrabajo_Movement
    call Movement("HotSpringsBathroomeventoenseatrabajo", "player", [["CHANGE_SPEED",3],"D","L","L"]) from _call_HotSpringsBathroomeventoenseatrabajo_Movement_1
    $ resolve_scene()
    Receptionist "Here are the towels, you always have to have them ready and clean for the customers"
    Leyna "All right, I'll remember that"
    call Movement("HotSpringsBathroomeventoenseatrabajo", "HotSpringsBathroomeventoenseatrabajo", ["D","D","D","R","D","D","D","D","R","R","R","R","R","TURN_L"]) from _call_HotSpringsBathroomeventoenseatrabajo_Movement_2
    call Movement("HotSpringsBathroomeventoenseatrabajo", "player", ["D","D",["WAIT",60],"D","D","D","D","D","R","R","R"]) from _call_HotSpringsBathroomeventoenseatrabajo_Movement_3
    $ resolve_scene()
    Receptionist "Here you have to put the flowers in the water, so that are mixed with the vapors so that the whole room smells good"
    "Recorder: as you know, those flowers have some qualities.. they excite our customers so they feel more... relaxed"
    Leyna "I see..."
    Receptionist "For now that's all, at the entrance you just have to be nice and show people where they can change their clothes"
    Receptionist "The bathrooms are mixed but the dressing rooms are not, remember"
    Leyna "Of course, no mixing in the locker room, be friendly to customers and have clean towels"
    Leyna "I think I'm ready"
    Leyna "Here is the uniform. Get changed and we'll see you at the reception"
    $ leyna_work = 9
    $ fade_out()
    call TransferPlayer("Reception", "HotSpringsBathroomeventoenseatrabajo", 9, 3, direction=2) from _call_HotSpringsBathroomeventoenseatrabajo_TransferPlayer
    $ fade_in()
    $ resolve_scene()
    return False

label HotSpringsBathroomeventoenseatrabajo(play_event = True, trigger = None): # autorun
    if is_erased("HotSpringsBathroomeventoenseatrabajo"):
        return None
    elif trigger == "autorun" and leyna_work >= 8:
        call PlayEvent(play_event, "HotSpringsBathroomeventoenseatrabajoBase", "HotSpringsBathroomeventoenseatrabajo") from _call_HotSpringsBathroomeventoenseatrabajo_PlayEvent
        return (1, "", "HotSpringsBathroomeventoenseatrabajo")
    return None

