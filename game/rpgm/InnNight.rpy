label InnNightSleep:
    pause 0.26
    Johan "I'm exhausted, what a day. Let's go to sleep, shall we?"
    Leyna "Yes, I'm also... exhausted"
    scene black with dissolve
    show pantallanegro with dissolve:
        xsize 898
        ysize 660
    "They are both asleep, but Leyna is tossing and turning. She seems to be dreaming something intense"
    if switch("massage_masturbation"):
        scene masage6
        Leyna "Here again?. I thought we had gone to the inn"
        Leyna "I feel so... warm"
        pause
        scene masage8
        Leyna "yes, right there... that's where I have all the tension (I feel like I'm melting, I just want him to keep touching me more and more)"
        pause
        scene masage10
        Leyna "(if I wasn't married...) hmmmm"
        pause
        scene masage11
        Leyna "(Just thinking about it, I find it hard to control myself...)"
        Leyna "(I need to alleviate this feeling, before it gets out of control, for sure he doesn't realize)"
        pause
        scene masagefruta1
        Leyna "Hmmm oh my god..."
        Leyna "(It will only take a second... all these days, with all the villagers looking at me... wanting me...)"
        Leyna "Oh?"
        pause
        scene masagefruta3
        Leyna "(He... is rubbing me with his ...?"
        pause
        scene masagefruta4
        Leyna "(it feels so good... I can't stop now) Ple-please..."
        Leyna "Do it please... Fuck me"
        pause
        scene masagefruta7
        Villager "Do you want it? Do you want me to fuck you right here?"
        Leyna "Ahh... YES PLEASE"
        Villager "As you wish"
        pause
        scene masagefruta8
        Leyna "FUUUUCK!!! OH MY GOD!!"
        Villager "oh wow, this pussy is amazing!!"
        pause
        scene masagefruta9
        play music "audio/audio follar.ogg" loop volume 0.9
        Leyna "OOOH YEAH! JOHAN DOESN'T GET THERE! FUCK ME HARDER!"
        Villager "I'M GONNA CUM!"
        Leyna "WAIT!"
        pause
        stop music fadeout 1
    if switch("massage_sex"):
        scene masagefruta4
        Leyna "(Why am I here again? I didn't want to come back in... what I did wasn't right...)"
        Leyna "(He is... again, and I can't control myself)"
        pause
        scene masagefruta7
        Leyna "(But I... am in love with Johan... But this man is so... great)"
        Leyna "Please... stop, i love my husband"
        Villager "Your body says otherwise"
        Leyna "I..."
        pause
        scene masagefruta8
        Villager "Come here I will make you feel like never before"
        Leyna "(I can't take it anymore, I'm too horny...)"
        Leyna "Fuck... Fuck me"
        pause
        scene masagefruta9
        play music "audio/audio follar.ogg" loop volume 0.9
        Villager "Your pussy feels amazing! It's so tight!"
        Leyna "FUCK ME! OH MY GOD! I'M MELTING"
        Villager "I knew you were a whore from the moment you walked in"
        Leyna "YES! YES! YES!"
        pause
        scene sue_oleyna1
        Johan "Leyna? Wh---what is this!!!???"
        stop music fadeout 1
        pause
        scene sue_oleyna2
        Johan "WHAT THE HELL IS THIS? HOW COULD YOU DO THIS TO ME, LEYNA?"
        Leyna "JOHAN?"
        pause
        scene sue_oleyna3
        Leyna "No Johan I'm sorry! Don't leave, wait..."
        pause
        scene sue_oleyna4
        Leyna "What have I done? Why did all this have to happen?"
        Villager "Well... shall we continue?..."
        pause
    scene pantallanegro:
        xsize 898
        ysize 660
    Leyna "AH! It was a dream?..."
    Leyna "damn massage, it's going to haunt me for all vacations"
    Leyna "Johan can't notice anything strange... it won't happen again"
    scene black with dissolve
    hide pantallanegro
    hide masage6
    hide masage8
    hide masage10
    hide masage11
    hide masagefruta1
    hide masagefruta3
    hide masagefruta4
    hide masagefruta7
    hide masagefruta8
    hide masagefruta9
    hide sue_oleyna1
    hide sue_oleyna2
    hide sue_oleyna3
    hide sue_oleyna4
    hide pantallanegro
    $ set_switch("leyna_dream_end", True)
    # TransferPlayer: "Town2"
    # fade in
    pause 0.26
    pause 0.2
    Johan "Leyna, what's wrong? You look bad... you didn't sleep well?"
    Leyna "I... what? I have slept well, I'm just a little worried... vacations are taking too long, don't you think?"
    Johan "Yes, the other day I was thinking about this... I think it would be a good idea to try to find some part-time job"
    Johan "While I work on the report, to cover expenses I'm sure the merchants have some jobe for you"
    Leyna "... Yes, that would be nice (so I can occupy my mind in other things...)"
    Johan "Well, I have to go today to send some pictures, see you later"
    Leyna "Okay, I guess I'll start asking around at the grocery store"
    scene black with dissolve
    play sound "audio/Move1.ogg" volume 0.9 noloop
    # fade in
    Leyna "Well, let's go to the food store (Maybe I should talk to the photographer too... but I'm not sure I want to follow that path..)"
    $ leyna_work = 1
    return

label InnNightentradaalaposadanoche_0:
    pause 0.24
    pause 0.22
    pause 0.2
    Johan "Leyna! I was starting to worry, you took a long time to come back"
    pause 0.34
    Johan "Are you okay? You seem a little nervous.."
    show plano_mujer_sorpresa_lado:
        xsize 1600
        ysize 900
    Leyna "Nervous? No, I'm fine... But let's spend the day together tomorrow, okay?"
    Johan "Of course, we'll go to the festival site to see if they can let us in"
    hide plano_mujer_sorpresa_lado
    show plano_mujer_sonrisa:
        xsize 1600
        ysize 900
    Leyna "Great"
    hide plano_mujer_sonrisa
    scene black with dissolve
    # TransferPlayer: "InnRooms"
    # fade in
    $ tint_screen((0, 0, 0, 0), 60, True)
    "THE NEXT MORNING"
    "You can choose between exploring the town by day or by night. Just go to bed and choose"
    $ set_switch("third_day", True)
    pause 0.24
    $ set_switch("leyna_alone", False)
    return

