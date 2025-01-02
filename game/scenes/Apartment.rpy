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
    scene black with dissolve
    call SetPlayerLocation("TownEntrance") from _call_ApartmentORDENADOR_SetPlayerLocation
    if switch("netorase"):
        show netorase4 with dissolve
        Johan ".... (god... I can't sleep... this opportunity is huge, it might be the beginning of something great... if I get promoted in the magazine because of this...)"
        Johan "(I need to distract myself with something... I'm going to the computer... I have to be careful not to wake Leyna...)"
        scene black with dissolve
        show netorase5 with dissolve
        Johan "I've been looking at pictures of the village for too long now, I'm getting obsessed with this... I need to let off some steam..."
        Johan "Now that Leyna is asleep I could... yeah, why not? I'm going to jerk off...."
        Johan "Let's see what's on Erotube..."
        scene netorase6
        Johan "!!!!"
        Johan "Oh, I've always liked this actress... I don't know why but she reminds me of Leyna... although I feel a little weird thinking about that"
        Johan "Let's see what the new video is like..."
        scene black with dissolve
        show netorase9 with dissolve
        Husband "H-how could you do this to me?!"
        Wife "I'm sorry! but it feels soooo good! these two huge cocks penetrating me... they're not small as yours..."
        Thug "That's right, bitch! Did you hear right, asshole? Your wife is enjoying it! So shut up and enjoy the show!"
        "Thug 2: Exactly, you have permission to jerk off looking at it if you want hahahaha"
        "Marido: My God..."
        Johan "!!!! Fuck, this is... horrible..."
        Johan "I feel like an emptiness in my stomach... I've never seen porn like this... do people like this?"
        Johan "I... I... I fucking need to jerk off"
        Johan "I haven't felt like this since I was a teenager... this nervousness... this is .... this is great!"
        Johan "If... If that was Leyna... god... oh!"
        $ flash_screen(wait=True)
        $ flash_screen(wait=True)
        scene netorase8
        Johan "Shit... I haven't lasted at all..."
        Johan "If Leyna were in that position... I can't stop thinking about it..."
        Johan "I must go to bed, tomorrow we have to get up early to go to town ...."
        scene black with dissolve
        hide netorase8
    # fade in
    return

