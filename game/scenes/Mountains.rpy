label MountainsWowThisPlaceIsBeautiful_0:
    pause 0.34
    $ set_switch("fruit_event", True)
    Leyna "Wow! This place is beautiful"
    Worker "Hahaha, has its charm, right? Here are the fruits that I commented to you, I've already taken some"
    Worker "Do you want to try one? It will cheer you up for the rest of the day!"
    "WARNING! Consuming this fruit can cause certain '' side effects ''. Some scenes will be different if you try the fruit!"
    menu:
        "Take the fruit":
            Johan "There's no problem for me! What do you think, Leyna?"
            Leyna "Of course! No problem"
            Worker "Great, let's get back now, we're late!"
            Johan "Okay"
            $ set_switch("ate_the_fruit", True)
        "Don't take it":
            $ set_switch("ate_the_fruit", False)
            Leyna "I don't know..."
            Worker "Hey! Don't worry, it's up to you"
            Leyna "I prefer not to take it"
            Worker "Great, let's get back now, we're late!"
    call SetPlayerLocation("Festival") from _call_MountainsEV002_0_SetPlayerLocation
    return

label MountainsYouWonANewObject_0:
    play sound "audio/Recovery.ogg" volume 0.9 noloop
    $ item_flowers = True
    "(YOU WON A NEW OBJECT)"
    $ leyna_work = 5
    return

label MountainsYouWonANewObject_v2_0:
    play sound "audio/Recovery.ogg" volume 0.9 noloop
    $ item_flowers = True
    "(YOU WON A NEW OBJECT)"
    $ leyna_work = 6
    return

label MountainsYouWonANewObject_v3_0:
    play sound "audio/Recovery.ogg" volume 0.9 noloop
    $ item_flowers = True
    "(YOU WON A NEW OBJECT)"
    $ leyna_work = 7
    return

label MountainsYouWonANewObject_v4_0:
    play sound "audio/Recovery.ogg" volume 0.9 noloop
    $ item_flowers = True
    "(YOU WON A NEW OBJECT)"
    $ leyna_work = 8
    Leyna "Well, I already have all the flowers... I should go the hotsprings to start the job as soon as possible"
    scene black with dissolve
    call SetPlayerLocation("Path") from _call_MountainsEV006_0_SetPlayerLocation
    # fade in
    return

