label Riverentradario_0:
    pause 0.22
    pause 0.22
    Villager "Hey! you can't pass with clothes on! Tradition says one can only pass if he goes naked."
    pause 0.22
    Johan "Sorry, we are not from here, we came to make an article and take some photos of the festivities, if you give us your permission, of course"
    Villager "An article, you say? hmmm if you are worried for the woman, we can make an exception for the circumstances.."
    "..but you have to go naked, this is a sacred tradition. The girl can carry a towel on her if she wants, just for this occasion."
    Johan "great, I have no problem. What do you think Leyna?"
    show plano_mujer_sorpresa_lado:
        xsize 1600
        ysize 900
    menu:
        "Yes":
            Villager "Perfect. Back there you have a small tent to leave your clothes."
            Johan "Perfect, we'll interview a couple of people and take photos of those who agree"
            hide plano_mujer_sorpresa_lado
            $ set_switch("separated_in_the_river", True)
            call SetPlayerLocation("River") from _call_Riverentradario_0_SetPlayerLocation
            pause 0.24
        "I'm not ready yet":
            Leyna "I think I'm not ready yet. I have to think about this a little more."
            Johan "Okey, no problem. We'll do it another time."
            call SetPlayerLocation("Town") from _call_Riverentradario_0_SetPlayerLocation_1
            pause 0.24
    return

label RiverNPCEventMan:
    Johan "Good afternoon, me and my wife are doing a report on the traditions of this town..."
    "... I was wondering if you would mind answering some questions for me and let me take some pictures of you by the river."
    show general_chica_rio:
        xsize 1600
        ysize 900
    Villager "Oh! Of course, no problem man, ask what you want"
    scene black with dissolve
    hide general_chica_rio
    # fade in
    Johan "So the celebration goes back thousands of years and is in honour of a very old fertility goddess..."
    "...how interesting! Great, now I'm going to take a couple of photos if you don't mind."
    Villager "Yes, of course ..."
    $ set_switch("separated_in_the_river", True)
    pause 0.26
    $ flash_screen(wait=True)
    Villager "I have an idea..."
    Johan "Yes?"
    Villager "It's just us in these photos. If you only show this in the article, people won't want to come to this town, right?"
    Johan "Well..."
    Villager "If you only see a group of ugly men posing on the camera it would be a disaster..."
    "...what these photos need is a feminine touch"
    show expresion_neutral_toalla:
        xsize 1600
        ysize 900
    Johan "A feminine touch?..."
    Villager "Exactly, why doesn't your wife come up and poses in a couple of photos with us?"
    show expresion_sorpresa_toalla:
        xsize 1600
        ysize 900
    Johan "I see... It makes sense, what do you think Leyna, would mind appearing in a couple of photos?..."
    "...anyway, I'm going to black out the faces and  the towel covers your body"
    Villager "(I can't believe this is working... So she's naked under the towel)"
    hide expresion_sorpresa_toalla
    Leyna "yeah... well, if you think it's a good idea... I guess it doesn't seem bad to me."
    Johan "Okay. Well, put yourself in the middle and I'll take some photos"
    scene black with dissolve
    hide expresion_neutral_toalla
    # fade in
    scene rio_1:
        pos (-125, 0)
        xsize 1104
        ysize 621
    Villager "(Damn... the girl smells great)"
    scene rio_2:
        pos (-125, 0)
        xsize 1104
        ysize 621
    Johan "Maybe you could go a little closer for the photo"
    Villager "O...Of course!"
    pause
    scene rio_3:
        pos (-125, 0)
        xsize 1104
        ysize 621
    Leyna "(!!!)"
    pause
    scene rio_4:
        pos (-125, 0)
        xsize 1104
        ysize 621
    if switch("netorare"):
        Johan "(They are too close ... well, I'm not going to bother them too much..."
        "...after all, they are doing us a favour letting us take photos of them)"
    if switch("netorase"):
        Johan "(They are so close... Fuck I must control myself or I'm going to have an erection right here...)"
        Johan "(I wish... I wish Leyna was naked... shit... why am I like this? Fuck I'm pathetic, I should have some self-respect)"
    pause
    scene rio_5:
        pos (-125, 0)
        xsize 1104
        ysize 621
    Villager "( This is my chance, but I have to do it right or I'll get caught! )"
    pause
    scene rio_6:
        pos (-125, 0)
        xsize 1104
        ysize 621
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    play music "audio/Dungeon3.ogg" loop volume 0.9
    pause
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    scene rio_7:
        pos (-125, 0)
        xsize 1104
        ysize 621
    Johan "(!!!!!!!!!)"
    Villager "(WOW DAMN! OKAY, KEEP CALM KEEP CALM)"
    pause
    scene rio_8:
        pos (-125, 0)
        xsize 1104
        ysize 621
    Leyna "Ooh?!!"
    if switch("netorare"):
        Johan "(Shit, they are seeing everything)"
    if switch("netorase"):
        Johan "(They're seeing everything! Fuck... just when I was thinking that this could happen it happens!)"
    pause
    scene rio_9:
        pos (-125, 0)
        xsize 1104
        ysize 621
    Villager "Oh boy, the towel has fallen off. Well don't worry too much, after all, this is a tradition here and we are all naked"
    pause
    scene rio_10:
        pos (-125, 0)
        xsize 1104
        ysize 621
    Leyna "(I have to put on the towel right now!)"
    Johan "( What the fuck!? They are huge )"
    pause
    scene rio_11:
        pos (-125, 0)
        xsize 1104
        ysize 621
    Villager "Sorry, but it's natural, isn't it? This kind of thing happens, and more after seeing a naked woman as beautiful as you"
    pause
    scene rio_12:
        pos (-125, 0)
        xsize 1104
        ysize 621
    play sound "audio/Jump2.ogg" volume 0.9 noloop
    Leyna "Ex...excuse me?"
    pause
    scene rio_13:
        pos (-125, 0)
        xsize 1104
        ysize 621
    Villager "You know, erections and that sort of thing."
    Leyna "Oh ... sure..."
    scene rio14:
        pos (-125, 0)
        xsize 1104
        ysize 621
    Villager "Well ... hey, don't you think it's a good artistic photo?I think in this position you could take a couple of good photos"
    if switch("netorare"):
        menu:
            "Okey":
                Johan "Yes ... I'll take one more photo and that's it."
                scene rio15:
                    pos (-125, 0)
                    xsize 1104
                    ysize 621
                Leyna "(what's going on?)"
                Leyna "(his ... things are very close to me ... Johan is fine with this?... I think he is not even aware of what is happening...)"
                Leyna "(I have to stop looking at... that so much. and maybe pose or something?)"
                Johan "Okay, that's it... Thanks for your help guys"
                Leyna "(!!!)"
                Villager "Thank you. Come back whenever you want!"
                Johan "(...)"
                pause
                scene black with dissolve
                hide rio15
                # fade in
                call SetPlayerLocation("Town") from _call_RiverNPCEventMan_SetPlayerLocation
                pause 0.24
                $ corruption = corruption + 2
                "CORRUPTION +2"
            "This has gone too far":
                Johan "No, enough guys! We are leaving..."
                scene black with dissolve
                # fade in
                call SetPlayerLocation("Town") from _call_RiverNPCEventMan_SetPlayerLocation_1
                pause 0.24
                $ corruption = corruption + 1
                "CORRUPTION +1"
    if switch("netorase"):
        Johan "Yes ... I'll take one more photo... or two..."
        scene rio15:
            pos (-125, 0)
            xsize 1104
            ysize 621
        Leyna "(what's going on?)"
        Leyna "(his ... things are very close to me ... Johan is fine with this?... I think he is not even aware of what is happening...)"
        Leyna "(I have to stop looking at... that so much. and maybe pose or something?)"
        Johan "Okay,  Leyna M-maybe you should get a little closer..."
        Leyna "(!!!)"
        Leyna "No... I think I've had enough for today."
        Johan "!!! !!! oh! Y-yeah sure I guess you're right, we're done for the day guys...."
        Villager "Thank you. Come back whenever you want!"
        Johan "(...)"
        pause
        scene black with dissolve
        hide rio15
        # fade in
        call SetPlayerLocation("Town") from _call_RiverNPCEventMan_SetPlayerLocation_2
        pause 0.24
        $ corruption = corruption + 2
        "CORRUPTION +2"
    $ set_switch("finished_river_scene", True)
    show plano_mujer_timida:
        xsize 1600
        ysize 900
    Leyna "( His ... \"things\" were huge. Are all like this in  here? )"
    Johan "Are you okay?"
    show plano_mujer_sorpresa_lado:
        xsize 1600
        ysize 900
    Leyna "Oh! Yes... I'm okey..."
    hide plano_mujer_timida
    hide plano_mujer_sorpresa_lado
    return

