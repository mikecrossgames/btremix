label Casinohombredelasuerte:
    pause 0.2
    OldMan "Welcome!"
    OldMan "Please take a ticket from the machine at your right, we'll start the draw right away"
    Johan "Okay"
    pause 0.26
    play sound "audio/Computer.ogg" volume 0.9 noloop
    pause 0.22
    Johan "Here you have your ticket Leyna"
    Leyna "Thanks"
    pause 0.32
    OldMan "Ok, we'll wait a little longer for the rest to arrive and we'll do the lottery"
    OldWoman "The rest? Everyone is out having a good time and drinking like crazy, nobody cares about this lottery anymore"
    OldMan "But..."
    OldWoman "No, no buts! Let's get this over with"
    OldMan "Hmmm ... okay, well.. let the lottery begin!"
    pause 0.22
    play sound "audio/Computer.ogg" volume 0.9 noloop
    pause 0.6
    pause 0.2
    pause 0.22
    OldMan "Okay ... the lucky person this year is ..."
    OldMan "The number 12!"
    ".... ...... ........ ............."
    Leyna "... Th-that's me"
    pause 0.22
    pause 0.22
    pause 0.22
    pause 0.22
    pause 0.22
    pause 0.22
    pause 0.22
    pause 0.22
    pause 0.22
    pause 0.22
    pause 0.22
    pause 0.2
    OldWoman "Hohoho..."
    OldMan "Interesting ... a tourist as a lucky person ... Well, you know how this is going guys"
    pause 0.24
    scene suerte1
    Worker "Well, I already have a year of good luck"
    Leyna "Oh my ... Just this? I was scared..."
    scene suerte2
    Worker "Well, people get a little anxious sometimes.. but that happened more years ago, now we are less people and they will take it more calmly"
    Johan "Good to know, I don't feel very comfortable with all these people touching my wife"
    Worker "Relax, it's just a tradition"
    Johan "(Another tradition huh?) Yeah...."
    scene suerte3
    Villager "Hey! A year of good luck to me"
    Leyna "...!"
    scene suerte4
    Villager2 "And for me!"
    "Villager3: Don't leave me behind, I want too!"
    scene suerte5
    Leyna "Wa-wait"
    scene suerte6
    Johan "Hey easy going guys!"
    "Villager4: Luck is running out!"
    scene suerte7
    Leyna "He-hey..."
    scene suerte9
    Leyna "(They're touching me in ...)"
    pause
    scene suerte8
    Leyna "Be careful guys ..."
    pause
    if switch("ate_the_fruit"):
        scene suerte10
        Leyna "(This ... this is turning me on a bit ... I can't let Johan know, I have to pretend)"
    "Villager5: Let's see if I win the lottery this year!"
    Johan "I think that's enough"
    Villager "... Yeah yeah.... sorry dude"
    pause
    scene suerte11
    Johan "Are you okay?"
    Leyna "Yes, I'm okay"
    if switch("ate_the_fruit"):
        Leyna "(Definitely, the fruit that I've eaten before is affecting...)"
    scene black with dissolve
    hide suerte11
    pause 0.22
    pause 0.22
    pause 0.22
    pause 0.22
    pause 0.22
    pause 0.22
    pause 0.22
    pause 0.22
    pause 0.22
    pause 0.22
    # fade in
    OldMan "Well guys! You have to spread the word about the lucky girl!"
    pause 0.2
    Villager "That's done boss!"
    Johan "Hey..."
    OldMan "(How lucky ... this year the lucky person is a beautiful tourist ... sure next year there's much more interest in coming to the lot)"
    Leyna "Johan ... Let's take a walk around the festival to see what can we do"
    Johan "Sure..."
    $ set_switch("lucky_person", True)
    call SetPlayerLocation("Festival") from _call_Casinohombredelasuerte_SetPlayerLocation
    pause 0.24
    if switch("ate_the_fruit"):
        $ corruption = corruption + 2
    if not switch("ate_the_fruit"):
        $ corruption = corruption + 1
    return

