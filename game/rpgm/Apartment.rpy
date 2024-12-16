label ApartmentNPCMUJER_0:
    Johan "Hi cutie"
    Leyna "Good morning. Check the email, I heard a notification"
    $ set_switch("introduction", True)
    return

label ApartmentORDENADOR:
    "You have a new message !"
    Johan "oh this is perfect!"
    pause 0.30
    Leyna "What is it?"
    Johan "Honey, I think this is a good idea for the article."
    show expresion_neutral_mujer:
        xsize 1600
        ysize 900
    "It's a small town lost in the mountains, very traditional, with ancient festivities that take place in the summer"
    "We could go and make an article about it."
    hide expresion_neutral_mujer
    show expresion_ilusion_mujer:
        xsize 1600
        ysize 900
    Leyna "Great! We could enjoy and relax a little, it's been a long time since we took a vacation."
    hide expresion_ilusion_mujer
    pause 0.22
    Johan "Yeah, they have hot springs, a beautiful river and they all seem very rustic and friendly"
    "We'll have a great time while we work"
    Leyna "It seems that the food is great, country food, I can't wait"
    Johan "Well then, it's decided! Pack your bags while I book a room in the village hostel."
    pause 0.22
    pause 0.54
    stop music fadeout 1
    $ set_switch("introduction", False)
    # TransferPlayer: "TownEntrance"
    return

