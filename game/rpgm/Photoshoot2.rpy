label Photoshoot2BG:
    $ set_transparency_backgrounds(["bg_photographers"])
    $ set_map_backgrounds(["bg_photographers"])
    return

label Photoshoot2Start:
    call Photoshoot2BG from _call_Photoshoot2BG
    stop music
    stop bgs
    return

label Photoshoot2End:
    return

label Photoshoot2Sesionfotografica2Base:
    call Movement("Photoshoot2Sesionfotografica2", "player", ["U","U","U","U","U","TURN_R"]) from _call_Photoshoot2Sesionfotografica2_Movement
    $ resolve_scene()
    OldMan "Leyna, this is my grandson"
    call Movement("Photoshoot2Sesionfotografica2", "player", ["TURN_U"]) from _call_Photoshoot2Sesionfotografica2_Movement_1
    $ resolve_scene()
    call PauseForBalloon("Photoshoot2Sesionfotografica2") from _call_Photoshoot2Sesionfotografica2_PauseForBalloon
    Leyna "Nice to meet you (He's very tall)"
    Grandson "Hello! Excuse me I'm a little nervous, it's my first time"
    Leyna "Well, this is my second time. It's relatively easy, let yourself go"
    Grandson "Okay.. (I didn't expect her to be so pretty)"
    Leyna "By the way, why is everyone in this town so big? hahahaha"
    OldMan "Hahaha cause we eat a lot, I guess.."
    OldMan "Okay guys, go change., Leyna I've left the package where it was the last time"
    OldMan "Let's start with the first of the two, with that one you will pose alone. With the second you will pose together"
    Leyna "O-okay"
    $ fade_out()
    call SetEventLocation("Photoshoot2Sesionfotografica2", "Photoshoot2Nieto", 7, 4) from _call_Photoshoot2Sesionfotografica2_setloc
    call TransferPlayer("Photoshoot2", "Photoshoot2Sesionfotografica2", 15, 5, direction=4) from _call_Photoshoot2Sesionfotografica2_TransferPlayer
    $ fade_in()
    $ resolve_scene()
    call PauseForBalloon("Photoshoot2Sesionfotografica2") from _call_Photoshoot2Sesionfotografica2_PauseForBalloon_1
    Leyna "Nightgown with straps... it's pretty"
    Leyna "It seems to be a little transparent ..."
    $ fade_out()
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_Photoshoot2Sesionfotografica2_PlaySound
    $ show_picture(1, "fotografo11")
    $ fade_in()
    $ resolve_scene()
    Leyna "I'm ready"
    OldMan "You look gorgeous with that Leyna, let's do a couple of poses"
    $ fade_out()
    $ show_picture(2, "fotografo13")
    $ fade_in()
    $ resolve_scene()
    "(A FEW MINUTES LATER)"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Photoshoot2Sesionfotografica2_PlaySound_1
    OldMan "This is enough for now"
    OldMan "You can change now so we start with the photos of both together"
    $ fade_out()
    $ erase_picture(1)
    $ erase_picture(2)
    $ fade_in()
    $ resolve_scene()
    call PauseForBalloon("Photoshoot2Sesionfotografica2") from _call_Photoshoot2Sesionfotografica2_PauseForBalloon_2
    Leyna "This is too provocative. Who's going to wear this? ..Well I just have to do a couple of poses with the boy and we're done but.."
    Leyna "Okay Leyna, focus... let's get this over with"
    $ fade_out()
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_Photoshoot2Sesionfotografica2_PlaySound_2
    $ show_picture(1, "fotografo14")
    $ fade_in()
    $ resolve_scene()
    Leyna "Are you sure this is the correct garment?"
    OldMan "Yeah pretty sure..."
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Photoshoot2Sesionfotografica2_PlaySound_3
    OldMan "Come on Leyna, let yourself go a little, you look very rigid"
    Leyna "Y-yeah"
    $ show_picture(2, "fotografo15")
    $ resolve_scene()
    Leyna "Like this?"
    OldMan "There you go. That's the stuff"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Photoshoot2Sesionfotografica2_PlaySound_4
    Grandson "(Wow! I've never seen a naked woman in person I'm getting a little hard, I've to hide)"
    OldMan "Now smile a little Leyna, you are much more beautiful when you smile"
    pause
    $ show_picture(3, "fotografo16")
    $ resolve_scene()
    Leyna "That's okay?"
    OldMan "Perfect!"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Photoshoot2Sesionfotografica2_PlaySound_5
    OldMan "Now let's start with the both together"
    OldMan "Come on boy! Don't be shy"
    $ show_picture(4, "fotografo17")
    $ resolve_scene()
    OldMan "Well ... I guess that's fine ..."
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Photoshoot2Sesionfotografica2_PlaySound_6
    OldMan "I need more movement guys!"
    Grandson "M-more movement?"
    OldMan "Yeah! And passion!"
    Leyna "(Passion?...)"
    Grandson "O-OKAY!"
    Leyna "(!!!)"
    $ show_picture(5, "fotografo18")
    call PlaySound("sound", "audio/Jump1.ogg", volume=0.9, no_loop=True) from _call_Photoshoot2Sesionfotografica2_PlaySound_7
    call PlaySound("music", "audio/Dungeon3.ogg", volume=0.9, no_loop=False) from _call_Photoshoot2Sesionfotografica2_PlaySound_8
    $ resolve_scene()
    Grandson "Th-there you go!"
    Leyna "AAAaah?!"
    OldMan "Well... (This is a bit extreme kid, but I guess it will work... and I'm enjoying some incredible views)"
    OldMan "Perfect! Relax Leyna, I will cut out the... delicate parts"
    Grandson "De-delicate parts?"
    OldMan "Some zoom and..."
    $ show_picture(6, "fotografo19")
    $ resolve_scene()
    OldMan "Yeah great!"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Photoshoot2Sesionfotografica2_PlaySound_9
    Leyna "What it's going on? I feel something in my..."
    Grandson "(Shit, it's going out! With this loincloth shit it's impossible to keep it inside)"
    pause
    $ show_picture(7, "fotografo20")
    $ resolve_scene()
    Leyna "Your dick is out!"
    Grandson "I-Im sorry I couldn't avoid it"
    OldMan "Don't worry, it's natural! You are 18 years old, I wish I had that ... energy"
    OldMan "But this is fine, the magazine has asked me for some raunchy photos, put the girl down"
    Grandson "Okay"
    $ show_picture(8, "fotografo21")
    $ resolve_scene()
    OldMan "Stay in that position"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Photoshoot2Sesionfotografica2_PlaySound_10
    Grandson "I'm sorry Leyna..."
    Leyna "I-It's... Okay"
    Leyna "(I'm getting wet...) Are many photos left to finish?"
    OldMan "No no, just a couple more and that's it"
    OldMan "Okay kid, pick her up again, and Leyna I know this is a little weird but I need you to smile"
    Leyna "Right..."
    $ show_picture(9, "fotografo23")
    $ resolve_scene()
    OldMan "Great! Stay still"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Photoshoot2Sesionfotografica2_PlaySound_11
    Leyna "(I feel horny... I've to finish this right now)"
    Grandson "Are you okay?"
    Leyna "Yeah, I'm alright don't worry..."
    OldMan "One last picture and that's it, Leyna get on your knees"
    Leyna "(...)"
    pause
    $ show_picture(10, "fotografo24")
    $ resolve_scene()
    OldMan "Nice!"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Photoshoot2Sesionfotografica2_PlaySound_12
    OldMan "Good work both of you!"
    Grandson "Thanks grandpa! It was a lot of fun in the end"
    OldMan "Hahaha yeah! I'm looking forward to work more with you two!"
    Leyna "Yeah... Well I better leave now"
    OldMan "Right! I will notify you when we have more work"
    Leyna "Hmm..."
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
    stop music fadeout 1
    call TransferPlayer("Town", "Photoshoot2Sesionfotografica2", 49, 11, direction=4) from _call_Photoshoot2Sesionfotografica2_TransferPlayer_1
    $ fade_in()
    call Movement("Photoshoot2Sesionfotografica2", "player", ["L","L","L"]) from _call_Photoshoot2Sesionfotografica2_Movement_2
    $ show_transparent(1, "plano_mujer_timida", width=1600, height=900)
    $ resolve_scene()
    Leyna "..."
    $ erase_picture(1)
    $ resolve_scene()
    "(+3 CORRUPTION)"
    $ set_switch("second_photo_session", True)
    call GalleryViewed("fotografo2") from _call_Photoshoot2Sesionfotografica2_GalleryViewed
    $ corruption = corruption + 3
    return False

label Photoshoot2Sesionfotografica2(play_event = True, trigger = None): # autorun
    if is_erased("Photoshoot2Sesionfotografica2"):
        return None
    elif trigger == "autorun":
        call PlayEvent(play_event, "Photoshoot2Sesionfotografica2Base", "Photoshoot2Sesionfotografica2") from _call_Photoshoot2Sesionfotografica2_PlayEvent
        return (0, "", "Photoshoot2Sesionfotografica2")
    return None

