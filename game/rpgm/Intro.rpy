label IntroHelloMyNameIsJohan:
    play music "audio/Field1.ogg" loop volume 0.9
    show marido_plano_general:
        pos (-140, 0)
        xsize 1600
        ysize 900
    "Hello! My name is Johan"
    "I write articles for a small tourism magazine, but lately I don't have much work."
    hide marido_plano_general
    show marido_plano_cerca:
        xsize 1600
        ysize 900
    "I'm going through a difficult situation. I live with my wife Leyna in this modest apartment"
    "We have been married for 7 years and we complement each other very well, she is currently unemployed"
    hide marido_plano_cerca
    show plano_mujer_cerca:
        xsize 1600
        ysize 900
    "And that's why she helps me at work until she can get one"
    "Even with all our problems we love and support each other and we have a simple and happy life."
    hide plano_mujer_cerca
    # TransferPlayer: "Apartment"
    stop music fadeout 1
    return

