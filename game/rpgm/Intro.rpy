label IntroBG:
    $ set_transparency_backgrounds(["bg_bedroom","darkbg"])
    $ set_map_backgrounds(["bg_bedroom","darkbg"])
    return

label IntroStart:
    call IntroBG from _call_IntroBG
    stop music
    stop bgs
    return

label IntroEnd:
    return

label IntroHelloMyNameIsJohanBase:
    call PlaySound("music", "audio/Field1.ogg", volume=0.9, no_loop=False) from _call_IntroEV001_PlaySound
    $ show_transparent(1, "marido_plano_general", pos=(-140, 0), width=1600, height=900)
    $ resolve_scene()
    "Hello! My name is Johan"
    "I write articles for a small tourism magazine, but lately I don't have much work."
    $ erase_picture(1)
    $ show_transparent(2, "marido_plano_cerca", width=1600, height=900)
    $ resolve_scene()
    "I'm going through a difficult situation. I live with my wife Leyna in this modest apartment"
    "We have been married for 7 years and we complement each other very well, she is currently unemployed"
    $ erase_picture(2)
    $ show_transparent(3, "plano_mujer_cerca", width=1600, height=900)
    $ resolve_scene()
    "And that's why she helps me at work until she can get one"
    "Even with all our problems we love and support each other and we have a simple and happy life."
    call ChangePartyMember("Leyna2", False) from _call_IntroEV001_ChangePartyMember
    call ChangePartyMember("Johan2", False) from _call_IntroEV001_ChangePartyMember_1
    $ erase_picture(3)
    call TransferPlayer("Apartment", "IntroEV001", 12, 11, direction=4) from _call_IntroEV001_TransferPlayer
    # UNHANDLED ChangeTransparency: [1]
    stop music fadeout 1
    $ resolve_scene()
    return False

label IntroHelloMyNameIsJohan(play_event = True, trigger = None): # autorun
    if is_erased("IntroHelloMyNameIsJohan"):
        return None
    elif trigger == "autorun":
        call PlayEvent(play_event, "IntroHelloMyNameIsJohanBase", "IntroHelloMyNameIsJohan") from _call_IntroHelloMyNameIsJohan_PlayEvent
        return (0, "", "IntroHelloMyNameIsJohan")
    return None

