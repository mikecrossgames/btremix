label HotSpringsExteriorBG:
    $ set_transparency_backgrounds(["map_hot_springs_exterior"])
    $ set_map_backgrounds(["map_hot_springs_exterior"])
    return

label HotSpringsExteriorStart:
    call HotSpringsExteriorBG from _call_HotSpringsExteriorBG
    stop music
    stop bgs
    return

label HotSpringsExteriorEnd:
    return

label HotSpringsExteriorToReceptionBase:
    call PlaySound("sound", "audio/Open1.ogg", volume=0.9, no_loop=True) from _call_HotSpringsExteriorEV001_PlaySound
    call Movement("HotSpringsExteriorEV001", "HotSpringsExteriorEV001", ["TURN_L",["WAIT",3],"TURN_R",["WAIT",3],"TURN_U","THROUGH_ON"]) from _call_HotSpringsExteriorEV001_Movement
    call Movement("HotSpringsExteriorEV001", "player", ["FORWARD"]) from _call_HotSpringsExteriorEV001_Movement_1
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_HotSpringsExteriorEV001_PlaySound_1
    call TransferPlayer("Reception", "HotSpringsExteriorEV001", 5, 12, direction=0) from _call_HotSpringsExteriorEV001_TransferPlayer
    $ resolve_scene()
    return False

label HotSpringsExteriorToReception(play_event = True, trigger = None): # event
    if is_erased("HotSpringsExteriorToReception"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "HotSpringsExteriorToReceptionBase", "HotSpringsExteriorToReception") from _call_HotSpringsExteriorToReception_PlayEvent
        return (1, "", "HotSpringsExteriorToReception")
    return None

label HotSpringsExteriorToReception_v2Base:
    call PlaySound("sound", "audio/Open1.ogg", volume=0.9, no_loop=True) from _call_HotSpringsExteriorEV002_PlaySound
    call Movement("HotSpringsExteriorEV002", "HotSpringsExteriorEV002", ["TURN_L",["WAIT",3],"TURN_R",["WAIT",3],"TURN_U","THROUGH_ON"]) from _call_HotSpringsExteriorEV002_Movement
    call Movement("HotSpringsExteriorEV002", "player", ["FORWARD"]) from _call_HotSpringsExteriorEV002_Movement_1
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_HotSpringsExteriorEV002_PlaySound_1
    call TransferPlayer("Reception", "HotSpringsExteriorEV002", 6, 12, direction=0) from _call_HotSpringsExteriorEV002_TransferPlayer
    $ resolve_scene()
    return False

label HotSpringsExteriorToReception_v2(play_event = True, trigger = None): # event
    if is_erased("HotSpringsExteriorToReception_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "HotSpringsExteriorToReception_v2Base", "HotSpringsExteriorToReception_v2") from _call_HotSpringsExteriorToReception_v2_PlayEvent
        return (1, "", "HotSpringsExteriorToReception_v2")
    return None

label HotSpringsExteriorHotSpingsBase:
    "~ HOT SPRINGS ~"
    return False

label HotSpringsExteriorHotSpings(play_event = True, trigger = None): # event
    if is_erased("HotSpringsExteriorHotSpings"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "HotSpringsExteriorHotSpingsBase", "HotSpringsExteriorHotSpings") from _call_HotSpringsExteriorHotSpings_PlayEvent
        return (1, "", "HotSpringsExteriorHotSpings")
    return None

label HotSpringsExteriorToPathBase:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_HotSpringsExteriorEV004_PlaySound
    call TransferPlayer("Path", "HotSpringsExteriorEV004", 11, 0, direction=2) from _call_HotSpringsExteriorEV004_TransferPlayer
    $ resolve_scene()
    return False

label HotSpringsExteriorToPath(play_event = True, trigger = None): # event
    if is_erased("HotSpringsExteriorToPath"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "HotSpringsExteriorToPathBase", "HotSpringsExteriorToPath") from _call_HotSpringsExteriorToPath_PlayEvent
        return (0, "", "HotSpringsExteriorToPath")
    return None

label HotSpringsExteriorToPath_v2Base:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_HotSpringsExteriorEV005_PlaySound
    call TransferPlayer("Path", "HotSpringsExteriorEV005", 12, 0, direction=2) from _call_HotSpringsExteriorEV005_TransferPlayer
    $ resolve_scene()
    return False

label HotSpringsExteriorToPath_v2(play_event = True, trigger = None): # event
    if is_erased("HotSpringsExteriorToPath_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "HotSpringsExteriorToPath_v2Base", "HotSpringsExteriorToPath_v2") from _call_HotSpringsExteriorToPath_v2_PlayEvent
        return (0, "", "HotSpringsExteriorToPath_v2")
    return None

label HotSpringsExteriorToPath_v3Base:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_HotSpringsExteriorEV006_PlaySound
    call TransferPlayer("Path", "HotSpringsExteriorEV006", 13, 0, direction=2) from _call_HotSpringsExteriorEV006_TransferPlayer
    $ resolve_scene()
    return False

label HotSpringsExteriorToPath_v3(play_event = True, trigger = None): # event
    if is_erased("HotSpringsExteriorToPath_v3"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "HotSpringsExteriorToPath_v3Base", "HotSpringsExteriorToPath_v3") from _call_HotSpringsExteriorToPath_v3_PlayEvent
        return (0, "", "HotSpringsExteriorToPath_v3")
    return None

