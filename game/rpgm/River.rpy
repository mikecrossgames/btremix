label Riverentradario_0(menu_choice = None):
    pause 0.22
    pause 0.22
    Villager "Hey! you can't pass with clothes on! Tradition says one can only pass if he goes naked."
    pause 0.22
    Johan "Sorry, we are not from here, we came to make an article and take some photos of the festivities, if you give us your permission, of course"
    Villager "An article, you say? hmmm if you are worried for the woman, we can make an exception for the circumstances.."
    "..but you have to go naked, this is a sacred tradition. The girl can carry a towel on her if she wants, just for this occasion."
    Johan "great, I have no problem. What do you think Leyna?"
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    call GetChoice([_("Yes"), _("I'm not ready yet")], value=menu_choice, called_from="Riverentradario_0") from _call_Riverentradario_0_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Yes"):
        $ menu_choice = None
        Villager "Perfect. Back there you have a small tent to leave your clothes."
        Johan "Perfect, we'll interview a couple of people and take photos of those who agree"
        $ erase_picture(1)
        $ set_switch("separated_in_the_river", True)
        # TransferPlayer: "River"
        pause 0.24
    elif menu_choice == _("I'm not ready yet"):
        $ menu_choice = None
        Leyna "I think I'm not ready yet. I have to think about this a little more."
        Johan "Okey, no problem. We'll do it another time."
        $ erase_picture(1)
        # TransferPlayer: "Town"
        pause 0.24
    return

label RiverNPCEventMan(menu_choice = None):
    Johan "Good afternoon, me and my wife are doing a report on the traditions of this town..."
    "... I was wondering if you would mind answering some questions for me and let me take some pictures of you by the river."
    $ show_transparent(1, "general_chica_rio", width=1600, height=900)
    Villager "Oh! Of course, no problem man, ask what you want"
    scene black with dissolve
    $ erase_picture(1)
    hide black with dissolve
    Johan "So the celebration goes back thousands of years and is in honour of a very old fertility goddess..."
    "...how interesting! Great, now I'm going to take a couple of photos if you don't mind."
    Villager "Yes, of course ..."
    $ set_switch("separated_in_the_river", True)
    pause 0.26
    $ flash_screen([255,255,255,170], 60, True)
    Villager "I have an idea..."
    Johan "Yes?"
    Villager "It's just us in these photos. If you only show this in the article, people won't want to come to this town, right?"
    Johan "Well..."
    Villager "If you only see a group of ugly men posing on the camera it would be a disaster..."
    "...what these photos need is a feminine touch"
    $ show_transparent(1, "expresion_neutral_toalla", width=1600, height=900)
    Johan "A feminine touch?..."
    Villager "Exactly, why doesn't your wife come up and poses in a couple of photos with us?"
    $ show_transparent(2, "expresion_sorpresa_toalla", width=1600, height=900)
    Johan "I see... It makes sense, what do you think Leyna, would mind appearing in a couple of photos?..."
    "...anyway, I'm going to black out the faces and  the towel covers your body"
    Villager "(I can't believe this is working... So she's naked under the towel)"
    $ erase_picture(2)
    Leyna "yeah... well, if you think it's a good idea... I guess it doesn't seem bad to me."
    Johan "Okay. Well, put yourself in the middle and I'll take some photos"
    scene black with dissolve
    $ erase_picture(1)
    hide black with dissolve
    $ show_picture(1, "rio_1", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    Villager "(Damn... the girl smells great)"
    $ show_picture(2, "rio_2", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    Johan "Maybe you could go a little closer for the photo"
    Villager "O...Of course!"
    pause
    $ show_picture(3, "rio_3", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    Leyna "(!!!)"
    pause
    $ show_picture(4, "rio_4", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    Johan "(They are too close ... well, I'm not going to bother them too much..."
    "...after all, they are doing us a favour letting us take photos of them)"
    pause
    $ show_picture(5, "rio_5", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    Villager "( This is my chance, but I have to do it right or I'll get caught! )"
    pause
    $ show_picture(6, "rio_6", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    play music "audio/Dungeon3.ogg" loop volume 0.9
    pause
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    $ show_picture(7, "rio_7", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    Johan "(!!!!!!!!!)"
    Villager "(WOW DAMN! OKAY, KEEP CALM KEEP CALM)"
    pause
    $ show_picture(8, "rio_8", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    Leyna "Ooh?!!"
    Johan "(Shit, they are seeing everything)"
    pause
    $ show_picture(9, "rio_9", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    Villager "Oh boy, the towel has fallen off. Well don't worry too much, after all, this is a tradition here and we are all naked"
    pause
    $ show_picture(10, "rio_10", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    Leyna "(I have to put on the towel right now!)"
    Johan "( What the fuck!? They are huge )"
    pause
    $ show_picture(11, "rio_11", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    Villager "Sorry, but it's natural, isn't it? This kind of thing happens, and more after seeing a naked woman as beautiful as you"
    pause
    $ show_picture(12, "rio_12", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    play sound "audio/Jump2.ogg" volume 0.9 noloop
    Leyna "Ex...excuse me?"
    pause
    $ show_picture(13, "rio_13", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    Villager "You know, erections and that sort of thing."
    Leyna "Oh ... sure..."
    $ show_picture(14, "rio14", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
    Villager "Well ... hey, don't you think it's a good artistic photo?I think in this position you could take a couple of good photos"
    call GetChoice([_("Okey"), _("This has gone too far")], value=menu_choice, called_from="RiverNPCEventMan") from _call_RiverNPCEventMan_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Okey"):
        $ menu_choice = None
        Johan "Yes ... I'll take one more photo and that's it."
        $ show_picture(15, "rio15", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
        Leyna "(what's going on?)"
        Leyna "(his ... things are very close to me ... Johan is fine with this?... I think he is not even aware of what is happening...)"
        Leyna "(I have to stop looking at... that so much. and maybe pose or something?)"
        Johan "Okay, that's it... Thanks for your help guys"
        Leyna "(!!!)"
        Villager "Thank you. Come back whenever you want!"
        Johan "(...)"
        pause
        scene black with dissolve
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(5)
        $ erase_picture(4)
        $ erase_picture(6)
        $ erase_picture(7)
        $ erase_picture(8)
        $ erase_picture(9)
        $ erase_picture(10)
        $ erase_picture(11)
        $ erase_picture(12)
        $ erase_picture(13)
        $ erase_picture(14)
        $ erase_picture(15)
        hide black with dissolve
        # TransferPlayer: "Town"
        pause 0.24
        $ corruption = corruption + 2
        "CORRUPTION +2"
    elif menu_choice == _("This has gone too far"):
        $ menu_choice = None
        Johan "No, enough guys! We are leaving..."
        scene black with dissolve
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
        $ erase_picture(11)
        $ erase_picture(12)
        $ erase_picture(13)
        $ erase_picture(14)
        $ erase_picture(15)
        hide black with dissolve
        # TransferPlayer: "Town"
        pause 0.24
        $ corruption = corruption + 1
        "CORRUPTION +1"
    $ set_switch("finished_river_scene", True)
    $ show_transparent(1, "plano_mujer_timida", width=1600, height=900)
    Leyna "( His ... \"things\" were huge. Are all like this in  here? )"
    Johan "Are you okay?"
    $ show_transparent(2, "plano_mujer_sorpresa_lado", width=1600, height=900)
    Leyna "Oh! Yes... I'm okey..."
    $ erase_picture(1)
    $ erase_picture(2)
    return

