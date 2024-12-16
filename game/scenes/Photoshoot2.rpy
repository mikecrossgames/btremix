label Photoshoot2Sesionfotografica2:
    pause 0.32
    OldMan "Leyna, this is my grandson"
    pause 0.22
    pause 0.2
    Leyna "Nice to meet you (He's very tall)"
    Grandson "Hello! Excuse me I'm a little nervous, it's my first time"
    Leyna "Well, this is my second time. It's relatively easy, let yourself go"
    Grandson "Okay.. (I didn't expect her to be so pretty)"
    Leyna "By the way, why is everyone in this town so big? hahahaha"
    OldMan "Hahaha cause we eat a lot, I guess.."
    OldMan "Okay guys, go change., Leyna I've left the package where it was the last time"
    OldMan "Let's start with the first of the two, with that one you will pose alone. With the second you will pose together"
    Leyna "O-okay"
    scene black with dissolve
    $ player_location = "Photoshoot2"
    # fade in
    pause 0.2
    Leyna "Nightgown with straps... it's pretty"
    Leyna "It seems to be a little transparent ..."
    scene black with dissolve
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    show fotografo11 with dissolve
    Leyna "I'm ready"
    OldMan "You look gorgeous with that Leyna, let's do a couple of poses"
    scene black with dissolve
    show fotografo13 with dissolve
    "(A FEW MINUTES LATER)"
    $ flash_screen(wait=True)
    play sound "audio/Key.ogg" volume 0.9 noloop
    OldMan "This is enough for now"
    OldMan "You can change now so we start with the photos of both together"
    scene black with dissolve
    hide fotografo11
    hide fotografo13
    # fade in
    pause 0.2
    Leyna "This is too provocative. Who's going to wear this? ..Well I just have to do a couple of poses with the boy and we're done but.."
    Leyna "Okay Leyna, focus... let's get this over with"
    scene black with dissolve
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    show fotografo14 with dissolve
    Leyna "Are you sure this is the correct garment?"
    OldMan "Yeah pretty sure..."
    $ flash_screen(wait=True)
    play sound "audio/Key.ogg" volume 0.9 noloop
    OldMan "Come on Leyna, let yourself go a little, you look very rigid"
    Leyna "Y-yeah"
    scene fotografo15
    Leyna "Like this?"
    OldMan "There you go. That's the stuff"
    $ flash_screen(wait=True)
    play sound "audio/Key.ogg" volume 0.9 noloop
    Grandson "(Wow! I've never seen a naked woman in person I'm getting a little hard, I've to hide)"
    OldMan "Now smile a little Leyna, you are much more beautiful when you smile"
    pause
    scene fotografo16
    Leyna "That's okay?"
    OldMan "Perfect!"
    $ flash_screen(wait=True)
    play sound "audio/Key.ogg" volume 0.9 noloop
    OldMan "Now let's start with the both together"
    OldMan "Come on boy! Don't be shy"
    scene fotografo17
    OldMan "Well ... I guess that's fine ..."
    $ flash_screen(wait=True)
    play sound "audio/Key.ogg" volume 0.9 noloop
    OldMan "I need more movement guys!"
    Grandson "M-more movement?"
    OldMan "Yeah! And passion!"
    Leyna "(Passion?...)"
    Grandson "O-OKAY!"
    Leyna "(!!!)"
    scene fotografo18
    play sound "audio/Jump1.ogg" volume 0.9 noloop
    play music "audio/Dungeon3.ogg" loop volume 0.9
    Grandson "Th-there you go!"
    Leyna "AAAaah?!"
    OldMan "Well... (This is a bit extreme kid, but I guess it will work... and I'm enjoying some incredible views)"
    OldMan "Perfect! Relax Leyna, I will cut out the... delicate parts"
    Grandson "De-delicate parts?"
    OldMan "Some zoom and..."
    scene fotografo19
    OldMan "Yeah great!"
    $ flash_screen(wait=True)
    play sound "audio/Key.ogg" volume 0.9 noloop
    Leyna "What it's going on? I feel something in my..."
    Grandson "(Shit, it's going out! With this loincloth shit it's impossible to keep it inside)"
    pause
    scene fotografo20
    Leyna "Your dick is out!"
    Grandson "I-Im sorry I couldn't avoid it"
    OldMan "Don't worry, it's natural! You are 18 years old, I wish I had that ... energy"
    OldMan "But this is fine, the magazine has asked me for some raunchy photos, put the girl down"
    Grandson "Okay"
    scene fotografo21
    OldMan "Stay in that position"
    $ flash_screen(wait=True)
    play sound "audio/Key.ogg" volume 0.9 noloop
    Grandson "I'm sorry Leyna..."
    Leyna "I-It's... Okay"
    Leyna "(I'm getting wet...) Are many photos left to finish?"
    OldMan "No no, just a couple more and that's it"
    OldMan "Okay kid, pick her up again, and Leyna I know this is a little weird but I need you to smile"
    Leyna "Right..."
    scene fotografo23
    OldMan "Great! Stay still"
    $ flash_screen(wait=True)
    play sound "audio/Key.ogg" volume 0.9 noloop
    Leyna "(I feel horny... I've to finish this right now)"
    Grandson "Are you okay?"
    Leyna "Yeah, I'm alright don't worry..."
    OldMan "One last picture and that's it, Leyna get on your knees"
    Leyna "(...)"
    pause
    scene fotografo24
    OldMan "Nice!"
    $ flash_screen(wait=True)
    play sound "audio/Key.ogg" volume 0.9 noloop
    OldMan "Good work both of you!"
    Grandson "Thanks grandpa! It was a lot of fun in the end"
    OldMan "Hahaha yeah! I'm looking forward to work more with you two!"
    Leyna "Yeah... Well I better leave now"
    OldMan "Right! I will notify you when we have more work"
    Leyna "Hmm..."
    scene black with dissolve
    hide fotografo24
    stop music fadeout 1
    $ player_location = "Town"
    # fade in
    pause 0.26
    show plano_mujer_timida:
        xsize 1600
        ysize 900
    Leyna "..."
    hide plano_mujer_timida
    "(+3 CORRUPTION)"
    $ set_switch("second_photo_session", True)
    $ corruption = corruption + 3
    return

