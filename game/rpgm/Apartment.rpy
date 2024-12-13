label ApartmentBG:
    $ set_transparency_backgrounds(["bg_apartment","darkbg"])
    $ set_map_backgrounds(["map_apartment"])
    return

label ApartmentStart:
    call ApartmentBG from _call_ApartmentBG
    stop music
    stop bgs
    return

label ApartmentEnd:
    return

label ApartmentNPCMUJER_0:
    Johan "Hi cutie"
    $ resolve_scene()
    Leyna "Good morning. Check the email, I heard a notification"
    $ set_switch("introduction", True)
    return False

label ApartmentNPCMUJER_1:
    Leyna "aren't you going to check the mail?"
    return False

label ApartmentNPCMUJER(play_event = True, trigger = None): # event
    if is_erased("ApartmentNPCMUJER"):
        return None
    elif trigger == "event" and switch("introduction"):
        call PlayEvent(play_event, "ApartmentNPCMUJER_1", "ApartmentNPCMUJER") from _call_ApartmentNPCMUJER_1_PlayEvent
        return (1, "", "ApartmentNPCMUJER_1")
    elif trigger == "event":
        call PlayEvent(play_event, "ApartmentNPCMUJER_0", "ApartmentNPCMUJER") from _call_ApartmentNPCMUJER_0_PlayEvent
        return (1, "", "ApartmentNPCMUJER_0")
    return None

label ApartmentORDENADORBase:
    "You have a new message !"
    $ resolve_scene()
    Johan "oh this is perfect!"
    call Movement("ApartmentORDENADOR", "ApartmentNPCMUJER", ["L","L","L","L","L"]) from _call_ApartmentORDENADOR_Movement
    $ resolve_scene()
    Leyna "What is it?"
    Johan "Honey, I think this is a good idea for the article."
    $ show_transparent(1, "expresion_neutral_mujer", width=1600, height=900)
    $ resolve_scene()
    "It's a small town lost in the mountains, very traditional, with ancient festivities that take place in the summer"
    "We could go and make an article about it."
    $ erase_picture(1)
    $ show_transparent(2, "expresion_ilusion_mujer", width=1600, height=900)
    $ resolve_scene()
    Leyna "Great! We could enjoy and relax a little, it's been a long time since we took a vacation."
    $ erase_picture(2)
    call Movement("ApartmentORDENADOR", "player", ["TURN_R"]) from _call_ApartmentORDENADOR_Movement_1
    $ resolve_scene()
    Johan "Yeah, they have hot springs, a beautiful river and they all seem very rustic and friendly"
    "We'll have a great time while we work"
    $ resolve_scene()
    Leyna "It seems that the food is great, country food, I can't wait"
    Johan "Well then, it's decided! Pack your bags while I book a room in the village hostel."
    call Movement("ApartmentORDENADOR", "player", ["TURN_U"]) from _call_ApartmentORDENADOR_Movement_2
    call Movement("ApartmentORDENADOR", "ApartmentNPCMUJER", ["D","D","D","D","D","L","L","L","L","L","L","L","U","U","U","U","U"]) from _call_ApartmentORDENADOR_Movement_3
    stop music fadeout 1
    $ set_switch("introduction", False)
    call TransferPlayer("TownEntrance", "ApartmentORDENADOR", 3, 5, direction=2) from _call_ApartmentORDENADOR_TransferPlayer
    $ resolve_scene()
    return False

label ApartmentORDENADOR(play_event = True, trigger = None): # event
    if is_erased("ApartmentORDENADOR"):
        return None
    elif trigger == "event" and switch("introduction"):
        call PlayEvent(play_event, "ApartmentORDENADORBase", "ApartmentORDENADOR") from _call_ApartmentORDENADOR_PlayEvent
        return (1, "", "ApartmentORDENADOR")
    return None

label ApartmenttelevisionBase:
    "There's only trash on TV. I guess that's why we only watch Netflix "
    return False

label Apartmenttelevision(play_event = True, trigger = None): # event
    if is_erased("Apartmenttelevision"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "ApartmenttelevisionBase", "Apartmenttelevision") from _call_Apartmenttelevision_PlayEvent
        return (1, "", "Apartmenttelevision")
    return None

label ApartmentarmarioBase:
    "Hmmm. I need new clothes."
    return False

label Apartmentarmario(play_event = True, trigger = None): # event
    if is_erased("Apartmentarmario"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "ApartmentarmarioBase", "Apartmentarmario") from _call_Apartmentarmario_PlayEvent
        return (1, "", "Apartmentarmario")
    return None

label ApartmentlavaboBase:
    call PlaySound("sound", "audio/Liquid.ogg", volume=0.9, no_loop=True) from _call_Apartmentlavabo_PlaySound
    $ resolve_scene()
    return False

label Apartmentlavabo(play_event = True, trigger = None): # event
    if is_erased("Apartmentlavabo"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "ApartmentlavaboBase", "Apartmentlavabo") from _call_Apartmentlavabo_PlayEvent
        return (1, "", "Apartmentlavabo")
    return None

label Apartmentpuerta_0:
    "Wait. I have to talk to my wife"
    call Movement("Apartmentpuerta_0", "player", ["TURN_U","U"]) from _call_Apartmentpuerta_0_Movement
    $ resolve_scene()
    return False

label Apartmentpuerta_1:
    " Wait. I have to look the new mail"
    call Movement("Apartmentpuerta_1", "player", ["TURN_U","U"]) from _call_Apartmentpuerta_1_Movement
    $ resolve_scene()
    return False

label Apartmentpuerta(play_event = True, trigger = None): # event
    if is_erased("Apartmentpuerta"):
        return None
    elif trigger == "event" and switch("introduction"):
        call PlayEvent(play_event, "Apartmentpuerta_1", "Apartmentpuerta") from _call_Apartmentpuerta_1_PlayEvent
        return (0, "", "Apartmentpuerta_1")
    elif trigger == "event":
        call PlayEvent(play_event, "Apartmentpuerta_0", "Apartmentpuerta") from _call_Apartmentpuerta_0_PlayEvent
        return (0, "", "Apartmentpuerta_0")
    return None

label ApartmentmusicapisoBase:
    call PlaySound("music", "audio/Ship1.ogg", volume=0.9, no_loop=False) from _call_Apartmentmusicapiso_PlaySound
    $ resolve_scene()
    return False

label Apartmentmusicapiso(play_event = True, trigger = None): # parallel
    if is_erased("Apartmentmusicapiso"):
        return None
    elif trigger == "parallel":
        call PlayEvent(play_event, "ApartmentmusicapisoBase", "Apartmentmusicapiso") from _call_Apartmentmusicapiso_PlayEvent
        return (0, "", "Apartmentmusicapiso")
    return None

