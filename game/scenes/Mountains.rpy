label MountainsWowThisPlaceIsBeautiful_0(menu_choice = None):
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
    $ player_location = "Festival"
    return

