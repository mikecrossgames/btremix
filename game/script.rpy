label start:
    stop music fadeout 1.0
    scene black
    call PlayEntireGame from _call_PlayEntireGame 
    return

label PlayEntireGame:
    call IntroHelloMyNameIsJohan from _call_IntroHelloMyNameIsJohan
    return