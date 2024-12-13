label InnNightSleep:
    pause 0.26
    Johan "I'm exhausted, what a day. Let's go to sleep, shall we?"
    Leyna "Yes, I'm also... exhausted"
    scene black with dissolve
    $ show_picture(1, "pantallanegro", scale=(110, 110), width=816, height=600)
    hide black with dissolve
    "They are both asleep, but Leyna is tossing and turning. She seems to be dreaming something intense"
    if switch("massage_masturbation"):
        $ show_picture(2, "masage6")
        Leyna "Here again?. I thought we had gone to the inn"
        Leyna "I feel so... warm"
        pause
        $ show_picture(3, "masage8")
        Leyna "yes, right there... that's where I have all the tension (I feel like I'm melting, I just want him to keep touching me more and more)"
        pause
        $ show_picture(4, "masage10")
        Leyna "(if I wasn't married...) hmmmm"
        pause
        $ show_picture(5, "masage11")
        Leyna "(Just thinking about it, I find it hard to control myself...)"
        Leyna "(I need to alleviate this feeling, before it gets out of control, for sure he doesn't realize)"
        pause
        $ show_picture(6, "masagefruta1")
        Leyna "Hmmm oh my god..."
        Leyna "(It will only take a second... all these days, with all the villagers looking at me... wanting me...)"
        Leyna "Oh?"
        pause
        $ show_picture(7, "masagefruta3")
        Leyna "(He... is rubbing me with his ...?"
        pause
        $ show_picture(8, "masagefruta4")
        Leyna "(it feels so good... I can't stop now) Ple-please..."
        Leyna "Do it please... Fuck me"
        pause
        $ show_picture(9, "masagefruta7")
        Villager "Do you want it? Do you want me to fuck you right here?"
        Leyna "Ahh... YES PLEASE"
        Villager "As you wish"
        pause
        $ show_picture(10, "masagefruta8")
        Leyna "FUUUUCK!!! OH MY GOD!!"
        Villager "oh wow, this pussy is amazing!!"
        pause
        $ show_picture(11, "masagefruta9")
        play music "audio/audio follar.ogg" loop volume 0.9
        Leyna "OOOH YEAH! JOHAN DOESN'T GET THERE! FUCK ME HARDER!"
        Villager "I'M GONNA CUM!"
        Leyna "WAIT!"
        pause
        stop music fadeout 1
    if switch("massage_sex"):
        $ show_picture(8, "masagefruta4")
        Leyna "(Why am I here again? I didn't want to come back in... what I did wasn't right...)"
        Leyna "(He is... again, and I can't control myself)"
        pause
        $ show_picture(9, "masagefruta7")
        Leyna "(But I... am in love with Johan... But this man is so... great)"
        Leyna "Please... stop, i love my husband"
        Villager "Your body says otherwise"
        Leyna "I..."
        pause
        $ show_picture(10, "masagefruta8")
        Villager "Come here I will make you feel like never before"
        Leyna "(I can't take it anymore, I'm too horny...)"
        Leyna "Fuck... Fuck me"
        pause
        $ show_picture(11, "masagefruta9")
        play music "audio/audio follar.ogg" loop volume 0.9
        Villager "Your pussy feels amazing! It's so tight!"
        Leyna "FUCK ME! OH MY GOD! I'M MELTING"
        Villager "I knew you were a whore from the moment you walked in"
        Leyna "YES! YES! YES!"
        pause
        $ show_picture(12, "sue_oleyna1")
        Johan "Leyna? Wh---what is this!!!???"
        stop music fadeout 1
        pause
        $ show_picture(13, "sue_oleyna2")
        Johan "WHAT THE HELL IS THIS? HOW COULD YOU DO THIS TO ME, LEYNA?"
        Leyna "JOHAN?"
        pause
        $ show_picture(14, "sue_oleyna3")
        Leyna "No Johan I'm sorry! Don't leave, wait..."
        pause
        $ show_picture(15, "sue_oleyna4")
        Leyna "What have I done? Why did all this have to happen?"
        Villager "Well... shall we continue?..."
        pause
    $ show_picture(16, "pantallanegro", scale=(110, 110), width=816, height=600)
    Leyna "AH! It was a dream?..."
    Leyna "damn massage, it's going to haunt me for all vacations"
    Leyna "Johan can't notice anything strange... it won't happen again"
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
    $ set_switch("leyna_dream_end", True)
    # TransferPlayer: "Town2"
    hide black with dissolve
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
    hide black with dissolve
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
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    Leyna "Nervous? No, I'm fine... But let's spend the day together tomorrow, okay?"
    Johan "Of course, we'll go to the festival site to see if they can let us in"
    $ erase_picture(1)
    $ show_transparent(1, "plano_mujer_sonrisa", width=1600, height=900)
    Leyna "Great"
    $ erase_picture(1)
    scene black with dissolve
    # TransferPlayer: "InnRooms"
    hide black with dissolve
    $ tint_screen((0, 0, 0, 0), 60, True)
    "THE NEXT MORNING"
    "You can choose between exploring the town by day or by night. Just go to bed and choose"
    $ set_switch("third_day", True)
    pause 0.24
    $ set_switch("leyna_alone", False)
    return

