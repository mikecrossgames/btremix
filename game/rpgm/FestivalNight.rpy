label FestivalNightLeynaropa(menu_choice = None):
    $ show_picture(1, "festivalnoche1", width=814, height=625)
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
    $ show_picture(2, "festivalnoche2", width=814, height=625)
    Villager "Change? what for? you're perfect to go through the festival like this"
    Leyna "Like this? but I'm practically naked..."
    Villager "Aren't we all? Look..."
    $ show_picture(3, "festivalnoche3", width=814, height=625)
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
        $ show_picture(4, "festivalnoche4", width=814, height=625)
        Villager "Here Leyna, have a beer"
        Leyna "Thank you very much!"
        $ show_picture(5, "festivalnoche5", width=814, height=625)
        Leyna "Johan seems to be having a great time... I haven't seen him this relaxed for a long time"
        Leyna "Is he dancing? hahahaha he must have had a lot of beers, he hates to dance"
        Villager "Hey, aren't you going with your husband?"
        Leyna "Yes, I'll be there in a moment... it looks like he's having a great time, I'm going to leave him alone for a little bit"
        Villager "What a good wife! I wish you were married to me, a perfect woman in every way!"
        Leyna "wow hahaha thanks"
        $ show_picture(6, "pantallanegro", scale=(120, 120), width=816, height=600)
        "Some time later"
        $ show_picture(7, "festivalnoche6", width=814, height=625)
        Villager "Come on Leyna! keep the party going! hahahaha here's another beer!"
        $ show_picture(8, "festivalnoche9", width=814, height=625)
        Johan "(Le-leyna? I didn't even realize she was here.... my god she's still wearing the uniform from the food stand... it's .... very very revealing)"
        Johan "(W-why didn't she come with me?.... I don't understand anything... I'd better go say hello and see what's going on)"
        $ show_picture(9, "festivalnoche10", width=814, height=625)
        Johan "Y-you..."
        Alexa "Hey handsome... where are you going?"
        Johan "I-I was going to..."
        Alexa "Come have a beer with me!"
        Johan "I don't know if I should... I'm already pretty drunk"
        Alexa "Come on! and you call yourself a man?"
        Johan "Of course! Give me that beer!"
        Alexa "hahahaha that's the way I like it!"
        $ show_picture(10, "pantallanegro", scale=(120, 120), width=816, height=600)
        "minutes later"
        $ show_picture(11, "festivalnoche11", width=814, height=625)
        Alexa "Heey Johan... let's dance"
        Johan "I... I don't like to dance, Alexa..."
        Alexa "Ohh come on Johan don't be shy we are going to have a great time...."
        DrunkVillager "Yessssss, come on Johan a pretty girl is inviting you to dance... not accepting would be rude!"
        DrunkVillager "E-hip!-exactly! Johan you are already the envy of the whole town, you have to dance with her!"
        Johan "HeheHE hip! come on ... if you insist I can't refuse"
        Villager "That's the way to talk, man"
        $ show_picture(12, "festivalnoche12", width=814, height=625)
        play music "audio/Psychedelic-Rock.ogg" loop volume 0.9
        Alexa "Wow... it looks like you're getting a little happy down there"
        Johan "W-well, tHat'S NorMal, IsN't iT? I'm A MaN aFfter All"
        $ show_picture(13, "festivalnoche13", width=814, height=625)
        Leyna "What! What is he doing? (my god... Johan is dancing in such a sexualized way with Alexa...)"
        Leyna "I'm just really drunk, it's silly... or not! How dare you do that with another woman! Now you'll see!"
        $ show_picture(14, "festivalnoche16", width=814, height=625)
        Leyna "Hey you!"
        Villager "M-me?"
        Leyna "Y-yes you... let's dance come on"
        DrunkVillager "OOOhh you lucky bastard"
        Leyna "You want to dance too? come on, you come too!"
        DrunkVillager "WOW! of course we will dance!"
        $ show_picture(15, "festivalnoche17", width=814, height=625)
        DrunkVillager "My God, you're sexy... wait a minute!"
        DrunkVillager "(S-she's wearing a butt plug?... mother of god! She's a real nymphomaniac! Look at her going out in public like that!)"
        $ show_picture(16, "festivalnoche19", width=814, height=625)
        Villager "I-I'm sorry Leyna... I couldn't help but have an erection"
        Leyna "N-no worries (is Johan watching?)"
        $ show_picture(17, "festivalnoche17", width=814, height=625)
        Johan "(My God, is that Leyna? What is she doing with those Villagers? I've never seen her dance like that with anyone.... I'm so drunk... it's hard for me to think..."
        Johan "(Th-that guy is naked! and Leyna's backside is completely exposed... I'm getting dizzy...)"
        scene black with dissolve
        $ show_picture(18, "festivalnoche20", width=814, height=625)
        hide black with dissolve
        Johan "Uff I have definitely had too much to drink"
        $ show_picture(19, "festivalnoche21", width=814, height=625)
        Alexa "Take it easy, you're fine! Take a breath and we'll continue dancing some more"
        Johan "Hahahaha yeah, you're right I'm fine"
        "a little later"
        $ show_picture(20, "festivalnoche22", width=814, height=625)
        Johan "Wow how beautiful you are... although I feel a bit sick... I'm dizzy... where are we?"
        Alexa "Where always silly, at the festival hahahaha"
        Alexa "Why don't you give me a kiss? you'll feel better"
        Johan "I-I can't, my wife has to be around...."
        $ show_picture(21, "festivalnoche23", width=814, height=625)
        Johan "Le-leyna? ahh... uff I'm really fucked up, I need to... I need to throw up"
        Johan "I-Is that Leyna?"
        Villager "Dude, are you okay?"
        scene black with dissolve
        $ show_picture(22, "festivalnoche25", width=814, height=625)
        hide black with dissolve
        Johan "Ufff I'm terrible... blueagggh... my god... blueeeghgghggh...."
        Johan "I've never been like this before... bluueeeegh.... I'm going to die?.... blueueeeeeaaagagga"
        if switch("corruption_average"):
            $ show_picture(23, "festivalnoche26", width=814, height=625)
            Johan "What's that? They're fucking a girl in the middle of the festival.... shit and I'm missing it"
            $ set_switch("corruption_high", True)
            $ set_switch("corruption_average", False)
        if switch("corruption_low"):
            $ show_picture(23, "festivalnoche26", width=814, height=625)
            Johan "What's that? They're fucking a girl in the middle of the festival.... shit and I'm missing it"
            $ set_switch("corruption_average", True)
            $ set_switch("corruption_low", False)
        Johan "When I tell Leyna she's going to be freaked out.... uff I think I need to throw up again...."
        scene black with dissolve
        $ show_picture(24, "festivalnoche27", width=814, height=625)
        hide black with dissolve
        Alexa "Are you ok Johan? you had me worried, you had been missing for quite a while"
        Johan "Wow... you were worried about me... hehehehe you are so cute"
        Alexa "Hehehee cute? it's been a while since I've heard that...."
        $ show_picture(25, "festivalnoche28", width=814, height=625)
        Johan "He-hey! I just threw up...you shouldn't kiss me... besides, I'm married"
        Alexa "I don't care... let's make love right here, Johan..."
        Johan "What?"
        $ show_picture(26, "festivalnoche30", width=814, height=625)
        Alexa "Yessssss... let's do it right now Johan, come on, I know you're looking forward to it"
        call GetChoice([_("Fuck Alexa"), _("I can't do it")], value=menu_choice, called_from="FestivalNightLeynaropa") from _call_FestivalNightLeynaropa_GetChoice_1
        $ menu_choice = _return
        if menu_choice == _("Fuck Alexa"):
            $ menu_choice = None
            Johan "If you ask me that way... I can't say no to you honey"
            Alexa "I knew you were dying for it...come on"
            scene black with dissolve
            $ show_picture(27, "festivalnoche29", width=814, height=625)
            hide black with dissolve
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
            $ show_picture(28, "pantallanegro", scale=(120, 120), width=816, height=600)
            Johan "OOohhhh"
            Johan "My God!!! what is happening to me?"
            Johan "What the hell was in the beers?"
            Johan "I think ... yes ... I'm going to sleep ... I can't..."
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
            $ erase_picture(16)
            $ erase_picture(17)
            $ erase_picture(18)
            $ erase_picture(19)
            $ erase_picture(20)
            $ erase_picture(21)
            $ erase_picture(22)
            $ erase_picture(23)
            $ erase_picture(24)
            $ erase_picture(25)
            $ erase_picture(26)
            $ erase_picture(27)
            $ erase_picture(28)
            stop music fadeout 1
            # TransferPlayer: "Glade"
            hide black with dissolve
        elif menu_choice == _("I can't do it"):
            $ menu_choice = None
            Johan "I-I'm sorry, I can't... I love Leyna"
            Alexa "I see... too bad, you're a great guy... though your wife seems to be having a great time without you"
            Johan "W-what?"
            $ shake_screen(5, 5, 60)
            $ flash_screen([255,255,255,170], 60, True)
            stop bgs fadeout 1
            Johan "I-I don't feel so good..."
            $ show_picture(27, "pantallanegro", scale=(120, 120), width=816, height=600)
            Johan "OOohhhh"
            Johan "My God!!! what is happening to me?"
            Johan "What the hell was in the beers?"
            Johan "I think ... yes ... I'm going to sleep ... I can't..."
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
            $ erase_picture(16)
            $ erase_picture(17)
            $ erase_picture(18)
            $ erase_picture(19)
            $ erase_picture(20)
            $ erase_picture(21)
            $ erase_picture(22)
            $ erase_picture(23)
            $ erase_picture(24)
            $ erase_picture(25)
            $ erase_picture(26)
            $ erase_picture(27)
            stop music fadeout 1
            # TransferPlayer: "Glade"
            hide black with dissolve
    elif menu_choice == _("Change clothes"):
        $ menu_choice = None
        $ festival_clothes = 2
        Leyna "I-I'm sorry, but I'm still going to go change, I don't feel comfortable dressed like this"
        Villager "Sure... okay, we'll wait for you here"
        Leyna "Great, thank you very much"
        $ show_picture(4, "festivalnoche7", width=814, height=625)
        Villager "You've changed quickly"
        Leyna "Hahahaha yeah, well... let's go ?"
        Villager "Sure! here's a beer for you"
        $ show_picture(5, "festivalnoche5", width=814, height=625)
        Leyna "Johan seems to be having a great time... I haven't seen him this relaxed for a long time"
        Leyna "Is he dancing? hahahaha he must have had a lot of beers, he hates to dance"
        Villager "Hey, aren't you going with your husband?"
        Leyna "Yes, I'll be there in a moment... it looks like he's having a great time, I'm going to leave him alone for a little bit"
        Villager "What a good wife! I wish you were married to me, a perfect woman in every way!"
        Leyna "wow hahaha thanks"
        $ show_picture(6, "pantallanegro", scale=(120, 120), width=816, height=600)
        "Some time later"
        $ show_picture(7, "festivalnoche7", width=814, height=625)
        Villager "Come on Leyna! keep the party going! hahahaha here's another beer!"
        $ show_picture(8, "festivalnoche8", width=814, height=625)
        Johan "(Le-leyna? I didn't even realize she was here.... Good thing he changed his uniform before coming here)"
        Johan "(W-why didn't she come with me?.... I don't understand anything... I'd better go say hello and see what's going on)"
        $ show_picture(9, "festivalnoche10", width=814, height=625)
        Johan "Y-you..."
        Alexa "Hey handsome... where are you going?"
        Johan "I-I was going to..."
        Alexa "Come have a beer with me!"
        Johan "I don't know if I should... I'm already pretty drunk"
        Alexa "Come on! and you call yourself a man?"
        Johan "Of course! Give me that beer!"
        Alexa "hahahaha that's the way I like it!"
        $ show_picture(10, "pantallanegro", scale=(120, 120), width=816, height=600)
        "minutes later"
        $ show_picture(11, "festivalnoche11", width=814, height=625)
        Alexa "Heey Johan... let's dance"
        Johan "I... I don't like to dance, Alexa..."
        Alexa "Ohh come on Johan don't be shy we are going to have a great time...."
        DrunkVillager "Yessssss, come on Johan a pretty girl is inviting you to dance... not accepting would be rude!"
        DrunkVillager "E-hip!-exactly! Johan you are already the envy of the whole town, you have to dance with her!"
        Johan "HeheHE hip! come on ... if you insist I can't refuse"
        Villager "That's the way to talk, man"
        $ show_picture(12, "festivalnoche12", width=814, height=625)
        play music "audio/Psychedelic-Rock.ogg" loop volume 0.9
        Alexa "Wow... it looks like you're getting a little happy down there"
        Johan "W-well, tHat'S NorMal, IsN't iT? I'm A MaN aFfter All"
        $ show_picture(13, "festivalnoche14", width=814, height=625)
        Leyna "What! What is he doing? (my god... Johan is dancing in such a sexualized way with Alexa...)"
        Leyna "I'm just really drunk, it's silly... or not! How dare you do that with another woman! Now you'll see!"
        $ show_picture(14, "festivalnoche15", width=814, height=625)
        Leyna "Hey you!"
        Villager "M-me?"
        Leyna "Y-yes you... let's dance come on"
        DrunkVillager "OOOhh you lucky bastard"
        Leyna "You want to dance too? come on, you come too!"
        DrunkVillager "WOW! of course we will dance!"
        $ show_picture(15, "festivalnoche18", width=814, height=625)
        DrunkVillager "My God, you're sexy..."
        Villager "I-I'm sorry Leyna... I couldn't help but have an erection"
        Leyna "N-no worries (is Johan watching?)"
        Johan "(My God, is that Leyna? What is she doing with those Villagers? I've never seen her dance like that with anyone.... I'm so drunk... it's hard for me to think..."
        Johan "(Th-that guy is naked!... I'm getting dizzy...)"
        scene black with dissolve
        $ show_picture(16, "festivalnoche20", width=814, height=625)
        hide black with dissolve
        Johan "Uff I have definitely had too much to drink"
        $ show_picture(17, "festivalnoche21", width=814, height=625)
        Alexa "Take it easy, you're fine! Take a breath and we'll continue dancing some more"
        Johan "Hahahaha yeah, you're right I'm fine"
        $ show_picture(18, "pantallanegro", scale=(120, 120), width=816, height=600)
        "a little later"
        $ show_picture(19, "festivalnoche22", width=814, height=625)
        Johan "Wow how beautiful you are... although I feel a bit sick... I'm dizzy... where are we?"
        Alexa "Where always silly, at the festival hahahaha"
        Alexa "Why don't you give me a kiss? you'll feel better"
        Johan "I-I can't, my wife has to be around...."
        $ show_picture(20, "festivalnoche24", width=814, height=625)
        Johan "Le-leyna? ahh... uff I'm really fucked up, I need to... I need to throw up"
        Johan "I-Is that Leyna?"
        Villager "Dude, are you okay?"
        scene black with dissolve
        $ show_picture(21, "festivalnoche25", width=814, height=625)
        hide black with dissolve
        Johan "Ufff I'm terrible... blueagggh... my god... blueeeghgghggh...."
        Johan "I've never been like this before... bluueeeegh.... I'm going to die?.... blueueeeeeaaagagga"
        if switch("corruption_average"):
            $ show_picture(22, "festivalnoche31", width=814, height=625)
            Johan "What's that? it looks like there's a girl dancing topless.... shit and I'm missing it"
        if switch("corruption_low"):
            $ show_picture(22, "festivalnoche31", width=814, height=625)
            Johan "What's that? it looks like there's a girl dancing topless.... shit and I'm missing it"
        Johan "When I tell Leyna she's going to be freaked out.... uff I think I need to throw up again...."
        scene black with dissolve
        $ show_picture(23, "festivalnoche27", width=814, height=625)
        hide black with dissolve
        Alexa "Are you ok Johan? you had me worried, you had been missing for quite a while"
        Johan "Wow... you were worried about me... hehehehe you are so cute"
        Alexa "Hehehee cute? it's been a while since I've heard that...."
        $ show_picture(25, "festivalnoche28", width=814, height=625)
        Johan "He-hey! I just threw up...you shouldn't kiss me... besides, I'm married"
        $ show_picture(25, "festivalnoche30", width=814, height=625)
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
            $ show_picture(26, "festivalnoche29", width=814, height=625)
            hide black with dissolve
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
            $ show_picture(27, "pantallanegro", scale=(120, 120), width=816, height=600)
            Johan "OOohhhh"
            Johan "My God!!! what is happening to me?"
            Johan "What the hell was in the beers?"
            Johan "I think ... yes ... I'm going to sleep ... I can't..."
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
            $ erase_picture(16)
            $ erase_picture(17)
            $ erase_picture(18)
            $ erase_picture(19)
            $ erase_picture(20)
            $ erase_picture(21)
            $ erase_picture(22)
            $ erase_picture(23)
            $ erase_picture(24)
            $ erase_picture(25)
            $ erase_picture(26)
            $ erase_picture(27)
            stop music fadeout 1
            # TransferPlayer: "Glade"
            hide black with dissolve
        elif menu_choice == _("I can't do it"):
            $ menu_choice = None
            Johan "I-I'm sorry, I can't... I love Leyna very much"
            Alexa "I see... too bad, you're a great guy... though your wife seems to be having a great time without you"
            Johan "W-what?"
            $ shake_screen(5, 5, 60)
            $ flash_screen([255,255,255,170], 60, True)
            stop bgs fadeout 1
            Johan "I-I don't feel so good..."
            $ show_picture(26, "pantallanegro", scale=(120, 120), width=816, height=600)
            Johan "OOohhhh"
            Johan "My God!!! what is happening to me?"
            Johan "What the hell was in the beers?"
            Johan "I think ... yes ... I'm going to sleep ... I can't..."
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
            $ erase_picture(16)
            $ erase_picture(17)
            $ erase_picture(18)
            $ erase_picture(19)
            $ erase_picture(20)
            $ erase_picture(21)
            $ erase_picture(22)
            $ erase_picture(23)
            $ erase_picture(24)
            $ erase_picture(25)
            $ erase_picture(26)
            stop music fadeout 1
            # TransferPlayer: "Glade"
            hide black with dissolve
    return

