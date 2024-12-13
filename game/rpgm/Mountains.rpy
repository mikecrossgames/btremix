label MountainsBG:
    $ set_transparency_backgrounds(["map_mountain"])
    $ set_map_backgrounds(["map_mountain"])
    return

label MountainsStart:
    call MountainsBG from _call_MountainsBG
    stop music
    stop bgs
    return

label MountainsEnd:
    return

label MountainsWowThisPlaceIsBeautiful_0(menu_choice = None):
    call Movement("MountainsEV002_0", "player", ["L","L","L","L","L","L","L"]) from _call_MountainsEV002_0_Movement
    $ set_switch("fruit_event", True)
    $ resolve_scene()
    Leyna "Wow! This place is beautiful"
    Worker "Hahaha, has its charm, right? Here are the fruits that I commented to you, I've already taken some"
    Worker "Do you want to try one? It will cheer you up for the rest of the day!"
    "WARNING! Consuming this fruit can cause certain '' side effects ''. Some scenes will be different if you try the fruit!"
    call GetChoice([_("Take the fruit"), _("Don't take it")], value=menu_choice, called_from="MountainsEV002_0") from _call_MountainsEV002_0_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Take the fruit"):
        $ menu_choice = None
        $ resolve_scene()
        Johan "There's no problem for me! What do you think, Leyna?"
        Leyna "Of course! No problem"
        Worker "Great, let's get back now, we're late!"
        Johan "Okay"
        $ set_switch("ate_the_fruit", True)
    elif menu_choice == _("Don't take it"):
        $ menu_choice = None
        $ set_switch("ate_the_fruit", False)
        Leyna "I don't know..."
        Worker "Hey! Don't worry, it's up to you"
        Leyna "I prefer not to take it"
        Worker "Great, let's get back now, we're late!"
    call TransferPlayer("Festival", "MountainsEV002_0", 0, 12, direction=6) from _call_MountainsEV002_0_TransferPlayer
    $ resolve_scene()
    return False

label MountainsWowThisPlaceIsBeautiful(play_event = True, trigger = None): # autorun
    if is_erased("MountainsWowThisPlaceIsBeautiful"):
        return None
    elif switch("fruit_event"):
        return None
    elif trigger == "autorun":
        call PlayEvent(play_event, "MountainsWowThisPlaceIsBeautiful_0", "MountainsWowThisPlaceIsBeautiful") from _call_MountainsWowThisPlaceIsBeautiful_0_PlayEvent
        return (0, "", "MountainsWowThisPlaceIsBeautiful_0")
    return None

label MountainsYouWonANewObject_0:
    call PlaySound("sound", "audio/Recovery.ogg", volume=0.9, no_loop=True) from _call_MountainsEV003_0_PlaySound
    $ resolve_scene()
    $ set_item("flowers", True)
    "(YOU WON A NEW OBJECT)"
    $ leyna_work = 5
    return False

label MountainsYouWonANewObject(play_event = True, trigger = None): # event
    if is_erased("MountainsYouWonANewObject"):
        return None
    elif leyna_work >= 5:
        return None
    elif trigger == "event" and leyna_work >= 4:
        call PlayEvent(play_event, "MountainsYouWonANewObject_0", "MountainsYouWonANewObject") from _call_MountainsYouWonANewObject_0_PlayEvent
        return (1, "", "MountainsYouWonANewObject_0")
    return None

label MountainsYouWonANewObject_v2_0:
    call PlaySound("sound", "audio/Recovery.ogg", volume=0.9, no_loop=True) from _call_MountainsEV004_0_PlaySound
    $ resolve_scene()
    $ set_item("flowers", True)
    "(YOU WON A NEW OBJECT)"
    $ leyna_work = 6
    return False

label MountainsYouWonANewObject_v2(play_event = True, trigger = None): # event
    if is_erased("MountainsYouWonANewObject_v2"):
        return None
    elif leyna_work >= 6:
        return None
    elif trigger == "event" and leyna_work >= 5:
        call PlayEvent(play_event, "MountainsYouWonANewObject_v2_0", "MountainsYouWonANewObject_v2") from _call_MountainsYouWonANewObject_v2_0_PlayEvent
        return (1, "", "MountainsYouWonANewObject_v2_0")
    return None

label MountainsYouWonANewObject_v3_0:
    call PlaySound("sound", "audio/Recovery.ogg", volume=0.9, no_loop=True) from _call_MountainsEV005_0_PlaySound
    $ resolve_scene()
    $ set_item("flowers", True)
    "(YOU WON A NEW OBJECT)"
    $ leyna_work = 7
    return False

label MountainsYouWonANewObject_v3(play_event = True, trigger = None): # event
    if is_erased("MountainsYouWonANewObject_v3"):
        return None
    elif leyna_work >= 7:
        return None
    elif trigger == "event" and leyna_work >= 6:
        call PlayEvent(play_event, "MountainsYouWonANewObject_v3_0", "MountainsYouWonANewObject_v3") from _call_MountainsYouWonANewObject_v3_0_PlayEvent
        return (1, "", "MountainsYouWonANewObject_v3_0")
    return None

label MountainsYouWonANewObject_v4_0:
    call PlaySound("sound", "audio/Recovery.ogg", volume=0.9, no_loop=True) from _call_MountainsEV006_0_PlaySound
    $ resolve_scene()
    $ set_item("flowers", True)
    "(YOU WON A NEW OBJECT)"
    $ leyna_work = 8
    Leyna "Well, I already have all the flowers... I should go the hotsprings to start the job as soon as possible"
    $ fade_out()
    call TransferPlayer("Path", "MountainsEV006_0", 2, 10, direction=6) from _call_MountainsEV006_0_TransferPlayer
    $ fade_in()
    $ resolve_scene()
    return False

label MountainsYouWonANewObject_v4(play_event = True, trigger = None): # event
    if is_erased("MountainsYouWonANewObject_v4"):
        return None
    elif leyna_work >= 8:
        return None
    elif trigger == "event" and leyna_work >= 7:
        call PlayEvent(play_event, "MountainsYouWonANewObject_v4_0", "MountainsYouWonANewObject_v4") from _call_MountainsYouWonANewObject_v4_0_PlayEvent
        return (1, "", "MountainsYouWonANewObject_v4_0")
    return None

