label RiverBG:
    $ set_transparency_backgrounds(["bg_river","midbg"])
    $ set_map_backgrounds(["map_river"])
    return

label RiverStart:
    call RiverBG from _call_RiverBG
    stop music
    stop bgs
    return

label RiverEnd:
    return

label RiverimpedimentoparasalirrioBase:
    Johan "We have to interview someone."
    call Movement("Riverimpedimentoparasalirrio", "player", ["TURN_R","R","R"]) from _call_Riverimpedimentoparasalirrio_Movement
    $ resolve_scene()
    return False

label Riverimpedimentoparasalirrio(play_event = True, trigger = None): # event
    if is_erased("Riverimpedimentoparasalirrio"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "RiverimpedimentoparasalirrioBase", "Riverimpedimentoparasalirrio") from _call_Riverimpedimentoparasalirrio_PlayEvent
        return (0, "", "Riverimpedimentoparasalirrio")
    return None

label Riverimpedimentoparasalirrio_v2Base:
    Johan "We have to interview someone."
    call Movement("Riverimpedimentoparasalirrio_v2", "player", ["TURN_R","R","R"]) from _call_Riverimpedimentoparasalirrio_v2_Movement
    $ resolve_scene()
    return False

label Riverimpedimentoparasalirrio_v2(play_event = True, trigger = None): # event
    if is_erased("Riverimpedimentoparasalirrio_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Riverimpedimentoparasalirrio_v2Base", "Riverimpedimentoparasalirrio_v2") from _call_Riverimpedimentoparasalirrio_v2_PlayEvent
        return (0, "", "Riverimpedimentoparasalirrio_v2")
    return None

label Riverentradario_0(menu_choice = None):
    call Movement("Riverentradario_0", "player", ["TURN_R"]) from _call_Riverentradario_0_Movement
    call Movement("Riverentradario_0", "RiverNPCEntranceMan", ["TURN_D"]) from _call_Riverentradario_0_Movement_1
    $ resolve_scene()
    Villager "Hey! you can't pass with clothes on! Tradition says one can only pass if he goes naked."
    call Movement("Riverentradario_0", "player", ["TURN_U"]) from _call_Riverentradario_0_Movement_2
    $ resolve_scene()
    Johan "Sorry, we are not from here, we came to make an article and take some photos of the festivities, if you give us your permission, of course"
    Villager "An article, you say? hmmm if you are worried for the woman, we can make an exception for the circumstances.."
    "..but you have to go naked, this is a sacred tradition. The girl can carry a towel on her if she wants, just for this occasion."
    Johan "great, I have no problem. What do you think Leyna?"
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    call GetChoice([_("Yes"), _("I'm not ready yet")], value=menu_choice, called_from="Riverentradario_0") from _call_Riverentradario_0_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Yes"):
        $ menu_choice = None
        $ resolve_scene()
        Villager "Perfect. Back there you have a small tent to leave your clothes."
        Johan "Perfect, we'll interview a couple of people and take photos of those who agree"
        $ erase_picture(1)
        call ChangePartyMember("Johan", False) from _call_Riverentradario_0_ChangePartyMember
        call ChangePartyMember("Leyna", False) from _call_Riverentradario_0_ChangePartyMember_1
        call ChangePartyMember("Leyna2", True) from _call_Riverentradario_0_ChangePartyMember_2
        call ChangePartyMember("Johan2", True) from _call_Riverentradario_0_ChangePartyMember_3
        $ set_switch("separated_in_the_river", True)
        call TransferPlayer("River", "Riverentradario_0", 0, 10, direction=6) from _call_Riverentradario_0_TransferPlayer
        call Movement("Riverentradario_0", "player", ["R","R"]) from _call_Riverentradario_0_Movement_3
    elif menu_choice == _("I'm not ready yet"):
        $ menu_choice = None
        $ resolve_scene()
        Leyna "I think I'm not ready yet. I have to think about this a little more."
        Johan "Okey, no problem. We'll do it another time."
        $ erase_picture(1)
        call TransferPlayer("Town", "Riverentradario_0", 47, 23, direction=4) from _call_Riverentradario_0_TransferPlayer_1
        call Movement("Riverentradario_0", "player", ["L","L"]) from _call_Riverentradario_0_Movement_4
    $ resolve_scene()
    return False

label Riverentradario(play_event = True, trigger = None): # autorun
    if is_erased("Riverentradario"):
        return None
    elif switch("separated_in_the_river"):
        return None
    elif trigger == "autorun":
        call PlayEvent(play_event, "Riverentradario_0", "Riverentradario") from _call_Riverentradario_0_PlayEvent
        return (0, "", "Riverentradario_0")
    return None

label RiverNPCEntranceManBase:
    Villager "Now that you are half-naked, the goddess will be pleased"
    return False

label RiverNPCEntranceMan(play_event = True, trigger = None): # event
    if is_erased("RiverNPCEntranceMan"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "RiverNPCEntranceManBase", "RiverNPCEntranceMan") from _call_RiverNPCEntranceMan_PlayEvent
        return (1, "", "RiverNPCEntranceMan")
    return None

label RiverNPCRiverBucket_0:
    Leyna "Excuse me, can I ask you a couple of questions?"
    Villager "??? (Wow, she's hot)... Yes of course"
    $ fade_out()
    $ fade_in()
    $ resolve_scene()
    Leyna "Thanks for your patience."
    Villager "Sure, if you have any questions you tell me."
    $ set_self_switch("River","RiverNPCRiverBucket","A",True)
    return False

label RiverNPCRiverBucket_1:
    Villager "Do you have any questions?"
    Leyna "No, thank you"
    return False

label RiverNPCRiverBucket(play_event = True, trigger = None): # event
    if is_erased("RiverNPCRiverBucket"):
        return None
    elif trigger == "event" and self_switch("River","RiverNPCRiverBucket","A"):
        call PlayEvent(play_event, "RiverNPCRiverBucket_1", "RiverNPCRiverBucket") from _call_RiverNPCRiverBucket_1_PlayEvent
        return (1, "", "RiverNPCRiverBucket_1")
    elif trigger == "event":
        call PlayEvent(play_event, "RiverNPCRiverBucket_0", "RiverNPCRiverBucket") from _call_RiverNPCRiverBucket_0_PlayEvent
        return (1, "", "RiverNPCRiverBucket_0")
    return None

label RiverNPCEventManBase(menu_choice = None):
    Johan "Good afternoon, me and my wife are doing a report on the traditions of this town..."
    "... I was wondering if you would mind answering some questions for me and let me take some pictures of you by the river."
    $ show_transparent(1, "general_chica_rio", width=1600, height=900)
    $ resolve_scene()
    Villager "Oh! Of course, no problem man, ask what you want"
    $ fade_out()
    $ erase_picture(1)
    $ fade_in()
    $ resolve_scene()
    Johan "So the celebration goes back thousands of years and is in honour of a very old fertility goddess..."
    "...how interesting! Great, now I'm going to take a couple of photos if you don't mind."
    Villager "Yes, of course ..."
    $ set_switch("separated_in_the_river", True)
    call Movement("RiverNPCEventMan", "player", ["D","R","TURN_U"]) from _call_RiverNPCEventMan_Movement
    $ resolve_scene()
    $ flash_screen([255,255,255,170], 60, True)
    $ resolve_scene()
    Villager "I have an idea..."
    Johan "Yes?"
    Villager "It's just us in these photos. If you only show this in the article, people won't want to come to this town, right?"
    Johan "Well..."
    Villager "If you only see a group of ugly men posing on the camera it would be a disaster..."
    "...what these photos need is a feminine touch "
    $ show_transparent(1, "expresion_neutral_toalla", width=1600, height=900)
    $ resolve_scene()
    Johan "A feminine touch?..."
    Villager "Exactly, why doesn't your wife come up and poses in a couple of photos with us?"
    $ show_transparent(2, "expresion_sorpresa_toalla", width=1600, height=900)
    $ resolve_scene()
    Johan "I see... It makes sense, what do you think Leyna, would mind appearing in a couple of photos?..."
    "...anyway, I'm going to black out the faces and  the towel covers your body"
    Villager "(I can't believe this is working... So she's naked under the towel)"
    $ erase_picture(2)
    $ resolve_scene()
    Leyna "yeah... well, if you think it's a good idea... I guess it doesn't seem bad to me."
    Johan "Okay. Well, put yourself in the middle and I'll take some photos"
    $ fade_out()
    $ erase_picture(1)
    $ fade_in()
    $ show_picture(1, "rio_1", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Villager "(Damn... the girl smells great)"
    $ show_picture(2, "rio_2", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Johan "Maybe you could go a little closer for the photo"
    Villager "O...Of course!"
    pause
    $ show_picture(3, "rio_3", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Leyna "(!!!)"
    pause
    $ show_picture(4, "rio_4", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Johan "(They are too close ... well, I'm not going to bother them too much..."
    "...after all, they are doing us a favour letting us take photos of them)"
    pause
    $ show_picture(5, "rio_5", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Villager "( This is my chance, but I have to do it right or I'll get caught! )"
    pause
    $ show_picture(6, "rio_6", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_RiverNPCEventMan_PlaySound
    call PlaySound("music", "audio/Dungeon3.ogg", volume=0.9, no_loop=False) from _call_RiverNPCEventMan_PlaySound_1
    $ resolve_scene()
    pause
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_RiverNPCEventMan_PlaySound_2
    $ show_picture(7, "rio_7", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Johan "(!!!!!!!!!)"
    Villager "(WOW DAMN! OKAY, KEEP CALM KEEP CALM)"
    pause
    $ show_picture(8, "rio_8", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Leyna "Ooh?!!"
    Johan "(Shit, they are seeing everything)"
    pause
    $ show_picture(9, "rio_9", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Villager "Oh boy, the towel has fallen off. Well don't worry too much, after all, this is a tradition here and we are all naked"
    pause
    $ show_picture(10, "rio_10", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Leyna "(I have to put on the towel right now!)"
    Johan "( What the fuck!? They are huge )"
    pause
    $ show_picture(11, "rio_11", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Villager "Sorry, but it's natural, isn't it? This kind of thing happens, and more after seeing a naked woman as beautiful as you"
    pause
    $ show_picture(12, "rio_12", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    call PlaySound("sound", "audio/Jump2.ogg", volume=0.9, no_loop=True) from _call_RiverNPCEventMan_PlaySound_3
    $ resolve_scene()
    Leyna "Ex...excuse me?"
    pause
    $ show_picture(13, "rio_13", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Villager "You know, erections and that sort of thing."
    Leyna "Oh ... sure..."
    $ show_picture(14, "rio14", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Villager "Well ... hey, don't you think it's a good artistic photo?I think in this position you could take a couple of good photos"
    call GetChoice([_("Okey"), _("This has gone too far")], value=menu_choice, called_from="RiverNPCEventMan") from _call_RiverNPCEventMan_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Okey"):
        $ menu_choice = None
        $ resolve_scene()
        Johan "Yes ... I'll take one more photo and that's it."
        $ show_picture(15, "rio15", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
        $ resolve_scene()
        Leyna "(what's going on?)"
        Leyna "(his ... things are very close to me ... Johan is fine with this?... I think he is not even aware of what is happening...)"
        Leyna "(I have to stop looking at... that so much. and maybe pose or something?)"
        Johan "Okay, that's it... Thanks for your help guys"
        Leyna "(!!!)"
        Villager "Thank you. Come back whenever you want!"
        Johan "(...)"
        pause
        $ fade_out()
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(5)
        $ erase_picture(4)
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
        call ChangePartyMember("Leyna2", False) from _call_RiverNPCEventMan_ChangePartyMember
        call ChangePartyMember("Johan2", False) from _call_RiverNPCEventMan_ChangePartyMember_1
        call ChangePartyMember("Johan", True) from _call_RiverNPCEventMan_ChangePartyMember_2
        call ChangePartyMember("Leyna", True) from _call_RiverNPCEventMan_ChangePartyMember_3
        $ fade_in()
        call TransferPlayer("Town", "RiverNPCEventMan", 47, 23, direction=4) from _call_RiverNPCEventMan_TransferPlayer
        call Movement("RiverNPCEventMan", "player", ["L","L"]) from _call_RiverNPCEventMan_Movement_1
        $ corruption = corruption + 2
        $ resolve_scene()
        "CORRUPTION +2"
    elif menu_choice == _("This has gone too far"):
        $ menu_choice = None
        Johan "No, enough guys! We are leaving..."
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
        call ChangePartyMember("Leyna2", False) from _call_RiverNPCEventMan_ChangePartyMember_4
        call ChangePartyMember("Johan2", False) from _call_RiverNPCEventMan_ChangePartyMember_5
        call ChangePartyMember("Johan", True) from _call_RiverNPCEventMan_ChangePartyMember_6
        call ChangePartyMember("Leyna", True) from _call_RiverNPCEventMan_ChangePartyMember_7
        $ fade_in()
        call TransferPlayer("Town", "RiverNPCEventMan", 47, 23, direction=4) from _call_RiverNPCEventMan_TransferPlayer_1
        call Movement("RiverNPCEventMan", "player", ["L","L"]) from _call_RiverNPCEventMan_Movement_2
        $ corruption = corruption + 1
        $ resolve_scene()
        "CORRUPTION +1"
    $ set_switch("finished_river_scene", True)
    call GalleryViewed("rio") from _call_RiverNPCEventMan_GalleryViewed
    $ show_transparent(1, "plano_mujer_timida", width=1600, height=900)
    $ resolve_scene()
    Leyna "( His ... \"things\" were huge. Are all like this in  here? )"
    Johan "Are you okay?"
    $ show_transparent(2, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Oh! Yes... I'm okey..."
    $ erase_picture(1)
    $ erase_picture(2)
    $ resolve_scene()
    return False

label RiverNPCEventMan(play_event = True, trigger = None): # event
    if is_erased("RiverNPCEventMan"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "RiverNPCEventManBase", "RiverNPCEventMan") from _call_RiverNPCEventMan_PlayEvent
        return (1, "", "RiverNPCEventMan")
    return None

label RiverNPChombreeventorio_v2Base(menu_choice = None):
    Johan "Good afternoon, me and my wife are doing a report on the traditions of this town..."
    "... I was wondering if you would mind answering some questions for me and let me take some pictures of you by the river."
    $ show_transparent(1, "general_chica_rio", width=1600, height=900)
    $ resolve_scene()
    Villager "Oh! Of course, no problem man, ask what you want"
    $ fade_out()
    $ erase_picture(1)
    $ fade_in()
    $ resolve_scene()
    Johan "So the celebration goes back thousands of years and is in honour of a very old fertility goddess..."
    "...how interesting! Great, now I'm going to take a couple of photos if you don't mind."
    Villager "Yes, of course ..."
    $ set_switch("separated_in_the_river", True)
    call Movement("RiverNPChombreeventorio_v2", "player", ["D","L","TURN_U"]) from _call_RiverNPChombreeventorio_v2_Movement
    $ resolve_scene()
    $ flash_screen([255,255,255,170], 60, True)
    $ resolve_scene()
    Villager "I have an idea..."
    Johan "Yes?"
    Villager "It's just us in these photos. If you only show this in the article, people won't want to come to this town, right?"
    Johan "Well..."
    Villager "If you only see a group of ugly men posing on the camera it would be a disaster..."
    "...what these photos need is a feminine touch "
    $ show_transparent(1, "expresion_neutral_toalla", width=1600, height=900)
    $ resolve_scene()
    Johan "A feminine touch?..."
    Villager "Exactly, why doesn't your wife come up and poses in a couple of photos with us?"
    $ show_transparent(2, "expresion_sorpresa_toalla", width=1600, height=900)
    $ resolve_scene()
    Johan "I see... It makes sense, what do you think Leyna, would mind appearing in a couple of photos?..."
    "...anyway, I'm going to black out the faces and  the towel covers your body"
    Villager "(I can't believe this is working... So she's naked under the towel)"
    $ erase_picture(2)
    $ resolve_scene()
    Leyna "yeah... well, if you think it's a good idea... I guess it doesn't seem bad to me."
    Johan "Okay. Well, put yourself in the middle and I'll take some photos"
    $ fade_out()
    $ erase_picture(1)
    $ fade_in()
    $ show_picture(1, "rio_1", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Villager "(Damn... the girl smells great)"
    $ show_picture(2, "rio_2", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Johan "Maybe you could go a little closer for the photo"
    Villager "O...Of course!"
    pause
    $ show_picture(3, "rio_3", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Leyna "(!!!)"
    pause
    $ show_picture(4, "rio_4", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Johan "(They are too close ... well, I'm not going to bother them too much..."
    "...after all, they are doing us a favour letting us take photos of them)"
    pause
    $ show_picture(5, "rio_5", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Villager "( This is my chance, but I have to do it right or I'll get caught! )"
    pause
    $ show_picture(6, "rio_6", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_RiverNPChombreeventorio_v2_PlaySound
    call PlaySound("music", "audio/Dungeon3.ogg", volume=0.9, no_loop=False) from _call_RiverNPChombreeventorio_v2_PlaySound_1
    $ resolve_scene()
    pause
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_RiverNPChombreeventorio_v2_PlaySound_2
    $ show_picture(7, "rio_7", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Johan "(!!!!!!!!!)"
    Villager "(WOW DAMN! OKAY, KEEP CALM KEEP CALM)"
    pause
    $ show_picture(8, "rio_8", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Leyna "Ooh?!!"
    Johan "(Shit, they are seeing everything)"
    pause
    $ show_picture(9, "rio_9", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Villager "Oh boy, the towel has fallen off. Well don't worry too much, after all, this is a tradition here and we are all naked"
    pause
    $ show_picture(10, "rio_10", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Leyna "(I have to put on the towel right now!)"
    Johan "( What the fuck!? They are huge )"
    pause
    $ show_picture(11, "rio_11", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Villager "Sorry, but it's natural, isn't it? This kind of thing happens, and more after seeing a naked woman as beautiful as you"
    pause
    $ show_picture(12, "rio_12", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    call PlaySound("sound", "audio/Jump2.ogg", volume=0.9, no_loop=True) from _call_RiverNPChombreeventorio_v2_PlaySound_3
    $ resolve_scene()
    Leyna "Ex...excuse me?"
    pause
    $ show_picture(13, "rio_13", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Villager "You know, erections and that sort of thing."
    Leyna "Oh ... sure..."
    $ show_picture(14, "rio14", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Villager "Well ... hey, don't you think it's a good artistic photo?I think in this position you could take a couple of good photos"
    call GetChoice([_("Okey"), _("This has gone too far")], value=menu_choice, called_from="RiverNPChombreeventorio_v2") from _call_RiverNPChombreeventorio_v2_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Okey"):
        $ menu_choice = None
        $ resolve_scene()
        Johan "Yes ... I'll take one more photo and that's it."
        $ show_picture(15, "rio15", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
        $ resolve_scene()
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_RiverNPChombreeventorio_v2_PlaySound_4
        Leyna "(what's going on?)"
        Leyna "(his ... things are very close to me ... Johan is fine with this?... I think he is not even aware of what is happening...)"
        Leyna "(I have to stop looking at... that so much. and maybe pose or something?)"
        Johan "Okay, that's it... Thanks for your help guys"
        Leyna "(!!!)"
        Villager "Thank you. Come back whenever you want!"
        Johan "(...)"
        pause
        $ fade_out()
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(5)
        $ erase_picture(4)
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
        call ChangePartyMember("Leyna2", False) from _call_RiverNPChombreeventorio_v2_ChangePartyMember
        call ChangePartyMember("Johan2", False) from _call_RiverNPChombreeventorio_v2_ChangePartyMember_1
        call ChangePartyMember("Johan", True) from _call_RiverNPChombreeventorio_v2_ChangePartyMember_2
        call ChangePartyMember("Leyna", True) from _call_RiverNPChombreeventorio_v2_ChangePartyMember_3
        $ fade_in()
        call TransferPlayer("Town", "RiverNPChombreeventorio_v2", 47, 23, direction=4) from _call_RiverNPChombreeventorio_v2_TransferPlayer
        call Movement("RiverNPChombreeventorio_v2", "player", ["L","L"]) from _call_RiverNPChombreeventorio_v2_Movement_1
        $ corruption = corruption + 2
        $ resolve_scene()
        "CORRUPTION +2"
    elif menu_choice == _("This has gone too far"):
        $ menu_choice = None
        Johan "No, enough guys! We are leaving..."
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
        call ChangePartyMember("Leyna2", False) from _call_RiverNPChombreeventorio_v2_ChangePartyMember_4
        call ChangePartyMember("Johan2", False) from _call_RiverNPChombreeventorio_v2_ChangePartyMember_5
        call ChangePartyMember("Johan", True) from _call_RiverNPChombreeventorio_v2_ChangePartyMember_6
        call ChangePartyMember("Leyna", True) from _call_RiverNPChombreeventorio_v2_ChangePartyMember_7
        $ fade_in()
        call TransferPlayer("Town", "RiverNPChombreeventorio_v2", 47, 23, direction=4) from _call_RiverNPChombreeventorio_v2_TransferPlayer_1
        call Movement("RiverNPChombreeventorio_v2", "player", ["L","L"]) from _call_RiverNPChombreeventorio_v2_Movement_2
        $ corruption = corruption + 1
        $ resolve_scene()
        "CORRUPTION +1"
    $ set_switch("finished_river_scene", True)
    call GalleryViewed("rio") from _call_RiverNPChombreeventorio_v2_GalleryViewed
    $ show_transparent(1, "plano_mujer_timida", width=1600, height=900)
    $ resolve_scene()
    Leyna "( His ... \"things\" were huge. Are all like this in  here? )"
    Johan "Are you okay?"
    $ show_transparent(2, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Oh! Yes... I'm okey..."
    $ erase_picture(1)
    $ erase_picture(2)
    $ resolve_scene()
    return False

label RiverNPChombreeventorio_v2(play_event = True, trigger = None): # event
    if is_erased("RiverNPChombreeventorio_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "RiverNPChombreeventorio_v2Base", "RiverNPChombreeventorio_v2") from _call_RiverNPChombreeventorio_v2_PlayEvent
        return (1, "", "RiverNPChombreeventorio_v2")
    return None

