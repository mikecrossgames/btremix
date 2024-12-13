label CasinoBG:
    $ set_transparency_backgrounds(["bg_casino"])
    $ set_map_backgrounds(["bg_casino"])
    return

label CasinoStart:
    call CasinoBG from _call_CasinoBG
    stop music
    stop bgs
    return

label CasinoEnd:
    return

label CasinohombredelasuerteBase:
    call PauseForBalloon("Casinohombredelasuerte") from _call_Casinohombredelasuerte_PauseForBalloon
    OldMan "Welcome!"
    OldMan "Please take a ticket from the machine at your right, we'll start the draw right away"
    Johan "Okay"
    call Movement("Casinohombredelasuerte", "player", ["R","R","TURN_U"]) from _call_Casinohombredelasuerte_Movement
    call PlaySound("sound", "audio/Computer.ogg", volume=0.9, no_loop=True) from _call_Casinohombredelasuerte_PlaySound
    call Movement("Casinohombredelasuerte", "player", ["TURN_L"]) from _call_Casinohombredelasuerte_Movement_1
    $ resolve_scene()
    Johan "Here you have your ticket Leyna"
    Leyna "Thanks"
    call Movement("Casinohombredelasuerte", "player", ["L","L","U","U","R","TURN_U"]) from _call_Casinohombredelasuerte_Movement_2
    $ resolve_scene()
    OldMan "Ok, we'll wait a little longer for the rest to arrive and we'll do the lottery"
    OldWoman "The rest? Everyone is out having a good time and drinking like crazy, nobody cares about this lottery anymore"
    OldMan "But..."
    OldWoman "No, no buts! Let's get this over with"
    OldMan "Hmmm ... okay, well.. let the lottery begin!"
    call Movement("Casinohombredelasuerte", "Casinopresentador", ["TURN_R"]) from _call_Casinohombredelasuerte_Movement_3
    call PlaySound("sound", "audio/Computer.ogg", volume=0.9, no_loop=True) from _call_Casinohombredelasuerte_PlaySound_1
    $ resolve_scene()
    pause 0.6
    $ resolve_scene()
    call PauseForBalloon("Casinohombredelasuerte") from _call_Casinohombredelasuerte_PauseForBalloon_1
    call Movement("Casinohombredelasuerte", "Casinopresentador", ["TURN_D"]) from _call_Casinohombredelasuerte_Movement_4
    $ resolve_scene()
    OldMan "Okay ... the lucky person this year is ..."
    OldMan "The number 12!"
    ".... ...... ........ ............."
    Leyna "... Th-that's me"
    call Movement("Casinohombredelasuerte", "player", ["TURN_L"]) from _call_Casinohombredelasuerte_Movement_5
    $ resolve_scene()
    call Movement("Casinohombredelasuerte", "Casinovillager1", ["TURN_R"]) from _call_Casinohombredelasuerte_Movement_6
    call Movement("Casinohombredelasuerte", "Casinovillager2", ["TURN_R"]) from _call_Casinohombredelasuerte_Movement_7
    call Movement("Casinohombredelasuerte", "Casinovillager3", ["TURN_L"]) from _call_Casinohombredelasuerte_Movement_8
    call Movement("Casinohombredelasuerte", "Casinovillager4", ["TURN_R"]) from _call_Casinohombredelasuerte_Movement_9
    call Movement("Casinohombredelasuerte", "Casinovillager5", ["TURN_L"]) from _call_Casinohombredelasuerte_Movement_10
    call Movement("Casinohombredelasuerte", "Casinovillager6", ["TURN_L"]) from _call_Casinohombredelasuerte_Movement_11
    call Movement("Casinohombredelasuerte", "Casinovillager7", ["TURN_R"]) from _call_Casinohombredelasuerte_Movement_12
    call Movement("Casinohombredelasuerte", "Casinovillager8", ["TURN_L"]) from _call_Casinohombredelasuerte_Movement_13
    call Movement("Casinohombredelasuerte", "Casinovillager9", ["TURN_R"]) from _call_Casinohombredelasuerte_Movement_14
    call Movement("Casinohombredelasuerte", "Casinovillager10", ["TURN_L"]) from _call_Casinohombredelasuerte_Movement_15
    $ resolve_scene()
    $ resolve_scene()
    $ resolve_scene()
    $ resolve_scene()
    $ resolve_scene()
    $ resolve_scene()
    $ resolve_scene()
    $ resolve_scene()
    $ resolve_scene()
    $ resolve_scene()
    call PauseForBalloon("Casinohombredelasuerte") from _call_Casinohombredelasuerte_PauseForBalloon_2
    OldWoman "Hohoho..."
    OldMan "Interesting ... a tourist as a lucky person ... Well, you know how this is going guys"
    call Movement("Casinohombredelasuerte", "Casinoworker", ["U","TURN_R"]) from _call_Casinohombredelasuerte_Movement_16
    $ show_picture(1, "suerte1")
    $ resolve_scene()
    Worker "Well, I already have a year of good luck"
    Leyna "Oh my ... Just this? I was scared..."
    $ show_picture(2, "suerte2")
    $ resolve_scene()
    Worker "Well, people get a little anxious sometimes.. but that happened more years ago, now we are less people and they will take it more calmly"
    Johan "Good to know, I don't feel very comfortable with all these people touching my wife"
    Worker "Relax, it's just a tradition"
    Johan "(Another tradition huh?) Yeah...."
    $ show_picture(3, "suerte3")
    $ resolve_scene()
    Villager "Hey! A year of good luck to me"
    Leyna "...!"
    $ show_picture(4, "suerte4")
    $ resolve_scene()
    Villager2 "And for me!"
    "Villager3: Don't leave me behind, I want too!"
    $ show_picture(5, "suerte5")
    $ resolve_scene()
    Leyna "Wa-wait"
    $ show_picture(6, "suerte6")
    $ resolve_scene()
    Johan "Hey easy going guys!"
    "Villager4: Luck is running out! "
    $ show_picture(7, "suerte7")
    $ resolve_scene()
    Leyna "He-hey..."
    $ show_picture(8, "suerte9")
    $ resolve_scene()
    Leyna "(They're touching me in ...)"
    pause
    $ show_picture(9, "suerte8")
    $ resolve_scene()
    Leyna "Be careful guys ..."
    pause
    if switch("ate_the_fruit"):
        $ show_picture(10, "suerte10")
        $ resolve_scene()
        Leyna "(This ... this is turning me on a bit ... I can't let Johan know, I have to pretend)"
    $ resolve_scene()
    "Villager5: Let's see if I win the lottery this year!"
    Johan "I think that's enough"
    Villager "... Yeah yeah.... sorry dude"
    pause
    $ show_picture(11, "suerte11")
    $ resolve_scene()
    Johan "Are you okay?"
    Leyna "Yes, I'm okay"
    if switch("ate_the_fruit"):
        $ resolve_scene()
        Leyna "(Definitely, the fruit that I've eaten before is affecting...)"
    $ fade_out()
    $ erase_picture(1)
    $ erase_picture(2)
    $ erase_picture(3)
    $ erase_picture(4)
    $ erase_picture(5)
    $ erase_picture(6)
    $ erase_picture(9)
    $ erase_picture(7)
    $ erase_picture(8)
    $ erase_picture(10)
    $ erase_picture(11)
    call Movement("Casinohombredelasuerte", "Casinovillager1", ["TURN_U"]) from _call_Casinohombredelasuerte_Movement_17
    call Movement("Casinohombredelasuerte", "Casinovillager2", ["TURN_U"]) from _call_Casinohombredelasuerte_Movement_18
    call Movement("Casinohombredelasuerte", "Casinovillager3", ["TURN_U"]) from _call_Casinohombredelasuerte_Movement_19
    call Movement("Casinohombredelasuerte", "Casinovillager4", ["TURN_U"]) from _call_Casinohombredelasuerte_Movement_20
    call Movement("Casinohombredelasuerte", "Casinovillager5", ["TURN_U"]) from _call_Casinohombredelasuerte_Movement_21
    call Movement("Casinohombredelasuerte", "Casinovillager6", ["TURN_U"]) from _call_Casinohombredelasuerte_Movement_22
    call Movement("Casinohombredelasuerte", "Casinovillager7", ["TURN_U"]) from _call_Casinohombredelasuerte_Movement_23
    call Movement("Casinohombredelasuerte", "Casinovillager8", ["TURN_U"]) from _call_Casinohombredelasuerte_Movement_24
    call Movement("Casinohombredelasuerte", "Casinovillager9", ["TURN_U"]) from _call_Casinohombredelasuerte_Movement_25
    call Movement("Casinohombredelasuerte", "Casinovillager10", ["TURN_U"]) from _call_Casinohombredelasuerte_Movement_26
    $ fade_in()
    $ resolve_scene()
    OldMan "Well guys! You have to spread the word about the lucky girl!"
    $ resolve_scene()
    call PauseForBalloon("Casinohombredelasuerte") from _call_Casinohombredelasuerte_PauseForBalloon_3
    Villager "That's done boss!"
    Johan "Hey..."
    OldMan "(How lucky ... this year the lucky person is a beautiful tourist ... sure next year there's much more interest in coming to the lot)"
    Leyna "Johan ... Let's take a walk around the festival to see what can we do"
    Johan "Sure..."
    $ set_switch("lucky_person", True)
    call GalleryViewed("suerte") from _call_Casinohombredelasuerte_GalleryViewed
    call TransferPlayer("Festival", "Casinohombredelasuerte", 4, 22, direction=0) from _call_Casinohombredelasuerte_TransferPlayer
    call Movement("Casinohombredelasuerte", "player", ["R","R"]) from _call_Casinohombredelasuerte_Movement_27
    if switch("ate_the_fruit"):
        $ corruption = corruption + 2
    if not switch("ate_the_fruit"):
        $ corruption = corruption + 1
    $ resolve_scene()
    return False

label Casinohombredelasuerte(play_event = True, trigger = None): # autorun
    if is_erased("Casinohombredelasuerte"):
        return None
    elif trigger == "autorun":
        call PlayEvent(play_event, "CasinohombredelasuerteBase", "Casinohombredelasuerte") from _call_Casinohombredelasuerte_PlayEvent
        return (0, "", "Casinohombredelasuerte")
    return None

