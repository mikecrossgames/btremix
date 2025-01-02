label HotSpringshotspringseventopart2:
    pause 0.34
    pause 0.34
    Villager "Wow, I see we are not alone"
    pause 0.22
    Leyna "Aaah!? (What the hell are those guys doing here)..."
    Leyna "What?! I ... I didn't know the hot springs are mixed"
    Villager "You are not from here, of course. Yeah, they are mixed but don't worry about us, relax.. We'll keep you company!"
    Leyna "Oh... I see"
    scene black with dissolve
    show onsen2 with dissolve
    play sound "audio/Dive.ogg" volume 0.9 noloop
    Villager "So, are you travelling?"
    Leyna "( He is too close ) Yes.. I've come with my husband.."
    Villager "Oh?... And where is your husband, if I may ask?"
    Leyna "In the town hall talking to some workers and the mayor"
    Villager "Hmm, I see.. better for haha, only us enjoying your company.."
    Leyna "What?"
    Villager "Hahaha is a joke, relax woman, this place is to enjoy and have a good time"
    Leyna "Hahaha of course..."
    scene black with dissolve
    play sound "audio/Liquid.ogg" volume 0.9 noloop
    show onsen3 with dissolve
    "(A FEW MINUTES LATER...)"
    Leyna "(I'm starting to get dizzy ... but I don't want to be seen naked and I've left the towel on the bench over there)"
    Villager "Are you okay lady?"
    pause
    scene onsen5
    Leyna "The heat is affecting me, I guess"
    Villager "Yeah, you are in a very tense position. Relax or you'll pass out"
    Leyna "Do you think so? ... I suppose you are right"
    pause
    scene onsen6
    play sound "audio/Jump1.ogg" volume 0.9 noloop
    Villager "This is better, right?"
    Leyna "I guess so... thank you very much, I need to relax more, after all I'm on a kind of vacation"
    Villager "Hahaha... Well I must admit you have a great body, and breasts as I've never seen in my life"
    Leyna "Tha..thanks"
    Villager "Plus, you're nice! The usual is a woman being angry when someone says this kind of thing to her"
    Leyna "Don't worry, it's a compliment, right?"
    Villager "(She's clearly not thinking straight.. probably because of the vapours and heat)"
    Villager "( What if I..? )"
    Villager "Yes... Hey, can I touch one? As I said, I've never seen such beautiful ones"
    Leyna "... ah?"
    Villager "Yeah, I'm older and at this rate, I don't think I'll ever get married. Let me touch you a tit, I have to do it before I die"
    Villager2 "Come on dude, don't be a dirty old man.."
    Leyna "...Well... if it's such an important thing to you... it's just touching a tit"
    scene onsen7
    play sound "audio/Jump1.ogg" volume 0.9 noloop
    play music "audio/Dungeon3.ogg" loop volume 0.9
    Leyna "(!!!)"
    Villager "Wow! Thanks.. as I said, perfect. They are soft and smooth, you have an incredible body"
    Leyna "... Thanks (I'm too dizzy for this)"
    Villager2 "... Hey! If he can, me too, right? It wouldn't be fair if only one of us could"
    Leyna "Well I don't..."
    scene onsen8
    play sound "audio/Jump1.ogg" volume 0.9 noloop
    Villager2 "You're right!! They are perfect, what a feeling !!! I wish I had known you years ago to ask you to marry me Your husband is very lucky"
    Leyna "Hahaha..."
    scene onsen9
    Leyna "I think I've been here too long ... I feel dizzy.. I better get out"
    Villager "Already?! What a shame.. we are having so  much fun.."
    Leyna "Excuse me..."
    scene onsen10
    play sound "audio/Jump2.ogg" volume 0.9 noloop
    Leyna "Oh?!!"
    Villager "Seems like you're very stunned, let me help you..."
    pause
    scene onsen11
    play sound "audio/Jump2.ogg" volume 0.9 noloop
    Leyna "Oooh ... don't..."
    Villager "Relax... I will take you to the locker room and give you something cold to drink"
    Leyna "..."
    Villager "Shit, the ground is wet… uoh shit!"
    play sound "audio/Fall.ogg" volume 0.9 noloop
    scene onsen12
    play sound "audio/Blow1.ogg" volume 0.9 noloop
    $ shake_screen()
    Leyna "What... Have we fallen?"
    pause
    scene onsen13
    play sound "audio/Jump2.ogg" volume 0.9 noloop
    Leyna "(!!!)"
    Villager "Shit my back... Wait a second miss, don't move. We have hit the ground.."
    Villager "(Oooh, I have to take advantage of this situation. I'm touching her with my... damn I have to tell this to the boys)"
    Leyna "I think ... I think we can get up now, right?"
    Villager "Yes, sure.. I'm better now.. (Fuck..)"
    scene black with dissolve
    show onsen14 with dissolve
    Leyna "Sorry for the inconvenience, because of me you hit you back... I owe you a favour, if you ever need anything tell me"
    Villager "Of course, don't worry, you're going to the festival right? we'll see you there ..."
    Leyna "Yeah right..."
    scene black with dissolve
    hide onsen13
    hide onsen14
    stop music fadeout 1
    # fade in
    call SetPlayerLocation("HotSpringsExterior") from _call_HotSpringshotspringseventopart2_SetPlayerLocation
    pause 0.24
    Leyna "That has been dangerous, I can't fall asleep in that place again ... I'm still a little giddy"
    "(+2 CORRUPTION)"
    $ set_switch("hot_springs_first_visit", True)
    $ corruption = corruption + 2
    return

