label PathBG:
    $ set_transparency_backgrounds(["bg_path"])
    $ set_map_backgrounds(["map_path"])
    return

label PathStart:
    call PathBG from _call_PathBG
    stop music
    stop bgs
    return

label PathEnd:
    return

label Pathnpcentradafestivalcamino_0:
    Villager "You can't pass yet, we are building the tents"
    return False

label Pathnpcentradafestivalcamino_1:
    "(We should go buy the clothes before)"
    return False

label Pathnpcentradafestivalcamino_2:
    call TransferPlayer("Festival", "Pathnpcentradafestivalcamino_2", 12, 0, direction=2) from _call_Pathnpcentradafestivalcamino_2_TransferPlayer
    $ resolve_scene()
    return False

label Pathnpcentradafestivalcamino_3:
    "(We should go to the inn and have some sleep)"
    return False

label Pathnpcentradafestivalcamino_4:
    Johan "Well, here we are, are you ready?"
    Leyna "Yeah, It sure will be fun, and there is traditional food and games, let's have a good time"
    Johan "Sure..."
    Johan "They told me that there's a changing room near here..."
    $ fade_out()
    $ show_picture(1, "vestuario1")
    $ fade_in()
    $ resolve_scene()
    Villager "Wow!Look at that woman! Is she going to change here,in front of us?"
    Villager2 "I hope so! Get ready to see the show my friend!"
    call PlaySound("sound", "audio/Applause1.ogg", volume=0.9, no_loop=True) from _call_Pathnpcentradafestivalcamino_4_PlaySound
    $ show_picture(2, "vestuario2")
    $ resolve_scene()
    Villager "WHAT? Is she wearing the festival clothes underneath?"
    call PlaySound("sound", "audio/Disappointment.ogg", volume=0.9, no_loop=True) from _call_Pathnpcentradafestivalcamino_4_PlaySound_1
    Villager2 "Damn! What a disappointment! Even so, she has a great body. You don't see this every day"
    $ show_picture(3, "vestuario3")
    $ resolve_scene()
    Villager "Yeah... Man I need to see her naked!"
    Villager2 "Relax, during all the festival games we will find a excuse to see her naked or something better"
    Villager "Don't give me much hope"
    $ show_picture(4, "vestuario4")
    $ resolve_scene()
    Villager "Fuck, what a good ass!"
    Villager2 "That woman will be mine"
    Villager "No, if I get it first"
    $ fade_out()
    $ erase_picture(1)
    $ erase_picture(2)
    $ erase_picture(3)
    $ erase_picture(4)
    call TransferPlayer("Festival", "Pathnpcentradafestivalcamino_4", 12, 0, direction=0) from _call_Pathnpcentradafestivalcamino_4_TransferPlayer
    $ fade_in()
    call PlaySound("music", "audio/Field2.ogg", volume=0.9, no_loop=False) from _call_Pathnpcentradafestivalcamino_4_PlaySound_2
    call Movement("Pathnpcentradafestivalcamino_4", "player", ["D","R","TURN_D"]) from _call_Pathnpcentradafestivalcamino_4_Movement
    $ resolve_scene()
    call PauseForBalloon("Pathnpcentradafestivalcamino_4") from _call_Pathnpcentradafestivalcamino_4_PauseForBalloon
    Johan "Wow, this changes quite a bit with so many people, it smells fantastic in here, my mouth is watering"
    Leyna "Cool!"
    Johan "It seems that there are so many things to do ... where could we start?"
    Leyna "Let's ask, surely there is someone who can help us"
    $ set_switch("festival", True)
    call GalleryViewed("vestuario") from _call_Pathnpcentradafestivalcamino_4_GalleryViewed
    return False

label Pathnpcentradafestivalcamino_5:
    call TransferPlayer("Festival", "Pathnpcentradafestivalcamino_5", 12, 0, direction=0) from _call_Pathnpcentradafestivalcamino_5_TransferPlayer
    $ resolve_scene()
    return False

label Pathnpcentradafestivalcamino_6:
    Leyna "I don't want to go there yet"
    return False

label Pathnpcentradafestivalcamino_7:
    call TransferPlayer("Mountains", "Pathnpcentradafestivalcamino_7", 12, 8, direction=4) from _call_Pathnpcentradafestivalcamino_7_TransferPlayer
    $ resolve_scene()
    return False

label Pathnpcentradafestivalcamino_8:
    Leyna "I should go to the hotsprings"
    return False

label Pathnpcentradafestivalcamino_9:
    Leyna "I don't need to go to the festival right now"
    return False

label Pathnpcentradafestivalcamino_10:
    $ fade_out()
    call TransferPlayer("Festival", "Pathnpcentradafestivalcamino_10", 12, 1, direction=2) from _call_Pathnpcentradafestivalcamino_10_TransferPlayer
    $ fade_in()
    $ resolve_scene()
    return False

label Pathnpcentradafestivalcamino_11:
    Johan "I don't feel like going to the festival right now"
    call Movement("Pathnpcentradafestivalcamino_11", "player", ["TURN_R","R"]) from _call_Pathnpcentradafestivalcamino_11_Movement
    $ resolve_scene()
    return False

label Pathnpcentradafestivalcamino_12:
    $ fade_out()
    $ show_picture(1, "vestuario2", scale=(120, 120))
    $ fade_in()
    $ resolve_scene()
    Johan "Well, this is it! I'm really looking forward to seeing what the festival has to offer!"
    Leyna "Yeah! I'm sure it'll be fun, I guess it'll be a good show or something!"
    Villager "Hey! what are you doing?"
    Johan "??? Well, put on the festival clothes, is there any problem?"
    Villager "Yes, there seems to have been some kind of misunderstanding"
    Leyna "How so?"
    Villager "Well, on the last day of the festival we all go naked, obviously!"
    Johan "naked?.... the mayor didn't say anything to me"
    Villager "Of course, he is a public employee, not even a job as simple as informing a reporter can be done well"
    Leyna "I see... well, we're already used to going naked thanks to this town, so I guess it's not much of a problem"
    Johan "Yes, you're right, I still would have liked to know beforehand"
    "Layna: Let's get undressed and enter the festival"
    Villager "Perfect, sorry for the inconvenience, guys"
    Johan "Don't worry"
    Villager2 "(whispering) Look Leyna has come to the last day of the festival"
    Villager3 "Really? but her husband is here... don't they know what's going to happen? well it's better for us!"
    Villager2 "And boy, oh boy! This year is going to be spectacular! I can't wait for the finale!"
    $ fade_out()
    call TransferPlayer("FestivalFinale", "Pathnpcentradafestivalcamino_12", 13, 6, direction=0) from _call_Pathnpcentradafestivalcamino_12_TransferPlayer
    $ erase_picture(1)
    $ fade_in()
    $ resolve_scene()
    return False

label Pathnpcentradafestivalcamino(play_event = True, trigger = None): # event
    if is_erased("Pathnpcentradafestivalcamino"):
        return None
    elif switch("festival_final"):
        return None
    elif trigger == "event" and switch("last_hotsprings"):
        call PlayEvent(play_event, "Pathnpcentradafestivalcamino_12", "Pathnpcentradafestivalcamino") from _call_Pathnpcentradafestivalcamino_12_PlayEvent
        return (0, "", "Pathnpcentradafestivalcamino_12")
    elif trigger == "event" and switch("party_at_festival"):
        call PlayEvent(play_event, "Pathnpcentradafestivalcamino_11", "Pathnpcentradafestivalcamino") from _call_Pathnpcentradafestivalcamino_11_PlayEvent
        return (0, "", "Pathnpcentradafestivalcamino_11")
    elif trigger == "event" and leyna_work >= 11:
        call PlayEvent(play_event, "Pathnpcentradafestivalcamino_10", "Pathnpcentradafestivalcamino") from _call_Pathnpcentradafestivalcamino_10_PlayEvent
        return (0, "", "Pathnpcentradafestivalcamino_10")
    elif trigger == "event" and leyna_work >= 10:
        call PlayEvent(play_event, "Pathnpcentradafestivalcamino_9", "Pathnpcentradafestivalcamino") from _call_Pathnpcentradafestivalcamino_9_PlayEvent
        return (0, "", "Pathnpcentradafestivalcamino_9")
    elif trigger == "event" and leyna_work >= 7:
        call PlayEvent(play_event, "Pathnpcentradafestivalcamino_8", "Pathnpcentradafestivalcamino") from _call_Pathnpcentradafestivalcamino_8_PlayEvent
        return (0, "", "Pathnpcentradafestivalcamino_8")
    elif trigger == "event" and leyna_work >= 4:
        call PlayEvent(play_event, "Pathnpcentradafestivalcamino_7", "Pathnpcentradafestivalcamino") from _call_Pathnpcentradafestivalcamino_7_PlayEvent
        return (0, "", "Pathnpcentradafestivalcamino_7")
    elif trigger == "event" and switch("leyna_dream_end"):
        call PlayEvent(play_event, "Pathnpcentradafestivalcamino_6", "Pathnpcentradafestivalcamino") from _call_Pathnpcentradafestivalcamino_6_PlayEvent
        return (0, "", "Pathnpcentradafestivalcamino_6")
    elif trigger == "event" and switch("festival"):
        call PlayEvent(play_event, "Pathnpcentradafestivalcamino_5", "Pathnpcentradafestivalcamino") from _call_Pathnpcentradafestivalcamino_5_PlayEvent
        return (0, "", "Pathnpcentradafestivalcamino_5")
    elif trigger == "event" and johan_dream >= 3:
        call PlayEvent(play_event, "Pathnpcentradafestivalcamino_4", "Pathnpcentradafestivalcamino") from _call_Pathnpcentradafestivalcamino_4_PlayEvent
        return (0, "", "Pathnpcentradafestivalcamino_4")
    elif trigger == "event" and elder_festival >= 8:
        call PlayEvent(play_event, "Pathnpcentradafestivalcamino_3", "Pathnpcentradafestivalcamino") from _call_Pathnpcentradafestivalcamino_3_PlayEvent
        return (0, "", "Pathnpcentradafestivalcamino_3")
    elif trigger == "event" and event_clothing >= 2:
        call PlayEvent(play_event, "Pathnpcentradafestivalcamino_2", "Pathnpcentradafestivalcamino") from _call_Pathnpcentradafestivalcamino_2_PlayEvent
        return (0, "", "Pathnpcentradafestivalcamino_2")
    elif trigger == "event" and elder_festival >= 6:
        call PlayEvent(play_event, "Pathnpcentradafestivalcamino_1", "Pathnpcentradafestivalcamino") from _call_Pathnpcentradafestivalcamino_1_PlayEvent
        return (0, "", "Pathnpcentradafestivalcamino_1")
    elif trigger == "event":
        call PlayEvent(play_event, "Pathnpcentradafestivalcamino_0", "Pathnpcentradafestivalcamino") from _call_Pathnpcentradafestivalcamino_0_PlayEvent
        return (1, "", "Pathnpcentradafestivalcamino_0")
    return None

label Pathespacioentradafestival_0:
    call Movement("Pathespacioentradafestival_0", "Pathnpcentradafestivalcamino", ["TURN_D"]) from _call_Pathespacioentradafestival_0_Movement
    $ resolve_scene()
    Villager "Hey! you can't pass yet, we are building the tents"
    Leyna "Oh, sorry"
    call Movement("Pathespacioentradafestival_0", "Pathjohan", ["TURN_R"]) from _call_Pathespacioentradafestival_0_Movement_1
    call Movement("Pathespacioentradafestival_0", "player", ["TURN_R","R"]) from _call_Pathespacioentradafestival_0_Movement_2
    $ resolve_scene()
    return False

label Pathespacioentradafestival_1:
    "(We should go buy the clothes before)"
    return False

label Pathespacioentradafestival_2:
    call TransferPlayer("Festival", "Pathespacioentradafestival_2", 12, 0, direction=2) from _call_Pathespacioentradafestival_2_TransferPlayer
    $ resolve_scene()
    return False

label Pathespacioentradafestival_3:
    "(We should go to the inn and have some sleep)"
    return False

label Pathespacioentradafestival_4:
    Johan "Well, here we are, are you ready?"
    Leyna "Yeah, It sure will be fun, and there is traditional food and games, let's have a good time"
    Johan "Sure..."
    Johan "They told me that there's a changing room near here..."
    $ fade_out()
    $ show_picture(1, "vestuario1")
    $ fade_in()
    $ resolve_scene()
    Villager "Wow!Look at that woman! Is she going to change here,in front of us?"
    Villager2 "I hope so! Get ready to see the show my friend!"
    call PlaySound("sound", "audio/Applause1.ogg", volume=0.9, no_loop=True) from _call_Pathespacioentradafestival_4_PlaySound
    $ show_picture(2, "vestuario2")
    $ resolve_scene()
    Villager "WHAT? Is she wearing the festival clothes underneath?"
    call PlaySound("sound", "audio/Disappointment.ogg", volume=0.9, no_loop=True) from _call_Pathespacioentradafestival_4_PlaySound_1
    Villager2 "Damn! What a disappointment! Even so, she has a great body. You don't see this every day"
    $ show_picture(3, "vestuario3")
    $ resolve_scene()
    Villager "Yeah... Man I need to see her naked!"
    Villager2 "Relax, during all the festival games we will find a excuse to see her naked or something better"
    Villager "Don't give me much hope"
    $ show_picture(4, "vestuario4")
    $ resolve_scene()
    Villager "Fuck, what a good ass!"
    Villager2 "That woman will be mine"
    Villager "No, if I get it first"
    $ fade_out()
    $ erase_picture(1)
    $ erase_picture(2)
    $ erase_picture(3)
    $ erase_picture(4)
    call TransferPlayer("Festival", "Pathespacioentradafestival_4", 12, 0, direction=0) from _call_Pathespacioentradafestival_4_TransferPlayer
    $ fade_in()
    call PlaySound("music", "audio/Field2.ogg", volume=0.9, no_loop=False) from _call_Pathespacioentradafestival_4_PlaySound_2
    call Movement("Pathespacioentradafestival_4", "player", ["D","R","TURN_D"]) from _call_Pathespacioentradafestival_4_Movement
    $ resolve_scene()
    call PauseForBalloon("Pathespacioentradafestival_4") from _call_Pathespacioentradafestival_4_PauseForBalloon
    Johan "Wow, this changes quite a bit with so many people, it smells fantastic in here, my mouth is watering"
    Leyna "Cool!"
    Johan "It seems that there are so many things to do ... where could we start?"
    Leyna "Let's ask, surely there is someone who can help us"
    $ set_switch("festival", True)
    call GalleryViewed("vestuario") from _call_Pathespacioentradafestival_4_GalleryViewed
    return False

label Pathespacioentradafestival_5:
    call TransferPlayer("Festival", "Pathespacioentradafestival_5", 12, 0, direction=0) from _call_Pathespacioentradafestival_5_TransferPlayer
    $ resolve_scene()
    return False

label Pathespacioentradafestival_6:
    Leyna "I don't want to go there yet"
    return False

label Pathespacioentradafestival_7:
    call TransferPlayer("Mountains", "Pathespacioentradafestival_7", 12, 8, direction=4) from _call_Pathespacioentradafestival_7_TransferPlayer
    $ resolve_scene()
    return False

label Pathespacioentradafestival_8:
    Leyna "I should go to the hotsprings"
    return False

label Pathespacioentradafestival_9:
    Leyna "I don't need to go to the festival right now"
    return False

label Pathespacioentradafestival_10:
    $ fade_out()
    call TransferPlayer("Festival", "Pathespacioentradafestival_10", 12, 1, direction=2) from _call_Pathespacioentradafestival_10_TransferPlayer
    $ fade_in()
    $ resolve_scene()
    return False

label Pathespacioentradafestival_11:
    Johan "I don't feel like going to the festival right now"
    call Movement("Pathespacioentradafestival_11", "player", ["TURN_R","R"]) from _call_Pathespacioentradafestival_11_Movement
    $ resolve_scene()
    return False

label Pathespacioentradafestival_12:
    $ fade_out()
    $ show_picture(1, "vestuario2", scale=(120, 120))
    $ fade_in()
    $ resolve_scene()
    Johan "Well, this is it! I'm really looking forward to seeing what the festival has to offer!"
    Leyna "Yeah! I'm sure it'll be fun, I guess it'll be a good show or something!"
    Villager "Hey! what are you doing?"
    Johan "??? Well, put on the festival clothes, is there any problem?"
    Villager "Yes, there seems to have been some kind of misunderstanding"
    Leyna "How so?"
    Villager "Well, on the last day of the festival we all go naked, obviously!"
    Johan "naked?.... the mayor didn't say anything to me"
    Villager "Of course, he is a public employee, not even a job as simple as informing a reporter can be done well"
    Leyna "I see... well, we're already used to going naked thanks to this town, so I guess it's not much of a problem"
    Johan "Yes, you're right, I still would have liked to know beforehand"
    "Layna: Let's get undressed and enter the festival"
    Villager "Perfect, sorry for the inconvenience, guys"
    Johan "Don't worry"
    Villager2 "(whispering) Look Leyna has come to the last day of the festival"
    Villager3 "Really? but her husband is here... don't they know what's going to happen? well it's better for us!"
    Villager2 "And boy, oh boy! This year is going to be spectacular! I can't wait for the finale!"
    $ fade_out()
    call TransferPlayer("FestivalFinale", "Pathespacioentradafestival_12", 13, 6, direction=0) from _call_Pathespacioentradafestival_12_TransferPlayer
    $ erase_picture(1)
    $ fade_in()
    $ resolve_scene()
    return False

label Pathespacioentradafestival(play_event = True, trigger = None): # event
    if is_erased("Pathespacioentradafestival"):
        return None
    elif switch("festival_final"):
        return None
    elif trigger == "event" and switch("last_hotsprings"):
        call PlayEvent(play_event, "Pathespacioentradafestival_12", "Pathespacioentradafestival") from _call_Pathespacioentradafestival_12_PlayEvent
        return (0, "", "Pathespacioentradafestival_12")
    elif trigger == "event" and switch("party_at_festival"):
        call PlayEvent(play_event, "Pathespacioentradafestival_11", "Pathespacioentradafestival") from _call_Pathespacioentradafestival_11_PlayEvent
        return (0, "", "Pathespacioentradafestival_11")
    elif trigger == "event" and leyna_work >= 11:
        call PlayEvent(play_event, "Pathespacioentradafestival_10", "Pathespacioentradafestival") from _call_Pathespacioentradafestival_10_PlayEvent
        return (0, "", "Pathespacioentradafestival_10")
    elif trigger == "event" and leyna_work >= 10:
        call PlayEvent(play_event, "Pathespacioentradafestival_9", "Pathespacioentradafestival") from _call_Pathespacioentradafestival_9_PlayEvent
        return (0, "", "Pathespacioentradafestival_9")
    elif trigger == "event" and leyna_work >= 7:
        call PlayEvent(play_event, "Pathespacioentradafestival_8", "Pathespacioentradafestival") from _call_Pathespacioentradafestival_8_PlayEvent
        return (0, "", "Pathespacioentradafestival_8")
    elif trigger == "event" and leyna_work >= 4:
        call PlayEvent(play_event, "Pathespacioentradafestival_7", "Pathespacioentradafestival") from _call_Pathespacioentradafestival_7_PlayEvent
        return (0, "", "Pathespacioentradafestival_7")
    elif trigger == "event" and switch("leyna_dream_end"):
        call PlayEvent(play_event, "Pathespacioentradafestival_6", "Pathespacioentradafestival") from _call_Pathespacioentradafestival_6_PlayEvent
        return (0, "", "Pathespacioentradafestival_6")
    elif trigger == "event" and switch("festival"):
        call PlayEvent(play_event, "Pathespacioentradafestival_5", "Pathespacioentradafestival") from _call_Pathespacioentradafestival_5_PlayEvent
        return (0, "", "Pathespacioentradafestival_5")
    elif trigger == "event" and johan_dream >= 3:
        call PlayEvent(play_event, "Pathespacioentradafestival_4", "Pathespacioentradafestival") from _call_Pathespacioentradafestival_4_PlayEvent
        return (0, "", "Pathespacioentradafestival_4")
    elif trigger == "event" and elder_festival >= 8:
        call PlayEvent(play_event, "Pathespacioentradafestival_3", "Pathespacioentradafestival") from _call_Pathespacioentradafestival_3_PlayEvent
        return (0, "", "Pathespacioentradafestival_3")
    elif trigger == "event" and event_clothing >= 2:
        call PlayEvent(play_event, "Pathespacioentradafestival_2", "Pathespacioentradafestival") from _call_Pathespacioentradafestival_2_PlayEvent
        return (0, "", "Pathespacioentradafestival_2")
    elif trigger == "event" and elder_festival >= 6:
        call PlayEvent(play_event, "Pathespacioentradafestival_1", "Pathespacioentradafestival") from _call_Pathespacioentradafestival_1_PlayEvent
        return (0, "", "Pathespacioentradafestival_1")
    elif trigger == "event":
        call PlayEvent(play_event, "Pathespacioentradafestival_0", "Pathespacioentradafestival") from _call_Pathespacioentradafestival_0_PlayEvent
        return (0, "", "Pathespacioentradafestival_0")
    return None

label PathToHotSpringsExteriorBase:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_PathEV003_PlaySound
    call TransferPlayer("HotSpringsExterior", "PathEV003", 11, 11, direction=8) from _call_PathEV003_TransferPlayer
    $ resolve_scene()
    return False

label PathToHotSpringsExterior(play_event = True, trigger = None): # event
    if is_erased("PathToHotSpringsExterior"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "PathToHotSpringsExteriorBase", "PathToHotSpringsExterior") from _call_PathToHotSpringsExterior_PlayEvent
        return (0, "", "PathToHotSpringsExterior")
    return None

label PathToHotSpringsExterior_v2Base:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_PathEV004_PlaySound
    call TransferPlayer("HotSpringsExterior", "PathEV004", 12, 11, direction=8) from _call_PathEV004_TransferPlayer
    $ resolve_scene()
    return False

label PathToHotSpringsExterior_v2(play_event = True, trigger = None): # event
    if is_erased("PathToHotSpringsExterior_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "PathToHotSpringsExterior_v2Base", "PathToHotSpringsExterior_v2") from _call_PathToHotSpringsExterior_v2_PlayEvent
        return (0, "", "PathToHotSpringsExterior_v2")
    return None

label PathToHotSpringsExterior_v3Base:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_PathEV005_PlaySound
    call TransferPlayer("HotSpringsExterior", "PathEV005", 13, 11, direction=8) from _call_PathEV005_TransferPlayer
    $ resolve_scene()
    return False

label PathToHotSpringsExterior_v3(play_event = True, trigger = None): # event
    if is_erased("PathToHotSpringsExterior_v3"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "PathToHotSpringsExterior_v3Base", "PathToHotSpringsExterior_v3") from _call_PathToHotSpringsExterior_v3_PlayEvent
        return (0, "", "PathToHotSpringsExterior_v3")
    return None

label PathHotSpringsTownBase:
    "^ |  Hot springs <- Festival - > Town"
    return False

label PathHotSpringsTown(play_event = True, trigger = None): # event
    if is_erased("PathHotSpringsTown"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "PathHotSpringsTownBase", "PathHotSpringsTown") from _call_PathHotSpringsTown_PlayEvent
        return (1, "", "PathHotSpringsTown")
    return None

label PathToTown_0:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_PathEV007_0_PlaySound
    call TransferPlayer("Town", "PathEV007_0", 0, 22, direction=6) from _call_PathEV007_0_TransferPlayer
    $ resolve_scene()
    return False

label PathToTown_1:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_PathEV007_1_PlaySound
    call TransferPlayer("Town2", "PathEV007_1", 0, 21, direction=0) from _call_PathEV007_1_TransferPlayer
    $ resolve_scene()
    return False

label PathToTown(play_event = True, trigger = None): # event
    if is_erased("PathToTown"):
        return None
    elif trigger == "event" and switch("third_day"):
        call PlayEvent(play_event, "PathToTown_1", "PathToTown") from _call_PathToTown_1_PlayEvent
        return (0, "", "PathToTown_1")
    elif trigger == "event":
        call PlayEvent(play_event, "PathToTown_0", "PathToTown") from _call_PathToTown_0_PlayEvent
        return (0, "", "PathToTown_0")
    return None

label PathToTown_v2_0:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_PathEV008_0_PlaySound
    call TransferPlayer("Town", "PathEV008_0", 0, 22, direction=6) from _call_PathEV008_0_TransferPlayer
    $ resolve_scene()
    return False

label PathToTown_v2_1:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_PathEV008_1_PlaySound
    call TransferPlayer("Town2", "PathEV008_1", 0, 22, direction=0) from _call_PathEV008_1_TransferPlayer
    $ resolve_scene()
    return False

label PathToTown_v2(play_event = True, trigger = None): # event
    if is_erased("PathToTown_v2"):
        return None
    elif trigger == "event" and switch("third_day"):
        call PlayEvent(play_event, "PathToTown_v2_1", "PathToTown_v2") from _call_PathToTown_v2_1_PlayEvent
        return (0, "", "PathToTown_v2_1")
    elif trigger == "event":
        call PlayEvent(play_event, "PathToTown_v2_0", "PathToTown_v2") from _call_PathToTown_v2_0_PlayEvent
        return (0, "", "PathToTown_v2_0")
    return None

label PathToTown_v3_0:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_PathEV009_0_PlaySound
    call TransferPlayer("Town", "PathEV009_0", 0, 22, direction=6) from _call_PathEV009_0_TransferPlayer
    $ resolve_scene()
    return False

label PathToTown_v3_1:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_PathEV009_1_PlaySound
    call TransferPlayer("Town2", "PathEV009_1", 0, 22, direction=0) from _call_PathEV009_1_TransferPlayer
    $ resolve_scene()
    return False

label PathToTown_v3(play_event = True, trigger = None): # event
    if is_erased("PathToTown_v3"):
        return None
    elif trigger == "event" and switch("third_day"):
        call PlayEvent(play_event, "PathToTown_v3_1", "PathToTown_v3") from _call_PathToTown_v3_1_PlayEvent
        return (0, "", "PathToTown_v3_1")
    elif trigger == "event":
        call PlayEvent(play_event, "PathToTown_v3_0", "PathToTown_v3") from _call_PathToTown_v3_0_PlayEvent
        return (0, "", "PathToTown_v3_0")
    return None

label PathMeowBase:
    "Meow"
    return False

label PathMeow(play_event = True, trigger = None): # event
    if is_erased("PathMeow"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "PathMeowBase", "PathMeow") from _call_PathMeow_PlayEvent
        return (1, "", "PathMeow")
    return None

label PathNPCFloatBase:
    ".....We all float down here..."
    return False

label PathNPCFloat(play_event = True, trigger = None): # event
    if is_erased("PathNPCFloat"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "PathNPCFloatBase", "PathNPCFloat") from _call_PathNPCFloat_PlayEvent
        return (1, "", "PathNPCFloat")
    return None

label PathNPCFestivalWorker_0:
    $ elder_festival = 1
    $ resolve_scene()
    Worker "I'm too old for this. Where is my fucking son?"
    Worker "Sorry miss, I was talking to myself.."
    Leyna "Don't worry, we've come to take a look before the opening.."
    "..is there a problem?"
    Worker "No problem at all... it's just I have to end the tents and my son should be here, helping me"
    "..we meet here at noon, sure last night he went out and he's drunk in any corner"
    Leyna "Sorry, if there's anything we can do to help you.."
    Worker "Actually yes! Although you are already here, you are not supposed to enter yet,  not until the opening"
    "But if you go find my son I will let it pass. He has my tools bag and I need them to finish the work"
    Johan "Okay sir, don't worry. We will bring your tools. Your son.. how does he look like?"
    Worker "I wish he looked as handsome as me hehehe.. He has brown hair and usually wears a blue t-shirt"
    "Don't take long, I have to finish this afternoon!"
    $ elder_festival = 2
    return False

label PathNPCFestivalWorker_1:
    Worker "What are you waiting for? Go find my son, please"
    return False

label PathNPCFestivalWorker_2:
    Worker "So? Do you have the tools?"
    Leyna "Yes sir, here you are"
    call PlaySound("sound", "audio/Recovery.ogg", volume=0.9, no_loop=True) from _call_PathEV012_2_PlaySound
    $ set_item("tools_bag", False)
    Worker "Thanks guys, now I can finish the tents on time. I'll let you pass right away, but it's better that you go first to the store to buy the traditional clothes"
    Leyna "Oh, perfect. We will be more integrated like that"
    Worker "See you there when you have the clothes"
    call Movement("PathEV012_2", "PathEV012", ["L","L","L","L","L"]) from _call_PathEV012_2_Movement
    $ fade_out()
    call SetEventLocation("PathEV012_2", "PathEV012", 20, 10) from _call_PathEV012_2_setloc
    $ elder_festival = 6
    $ fade_in()
    $ resolve_scene()
    return False

label PathNPCFestivalWorker(play_event = True, trigger = None): # event
    if is_erased("PathNPCFestivalWorker"):
        return None
    elif elder_festival >= 6:
        return None
    elif trigger == "event" and elder_festival >= 5:
        call PlayEvent(play_event, "PathNPCFestivalWorker_2", "PathNPCFestivalWorker") from _call_PathNPCFestivalWorker_2_PlayEvent
        return (1, "", "PathNPCFestivalWorker_2")
    elif trigger == "event" and elder_festival >= 2:
        call PlayEvent(play_event, "PathNPCFestivalWorker_1", "PathNPCFestivalWorker") from _call_PathNPCFestivalWorker_1_PlayEvent
        return (1, "", "PathNPCFestivalWorker_1")
    elif trigger == "event" and photograph_3 >= 1:
        call PlayEvent(play_event, "PathNPCFestivalWorker_0", "PathNPCFestivalWorker") from _call_PathNPCFestivalWorker_0_PlayEvent
        return (1, "", "PathNPCFestivalWorker_0")
    return None

label PathEV013_0:
    label PathEV013_0_loop_1:
        $ resolve_scene()
        call PauseForBalloon("PathEV013_0") from _call_PathEV013_0_PauseForBalloon
        # jump PathEV013_0_loop_1
    label PathEV013_0_loop_1_end:
        pass
    $ elder_festival = 1
    $ resolve_scene()
    return False

label PathEV013(play_event = True, trigger = None): # None-only parallel
    if is_erased("PathEV013"):
        return None
    elif elder_festival >= 1:
        return None
    elif trigger == "parallel" and photograph_3 >= 1:
        return None # PathEV013_0 potentially infinite looping parallel
    return None

label PathEV014Base:
    $ johan_dream = 3
    $ resolve_scene()
    return False

label PathEV014(play_event = True, trigger = None): # event
    if is_erased("PathEV014"):
        return None
    elif trigger == "event" and johan_dream >= 2:
        call PlayEvent(play_event, "PathEV014Base", "PathEV014") from _call_PathEV014_PlayEvent
        return (0, "", "PathEV014")
    return None

label PathEV015Base:
    $ johan_dream = 3
    $ resolve_scene()
    return False

label PathEV015(play_event = True, trigger = None): # event
    if is_erased("PathEV015"):
        return None
    elif trigger == "event" and johan_dream >= 2:
        call PlayEvent(play_event, "PathEV015Base", "PathEV015") from _call_PathEV015_PlayEvent
        return (0, "", "PathEV015")
    return None

label PathJohan_0:
    call Movement("PathEV016_0", "player", [["CHANGE_SPEED",4],"D","D","D","D","D","D","D"]) from _call_PathEV016_0_Movement
    $ resolve_scene()
    call PauseForBalloon("PathEV016_0") from _call_PathEV016_0_PauseForBalloon
    Leyna "Johan?"
    call Movement("PathEV016_0", "Pathjohan", ["TURN_U"]) from _call_PathEV016_0_Movement_1
    $ resolve_scene()
    call PauseForBalloon("PathEV016_0") from _call_PathEV016_0_PauseForBalloon_1
    Johan "Leyna! I was looking for you, how did the job search go?"
    Leyna "Well... After a lot of searching I have found a job in the hotsprings"
    Johan "So in the hotsprings eh?..... well it's better than nothing... I guess they won't make you do anything weird, right?"
    Leyna "Oh no... Don't worry, I'm only in charge of cleaning and that kind of stuff"
    Johan "Well, great then... I have also finished with what I had pending, I had thought about spending some time at the festival"
    Johan "This way I can finish a couple of pending interviews and we can relax for a while and have something to eat"
    Leyna "Sure, if that's okay with you, that's fine with me"
    $ fade_out()
    $ leyna_work = 11
    call ChangePartyMember("Johan", True) from _call_PathEV016_0_ChangePartyMember
    $ fade_in()
    $ resolve_scene()
    return False

label PathJohan(play_event = True, trigger = None): # autorun
    if is_erased("PathJohan"):
        return None
    elif leyna_work >= 11:
        return None
    elif trigger == "autorun" and leyna_work >= 10:
        call PlayEvent(play_event, "PathJohan_0", "PathJohan") from _call_PathJohan_0_PlayEvent
        return (0, "", "PathJohan_0")
    return None

label PathLeynaWorkTrigger_0:
    call PauseForBalloon("PathEV018_0") from _call_PathEV018_0_PauseForBalloon
    Leyna ".... Shit... Do I really have to do this? ... Who am I kidding? It's normal for Johan to get like this..."
    Leyna "The strange thing is that he didn't realize before that something strange was going on... just remembering what happened the other day..."
    $ fade_out()
    $ show_picture(1, "hotspringsjuntos6")
    $ fade_in()
    $ resolve_scene()
    "THE LAST DAY LEYNA WENT TO WORK..."
    Villager "Hey... You're the new girl working here, right?"
    Leyna "Hmmm yes, it's me, do you need anything?"
    Villager "Yes, my friend and I have a problem, come with us and we'll show you, it's a little delicate"
    Leyna "Su-sure"
    $ show_picture(2, "flashback1")
    $ resolve_scene()
    Leyna "Tell me, what is the problem?"
    Villager "Well, you tell me!"
    Leyna "What?"
    Villager "As you heard!  explain to me why you have the facilities in such a bad condition, I don't know what kind of weeds you put in the water but..."
    Villager "I've got a rash! look! this is all your fault! especially yours as you're the one in charge of this!"
    Villager "I guess I'll have to talk to the manager and discuss your future in this job"
    Leyna "I-I, please don't! (I haven't been paid for the photo shoots yet...) I need the money... please... how can I make it up to you?"
    Villager "(I can't believe this is working!).... Well... if you get like that... I guess you could make it up to me..."
    Leyna "??? Sure! Tell me what do you need..."
    Villager "First of all, I want you to see what you've done! look closely at the rash I got here!"
    $ show_picture(3, "flashback2")
    $ resolve_scene()
    Villager "That's right, get down!"
    Leyna "(Do I always have to end up with someone's cock so close to my face?)... n-not seeing anything"
    Villager "Ehm... of course! because it's not there! it's here!"
    $ show_picture(4, "flashback3")
    call PlaySound("sound", "audio/Jump2.ogg", volume=0.9, no_loop=True) from _call_PathEV018_0_PlaySound
    $ resolve_scene()
    Leyna "AH!!"
    Villager "Do you see it now?"
    Leyna "(I still don't see anything, but I'd better play along so that this is over as soon as possible) Yes, I see it, Sorry, it's my fault"
    Leyna "(This is so humiliating...)"
    Villager "Exactly... I was thinking of talking to your manager! but seeing that you have recognized your mistakes and that you are willing to help us with this..."
    Villager "We can fix it right now! you only have to do one thing..."
    Leyna "Tell me..."
    Villager "Kiss me down there, one kiss is enough for me!"
    Leyna "A-a kiss? There? I..."
    Villager2 "Yes! and if I were you I'd hurry up, with how full this place is today they could see us at any moment!"
    Leyna "(!!! shit! he's right and... and Johan is on the other side of these curtains...if he would see me in this situation...  I don't know what would happen)"
    Leyna "Okay..."
    $ show_picture(5, "flashback4")
    $ resolve_scene()
    Villager "That's right, good girl"
    Villager2 "(What a fucker! Now I want some too.... Hehehehe I have an idea)"
    Villager2 "Oh boy, you've had a bath too, haven't you, girl? I'm the town doctor and I can see you've got a little problem down there too"
    Leyna "???"
    Villager2 "Yes, this looks bad, I'm going to inspect you a little bit..."
    $ show_picture(6, "flashback5")
    call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV018_0_PlaySound_1
    $ resolve_scene()
    Leyna "Aahh..."
    Villager "You see? we all help each other here hahahaha"
    Villager2 "Exactly! and it looks like I'm helping you out quite a bit hehehe! you're dripping"
    pause
    $ show_picture(7, "flashback6")
    stop bgs fadeout 1
    $ resolve_scene()
    Leyna "Ah ah ah ah... D-don't keep going... (We could be seen at any moment... I can't go on with this... Johan is right there... but it feels soooo good)"
    if switch("infusion"):
        $ resolve_scene()
        Leyna "...(I can't help it, I just want it to go on a little longer... I need it or I'll go crazy...)"
        $ show_picture(8, "flashback7")
        $ resolve_scene()
        Villager2 "I'm going to inspect you a little more thoroughly, sweetie..."
        Leyna "I... we shouldn't... my husband..."
        Villager2 "Oh... it will only take a few minutes, don't worry, it won't take long at all"
        Leyna "!!!"
        pause
        $ show_picture(9, "flashback8")
        $ resolve_scene()
        Villager2 "That's it...that's it, all the way to the deep end very good... wow You're really tight down there... You needed this, huh?"
        Leyna "Aahhh... (My God it's huge... it's going to break me in half... )... Yeah? ah ah ah"
        Villager "(What a son of a bitch, I could have thought of that myself...)"
        Villager2 "All right, ready? I'm going to help you really good"
        pause
        $ show_picture(10, "flashback9")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV018_0_PlaySound_2
        $ resolve_scene()
        Leyna "AH! AH! AH!"
        Villager2 "That's it! do you like it? you don't need to tell me I know you love it, bitch!"
        Leyna "Hmmmm!! YES YES!"
        Villager "Wow, You were right, this girl is a real slut"
        Villager2 "I told you! A girl dressed like that surrounded by men is just begging to be fucked!"
        Leyna "N-no! (Why does it make me so horny to be talked to like that? I would never...) ... AAAH!!! HMMM..."
        Villager2 "What's wrong? Your husband doesn't fuck you like he should? I'm sure that's it... well, don't worry, we'll take care of you, slut!"
        Leyna "S-stop... I... Ah ah ah!"
        pause
        $ show_picture(11, "flashback10")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV018_0_PlaySound_3
        $ resolve_scene()
        Villager3 "Hey, you wouldn't happen to have any spare towels lying around, would you? FUCK! WHAT THE FUCK IS GOING ON?"
        stop bgs fadeout 1
        Leyna "!!!"
        Villager "!!!! Oh Shit"
        Villager2 "Shit..."
        Leyna "Get off of me NOW!"
        "vILLAGER 2: Tch... Yeah yeah..."
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
        $ fade_in()
    if not switch("infusion"):
        $ resolve_scene()
        "lEYNA: Sto-stop... please stop..."
        Villager2 "What? no way, I'll help you right away and you'll be much better"
        Leyna "N-NO! I've done what you wanted, leave me alone! I have to keep working"
        Villager2 "Fuck... okay as you wish...."
        $ fade_out()
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(4)
        $ erase_picture(5)
        $ erase_picture(6)
        $ erase_picture(7)
        $ fade_in()
    $ resolve_scene()
    Leyna "N-no! I can't go on like this with this job! it's too much! I'll talk to the manager and..."
    Leyna "I'm sure I'll find something else while I'm waiting for the payments from my modeling job... maybe if I ask the bar again? I hope so..."
    $ set_switch("flashback", True)
    call GalleryViewed("flashback") from _call_PathEV018_0_GalleryViewed
    Leyna "It can't get any worse than this, can it?"
    $ set_self_switch("Path","PathLeynaWorkTrigger","A",True)
    return False

label PathLeynaWorkTrigger_1:
    call PauseForBalloon("PathEV018_1") from _call_PathEV018_1_PauseForBalloon
    Leyna ".... Shit... Do I really have to do this? ... Who am I kidding? It's normal for Johan to get like this..."
    Leyna "The strange thing is that he didn't realize before that something strange was going on... just remembering what happened the other day..."
    $ fade_out()
    $ show_picture(1, "hotspringsjuntos6")
    $ fade_in()
    $ resolve_scene()
    "THE LAST DAY LEYNA WENT TO WORK..."
    Villager "Hey... You're the new girl working here, right?"
    Leyna "Hmmm yes, it's me, do you need anything?"
    Villager "Yes, my friend and I have a problem, come with us and we'll show you, it's a little delicate"
    Leyna "Su-sure"
    $ show_picture(2, "flashback1")
    $ resolve_scene()
    Leyna "Tell me, what is the problem?"
    Villager "Well, you tell me!"
    Leyna "What?"
    Villager "As you heard!  explain to me why you have the facilities in such a bad condition, I don't know what kind of weeds you put in the water but..."
    Villager "I've got a rash! look! this is all your fault! especially yours as you're the one in charge of this!"
    Villager "I guess I'll have to talk to the manager and discuss your future in this job"
    Leyna "I-I, please don't! (I haven't been paid for the photo shoots yet...) I need the money... please... how can I make it up to you?"
    Villager "(I can't believe this is working!).... Well... if you get like that... I guess you could make it up to me..."
    Leyna "??? Sure! Tell me what do you need..."
    Villager "First of all, I want you to see what you've done! look closely at the rash I got here!"
    $ show_picture(3, "flashback2")
    $ resolve_scene()
    Villager "That's right, get down!"
    Leyna "(Do I always have to end up with someone's cock so close to my face?)... n-not seeing anything"
    Villager "Ehm... of course! because it's not there! it's here!"
    $ show_picture(4, "flashback3")
    call PlaySound("sound", "audio/Jump2.ogg", volume=0.9, no_loop=True) from _call_PathEV018_1_PlaySound
    $ resolve_scene()
    Leyna "AH!!"
    Villager "Do you see it now?"
    Leyna "(I still don't see anything, but I'd better play along so that this is over as soon as possible) Yes, I see it, Sorry, it's my fault"
    Leyna "(This is so humiliating...)"
    Villager "Exactly... I was thinking of talking to your manager! but seeing that you have recognized your mistakes and that you are willing to help us with this..."
    Villager "We can fix it right now! you only have to do one thing..."
    Leyna "Tell me..."
    Villager "Kiss me down there, one kiss is enough for me!"
    Leyna "A-a kiss? There? I..."
    Villager2 "Yes! and if I were you I'd hurry up, with how full this place is today they could see us at any moment!"
    Leyna "(!!! shit! he's right and... and Johan is on the other side of these curtains...if he would see me in this situation...  I don't know what would happen)"
    Leyna "Okay..."
    $ show_picture(5, "flashback4")
    $ resolve_scene()
    Villager "That's right, good girl"
    Villager2 "(What a fucker! Now I want some too.... Hehehehe I have an idea)"
    Villager2 "Oh boy, you've had a bath too, haven't you, girl? I'm the town doctor and I can see you've got a little problem down there too"
    Leyna "???"
    Villager2 "Yes, this looks bad, I'm going to inspect you a little bit..."
    $ show_picture(6, "flashback5")
    call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV018_1_PlaySound_1
    $ resolve_scene()
    Leyna "Aahh..."
    Villager "You see? we all help each other here hahahaha"
    Villager2 "Exactly! and it looks like I'm helping you out quite a bit hehehe! you're dripping"
    pause
    $ show_picture(7, "flashback6")
    stop bgs fadeout 1
    $ resolve_scene()
    Leyna "Ah ah ah ah... D-don't keep going... (We could be seen at any moment... I can't go on with this... Johan is right there... but it feels soooo good)"
    if switch("infusion"):
        $ resolve_scene()
        Leyna "...(I can't help it, I just want it to go on a little longer... I need it or I'll go crazy...)"
        $ show_picture(8, "flashback7")
        $ resolve_scene()
        Villager2 "I'm going to inspect you a little more thoroughly, sweetie..."
        Leyna "I... we shouldn't... my husband..."
        Villager2 "Oh... it will only take a few minutes, don't worry, it won't take long at all"
        Leyna "!!!"
        pause
        $ show_picture(9, "flashback8")
        $ resolve_scene()
        Villager2 "That's it...that's it, all the way to the deep end very good... wow You're really tight down there... You needed this, huh?"
        Leyna "Aahhh... (My God it's huge... it's going to break me in half... )... Yeah? ah ah ah"
        Villager "(What a son of a bitch, I could have thought of that myself...)"
        Villager2 "All right, ready? I'm going to help you really good"
        pause
        $ show_picture(10, "flashback9")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV018_1_PlaySound_2
        $ resolve_scene()
        Leyna "AH! AH! AH!"
        Villager2 "That's it! do you like it? you don't need to tell me I know you love it, bitch!"
        Leyna "Hmmmm!! YES YES!"
        Villager "Wow, You were right, this girl is a real slut"
        Villager2 "I told you! A girl dressed like that surrounded by men is just begging to be fucked!"
        Leyna "N-no! (Why does it make me so horny to be talked to like that? I would never...) ... AAAH!!! HMMM..."
        Villager2 "What's wrong? Your husband doesn't fuck you like he should? I'm sure that's it... well, don't worry, we'll take care of you, slut!"
        Leyna "S-stop... I... Ah ah ah!"
        pause
        $ show_picture(11, "flashback10")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV018_1_PlaySound_3
        $ resolve_scene()
        Villager3 "Hey, you wouldn't happen to have any spare towels lying around, would you? FUCK! WHAT THE FUCK IS GOING ON?"
        stop bgs fadeout 1
        Leyna "!!!"
        Villager "!!!! Oh Shit"
        Villager2 "Shit..."
        Leyna "Get off of me NOW!"
        "vILLAGER 2: Tch... Yeah yeah..."
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
        $ fade_in()
    if not switch("infusion"):
        $ resolve_scene()
        "lEYNA: Sto-stop... please stop..."
        Villager2 "What? no way, I'll help you right away and you'll be much better"
        Leyna "N-NO! I've done what you wanted, leave me alone! I have to keep working"
        Villager2 "Fuck... okay as you wish...."
        $ fade_out()
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(4)
        $ erase_picture(5)
        $ erase_picture(6)
        $ erase_picture(7)
        $ fade_in()
    $ resolve_scene()
    Leyna "N-no! I can't go on like this with this job! it's too much! I'll talk to the manager and..."
    Leyna "I'm sure I'll find something else while I'm waiting for the payments from my modeling job... maybe if I ask the bar again? I hope so..."
    $ set_switch("flashback", True)
    call GalleryViewed("flashback") from _call_PathEV018_1_GalleryViewed
    Leyna "It can't get any worse than this, can it?"
    $ set_self_switch("Path","PathLeynaWorkTrigger","A",True)
    return False

label PathLeynaWorkTrigger_3:
    "closed today"
    return False

label PathLeynaWorkTrigger(play_event = True, trigger = None): # event
    if is_erased("PathLeynaWorkTrigger"):
        return None
    elif switch("last_bar"):
        return None
    elif trigger == "event" and switch("party_at_festival"):
        call PlayEvent(play_event, "PathLeynaWorkTrigger_3", "PathLeynaWorkTrigger") from _call_PathLeynaWorkTrigger_3_PlayEvent
        return (1, "", "PathLeynaWorkTrigger_3")
    elif self_switch("Path","PathLeynaWorkTrigger","A"):
        return None
    elif trigger == "event" and bet_together >= 2:
        call PlayEvent(play_event, "PathLeynaWorkTrigger_1", "PathLeynaWorkTrigger") from _call_PathLeynaWorkTrigger_1_PlayEvent
        return (0, "", "PathLeynaWorkTrigger_1")
    elif trigger == "event" and bet_together >= 1:
        call PlayEvent(play_event, "PathLeynaWorkTrigger_0", "PathLeynaWorkTrigger") from _call_PathLeynaWorkTrigger_0_PlayEvent
        return (0, "", "PathLeynaWorkTrigger_0")
    return None

label PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v2_0:
    call PauseForBalloon("PathEV019_0") from _call_PathEV019_0_PauseForBalloon
    Leyna ".... Shit... Do I really have to do this? ... Who am I kidding? It's normal for Johan to get like this..."
    Leyna "The strange thing is that he didn't realize before that something strange was going on... just remembering what happened the other day..."
    $ fade_out()
    $ show_picture(1, "hotspringsjuntos6")
    $ fade_in()
    $ resolve_scene()
    "THE LAST DAY LEYNA WENT TO WORK..."
    Villager "Hey... You're the new girl working here, right?"
    Leyna "Hmmm yes, it's me, do you need anything?"
    Villager "Yes, my friend and I have a problem, come with us and we'll show you, it's a little delicate"
    Leyna "Su-sure"
    $ show_picture(2, "flashback1")
    $ resolve_scene()
    Leyna "Tell me, what is the problem?"
    Villager "Well, you tell me!"
    Leyna "What?"
    Villager "As you heard!  explain to me why you have the facilities in such a bad condition, I don't know what kind of weeds you put in the water but..."
    Villager "I've got a rash! look! this is all your fault! especially yours as you're the one in charge of this!"
    Villager "I guess I'll have to talk to the manager and discuss your future in this job"
    Leyna "I-I, please don't! (I haven't been paid for the photo shoots yet...) I need the money... please... how can I make it up to you?"
    Villager "(I can't believe this is working!).... Well... if you get like that... I guess you could make it up to me..."
    Leyna "??? Sure! Tell me what do you need..."
    Villager "First of all, I want you to see what you've done! look closely at the rash I got here!"
    $ show_picture(3, "flashback2")
    $ resolve_scene()
    Villager "That's right, get down!"
    Leyna "(Do I always have to end up with someone's cock so close to my face?)... n-not seeing anything"
    Villager "Ehm... of course! because it's not there! it's here!"
    $ show_picture(4, "flashback3")
    call PlaySound("sound", "audio/Jump2.ogg", volume=0.9, no_loop=True) from _call_PathEV019_0_PlaySound
    $ resolve_scene()
    Leyna "AH!!"
    Villager "Do you see it now?"
    Leyna "(I still don't see anything, but I'd better play along so that this is over as soon as possible) Yes, I see it, Sorry, it's my fault"
    Leyna "(This is so humiliating...)"
    Villager "Exactly... I was thinking of talking to your manager! but seeing that you have recognized your mistakes and that you are willing to help us with this..."
    Villager "We can fix it right now! you only have to do one thing..."
    Leyna "Tell me..."
    Villager "Kiss me down there, one kiss is enough for me!"
    Leyna "A-a kiss? There? I..."
    Villager2 "Yes! and if I were you I'd hurry up, with how full this place is today they could see us at any moment!"
    Leyna "(!!! shit! he's right and... and Johan is on the other side of these curtains...if he would see me in this situation...  I don't know what would happen)"
    Leyna "Okay..."
    $ show_picture(5, "flashback4")
    $ resolve_scene()
    Villager "That's right, good girl"
    Villager2 "(What a fucker! Now I want some too.... Hehehehe I have an idea)"
    Villager2 "Oh boy, you've had a bath too, haven't you, girl? I'm the town doctor and I can see you've got a little problem down there too"
    Leyna "???"
    Villager2 "Yes, this looks bad, I'm going to inspect you a little bit..."
    $ show_picture(6, "flashback5")
    call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV019_0_PlaySound_1
    $ resolve_scene()
    Leyna "Aahh..."
    Villager "You see? we all help each other here hahahaha"
    Villager2 "Exactly! and it looks like I'm helping you out quite a bit hehehe! you're dripping"
    pause
    $ show_picture(7, "flashback6")
    stop bgs fadeout 1
    $ resolve_scene()
    Leyna "Ah ah ah ah... D-don't keep going... (We could be seen at any moment... I can't go on with this... Johan is right there... but it feels soooo good)"
    if switch("infusion"):
        $ resolve_scene()
        Leyna "...(I can't help it, I just want it to go on a little longer... I need it or I'll go crazy...)"
        $ show_picture(8, "flashback7")
        $ resolve_scene()
        Villager2 "I'm going to inspect you a little more thoroughly, sweetie..."
        Leyna "I... we shouldn't... my husband..."
        Villager2 "Oh... it will only take a few minutes, don't worry, it won't take long at all"
        Leyna "!!!"
        pause
        $ show_picture(9, "flashback8")
        $ resolve_scene()
        Villager2 "That's it...that's it, all the way to the deep end very good... wow You're really tight down there... You needed this, huh?"
        Leyna "Aahhh... (My God it's huge... it's going to break me in half... )... Yeah? ah ah ah"
        Villager "(What a son of a bitch, I could have thought of that myself...)"
        Villager2 "All right, ready? I'm going to help you really good"
        pause
        $ show_picture(10, "flashback9")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV019_0_PlaySound_2
        $ resolve_scene()
        Leyna "AH! AH! AH!"
        Villager2 "That's it! do you like it? you don't need to tell me I know you love it, bitch!"
        Leyna "Hmmmm!! YES YES!"
        Villager "Wow, You were right, this girl is a real slut"
        Villager2 "I told you! A girl dressed like that surrounded by men is just begging to be fucked!"
        Leyna "N-no! (Why does it make me so horny to be talked to like that? I would never...) ... AAAH!!! HMMM..."
        Villager2 "What's wrong? Your husband doesn't fuck you like he should? I'm sure that's it... well, don't worry, we'll take care of you, slut!"
        Leyna "S-stop... I... Ah ah ah!"
        pause
        $ show_picture(11, "flashback10")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV019_0_PlaySound_3
        $ resolve_scene()
        Villager3 "Hey, you wouldn't happen to have any spare towels lying around, would you? FUCK! WHAT THE FUCK IS GOING ON?"
        stop bgs fadeout 1
        Leyna "!!!"
        Villager "!!!! Oh Shit"
        Villager2 "Shit..."
        Leyna "Get off of me NOW!"
        "vILLAGER 2: Tch... Yeah yeah..."
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
        $ fade_in()
    if not switch("infusion"):
        $ resolve_scene()
        "lEYNA: Sto-stop... please stop..."
        Villager2 "What? no way, I'll help you right away and you'll be much better"
        Leyna "N-NO! I've done what you wanted, leave me alone! I have to keep working"
        Villager2 "Fuck... okay as you wish...."
        $ fade_out()
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(4)
        $ erase_picture(5)
        $ erase_picture(6)
        $ erase_picture(7)
        $ fade_in()
    $ resolve_scene()
    Leyna "N-no! I can't go on like this with this job! it's too much! I'll talk to the manager and..."
    Leyna "I'm sure I'll find something else while I'm waiting for the payments from my modeling job... maybe if I ask the bar again? I hope so..."
    $ set_switch("flashback", True)
    call GalleryViewed("flashback") from _call_PathEV019_0_GalleryViewed
    Leyna "It can't get any worse than this, can it?"
    $ set_self_switch("Path","PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v2","A",True)
    return False

label PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v2_1:
    call PauseForBalloon("PathEV019_1") from _call_PathEV019_1_PauseForBalloon
    Leyna ".... Shit... Do I really have to do this? ... Who am I kidding? It's normal for Johan to get like this..."
    Leyna "The strange thing is that he didn't realize before that something strange was going on... just remembering what happened the other day..."
    $ fade_out()
    $ show_picture(1, "hotspringsjuntos6")
    $ fade_in()
    $ resolve_scene()
    "THE LAST DAY LEYNA WENT TO WORK..."
    Villager "Hey... You're the new girl working here, right?"
    Leyna "Hmmm yes, it's me, do you need anything?"
    Villager "Yes, my friend and I have a problem, come with us and we'll show you, it's a little delicate"
    Leyna "Su-sure"
    $ show_picture(2, "flashback1")
    $ resolve_scene()
    Leyna "Tell me, what is the problem?"
    Villager "Well, you tell me!"
    Leyna "What?"
    Villager "As you heard!  explain to me why you have the facilities in such a bad condition, I don't know what kind of weeds you put in the water but..."
    Villager "I've got a rash! look! this is all your fault! especially yours as you're the one in charge of this!"
    Villager "I guess I'll have to talk to the manager and discuss your future in this job"
    Leyna "I-I, please don't! (I haven't been paid for the photo shoots yet...) I need the money... please... how can I make it up to you?"
    Villager "(I can't believe this is working!).... Well... if you get like that... I guess you could make it up to me..."
    Leyna "??? Sure! Tell me what do you need..."
    Villager "First of all, I want you to see what you've done! look closely at the rash I got here!"
    $ show_picture(3, "flashback2")
    $ resolve_scene()
    Villager "That's right, get down!"
    Leyna "(Do I always have to end up with someone's cock so close to my face?)... n-not seeing anything"
    Villager "Ehm... of course! because it's not there! it's here!"
    $ show_picture(4, "flashback3")
    call PlaySound("sound", "audio/Jump2.ogg", volume=0.9, no_loop=True) from _call_PathEV019_1_PlaySound
    $ resolve_scene()
    Leyna "AH!!"
    Villager "Do you see it now?"
    Leyna "(I still don't see anything, but I'd better play along so that this is over as soon as possible) Yes, I see it, Sorry, it's my fault"
    Leyna "(This is so humiliating...)"
    Villager "Exactly... I was thinking of talking to your manager! but seeing that you have recognized your mistakes and that you are willing to help us with this..."
    Villager "We can fix it right now! you only have to do one thing..."
    Leyna "Tell me..."
    Villager "Kiss me down there, one kiss is enough for me!"
    Leyna "A-a kiss? There? I..."
    Villager2 "Yes! and if I were you I'd hurry up, with how full this place is today they could see us at any moment!"
    Leyna "(!!! shit! he's right and... and Johan is on the other side of these curtains...if he would see me in this situation...  I don't know what would happen)"
    Leyna "Okay..."
    $ show_picture(5, "flashback4")
    $ resolve_scene()
    Villager "That's right, good girl"
    Villager2 "(What a fucker! Now I want some too.... Hehehehe I have an idea)"
    Villager2 "Oh boy, you've had a bath too, haven't you, girl? I'm the town doctor and I can see you've got a little problem down there too"
    Leyna "???"
    Villager2 "Yes, this looks bad, I'm going to inspect you a little bit..."
    $ show_picture(6, "flashback5")
    call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV019_1_PlaySound_1
    $ resolve_scene()
    Leyna "Aahh..."
    Villager "You see? we all help each other here hahahaha"
    Villager2 "Exactly! and it looks like I'm helping you out quite a bit hehehe! you're dripping"
    pause
    $ show_picture(7, "flashback6")
    stop bgs fadeout 1
    $ resolve_scene()
    Leyna "Ah ah ah ah... D-don't keep going... (We could be seen at any moment... I can't go on with this... Johan is right there... but it feels soooo good)"
    if switch("infusion"):
        $ resolve_scene()
        Leyna "...(I can't help it, I just want it to go on a little longer... I need it or I'll go crazy...)"
        $ show_picture(8, "flashback7")
        $ resolve_scene()
        Villager2 "I'm going to inspect you a little more thoroughly, sweetie..."
        Leyna "I... we shouldn't... my husband..."
        Villager2 "Oh... it will only take a few minutes, don't worry, it won't take long at all"
        Leyna "!!!"
        pause
        $ show_picture(9, "flashback8")
        $ resolve_scene()
        Villager2 "That's it...that's it, all the way to the deep end very good... wow You're really tight down there... You needed this, huh?"
        Leyna "Aahhh... (My God it's huge... it's going to break me in half... )... Yeah? ah ah ah"
        Villager "(What a son of a bitch, I could have thought of that myself...)"
        Villager2 "All right, ready? I'm going to help you really good"
        pause
        $ show_picture(10, "flashback9")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV019_1_PlaySound_2
        $ resolve_scene()
        Leyna "AH! AH! AH!"
        Villager2 "That's it! do you like it? you don't need to tell me I know you love it, bitch!"
        Leyna "Hmmmm!! YES YES!"
        Villager "Wow, You were right, this girl is a real slut"
        Villager2 "I told you! A girl dressed like that surrounded by men is just begging to be fucked!"
        Leyna "N-no! (Why does it make me so horny to be talked to like that? I would never...) ... AAAH!!! HMMM..."
        Villager2 "What's wrong? Your husband doesn't fuck you like he should? I'm sure that's it... well, don't worry, we'll take care of you, slut!"
        Leyna "S-stop... I... Ah ah ah!"
        pause
        $ show_picture(11, "flashback10")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV019_1_PlaySound_3
        $ resolve_scene()
        Villager3 "Hey, you wouldn't happen to have any spare towels lying around, would you? FUCK! WHAT THE FUCK IS GOING ON?"
        stop bgs fadeout 1
        Leyna "!!!"
        Villager "!!!! Oh Shit"
        Villager2 "Shit..."
        Leyna "Get off of me NOW!"
        "vILLAGER 2: Tch... Yeah yeah..."
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
        $ fade_in()
    if not switch("infusion"):
        $ resolve_scene()
        "lEYNA: Sto-stop... please stop..."
        Villager2 "What? no way, I'll help you right away and you'll be much better"
        Leyna "N-NO! I've done what you wanted, leave me alone! I have to keep working"
        Villager2 "Fuck... okay as you wish...."
        $ fade_out()
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(4)
        $ erase_picture(5)
        $ erase_picture(6)
        $ erase_picture(7)
        $ fade_in()
    $ resolve_scene()
    Leyna "N-no! I can't go on like this with this job! it's too much! I'll talk to the manager and..."
    Leyna "I'm sure I'll find something else while I'm waiting for the payments from my modeling job... maybe if I ask the bar again? I hope so..."
    $ set_switch("flashback", True)
    call GalleryViewed("flashback") from _call_PathEV019_1_GalleryViewed
    Leyna "It can't get any worse than this, can it?"
    $ set_self_switch("Path","PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v2","A",True)
    return False

label PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v2_3:
    "closed today"
    return False

label PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v2(play_event = True, trigger = None): # event
    if is_erased("PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v2"):
        return None
    elif switch("last_bar"):
        return None
    elif trigger == "event" and switch("party_at_festival"):
        call PlayEvent(play_event, "PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v2_3", "PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v2") from _call_PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v2_3_PlayEvent
        return (1, "", "PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v2_3")
    elif self_switch("Path","PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v2","A"):
        return None
    elif trigger == "event" and bet_together >= 2:
        call PlayEvent(play_event, "PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v2_1", "PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v2") from _call_PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v2_1_PlayEvent
        return (0, "", "PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v2_1")
    elif trigger == "event" and bet_together >= 1:
        call PlayEvent(play_event, "PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v2_0", "PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v2") from _call_PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v2_0_PlayEvent
        return (0, "", "PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v2_0")
    return None

label PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v3_0:
    call PauseForBalloon("PathEV020_0") from _call_PathEV020_0_PauseForBalloon
    Leyna ".... Shit... Do I really have to do this? ... Who am I kidding? It's normal for Johan to get like this..."
    Leyna "The strange thing is that he didn't realize before that something strange was going on... just remembering what happened the other day..."
    $ fade_out()
    $ show_picture(1, "hotspringsjuntos6")
    $ fade_in()
    $ resolve_scene()
    "THE LAST DAY LEYNA WENT TO WORK..."
    Villager "Hey... You're the new girl working here, right?"
    Leyna "Hmmm yes, it's me, do you need anything?"
    Villager "Yes, my friend and I have a problem, come with us and we'll show you, it's a little delicate"
    Leyna "Su-sure"
    $ show_picture(2, "flashback1")
    $ resolve_scene()
    Leyna "Tell me, what is the problem?"
    Villager "Well, you tell me!"
    Leyna "What?"
    Villager "As you heard!  explain to me why you have the facilities in such a bad condition, I don't know what kind of weeds you put in the water but..."
    Villager "I've got a rash! look! this is all your fault! especially yours as you're the one in charge of this!"
    Villager "I guess I'll have to talk to the manager and discuss your future in this job"
    Leyna "I-I, please don't! (I haven't been paid for the photo shoots yet...) I need the money... please... how can I make it up to you?"
    Villager "(I can't believe this is working!).... Well... if you get like that... I guess you could make it up to me..."
    Leyna "??? Sure! Tell me what do you need..."
    Villager "First of all, I want you to see what you've done! look closely at the rash I got here!"
    $ show_picture(3, "flashback2")
    $ resolve_scene()
    Villager "That's right, get down!"
    Leyna "(Do I always have to end up with someone's cock so close to my face?)... n-not seeing anything"
    Villager "Ehm... of course! because it's not there! it's here!"
    $ show_picture(4, "flashback3")
    call PlaySound("sound", "audio/Jump2.ogg", volume=0.9, no_loop=True) from _call_PathEV020_0_PlaySound
    $ resolve_scene()
    Leyna "AH!!"
    Villager "Do you see it now?"
    Leyna "(I still don't see anything, but I'd better play along so that this is over as soon as possible) Yes, I see it, Sorry, it's my fault"
    Leyna "(This is so humiliating...)"
    Villager "Exactly... I was thinking of talking to your manager! but seeing that you have recognized your mistakes and that you are willing to help us with this..."
    Villager "We can fix it right now! you only have to do one thing..."
    Leyna "Tell me..."
    Villager "Kiss me down there, one kiss is enough for me!"
    Leyna "A-a kiss? There? I..."
    Villager2 "Yes! and if I were you I'd hurry up, with how full this place is today they could see us at any moment!"
    Leyna "(!!! shit! he's right and... and Johan is on the other side of these curtains...if he would see me in this situation...  I don't know what would happen)"
    Leyna "Okay..."
    $ show_picture(5, "flashback4")
    $ resolve_scene()
    Villager "That's right, good girl"
    Villager2 "(What a fucker! Now I want some too.... Hehehehe I have an idea)"
    Villager2 "Oh boy, you've had a bath too, haven't you, girl? I'm the town doctor and I can see you've got a little problem down there too"
    Leyna "???"
    Villager2 "Yes, this looks bad, I'm going to inspect you a little bit..."
    $ show_picture(6, "flashback5")
    call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV020_0_PlaySound_1
    $ resolve_scene()
    Leyna "Aahh..."
    Villager "You see? we all help each other here hahahaha"
    Villager2 "Exactly! and it looks like I'm helping you out quite a bit hehehe! you're dripping"
    pause
    $ show_picture(7, "flashback6")
    stop bgs fadeout 1
    $ resolve_scene()
    Leyna "Ah ah ah ah... D-don't keep going... (We could be seen at any moment... I can't go on with this... Johan is right there... but it feels soooo good)"
    if switch("infusion"):
        $ resolve_scene()
        Leyna "...(I can't help it, I just want it to go on a little longer... I need it or I'll go crazy...)"
        $ show_picture(8, "flashback7")
        $ resolve_scene()
        Villager2 "I'm going to inspect you a little more thoroughly, sweetie..."
        Leyna "I... we shouldn't... my husband..."
        Villager2 "Oh... it will only take a few minutes, don't worry, it won't take long at all"
        Leyna "!!!"
        pause
        $ show_picture(9, "flashback8")
        $ resolve_scene()
        Villager2 "That's it...that's it, all the way to the deep end very good... wow You're really tight down there... You needed this, huh?"
        Leyna "Aahhh... (My God it's huge... it's going to break me in half... )... Yeah? ah ah ah"
        Villager "(What a son of a bitch, I could have thought of that myself...)"
        Villager2 "All right, ready? I'm going to help you really good"
        pause
        $ show_picture(10, "flashback9")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV020_0_PlaySound_2
        $ resolve_scene()
        Leyna "AH! AH! AH!"
        Villager2 "That's it! do you like it? you don't need to tell me I know you love it, bitch!"
        Leyna "Hmmmm!! YES YES!"
        Villager "Wow, You were right, this girl is a real slut"
        Villager2 "I told you! A girl dressed like that surrounded by men is just begging to be fucked!"
        Leyna "N-no! (Why does it make me so horny to be talked to like that? I would never...) ... AAAH!!! HMMM..."
        Villager2 "What's wrong? Your husband doesn't fuck you like he should? I'm sure that's it... well, don't worry, we'll take care of you, slut!"
        Leyna "S-stop... I... Ah ah ah!"
        pause
        $ show_picture(11, "flashback10")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV020_0_PlaySound_3
        $ resolve_scene()
        Villager3 "Hey, you wouldn't happen to have any spare towels lying around, would you? FUCK! WHAT THE FUCK IS GOING ON?"
        stop bgs fadeout 1
        Leyna "!!!"
        Villager "!!!! Oh Shit"
        Villager2 "Shit..."
        Leyna "Get off of me NOW!"
        "vILLAGER 2: Tch... Yeah yeah..."
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
        $ fade_in()
    if not switch("infusion"):
        $ resolve_scene()
        "lEYNA: Sto-stop... please stop..."
        Villager2 "What? no way, I'll help you right away and you'll be much better"
        Leyna "N-NO! I've done what you wanted, leave me alone! I have to keep working"
        Villager2 "Fuck... okay as you wish...."
        $ fade_out()
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(4)
        $ erase_picture(5)
        $ erase_picture(6)
        $ erase_picture(7)
        $ fade_in()
    $ resolve_scene()
    Leyna "N-no! I can't go on like this with this job! it's too much! I'll talk to the manager and..."
    Leyna "I'm sure I'll find something else while I'm waiting for the payments from my modeling job... maybe if I ask the bar again? I hope so..."
    $ set_switch("flashback", True)
    call GalleryViewed("flashback") from _call_PathEV020_0_GalleryViewed
    Leyna "It can't get any worse than this, can it?"
    $ set_self_switch("Path","PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v3","A",True)
    return False

label PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v3_1:
    call PauseForBalloon("PathEV020_1") from _call_PathEV020_1_PauseForBalloon
    Leyna ".... Shit... Do I really have to do this? ... Who am I kidding? It's normal for Johan to get like this..."
    Leyna "The strange thing is that he didn't realize before that something strange was going on... just remembering what happened the other day..."
    $ fade_out()
    $ show_picture(1, "hotspringsjuntos6")
    $ fade_in()
    $ resolve_scene()
    "THE LAST DAY LEYNA WENT TO WORK..."
    Villager "Hey... You're the new girl working here, right?"
    Leyna "Hmmm yes, it's me, do you need anything?"
    Villager "Yes, my friend and I have a problem, come with us and we'll show you, it's a little delicate"
    Leyna "Su-sure"
    $ show_picture(2, "flashback1")
    $ resolve_scene()
    Leyna "Tell me, what is the problem?"
    Villager "Well, you tell me!"
    Leyna "What?"
    Villager "As you heard!  explain to me why you have the facilities in such a bad condition, I don't know what kind of weeds you put in the water but..."
    Villager "I've got a rash! look! this is all your fault! especially yours as you're the one in charge of this!"
    Villager "I guess I'll have to talk to the manager and discuss your future in this job"
    Leyna "I-I, please don't! (I haven't been paid for the photo shoots yet...) I need the money... please... how can I make it up to you?"
    Villager "(I can't believe this is working!).... Well... if you get like that... I guess you could make it up to me..."
    Leyna "??? Sure! Tell me what do you need..."
    Villager "First of all, I want you to see what you've done! look closely at the rash I got here!"
    $ show_picture(3, "flashback2")
    $ resolve_scene()
    Villager "That's right, get down!"
    Leyna "(Do I always have to end up with someone's cock so close to my face?)... n-not seeing anything"
    Villager "Ehm... of course! because it's not there! it's here!"
    $ show_picture(4, "flashback3")
    call PlaySound("sound", "audio/Jump2.ogg", volume=0.9, no_loop=True) from _call_PathEV020_1_PlaySound
    $ resolve_scene()
    Leyna "AH!!"
    Villager "Do you see it now?"
    Leyna "(I still don't see anything, but I'd better play along so that this is over as soon as possible) Yes, I see it, Sorry, it's my fault"
    Leyna "(This is so humiliating...)"
    Villager "Exactly... I was thinking of talking to your manager! but seeing that you have recognized your mistakes and that you are willing to help us with this..."
    Villager "We can fix it right now! you only have to do one thing..."
    Leyna "Tell me..."
    Villager "Kiss me down there, one kiss is enough for me!"
    Leyna "A-a kiss? There? I..."
    Villager2 "Yes! and if I were you I'd hurry up, with how full this place is today they could see us at any moment!"
    Leyna "(!!! shit! he's right and... and Johan is on the other side of these curtains...if he would see me in this situation...  I don't know what would happen)"
    Leyna "Okay..."
    $ show_picture(5, "flashback4")
    $ resolve_scene()
    Villager "That's right, good girl"
    Villager2 "(What a fucker! Now I want some too.... Hehehehe I have an idea)"
    Villager2 "Oh boy, you've had a bath too, haven't you, girl? I'm the town doctor and I can see you've got a little problem down there too"
    Leyna "???"
    Villager2 "Yes, this looks bad, I'm going to inspect you a little bit..."
    $ show_picture(6, "flashback5")
    call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV020_1_PlaySound_1
    $ resolve_scene()
    Leyna "Aahh..."
    Villager "You see? we all help each other here hahahaha"
    Villager2 "Exactly! and it looks like I'm helping you out quite a bit hehehe! you're dripping"
    pause
    $ show_picture(7, "flashback6")
    stop bgs fadeout 1
    $ resolve_scene()
    Leyna "Ah ah ah ah... D-don't keep going... (We could be seen at any moment... I can't go on with this... Johan is right there... but it feels soooo good)"
    if switch("infusion"):
        $ resolve_scene()
        Leyna "...(I can't help it, I just want it to go on a little longer... I need it or I'll go crazy...)"
        $ show_picture(8, "flashback7")
        $ resolve_scene()
        Villager2 "I'm going to inspect you a little more thoroughly, sweetie..."
        Leyna "I... we shouldn't... my husband..."
        Villager2 "Oh... it will only take a few minutes, don't worry, it won't take long at all"
        Leyna "!!!"
        pause
        $ show_picture(9, "flashback8")
        $ resolve_scene()
        Villager2 "That's it...that's it, all the way to the deep end very good... wow You're really tight down there... You needed this, huh?"
        Leyna "Aahhh... (My God it's huge... it's going to break me in half... )... Yeah? ah ah ah"
        Villager "(What a son of a bitch, I could have thought of that myself...)"
        Villager2 "All right, ready? I'm going to help you really good"
        pause
        $ show_picture(10, "flashback9")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV020_1_PlaySound_2
        $ resolve_scene()
        Leyna "AH! AH! AH!"
        Villager2 "That's it! do you like it? you don't need to tell me I know you love it, bitch!"
        Leyna "Hmmmm!! YES YES!"
        Villager "Wow, You were right, this girl is a real slut"
        Villager2 "I told you! A girl dressed like that surrounded by men is just begging to be fucked!"
        Leyna "N-no! (Why does it make me so horny to be talked to like that? I would never...) ... AAAH!!! HMMM..."
        Villager2 "What's wrong? Your husband doesn't fuck you like he should? I'm sure that's it... well, don't worry, we'll take care of you, slut!"
        Leyna "S-stop... I... Ah ah ah!"
        pause
        $ show_picture(11, "flashback10")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV020_1_PlaySound_3
        $ resolve_scene()
        Villager3 "Hey, you wouldn't happen to have any spare towels lying around, would you? FUCK! WHAT THE FUCK IS GOING ON?"
        stop bgs fadeout 1
        Leyna "!!!"
        Villager "!!!! Oh Shit"
        Villager2 "Shit..."
        Leyna "Get off of me NOW!"
        "vILLAGER 2: Tch... Yeah yeah..."
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
        $ fade_in()
    if not switch("infusion"):
        $ resolve_scene()
        "lEYNA: Sto-stop... please stop..."
        Villager2 "What? no way, I'll help you right away and you'll be much better"
        Leyna "N-NO! I've done what you wanted, leave me alone! I have to keep working"
        Villager2 "Fuck... okay as you wish...."
        $ fade_out()
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(4)
        $ erase_picture(5)
        $ erase_picture(6)
        $ erase_picture(7)
        $ fade_in()
    $ resolve_scene()
    Leyna "N-no! I can't go on like this with this job! it's too much! I'll talk to the manager and..."
    Leyna "I'm sure I'll find something else while I'm waiting for the payments from my modeling job... maybe if I ask the bar again? I hope so..."
    $ set_switch("flashback", True)
    call GalleryViewed("flashback") from _call_PathEV020_1_GalleryViewed
    Leyna "It can't get any worse than this, can it?"
    $ set_self_switch("Path","PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v3","A",True)
    return False

label PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v3_3:
    "closed today"
    return False

label PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v3(play_event = True, trigger = None): # event
    if is_erased("PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v3"):
        return None
    elif switch("last_bar"):
        return None
    elif trigger == "event" and switch("party_at_festival"):
        call PlayEvent(play_event, "PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v3_3", "PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v3") from _call_PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v3_3_PlayEvent
        return (1, "", "PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v3_3")
    elif self_switch("Path","PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v3","A"):
        return None
    elif trigger == "event" and bet_together >= 2:
        call PlayEvent(play_event, "PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v3_1", "PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v3") from _call_PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v3_1_PlayEvent
        return (0, "", "PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v3_1")
    elif trigger == "event" and bet_together >= 1:
        call PlayEvent(play_event, "PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v3_0", "PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v3") from _call_PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v3_0_PlayEvent
        return (0, "", "PathShitDoIReallyHaveToDoThisWhoAmIKiddingItsNormalForJohanToGetLikeThis_v3_0")
    return None

label PathWowItLooksLikeTheHotspringsHaveReopened_0:
    call Movement("PathEV021_0", "player", ["L","TURN_U"]) from _call_PathEV021_0_Movement
    $ resolve_scene()
    call PauseForBalloon("PathEV021_0") from _call_PathEV021_0_PauseForBalloon
    Johan "Wow, it looks like the hotsprings have reopened!"
    Leyna "Yes..."
    Johan "shall we enter?"
    Leyna "I don't know... if I feel like it right now..."
    Johan "Come on, this may be the last time we can go, don't you want to take a bath before we leave for good?"
    Leyna "O-okay..."
    Johan "Perfect, let's go then"
    $ fade_out()
    $ show_picture(1, "drunk1")
    $ fade_in()
    $ resolve_scene()
    Leyna "Aaaah..."
    Johan "See? I told you it would be okay, we have to enjoy this before it's over and we have to go home"
    $ show_picture(2, "drunk2")
    $ resolve_scene()
    Leyna "Hehehee yes... you're right"
    Johan "Ahhh... once I deliver the article I will invite you to a nice restaurant"
    Leyna "Hmmm I've always wanted to go to the posh restaurant downtown, the one with the meat where the cook sprinkles salt in a funny way"
    Johan "hahahaha and I... we'll be able to go there soon, you'll see"
    Leyna "Great... God I'm so comfortable here..."
    Johan "Yes... let's stay for a while"
    Leyna "I thought you wanted to go see how they build the festival events?"
    Johan "Well... I've changed my mind, it's not that important hahahaha"
    Leyna "Yes... you're right hahahaha"
    $ show_picture(3, "drunk3")
    $ resolve_scene()
    Villager "OH Hey guys! How's it going?"
    Leyna "!!! Oh hey, how are you?"
    Johan "Hey guys! we were enjoying the hotsprings for the last time before we left!"
    Villager "Great, I'm sure you will miss them in the city, there are no things like this there, right?"
    Johan "There is something... but certainly not as good as this, which is at another level"
    Villager2 "Hahahahaha great, we came to relax a bit before the end of the festival, we brought some craft beer that my dad makes"
    Villager2 "Do you want? we have brought plenty"
    Leyna "I don't know if we should.... we have been drinking a lot lately"
    Johan "Well let's drink anyway, it's the last day of the festival so I guess we should do what everyone else does, don't you think?"
    Leyna "... yeah I guess you're right.... hahahaha come on pass me that beer!"
    Johan "Hahaha Nice"
    $ fade_out()
    $ show_picture(4, "drunk4")
    $ fade_in()
    $ resolve_scene()
    "Some time later... "
    Johan "Wow... that beer is really strong..."
    Leyna "Hip! yeah... we haven't tried this one yet... it tastes a little weird but it's good"
    "Villager2: I'm glad you like it, it's the family's specialty"
    Johan "Hip! yes, at least I like it a lot, give me another sip!"
    Villager2 "Sure, take whatever you want, we have plenty"
    Johan "Thank you very much"
    $ fade_out()
    $ show_picture(5, "drunk5")
    $ fade_in()
    $ resolve_scene()
    Johan "(Wow, I'm a little drunk... and it's so cozy in here... with the hot water and the scent of herbs)"
    Johan "(I shouldn't be sleeping here... but... but it's so good.... and tonight it seems that I didn't sleep very well...)"
    $ show_picture(6, "drunk6")
    $ resolve_scene()
    Johan "(I'm so sleepy... no... I don't think a little snooze will hurt..... Leyna will wake me up in a few minutes... it's ok)"
    Johan "(yes... I'm going to... I'm.....) hmm"
    $ show_picture(7, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "....."
    "......."
    Villager "Oh my! hehehehehe"
    Johan "Hm?..."
    Leyna "Oh ups hahahaha"
    $ show_picture(8, "drunk7")
    $ resolve_scene()
    Villager "I'm glad I came here today hahahaah"
    Villager2 "God... you are amazing Leyna...."
    Leyna "Hahahaha shut up don't be silly"
    pause
    $ show_picture(9, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "....."
    "........"
    Leyna "H-hey stop... we shouldn't..."
    $ show_picture(10, "drunk8")
    $ resolve_scene()
    Villager "Oh come on, it's just fooling around! We're just playing"
    Leyna "But.. Johan"
    Villager2 "Johan is perfectly fine! Look at him, he's sleeping there"
    Leyna "If you say so..."
    $ show_picture(11, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "....."
    "........"
    Leyna "Oh come on, you're both very... big, there's no need to compete"
    $ show_picture(12, "drunk9")
    $ resolve_scene()
    Villager "Hey, we won't have this opportunity again!"
    Leyna "Hehehe well... you don't have to worry... you can be with any girl in town"
    Villager2 "Does that include you beautiful?"
    Leyna "I... Well..."
    $ show_picture(13, "pantallanegro", scale=(120, 120), width=816, height=600)
    if switch("corruption_high"):
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV021_0_PlaySound
        $ resolve_scene()
        "....."
        "........"
        Leyna "Ah ah ah Oh My god!"
        $ show_picture(14, "drunk10")
        $ resolve_scene()
        Villager "You like it slut? look what you're doing in front of your husband"
        Leyna "Yes I like it! keep it up! keep it up!"
        Villager2 "Shut up and suck my fucking cock"
        Leyna "Hmmmf! (cough cough) you're driving me crazy"
        Villager "God I love this bitch!"
        Johan "hmmm?... (w-what's going on?)"
        Leyna "Shit"
        Villager "Is he... is he awake?"
        Villager2 "Nah no way... let's go on!"
        stop bgs fadeout 1
        $ erase_picture(14)
    $ resolve_scene()
    "....."
    "........"
    $ show_picture(14, "drunk11")
    $ resolve_scene()
    Leyna "Johan? Johan!"
    Johan "Hmm! ah? ah!"
    $ show_picture(15, "drunk12")
    $ resolve_scene()
    Leyna "Johan! hahahahaha you have fallen asleep"
    Villager "Hey Johan! Looks like the beer is really good eh? hahahaha"
    Johan "Hmmm yeah... sorry guys, between the hot water and that...."
    Johan "Le-leyna?... you're ... nude"
    Leyna "Oh yeah... sorry I must have lost the towel somewhere"
    Leyna "But it's okay, I'm used to being naked in front of others after everything that has happened these days"
    Johan "I see... W-well, we should get going to the festival. How long have I been asleep?"
    Villager2 "At least one hour"
    Johan "One hour? my god and what have you been doing all this time?"
    $ show_picture(16, "drunk13")
    $ resolve_scene()
    Leyna "..."
    Villager "Drinking beer of course hahahaha come on let's go, we're all wrinkled from being here that long"
    Johan "Yes... you are right"
    Leyna "Let's get dressed up and go to the festival honey"
    Johan "Y-yeah"
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
    call TransferPlayer("Path", "PathEV021_0", 10, 10, direction=4) from _call_PathEV021_0_TransferPlayer
    $ set_switch("last_hotsprings", True)
    call Movement("PathEV021_0", "player", ["L","L","TURN_R"]) from _call_PathEV021_0_Movement_1
    $ fade_in()
    $ resolve_scene()
    Johan "Well... it's time, we should get into the festival... are you ready?"
    Leyna "I'm a little nervous, I'm not going to fool you... I can't believe that all this is coming to an end..."
    Johan "Yeah... I've also gotten used to being in this town... and all in such a short time"
    "Johan. Well... let's not waste any more time, let's go inside and enjoy the experience"
    call GalleryViewed("drunk") from _call_PathEV021_0_GalleryViewed
    Leyna "Yes!"
    return False

label PathWowItLooksLikeTheHotspringsHaveReopened(play_event = True, trigger = None): # event
    if is_erased("PathWowItLooksLikeTheHotspringsHaveReopened"):
        return None
    elif switch("last_hotsprings"):
        return None
    elif trigger == "event" and switch("last_bar"):
        call PlayEvent(play_event, "PathWowItLooksLikeTheHotspringsHaveReopened_0", "PathWowItLooksLikeTheHotspringsHaveReopened") from _call_PathWowItLooksLikeTheHotspringsHaveReopened_0_PlayEvent
        return (0, "", "PathWowItLooksLikeTheHotspringsHaveReopened_0")
    return None

label PathWowItLooksLikeTheHotspringsHaveReopened_v2_0:
    call Movement("PathEV022_0", "player", ["L","TURN_U"]) from _call_PathEV022_0_Movement
    $ resolve_scene()
    call PauseForBalloon("PathEV022_0") from _call_PathEV022_0_PauseForBalloon
    Johan "Wow, it looks like the hotsprings have reopened!"
    Leyna "Yes..."
    Johan "shall we enter?"
    Leyna "I don't know... if I feel like it right now..."
    Johan "Come on, this may be the last time we can go, don't you want to take a bath before we leave for good?"
    Leyna "O-okay..."
    Johan "Perfect, let's go then"
    $ fade_out()
    $ show_picture(1, "drunk1")
    $ fade_in()
    $ resolve_scene()
    Leyna "Aaaah..."
    Johan "See? I told you it would be okay, we have to enjoy this before it's over and we have to go home"
    $ show_picture(2, "drunk2")
    $ resolve_scene()
    Leyna "Hehehee yes... you're right"
    Johan "Ahhh... once I deliver the article I will invite you to a nice restaurant"
    Leyna "Hmmm I've always wanted to go to the posh restaurant downtown, the one with the meat where the cook sprinkles salt in a funny way"
    Johan "hahahaha and I... we'll be able to go there soon, you'll see"
    Leyna "Great... God I'm so comfortable here..."
    Johan "Yes... let's stay for a while"
    Leyna "I thought you wanted to go see how they build the festival events?"
    Johan "Well... I've changed my mind, it's not that important hahahaha"
    Leyna "Yes... you're right hahahaha"
    $ show_picture(3, "drunk3")
    $ resolve_scene()
    Villager "OH Hey guys! How's it going?"
    Leyna "!!! Oh hey, how are you?"
    Johan "Hey guys! we were enjoying the hotsprings for the last time before we left!"
    Villager "Great, I'm sure you will miss them in the city, there are no things like this there, right?"
    Johan "There is something... but certainly not as good as this, which is at another level"
    Villager2 "Hahahahaha great, we came to relax a bit before the end of the festival, we brought some craft beer that my dad makes"
    Villager2 "Do you want? we have brought plenty"
    Leyna "I don't know if we should.... we have been drinking a lot lately"
    Johan "Well let's drink anyway, it's the last day of the festival so I guess we should do what everyone else does, don't you think?"
    Leyna "... yeah I guess you're right.... hahahaha come on pass me that beer!"
    Johan "Hahaha Nice"
    $ fade_out()
    $ show_picture(4, "drunk4")
    $ fade_in()
    $ resolve_scene()
    "Some time later... "
    Johan "Wow... that beer is really strong..."
    Leyna "Hip! yeah... we haven't tried this one yet... it tastes a little weird but it's good"
    "Villager2: I'm glad you like it, it's the family's specialty"
    Johan "Hip! yes, at least I like it a lot, give me another sip!"
    Villager2 "Sure, take whatever you want, we have plenty"
    Johan "Thank you very much"
    $ fade_out()
    $ show_picture(5, "drunk5")
    $ fade_in()
    $ resolve_scene()
    Johan "(Wow, I'm a little drunk... and it's so cozy in here... with the hot water and the scent of herbs)"
    Johan "(I shouldn't be sleeping here... but... but it's so good.... and tonight it seems that I didn't sleep very well...)"
    $ show_picture(6, "drunk6")
    $ resolve_scene()
    Johan "(I'm so sleepy... no... I don't think a little snooze will hurt..... Leyna will wake me up in a few minutes... it's ok)"
    Johan "(yes... I'm going to... I'm.....) hmm"
    $ show_picture(7, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "....."
    "......."
    Villager "Oh my! hehehehehe"
    Johan "Hm?..."
    Leyna "Oh ups hahahaha"
    $ show_picture(8, "drunk7")
    $ resolve_scene()
    Villager "I'm glad I came here today hahahaah"
    Villager2 "God... you are amazing Leyna...."
    Leyna "Hahahaha shut up don't be silly"
    pause
    $ show_picture(9, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "....."
    "........"
    Leyna "H-hey stop... we shouldn't..."
    $ show_picture(10, "drunk8")
    $ resolve_scene()
    Villager "Oh come on, it's just fooling around! We're just playing"
    Leyna "But.. Johan"
    Villager2 "Johan is perfectly fine! Look at him, he's sleeping there"
    Leyna "If you say so..."
    $ show_picture(11, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "....."
    "........"
    Leyna "Oh come on, you're both very... big, there's no need to compete"
    $ show_picture(12, "drunk9")
    $ resolve_scene()
    Villager "Hey, we won't have this opportunity again!"
    Leyna "Hehehe well... you don't have to worry... you can be with any girl in town"
    Villager2 "Does that include you beautiful?"
    Leyna "I... Well..."
    $ show_picture(13, "pantallanegro", scale=(120, 120), width=816, height=600)
    if switch("corruption_high"):
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV022_0_PlaySound
        $ resolve_scene()
        "....."
        "........"
        Leyna "Ah ah ah Oh My god!"
        $ show_picture(14, "drunk10")
        $ resolve_scene()
        Villager "You like it slut? look what you're doing in front of your husband"
        Leyna "Yes I like it! keep it up! keep it up!"
        Villager2 "Shut up and suck my fucking cock"
        Leyna "Hmmmf! (cough cough) you're driving me crazy"
        Villager "God I love this bitch!"
        Johan "hmmm?... (w-what's going on?)"
        Leyna "Shit"
        Villager "Is he... is he awake?"
        Villager2 "Nah no way... let's go on!"
        stop bgs fadeout 1
        $ erase_picture(14)
    $ resolve_scene()
    "....."
    "........"
    $ show_picture(14, "drunk11")
    $ resolve_scene()
    Leyna "Johan? Johan!"
    Johan "Hmm! ah? ah!"
    $ show_picture(15, "drunk12")
    $ resolve_scene()
    Leyna "Johan! hahahahaha you have fallen asleep"
    Villager "Hey Johan! Looks like the beer is really good eh? hahahaha"
    Johan "Hmmm yeah... sorry guys, between the hot water and that...."
    Johan "Le-leyna?... you're ... nude"
    Leyna "Oh yeah... sorry I must have lost the towel somewhere"
    Leyna "But it's okay, I'm used to being naked in front of others after everything that has happened these days"
    Johan "I see... W-well, we should get going to the festival. How long have I been asleep?"
    Villager2 "At least one hour"
    Johan "One hour? my god and what have you been doing all this time?"
    $ show_picture(16, "drunk13")
    $ resolve_scene()
    Leyna "..."
    Villager "Drinking beer of course hahahaha come on let's go, we're all wrinkled from being here that long"
    Johan "Yes... you are right"
    Leyna "Let's get dressed up and go to the festival honey"
    Johan "Y-yeah"
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
    call TransferPlayer("Path", "PathEV022_0", 10, 10, direction=4) from _call_PathEV022_0_TransferPlayer
    $ set_switch("last_hotsprings", True)
    call Movement("PathEV022_0", "player", ["L","L","TURN_R"]) from _call_PathEV022_0_Movement_1
    $ fade_in()
    $ resolve_scene()
    Johan "Well... it's time, we should get into the festival... are you ready?"
    Leyna "I'm a little nervous, I'm not going to fool you... I can't believe that all this is coming to an end..."
    Johan "Yeah... I've also gotten used to being in this town... and all in such a short time"
    "Johan. Well... let's not waste any more time, let's go inside and enjoy the experience"
    call GalleryViewed("drunk") from _call_PathEV022_0_GalleryViewed
    Leyna "Yes!"
    return False

label PathWowItLooksLikeTheHotspringsHaveReopened_v2(play_event = True, trigger = None): # event
    if is_erased("PathWowItLooksLikeTheHotspringsHaveReopened_v2"):
        return None
    elif switch("last_hotsprings"):
        return None
    elif trigger == "event" and switch("last_bar"):
        call PlayEvent(play_event, "PathWowItLooksLikeTheHotspringsHaveReopened_v2_0", "PathWowItLooksLikeTheHotspringsHaveReopened_v2") from _call_PathWowItLooksLikeTheHotspringsHaveReopened_v2_0_PlayEvent
        return (0, "", "PathWowItLooksLikeTheHotspringsHaveReopened_v2_0")
    return None

label PathWowItLooksLikeTheHotspringsHaveReopened_v3_0:
    call Movement("PathEV023_0", "player", ["L","TURN_U"]) from _call_PathEV023_0_Movement
    $ resolve_scene()
    call PauseForBalloon("PathEV023_0") from _call_PathEV023_0_PauseForBalloon
    Johan "Wow, it looks like the hotsprings have reopened!"
    Leyna "Yes..."
    Johan "shall we enter?"
    Leyna "I don't know... if I feel like it right now..."
    Johan "Come on, this may be the last time we can go, don't you want to take a bath before we leave for good?"
    Leyna "O-okay..."
    Johan "Perfect, let's go then"
    $ fade_out()
    $ show_picture(1, "drunk1")
    $ fade_in()
    $ resolve_scene()
    Leyna "Aaaah..."
    Johan "See? I told you it would be okay, we have to enjoy this before it's over and we have to go home"
    $ show_picture(2, "drunk2")
    $ resolve_scene()
    Leyna "Hehehee yes... you're right"
    Johan "Ahhh... once I deliver the article I will invite you to a nice restaurant"
    Leyna "Hmmm I've always wanted to go to the posh restaurant downtown, the one with the meat where the cook sprinkles salt in a funny way"
    Johan "hahahaha and I... we'll be able to go there soon, you'll see"
    Leyna "Great... God I'm so comfortable here..."
    Johan "Yes... let's stay for a while"
    Leyna "I thought you wanted to go see how they build the festival events?"
    Johan "Well... I've changed my mind, it's not that important hahahaha"
    Leyna "Yes... you're right hahahaha"
    $ show_picture(3, "drunk3")
    $ resolve_scene()
    Villager "OH Hey guys! How's it going?"
    Leyna "!!! Oh hey, how are you?"
    Johan "Hey guys! we were enjoying the hotsprings for the last time before we left!"
    Villager "Great, I'm sure you will miss them in the city, there are no things like this there, right?"
    Johan "There is something... but certainly not as good as this, which is at another level"
    Villager2 "Hahahahaha great, we came to relax a bit before the end of the festival, we brought some craft beer that my dad makes"
    Villager2 "Do you want? we have brought plenty"
    Leyna "I don't know if we should.... we have been drinking a lot lately"
    Johan "Well let's drink anyway, it's the last day of the festival so I guess we should do what everyone else does, don't you think?"
    Leyna "... yeah I guess you're right.... hahahaha come on pass me that beer!"
    Johan "Hahaha Nice"
    $ fade_out()
    $ show_picture(4, "drunk4")
    $ fade_in()
    $ resolve_scene()
    "Some time later... "
    Johan "Wow... that beer is really strong..."
    Leyna "Hip! yeah... we haven't tried this one yet... it tastes a little weird but it's good"
    "Villager2: I'm glad you like it, it's the family's specialty"
    Johan "Hip! yes, at least I like it a lot, give me another sip!"
    Villager2 "Sure, take whatever you want, we have plenty"
    Johan "Thank you very much"
    $ fade_out()
    $ show_picture(5, "drunk5")
    $ fade_in()
    $ resolve_scene()
    Johan "(Wow, I'm a little drunk... and it's so cozy in here... with the hot water and the scent of herbs)"
    Johan "(I shouldn't be sleeping here... but... but it's so good.... and tonight it seems that I didn't sleep very well...)"
    $ show_picture(6, "drunk6")
    $ resolve_scene()
    Johan "(I'm so sleepy... no... I don't think a little snooze will hurt..... Leyna will wake me up in a few minutes... it's ok)"
    Johan "(yes... I'm going to... I'm.....) hmm"
    $ show_picture(7, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "....."
    "......."
    Villager "Oh my! hehehehehe"
    Johan "Hm?..."
    Leyna "Oh ups hahahaha"
    $ show_picture(8, "drunk7")
    $ resolve_scene()
    Villager "I'm glad I came here today hahahaah"
    Villager2 "God... you are amazing Leyna...."
    Leyna "Hahahaha shut up don't be silly"
    pause
    $ show_picture(9, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "....."
    "........"
    Leyna "H-hey stop... we shouldn't..."
    $ show_picture(10, "drunk8")
    $ resolve_scene()
    Villager "Oh come on, it's just fooling around! We're just playing"
    Leyna "But.. Johan"
    Villager2 "Johan is perfectly fine! Look at him, he's sleeping there"
    Leyna "If you say so..."
    $ show_picture(11, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "....."
    "........"
    Leyna "Oh come on, you're both very... big, there's no need to compete"
    $ show_picture(12, "drunk9")
    $ resolve_scene()
    Villager "Hey, we won't have this opportunity again!"
    Leyna "Hehehe well... you don't have to worry... you can be with any girl in town"
    Villager2 "Does that include you beautiful?"
    Leyna "I... Well..."
    $ show_picture(13, "pantallanegro", scale=(120, 120), width=816, height=600)
    if switch("corruption_high"):
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV023_0_PlaySound
        $ resolve_scene()
        "....."
        "........"
        Leyna "Ah ah ah Oh My god!"
        $ show_picture(14, "drunk10")
        $ resolve_scene()
        Villager "You like it slut? look what you're doing in front of your husband"
        Leyna "Yes I like it! keep it up! keep it up!"
        Villager2 "Shut up and suck my fucking cock"
        Leyna "Hmmmf! (cough cough) you're driving me crazy"
        Villager "God I love this bitch!"
        Johan "hmmm?... (w-what's going on?)"
        Leyna "Shit"
        Villager "Is he... is he awake?"
        Villager2 "Nah no way... let's go on!"
        stop bgs fadeout 1
        $ erase_picture(14)
    $ resolve_scene()
    "....."
    "........"
    $ show_picture(14, "drunk11")
    $ resolve_scene()
    Leyna "Johan? Johan!"
    Johan "Hmm! ah? ah!"
    $ show_picture(15, "drunk12")
    $ resolve_scene()
    Leyna "Johan! hahahahaha you have fallen asleep"
    Villager "Hey Johan! Looks like the beer is really good eh? hahahaha"
    Johan "Hmmm yeah... sorry guys, between the hot water and that...."
    Johan "Le-leyna?... you're ... nude"
    Leyna "Oh yeah... sorry I must have lost the towel somewhere"
    Leyna "But it's okay, I'm used to being naked in front of others after everything that has happened these days"
    Johan "I see... W-well, we should get going to the festival. How long have I been asleep?"
    Villager2 "At least one hour"
    Johan "One hour? my god and what have you been doing all this time?"
    $ show_picture(16, "drunk13")
    $ resolve_scene()
    Leyna "..."
    Villager "Drinking beer of course hahahaha come on let's go, we're all wrinkled from being here that long"
    Johan "Yes... you are right"
    Leyna "Let's get dressed up and go to the festival honey"
    Johan "Y-yeah"
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
    call TransferPlayer("Path", "PathEV023_0", 10, 10, direction=4) from _call_PathEV023_0_TransferPlayer
    $ set_switch("last_hotsprings", True)
    call Movement("PathEV023_0", "player", ["L","L","TURN_R"]) from _call_PathEV023_0_Movement_1
    $ fade_in()
    $ resolve_scene()
    Johan "Well... it's time, we should get into the festival... are you ready?"
    Leyna "I'm a little nervous, I'm not going to fool you... I can't believe that all this is coming to an end..."
    Johan "Yeah... I've also gotten used to being in this town... and all in such a short time"
    "Johan. Well... let's not waste any more time, let's go inside and enjoy the experience"
    call GalleryViewed("drunk") from _call_PathEV023_0_GalleryViewed
    Leyna "Yes!"
    return False

label PathWowItLooksLikeTheHotspringsHaveReopened_v3(play_event = True, trigger = None): # event
    if is_erased("PathWowItLooksLikeTheHotspringsHaveReopened_v3"):
        return None
    elif switch("last_hotsprings"):
        return None
    elif trigger == "event" and switch("last_bar"):
        call PlayEvent(play_event, "PathWowItLooksLikeTheHotspringsHaveReopened_v3_0", "PathWowItLooksLikeTheHotspringsHaveReopened_v3") from _call_PathWowItLooksLikeTheHotspringsHaveReopened_v3_0_PlayEvent
        return (0, "", "PathWowItLooksLikeTheHotspringsHaveReopened_v3_0")
    return None

label PathWowItLooksLikeTheHotspringsHaveReopened_v4_0:
    call Movement("PathEV024_0", "player", ["L","TURN_U"]) from _call_PathEV024_0_Movement
    $ resolve_scene()
    call PauseForBalloon("PathEV024_0") from _call_PathEV024_0_PauseForBalloon
    Johan "Wow, it looks like the hotsprings have reopened!"
    Leyna "Yes..."
    Johan "shall we enter?"
    Leyna "I don't know... if I feel like it right now..."
    Johan "Come on, this may be the last time we can go, don't you want to take a bath before we leave for good?"
    Leyna "O-okay..."
    Johan "Perfect, let's go then"
    $ fade_out()
    $ show_picture(1, "drunk1")
    $ fade_in()
    $ resolve_scene()
    Leyna "Aaaah..."
    Johan "See? I told you it would be okay, we have to enjoy this before it's over and we have to go home"
    $ show_picture(2, "drunk2")
    $ resolve_scene()
    Leyna "Hehehee yes... you're right"
    Johan "Ahhh... once I deliver the article I will invite you to a nice restaurant"
    Leyna "Hmmm I've always wanted to go to the posh restaurant downtown, the one with the meat where the cook sprinkles salt in a funny way"
    Johan "hahahaha and I... we'll be able to go there soon, you'll see"
    Leyna "Great... God I'm so comfortable here..."
    Johan "Yes... let's stay for a while"
    Leyna "I thought you wanted to go see how they build the festival events?"
    Johan "Well... I've changed my mind, it's not that important hahahaha"
    Leyna "Yes... you're right hahahaha"
    $ show_picture(3, "drunk3")
    $ resolve_scene()
    Villager "OH Hey guys! How's it going?"
    Leyna "!!! Oh hey, how are you?"
    Johan "Hey guys! we were enjoying the hotsprings for the last time before we left!"
    Villager "Great, I'm sure you will miss them in the city, there are no things like this there, right?"
    Johan "There is something... but certainly not as good as this, which is at another level"
    Villager2 "Hahahahaha great, we came to relax a bit before the end of the festival, we brought some craft beer that my dad makes"
    Villager2 "Do you want? we have brought plenty"
    Leyna "I don't know if we should.... we have been drinking a lot lately"
    Johan "Well let's drink anyway, it's the last day of the festival so I guess we should do what everyone else does, don't you think?"
    Leyna "... yeah I guess you're right.... hahahaha come on pass me that beer!"
    Johan "Hahaha Nice"
    $ fade_out()
    $ show_picture(4, "drunk4")
    $ fade_in()
    $ resolve_scene()
    "Some time later... "
    Johan "Wow... that beer is really strong..."
    Leyna "Hip! yeah... we haven't tried this one yet... it tastes a little weird but it's good"
    "Villager2: I'm glad you like it, it's the family's specialty"
    Johan "Hip! yes, at least I like it a lot, give me another sip!"
    Villager2 "Sure, take whatever you want, we have plenty"
    Johan "Thank you very much"
    $ fade_out()
    $ show_picture(5, "drunk5")
    $ fade_in()
    $ resolve_scene()
    Johan "(Wow, I'm a little drunk... and it's so cozy in here... with the hot water and the scent of herbs)"
    Johan "(I shouldn't be sleeping here... but... but it's so good.... and tonight it seems that I didn't sleep very well...)"
    $ show_picture(6, "drunk6")
    $ resolve_scene()
    Johan "(I'm so sleepy... no... I don't think a little snooze will hurt..... Leyna will wake me up in a few minutes... it's ok)"
    Johan "(yes... I'm going to... I'm.....) hmm"
    $ show_picture(7, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "....."
    "......."
    Villager "Oh my! hehehehehe"
    Johan "Hm?..."
    Leyna "Oh ups hahahaha"
    $ show_picture(8, "drunk7")
    $ resolve_scene()
    Villager "I'm glad I came here today hahahaah"
    Villager2 "God... you are amazing Leyna...."
    Leyna "Hahahaha shut up don't be silly"
    pause
    $ show_picture(9, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "....."
    "........"
    Leyna "H-hey stop... we shouldn't..."
    $ show_picture(10, "drunk8")
    $ resolve_scene()
    Villager "Oh come on, it's just fooling around! We're just playing"
    Leyna "But.. Johan"
    Villager2 "Johan is perfectly fine! Look at him, he's sleeping there"
    Leyna "If you say so..."
    $ show_picture(11, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "....."
    "........"
    Leyna "Oh come on, you're both very... big, there's no need to compete"
    $ show_picture(12, "drunk9")
    $ resolve_scene()
    Villager "Hey, we won't have this opportunity again!"
    Leyna "Hehehe well... you don't have to worry... you can be with any girl in town"
    Villager2 "Does that include you beautiful?"
    Leyna "I... Well..."
    $ show_picture(13, "pantallanegro", scale=(120, 120), width=816, height=600)
    if switch("corruption_high"):
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_PathEV024_0_PlaySound
        $ resolve_scene()
        "....."
        "........"
        Leyna "Ah ah ah Oh My god!"
        $ show_picture(14, "drunk10")
        $ resolve_scene()
        Villager "You like it slut? look what you're doing in front of your husband"
        Leyna "Yes I like it! keep it up! keep it up!"
        Villager2 "Shut up and suck my fucking cock"
        Leyna "Hmmmf! (cough cough) you're driving me crazy"
        Villager "God I love this bitch!"
        Johan "hmmm?... (w-what's going on?)"
        Leyna "Shit"
        Villager "Is he... is he awake?"
        Villager2 "Nah no way... let's go on!"
        stop bgs fadeout 1
        $ erase_picture(14)
    $ resolve_scene()
    "....."
    "........"
    $ show_picture(14, "drunk11")
    $ resolve_scene()
    Leyna "Johan? Johan!"
    Johan "Hmm! ah? ah!"
    $ show_picture(15, "drunk12")
    $ resolve_scene()
    Leyna "Johan! hahahahaha you have fallen asleep"
    Villager "Hey Johan! Looks like the beer is really good eh? hahahaha"
    Johan "Hmmm yeah... sorry guys, between the hot water and that...."
    Johan "Le-leyna?... you're ... nude"
    Leyna "Oh yeah... sorry I must have lost the towel somewhere"
    Leyna "But it's okay, I'm used to being naked in front of others after everything that has happened these days"
    Johan "I see... W-well, we should get going to the festival. How long have I been asleep?"
    Villager2 "At least one hour"
    Johan "One hour? my god and what have you been doing all this time?"
    $ show_picture(16, "drunk13")
    $ resolve_scene()
    Leyna "..."
    Villager "Drinking beer of course hahahaha come on let's go, we're all wrinkled from being here that long"
    Johan "Yes... you are right"
    Leyna "Let's get dressed up and go to the festival honey"
    Johan "Y-yeah"
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
    call TransferPlayer("Path", "PathEV024_0", 10, 10, direction=4) from _call_PathEV024_0_TransferPlayer
    $ set_switch("last_hotsprings", True)
    call Movement("PathEV024_0", "player", ["L","L","TURN_R"]) from _call_PathEV024_0_Movement_1
    $ fade_in()
    $ resolve_scene()
    Johan "Well... it's time, we should get into the festival... are you ready?"
    Leyna "I'm a little nervous, I'm not going to fool you... I can't believe that all this is coming to an end..."
    Johan "Yeah... I've also gotten used to being in this town... and all in such a short time"
    "Johan. Well... let's not waste any more time, let's go inside and enjoy the experience"
    call GalleryViewed("drunk") from _call_PathEV024_0_GalleryViewed
    Leyna "Yes!"
    return False

label PathWowItLooksLikeTheHotspringsHaveReopened_v4(play_event = True, trigger = None): # event
    if is_erased("PathWowItLooksLikeTheHotspringsHaveReopened_v4"):
        return None
    elif switch("last_hotsprings"):
        return None
    elif trigger == "event" and switch("last_bar"):
        call PlayEvent(play_event, "PathWowItLooksLikeTheHotspringsHaveReopened_v4_0", "PathWowItLooksLikeTheHotspringsHaveReopened_v4") from _call_PathWowItLooksLikeTheHotspringsHaveReopened_v4_0_PlayEvent
        return (0, "", "PathWowItLooksLikeTheHotspringsHaveReopened_v4_0")
    return None

