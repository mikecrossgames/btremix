label InnNightBG:
    $ set_transparency_backgrounds(["bg_inn"])
    $ set_map_backgrounds(["map_inn_night"])
    return

label InnNightStart:
    call InnNightBG from _call_InnNightBG
    stop music
    stop bgs
    return

label InnNightEnd:
    return

label InnNightToInnRoomsNightBase:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_InnNightEV001_PlaySound
    call TransferPlayer("InnRoomsNight", "InnNightEV001", 6, 18, direction=8) from _call_InnNightEV001_TransferPlayer
    $ resolve_scene()
    return False

label InnNightToInnRoomsNight(play_event = True, trigger = None): # event
    if is_erased("InnNightToInnRoomsNight"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnNightToInnRoomsNightBase", "InnNightToInnRoomsNight") from _call_InnNightToInnRoomsNight_PlayEvent
        return (0, "", "InnNightToInnRoomsNight")
    return None

label InnNightToInnRoomsNight_v2Base:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_InnNightEV002_PlaySound
    call TransferPlayer("InnRoomsNight", "InnNightEV002", 7, 18, direction=8) from _call_InnNightEV002_TransferPlayer
    $ resolve_scene()
    return False

label InnNightToInnRoomsNight_v2(play_event = True, trigger = None): # event
    if is_erased("InnNightToInnRoomsNight_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnNightToInnRoomsNight_v2Base", "InnNightToInnRoomsNight_v2") from _call_InnNightToInnRoomsNight_v2_PlayEvent
        return (0, "", "InnNightToInnRoomsNight_v2")
    return None

label InnNightToTownNightBase:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_InnNightEV006_PlaySound
    call TransferPlayer("TownNight", "InnNightEV006", 28, 21, direction=2) from _call_InnNightEV006_TransferPlayer
    $ resolve_scene()
    return False

label InnNightToTownNight(play_event = True, trigger = None): # event
    if is_erased("InnNightToTownNight"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnNightToTownNightBase", "InnNightToTownNight") from _call_InnNightToTownNight_PlayEvent
        return (0, "", "InnNightToTownNight")
    return None

label InnNightSleepBase:
    call Movement("InnNightSleep", "player", ["U","U","TURN_D"]) from _call_InnNightSleep_Movement
    $ resolve_scene()
    Johan "I'm exhausted, what a day. Let's go to sleep, shall we?"
    Leyna "Yes, I'm also... exhausted"
    $ fade_out()
    $ show_picture(1, "pantallanegro", scale=(110, 110), width=816, height=600)
    $ fade_in()
    $ resolve_scene()
    "They are both asleep, but Leyna is tossing and turning. She seems to be dreaming something intense"
    if switch("massage_masturbation"):
        $ show_picture(2, "masage6")
        $ resolve_scene()
        Leyna "Here again?. I thought we had gone to the inn"
        Leyna "I feel so... warm"
        pause
        $ show_picture(3, "masage8")
        $ resolve_scene()
        Leyna "yes, right there... that's where I have all the tension (I feel like I'm melting, I just want him to keep touching me more and more)"
        pause
        $ show_picture(4, "masage10")
        $ resolve_scene()
        Leyna "(if I wasn't married...) hmmmm"
        pause
        $ show_picture(5, "masage11")
        $ resolve_scene()
        Leyna "(Just thinking about it, I find it hard to control myself...)"
        Leyna "(I need to alleviate this feeling, before it gets out of control, for sure he doesn't realize)"
        pause
        $ show_picture(6, "masagefruta1")
        $ resolve_scene()
        Leyna "Hmmm oh my god..."
        Leyna "(It will only take a second... all these days, with all the villagers looking at me... wanting me...)"
        Leyna "Oh?"
        pause
        $ show_picture(7, "masagefruta3")
        $ resolve_scene()
        Leyna "(He... is rubbing me with his ...?"
        pause
        $ show_picture(8, "masagefruta4")
        $ resolve_scene()
        Leyna "(it feels so good... I can't stop now) Ple-please..."
        Leyna "Do it please... Fuck me"
        pause
        $ show_picture(9, "masagefruta7")
        $ resolve_scene()
        Villager "Do you want it? Do you want me to fuck you right here?"
        Leyna "Ahh... YES PLEASE"
        Villager "As you wish"
        pause
        $ show_picture(10, "masagefruta8")
        $ resolve_scene()
        Leyna "FUUUUCK!!! OH MY GOD!!"
        Villager "oh wow, this pussy is amazing!!"
        pause
        $ show_picture(11, "masagefruta9")
        call PlaySound("music", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_InnNightSleep_PlaySound
        $ resolve_scene()
        Leyna "OOOH YEAH! JOHAN DOESN'T GET THERE! FUCK ME HARDER!"
        Villager "I'M GONNA CUM!"
        Leyna "WAIT!"
        pause
        stop music fadeout 1
    if switch("massage_sex"):
        $ show_picture(8, "masagefruta4")
        $ resolve_scene()
        Leyna "(Why am I here again? I didn't want to come back in... what I did wasn't right...)"
        Leyna "(He is... again, and I can't control myself)"
        pause
        $ show_picture(9, "masagefruta7")
        $ resolve_scene()
        Leyna "(But I... am in love with Johan... But this man is so... great)"
        Leyna "Please... stop, i love my husband"
        Villager "Your body says otherwise"
        Leyna "I..."
        pause
        $ show_picture(10, "masagefruta8")
        $ resolve_scene()
        Villager "Come here I will make you feel like never before"
        Leyna "(I can't take it anymore, I'm too horny...)"
        Leyna "Fuck... Fuck me"
        pause
        $ show_picture(11, "masagefruta9")
        call PlaySound("music", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_InnNightSleep_PlaySound_1
        $ resolve_scene()
        Villager "Your pussy feels amazing! It's so tight!"
        Leyna "FUCK ME! OH MY GOD! I'M MELTING"
        Villager "I knew you were a whore from the moment you walked in"
        Leyna "YES! YES! YES!"
        pause
        $ show_picture(12, "sue_oleyna1")
        $ resolve_scene()
        Johan "Leyna? Wh---what is this!!!???"
        stop music fadeout 1
        pause
        $ show_picture(13, "sue_oleyna2")
        $ resolve_scene()
        Johan "WHAT THE HELL IS THIS? HOW COULD YOU DO THIS TO ME, LEYNA?"
        Leyna "JOHAN?"
        pause
        $ show_picture(14, "sue_oleyna3")
        $ resolve_scene()
        Leyna "No Johan I'm sorry! Don't leave, wait..."
        pause
        $ show_picture(15, "sue_oleyna4")
        $ resolve_scene()
        Leyna "What have I done? Why did all this have to happen?"
        Villager "Well... shall we continue?..."
        pause
    $ show_picture(16, "pantallanegro", scale=(110, 110), width=816, height=600)
    $ resolve_scene()
    Leyna "AH! It was a dream?..."
    Leyna "damn massage, it's going to haunt me for all vacations"
    Leyna "Johan can't notice anything strange... it won't happen again"
    $ fade_out()
    $ erase_picture(1)
    $ erase_picture(2)
    $ erase_picture(3)
    $ erase_picture(4)
    $ erase_picture(5)
    $ erase_picture(6)
    $ erase_picture(7)
    $ erase_picture(8)
    $ erase_picture(9)
    $ erase_picture(10)
    $ erase_picture(11)
    $ erase_picture(12)
    $ erase_picture(13)
    $ erase_picture(14)
    $ erase_picture(15)
    $ erase_picture(16)
    $ set_switch("leyna_dream_end", True)
    call GalleryViewed("sue_oleyna") from _call_InnNightSleep_GalleryViewed
    call TransferPlayer("Town2", "InnNightSleep", 28, 22, direction=2) from _call_InnNightSleep_TransferPlayer
    $ fade_in()
    call Movement("InnNightSleep", "player", ["D","D","TURN_U"]) from _call_InnNightSleep_Movement_1
    $ resolve_scene()
    call PauseForBalloon("InnNightSleep") from _call_InnNightSleep_PauseForBalloon
    Johan "Leyna, what's wrong? You look bad... you didn't sleep well?"
    Leyna "I... what? I have slept well, I'm just a little worried... vacations are taking too long, don't you think?"
    Johan "Yes, the other day I was thinking about this... I think it would be a good idea to try to find some part-time job"
    Johan "While I work on the report, to cover expenses I'm sure the merchants have some jobe for you"
    Leyna "... Yes, that would be nice (so I can occupy my mind in other things...)"
    Johan "Well, I have to go today to send some pictures, see you later"
    Leyna "Okay, I guess I'll start asking around at the grocery store"
    $ fade_out()
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_InnNightSleep_PlaySound_2
    call ChangePartyMember("Johan", False) from _call_InnNightSleep_ChangePartyMember
    $ fade_in()
    $ resolve_scene()
    Leyna "Well, let's go to the food store (Maybe I should talk to the photographer too... but I'm not sure I want to follow that path..)"
    $ leyna_work = 1
    return False

label InnNightSleep(play_event = True, trigger = None): # autorun
    if is_erased("InnNightSleep"):
        return None
    elif trigger == "autorun" and switch("lucky_person"):
        call PlayEvent(play_event, "InnNightSleepBase", "InnNightSleep") from _call_InnNightSleep_PlayEvent
        return (0, "", "InnNightSleep")
    return None

label InnNightmusicaposadaBase:
    $ tint_screen((-68, -68, 0, 68), 60, True)
    call PlaySound("music", "audio/Ship1.ogg", volume=0.9, no_loop=False) from _call_InnNightmusicaposada_PlaySound
    return False

label InnNightmusicaposada(play_event = True, trigger = None): # parallel
    if is_erased("InnNightmusicaposada"):
        return None
    elif trigger == "parallel":
        call PlayEvent(play_event, "InnNightmusicaposadaBase", "InnNightmusicaposada") from _call_InnNightmusicaposada_PlayEvent
        return (0, "", "InnNightmusicaposada")
    return None

label InnNightpapelesposadaBase:
    "( Someone has left is rent papers)"
    return False

label InnNightpapelesposada(play_event = True, trigger = None): # event
    if is_erased("InnNightpapelesposada"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnNightpapelesposadaBase", "InnNightpapelesposada") from _call_InnNightpapelesposada_PlayEvent
        return (1, "", "InnNightpapelesposada")
    return None

label InnNightpanBase:
    "(hmmm it smells really good)"
    return False

label InnNightpan(play_event = True, trigger = None): # event
    if is_erased("InnNightpan"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnNightpanBase", "InnNightpan") from _call_InnNightpan_PlayEvent
        return (0, "", "InnNightpan")
    return None

label InnNightentradaalaposadanoche_0:
    call Movement("InnNightentradaalaposadanoche_0", "player", ["U","U"]) from _call_InnNightentradaalaposadanoche_0_Movement
    call Movement("InnNightentradaalaposadanoche_0", "InnNightjohan", ["TURN_D"]) from _call_InnNightentradaalaposadanoche_0_Movement_1
    $ resolve_scene()
    call PauseForBalloon("InnNightentradaalaposadanoche_0") from _call_InnNightentradaalaposadanoche_0_PauseForBalloon
    Johan "Leyna! I was starting to worry, you took a long time to come back"
    call Movement("InnNightentradaalaposadanoche_0", "InnNightjohan", ["D","D","R","R","R","R","TURN_D"]) from _call_InnNightentradaalaposadanoche_0_Movement_2
    $ resolve_scene()
    Johan "Are you okay? You seem a little nervous.."
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Nervous? No, I'm fine... But let's spend the day together tomorrow, okay?"
    Johan "Of course, we'll go to the festival site to see if they can let us in"
    $ erase_picture(1)
    $ show_transparent(1, "plano_mujer_sonrisa", width=1600, height=900)
    $ resolve_scene()
    Leyna "Great"
    $ erase_picture(1)
    $ fade_out()
    call ChangePartyMember("Johan", True) from _call_InnNightentradaalaposadanoche_0_ChangePartyMember
    call TransferPlayer("InnRooms", "InnNightentradaalaposadanoche_0", 13, 10, direction=2) from _call_InnNightentradaalaposadanoche_0_TransferPlayer
    $ fade_in()
    $ resolve_scene()
    $ tint_screen((0, 0, 0, 0), 60, True)
    "THE NEXT MORNING"
    "You can choose between exploring the town by day or by night. Just go to bed and choose"
    $ set_switch("third_day", True)
    call Movement("InnNightentradaalaposadanoche_0", "player", ["D","L"]) from _call_InnNightentradaalaposadanoche_0_Movement_3
    $ set_switch("leyna_alone", False)
    $ resolve_scene()
    return False

label InnNightentradaalaposadanoche(play_event = True, trigger = None): # autorun
    if is_erased("InnNightentradaalaposadanoche"):
        return None
    elif switch("third_day"):
        return None
    elif trigger == "autorun":
        call PlayEvent(play_event, "InnNightentradaalaposadanoche_0", "InnNightentradaalaposadanoche") from _call_InnNightentradaalaposadanoche_0_PlayEvent
        return (0, "", "InnNightentradaalaposadanoche_0")
    return None

