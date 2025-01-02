label InnRoomsDEJANDOlasmaletas_0:
    Johan "Well this is the room ... it's a little small but it has its charm."
    Leyna "I love it!. let's leave our things and go for a walk."
    scene black with dissolve
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    # fade in
    $ suitcases = 1
    $ set_switch("suitcases", True)
    return

label InnRoomsSleep_0:
    "Do you want to wait until night?"
    menu:
        "Yes":
            scene black with dissolve
            if not renpy.in_rollback():
                $ _saved_bgm = renpy.music.get_playing()
            play music "audio/Inn.ogg" volume 0.9 noloop
            if _saved_bgm is not None and not renpy.in_rollback():
                queue music _saved_bgm
                $ _saved_bgm = None
            call SetPlayerLocation("InnRoomsNight") from _call_InnRoomsSleep_0_SetPlayerLocation
            # fade in
        "No":
            pass
    return

label InnRoomssueojohan_0:
    pause 0.42
    Leyna "Time to sleep"
    Johan "Yes, I'm exhausted"
    scene black with dissolve
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    pause 0.6
    play music "audio/Dungeon1.ogg" loop volume 0.9
    Johan "(Hmmm... What's this? I feel... strange)"
    if switch("johan_silent"):
        show publico14 with dissolve
        Johan "Oh no.. this again?"
        pause
        scene publico16
        Johan "(S-stop!... Shit! I can't move or speak)"
        Johan "(What the hell do you think you're doing to my wife?)"
        pause
        hide publico16
    if switch("johan_intervened"):
        scene publico13
        # fade in
        Johan "Oh no.. this again?"
        Johan "(Why are you looking at my wife like this?)"
        scene publico16
        Johan "(Hey! What the hell are you doing with my wife?)"
        Johan "(S-stop!... Shit! I can't move or speak)"
        pause
        hide publico16
    scene sue_o1
    OldMan "Yeah, that position is perfect!"
    Johan "(Perfect?!, stop touching her!)"
    Villager1 "I have an idea! Did you want risque photos right? Well, look"
    scene sue_o2
    OldMan "Yeah! Great work guys!"
    Johan "(No! Stop!)"
    Villager2 "Shit! Look at those tits, they're perfect!"
    Villager1 "Yeah! Fuck this I can't hold it anymore"
    scene sue_o3
    Johan "(They have taken out their cocks! Leyna, Leyna say something!)"
    Villager1 "What do you think honey, you like what you see?"
    Leyna "They're ... they're huge"
    Villager2 "Seems she is enjoying it. Hey photographer! Take a picture of this, surely the magazine will love it"
    pause
    scene sue_o4
    OldMan "Yes!"
    Villager2 "It seems that you are wet down there precious"
    Leyna "Wha-What are you going to do?"
    Villager2 "Shhhh, quiet. Just enjoy bitch"
    pause
    scene sue_o6
    Johan "(He is fucking her! Stop!... Why?... Why I feel like this? I'm getting hard)"
    Leyna "OOoohh it's sooo big!"
    Villager2 "Just say it bitch! Say \"fuck me\""
    Leyna "I.. I... fuck me"
    Villager2 "What?"
    Leyna "Fuck me please"
    Villager2 "Okey!"
    scene sue_o7
    play bgs "audio/audio follar.ogg" loop volume 0.9
    Johan "(Am I enjoying this?... Why can't I stop looking at? This feeling in my stomach ... I've never felt like this)"
    Villager2 "YEAH! You like it?"
    Leyna "I LOVE IT, PLEASE FUCK ME HARDER!"
    Johan "(No... please stop! I can't take this anymore!)"
    scene black with dissolve
    stop music fadeout 1
    stop bgs fadeout 1
    hide sue_o7
    call SetPlayerLocation("InnRooms") from _call_InnRoomssueojohan_0_SetPlayerLocation
    # fade in
    pause 0.22
    Johan "LEYNA!!"
    pause 0.38
    pause 0.2
    Johan "... It was just a dream..."
    Johan "Shit! I have an erection..."
    Johan "Where is Leyna?.."
    pause 0.32
    $ johan_dream = 1
    call SetPlayerLocation("Inn") from _call_InnRoomssueojohan_0_SetPlayerLocation_1
    return

label InnRoomsescenadildo_0:
    pause 0.28
    scene black with dissolve
    call SetPlayerLocation("InnRooms") from _call_InnRoomsescenadildo_0_SetPlayerLocation
    pause 0.24
    # fade in
    Leyna "...Well, what do you want to talk to me about?"
    Johan "I'm... well... I'm a little nervous... let's see... I want us to enjoy a little more, you know?"
    Leyna "???"
    Johan "Lately our sex life has been a little... monotonous, so I thought I'd make things a little more interesting"
    Leyna "O-oh! I see... what did you have in mind?"
    Johan "I... well, the truth is that I've heard a lot of good things about... ahem... well about anal sex"
    Leyna "A-anal sex?"
    Johan "Y-yes... and the truth is that I would like to try it... we have never done it... and well... that's all, a friend left me this"
    Leyna "!!!!"
    Johan "It's for you... I've been told that you can't do it in a rough way and that first you have to... practice so to speak... you know..."
    Leyna "I..."
    Johan "Y-you don't have to answer me now but think about it, okay?"
    Leyna "Wait!... ok... let's try it, the truth is that I was also curious"
    Johan "WOW! really? Great!"
    Leyna "(Hahahaha looks like a kid with a new toy) But I have to try it alone first, okay?"
    Johan "YES YES! relax, I have to go for a walk so I'll be out for the rest of the afternoon... ahem I.... well let me know how it goes"
    Leyna "Haahahahaha sure Johan... see you later"
    scene black with dissolve
    call SetPlayerLocation("Town2") from _call_InnRoomsescenadildo_0_SetPlayerLocation_1
    # fade in
    Johan "WOw, I can't believe she said yes!...."
    Johan "I'm a little nervous about it... but I can't wait to try it out"
    scene black with dissolve
    call SetPlayerLocation("InnRooms") from _call_InnRoomsescenadildo_0_SetPlayerLocation_2
    # fade in
    pause 0.2
    Leyna "Well... I guess now is as good a time as any to try this sucker...."
    scene dildo1
    Leyna "I should close the door, though... anyone could see me here"
    Leyna "Wow... looks like he also left me a lubricant I guess that makes sense"
    Leyna "... I can't believe I'm going to do this right now...."
    scene dildo2
    Leyna "It's... quite big... Is that okay with Johan? This thing is much bigger than his penis...."
    Leyna "Just thinking about what I'm going to do already makes me wet down there"
    Leyna "Well there is no point in waiting..."
    scene dildo3
    Leyna "I haven't even started and I'm already so horny....."
    Leyna "hmmmmm...."
    pause
    scene dildo4
    Leyna "will this fit?...it's so big...."
    Leyna "Let's do it little by little... I don't want to hurt myself"
    pause
    scene dildo5
    Leyna "Ahhh... little by little... hmmm... it hurts a little... but"
    Leyna "Ahhh... it's coming in... ohhh"
    pause
    scene dildo6
    Leyna "This is it... almost to the bottom... my god this feels... feels much better than I expected..."
    Leyna "I can't believe how good this feels... I'm going to cum... and I just put it in....."
    pause
    scene dildo7
    Leyna "AH!... this thing vibrates... and it's stimulating my clitoris while penetrating my ass..."
    Leyna "It feels amazing!.... AH ah ah ah!"
    Leyna "This... this is amazing"
    pause
    scene dildo8
    play bgs "audio/audio follar.ogg" loop volume 0.9
    Leyna "Ah ah ah!!! .... AAAHH!!!"
    Leyna "It hurts a little but .... feels amazing"
    Leyna "I'm going to cum! I'M CUMMING!!!"
    Leyna "aaaaahhhhH!!!"
    pause
    scene dildo9
    stop bgs fadeout 1
    Leyna "AAAAAAAAAHHH!!!"
    Leyna "I've already cum.... I haven't lasted at all, I've never cum so fast... this has been awesome"
    Leyna "I can't... I can't wait to do it again..."
    pause
    scene black with dissolve
    hide dildo9
    call SetPlayerLocation("Town2") from _call_InnRoomsescenadildo_0_SetPlayerLocation_3
    # fade in
    Leyna "Hahahahaha I feel great... I'm like new... I could go back to work right now and I wouldn't get tired of it"
    Leyna "can't wait to tell Johan about it hehehehe"
    scene black with dissolve
    call SetPlayerLocation("Town2") from _call_InnRoomsescenadildo_0_SetPlayerLocation_4
    # fade in
    pause 0.2
    Johan "Another failed attempt to enter the castle... at this rate we won't be able to visit it before going back to the city... anyway..."
    pause 0.2
    Johan "Leyna has already tried that?...I'm a little nervous ...I couldn't help but order a little extra toy for her on the internet"
    Johan "Although I guess it won't arrive for a couple of days and that's if we are lucky, this town is in the middle of nowhere"
    play sound "audio/Saint5.ogg" volume 0.9 noloop
    pause 0.2
    Johan "A message?"
    Johan "WHAT?.... it can't be... the package has already arrived... I know I put express shipping but I ordered it a couple of hours ago..."
    Johan "Is it manufactured here?... what a coincidence it would be..."
    Johan "Anyway, it says that the pick up point is at the inn, I should go to pick it up before the innkeeper opens the package to gossip"
    $ butt_plug = 1
    return

label InnRoomsMyHeadIsKillingMeSeemsLikeYesterdayWeHadTooMuchToDrinkAgainICanBarelyRememberWhatHappened_0:
    pause 0.2
    Johan "my head is killing me... seems like yesterday we had too much to drink... again... I can barely remember what happened"
    Johan "Something from a card game... and Alexa was there too... God, what a mess I am, I hope I didn't make a fool of myself"
    Johan "Although I don't remember getting here... Leyna brought me here?...."
    pause 0.32
    pause 0.2
    Johan "Speaking of Leyna... Where has she gone? I should go and look for her..."
    Johan "It's the last day of the festival, at least I will spend it with her"
    return

label InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_0:
    pause 0.36
    Leyna "Johan hasn't slept here tonight... where is he? I should look for him... or not... maybe he's at the bus stop"
    Leyna "Although I could also take a last walk around town... I have some unfinished business in and around the bar hehehe"
    return

label InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_1:
    pause 0.36
    Leyna "Johan hasn't slept here tonight.... where is he? he's probably furious about yesterday... and rightly so, what the hell was I thinking?"
    Leyna "I have to fix this any way I can... I have to find my husband, my god .... he's probably at the bus stop"
    return

