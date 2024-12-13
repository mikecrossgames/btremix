label IntroHelloMyNameIsJohan:
    play music "audio/Field1.ogg" loop volume 0.9
    $ show_transparent(1, "marido_plano_general", pos=(-140, 0), width=1600, height=900)
    "Hello! My name is Johan"
    "I write articles for a small tourism magazine, but lately I don't have much work."
    $ erase_picture(1)
    $ show_transparent(2, "marido_plano_cerca", width=1600, height=900)
    "I'm going through a difficult situation. I live with my wife Leyna in this modest apartment"
    "We have been married for 7 years and we complement each other very well, she is currently unemployed"
    $ erase_picture(2)
    $ show_transparent(3, "plano_mujer_cerca", width=1600, height=900)
    "And that's why she helps me at work until she can get one"
    "Even with all our problems we love and support each other and we have a simple and happy life."
    $ erase_picture(3)
    # TransferPlayer: "Apartment"
    stop music fadeout 1
    return

