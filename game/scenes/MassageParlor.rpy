label MassageParlorICantWaitToHaveARelaxingMassage_0:
    play music "audio/Theme2.ogg" loop volume 0.9
    pause 0.24
    pause 0.2
    Leyna "I can't wait to have a relaxing massage"
    Johan "Yeah.. but it seems that we have to go separated"
    Leyna "Oh.. it's okay, we are here to relax anyway"
    Leyna "Maybe I fall asleep hahaha"
    Johan "Try not to, there are many things to do at the festival"
    Johan "See you later honey"
    scene black with dissolve
    play sound "audio/Move1.ogg" volume 0.9 noloop
    # fade in
    scene masage1
    "David: Hi, my name is David, I'm going to give you the massage"
    scene masage2
    Leyna "David? I thought it was going to be a woman.."
    scene masage3
    "David: Is there a problem?"
    Leyna "Oh, no, don't worry. I'm here to enjoy and I really need a massage"
    "David: Okay then, please take a seat (she's so cute, all blushed)"
    scene masage4
    "David: What is it going to be? The back, shoulders, legs.."
    Leyna "I usually have back pain, so there would be fine"
    "David: (no wonder, her tits are big and perfect...)"
    "David: Perfect, let's begin"
    scene masage5
    "David: Are you comfortable? Sorry, you didn't tell me your name"
    Leyna "I..I'm Leyna (this is how they massage here? With this damn clothes I can feel... his thing)"
    "David: What a beautiful name.. Leyna.. Your skin is so soft"
    "David: I have to take off your bra, sorry, is for the massage.. (the best part of my job)"
    scene masage6
    Leyna "I understand, don't worry, do your thing (he is so gentle, not like the rest of the villagers)"
    scene masage7
    "David: Much better like this. I see you have a couple of contractures around here.."
    Leyna "Really? My husband never gives me massages, that's why it hurts from time to time .."
    scene masage8
    "David: So you are married? (Fuck, goodbye to my chances)"
    scene masage9
    Leyna "Yes, he is in the other room. Are all the masseurs here that good? I'm going to get jealous"
    scene masage10
    "David: Not like me, I'm the best"
    scene masage11
    Leyna "Oh .. I see .. (is he flirting with me?)"
    if switch("ate_the_fruit"):
        scene masage8
        "David: You are a pretty woman, your husband should give you massages from time to time"
        "David: With my previous girlfriend, we used it as a warm-up before having sex"
        "David: That was the best sex of my life. I can teach you if you want to try it with your husband"
        scene masage11
        Leyna "S..sure, go ahead (this situation is turning me on, that fruit is quite strong)"
        scene masage10
        "David: You start by gently touching the back, with a little pressure on the butt.."
        "David: You can make small movements, as if you were fucking but without doing it, you know? (this ass is so nice..)"
        scene masage11
        Leyna "(This guy is so sexy..)"
        Leyna "(The way he's touching me... johan never touches me like this, i can barely think straight... i feel sooo hot)"
        Leyna "(I.. I can't help it.. I think I'm going to... i need it)"
        scene masagefruta1
        Leyna "Wh..what else? (please don't stop)"
        "David: You keep doing this for a while and then.."
        scene masagefruta2
        "David: (Wait, is she masturbating? Okay, calm down, maybe if you keep talking about the technique..)"
        "David: By this moment, you both should be turned on so.."
        scene masagefruta3
        "David: This is when your husband should start rubbing gently until.."
        Leyna "(is it touching me down there? ... with her huge... I should say something ... but I don't want it to stop)"
        pause
        scene masagefruta4
        Leyna "Until what?.. What is next? (I'm getting too carried away but I can't ...)"
        scene masagefruta5
        "David: He shall start pushing, not too hard or the situation will be finished too soon"
        Leyna "Ooooh... (It's ... it's much bigger than johan's)"
        pause
        scene masagefruta6
        Leyna "O..okay, I think I can imagine it, and then..?"
        "David: (Fuck, this is so good) Th..then, you can try other postures, maybe you can take the initiative.."
        "David: What do you like the most, Leyna?"
        Leyna "Me? I'm.. quite traditional, I don't really know.."
        pause
        scene masagefruta7
        "David: A man with initiative has to know how to treat a woman, do you like it rough, Leyna ?"
        Leyna "OHH, that's good!"
        pause
        scene masagefruta8
        "David: Come here, I want you to take a good memory of the massage"
        Leyna "Wa-wait we shouldn't..."
        "David: Sssh quiet...You don't want them to listen to us, right?"
        Leyna "hmmm..."
        pause
        scene masagefruta9
        play bgs "audio/audio follar.ogg" loop volume 0.9
        Leyna "Mmmmmm .. ( this boy is ...!!!)"
        Leyna "B...but.. please stop.. my husband.."
        "David: Don't worry, it's just a moment"
        Leyna "(What if Johan seed us? I have to stop even though I'm.. going to... ) OOOooh!!"
        Leyna "Stop!! Stop please! this is so wrong.."
        pause
        scene black with dissolve
        stop bgs fadeout 1
        show masagefruta10 with dissolve
        "David: Leyna, sorry.. I didn't mean to.. it's just the situation.."
        Leyna "Fuck, what was I thinking?"
        scene black with dissolve
        Johan "Leyna?"
        show masagefruta11 with dissolve
        Johan "Leyna? Are you finished?"
        Leyna "Yes! I'm done.."
        Johan "It was amazing, I'm so relaxed now, you look relaxed too"
        Leyna "Yeah.. let's get a sit by some tree"
        Johan "Okay honey. Hey guy, thanks for the massage!"
        "David: ................."
        scene black with dissolve
        hide masagefruta9
        hide masagefruta10
        hide masagefruta11
        call SetPlayerLocation("Festival") from _call_MassageParlorEV003_0_SetPlayerLocation
        # fade in
        pause 0.26
        $ set_switch("massage_sex", True)
        Leyna "(Why I've done that? What were you thinking Leyna? You love Johan!...This never has to happen again!... even if it felt sooo good....)"
        Johan "I'm tired right now, can we go back to the inn and get some rest?"
        Leyna "Yeah! Of course..."
        "Leyna had sex with another man apart from Johan, something inside her is shaken ..."
        "Let's hope David doesn't say anything to the other men in town"
    if not switch("ate_the_fruit"):
        scene masage8
        "David: You are a pretty woman, your husband should give you massages from time to time"
        "David: I can teach you how, if you want to try it with your husband"
        Leyna "I.. I don't think this is appropriated.."
        "David: Oh, sorry.. I didn't mean to make you feel uncomfortable (I think I should stop, she definitely doesn't want anything)"
        Leyna "Don't worry, it's okay"
        scene masage10
        "David: So.. we are almost finished, just some pressure around here.. (at least I can touch something)"
        Leyna "(Thats my butt.. )"
        scene black with dissolve
        show masagemastur1 with dissolve
        "David: We are finished, I hope you enjoyed it"
        Leyna "It has been very relaxing (I think I got a little horny..)"
        "David: I'm glad to hear that. See you another time, and don't forget to get dressed before leaving"
        scene masagemastur2
        Leyna "W...what? (Oh my god, I forgot I was half naked)"
        "David: They are beautiful, don't be ashamed (I wish my girlfriend's were that big..)"
        Leyna "T..thanks.."
        scene black with dissolve
        play sound "audio/Move1.ogg" volume 0.9 noloop
        show masagemastur3 with dissolve
        Leyna "I'm glad he left, with those hands and that voice, I was getting horny"
        Leyna "Johan is not finished yet, maybe.."
        scene masage11
        Leyna "If I lay here before he ends, nobody will see me.."
        Leyna "I wish Johan would give me massages like the one David gave me"
        Leyna "He.. he seems very delicate when touching a woman.."
        Leyna "What if you come in now and see me like this?.. Oh .."
        Leyna "If I wasn't married I'd just let him ...mm.."
        scene masagemastur5
        Leyna "I can imagine him massaging my whole body and .."
        Leyna "Hmmmm..."
        $ set_switch("massage_masturbation", True)
        scene black with dissolve
        hide masagemastur5
        call SetPlayerLocation("MassageParlor") from _call_MassageParlorEV003_0_SetPlayerLocation_1
        # fade in
        pause 0.36
        Johan "Mmm, where is Leyna? she should have finished already. Should I go see her? ... I don't want to interrupt the massage"
        menu:
            "See her":
                $ set_switch("johan_mira_massage", True)
                Johan "Yeah, why not?"
                pause 0.50
                pause 0.2
                scene masagentr
                Johan "(WHAT?!...what the hell is she doing?... in a place like this ...)"
                Johan "(Anyone could see her... didn't imagine she liked doing these things)"
                Johan "(.. why am I getting hard seeing her in this situation?..)"
                pause
                hide masagentr
                pause 0.26
                pause 0.2
                Johan "(.. I'm going to pretend that I haven't seen anything.. I'll stay here so no one can see her and wait for her to finish.. Leyna..)"
                scene black with dissolve
                call SetPlayerLocation("Festival") from _call_MassageParlorEV003_0_SetPlayerLocation_2
                # fade in
                pause 0.26
                Leyna "I feel soooo good and relaxed..."
                Johan "Yeah... I'm tired right now, can we go back to the inn and get some rest?"
                Leyna "Yeah! Of course"
            "Don't":
                Johan "Nah, I don't want to interrupt"
                Johan "I'll just wait here"
                scene black with dissolve
                call SetPlayerLocation("Festival") from _call_MassageParlorEV003_0_SetPlayerLocation_3
                # fade in
                pause 0.26
                Leyna "I feel soooo good and relaxed..."
                Johan "Yeah... I'm tired right now, can we go back to the inn and get some rest?"
                Leyna "Yeah! Of course"
    if switch("ate_the_fruit"):
        $ corruption = corruption + 5
    if not switch("ate_the_fruit"):
        $ corruption = corruption + 2
    scene black with dissolve
    call SetPlayerLocation("InnNight") from _call_MassageParlorEV003_0_SetPlayerLocation_4
    # fade in
    return

