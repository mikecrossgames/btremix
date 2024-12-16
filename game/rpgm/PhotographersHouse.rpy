label PhotographersHousesesionfotografica1:
    pause 0.32
    pause 0.22
    OldMan "Alright, let's start. Clothes are in a package on top of my bed, you should put on the swimsuit in the first place..."
    Leyna "Great!"
    pause 0.22
    # TransferPlayer: "PhotographersHouse"
    pause 0.26
    pause 0.6
    show expresion_ilusion_mujer:
        xsize 1600
        ysize 900
    Leyna "This swimsuit is beautiful!"
    Leyna "I should change now ..."
    scene black with dissolve
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    hide expresion_ilusion_mujer
    # TransferPlayer: "PhotographersHouse"
    # fade in
    pause 0.36
    pause 0.6
    scene fotografo1
    Leyna "I'm ready..."
    OldMan "Wow! Great, let's start improvising a bit, pose freely for now"
    pause
    scene fotografo2
    Leyna "Like this?..."
    OldMan "Yeah! That's perfect"
    $ flash_screen([255,255,255,170], 60, True)
    play sound "audio/Switch2.ogg" volume 0.9 noloop
    OldMan "Okay, let's try a different one"
    scene fotografo3
    OldMan "Great!"
    $ flash_screen([255,255,255,170], 60, True)
    play sound "audio/Switch2.ogg" volume 0.9 noloop
    OldMan "I think with this swimsuit we already have enough, you can already change with the lingerie that is in the second package..."
    Leyna "Great! ( This is fun! )"
    scene black with dissolve
    hide fotografo1
    hide fotografo2
    hide fotografo3
    # TransferPlayer: "PhotographersHouse"
    # fade in
    pause 0.6
    Leyna "Is this..? It's a little ... revealing, I don't know if I should ..."
    OldMan "Is there any problem?"
    Leyna "Oh  (come on Leyna, it's just a photo shoot ...) No, any problem at all..."
    # TransferPlayer: "PhotographersHouse"
    pause 0.36
    scene fotografo4
    Leyna "Isn't it too provocative?..."
    OldMan "Oh no! Not at all. You look stunning with that lingerie"
    Leyna "Thank you..."
    scene fotografo5
    OldMan "(Damn, I can see everything!)"
    pause
    hide fotografo5
    OldMan "Okay precious, pose a little for me, you look very sexy, you can do this!"
    Leyna "Hahahaha O-okay..."
    scene fotografo6
    Leyna "Like this?..."
    OldMan "Yeah perfect!"
    $ flash_screen([255,255,255,170], 60, True)
    play sound "audio/Switch2.ogg" volume 0.9 noloop
    OldMan "Great, next pose"
    scene fotografo7
    OldMan "Wonderful ( She's gaining confidence.. )"
    $ flash_screen([255,255,255,170], 60, True)
    play sound "audio/Switch2.ogg" volume 0.9 noloop
    OldMan "Now let's try something sexier..."
    Leyna "Okay..."
    pause
    scene fotografo8
    OldMan "Great! That's perfect!"
    $ flash_screen([255,255,255,170], 60, True)
    play sound "audio/Switch2.ogg" volume 0.9 noloop
    OldMan "You're doing a great job!"
    OldMan "One last pic and we're done for now"
    Leyna "Nice!"
    pause
    scene fotografo10
    OldMan "Yeah that's perfect!"
    $ flash_screen([255,255,255,170], 60, True)
    play sound "audio/Switch2.ogg" volume 0.9 noloop
    OldMan "We're done, you can change now"
    scene black with dissolve
    hide fotografo4
    hide fotografo6
    hide fotografo7
    hide fotografo8
    hide fotografo10
    # TransferPlayer: "PhotographersHouse"
    # fade in
    pause 0.24
    pause 0.22
    OldMan "The photos have turned out great. If you want you can come back later and do another photoshoot"
    Leyna "I would love that, it was really fun!"
    OldMan "Great, see you later then..."
    # TransferPlayer: "Town"
    pause 0.24
    $ set_switch("first_photo_session", True)
    return

