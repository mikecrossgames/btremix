label ClothingStoreBG:
    $ set_transparency_backgrounds(["bg_clothing_store"])
    $ set_map_backgrounds(["map_clothing_store"])
    return

label ClothingStoreStart:
    call ClothingStoreBG from _call_ClothingStoreBG
    stop music
    stop bgs
    return

label ClothingStoreEnd:
    return

label ClothingStoreToTown_0:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_ClothingStoreEV001_0_PlaySound
    call TransferPlayer("Town", "ClothingStoreEV001_0", 36, 21, direction=2) from _call_ClothingStoreEV001_0_TransferPlayer
    $ resolve_scene()
    return False

label ClothingStoreToTown_1:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_ClothingStoreEV001_1_PlaySound
    call TransferPlayer("Town2", "ClothingStoreEV001_1", 36, 21, direction=2) from _call_ClothingStoreEV001_1_TransferPlayer
    $ resolve_scene()
    return False

label ClothingStoreToTown(play_event = True, trigger = None): # event
    if is_erased("ClothingStoreToTown"):
        return None
    elif trigger == "event" and switch("third_day"):
        call PlayEvent(play_event, "ClothingStoreToTown_1", "ClothingStoreToTown") from _call_ClothingStoreToTown_1_PlayEvent
        return (0, "", "ClothingStoreToTown_1")
    elif trigger == "event":
        call PlayEvent(play_event, "ClothingStoreToTown_0", "ClothingStoreToTown") from _call_ClothingStoreToTown_0_PlayEvent
        return (0, "", "ClothingStoreToTown_0")
    return None

label ClothingStoreHeyThere_0:
    if not switch("leyna_alone"):
        $ resolve_scene()
        Merchant "Hey there"
        "Let me know if you need anything"
    if switch("leyna_alone"):
        Merchant "Here we sell the clothes for the festival"
        "Come back in other moment and try it"
    $ resolve_scene()
    return False

label ClothingStoreHeyThere_1:
    Leyna "I come for the photographer's package"
    Merchant "The photographer's package? I see.."
    "So you are the new victim.. sometimes I think he just pretends he has this magazine jobs to take lewd photos"
    $ show_transparent(1, "plano_mujer_ojos_blanco_negro", width=1600, height=900)
    $ resolve_scene()
    Leyna "What? He seems such a nice old man"
    Merchant "Yes, he is... just be careful"
    $ erase_picture(1)
    $ show_transparent(2, "plano_mujer_sonrisa", width=1600, height=900)
    $ resolve_scene()
    Leyna "Okay, thanks for the advice"
    Merchant "Here you have the package"
    $ erase_picture(2)
    call PlaySound("sound", "audio/Recovery.ogg", volume=0.9, no_loop=True) from _call_ClothingStoreEVENTOROPA_1_PlaySound
    $ resolve_scene()
    $ set_item("clothes", True)
    "(YOU WON A NEW OBJECT)"
    Leyna "Thank you!"
    $ set_switch("pick_up_package", False)
    $ set_switch("collected_package", True)
    return False

label ClothingStoreHeyThere_2:
    Merchant "Welcome again to my store! As I told you, I already have the festival clothes"
    "Do you want to try them on?"
    Leyna "Sure, I'm so excited!"
    Merchant "The fitting room is over there and the clothes are inside, just choose your size"
    Leyna "Thank you"
    $ event_clothing = 1
    return False

label ClothingStoreHeyThere_3:
    Merchant "Everything alright?"
    return False

label ClothingStoreHeyThere(play_event = True, trigger = None): # event
    if is_erased("ClothingStoreHeyThere"):
        return None
    elif trigger == "event" and event_clothing >= 1:
        call PlayEvent(play_event, "ClothingStoreHeyThere_3", "ClothingStoreHeyThere") from _call_ClothingStoreHeyThere_3_PlayEvent
        return (1, "", "ClothingStoreHeyThere_3")
    elif trigger == "event" and elder_festival >= 6:
        call PlayEvent(play_event, "ClothingStoreHeyThere_2", "ClothingStoreHeyThere") from _call_ClothingStoreHeyThere_2_PlayEvent
        return (1, "", "ClothingStoreHeyThere_2")
    elif trigger == "event" and switch("pick_up_package"):
        call PlayEvent(play_event, "ClothingStoreHeyThere_1", "ClothingStoreHeyThere") from _call_ClothingStoreHeyThere_1_PlayEvent
        return (1, "", "ClothingStoreHeyThere_1")
    elif trigger == "event":
        call PlayEvent(play_event, "ClothingStoreHeyThere_0", "ClothingStoreHeyThere") from _call_ClothingStoreHeyThere_0_PlayEvent
        return (1, "", "ClothingStoreHeyThere_0")
    return None

label ClothingStoreIShouldComeBackLaterToTryTheFestivalClothes_0:
    "(I should come back later to try the festival clothes)"
    return False

label ClothingStoreIShouldComeBackLaterToTryTheFestivalClothes_1:
    $ show_transparent(1, "expresion_gui_o_lengua")
    $ resolve_scene()
    Leyna "I'm going to try it on, wait here and I'll let you know when I'm ready"
    Johan "O..okay"
    $ fade_out()
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_ClothingStoreEV005_1_PlaySound
    Leyna "Johan? Come in"
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_ClothingStoreEV005_1_PlaySound_1
    $ erase_picture(1)
    $ show_picture(2, "probador1")
    $ fade_in()
    $ resolve_scene()
    Leyna "So ... what do you think?"
    Johan "Wow, that's so sexy!"
    $ show_picture(3, "probador2")
    $ resolve_scene()
    Leyna "Do I look good?"
    Johan "You are beautiful (I would say too beautiful. Now that I think about it, is she supposed to go through the festival like this in front of everyone?)"
    Johan "(Now that I remember, these last days Leyna has had several \"accidents\" around the men of this village)"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Poison.ogg", volume=0.9, no_loop=True) from _call_ClothingStoreEV005_1_PlaySound_2
    $ show_picture(11, "rio_7", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Johan "Why am I thinking about this right now?"
    Johan "(I feel something in my stomach ... Am I getting turned on thinking about this?... No, I'm just...)"
    $ erase_picture(11)
    $ resolve_scene()
    $ flash_screen([255,255,255,170], 60, True)
    $ show_picture(4, "probador3")
    $ resolve_scene()
    Leyna "Why are you staring at me so hard, Johan?"
    Johan "I'm just... You're so sexy in that outfit... I can't control myself"
    Johan "Let's make love, here and now"
    Leyna "Johan... we shouldn't..."
    Johan "Come here"
    $ fade_out()
    $ erase_picture(2)
    $ erase_picture(3)
    $ erase_picture(4)
    # UNHANDLED ChangeTransparency: [0]
    $ fade_in()
    $ resolve_scene()
    call PauseForBalloon("ClothingStoreEV005_1") from _call_ClothingStoreEV005_1_PauseForBalloon
    Merchant "They are taking a long time ..."
    call PlaySound("music", "audio/Dungeon3.ogg", volume=0.9, no_loop=False) from _call_ClothingStoreEV005_1_PlaySound_3
    $ show_picture(11, "probador4")
    $ resolve_scene()
    Johan "Oh God,  I can't take it anymore, it's been weeks since last time..."
    Leyna "Ssshhh..."
    $ show_picture(6, "probador5")
    $ erase_picture(11)
    $ resolve_scene()
    Johan "Ooh! Yes..."
    Leyna "Hm hm hm...."
    pause
    $ show_picture(7, "probador6")
    $ resolve_scene()
    Leyna "You like it?"
    Johan "I love it"
    pause
    $ flash_screen([255,255,255,170], 60, True)
    $ show_picture(11, "escena_camisa_mojada_1", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Johan "Shit, this again? What the hell is wrong with me?"
    $ erase_picture(11)
    $ resolve_scene()
    Johan "Get up Leyna"
    Leyna "!!!"
    $ show_picture(8, "probador7")
    $ resolve_scene()
    Johan "Right there"
    Leyna "hmmmmmmm...."
    $ show_picture(9, "probador8")
    call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_ClothingStoreEV005_1_PlaySound_4
    $ resolve_scene()
    Johan "Yes... damn...."
    Leyna "Oooh... (I have never seen Johan so excited... Does he like to do it in public?)"
    Johan "(Shit ... I can't get those pictures out of my head ... I'm...)"
    Johan "I'm coming!"
    Leyna "Wa...Wait! Take it out"
    $ show_picture(10, "probador9")
    stop bgs fadeout 1
    $ resolve_scene()
    $ flash_screen([255,255,255,170], 60, True)
    Johan "OOOHHH"
    Leyna "!!!"
    Johan "SHIT! I'm sorry, let me find something to clean you with"
    $ fade_out()
    $ erase_picture(6)
    $ erase_picture(7)
    $ erase_picture(8)
    $ erase_picture(9)
    $ erase_picture(10)
    stop bgs fadeout 1
    call TransferPlayer("ClothingStore", "ClothingStoreEV005_1", 3, 11, direction=6) from _call_ClothingStoreEV005_1_TransferPlayer
    # UNHANDLED ChangeTransparency: [1]
    $ fade_in()
    call Movement("ClothingStoreEV005_1", "player", ["R","R","U","U","R","U","U","U","L","U"]) from _call_ClothingStoreEV005_1_Movement
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "The clothes are perfect for me"
    Merchant "Glad to hear that, have fun at the festival!"
    Johan "... We will"
    $ fade_out()
    $ erase_picture(1)
    call TransferPlayer("Town2", "ClothingStoreEV005_1", 36, 21, direction=2) from _call_ClothingStoreEV005_1_TransferPlayer_1
    $ fade_in()
    call Movement("ClothingStoreEV005_1", "player", ["D","D"]) from _call_ClothingStoreEV005_1_Movement_1
    $ resolve_scene()
    Johan "(What is happening to me? ... I've never had these kinds of thoughts)"
    $ corruption = corruption + 3
    $ event_clothing = 2
    call GalleryViewed("probador") from _call_ClothingStoreEV005_1_GalleryViewed
    return False

label ClothingStoreIShouldComeBackLaterToTryTheFestivalClothes(play_event = True, trigger = None): # event
    if is_erased("ClothingStoreIShouldComeBackLaterToTryTheFestivalClothes"):
        return None
    elif event_clothing >= 2:
        return None
    elif trigger == "event" and event_clothing >= 1:
        call PlayEvent(play_event, "ClothingStoreIShouldComeBackLaterToTryTheFestivalClothes_1", "ClothingStoreIShouldComeBackLaterToTryTheFestivalClothes") from _call_ClothingStoreIShouldComeBackLaterToTryTheFestivalClothes_1_PlayEvent
        return (1, "", "ClothingStoreIShouldComeBackLaterToTryTheFestivalClothes_1")
    elif trigger == "event":
        call PlayEvent(play_event, "ClothingStoreIShouldComeBackLaterToTryTheFestivalClothes_0", "ClothingStoreIShouldComeBackLaterToTryTheFestivalClothes") from _call_ClothingStoreIShouldComeBackLaterToTryTheFestivalClothes_0_PlayEvent
        return (1, "", "ClothingStoreIShouldComeBackLaterToTryTheFestivalClothes_0")
    return None

