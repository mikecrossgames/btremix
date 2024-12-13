label PhotographersHouseBG:
    $ set_transparency_backgrounds(["bg_photographers"])
    $ set_map_backgrounds(["bg_photographers"])
    return

label PhotographersHouseStart:
    call PhotographersHouseBG from _call_PhotographersHouseBG
    stop music
    stop bgs
    return

label PhotographersHouseEnd:
    return

label PhotographersHousesesionfotografica1Base:
    call Movement("PhotographersHousesesionfotografica1", "player", ["U","U","U","U","U","R"]) from _call_PhotographersHousesesionfotografica1_Movement
    call Movement("PhotographersHousesesionfotografica1", "PhotographersHousefotografo", ["TURN_L"]) from _call_PhotographersHousesesionfotografica1_Movement_1
    $ resolve_scene()
    OldMan "Alright, let's start. Clothes are in a package on top of my bed, you should put on the swimsuit in the first place..."
    Leyna "Great!"
    call Movement("PhotographersHousesesionfotografica1", "PhotographersHousefotografo", ["TURN_U"]) from _call_PhotographersHousesesionfotografica1_Movement_2
    call TransferPlayer("PhotographersHouse", "PhotographersHousesesionfotografica1", 15, 7, direction=8) from _call_PhotographersHousesesionfotografica1_TransferPlayer
    call Movement("PhotographersHousesesionfotografica1", "player", ["U","U","TURN_L"]) from _call_PhotographersHousesesionfotografica1_Movement_3
    $ resolve_scene()
    pause 0.6
    $ show_transparent(1, "expresion_ilusion_mujer", width=1600, height=900)
    $ resolve_scene()
    Leyna "This swimsuit is beautiful!"
    Leyna "I should change now ..."
    $ fade_out()
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_PhotographersHousesesionfotografica1_PlaySound
    $ erase_picture(1)
    call TransferPlayer("PhotographersHouse", "PhotographersHousesesionfotografica1", 8, 7, direction=4) from _call_PhotographersHousesesionfotografica1_TransferPlayer_1
    $ fade_in()
    call Movement("PhotographersHousesesionfotografica1", "player", ["L","L","U","U","U","L","L","TURN_D"]) from _call_PhotographersHousesesionfotografica1_Movement_4
    $ resolve_scene()
    pause 0.6
    $ show_picture(1, "fotografo1")
    $ resolve_scene()
    Leyna "I'm ready..."
    OldMan "Wow! Great, let's start improvising a bit, pose freely for now"
    pause
    $ show_picture(2, "fotografo2")
    $ resolve_scene()
    Leyna "Like this?..."
    OldMan "Yeah! That's perfect"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Switch2.ogg", volume=0.9, no_loop=True) from _call_PhotographersHousesesionfotografica1_PlaySound_1
    OldMan "Okay, let's try a different one"
    $ show_picture(3, "fotografo3")
    $ resolve_scene()
    OldMan "Great!"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Switch2.ogg", volume=0.9, no_loop=True) from _call_PhotographersHousesesionfotografica1_PlaySound_2
    OldMan "I think with this swimsuit we already have enough, you can already change with the lingerie that is in the second package..."
    Leyna "Great! ( This is fun! )"
    $ fade_out()
    $ erase_picture(1)
    $ erase_picture(2)
    $ erase_picture(3)
    call TransferPlayer("PhotographersHouse", "PhotographersHousesesionfotografica1", 15, 5, direction=4) from _call_PhotographersHousesesionfotografica1_TransferPlayer_2
    $ fade_in()
    $ resolve_scene()
    pause 0.6
    Leyna "Is this..? It's a little ... revealing, I don't know if I should ..."
    OldMan "Is there any problem?"
    Leyna "Oh  (come on Leyna, it's just a photo shoot ...) No, any problem at all..."
    call TransferPlayer("PhotographersHouse", "PhotographersHousesesionfotografica1", 8, 7, direction=4) from _call_PhotographersHousesesionfotografica1_TransferPlayer_3
    call Movement("PhotographersHousesesionfotografica1", "player", ["L","L","U","U","U","L","L","TURN_D"]) from _call_PhotographersHousesesionfotografica1_Movement_5
    $ show_picture(4, "fotografo4")
    $ resolve_scene()
    Leyna "Isn't it too provocative?..."
    OldMan "Oh no! Not at all. You look stunning with that lingerie"
    Leyna "Thank you..."
    $ show_picture(5, "fotografo5")
    $ resolve_scene()
    OldMan "(Damn, I can see everything!)"
    pause
    $ erase_picture(5)
    $ resolve_scene()
    OldMan "Okay precious, pose a little for me, you look very sexy, you can do this!"
    Leyna "Hahahaha O-okay..."
    $ show_picture(6, "fotografo6")
    $ resolve_scene()
    Leyna "Like this?..."
    OldMan "Yeah perfect!"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Switch2.ogg", volume=0.9, no_loop=True) from _call_PhotographersHousesesionfotografica1_PlaySound_3
    OldMan "Great, next pose"
    $ show_picture(7, "fotografo7")
    $ resolve_scene()
    OldMan "Wonderful ( She's gaining confidence.. )"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Switch2.ogg", volume=0.9, no_loop=True) from _call_PhotographersHousesesionfotografica1_PlaySound_4
    OldMan "Now let's try something sexier..."
    Leyna "Okay..."
    pause
    $ show_picture(8, "fotografo8")
    $ resolve_scene()
    OldMan "Great! That's perfect!"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Switch2.ogg", volume=0.9, no_loop=True) from _call_PhotographersHousesesionfotografica1_PlaySound_5
    OldMan "You're doing a great job!"
    OldMan "One last pic and we're done for now"
    Leyna "Nice!"
    pause
    $ show_picture(9, "fotografo10")
    $ resolve_scene()
    OldMan "Yeah that's perfect!"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Switch2.ogg", volume=0.9, no_loop=True) from _call_PhotographersHousesesionfotografica1_PlaySound_6
    OldMan "We're done, you can change now"
    $ fade_out()
    $ erase_picture(4)
    $ erase_picture(6)
    $ erase_picture(7)
    $ erase_picture(8)
    $ erase_picture(9)
    call TransferPlayer("PhotographersHouse", "PhotographersHousesesionfotografica1", 8, 7, direction=4) from _call_PhotographersHousesesionfotografica1_TransferPlayer_4
    $ fade_in()
    call Movement("PhotographersHousesesionfotografica1", "player", ["L","L"]) from _call_PhotographersHousesesionfotografica1_Movement_6
    call Movement("PhotographersHousesesionfotografica1", "PhotographersHousefotografo", ["TURN_R"]) from _call_PhotographersHousesesionfotografica1_Movement_7
    $ resolve_scene()
    OldMan "The photos have turned out great. If you want you can come back later and do another photoshoot"
    Leyna "I would love that, it was really fun!"
    OldMan "Great, see you later then..."
    call TransferPlayer("Town", "PhotographersHousesesionfotografica1", 49, 12, direction=4) from _call_PhotographersHousesesionfotografica1_TransferPlayer_5
    call Movement("PhotographersHousesesionfotografica1", "player", ["L","L"]) from _call_PhotographersHousesesionfotografica1_Movement_8
    $ set_switch("first_photo_session", True)
    call GalleryViewed("fotografo1") from _call_PhotographersHousesesionfotografica1_GalleryViewed
    $ resolve_scene()
    return False

label PhotographersHousesesionfotografica1(play_event = True, trigger = None): # autorun
    if is_erased("PhotographersHousesesionfotografica1"):
        return None
    elif trigger == "autorun":
        call PlayEvent(play_event, "PhotographersHousesesionfotografica1Base", "PhotographersHousesesionfotografica1") from _call_PhotographersHousesesionfotografica1_PlayEvent
        return (0, "", "PhotographersHousesesionfotografica1")
    return None

