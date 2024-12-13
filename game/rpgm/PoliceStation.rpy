label PoliceStationBG:
    $ set_transparency_backgrounds(["bg_police_station"])
    $ set_map_backgrounds(["map_police_station"])
    return

label PoliceStationStart:
    call PoliceStationBG from _call_PoliceStationBG
    stop music
    stop bgs
    return

label PoliceStationEnd:
    return

label PoliceStationNPCCaptain_0:
    PoliceCaptain "Welcome to the police station. This is where we do the paperwork"
    return False

label PoliceStationNPCCaptain_1:
    PoliceCaptain "We have a troublesome guy locked up, has been giving problems to the few women of the town, don't go near the cell"
    PoliceCaptain "The festival has everyone a little ... excited"
    return False

label PoliceStationNPCCaptain_2:
    PoliceCaptain "I imagine that I will not have to repeat that of ''not approaching the cell'', right?"
    return False

label PoliceStationNPCCaptain_3:
    if jail == 0:
        $ resolve_scene()
        PoliceCaptain "Need anything?"
    if jail == 1:
        PoliceCaptain "I imagine that I will not have to repeat that of ''not approaching the cell'', right?"
    $ resolve_scene()
    return False

label PoliceStationNPCCaptain(play_event = True, trigger = None): # event
    if is_erased("PoliceStationNPCCaptain"):
        return None
    elif trigger == "event" and switch("leyna_dream_end"):
        call PlayEvent(play_event, "PoliceStationNPCCaptain_3", "PoliceStationNPCCaptain") from _call_PoliceStationNPCCaptain_3_PlayEvent
        return (1, "", "PoliceStationNPCCaptain_3")
    elif trigger == "event" and jail >= 1:
        call PlayEvent(play_event, "PoliceStationNPCCaptain_2", "PoliceStationNPCCaptain") from _call_PoliceStationNPCCaptain_2_PlayEvent
        return (1, "", "PoliceStationNPCCaptain_2")
    elif trigger == "event" and switch("third_day"):
        call PlayEvent(play_event, "PoliceStationNPCCaptain_1", "PoliceStationNPCCaptain") from _call_PoliceStationNPCCaptain_1_PlayEvent
        return (1, "", "PoliceStationNPCCaptain_1")
    elif trigger == "event":
        call PlayEvent(play_event, "PoliceStationNPCCaptain_0", "PoliceStationNPCCaptain") from _call_PoliceStationNPCCaptain_0_PlayEvent
        return (1, "", "PoliceStationNPCCaptain_0")
    return None

label PoliceStationSorryYouCantBeHerePleaseGoToTheHallBase:
    Officer "Sorry, you can't be here. Please go to the hall"
    return False

label PoliceStationSorryYouCantBeHerePleaseGoToTheHall(play_event = True, trigger = None): # event
    if is_erased("PoliceStationSorryYouCantBeHerePleaseGoToTheHall"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "PoliceStationSorryYouCantBeHerePleaseGoToTheHallBase", "PoliceStationSorryYouCantBeHerePleaseGoToTheHall") from _call_PoliceStationSorryYouCantBeHerePleaseGoToTheHall_PlayEvent
        return (1, "", "PoliceStationSorryYouCantBeHerePleaseGoToTheHall")
    return None

label PoliceStationToTown_0:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_PoliceStationEV004_0_PlaySound
    call TransferPlayer("Town", "PoliceStationEV004_0", 3, 20, direction=2) from _call_PoliceStationEV004_0_TransferPlayer
    $ resolve_scene()
    return False

label PoliceStationToTown_1:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_PoliceStationEV004_1_PlaySound
    call TransferPlayer("Town2", "PoliceStationEV004_1", 4, 20, direction=2) from _call_PoliceStationEV004_1_TransferPlayer
    $ resolve_scene()
    return False

label PoliceStationToTown(play_event = True, trigger = None): # event
    if is_erased("PoliceStationToTown"):
        return None
    elif trigger == "event" and switch("third_day"):
        call PlayEvent(play_event, "PoliceStationToTown_1", "PoliceStationToTown") from _call_PoliceStationToTown_1_PlayEvent
        return (0, "", "PoliceStationToTown_1")
    elif trigger == "event":
        call PlayEvent(play_event, "PoliceStationToTown_0", "PoliceStationToTown") from _call_PoliceStationToTown_0_PlayEvent
        return (0, "", "PoliceStationToTown_0")
    return None

label PoliceStationToTown_v2_0:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_PoliceStationEV005_0_PlaySound
    call TransferPlayer("Town", "PoliceStationEV005_0", 5, 20, direction=2) from _call_PoliceStationEV005_0_TransferPlayer
    $ resolve_scene()
    return False

label PoliceStationToTown_v2_1:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_PoliceStationEV005_1_PlaySound
    call TransferPlayer("Town2", "PoliceStationEV005_1", 5, 20, direction=2) from _call_PoliceStationEV005_1_TransferPlayer
    $ resolve_scene()
    return False

label PoliceStationToTown_v2(play_event = True, trigger = None): # event
    if is_erased("PoliceStationToTown_v2"):
        return None
    elif trigger == "event" and switch("third_day"):
        call PlayEvent(play_event, "PoliceStationToTown_v2_1", "PoliceStationToTown_v2") from _call_PoliceStationToTown_v2_1_PlayEvent
        return (0, "", "PoliceStationToTown_v2_1")
    elif trigger == "event":
        call PlayEvent(play_event, "PoliceStationToTown_v2_0", "PoliceStationToTown_v2") from _call_PoliceStationToTown_v2_0_PlayEvent
        return (0, "", "PoliceStationToTown_v2_0")
    return None

label PoliceStationeventocomisaria_0:
    call ShowAnimation(1, "player", "PoliceStationeventocomisaria_0") from _call_PoliceStationeventocomisaria_0_ShowAnimation
    Leyna "Hey!!"
    call PlaySound("music", "audio/Dungeon1.ogg", volume=0.9, no_loop=False) from _call_PoliceStationeventocomisaria_0_PlaySound
    $ show_picture(1, "carcel1")
    $ resolve_scene()
    Johan "Leyna!"
    Johan "Somebody help us!!"
    $ show_picture(2, "carcel2")
    $ resolve_scene()
    Policeman "Shit... I told you not to go near the cell"
    Prisoner "What a fine woman you've brought me"
    Johan "Get away from my wife right now"
    Prisoner "I don't think so ... I haven't fucked a woman as pretty as you in years, darling"
    Prisoner "Let me see those tits"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_PoliceStationeventocomisaria_0_PlaySound_1
    $ show_picture(3, "carcel3")
    $ resolve_scene()
    Johan "YOU SON OF A BITCH LET HER GO!"
    Johan "Are you not going to do anything?"
    Policeman "Wait, as soon as we get the chance we'll release your wife"
    Prisoner "Are you getting horny with this, bitch?"
    Leyna "Please let me go!"
    Prisoner "Nah, let me touch your pussy and see if you're wet"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_PoliceStationeventocomisaria_0_PlaySound_2
    $ show_picture(4, "carcel4")
    $ resolve_scene()
    Leyna "NO! PLEASE!"
    Johan "STOP!"
    Policeman "(I have to stop it but ... what a good view!)"
    Prisoner "God damn! You're sexy as fuck, girl"
    Prisoner "Since you are showing me everything, let me show you mine"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_PoliceStationeventocomisaria_0_PlaySound_3
    $ show_picture(5, "carcel5")
    $ resolve_scene()
    Prisoner "You're very hot down there, can you really be getting horny with this? You are a whore!"
    Leyna "Shu-shut up!"
    Johan "!!!"
    Prisoner "I can't wait any longer, I have to fuck this pussy right now"
    Leyna "What?!"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_PoliceStationeventocomisaria_0_PlaySound_4
    $ show_picture(6, "carcel6")
    $ resolve_scene()
    Leyna "NO! STOP!"
    Prisoner "Almost there!"
    Policeman "NOW! Stop him!"
    Prisoner "Hm?"
    $ fade_out()
    stop music fadeout 1
    $ erase_picture(1)
    $ erase_picture(2)
    $ erase_picture(3)
    $ erase_picture(4)
    $ erase_picture(5)
    $ erase_picture(6)
    call TransferPlayer("PoliceStation", "PoliceStationeventocomisaria_0", 10, 10, direction=4) from _call_PoliceStationeventocomisaria_0_TransferPlayer
    call SetEventLocation("PoliceStationeventocomisaria_0", "PoliceStationNPCCaptain", 8, 10) from _call_PoliceStationeventocomisaria_0_setloc
    call SetEventLocation("PoliceStationeventocomisaria_0", "PoliceStationprisionero", 3, 9) from _call_PoliceStationeventocomisaria_0_setloc_1
    call SetEventLocation("PoliceStationeventocomisaria_0", "PoliceStationEV002", 3, 10) from _call_PoliceStationeventocomisaria_0_setloc_2
    $ fade_in()
    $ resolve_scene()
    call ShowAnimation(1, "PoliceStationprisionero", "PoliceStationeventocomisaria_0") from _call_PoliceStationeventocomisaria_0_ShowAnimation_1
    PoliceCaptain "My sincere apologies for this, but in this way you will learn that you should not get back to approach a prisoner"
    Johan "Are you talking seriously? something very serious could have happened, they should put better bars in the cell"
    Leyna "Johan... let's go"
    Johan "Yeah..."
    PoliceCaptain "(Douchebag...)"
    Johan "(Dickhead...)"
    $ fade_out()
    call SetEventLocation("PoliceStationeventocomisaria_0", "PoliceStationEV002", 11, 5) from _call_PoliceStationeventocomisaria_0_setloc_3
    call SetEventLocation("PoliceStationeventocomisaria_0", "PoliceStationNPCCaptain", 13, 7) from _call_PoliceStationeventocomisaria_0_setloc_4
    call TransferPlayer("Town2", "PoliceStationeventocomisaria_0", 4, 20, direction=2) from _call_PoliceStationeventocomisaria_0_TransferPlayer_1
    $ fade_in()
    call Movement("PoliceStationeventocomisaria_0", "player", ["D","D","TURN_U"]) from _call_PoliceStationeventocomisaria_0_Movement
    $ resolve_scene()
    Johan "Are you okay Leyna?"
    Leyna "I'm ... fine, still shaking a bit from what happened, but fine"
    $ corruption = corruption + 2
    $ jail = 1
    call GalleryViewed("carcel") from _call_PoliceStationeventocomisaria_0_GalleryViewed
    return False

label PoliceStationeventocomisaria(play_event = True, trigger = None): # event
    if is_erased("PoliceStationeventocomisaria"):
        return None
    elif switch("leyna_dream_end"):
        return None
    elif jail >= 1:
        return None
    elif trigger == "event" and switch("third_day"):
        call PlayEvent(play_event, "PoliceStationeventocomisaria_0", "PoliceStationeventocomisaria") from _call_PoliceStationeventocomisaria_0_PlayEvent
        return (0, "", "PoliceStationeventocomisaria_0")
    return None

