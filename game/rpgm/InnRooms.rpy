label InnRoomsBG:
    $ set_transparency_backgrounds(["bg_inn_rooms"])
    $ set_map_backgrounds(["map_inn_rooms"])
    return

label InnRoomsStart:
    call InnRoomsBG from _call_InnRoomsBG
    stop music
    stop bgs
    return

label InnRoomsEnd:
    return

label InnRoomsDEJANDOlasmaletas_0:
    Johan "Well this is the room ... it's a little small but it has its charm."
    Leyna "I love it!. let's leave our things and go for a walk."
    $ fade_out()
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_InnRoomsDEJANDOlasmaletas_0_PlaySound
    $ fade_in()
    $ suitcases = 1
    $ set_switch("suitcases", True)
    $ resolve_scene()
    return False

label InnRoomsDEJANDOlasmaletas(play_event = True, trigger = None): # event
    if is_erased("InnRoomsDEJANDOlasmaletas"):
        return None
    elif switch("inn_departure"):
        return None
    elif switch("suitcases"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnRoomsDEJANDOlasmaletas_0", "InnRoomsDEJANDOlasmaletas") from _call_InnRoomsDEJANDOlasmaletas_0_PlayEvent
        return (0, "", "InnRoomsDEJANDOlasmaletas_0")
    return None

label InnRoomsDEJANDOlasmaletas_v2_0:
    Johan "Well this is the room ... it's a little small but it has its charm."
    Leyna "I love it!. let's leave our things and go for a walk."
    $ fade_out()
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_InnRoomsDEJANDOlasmaletas_v2_0_PlaySound
    $ fade_in()
    $ suitcases = 1
    $ set_switch("suitcases", True)
    $ resolve_scene()
    return False

label InnRoomsDEJANDOlasmaletas_v2(play_event = True, trigger = None): # event
    if is_erased("InnRoomsDEJANDOlasmaletas_v2"):
        return None
    elif switch("inn_departure"):
        return None
    elif switch("suitcases"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnRoomsDEJANDOlasmaletas_v2_0", "InnRoomsDEJANDOlasmaletas_v2") from _call_InnRoomsDEJANDOlasmaletas_v2_0_PlayEvent
        return (0, "", "InnRoomsDEJANDOlasmaletas_v2_0")
    return None

label InnRoomsnioBase:
    Boy "What are you doing in my room?"
    return False

label InnRoomsnio(play_event = True, trigger = None): # event
    if is_erased("InnRoomsnio"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnRoomsnioBase", "InnRoomsnio") from _call_InnRoomsnio_PlayEvent
        return (1, "", "InnRoomsnio")
    return None

label InnRoomsToInnBase:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_InnRoomsEV004_PlaySound
    call TransferPlayer("Inn", "InnRoomsEV004", 1, 0, direction=2) from _call_InnRoomsEV004_TransferPlayer
    $ resolve_scene()
    return False

label InnRoomsToInn(play_event = True, trigger = None): # event
    if is_erased("InnRoomsToInn"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnRoomsToInnBase", "InnRoomsToInn") from _call_InnRoomsToInn_PlayEvent
        return (0, "", "InnRoomsToInn")
    return None

label InnRoomsToInn_v2Base:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_InnRoomsEV005_PlaySound
    call TransferPlayer("Inn", "InnRoomsEV005", 1, 0, direction=2) from _call_InnRoomsEV005_TransferPlayer
    $ resolve_scene()
    return False

label InnRoomsToInn_v2(play_event = True, trigger = None): # event
    if is_erased("InnRoomsToInn_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnRoomsToInn_v2Base", "InnRoomsToInn_v2") from _call_InnRoomsToInn_v2_PlayEvent
        return (0, "", "InnRoomsToInn_v2")
    return None

label InnRoomspersonabaoBase:
    Tourist "I always stay here when I come to the festival"
    return False

label InnRoomspersonabao(play_event = True, trigger = None): # event
    if is_erased("InnRoomspersonabao"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnRoomspersonabaoBase", "InnRoomspersonabao") from _call_InnRoomspersonabao_PlayEvent
        return (1, "", "InnRoomspersonabao")
    return None

label InnRoomsIchaIchaParadiseAuthorJiraiyaBase(menu_choice = None):
    "ICHA ICHA PARADISE - AUTHOR: JIRAIYA"
    "Do you want to read it?"
    call GetChoice([_("Yes"), _("No")], value=menu_choice, called_from="InnRoomsEV007") from _call_InnRoomsEV007_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Yes"):
        $ menu_choice = None
        $ show_picture(1, "menofculture")
        $ resolve_scene()
        pause
    elif menu_choice == _("No"):
        $ menu_choice = None
        $ show_picture(2, "jiraiya")
        $ resolve_scene()
        pause
    $ erase_picture(1)
    $ erase_picture(2)
    $ resolve_scene()
    return False

label InnRoomsIchaIchaParadiseAuthorJiraiya(play_event = True, trigger = None): # event
    if is_erased("InnRoomsIchaIchaParadiseAuthorJiraiya"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnRoomsIchaIchaParadiseAuthorJiraiyaBase", "InnRoomsIchaIchaParadiseAuthorJiraiya") from _call_InnRoomsIchaIchaParadiseAuthorJiraiya_PlayEvent
        return (1, "", "InnRoomsIchaIchaParadiseAuthorJiraiya")
    return None

label InnRoomsSleep_0(menu_choice = None):
    "Do you want to wait until night?"
    call GetChoice([_("Yes"), _("No")], value=menu_choice, called_from="InnRoomsSleep_0") from _call_InnRoomsSleep_0_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Yes"):
        $ menu_choice = None
        $ fade_out()
        if not renpy.in_rollback():
            $ _saved_bgm = renpy.music.get_playing()
        play music "audio/Inn.ogg" volume 0.9 noloop
        if _saved_bgm is not None and not renpy.in_rollback():
            queue music _saved_bgm
            $ _saved_bgm = None
        call TransferPlayer("InnRoomsNight", "InnRoomsSleep_0", 11, 11, direction=2) from _call_InnRoomsSleep_0_TransferPlayer
        $ resolve_scene()
        $ tint_screen((-68, -68, 0, 68), 60, True)
        $ fade_in()
    elif menu_choice == _("No"):
        $ menu_choice = None
    $ resolve_scene()
    return False

label InnRoomsSleep(play_event = True, trigger = None): # event
    if is_erased("InnRoomsSleep"):
        return None
    elif switch("leyna_dream_end"):
        return None
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "InnRoomsSleep_0", "InnRoomsSleep") from _call_InnRoomsSleep_0_PlayEvent
        return (1, "", "InnRoomsSleep_0")
    return None

label InnRoomssueojohan_0:
    call Movement("InnRoomssueojohan_0", "player", ["U","R","R","R","R","U","U","U","U","U","TURN_D"]) from _call_InnRoomssueojohan_0_Movement
    $ resolve_scene()
    Leyna "Time to sleep"
    Johan "Yes, I'm exhausted"
    $ fade_out()
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_InnRoomssueojohan_0_PlaySound
    pause 0.6
    call PlaySound("music", "audio/Dungeon1.ogg", volume=0.9, no_loop=False) from _call_InnRoomssueojohan_0_PlaySound_1
    Johan "(Hmmm... What's this? I feel... strange)"
    if switch("johan_silent"):
        $ show_picture(1, "publico14")
        $ fade_in()
        $ resolve_scene()
        Johan "Oh no.. this again?"
        pause
        $ show_picture(2, "publico16")
        $ resolve_scene()
        Johan "(S-stop!... Shit! I can't move or speak)"
        Johan "(What the hell do you think you're doing to my wife?)"
        pause
        $ erase_picture(1)
        $ erase_picture(2)
    if switch("johan_intervened"):
        $ show_picture(1, "publico13")
        $ fade_in()
        $ resolve_scene()
        Johan "Oh no.. this again?"
        Johan "(Why are you looking at my wife like this?)"
        $ show_picture(2, "publico16")
        $ resolve_scene()
        Johan "(Hey! What the hell are you doing with my wife?)"
        Johan "(S-stop!... Shit! I can't move or speak)"
        pause
        $ erase_picture(1)
        $ erase_picture(2)
    $ show_picture(1, "sue_o1")
    $ resolve_scene()
    OldMan "Yeah, that position is perfect!"
    Johan "(Perfect?!, stop touching her!)"
    Villager1 "I have an idea! Did you want risque photos right? Well, look"
    $ show_picture(2, "sue_o2")
    $ resolve_scene()
    OldMan "Yeah! Great work guys!"
    Johan "(No! Stop!)"
    Villager2 "Shit! Look at those tits, they're perfect!"
    Villager1 "Yeah! Fuck this I can't hold it anymore"
    $ show_picture(3, "sue_o3")
    $ resolve_scene()
    Johan "(They have taken out their cocks! Leyna, Leyna say something!)"
    Villager1 "What do you think honey, you like what you see?"
    Leyna "They're ... they're huge"
    Villager2 "Seems she is enjoying it. Hey photographer! Take a picture of this, surely the magazine will love it"
    pause
    $ show_picture(4, "sue_o4")
    $ resolve_scene()
    OldMan "Yes!"
    Villager2 "It seems that you are wet down there precious"
    Leyna "Wha-What are you going to do?"
    Villager2 "Shhhh, quiet. Just enjoy bitch"
    pause
    $ show_picture(5, "sue_o6")
    $ resolve_scene()
    Johan "(He is fucking her! Stop!... Why?... Why I feel like this? I'm getting hard)"
    Leyna "OOoohh it's sooo big!"
    Villager2 "Just say it bitch! Say \"fuck me\""
    Leyna "I.. I... fuck me"
    Villager2 "What?"
    Leyna "Fuck me please"
    Villager2 "Okey!"
    $ show_picture(6, "sue_o7")
    call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_InnRoomssueojohan_0_PlaySound_2
    $ resolve_scene()
    Johan "(Am I enjoying this?... Why can't I stop looking at? This feeling in my stomach ... I've never felt like this)"
    Villager2 "YEAH! You like it?"
    Leyna "I LOVE IT, PLEASE FUCK ME HARDER!"
    Johan "(No... please stop! I can't take this anymore!)"
    $ fade_out()
    stop music fadeout 1
    stop bgs fadeout 1
    $ erase_picture(1)
    $ erase_picture(2)
    $ erase_picture(3)
    $ erase_picture(4)
    $ erase_picture(5)
    $ erase_picture(6)
    call ChangePartyMember("Leyna", False) from _call_InnRoomssueojohan_0_ChangePartyMember
    call TransferPlayer("InnRooms", "InnRoomssueojohan_0", 13, 9, direction=6) from _call_InnRoomssueojohan_0_TransferPlayer
    $ fade_in()
    call Movement("InnRoomssueojohan_0", "player", [["JUMP",0,0]]) from _call_InnRoomssueojohan_0_Movement_1
    $ resolve_scene()
    Johan "LEYNA!!"
    call Movement("InnRoomssueojohan_0", "player", ["TURN_D",["WAIT",60],"TURN_L",["WAIT",60],"TURN_R",["WAIT",60],"TURN_U",["WAIT",60],"TURN_D"]) from _call_InnRoomssueojohan_0_Movement_2
    $ resolve_scene()
    call PauseForBalloon("InnRoomssueojohan_0") from _call_InnRoomssueojohan_0_PauseForBalloon
    Johan "... It was just a dream..."
    Johan "Shit! I have an erection..."
    Johan "Where is Leyna?.."
    call Movement("InnRoomssueojohan_0", "player", ["D","L","L","D","D","D"]) from _call_InnRoomssueojohan_0_Movement_3
    $ johan_dream = 1
    call GalleryViewed("sue_o") from _call_InnRoomssueojohan_0_GalleryViewed
    call TransferPlayer("Inn", "InnRoomssueojohan_0", 2, 2, direction=2) from _call_InnRoomssueojohan_0_TransferPlayer_1
    $ resolve_scene()
    return False

label InnRoomssueojohan(play_event = True, trigger = None): # autorun
    if is_erased("InnRoomssueojohan"):
        return None
    elif johan_dream >= 2:
        return None
    elif trigger == "autorun" and elder_festival >= 8:
        call PlayEvent(play_event, "InnRoomssueojohan_0", "InnRoomssueojohan") from _call_InnRoomssueojohan_0_PlayEvent
        return (0, "", "InnRoomssueojohan_0")
    return None

label InnRoomsescenadildo_0:
    call Movement("InnRoomsescenadildo_0", "player", ["U","R","R","R"]) from _call_InnRoomsescenadildo_0_Movement
    $ fade_out()
    call TransferPlayer("InnRooms", "InnRoomsescenadildo_0", 11, 10, direction=0) from _call_InnRoomsescenadildo_0_TransferPlayer
    call Movement("InnRoomsescenadildo_0", "player", ["R","TURN_L"]) from _call_InnRoomsescenadildo_0_Movement_1
    $ fade_in()
    $ resolve_scene()
    Leyna "...Well, what do you want to talk to me about?"
    Johan "I'm... well... I'm a little nervous... let's see... I want us to enjoy a little more, you know?"
    Leyna "???"
    Johan "Lately our sex life has been a little... monotonous, so I thought I'd make things a little more interesting"
    Leyna "O-oh! I see... what did you have in mind?"
    Johan "I... well, the truth is that I've heard a lot of good things about... ahem... well about anal sex"
    Leyna "A-anal sex?"
    Johan "Y-yes... and the truth is that I would like to try it... we have never done it... and well... that's all, a friend left me this"
    Leyna "!!!!"
    Johan "It's for you... I've been told that you can't do it in a rough way and that first you have to... practice so to speak... you know..."
    Leyna "I..."
    Johan "Y-you don't have to answer me now but think about it, okay?"
    Leyna "Wait!... ok... let's try it, the truth is that I was also curious"
    Johan "WOW! really? Great!"
    Leyna "(Hahahaha looks like a kid with a new toy) But I have to try it alone first, okay?"
    Johan "YES YES! relax, I have to go for a walk so I'll be out for the rest of the afternoon... ahem I.... well let me know how it goes"
    Leyna "Haahahahaha sure Johan... see you later"
    $ fade_out()
    call ChangePartyMember("Leyna", False) from _call_InnRoomsescenadildo_0_ChangePartyMember
    call TransferPlayer("Town2", "InnRoomsescenadildo_0", 22, 23, direction=4) from _call_InnRoomsescenadildo_0_TransferPlayer_1
    $ fade_in()
    $ resolve_scene()
    Johan "WOw, I can't believe she said yes!...."
    Johan "I'm a little nervous about it... but I can't wait to try it out"
    $ fade_out()
    call ChangePartyMember("Leyna", True) from _call_InnRoomsescenadildo_0_ChangePartyMember_1
    call ChangePartyMember("Johan", False) from _call_InnRoomsescenadildo_0_ChangePartyMember_2
    call TransferPlayer("InnRooms", "InnRoomsescenadildo_0", 13, 9, direction=4) from _call_InnRoomsescenadildo_0_TransferPlayer_2
    $ fade_in()
    $ resolve_scene()
    call PauseForBalloon("InnRoomsescenadildo_0") from _call_InnRoomsescenadildo_0_PauseForBalloon
    Leyna "Well... I guess now is as good a time as any to try this sucker...."
    $ show_picture(1, "dildo1")
    $ resolve_scene()
    Leyna "I should close the door, though... anyone could see me here"
    Leyna "Wow... looks like he also left me a lubricant I guess that makes sense"
    Leyna "... I can't believe I'm going to do this right now...."
    $ show_picture(2, "dildo2")
    $ resolve_scene()
    Leyna "It's... quite big... Is that okay with Johan? This thing is much bigger than his penis...."
    Leyna "Just thinking about what I'm going to do already makes me wet down there"
    Leyna "Well there is no point in waiting..."
    $ show_picture(3, "dildo3")
    $ resolve_scene()
    Leyna "I haven't even started and I'm already so horny....."
    Leyna "hmmmmm...."
    pause
    $ show_picture(4, "dildo4")
    $ resolve_scene()
    Leyna "will this fit?...it's so big...."
    Leyna "Let's do it little by little... I don't want to hurt myself"
    pause
    $ show_picture(5, "dildo5")
    $ resolve_scene()
    Leyna "Ahhh... little by little... hmmm... it hurts a little... but"
    Leyna "Ahhh... it's coming in... ohhh"
    pause
    $ show_picture(6, "dildo6")
    $ resolve_scene()
    Leyna "This is it... almost to the bottom... my god this feels... feels much better than I expected..."
    Leyna "I can't believe how good this feels... I'm going to cum... and I just put it in....."
    pause
    $ show_picture(7, "dildo7")
    $ resolve_scene()
    Leyna "AH!... this thing vibrates... and it's stimulating my clitoris while penetrating my ass..."
    Leyna "It feels amazing!.... AH ah ah ah!"
    Leyna "This... this is amazing"
    pause
    $ show_picture(8, "dildo8")
    call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_InnRoomsescenadildo_0_PlaySound
    $ resolve_scene()
    Leyna "Ah ah ah!!! .... AAAHH!!!"
    Leyna "It hurts a little but .... feels amazing"
    Leyna "I'm going to cum! I'M CUMMING!!!"
    Leyna "aaaaahhhhH!!!"
    pause
    $ show_picture(9, "dildo9")
    stop bgs fadeout 1
    $ resolve_scene()
    Leyna "AAAAAAAAAHHH!!!"
    Leyna "I've already cum.... I haven't lasted at all, I've never cum so fast... this has been awesome"
    Leyna "I can't... I can't wait to do it again..."
    pause
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
    call TransferPlayer("Town2", "InnRoomsescenadildo_0", 28, 22, direction=0) from _call_InnRoomsescenadildo_0_TransferPlayer_3
    $ fade_in()
    $ resolve_scene()
    Leyna "Hahahahaha I feel great... I'm like new... I could go back to work right now and I wouldn't get tired of it"
    Leyna "can't wait to tell Johan about it hehehehe"
    $ fade_out()
    call ChangePartyMember("Johan", True) from _call_InnRoomsescenadildo_0_ChangePartyMember_3
    call ChangePartyMember("Leyna", False) from _call_InnRoomsescenadildo_0_ChangePartyMember_4
    call TransferPlayer("Town2", "InnRoomsescenadildo_0", 10, 9, direction=2) from _call_InnRoomsescenadildo_0_TransferPlayer_4
    $ fade_in()
    $ resolve_scene()
    call PauseForBalloon("InnRoomsescenadildo_0") from _call_InnRoomsescenadildo_0_PauseForBalloon_1
    Johan "Another failed attempt to enter the castle... at this rate we won't be able to visit it before going back to the city... anyway..."
    $ resolve_scene()
    call PauseForBalloon("InnRoomsescenadildo_0") from _call_InnRoomsescenadildo_0_PauseForBalloon_2
    Johan "Leyna has already tried that?...I'm a little nervous ...I couldn't help but order a little extra toy for her on the internet"
    Johan "Although I guess it won't arrive for a couple of days and that's if we are lucky, this town is in the middle of nowhere"
    call PlaySound("sound", "audio/Saint5.ogg", volume=0.9, no_loop=True) from _call_InnRoomsescenadildo_0_PlaySound_1
    $ resolve_scene()
    call PauseForBalloon("InnRoomsescenadildo_0") from _call_InnRoomsescenadildo_0_PauseForBalloon_3
    Johan "A message?"
    Johan "WHAT?.... it can't be... the package has already arrived... I know I put express shipping but I ordered it a couple of hours ago..."
    Johan "Is it manufactured here?... what a coincidence it would be..."
    Johan "Anyway, it says that the pick up point is at the inn, I should go to pick it up before the innkeeper opens the package to gossip"
    $ butt_plug = 1
    call GalleryViewed("dildo") from _call_InnRoomsescenadildo_0_GalleryViewed
    return False

label InnRoomsescenadildo(play_event = True, trigger = None): # autorun
    if is_erased("InnRoomsescenadildo"):
        return None
    elif butt_plug >= 1:
        return None
    elif trigger == "autorun" and bar_work >= 4:
        call PlayEvent(play_event, "InnRoomsescenadildo_0", "InnRoomsescenadildo") from _call_InnRoomsescenadildo_0_PlayEvent
        return (0, "", "InnRoomsescenadildo_0")
    return None

label InnRoomsEV011Base(menu_choice = None):
    "do you want to enter the gallery?"
    call GetChoice([_("Yes"), _("No")], value=menu_choice, called_from="InnRoomsEV011") from _call_InnRoomsEV011_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Yes"):
        $ menu_choice = None
        call TransferPlayer("Gallery", "InnRoomsEV011", 14, 2, direction=2) from _call_InnRoomsEV011_TransferPlayer
    elif menu_choice == _("No"):
        $ menu_choice = None
    $ resolve_scene()
    return False

label InnRoomsEV011(play_event = True, trigger = None): # event
    if is_erased("InnRoomsEV011"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnRoomsEV011Base", "InnRoomsEV011") from _call_InnRoomsEV011_PlayEvent
        return (1, "", "InnRoomsEV011")
    return None

label InnRoomsMyHeadIsKillingMeSeemsLikeYesterdayWeHadTooMuchToDrinkAgainICanBarelyRememberWhatHappened_0:
    call PauseForBalloon("InnRoomsEV012_0") from _call_InnRoomsEV012_0_PauseForBalloon
    Johan "my head is killing me... seems like yesterday we had too much to drink... again... I can barely remember what happened"
    Johan "Something from a card game... and Alexa was there too... God, what a mess I am, I hope I didn't make a fool of myself"
    Johan "Although I don't remember getting here... Leyna brought me here?...."
    call Movement("InnRoomsEV012_0", "player", ["TURN_L",["WAIT",60],"TURN_R",["WAIT",60],"TURN_D",["WAIT",60]]) from _call_InnRoomsEV012_0_Movement
    $ resolve_scene()
    call PauseForBalloon("InnRoomsEV012_0") from _call_InnRoomsEV012_0_PauseForBalloon_1
    Johan "Speaking of Leyna... Where has she gone? I should go and look for her..."
    Johan "It's the last day of the festival, at least I will spend it with her"
    $ set_self_switch("InnRooms","InnRoomsMyHeadIsKillingMeSeemsLikeYesterdayWeHadTooMuchToDrinkAgainICanBarelyRememberWhatHappened","A",True)
    return False

label InnRoomsMyHeadIsKillingMeSeemsLikeYesterdayWeHadTooMuchToDrinkAgainICanBarelyRememberWhatHappened(play_event = True, trigger = None): # autorun
    if is_erased("InnRoomsMyHeadIsKillingMeSeemsLikeYesterdayWeHadTooMuchToDrinkAgainICanBarelyRememberWhatHappened"):
        return None
    elif self_switch("InnRooms","InnRoomsMyHeadIsKillingMeSeemsLikeYesterdayWeHadTooMuchToDrinkAgainICanBarelyRememberWhatHappened","A"):
        return None
    elif trigger == "autorun" and switch("bet_2"):
        call PlayEvent(play_event, "InnRoomsMyHeadIsKillingMeSeemsLikeYesterdayWeHadTooMuchToDrinkAgainICanBarelyRememberWhatHappened_0", "InnRoomsMyHeadIsKillingMeSeemsLikeYesterdayWeHadTooMuchToDrinkAgainICanBarelyRememberWhatHappened") from _call_InnRoomsMyHeadIsKillingMeSeemsLikeYesterdayWeHadTooMuchToDrinkAgainICanBarelyRememberWhatHappened_0_PlayEvent
        return (0, "", "InnRoomsMyHeadIsKillingMeSeemsLikeYesterdayWeHadTooMuchToDrinkAgainICanBarelyRememberWhatHappened_0")
    return None

label InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_0:
    call Movement("InnRoomsEV013_0", "player", ["TURN_L",["WAIT",60],"TURN_R",["WAIT",60],"TURN_U",["WAIT",60],"TURN_D",["WAIT",60]]) from _call_InnRoomsEV013_0_Movement
    $ resolve_scene()
    Leyna "Johan hasn't slept here tonight... where is he? I should look for him... or not... maybe he's at the bus stop"
    Leyna "Although I could also take a last walk around town... I have some unfinished business in and around the bar hehehe"
    $ set_self_switch("InnRooms","InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop","A",True)
    return False

label InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_1:
    call Movement("InnRoomsEV013_1", "player", ["TURN_L",["WAIT",60],"TURN_R",["WAIT",60],"TURN_U",["WAIT",60],"TURN_D",["WAIT",60]]) from _call_InnRoomsEV013_1_Movement
    $ resolve_scene()
    Leyna "Johan hasn't slept here tonight.... where is he? he's probably furious about yesterday... and rightly so, what the hell was I thinking?"
    Leyna "I have to fix this any way I can... I have to find my husband, my god .... he's probably at the bus stop"
    $ set_self_switch("InnRooms","InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop","A",True)
    return False

label InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop(play_event = True, trigger = None): # autorun
    if is_erased("InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop"):
        return None
    elif self_switch("InnRooms","InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop","A"):
        return None
    elif trigger == "autorun" and switch("festival_final") and switch("corruption_average"):
        call PlayEvent(play_event, "InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_1", "InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop") from _call_InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_1_PlayEvent
        return (0, "", "InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_1")
    elif trigger == "autorun" and switch("festival_final") and switch("corruption_high"):
        call PlayEvent(play_event, "InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_0", "InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop") from _call_InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_0_PlayEvent
        return (0, "", "InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_0")
    return None

