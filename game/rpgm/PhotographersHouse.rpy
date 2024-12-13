label PhotographersHousesesionfotografica1:
    pause 0.32
    pause 0.22
    OldMan "Alright, let's start. Clothes are in a package on top of my bed, you should put on the swimsuit in the first place..."
    Leyna "Great!"
    pause 0.22
    # TransferPlayer: "PhotographersHouse"
    pause 0.26
    pause 0.6
    $ show_transparent(1, "expresion_ilusion_mujer", width=1600, height=900)
    Leyna "This swimsuit is beautiful!"
    Leyna "I should change now ..."
    scene black with dissolve
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    $ erase_picture(1)
    # TransferPlayer: "PhotographersHouse"
    hide black with dissolve
    pause 0.36
    pause 0.6
    $ show_picture(1, "fotografo1")
    Leyna "I'm ready..."
    OldMan "Wow! Great, let's start improvising a bit, pose freely for now"
    pause
    $ show_picture(2, "fotografo2")
    Leyna "Like this?..."
    OldMan "Yeah! That's perfect"
    $ flash_screen([255,255,255,170], 60, True)
    play sound "audio/Switch2.ogg" volume 0.9 noloop
    OldMan "Okay, let's try a different one"
    $ show_picture(3, "fotografo3")
    OldMan "Great!"
    $ flash_screen([255,255,255,170], 60, True)
    play sound "audio/Switch2.ogg" volume 0.9 noloop
    OldMan "I think with this swimsuit we already have enough, you can already change with the lingerie that is in the second package..."
    Leyna "Great! ( This is fun! )"
    scene black with dissolve
    $ erase_picture(1)
    $ erase_picture(2)
    $ erase_picture(3)
    # TransferPlayer: "PhotographersHouse"
    hide black with dissolve
    pause 0.6
    Leyna "Is this..? It's a little ... revealing, I don't know if I should ..."
    OldMan "Is there any problem?"
    Leyna "Oh  (come on Leyna, it's just a photo shoot ...) No, any problem at all..."
    # TransferPlayer: "PhotographersHouse"
    pause 0.36
    $ show_picture(4, "fotografo4")
    Leyna "Isn't it too provocative?..."
    OldMan "Oh no! Not at all. You look stunning with that lingerie"
    Leyna "Thank you..."
    $ show_picture(5, "fotografo5")
    OldMan "(Damn, I can see everything!)"
    pause
    $ erase_picture(5)
    OldMan "Okay precious, pose a little for me, you look very sexy, you can do this!"
    Leyna "Hahahaha O-okay..."
    $ show_picture(6, "fotografo6")
    Leyna "Like this?..."
    OldMan "Yeah perfect!"
    $ flash_screen([255,255,255,170], 60, True)
    play sound "audio/Switch2.ogg" volume 0.9 noloop
    OldMan "Great, next pose"
    $ show_picture(7, "fotografo7")
    OldMan "Wonderful ( She's gaining confidence.. )"
    $ flash_screen([255,255,255,170], 60, True)
    play sound "audio/Switch2.ogg" volume 0.9 noloop
    OldMan "Now let's try something sexier..."
    Leyna "Okay..."
    pause
    $ show_picture(8, "fotografo8")
    OldMan "Great! That's perfect!"
    $ flash_screen([255,255,255,170], 60, True)
    play sound "audio/Switch2.ogg" volume 0.9 noloop
    OldMan "You're doing a great job!"
    OldMan "One last pic and we're done for now"
    Leyna "Nice!"
    pause
    $ show_picture(9, "fotografo10")
    OldMan "Yeah that's perfect!"
    $ flash_screen([255,255,255,170], 60, True)
    play sound "audio/Switch2.ogg" volume 0.9 noloop
    OldMan "We're done, you can change now"
    scene black with dissolve
    $ erase_picture(4)
    $ erase_picture(6)
    $ erase_picture(7)
    $ erase_picture(8)
    $ erase_picture(9)
    # TransferPlayer: "PhotographersHouse"
    hide black with dissolve
    pause 0.24
    pause 0.22
    OldMan "The photos have turned out great. If you want you can come back later and do another photoshoot"
    Leyna "I would love that, it was really fun!"
    OldMan "Great, see you later then..."
    # TransferPlayer: "Town"
    pause 0.24
    $ set_switch("first_photo_session", True)
    return

