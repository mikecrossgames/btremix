label FestivalNightLeynaropa(menu_choice = None):
    scene festivalnoche1:
        xsize 814
        ysize 625
    $ set_switch("party_at_festival", True)
    Villager "Hey!"
    Leyna "!!! (shit, have They seen what's up my ass?)"
    Leyna "H-hey, what's up?"
    Villager "Don't you remember us? the other night we had a great time at the river with you and your husband"
    Leyna "O-oh Y-yes (That was when we got so drunk, wasn't it?... I can hardly remember what happened that night)"
    Leyna "I'm sorry, it's just that with all the drinking, that night..."
    Villager "Hahahahaha too bad, but I hear you, we were pretty drunk too"
    Leyna "Well..."
    Villager "You're not going to leave now, are you? This is when the best starts!"
    Leyna "Ah! n-no, don't worry, I have to change and I'll be right back"
    scene festivalnoche2:
        xsize 814
        ysize 625
    Villager "Change? what for? you're perfect to go through the festival like this"
    Leyna "Like this? but I'm practically naked..."
    Villager "Aren't we all? Look..."
    scene festivalnoche3:
        xsize 814
        ysize 625
    Villager "See? no shame, now I'm naked too, so you have nothing to be ashamed of"
    Leyna "I-It's just that my husband..."
    Villager "Johan? we just saw him back there, he's having a great time, he won't have time to get angry with the beer he's already drank"
    Leyna "W-well..."
    call GetChoice([_("Go with current clothing"), _("Change clothes")], value=menu_choice, called_from="FestivalNightLeynaropa") from _call_FestivalNightLeynaropa_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Go with current clothing"):
        $ menu_choice = None
        $ festival_clothes = 1
        Leyna "I guess you are right"
        Villager "Exactly! let's go and have a drink with the others!"
        Leyna "hahahaha Su-sure!"
        scene festivalnoche4:
            xsize 814
            ysize 625
        Villager "Here Leyna, have a beer"
        Leyna "Thank you very much!"
        scene festivalnoche5:
            xsize 814
            ysize 625
        Leyna "Johan seems to be having a great time... I haven't seen him this relaxed for a long time"
        Leyna "Is he dancing? hahahaha he must have had a lot of beers, he hates to dance"
        Villager "Hey, aren't you going with your husband?"
        Leyna "Yes, I'll be there in a moment... it looks like he's having a great time, I'm going to leave him alone for a little bit"
        Villager "What a good wife! I wish you were married to me, a perfect woman in every way!"
        Leyna "wow hahaha thanks"
        scene pantallanegro:
            xsize 979
            ysize 720
        "Some time later"
        scene festivalnoche6:
            xsize 814
            ysize 625
        Villager "Come on Leyna! keep the party going! hahahaha here's another beer!"
        scene festivalnoche9:
            xsize 814
            ysize 625
        Johan "(Le-leyna? I didn't even realize she was here.... my god she's still wearing the uniform from the food stand... it's .... very very revealing)"
        Johan "(W-why didn't she come with me?.... I don't understand anything... I'd better go say hello and see what's going on)"
        scene festivalnoche10:
            xsize 814
            ysize 625
        Johan "Y-you..."
        Alexa "Hey handsome... where are you going?"
        Johan "I-I was going to..."
        Alexa "Come have a beer with me!"
        Johan "I don't know if I should... I'm already pretty drunk"
        Alexa "Come on! and you call yourself a man?"
        Johan "Of course! Give me that beer!"
        Alexa "hahahaha that's the way I like it!"
        scene pantallanegro:
            xsize 979
            ysize 720
        "minutes later"
        scene festivalnoche11:
            xsize 814
            ysize 625
        Alexa "Heey Johan... let's dance"
        Johan "I... I don't like to dance, Alexa..."
        Alexa "Ohh come on Johan don't be shy we are going to have a great time...."
        DrunkVillager "Yessssss, come on Johan a pretty girl is inviting you to dance... not accepting would be rude!"
        DrunkVillager "E-hip!-exactly! Johan you are already the envy of the whole town, you have to dance with her!"
        Johan "HeheHE hip! come on ... if you insist I can't refuse"
        Villager "That's the way to talk, man"
        scene festivalnoche12:
            xsize 814
            ysize 625
        play music "audio/Psychedelic-Rock.ogg" loop volume 0.9
        Alexa "Wow... it looks like you're getting a little happy down there"
        Johan "W-well, tHat'S NorMal, IsN't iT? I'm A MaN aFfter All"
        scene festivalnoche13:
            xsize 814
            ysize 625
        Leyna "What! What is he doing? (my god... Johan is dancing in such a sexualized way with Alexa...)"
        Leyna "I'm just really drunk, it's silly... or not! How dare you do that with another woman! Now you'll see!"
        scene festivalnoche16:
            xsize 814
            ysize 625
        Leyna "Hey you!"
        Villager "M-me?"
        Leyna "Y-yes you... let's dance come on"
        DrunkVillager "OOOhh you lucky bastard"
        Leyna "You want to dance too? come on, you come too!"
        DrunkVillager "WOW! of course we will dance!"
        scene festivalnoche17:
            xsize 814
            ysize 625
        DrunkVillager "My God, you're sexy... wait a minute!"
        DrunkVillager "(S-she's wearing a butt plug?... mother of god! She's a real nymphomaniac! Look at her going out in public like that!)"
        scene festivalnoche19:
            xsize 814
            ysize 625
        Villager "I-I'm sorry Leyna... I couldn't help but have an erection"
        Leyna "N-no worries (is Johan watching?)"
        scene festivalnoche17:
            xsize 814
            ysize 625
        Johan "(My God, is that Leyna? What is she doing with those Villagers? I've never seen her dance like that with anyone.... I'm so drunk... it's hard for me to think..."
        Johan "(Th-that guy is naked! and Leyna's backside is completely exposed... I'm getting dizzy...)"
        scene black with dissolve
        show festivalnoche20 with dissolve:
            xsize 814
            ysize 625
        Johan "Uff I have definitely had too much to drink"
        scene festivalnoche21:
            xsize 814
            ysize 625
        Alexa "Take it easy, you're fine! Take a breath and we'll continue dancing some more"
        Johan "Hahahaha yeah, you're right I'm fine"
        "a little later"
        scene festivalnoche22:
            xsize 814
            ysize 625
        Johan "Wow how beautiful you are... although I feel a bit sick... I'm dizzy... where are we?"
        Alexa "Where always silly, at the festival hahahaha"
        Alexa "Why don't you give me a kiss? you'll feel better"
        Johan "I-I can't, my wife has to be around...."
        scene festivalnoche23:
            xsize 814
            ysize 625
        Johan "Le-leyna? ahh... uff I'm really fucked up, I need to... I need to throw up"
        Johan "I-Is that Leyna?"
        Villager "Dude, are you okay?"
        scene black with dissolve
        show festivalnoche25 with dissolve:
            xsize 814
            ysize 625
        Johan "Ufff I'm terrible... blueagggh... my god... blueeeghgghggh...."
        Johan "I've never been like this before... bluueeeegh.... I'm going to die?.... blueueeeeeaaagagga"
        if switch("corruption_average"):
            scene festivalnoche26:
                xsize 814
                ysize 625
            Johan "What's that? They're fucking a girl in the middle of the festival.... shit and I'm missing it"
            $ set_switch("corruption_high", True)
            $ set_switch("corruption_average", False)
        if switch("corruption_low"):
            scene festivalnoche26:
                xsize 814
                ysize 625
            Johan "What's that? They're fucking a girl in the middle of the festival.... shit and I'm missing it"
            $ set_switch("corruption_average", True)
            $ set_switch("corruption_low", False)
        Johan "When I tell Leyna she's going to be freaked out.... uff I think I need to throw up again...."
        scene black with dissolve
        show festivalnoche27 with dissolve:
            xsize 814
            ysize 625
        Alexa "Are you ok Johan? you had me worried, you had been missing for quite a while"
        Johan "Wow... you were worried about me... hehehehe you are so cute"
        Alexa "Hehehee cute? it's been a while since I've heard that...."
        scene festivalnoche28:
            xsize 814
            ysize 625
        Johan "He-hey! I just threw up...you shouldn't kiss me... besides, I'm married"
        Alexa "I don't care... let's make love right here, Johan..."
        Johan "What?"
        scene festivalnoche30:
            xsize 814
            ysize 625
        Alexa "Yessssss... let's do it right now Johan, come on, I know you're looking forward to it"
        call GetChoice([_("Fuck Alexa"), _("I can't do it")], value=menu_choice, called_from="FestivalNightLeynaropa") from _call_FestivalNightLeynaropa_GetChoice_1
        $ menu_choice = _return
        if menu_choice == _("Fuck Alexa"):
            $ menu_choice = None
            Johan "If you ask me that way... I can't say no to you honey"
            Alexa "I knew you were dying for it...come on"
            scene black with dissolve
            show festivalnoche29 with dissolve:
                xsize 814
                ysize 625
            play bgs "audio/audio follar.ogg" loop volume 0.9
            Alexa "Like that... slowly... ahhh"
            Alexa "Very good...."
            Alexa "You certainly don't have as big a dick as the guys in this town, but at least you don't cum after 5 seconds"
            Johan "Hehehehe I take it as a compliment"
            Alexa "It is, let's go to a more comfortable place"
            Johan "A more comfortable place?"
            $ shake_screen(5, 5, 60)
            $ flash_screen([255,255,255,170], 60, True)
            stop bgs fadeout 1
            Johan "I-I don't feel so good..."
            scene pantallanegro:
                xsize 979
                ysize 720
            Johan "OOohhhh"
            Johan "My God!!! what is happening to me?"
            Johan "What the hell was in the beers?"
            Johan "I think ... yes ... I'm going to sleep ... I can't..."
            scene black with dissolve
            hide festivalnoche1
            hide festivalnoche2
            hide festivalnoche3
            hide festivalnoche4
            hide festivalnoche5
            hide pantallanegro
            hide festivalnoche6
            hide festivalnoche9
            hide festivalnoche10
            hide pantallanegro
            hide festivalnoche11
            hide festivalnoche12
            hide festivalnoche13
            hide festivalnoche16
            hide festivalnoche17
            hide festivalnoche19
            hide festivalnoche17
            hide festivalnoche20
            hide festivalnoche21
            hide festivalnoche22
            hide festivalnoche23
            hide festivalnoche25
            hide festivalnoche26
            hide festivalnoche27
            hide festivalnoche28
            hide festivalnoche30
            hide festivalnoche29
            hide pantallanegro
            stop music fadeout 1
            # TransferPlayer: "Glade"
            # fade in
        elif menu_choice == _("I can't do it"):
            $ menu_choice = None
            Johan "I-I'm sorry, I can't... I love Leyna"
            Alexa "I see... too bad, you're a great guy... though your wife seems to be having a great time without you"
            Johan "W-what?"
            $ shake_screen(5, 5, 60)
            $ flash_screen([255,255,255,170], 60, True)
            stop bgs fadeout 1
            Johan "I-I don't feel so good..."
            scene pantallanegro:
                xsize 979
                ysize 720
            Johan "OOohhhh"
            Johan "My God!!! what is happening to me?"
            Johan "What the hell was in the beers?"
            Johan "I think ... yes ... I'm going to sleep ... I can't..."
            scene black with dissolve
            hide pantallanegro
            stop music fadeout 1
            # TransferPlayer: "Glade"
            # fade in
    elif menu_choice == _("Change clothes"):
        $ menu_choice = None
        $ festival_clothes = 2
        Leyna "I-I'm sorry, but I'm still going to go change, I don't feel comfortable dressed like this"
        Villager "Sure... okay, we'll wait for you here"
        Leyna "Great, thank you very much"
        scene festivalnoche7:
            xsize 814
            ysize 625
        Villager "You've changed quickly"
        Leyna "Hahahaha yeah, well... let's go ?"
        Villager "Sure! here's a beer for you"
        scene festivalnoche5:
            xsize 814
            ysize 625
        Leyna "Johan seems to be having a great time... I haven't seen him this relaxed for a long time"
        Leyna "Is he dancing? hahahaha he must have had a lot of beers, he hates to dance"
        Villager "Hey, aren't you going with your husband?"
        Leyna "Yes, I'll be there in a moment... it looks like he's having a great time, I'm going to leave him alone for a little bit"
        Villager "What a good wife! I wish you were married to me, a perfect woman in every way!"
        Leyna "wow hahaha thanks"
        scene pantallanegro:
            xsize 979
            ysize 720
        "Some time later"
        scene festivalnoche7:
            xsize 814
            ysize 625
        Villager "Come on Leyna! keep the party going! hahahaha here's another beer!"
        scene festivalnoche8:
            xsize 814
            ysize 625
        Johan "(Le-leyna? I didn't even realize she was here.... Good thing he changed his uniform before coming here)"
        Johan "(W-why didn't she come with me?.... I don't understand anything... I'd better go say hello and see what's going on)"
        scene festivalnoche10:
            xsize 814
            ysize 625
        Johan "Y-you..."
        Alexa "Hey handsome... where are you going?"
        Johan "I-I was going to..."
        Alexa "Come have a beer with me!"
        Johan "I don't know if I should... I'm already pretty drunk"
        Alexa "Come on! and you call yourself a man?"
        Johan "Of course! Give me that beer!"
        Alexa "hahahaha that's the way I like it!"
        scene pantallanegro:
            xsize 979
            ysize 720
        "minutes later"
        scene festivalnoche11:
            xsize 814
            ysize 625
        Alexa "Heey Johan... let's dance"
        Johan "I... I don't like to dance, Alexa..."
        Alexa "Ohh come on Johan don't be shy we are going to have a great time...."
        DrunkVillager "Yessssss, come on Johan a pretty girl is inviting you to dance... not accepting would be rude!"
        DrunkVillager "E-hip!-exactly! Johan you are already the envy of the whole town, you have to dance with her!"
        Johan "HeheHE hip! come on ... if you insist I can't refuse"
        Villager "That's the way to talk, man"
        scene festivalnoche12:
            xsize 814
            ysize 625
        play music "audio/Psychedelic-Rock.ogg" loop volume 0.9
        Alexa "Wow... it looks like you're getting a little happy down there"
        Johan "W-well, tHat'S NorMal, IsN't iT? I'm A MaN aFfter All"
        scene festivalnoche14:
            xsize 814
            ysize 625
        Leyna "What! What is he doing? (my god... Johan is dancing in such a sexualized way with Alexa...)"
        Leyna "I'm just really drunk, it's silly... or not! How dare you do that with another woman! Now you'll see!"
        scene festivalnoche15:
            xsize 814
            ysize 625
        Leyna "Hey you!"
        Villager "M-me?"
        Leyna "Y-yes you... let's dance come on"
        DrunkVillager "OOOhh you lucky bastard"
        Leyna "You want to dance too? come on, you come too!"
        DrunkVillager "WOW! of course we will dance!"
        scene festivalnoche18:
            xsize 814
            ysize 625
        DrunkVillager "My God, you're sexy..."
        Villager "I-I'm sorry Leyna... I couldn't help but have an erection"
        Leyna "N-no worries (is Johan watching?)"
        Johan "(My God, is that Leyna? What is she doing with those Villagers? I've never seen her dance like that with anyone.... I'm so drunk... it's hard for me to think..."
        Johan "(Th-that guy is naked!... I'm getting dizzy...)"
        scene black with dissolve
        show festivalnoche20 with dissolve:
            xsize 814
            ysize 625
        Johan "Uff I have definitely had too much to drink"
        scene festivalnoche21:
            xsize 814
            ysize 625
        Alexa "Take it easy, you're fine! Take a breath and we'll continue dancing some more"
        Johan "Hahahaha yeah, you're right I'm fine"
        scene pantallanegro:
            xsize 979
            ysize 720
        "a little later"
        scene festivalnoche22:
            xsize 814
            ysize 625
        Johan "Wow how beautiful you are... although I feel a bit sick... I'm dizzy... where are we?"
        Alexa "Where always silly, at the festival hahahaha"
        Alexa "Why don't you give me a kiss? you'll feel better"
        Johan "I-I can't, my wife has to be around...."
        scene festivalnoche24:
            xsize 814
            ysize 625
        Johan "Le-leyna? ahh... uff I'm really fucked up, I need to... I need to throw up"
        Johan "I-Is that Leyna?"
        Villager "Dude, are you okay?"
        scene black with dissolve
        show festivalnoche25 with dissolve:
            xsize 814
            ysize 625
        Johan "Ufff I'm terrible... blueagggh... my god... blueeeghgghggh...."
        Johan "I've never been like this before... bluueeeegh.... I'm going to die?.... blueueeeeeaaagagga"
        if switch("corruption_average"):
            scene festivalnoche31:
                xsize 814
                ysize 625
            Johan "What's that? it looks like there's a girl dancing topless.... shit and I'm missing it"
        if switch("corruption_low"):
            scene festivalnoche31:
                xsize 814
                ysize 625
            Johan "What's that? it looks like there's a girl dancing topless.... shit and I'm missing it"
        Johan "When I tell Leyna she's going to be freaked out.... uff I think I need to throw up again...."
        scene black with dissolve
        show festivalnoche27 with dissolve:
            xsize 814
            ysize 625
        Alexa "Are you ok Johan? you had me worried, you had been missing for quite a while"
        Johan "Wow... you were worried about me... hehehehe you are so cute"
        Alexa "Hehehee cute? it's been a while since I've heard that...."
        scene festivalnoche28:
            xsize 814
            ysize 625
        Johan "He-hey! I just threw up...you shouldn't kiss me... besides, I'm married"
        scene festivalnoche30:
            xsize 814
            ysize 625
        Alexa "I don't care... let's make love right here, Johan..."
        Johan "What?"
        Alexa "Yessssss... let's do it right now Johan, come on, I know you're looking forward to it"
        call GetChoice([_("Fuck Alexa"), _("I can't do it")], value=menu_choice, called_from="FestivalNightLeynaropa") from _call_FestivalNightLeynaropa_GetChoice_2
        $ menu_choice = _return
        if menu_choice == _("Fuck Alexa"):
            $ menu_choice = None
            Johan "If you ask me that way... I can't say no to you honey"
            Alexa "I knew you were dying for it...come on"
            scene black with dissolve
            show festivalnoche29 with dissolve:
                xsize 814
                ysize 625
            play bgs "audio/audio follar.ogg" loop volume 0.9
            Alexa "Like that... slowly... ahhh"
            Alexa "Very good...."
            Alexa "You certainly don't have as big a dick as the guys in this town, but at least you don't cum after 5 seconds"
            Johan "Hehehehe I take it as a compliment"
            Alexa "It is, let's go to a more comfortable place"
            Johan "A more comfortable place?"
            $ shake_screen(5, 5, 60)
            $ flash_screen([255,255,255,170], 60, True)
            stop bgs fadeout 1
            Johan "I-I don't feel so good..."
            scene pantallanegro:
                xsize 979
                ysize 720
            Johan "OOohhhh"
            Johan "My God!!! what is happening to me?"
            Johan "What the hell was in the beers?"
            Johan "I think ... yes ... I'm going to sleep ... I can't..."
            scene black with dissolve
            hide festivalnoche7
            hide festivalnoche5
            hide pantallanegro
            hide festivalnoche7
            hide festivalnoche8
            hide festivalnoche10
            hide pantallanegro
            hide festivalnoche11
            hide festivalnoche12
            hide festivalnoche14
            hide festivalnoche15
            hide festivalnoche18
            hide festivalnoche20
            hide festivalnoche21
            hide pantallanegro
            hide festivalnoche22
            hide festivalnoche24
            hide festivalnoche25
            hide festivalnoche31
            hide festivalnoche27
            hide festivalnoche30
            hide festivalnoche29
            hide pantallanegro
            stop music fadeout 1
            # TransferPlayer: "Glade"
            # fade in
        elif menu_choice == _("I can't do it"):
            $ menu_choice = None
            Johan "I-I'm sorry, I can't... I love Leyna very much"
            Alexa "I see... too bad, you're a great guy... though your wife seems to be having a great time without you"
            Johan "W-what?"
            $ shake_screen(5, 5, 60)
            $ flash_screen([255,255,255,170], 60, True)
            stop bgs fadeout 1
            Johan "I-I don't feel so good..."
            scene pantallanegro:
                xsize 979
                ysize 720
            Johan "OOohhhh"
            Johan "My God!!! what is happening to me?"
            Johan "What the hell was in the beers?"
            Johan "I think ... yes ... I'm going to sleep ... I can't..."
            scene black with dissolve
            hide pantallanegro
            stop music fadeout 1
            # TransferPlayer: "Glade"
            # fade in
    return

