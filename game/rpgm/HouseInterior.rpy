label HouseInteriorBG:
    $ set_transparency_backgrounds(["bg_house"])
    $ set_map_backgrounds(["bg_house"])
    return

label HouseInteriorStart:
    call HouseInteriorBG from _call_HouseInteriorBG
    stop music
    stop bgs
    return

label HouseInteriorEnd:
    return

label HouseInteriorpersonacasa1_0:
    if not switch("leyna_alone"):
        $ resolve_scene()
        Kevin "My wife is cooking my favourite meal.. She cooks pretty bad, but I pretend it tastes delicious"
    if switch("leyna_alone"):
        Kevin "I see that you're interested in my house"
        "come back when my wife leaves and I can show it to you in private...  ..the house"
    $ resolve_scene()
    return False

label HouseInteriorpersonacasa1_1:
    Kevin "I see that you're interested in my house"
    "come back when my wife leaves and I can show it to you in private...  ..the house"
    return False

label HouseInteriorpersonacasa1(play_event = True, trigger = None): # event
    if is_erased("HouseInteriorpersonacasa1"):
        return None
    elif trigger == "event" and switch("leyna_alone"):
        call PlayEvent(play_event, "HouseInteriorpersonacasa1_1", "HouseInteriorpersonacasa1") from _call_HouseInteriorpersonacasa1_1_PlayEvent
        return (1, "", "HouseInteriorpersonacasa1_1")
    elif trigger == "event":
        call PlayEvent(play_event, "HouseInteriorpersonacasa1_0", "HouseInteriorpersonacasa1") from _call_HouseInteriorpersonacasa1_0_PlayEvent
        return (1, "", "HouseInteriorpersonacasa1_0")
    return None

label HouseInteriormujercasa1Base:
    if not switch("leyna_alone"):
        $ resolve_scene()
        Daniela "This bum can't do anything but eat, someday I'll poison him hehehe"
    if switch("leyna_alone"):
        Daniela "Have you seen the town already?"
    $ resolve_scene()
    return False

label HouseInteriormujercasa1(play_event = True, trigger = None): # event
    if is_erased("HouseInteriormujercasa1"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "HouseInteriormujercasa1Base", "HouseInteriormujercasa1") from _call_HouseInteriormujercasa1_PlayEvent
        return (1, "", "HouseInteriormujercasa1")
    return None

label HouseInteriorToTown_0:
    call TransferPlayer("Town", "HouseInteriorEV004_0", 12, 28, direction=2) from _call_HouseInteriorEV004_0_TransferPlayer
    $ resolve_scene()
    return False

label HouseInteriorToTown_1:
    call TransferPlayer("Town2", "HouseInteriorEV004_1", 12, 28, direction=2) from _call_HouseInteriorEV004_1_TransferPlayer
    $ resolve_scene()
    return False

label HouseInteriorToTown(play_event = True, trigger = None): # event
    if is_erased("HouseInteriorToTown"):
        return None
    elif trigger == "event" and switch("third_day"):
        call PlayEvent(play_event, "HouseInteriorToTown_1", "HouseInteriorToTown") from _call_HouseInteriorToTown_1_PlayEvent
        return (0, "", "HouseInteriorToTown_1")
    elif trigger == "event":
        call PlayEvent(play_event, "HouseInteriorToTown_0", "HouseInteriorToTown") from _call_HouseInteriorToTown_0_PlayEvent
        return (0, "", "HouseInteriorToTown_0")
    return None

