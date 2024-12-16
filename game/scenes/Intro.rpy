label IntroOhHelloThere(menu_choice = None):
    scene black with dissolve
    show pantallanegro with dissolve:
        xsize 979
        ysize 720
    "......."
    "....."
    "..."
    "."
    $ flash_screen(wait=True)
    scene netorase1
    play sound "audio/Saint4.ogg" volume 0.9 noloop
    "....."
    scene netorase2
    "Oh! Hello there!"
    "You may wonder who I am..."
    "Well... I am the anthropormofic representation of Aedirn studio!"
    "I just wanted to inform you about a couple of things before you start playing Bawdy Traditions..."
    "The first one is that I hope with all my heart that you have a good time with this game, I've worked hard on this project and my only wish is that you have fun and enjoy it...."
    "Secondly, this game is completely focused on the NTR genre, if you are here I guess you already know that...."
    "Although you can enjoy the game without your beloved wife cheating on you... it is not the goal of the game, so the content in this purest route is more scarce than in the others..."
    "Although there is exclusive content in case you want to try it sometime..."
    "The most important thing to know is that the NTR genre has several subgenres but I only want to explain the two biggest ones to you"
    "Netorare and netorase"
    "I am going to summarize it in a nutshell and make it as simple as possible"
    "Netorare is when the partner ends up openly or secretly cheating on the protagonist and the protagonist does not know or does not like it"
    "Netorase on the other hand is when the protagonist wants his partner to sleep with other people and seeks and enjoys it"
    "the explanation is not entirely accurate, but it helps you to understand more or less what it's all about"
    "So... now you will have to choose what you want the game to offer you..."
    scene netorase3
    "The netorare route is complete and the netorase is in development... keep that in mind..."
    menu:
        "Netorare":
            $ set_switch("netorare", True)
        "Netorase":
            $ set_switch("netorase", True)
    "Perfect, I'm not bothering you anymore, I welcome you to Bawdy Traditions, enjoy the trip..."
    scene black with dissolve
    hide netorase3
    # fade in
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
    $ player_location = "Apartment"
    stop music fadeout 1
    return

