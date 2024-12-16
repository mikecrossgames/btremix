label Galleryeventorio_1(menu_choice = None):
    "First accident in the river: do you want to see the scene again?"
    menu:
        "Yes":
            scene black with dissolve
            # fade in
            scene pantallanegro:
                xsize 979
                ysize 720
            Johan "So the celebration goes back thousands of years and is in honour of a very old fertility goddess..."
            "...how interesting! Great, now I'm going to take a couple of photos if you don't mind."
            Villager "Yes, of course ..."
            $ flash_screen(wait=True)
            Villager "I have an idea..."
            Johan "Yes?"
            Villager "It's just us in these photos. If you only show this in the article, people won't want to come to this town, right?"
            Johan "Well..."
            Villager "If you only see a group of ugly men posing on the camera it would be a disaster..."
            "...what these photos need is a feminine touch"
            scene black with dissolve
            # fade in
            scene rio_1:
                pos (-125, 0)
                xsize 1104
                ysize 621
            Villager "(Damn... the girl smells great)"
            scene rio_2:
                pos (-125, 0)
                xsize 1104
                ysize 621
            Johan "Maybe you could go a little closer for the photo"
            Villager "O...Of course!"
            pause
            scene rio_3:
                pos (-125, 0)
                xsize 1104
                ysize 621
            Leyna "(!!!)"
            pause
            scene rio_4:
                pos (-125, 0)
                xsize 1104
                ysize 621
            Johan "(They are too close ... well, I'm not going to bother them too much..."
            "...after all, they are doing us a favour letting us take photos of them)"
            pause
            scene rio_5:
                pos (-125, 0)
                xsize 1104
                ysize 621
            Villager "( This is my chance, but I have to do it right or I'll get caught! )"
            pause
            scene rio_6:
                pos (-125, 0)
                xsize 1104
                ysize 621
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            play music "audio/Dungeon3.ogg" loop volume 0.9
            pause
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            scene rio_7:
                pos (-125, 0)
                xsize 1104
                ysize 621
            Johan "(!!!!!!!!!)"
            Villager "(WOW DAMN! OKAY, KEEP CALM KEEP CALM)"
            pause
            scene rio_8:
                pos (-125, 0)
                xsize 1104
                ysize 621
            Leyna "Ooh?!!"
            Johan "(Shit, they are seeing everything)"
            pause
            scene rio_9:
                pos (-125, 0)
                xsize 1104
                ysize 621
            Villager "Oh boy, the towel has fallen off. Well don't worry too much, after all, this is a tradition here and we are all naked"
            pause
            scene rio_10:
                pos (-125, 0)
                xsize 1104
                ysize 621
            Leyna "(I have to put on the towel right now!)"
            Johan "( What the fuck!? They are huge )"
            pause
            scene rio_11:
                pos (-125, 0)
                xsize 1104
                ysize 621
            Villager "Sorry, but it's natural, isn't it? This kind of thing happens, and more after seeing a naked woman as beautiful as you"
            pause
            scene rio_12:
                pos (-125, 0)
                xsize 1104
                ysize 621
            play sound "audio/Jump2.ogg" volume 0.9 noloop
            Leyna "Ex...excuse me?"
            pause
            scene rio_13:
                pos (-125, 0)
                xsize 1104
                ysize 621
            Villager "You know, erections and that sort of thing."
            Leyna "Oh ... sure..."
            scene rio14:
                pos (-125, 0)
                xsize 1104
                ysize 621
            Villager "Well ... hey, don't you think it's a good artistic photo?I think in this position you could take a couple of good photos"
            menu:
                "Okey":
                    Johan "Yes ... I'll take one more photo and that's it."
                    scene rio15:
                        pos (-125, 0)
                        xsize 1104
                        ysize 621
                    Leyna "(what's going on?)"
                    Leyna "(his ... things are very close to me ... Johan is fine with this?... I think he is not even aware of what is happening...)"
                    Leyna "(I have to stop looking at... that so much. and maybe pose or something?)"
                    Johan "Okay, that's it... Thanks for your help guys"
                    Leyna "(!!!)"
                    Villager "Thank you. Come back whenever you want!"
                    Johan "(...)"
                    pause
                    scene black with dissolve
                    hide rio15
                    # fade in
                "This has gone too far":
                    Johan "No, enough guys! We are leaving..."
                    scene black with dissolve
                    # fade in
        "No":
            pass
    return

label GalleryFotografo1_1(menu_choice = None):
    "First session with the photographer"
    "Do you want to see it?"
    menu:
        "Yes":
            scene black with dissolve
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            # fade in
            scene fotografo1
            Leyna "I'm ready..."
            OldMan "Wow! Great, let's start improvising a bit, pose freely for now"
            pause
            scene fotografo2
            Leyna "Like this?..."
            OldMan "Yeah! That's perfect"
            $ flash_screen(wait=True)
            play sound "audio/Switch2.ogg" volume 0.9 noloop
            OldMan "Okay, let's try a different one"
            scene fotografo3
            OldMan "Great!"
            $ flash_screen(wait=True)
            play sound "audio/Switch2.ogg" volume 0.9 noloop
            OldMan "I think with this swimsuit we already have enough, you can already change with the lingerie that is in the second package..."
            Leyna "Great! ( This is fun! )"
            scene black with dissolve
            hide fotografo3
            show fotografo4 with dissolve
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
            $ flash_screen(wait=True)
            play sound "audio/Switch2.ogg" volume 0.9 noloop
            OldMan "Great, next pose"
            scene fotografo7
            OldMan "Wonderful ( She's gaining confidence.. )"
            $ flash_screen(wait=True)
            play sound "audio/Switch2.ogg" volume 0.9 noloop
            OldMan "Now let's try something sexier..."
            Leyna "Okay..."
            pause
            scene fotografo8
            OldMan "Great! That's perfect!"
            $ flash_screen(wait=True)
            play sound "audio/Switch2.ogg" volume 0.9 noloop
            OldMan "You're doing a great job!"
            OldMan "One last pic and we're done for now"
            Leyna "Nice!"
            pause
            scene fotografo10
            OldMan "Yeah that's perfect!"
            $ flash_screen(wait=True)
            play sound "audio/Switch2.ogg" volume 0.9 noloop
            OldMan "We're done, you can change now"
            scene black with dissolve
            hide fotografo10
            # fade in
        "No":
            pass
    return

label Galleryonsen1_1(menu_choice = None):
    "Hotsprings 1, Do you want to see it?"
    menu:
        "Yes":
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
        "No":
            pass
    return

label GallerySecondSessionWithThePhotographer_1(menu_choice = None):
    "Second session with the photographer"
    "Do you want to see it?"
    menu:
        "Yes":
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
            # fade in
        "No":
            pass
    return

label GalleryBarSceneGambling_1(menu_choice = None):
    "Bar scene, gambling"
    "Do you want to see it?"
    menu:
        "Yes":
            scene black with dissolve
            show bar2 with dissolve:
                pos (-125, 0)
                xsize 1104
                ysize 621
            Leyna "Hey! I'm getting pretty good at this!"
            Villager "(Too good I would say ... at this rate we won't see anything)"
            Villager "Hahahahaha, Don't get too cocky, girl..."
            scene black with dissolve
            hide bar2
            show bar3 with dissolve:
                pos (-125, 0)
                xsize 1104
                ysize 621
            play sound "audio/Miss.ogg" volume 0.9 noloop
            "(A FEW MINUTES LATER ...)"
            Leyna "What were you saying?"
            Villager "(What the hell is going on? Why is she so good at this?)"
            Villager2 "(Aaah, all hope is lost...)"
            Leyna "Hahahahaha it seems like I've won guys, if you excuse me I'm going to go to the Inn..."
            Villager "Wait wait! After this humiliation, I need one last chance. You have removed us all our clothes already"
            "... so the bet will be different, let's see ... Yes! I have 300 dollars on me. I'll bet all in the next round!"
            scene bar4:
                pos (-125, 0)
                xsize 1104
                ysize 621
            Leyna "300!!!?..."
            Leyna "(That's a lot of money to earn in such a short time ... and Johan and I need it ... but)"
            Leyna "Sorry guys but I don't have that much money on me. I can't match the bet"
            Villager "Well ... 300 is a lot, right, maybe you could do something of equal value, right?"
            Leyna "Equal value?..."
            Villager "Yes ... if I win you have to make me ejaculate. There are almost no women in this town and I am quite in need of female contact"
            Leyna "Ejaculate?!!"
            Leyna "(I can't do that but... I've won all the rounds so far and.. 300 could come in handy to pay for travel expenses)"
            menu:
                "Okey I'll do it":
                    Leyna "Okey ... Okey, let's do it"
                    Villager "Nice!"
                    Villager "(It's time to use my last trick)"
                    scene black with dissolve
                    hide bar4
                    show bar5 with dissolve:
                        pos (-125, 0)
                        xsize 1104
                        ysize 621
                    play sound "audio/Attack2.ogg" volume 0.9 noloop
                    Villager "YEAH!! I WON!!"
                    Leyna "What..."
                    Leyna "(Oh no no no..)"
                    Villager "It seems luck is no longer on your side"
                    Villager "(HELL YES!! I CAN'T BELIEVE THIS IS HAPPENING)"
                    Villager2 "(He did it! The absolute madman!!)"
                    Villager "Very good... well ... you can do it as you want, As long as I cum there is no problem"
                    scene black with dissolve
                    hide bar5
                    show bar6 with dissolve:
                        pos (-125, 0)
                        xsize 1104
                        ysize 621
                    play music "audio/Dungeon3.ogg" loop volume 0.9
                    Leyna "Hmmm I see ... but ... I'm married and ..."
                    Villager "Come on, you just have to make me come, it will take just a minute, a bet's a bet"
                    Villager "A woman hasn't touched me for centuries, I will not last at all!"
                    pause
                    scene bar7:
                        pos (-125, 0)
                        xsize 1104
                        ysize 621
                    Leyna "(It's so close...)"
                    image paja_webm = Movie(play="movies/paja.webm", loop=True, size=(816, 459), ypos=83)
                    scene paja_webm
                    pause
                    scene bar8:
                        pos (-125, 0)
                        xsize 1104
                        ysize 621
                    Leyna "(Why is this taking so long?...)"
                    image paja_webm = Movie(play="movies/paja.webm", loop=True, size=(816, 459), ypos=83)
                    scene paja_webm
                    pause
                    Villager "(Endure... ENDURE!!! It's been soo long)"
                    Villager "(I don't know when next time will be, I have to enjoy it as much as possible)"
                    scene bar9:
                        pos (-125, 0)
                        xsize 1104
                        ysize 621
                    Villager "You know... If you do it this way you won't get it. At this rate, we can be here all afternoon"
                    pause
                    scene bar10:
                        pos (-125, 0)
                        xsize 1104
                        ysize 621
                    Leyna "(Maybe... maybe if I use my mouth?)"
                    pause
                    play sound "audio/Poison.ogg" volume 0.9 noloop
                    scene bar11:
                        pos (-125, 0)
                        xsize 1104
                        ysize 621
                    Villager "(YES! But... I can't hold it anymore)"
                    pause
                    play sound "audio/Poison.ogg" volume 0.9 noloop
                    scene bar12:
                        pos (-125, 0)
                        xsize 1104
                        ysize 621
                    Villager2 "(Oh she's really going to do it!)"
                    pause
                    play sound "audio/Poison.ogg" volume 0.9 noloop
                    scene bar13:
                        pos (-125, 0)
                        xsize 1104
                        ysize 621
                    Villager "Almost there..."
                    Leyna "hmm?..."
                    Villager "OOOooohh!!!"
                    Leyna "(!!!)"
                    $ flash_screen(wait=True)
                    play sound "audio/Poison.ogg" volume 0.9 noloop
                    $ flash_screen(wait=True)
                    scene black with dissolve
                    hide bar13
                    show bar14 with dissolve:
                        pos (-125, 0)
                        xsize 1104
                        ysize 621
                    Leyna "AAaah?!!!"
                    Villager "Sorry. It's been so long since a woman touched me that I couldn't help it"
                    Leyna "It's.. it's all over my face ..."
                    Villager "Relax, I bring you a rag to clean yourself"
                    Leyna "Than... thanks. I have to go now or I will pass out.."
                    "It has been..................... fun? Bye"
                    scene black with dissolve
                    hide bar14
                    # fade in
                    show plano_mujer_timida:
                        xsize 1600
                        ysize 900
                    Leyna "..."
                    "What the hell have I done?... I can't let Johan find out about this ..."
                    hide plano_mujer_timida
                "No, this is to much":
                    Leyna "Sorry guys, but I'm a married woman and I can't do this kind of thing..."
                    Villager "I see, don't worry, have a good time at the festival."
                    Villager "(I have time to seduce this girl little by little.. there's no reason to rush)"
                    scene black with dissolve
                    # fade in
        "No":
            pass
    return

label GalleryBarSceneGambling_2(menu_choice = None):
    "Bar scene, gambling"
    "Do you want to see it?"
    menu:
        "Yes":
            scene black with dissolve
            show bar2 with dissolve:
                pos (-125, 0)
                xsize 1104
                ysize 621
            Leyna "Hey! I'm getting pretty good at this!"
            Villager "(Too good I would say ... at this rate we won't see anything)"
            Villager "Hahahahaha, Don't get too cocky, girl..."
            scene black with dissolve
            hide bar2
            show bar3 with dissolve:
                pos (-125, 0)
                xsize 1104
                ysize 621
            play sound "audio/Miss.ogg" volume 0.9 noloop
            "(A FEW MINUTES LATER ...)"
            Leyna "What were you saying?"
            Villager "(What the hell is going on? Why is she so good at this?)"
            Villager2 "(Aaah, all hope is lost...)"
            Leyna "Hahahahaha it seems like I've won guys, if you excuse me I'm going to go to the Inn..."
            Villager "Wait wait! After this humiliation, I need one last chance. You have removed us all our clothes already"
            "... so the bet will be different, let's see ... Yes! I have 300 dollars on me. I'll bet all in the next round!"
            scene bar4:
                pos (-125, 0)
                xsize 1104
                ysize 621
            Leyna "300!!!?..."
            Leyna "(That's a lot of money to earn in such a short time ... and Johan and I need it ... but)"
            Leyna "Sorry guys but I don't have that much money on me. I can't match the bet"
            Villager "Well ... 300 is a lot, right, maybe you could do something of equal value, right?"
            Leyna "Equal value?..."
            Villager "Yes ... if I win you have to make me ejaculate. There are almost no women in this town and I am quite in need of female contact"
            Leyna "Ejaculate?!!"
            Leyna "(I can't do that but... I've won all the rounds so far and.. 300 could come in handy to pay for travel expenses)"
            menu:
                "Okey I'll do it":
                    Leyna "Okey ... Okey, let's do it"
                    Villager "Nice!"
                    Villager "(It's time to use my last trick)"
                    scene black with dissolve
                    hide bar4
                    show bar5 with dissolve:
                        pos (-125, 0)
                        xsize 1104
                        ysize 621
                    play sound "audio/Attack2.ogg" volume 0.9 noloop
                    Villager "YEAH!! I WON!!"
                    Leyna "What..."
                    Leyna "(Oh no no no..)"
                    Villager "It seems luck is no longer on your side"
                    Villager "(HELL YES!! I CAN'T BELIEVE THIS IS HAPPENING)"
                    Villager2 "(He did it! The absolute madman!!)"
                    Villager "Very good... well ... you can do it as you want, As long as I cum there is no problem"
                    scene black with dissolve
                    hide bar5
                    show bar6 with dissolve:
                        pos (-125, 0)
                        xsize 1104
                        ysize 621
                    play music "audio/Dungeon3.ogg" loop volume 0.9
                    Leyna "Hmmm I see ... but ... I'm married and ..."
                    Villager "Come on, you just have to make me come, it will take just a minute, a bet's a bet"
                    Villager "A woman hasn't touched me for centuries, I will not last at all!"
                    pause
                    scene bar7:
                        pos (-125, 0)
                        xsize 1104
                        ysize 621
                    Leyna "(It's so close...)"
                    image paja_webm = Movie(play="movies/paja.webm", loop=True, size=(816, 459), ypos=83)
                    scene paja_webm
                    pause
                    scene bar8:
                        pos (-125, 0)
                        xsize 1104
                        ysize 621
                    Leyna "(Why is this taking so long?...)"
                    image paja_webm = Movie(play="movies/paja.webm", loop=True, size=(816, 459), ypos=83)
                    scene paja_webm
                    pause
                    Villager "(Endure... ENDURE!!! It's been soo long)"
                    Villager "(I don't know when next time will be, I have to enjoy it as much as possible)"
                    scene bar9:
                        pos (-125, 0)
                        xsize 1104
                        ysize 621
                    Villager "You know... If you do it this way you won't get it. At this rate, we can be here all afternoon"
                    pause
                    scene bar10:
                        pos (-125, 0)
                        xsize 1104
                        ysize 621
                    Leyna "(Maybe... maybe if I use my mouth?)"
                    pause
                    play sound "audio/Poison.ogg" volume 0.9 noloop
                    scene bar11:
                        pos (-125, 0)
                        xsize 1104
                        ysize 621
                    Villager "(YES! But... I can't hold it anymore)"
                    pause
                    play sound "audio/Poison.ogg" volume 0.9 noloop
                    scene bar12:
                        pos (-125, 0)
                        xsize 1104
                        ysize 621
                    Villager2 "(Oh she's really going to do it!)"
                    pause
                    play sound "audio/Poison.ogg" volume 0.9 noloop
                    scene bar13:
                        pos (-125, 0)
                        xsize 1104
                        ysize 621
                    Villager "Almost there..."
                    Leyna "hmm?..."
                    Villager "OOOooohh!!!"
                    Leyna "(!!!)"
                    $ flash_screen(wait=True)
                    play sound "audio/Poison.ogg" volume 0.9 noloop
                    $ flash_screen(wait=True)
                    scene black with dissolve
                    hide bar13
                    show bar14 with dissolve:
                        pos (-125, 0)
                        xsize 1104
                        ysize 621
                    Leyna "AAaah?!!!"
                    Villager "Sorry. It's been so long since a woman touched me that I couldn't help it"
                    Leyna "It's.. it's all over my face ..."
                    Villager "Relax, I bring you a rag to clean yourself"
                    Leyna "Than... thanks. I have to go now or I will pass out.."
                    "It has been..................... fun? Bye"
                    scene black with dissolve
                    hide bar14
                    # fade in
                    show plano_mujer_timida:
                        xsize 1600
                        ysize 900
                    Leyna "..."
                    "What the hell have I done?... I can't let Johan find out about this ..."
                    hide plano_mujer_timida
                "No, this is to much":
                    Leyna "Sorry guys, but I'm a married woman and I can't do this kind of thing..."
                    Villager "I see, don't worry, have a good time at the festival."
                    Villager "(I have time to seduce this girl little by little.. there's no reason to rush)"
                    scene black with dissolve
                    # fade in
        "No":
            pass
    return

label GalleryAtTheRiverWithAlexa_1(menu_choice = None):
    "At the river with Alexa"
    "Do you want to see it?"
    menu:
        "Yes":
            scene rio17
            Alexa "I feel sooo liberated, it's also a great day and we have the perfect temperature to take a bath"
            Leyna "Can we... enter the river now? I don't like being exposed in front of all these people"
            Alexa "Okay okay..."
            Villager "I can't believe my eyes... look at those women! Hey come on, let's go and talk to them"
            Villager2 "Dude I'm married..."
            Villager "Exactly YOU'RE married, fucking whenever you want... But for me? It's been years since I fuck a girl and those two are the sexier fucking girls I've ever seen"
            Villager2 "(Whenever I want?...) Tch... Okay man, but don't be a creep, take it easy"
            Villager "Yeah, relax I'm a dandy! Those two will be on her knees in a blink of an eye"
            Villager2 "(Yeah right... and the \"no fucking in years\"?)"
            scene rio18
            Villager "Hello ladies... I see you two are alone, can we join?"
            Alexa "Oh?... I think you can, sure"
            Leyna "Alexa? I thought we were going to be alone and relax for a while"
            Alexa "Come on Leyna, it's an opportunity to meet new people and have a good time, you worry too much"
            Leyna "..."
            Alexa "Come on guys let's go to the river and take a bath"
            scene rio19
            Alexa "Well... Tell me guys, you work in this town?"
            Villager "Yeah we are from this town and have been working in the coal mine all of our lives"
            Alexa "Oh? I suppose that's why you two are so muscular"
            Leyna "(Is she flirting with them?... Now I see why her husband is so jealous)"
            scene rio20
            Villager2 "I-I'm sorry about this, my friend is... too socially active I suppose"
            Leyna "Don't worry, it's just... I don't feel too comfortable being naked around you.. I'm married after all"
            Villager2 "Yeah I'm married too, don't worry about me I don't wanna do anything to you, I'm here to make sure my friend doesn't make something crazy"
            Leyna "Hahahaha"
            Villager "See?... I told you"
            Alexa "Wow..."
            Leyna "???"
            scene rio21
            Alexa "You're quite big... and sure you're happy to see me..."
            Villager "Hehehe I couldn't help myself... it's so lonely in this town, you know? Not enough woman for all of us"
            Alexa "I can see that... yeah"
            Leyna "(What the hell are they talking about?)"
            Villager2 "Soo..."
            hide rio21
            Leyna "Yeah?"
            Villager2 "You two are here for the festival or...?"
            Leyna "Oh no, I came with my husband to make an article about the traditions of this place, and enjoy the local food"
            Villager2 "So you didn't come with this girl?"
            Leyna "Alexa? No, I meet her today, it seems to have some problems with her husband and we... you know... came here to relax"
            Villager2 "She's married?... (poor guy) Well if you need to know something for your article you can ask me anything"
            Leyna "Okay thank you"
            scene rio22
            Alexa "You're right, it can't fit in my mouth hehehe. Your cock is huge..."
            Villager "Hehehe I told you so..."
            Alexa "Sshhh... be quiet"
            scene black with dissolve
            hide rio22
            # fade in
            "(A FEW MOMENTS LATER...)"
            Leyna "Hahahaaha you're right!"
            Villager "Shit, I can't hold it anymore, come here!"
            Alexa "Hmmmm"
            Villager2 "Hahahaha and I... WOAH what the fuck?!"
            scene rio23
            play music "audio/Dungeon3.ogg" loop volume 0.9
            Alexa "I don't know..."
            Leyna "WHAT?! (are you fucking serious?)"
            Villager2 "Shit, man... you're crazy"
            pause
            scene rio24_movimiento
            play bgs "audio/audio follar.ogg" loop volume 0.9
            Alexa "Oh Oh  OOOHH!! FUCK ME! HARDER!"
            Villager "YOU LIKE THIS?!! FUCK YES!!"
            Leyna "(I can't believe this... ''trying to save my marriage'' my ass)"
            scene rio25
            stop bgs fadeout 1
            Leyna "(But... seems to be enjoying it so much)"
            Leyna "(I'm getting wet seeing all this .. I have to get out of here... I just... I'll stay a little longer ... so that nothing bad happens to Alexa)"
            Villager2 "(This girl is in shock looking at her friend being fucked in public ... maybe this whole situation is exciting her?)"
            Villager2 "(Maybe if I... NO! I'm married... but man this girl is too sexy and with all this situation my cock is hard. If we do it ... I don't think my wife finds out)"
            pause
            scene rio26
            Villager2 "Hey..."
            Leyna "???"
            Villager2 "Ma-maybe you and I?"
            Leyna "(Is he saying... he wants to fuck me here?... His cock is so close to me...)"
            Leyna "What?... OH no! I'm married and you too... I'm definitely going to leave right now"
            Villager2 "I'm just saying... nobody has to know about this, you know?"
            Leyna "We are in public, the whole town will know about this! I'm leaving!"
            Villager2 "O-Okey... (Shit, It was too good to be true)"
            pause
            stop music fadeout 1
            scene black with dissolve
            hide rio26
            # fade in
        "No":
            pass
    return

label GalleryThirdSessionWithThePhotographer_1(menu_choice = None):
    "Third session with the photographer"
    "Do you want to see it?"
    menu:
        "Yes":
            scene publico1
            Johan "Are you sure you want to do this?"
            Leyna "Yes, I know it seems strange but once you start it's not that bad. He is a very professional man"
            Johan "Okay, let's start then"
            OldMan "Great"
            OldMan "Let's start with a natural pose and move forward on the go"
            scene publico2
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "Great, next one"
            pause
            scene publico3
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "Nice, unbutton the top of the blouse and change your posture"
            pause
            scene publico4
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "Very sexy! Let's continue"
            OldMan "Turn up the bottom of the blouse so we can see the lingerie"
            Johan "...!"
            pause
            scene publico5
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "Amazing! Now take off your blouse and perform a couple more poses"
            pause
            scene publico6
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            Johan "(I... feel weird, seeing Leyna like that in public.)"
            OldMan "Okey, the next one"
            pause
            scene publico7
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "Great work Leyna!"
            Johan "(I feel butterflies in my stomach thinking that at any moment someone could come and see this whole situation)"
            pause
            Villager1 "Oh! Wow! What's going on here?"
            Johan "...!!!!"
            scene publico8
            Villager2 "Amazing! What is this, a pornographic session?"
            OldMan "Have a little respect, we are working! And it's for a fashion magazine, so behave!"
            Villager1 "Oh, okay relax, what a shame! (What a bad mood this old man has) You are a supermodel!"
            scene publico9
            Leyna "Thank you.."
            OldMan "Come on Leyna, a couple of poses more, smile a little.."
            Johan "(Wait, are these two going to continue here?)"
            scene publico10
            OldMan "You two stay where you are"
            Villager1 "Okay, no problem..."
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "(Muttering) Yes, this is what they were looking for. But ... I see, yes"
            Johan "(What is he saying?)"
            scene publico12
            Villager1 "(That ass is amazing...)"
            pause
            scene publico13
            OldMan "That's great Leyna!"
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "The problem ... yes, they had already told me ..."
            Leyna "???"
            Leyna "Have we finished?"
            OldMan "No... not yet"
            OldMan "Boys! By chance, are you wearing the festival clothes underneath?"
            Villager1 "... Hmm. Yes, why?"
            OldMan "Would you be interested in posing with the girl?"
            OldMan "The magazine has asked me for more male intervention in the sessions, but my grandson is working right now and cannot come"
            Johan "!!!"
            menu:
                "Intervene":
                    Johan "Hey I think this is more than enough, it was supposed to be a quick session and that nobody was going to be around here"
                    Leyna "(Johan...)"
                    OldMan "True true, sorry. At my age, I keep letting myself go like a small child with the things I like"
                    Johan "..."
                    OldMan "Okay,  we have enough for today, I will talk to the magazine and I will contact you again if I need anything else"
                    Johan "Right..."
                    scene black with dissolve
                    hide publico13
                    # fade in
                "Stay quiet":
                    Villager1 "Will you pay us something?"
                    OldMan "Of course!"
                    Villager1 "Well then ... What are we waiting for?"
                    OldMan "Great! Undress and get together with the girl"
                    Villager2 "Okey!"
                    scene publico14
                    $ flash_screen(wait=True)
                    play sound "audio/Key.ogg" volume 0.9 noloop
                    OldMan "Okay guys, I need a more dominant attitude on your part"
                    Johan "(Dominant?)"
                    pause
                    scene publico15
                    Villager1 "Like this?"
                    OldMan "Not bad but... Both of you"
                    Villager2 "Okey..."
                    pause
                    scene publico16
                    Villager2 "What do you think like that?"
                    OldMan "Like that is perfect!"
                    Johan "(They are touching Leyna... I'm... getting an erection seeing this?... it must be because of the nerves)"
                    $ flash_screen(wait=True)
                    play sound "audio/Key.ogg" volume 0.9 noloop
                    OldMan "Okay, I have enough for now with this"
                    Villager1 "A-are you sure?"
                    OldMan "Yes, let's see what the magazine thinks and I'll contact you two if I need something else"
                    Villager2 "Great (easy money)"
                    Johan "(Thank goodness it's already over...)"
                    scene black with dissolve
                    hide publico16
                    # fade in
        "No":
            pass
    return

label GalleryChangingRoomScene_1(menu_choice = None):
    "Changing room scene"
    "Do you want to see it?"
    menu:
        "yes":
            scene pantallanegro:
                xsize 979
                ysize 720
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            Leyna "Johan? Come in"
            play sound "audio/Move1.ogg" volume 0.9 noloop
            scene probador1
            Leyna "So ... what do you think?"
            Johan "Wow, that's so sexy!"
            scene probador2
            Leyna "Do I look good?"
            Johan "You are beautiful (I would say too beautiful. Now that I think about it, is she supposed to go through the festival like this in front of everyone?)"
            Johan "(Now that I remember, these last days Leyna has had several \"accidents\" around the men of this village)"
            $ flash_screen(wait=True)
            play sound "audio/Poison.ogg" volume 0.9 noloop
            scene rio_7:
                pos (-125, 0)
                xsize 1104
                ysize 621
            Johan "Why am I thinking about this right now?"
            Johan "(I feel something in my stomach ... Am I getting turned on thinking about this?... No, I'm just...)"
            hide rio_7
            $ flash_screen(wait=True)
            scene probador3
            Leyna "Why are you staring at me so hard, Johan?"
            Johan "I'm just... You're so sexy in that outfit... I can't control myself"
            Johan "Let's make love, here and now"
            Leyna "Johan... we shouldn't..."
            Johan "Come here"
            scene black with dissolve
            hide probador3
            # fade in
            play music "audio/Dungeon3.ogg" loop volume 0.9
            scene probador4
            Johan "Oh God,  I can't take it anymore, it's been weeks since last time..."
            Leyna "Ssshhh..."
            scene probador5
            Johan "Ooh! Yes..."
            Leyna "Hm hm hm...."
            pause
            scene probador6
            Leyna "You like it?"
            Johan "I love it"
            pause
            $ flash_screen(wait=True)
            scene escena_camisa_mojada_1:
                pos (-125, 0)
                xsize 1104
                ysize 621
            Johan "Shit, this again? What the hell is wrong with me?"
            hide escena_camisa_mojada_1
            Johan "Get up Leyna"
            Leyna "!!!"
            scene probador7
            Johan "Right there"
            Leyna "hmmmmmmm...."
            scene probador8
            play bgs "audio/audio follar.ogg" loop volume 0.9
            Johan "Yes... damn...."
            Leyna "Oooh... (I have never seen Johan so excited... Does he like to do it in public?)"
            Johan "(Shit ... I can't get those pictures out of my head ... I'm...)"
            Johan "I'm coming!"
            Leyna "Wa...Wait! Take it out"
            scene probador9
            stop bgs fadeout 1
            $ flash_screen(wait=True)
            Johan "OOOHHH"
            Leyna "!!!"
            Johan "SHIT! I'm sorry, let me find something to clean you with"
            scene black with dissolve
            hide probador9
            stop bgs fadeout 1
            # fade in
        "No":
            pass
    return

label GalleryJohansDream_1(menu_choice = None):
    "Johan's dream"
    "do you want to see it?"
    menu:
        "yes":
            scene black with dissolve
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            pause 0.6
            play music "audio/Dungeon1.ogg" loop volume 0.9
            Johan "(Hmmm... What's this? I feel... strange)"
            if switch("johan_silent"):
                show publico14 with dissolve
                Johan "Oh no.. this again?"
                pause
                scene publico16
                Johan "(S-stop!... Shit! I can't move or speak)"
                Johan "(What the hell do you think you're doing to my wife?)"
                pause
                hide publico16
            if switch("johan_intervened"):
                scene publico13
                # fade in
                Johan "Oh no.. this again?"
                Johan "(Why are you looking at my wife like this?)"
                scene publico16
                Johan "(Hey! What the hell are you doing with my wife?)"
                Johan "(S-stop!... Shit! I can't move or speak)"
                pause
                hide publico16
            scene sue_o1
            OldMan "Yeah, that position is perfect!"
            Johan "(Perfect?!, stop touching her!)"
            Villager1 "I have an idea! Did you want risque photos right? Well, look"
            scene sue_o2
            OldMan "Yeah! Great work guys!"
            Johan "(No! Stop!)"
            Villager2 "Shit! Look at those tits, they're perfect!"
            Villager1 "Yeah! Fuck this I can't hold it anymore"
            scene sue_o3
            Johan "(They have taken out their cocks! Leyna, Leyna say something!)"
            Villager1 "What do you think honey, you like what you see?"
            Leyna "They're ... they're huge"
            Villager2 "Seems she is enjoying it. Hey photographer! Take a picture of this, surely the magazine will love it"
            pause
            scene sue_o4
            OldMan "Yes!"
            Villager2 "It seems that you are wet down there precious"
            Leyna "Wha-What are you going to do?"
            Villager2 "Shhhh, quiet. Just enjoy bitch"
            pause
            scene sue_o6
            Johan "(He is fucking her! Stop!... Why?... Why I feel like this? I'm getting hard)"
            Leyna "OOoohh it's sooo big!"
            Villager2 "Just say it bitch! Say \"fuck me\""
            Leyna "I.. I... fuck me"
            Villager2 "What?"
            Leyna "Fuck me please"
            Villager2 "Okey!"
            scene sue_o7
            play bgs "audio/audio follar.ogg" loop volume 0.9
            Johan "(Am I enjoying this?... Why can't I stop looking at? This feeling in my stomach ... I've never felt like this)"
            Villager2 "YEAH! You like it?"
            Leyna "I LOVE IT, PLEASE FUCK ME HARDER!"
            Johan "(No... please stop! I can't take this anymore!)"
            scene black with dissolve
            stop music fadeout 1
            stop bgs fadeout 1
            hide sue_o7
            # fade in
        "No":
            pass
    return

label GalleryJailScene_1(menu_choice = None):
    "Jail scene"
    "Do you want to see it?"
    menu:
        "Yes":
            scene carcel1
            Johan "Leyna!"
            Johan "Somebody help us!!"
            scene carcel2
            Policeman "Shit... I told you not to go near the cell"
            Prisoner "What a fine woman you've brought me"
            Johan "Get away from my wife right now"
            Prisoner "I don't think so ... I haven't fucked a woman as pretty as you in years, darling"
            Prisoner "Let me see those tits"
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            scene carcel3
            Johan "YOU SON OF A BITCH LET HER GO!"
            Johan "Are you not going to do anything?"
            Policeman "Wait, as soon as we get the chance we'll release your wife"
            Prisoner "Are you getting horny with this, bitch?"
            Leyna "Please let me go!"
            Prisoner "Nah, let me touch your pussy and see if you're wet"
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            scene carcel4
            Leyna "NO! PLEASE!"
            Johan "STOP!"
            Policeman "(I have to stop it but ... what a good view!)"
            Prisoner "God damn! You're sexy as fuck, girl"
            Prisoner "Since you are showing me everything, let me show you mine"
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            scene carcel5
            Prisoner "You're very hot down there, can you really be getting horny with this? You are a whore!"
            Leyna "Shu-shut up!"
            Johan "!!!"
            Prisoner "I can't wait any longer, I have to fuck this pussy right now"
            Leyna "What?!"
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            scene carcel6
            Leyna "NO! STOP!"
            Prisoner "Almost there!"
            Policeman "NOW! Stop him!"
            Prisoner "Hm?"
            scene black with dissolve
            stop music fadeout 1
            hide carcel6
            # fade in
        "No":
            pass
    return

label GalleryAtNightWithTheYoungBoys_1(menu_choice = None):
    "At night with the young boys"
    "Do you want to see it?"
    menu:
        "Yes":
            scene adolescentes1
            Johan "Wow this liquor is quite strong"
            YoungVillager "Hahahaha I know, in this town we make liquors quite strong"
            Leyna "So you have already tried it, huh?"
            YoungVillager "Mmm yes.. from time to time I take a little from my father, but it's not enough for all of us"
            YoungVillager "Hey, I don't know your names yet"
            Johan "Oh sure, I'm Johan and this is my wife Leyna"
            YoungVillager "A pleasure guys! Hey Leyna, don't you want to drink a couple of shots?"
            Leyna "Oh ... I don't know if I should ..."
            Johan "(Leyna feels bad about alcohol ... but a little shouldn't hurt)"
            YoungVillager "Came on! It's not a proper party if we don't all drink"
            Johan "He's right, come on Leyna, a little doesn't hurt"
            Leyna "If that's okay with you then ... why not?"
            YoungVillager "Great!"
            scene adolescentes2
            Johan "(Wow that's a pretty big drink)"
            YoungVillager "(Cool she's not playing, she almost drinks half a bottle in one go)"
            scene adolescentes3
            Leyna "Wow! It's strong but it's very good"
            YoungVillager2 "So tell me, are you here on vacation?"
            Leyna "Yes, we've come to do a report of the festival for a tourism magazine, we are from the capital"
            YoungVillager2 "Great, the capital! I've always wanted to go but my father makes me work every day in the fields and I don't have time for anything"
            YoungVillager "Yes, it must be great to live in the capital, surely there are many beautiful girls like you there"
            scene adolescentes4
            Leyna "Pretty girls? Hahaha thanks"
            YoungVillager "Here there are almost none and those who live here are already married or their parents have them out of our reach"
            Johan "Hahahahha a classic, Leyna's father was also very protective of her"
            YoungVillager2 "Ahh so in the capital they are also like that.. there is no hope guys! let's drink more"
            Johan "Hahahah perfect, but I have to control myself, that liquor is very strong and it is already going to my head!"
            YoungVillager "Well ... that's the idea isn't it? hahaha"
            Johan "You're right (although Leyna worries me, you can see in her face that she's quite drunk)"
            YoungVillager2 "Ahh !! Man, we're going to die without seeing a naked woman"
            Johan "Come on come on, it's not so bad, you will surely find your ideal woman and meanwhile you have internet to entertain you"
            YoungVillager "Internet? There is no connection here except in the town hall and there it's impossible to see anything"
            Johan "(Wow, teenagers without internet or girls ... poor guys I can't imagine how bad it would have been for me)"
            Johan "Come on guys don't get depressed, for sure it will be solved!"
            YoungVillager2 "It's easy for you to say, you are with a beautiful woman. Sure you do it every day!"
            Johan "(I wish I were...) Hahaha well it's not that simple.."
            YoungVillager "Right, if I had a wife like Leyna I would be fucking everyday day without stopping"
            scene adolescentes5
            Leyna "Hahaha what an impressive youth"
            YoungVillager2 "And.. this.. since you see them every day.. How are they?"
            Johan "... the boobs?"
            YoungVillager "Yes yes!"
            Johan "Well they are ... very pretty?"
            YoungVillager2 "Ahh very pretty and we will die without seeing some"
            YoungVillager "Hey ... couldn't you show us something Leyna? Just a a little to know how they are"
            Leyna "Ah?!"
            YoungVillager "Come on it will be only a second! You're beautiful! Just a little bit and we won't talk about it again"
            Johan "Wow, slow down!"
            YoungVillager "Oh! Of course if you give us permission Johan, let's go, we don't have internet and we are crazy to know a little"
            YoungVillager2 "Yes! And what if one day I do it with a woman and I haven't seen anything before? I will stay like a stone. How embarrassing.."
            Johan "Guys..."
            YoungVillager "Please it will only be a second"
            Johan "eh..."
            Leyna "If it's only for a second ..."
            Johan "Leyna?"
            Leyna "They're just kids, they're harmless! They give me a little pity"
            Johan "...(Leyna is clearly drunk ... well and I am too ... just a second? The truth is they also give me some pity ..)"
            Johan "(If she shows them something they will leave us alone with the subject ...)"
            menu:
                "Yes":
                    Johan "Okay guys, but just a second and that's it!"
                    YoungVillager "REALLY?! Great, thank you very much!"
                    YoungVillager2 "Incredible I can't believe it, thank you very much!"
                    Leyna "Okay, just a little look and that's it"
                    scene adolescentes6
                    Leyna "Here they are!"
                    YoungVillager "Wow!! Amazing!"
                    YoungVillager2 "Great, I'm going to jerk off tonight, thank you very much!"
                    Johan "Hey you don't have to tell us that"
                    YoungVillager "Hey can I ... can I touch them?"
                    Leyna "Ehm..."
                    Johan "No way! Without touching, this has been enough!"
                    YoungVillager "Sorry..."
                    pause
                    scene black with dissolve
                    hide adolescentes6
                    # fade in
                    "...A FEW DRINKS OF LIQUOR LATER..."
                    Leyna "Well ... I think it's about time we go"
                    YoungVillager2 "Oooh! Now that we were having a good time?"
                    Johan "Relax, we'll see you around here"
                    YoungVillager "I take your word, if you want to have a good time one day you know where we are"
                "No":
                    Johan "You're drunk, you don't know what you're saying"
                    Johan "You're definitely not going to show your tits to these kids, sorry guys."
                    Johan "We were having a good time but we should go"
        "No":
            pass
    return

label GalleryAtNightWithTheYoungBoys_2(menu_choice = None):
    "At night with the young boys"
    "Do you want to see it?"
    menu:
        "Yes":
            scene adolescentes1
            Johan "Wow this liquor is quite strong"
            YoungVillager "Hahahaha I know, in this town we make liquors quite strong"
            Leyna "So you have already tried it, huh?"
            YoungVillager "Mmm yes.. from time to time I take a little from my father, but it's not enough for all of us"
            YoungVillager "Hey, I don't know your names yet"
            Johan "Oh sure, I'm Johan and this is my wife Leyna"
            YoungVillager "A pleasure guys! Hey Leyna, don't you want to drink a couple of shots?"
            Leyna "Oh ... I don't know if I should ..."
            Johan "(Leyna feels bad about alcohol ... but a little shouldn't hurt)"
            YoungVillager "Came on! It's not a proper party if we don't all drink"
            Johan "He's right, come on Leyna, a little doesn't hurt"
            Leyna "If that's okay with you then ... why not?"
            YoungVillager "Great!"
            scene adolescentes2
            Johan "(Wow that's a pretty big drink)"
            YoungVillager "(Cool she's not playing, she almost drinks half a bottle in one go)"
            scene adolescentes3
            Leyna "Wow! It's strong but it's very good"
            YoungVillager2 "So tell me, are you here on vacation?"
            Leyna "Yes, we've come to do a report of the festival for a tourism magazine, we are from the capital"
            YoungVillager2 "Great, the capital! I've always wanted to go but my father makes me work every day in the fields and I don't have time for anything"
            YoungVillager "Yes, it must be great to live in the capital, surely there are many beautiful girls like you there"
            scene adolescentes4
            Leyna "Pretty girls? Hahaha thanks"
            YoungVillager "Here there are almost none and those who live here are already married or their parents have them out of our reach"
            Johan "Hahahahha a classic, Leyna's father was also very protective of her"
            YoungVillager2 "Ahh so in the capital they are also like that.. there is no hope guys! let's drink more"
            Johan "Hahahah perfect, but I have to control myself, that liquor is very strong and it is already going to my head!"
            YoungVillager "Well ... that's the idea isn't it? hahaha"
            Johan "You're right (although Leyna worries me, you can see in her face that she's quite drunk)"
            YoungVillager2 "Ahh !! Man, we're going to die without seeing a naked woman"
            Johan "Come on come on, it's not so bad, you will surely find your ideal woman and meanwhile you have internet to entertain you"
            YoungVillager "Internet? There is no connection here except in the town hall and there it's impossible to see anything"
            Johan "(Wow, teenagers without internet or girls ... poor guys I can't imagine how bad it would have been for me)"
            Johan "Come on guys don't get depressed, for sure it will be solved!"
            YoungVillager2 "It's easy for you to say, you are with a beautiful woman. Sure you do it every day!"
            Johan "(I wish I were...) Hahaha well it's not that simple.."
            YoungVillager "Right, if I had a wife like Leyna I would be fucking everyday day without stopping"
            scene adolescentes5
            Leyna "Hahaha what an impressive youth"
            YoungVillager2 "And.. this.. since you see them every day.. How are they?"
            Johan "... the boobs?"
            YoungVillager "Yes yes!"
            Johan "Well they are ... very pretty?"
            YoungVillager2 "Ahh very pretty and we will die without seeing some"
            YoungVillager "Hey ... couldn't you show us something Leyna? Just a a little to know how they are"
            Leyna "Ah?!"
            YoungVillager "Come on it will be only a second! You're beautiful! Just a little bit and we won't talk about it again"
            Johan "Wow, slow down!"
            YoungVillager "Oh! Of course if you give us permission Johan, let's go, we don't have internet and we are crazy to know a little"
            YoungVillager2 "Yes! And what if one day I do it with a woman and I haven't seen anything before? I will stay like a stone. How embarrassing.."
            Johan "Guys..."
            YoungVillager "Please it will only be a second"
            Johan "eh..."
            Leyna "If it's only for a second ..."
            Johan "Leyna?"
            Leyna "They're just kids, they're harmless! They give me a little pity"
            Johan "...(Leyna is clearly drunk ... well and I am too ... just a second? The truth is they also give me some pity ..)"
            Johan "(If she shows them something they will leave us alone with the subject ...)"
            menu:
                "Yes":
                    Johan "Okay guys, but just a second and that's it!"
                    YoungVillager "REALLY?! Great, thank you very much!"
                    YoungVillager2 "Incredible I can't believe it, thank you very much!"
                    Leyna "Okay, just a little look and that's it"
                    scene adolescentes6
                    Leyna "Here they are!"
                    YoungVillager "Wow!! Amazing!"
                    YoungVillager2 "Great, I'm going to jerk off tonight, thank you very much!"
                    Johan "Hey you don't have to tell us that"
                    YoungVillager "Hey can I ... can I touch them?"
                    Leyna "Ehm..."
                    Johan "No way! Without touching, this has been enough!"
                    YoungVillager "Sorry..."
                    pause
                    scene black with dissolve
                    hide adolescentes6
                    # fade in
                    "...A FEW DRINKS OF LIQUOR LATER..."
                    Leyna "Well ... I think it's about time we go"
                    YoungVillager2 "Oooh! Now that we were having a good time?"
                    Johan "Relax, we'll see you around here"
                    YoungVillager "I take your word, if you want to have a good time one day you know where we are"
                "No":
                    Johan "You're drunk, you don't know what you're saying"
                    Johan "You're definitely not going to show your tits to these kids, sorry guys."
                    Johan "We were having a good time but we should go"
        "No":
            pass
    return

label GalleryHotsprings3_1(menu_choice = None):
    "Hotsprings 3"
    "do you want to see it?"
    menu:
        "Yes":
            scene black with dissolve
            show hotspringsjuntos2 with dissolve
            Villager "Hey, is this your first time? I don't think I know you from the village!"
            Johan "Well, yes, I came with my wife to work and take a little vacation"
            Villager "Ohh great great! I hope you enjoy it, we have the best Hotsprings in the country that's for sure! we put some special herbs that only grow here"
            Johan "Wow! I had imagined it, they certainly have a revitalizing effect on the body!"
            Villager "You're telling me! hahahahahahaha!"
            Johan "(Did I say something funny?) Yeah hahaha... by the way this is pretty crowded isn't it? is it always like this?"
            Villager "Oh no no no, we only come on special occasions, winter festivals and such..."
            Villager "... But do you want to know the truth?"
            Johan "The truth? sure, tell me"
            Villager "Word has spread around town that a new girl has come to work here and she is nothing less than a beauty!"
            Johan "!!!..."
            Villager "A goddess by all accounts! And of course the guys can't help but come in droves to gossip and if they can show off a bit in front of the girl too hahaha"
            Johan "Of course hahahaha (Shit he's talking about Leyna right?, more attention to Leyna...)"
            scene hotspringsjuntos3
            Johan "(Leyna has arrived! She seems to be a little nervous but I'm sure she'll do fine)"
            Johan "(I hope no one goes overboard with her)"
            scene hotspringsjuntos4
            Johan "????"
            Johan "(What the hell, when I arrived everyone was dressed! and now they're all naked!)"
            scene hotspringsjuntos5
            Johan "(And that guy has a boner! They're all surrounding her, it's not necessary to get that close)"
            Johan "(What are they saying to him? damn it, from here I can't hear anything they are saying... but getting close would be a bit... embarrassing)"
            Johan "(I don't want to go and make Leyna even more nervous, she might lose her job...)"
            scene hotspringsjuntos6
            Johan "(It seems that he has been asked for something from the storage)"
            Johan "(Well, she seems to be calmer and in a good mood, I guess after these days in this town she is getting used to seeing naked men)"
            Johan "(I'm glad she's calmer.... but I don't like this situation)"
            scene hotspringsjuntos7
            Johan "(Well, he will be giving them the products whatever they have asked him for)"
            pause
            if switch("infusion"):
                scene hotspringsjuntos8
                Johan "(what's going on there? I hope they are not giving problems to Leyna...)"
                Johan "(she will be looking for something on the shelves... some cream or balm)"
                pause
                scene hotspringsjuntos9
                Johan "(They are taking a long time.... Why am I so worried? my stomach is upset... I don't know what's been happening to me for a couple of days now)"
                Johan "(Am I becoming a jealous husband?... I have to stop having such a hard time when Leyna is not with me for the sake of our relationship)"
                Johan "(And my mental health... shit... it's taking too long, isn't it... here we go again Johan try to relax)"
                pause
                scene black with dissolve
                hide hotspringsjuntos9
            if not switch("infusion"):
                Johan "(what's going on there? I hope they are not giving problems to Leyna...)"
                Johan "(she will be looking for something on the shelves... some cream or balm)"
                Johan "(Am I becoming a jealous husband?... I have to stop having such a hard time when Leyna is not with me for the sake of our relationship)"
                Johan "(And my mental health... shit... it's taking too long, isn't it... here we go again Johan try to relax)"
                pause
                scene black with dissolve
            scene hotspringsjuntos8
            show hotspringsjuntos10 with dissolve
            "A FEW MOMENTS LATER"
            Johan "!!! (It looks like Leyna has finished helping those guys and comes to greet me)"
            Johan "(At the end it does seem that she is a little uncomfortable with all these naked men around her... the truth is that I feel a little relieved hahaha)"
            scene hotspringsjuntos11
            Leyna "Hello Johan, is everything all right?"
            Johan "Yes! everything is perfect honey, you don't need to pay much attention to me, I don't want to cause you any problems"
            if switch("infusion"):
                scene hotspringsjuntos13
                Leyna "Ohh don't worry, I'm almost done... in half an hour everything will be ready and I'll be able to go out"
                Johan "Great! I'll wait for you to finish and we'll go out together Is that okay with you?"
                Leyna "Yes, of course!"
                scene black with dissolve
            if not switch("infusion"):
                Leyna "Ohh don't worry, I'm almost done... in half an hour everything will be ready and I'll be able to go out"
                Johan "Great! I'll wait for you to finish and we'll go out together Is that okay with you?"
                Leyna "Yes, of course!"
                scene black with dissolve
            hide hotspringsjuntos13
            show hotspringsjuntos12 with dissolve
        "No":
            pass
    return

label GalleryHotsprings2_1(menu_choice = None):
    "Hotsprings 2"
    "do you want to see it?"
    menu:
        "Yes":
            scene trabajo1
            Leyna "Is this serious? What a uniform... this is too provocative, she goes with normal clothes.. Why do I have to put on this kind of clothing?"
            Leyna "You can see everything ..."
            WomansVoice "Leyna? what are you doing here?"
            scene trabajo2
            Leyna "???"
            Leyna "(I can't believe she's here without her husband, well, it was to be expected)"
            scene trabajo3
            Leyna "Wow Alexa, I didn't expect to see you here... alone"
            Leyna "You know that the hotsprings are mixed, right?"
            Alexa "I know..."
            Alexa "My husband is with the friends who accompany us in the trip and I didn't want to be alone"
            scene trabajo4
            Leyna "I see... although you never stay alone for long..."
            Alexa "I like to be accompanied, what can I say... hehehe"
            scene trabajo5
            Alexa "Well... and you? What are you doing here alone?"
            Leyna "I've started working here today so I will prepare your bath, I hope you enjoy it"
            Alexa "I'm sure I will hehehe"
            scene black with dissolve
            show trabajo6 with dissolve
            "A FEW MOMENTS LATER"
            Leyna "Alexa? I leave you here a few dry towe..."
            scene trabajo7
            Leyna "(what's going on here? where did these people come from?... I can't believe it, doing this in public again)"
            scene trabajo8
            Alexa "Right there, you're going to break me in half"
            Villager "What a dirty bitch"
            scene trabajo9
            Leyna "(They don't worry that somebody can see them? somebody could enter at any moment)"
            scene trabajo10
            Alexa "Fuck me, come on!"
            Villager2 "This bitch is crazy"
            Villager "I know... It's great, we have to take advantage of this unique opportunity in life, dude"
            Alexa "we don't have much time, fuck me before someone comes"
            scene trabajo11
            Leyna "(I... am I getting turned on? by this? What kind of person I' m becoming?)"
            scene trabajo12
            play bgs "audio/audio follar.ogg" loop volume 0.9
            Villager "Do you like it bitch?"
            Alexa "I love it! FUCK ME PLEASE! HARDER!"
            Villager2 "I'm going to cum, your ass is incredible!"
            Alexa "DON'T CUM YET! KEEP FUCKING ME PLEASE!!"
            stop bgs fadeout 1
            play music "audio/Town1.ogg" loop volume 0.9
            scene trabajo13
            Leyna "(... I think anyone can't see me from here. They don't even know I'm here)"
            Leyna "(I have to get it off my chest, it will only take a second)"
            scene trabajo14
            Leyna "Ahhhh"
            Leyna "(Shit, I have to be quiet or they might discover me and that... would be a problem)"
            Leyna "(Yes, I would be in serious trouble, I could get caught and between them two...)"
            scene trabajo15
            Leyna "Hmmmmm"
            Leyna "(I would be caught between the two of them and... fuck me through every hole in my body, using me)"
            $ flash_screen(wait=True)
            Leyna "Aaah!"
            $ flash_screen(wait=True)
            Leyna "I'm... I'm ..."
            $ flash_screen(wait=True)
            Leyna "Hmmmmmaaa..."
            scene trabajo16
            Leyna "Shit, I hope the didn't notice"
            Leyna "That... was very good, but I shouldn't have done it... just thinking about it, again I'm ... I'm not being myself, I should go back"
            pause
            scene black with dissolve
            hide trabajo16
            # fade in
        "No":
            pass
    return

label GalleryFoodStall1_1(menu_choice = None):
    "Food stall 1"
    "do you want to see it?"
    menu:
        "yes":
            scene puesto2
            Friend "She's so hot. Look at that ass"
            scene puesto3
            WorkersSon "Right? Everyone here is trying to fuck her, it's like she is asking for it."
            scene puesto4
            WorkersSon "I have an idea, let's say hi, keep talking to the man and I will try something"
            Friend "Be careful man, I don't want any trouble"
            WorkersSon "Don't worry,I can be stealthy when I want"
            scene puesto5
            WorkersSon "Hey guys, what a surprise to see you here. Are you having a good time?"
            Johan "Hey kid! Yes, this is very fun"
            scene puesto6
            WorkersSon "\"Whispering \"Leyna, it's nice to see you in those clothes"
            scene puesto7
            Leyna "He..hello"
            scene puesto8
            WorkersSon "They say you are the lucky person this year, everyone has to touch you, right?"
            Leyna "I guess..."
            scene puesto6
            WorkersSon "Do you know what brings more lucky?"
            Leyna "W...what?"
            scene puesto10
            Johan "This place is beautiful, I love your festivities!"
            Friend "Everyone here is very kind, right? We want you to feel as well as possible"
            scene puesto9
            WorkersSon "Touching gently the lucky person. The happier she is, the more luck she will bring to others"
            if switch("ate_the_fruit"):
                Leyna "(What is he doing? I don't want to say anything, I wouldn't want to get Johan in trouble)"
                Leyna "(Oh my god, this boy... what is he doing? I can't resist, this fruit has turned me on so much...)"
                scene puesto11
                WorkersSon "Do you like it?"
                scene puesto12
                Leyna "Y...yes... (If Johan see us.... but I don't really care right now..)"
                scene puesto13
                WorkersSon "I want to be lucky for many years, you know?"
                scene puesto14
                WorkersSon "And you are so hot, I can't resist my self. I don't usually do this but.."
                scene puesto15
                WorkersSon "You are so warm down there.. I want a little of what your husband has"
                scene puesto16
                WorkersSon "Oh yes!"
                scene puesto17
                Leyna "OHH!!!!!!!!"
                scene puesto16
                WorkersSon "SHH! Don't scream. We don't want your husband to see us, right? Just enjoy.."
                scene puesto12
                Leyna "Please,do..don't, I love Johan... and..."
                scene puesto15
                WorkersSon "I don't doubt it, we are just having a good time"
                scene puesto10
                Johan "Well guys, see you over there then.."
                scene puesto18
                WorkersSon "Fuck....."
                scene puesto19
                WorkersSon "Yeah! See you..."
                Leyna "(Why are they leaving? I was so...)"
                Leyna "Yeah, bye guys.."
                hide puesto19
            if not switch("ate_the_fruit"):
                Leyna "(What is he doing? I don't want to say anything, I wouldn't want to get Johan in trouble)"
                scene puesto11
                WorkersSon "Do you like it?"
                Leyna "Mmmm... we should stop this.."
                scene puesto13
                WorkersSon "I want to be lucky for many years, you know?"
                scene puesto14
                WorkersSon "And you are so hot, I can't resist my self. I don't usually do this but.."
                Leyna "Stop now"
                hide puesto14
                play sound "audio/Blow1.ogg" volume 0.9 noloop
                pause 0.6
                scene puesto10
                Johan "Well guys, see you over there then.."
                scene puesto19
                WorkersSon "Yeah! See you..."
                Leyna "Yeah, bye guys (that was close..)"
                hide puesto19
        "No":
            pass
    return

label GalleryFindTheYoungVillager_1(menu_choice = None):
    "Find the young villager"
    "Do you want to see it?"
    menu:
        "Yes":
            Leyna "I found you!"
            scene mamada1
            YoungVillager "Right and now comes the best part, go ahead and give me a kiss"
            scene mamada2
            Leyna "Well, a peck on the cheek"
            scene mamada3
            YoungVillager "No kiss on the cheek, the kiss has to be on the mouth, I'm not a child anymore, that's what tradition dictates"
            scene mamada4
            Leyna "(This town and its damn traditions)"
            Leyna "Let's get this over with I'll give you the kiss and we'll be back"
            YoungVillager "Great..."
            Leyna "(Well, it's just an innocent kiss Leyna)"
            scene mamada5
            Leyna "!!!!"
            Leyna "(This boy!!)"
            scene mamada6
            Leyna "(it's certainly not the first kiss he's given... it can't be)"
            Leyna "(I'm getting too excited with this kiss... I should stop now but... it's so... hard to stop now)"
            scene mamada7
            Leyna "... Stop... stop now"
            YoungVillager "Stop? why?"
            scene mamada8
            Leyna "Because I'm married! we have to go back now"
            YoungVillager "We can't go back now"
            Leyna "And why can't we?"
            scene mamada9
            YoungVillager "Look how I am now! I can't go around town like this"
            Leyna "Oh...."
            Leyna "(... Of course, it has to be huge...)"
            scene mamada10
            YoungVillager "And this is all your fault"
            Leyna "My fault?"
            scene mamada11
            YoungVillager "Of course, you enjoyed that kiss too, didn't you? I could tell, you're so sexy that my body can't control itself"
            Leyna "But..."
            YoungVillager "No! I can't go around town like this, what if my mother sees me? she'll think I'm a pervert!"
            YoungVillager "You have to take responsibility for your actions and help me with this"
            scene mamada12
            Leyna "Res-responsibility?"
            menu:
                "Help him":
                    Leyna "O...okay I will help you with this"
                    Leyna "I'll... I'll show you my body a little bit and you can... touch yourself"
                    YoungVillager "... Well... go ahead"
                    scene mamada13
                    Leyna "(I can't believe I'm doing this in the middle of the street)"
                    Leyna "Go on..."
                    play music "audio/audio follar.ogg" loop volume 0.9
                    scene mamada15
                    YoungVillager "..."
                    YoungVillager "......"
                    YoungVillager "............"
                    scene mamada14
                    stop music fadeout 1
                    play music "audio/Town1.ogg" loop volume 0.9
                    Leyna "Are you done?"
                    YoungVillager "AAAh I can't do this! you can't rush me with this! besides I've already seen boobs in magazines and stuff... this is not enough, you have to help me!"
                    Leyna "Help you more?...."
                    YoungVillager "Yeah... come on, you're a grown woman, you must have done this a hundred times..."
                    Leyna "... Okay... I'll help you, let's get this over with before someone sees us"
                    scene mamada16
                    Leyna "God..."
                    YoungVillager "Big, right?"
                    Leyna "Don't... don't say anything"
                    scene mamada17
                    Leyna ".... ( Is so close to me... )"
                    pause
                    scene mamada18
                    stop music fadeout 1
                    play music "audio/audio follar.ogg" loop volume 0.9
                    YoungVillager "Ohhh yes, keep it up"
                    Leyna "(I'm really wet down there... right now, we could fuck and no one would notice...)"
                    Leyna "... you are taking too long..."
                    YoungVillager "Sssshh...."
                    YoungVillager "I'm almost there... I'm almost there"
                    stop music fadeout 1
                    if switch("infusion"):
                        Leyna "(If this keeps up we'll end up getting caught, I have to end this quickly)"
                        Leyna "... I'll have to help you a little bit more ...."
                        YoungVillager "???"
                        scene mamada19
                        stop music fadeout 1
                        play music "audio/Town1.ogg" loop volume 0.9
                        YoungVillager "Oooh great!!!"
                        Leyna "( It barely fits in my mouth...)"
                        YoungVillager "This is the best thing that has ever happened to me!"
                        Leyna "(My God, what am I doing? I've never behaved like this... but I'm so horny... it's hard to control myself)"
                        stop music fadeout 1
                        play music "audio/audio follar.ogg" loop volume 0.15
                        image mamada_webm = Movie(play="movies/mamada.webm", loop=True, size=(816, 459), ypos=83)
                        scene mamada_webm
                        pause
                        scene mamada20
                        Leyna "(It's still taking too long... maybe if I... put it inside me I'll finish sooner... maybe... maybe I'll have to fuck him...)"
                        stop music fadeout 1
                        play music "audio/Town1.ogg" loop volume 0.9
                        Leyna "Hey..."
                        scene black with dissolve
                        # fade in
                    scene mamada21
                    $ flash_screen(wait=True)
                    YoungVillager "OOOoooh!!!"
                    pause
                    if switch("infusion"):
                        Leyna "(That's it... what was I about to do? was I going to fuck this guy in the middle of the street if I had gone a little bit longer?)"
                    scene mamada22
                    Leyna "(thank goodness it's over, although now I have to clean up this mess)"
                    scene mamada23
                    YoungVillager "Well, that's it... thank you very much!"
                    Leyna "Stop being thankful... bring me something I can clean myself with! and fast!"
                    YoungVillager "Y-yes sure! I'll be right back"
                    Leyna "...."
                    scene black with dissolve
                    show mamada24 with dissolve
                    YoungVillager2 "I can't believe it! what a lucky son of a bitch!"
                    YoungVillager3 "Some are born lucky and others like us are not.... But don't worry, I've taken pictures and I'll pass them on to you later!!"
                    YoungVillager2 "Oh! so you took pictures! hahahaha I have an idea!"
                    stop music fadeout 1
                    if not renpy.in_rollback():
                        $ _saved_bgm = renpy.music.get_playing()
                    play music "audio/Curse1.ogg" volume 0.5 noloop
                    if _saved_bgm is not None and not renpy.in_rollback():
                        queue music _saved_bgm
                        $ _saved_bgm = None
                    scene black with dissolve
                    hide mamada23
                    hide mamada24
                "Don't help him":
                    scene black with dissolve
                    show mamada25 with dissolve
                    Leyna "NO... I cannot help you I am a married woman"
                    YoungVillager "You're going to leave me like this? you can't do that"
                    scene mamada26
                    Leyna "Sorry I have to go!"
                    YoungVillager "Wait!"
                    scene black with dissolve
                    hide mamada26
            # fade in
        "No":
            pass
    return

label GalleryBonfireWithTheYoungBoys_1(menu_choice = None):
    "Bonfire with the young boys"
    "Do you want to see it?"
    menu:
        "Yes":
            scene blackmail1
            YoungVillager "Hey! What's up guys? You going out tonight? Do you want to join us for a drink? We had a great time the other day"
            Johan "Sure, guys, we can stay for a while"
            Leyna "... (Shit, this is the last situation I wanted)"
            scene blackmail2
            YoungVillager2 "We've run out of liquor, but I have a bottle left at home. Johan, will you come with me? So you can carry the bottle around town without me getting caught"
            Johan "Oh, sure, no problem"
            Leyna "Great, I'm coming too"
            Johan "Don’t worry, wait for me here and relax a bit at the bonfire"
            Leyna "Oh... sure..."
            scene black with dissolve
            hide blackmail2
            # fade in
            if switch("corruption_average"):
                scene blackmail3
                YoungVillager "So... what do you think about our festival?"
                Leyna "Mmmm... well, I guess"
                YoungVillager "Ah... great yeah... hey, look at this cool picture"
                Leyna "Well, let's see..!!!!!!!!!!! Th-this is.. H-how?"
                scene blackmail4
                Leyna "WHATTT?!!"
                Leyna "How... where did you get that picture?"
                YoungVillager "I took it... yes, we caught you in the act, you don't want your husband to see this picture, do you?"
                Leyna "What? Of course not!"
                YoungVillager "Well if you don't want that to happen, you will listen to us"
                scene blackmail5
                Leyna "I... what do you want? I don't have much money..."
                YoungVillager "We don't want money, you see, we can't let our friend go around bragging to us about getting a blowjob from a beauty like you"
                YoungVillager "And we're just sitting here... so you know, we want you to do the same to us as you did to him"
                scene blackmail6
                Leyna "HOW? you have so little shame, how dare you? I refuse!"
                YoungVillager "Well, then I guess you don't mind so much... now when your husband gets back I'll show him the picture if you don't mind.."
                scene blackmail7
                Leyna "WAIT! wait... okay... okay damn it..."
                YoungVillager "Great, let's go to the alley"
                Leyna "Wait, right now?  But..."
                YoungVillager "Exactly, right now. And we have to hurry, they'll be right back. You don't want them to catch us in the act, do you?"
                Leyna "(Fucking son of a bitch).... of course"
                YoungVillager "Great, let's get it over with"
                scene blackmail8
                YoungVillager "Well, here we are"
                YoungVillager "Here you go, free buffet ahahaha"
                Leyna "Shut up... (fuck...)"
                scene blackmail9
                Leyna "(I can't believe I'm going to do this again in public)"
                YoungVillager "What are you waiting for? You don't want us to get caught, do you?"
                Leyna "I... okay"
                scene blackmail10
                Leyna "(My god, I don't think I can even fit in my mouth...I have to get this over with fast or it could go terribly wrong)"
                YoungVillager "Come on, don't make me wait any longer, I'm feeling your breath on my cock, don't worry, I'm sure we'll cum in no time"
                scene blackmail11
                YoungVillager "OOoooh! That feels so good, it's so warm in there. Keep it up"
                Leyna "(shut up, don't keep talking please..... why is my body behaving this way? i'm getting horny doing this)"
                YoungVillager "Hey! Don't forget about me, come on, suck my dick"
                Leyna "O..okay.."
                scene blackmail12
                YoungVillager3 "Uoh great, this is the best!"
                Leyna "(Doing this to two guys at the same time on the street...I've never done anything like this... but it feels so good..)"
                Leyna "(.. but, what am I saying? I'm not like this)"
                play sound "audio/Equip2.ogg" volume 0.9 noloop
                scene blackmail13
                Leyna "What are you doing?!"
                YoungVillager "You don't need this hahahaha besides, if I don't see something while you're blowing my friend, we'll never finish"
                YoungVillager3 "Good idea! since the last time you showed them to us,I have not been able to get them out of my head"
                Leyna "I..."
                scene blackmail14
                play bgs "audio/audio follar.ogg" loop volume 0.9
                YoungVillager3 "Who told you to stop sucking my dick? COME ON, GET IT OVER WITH"
                Leyna "Ugh!"
                YoungVillager "Wow! A deep throat! This girl has experience! She looks like a saint but she's a whore!"
                Leyna "(He's fucking my mouth! he's being too gross but... I haven't been this horny in a long time.. right now.."
                Leyna "..right now I just want to be fucked  for both of them)"
                YoungVillager3 "UOOo I'm coming!"
                YoungVillager "Yeah, me too!"
                stop bgs fadeout 1
                $ flash_screen(wait=True)
                scene blackmail15
                play sound "audio/Poison.ogg" volume 0.9 noloop
                $ flash_screen(wait=True)
                Leyna "!!!"
                YoungVillager "That was... incredible! I could go on all night!"
                YoungVillager3 "Yeah! Too bad we didn't fuck her, but some other time!"
                Leyna "There won't be another time! bring me something to clean me up."
                scene black with dissolve
                show blackmail16 with dissolve
                Johan "Here we are with the drink... ? Leyna? are you ok?"
                Leyna "Oh yes, I'm fine.. We were.."
                YoungVillager "W-we were looking for beers too, never too much hahaha, but we didn't find anything"
                Johan "(Leyna seems a little alarmed about something... it's just my imagination)"
                Leyna "..."
                Johan "Well, shall we drink a little, guys?"
                YoungVillager "Say no more! I'm very dry, I need a drink"
                Johan "Anyone would say you've done a marathon hahaha"
                YoungVillager "Yeah hahaha pretty much!"
                Leyna "..."
                scene black with dissolve
                hide blackmail15
                hide blackmail16
                # fade in
            if switch("corruption_low"):
                scene blackmail3
                YoungVillager "If I may say so, Leyna, you look very sexy today"
                Leyna "Oh, thanks"
                if bottle_event == 3:
                    YoungVillager "No, thanks to you, I must have jerked off ten times thinking about when you showed us your tits the other night"
                    Leyna "I don't think that needs to be said...."
                    YoungVillager "Oh yeah, of course I guess you're right, sorry"
                scene black with dissolve
                hide blackmail3
                show blackmail2 with dissolve
                "(FEW MOMENTS LATER..)"
                Johan "Well, here we are!"
                YoungVillager "Great, so let's not waste any more time and let's get drinking"
                scene black with dissolve
                hide blackmail2
                # fade in
                scene noblackmail1
                "AFTER A FEW BEERS.."
                YoungVillager "(Wow, leyna is so sexy! she has the perfect body..... damn, it sucks that she came with her husband on vacation!I could.... I'm sure I could"
                "... seduce her in some way.... I have to think about it, there has to be some way for me to lose my virginity with this goddess)"
                YoungVillager3 ".... and I saw his dick and he had it like a peanut hhahahahaaha"
                Leyna "Hahaahaha"
                YoungVillager "(Wait, is he talking about me?) hey asshole! We were 8 years old! Now I've got it so much bigger than you!"
                YoungVillager3 "In your dreams maybe! if you want we can compare right now"
                Johan "Hahahahaha hey come on guys no need...!!!!"
                scene noblackmail2
                Leyna "Wow!"
                YoungVillager "See, mine is bigger than yours!"
                YoungVillager3 "Well I see mine bigger! ... plus it's cold! Give me a second and you'll see how much bigger it is!"
                Johan "Come on guys! Stop showing off! There's a lady in front of you, this is no way to behave!"
                YoungVillager "Oh... you're right"
                scene noblackmail3
                YoungVillager3 "Right, Leyna is in front of us... we can ask her! Who has the biggest dick? Me, right?"
                Leyna "W-well! You both have it huge hehehe you don't have to worry so much"
                YoungVillager "OH? So we have it huge eh? Tthank you.... Bigger than Johan's?"
                Leyna "Well,then s..."
                Johan "Hey! You guys are going too far! (Shit, the alcohol is speaking for Leyna again) Keep that in your pants, come on"
                YoungVillager "Hmmm yeah sorry Johan! We stopped already"
                Leyna "...."
                scene black with dissolve
                hide noblackmail3
                # fade in
        "No":
            pass
    return

label GalleryBonfireWithTheYoungBoys_2(menu_choice = None):
    "Bonfire with the young boys"
    "Do you want to see it?"
    menu:
        "Yes":
            scene blackmail1
            YoungVillager "Hey! What's up guys? You going out tonight? Do you want to join us for a drink? We had a great time the other day"
            Johan "Sure, guys, we can stay for a while"
            Leyna "... (Shit, this is the last situation I wanted)"
            scene blackmail2
            YoungVillager2 "We've run out of liquor, but I have a bottle left at home. Johan, will you come with me? So you can carry the bottle around town without me getting caught"
            Johan "Oh, sure, no problem"
            Leyna "Great, I'm coming too"
            Johan "Don’t worry, wait for me here and relax a bit at the bonfire"
            Leyna "Oh... sure..."
            scene black with dissolve
            hide blackmail2
            # fade in
            if switch("corruption_average"):
                scene blackmail3
                YoungVillager "So... what do you think about our festival?"
                Leyna "Mmmm... well, I guess"
                YoungVillager "Ah... great yeah... hey, look at this cool picture"
                Leyna "Well, let's see..!!!!!!!!!!! Th-this is.. H-how?"
                scene blackmail4
                Leyna "WHATTT?!!"
                Leyna "How... where did you get that picture?"
                YoungVillager "I took it... yes, we caught you in the act, you don't want your husband to see this picture, do you?"
                Leyna "What? Of course not!"
                YoungVillager "Well if you don't want that to happen, you will listen to us"
                scene blackmail5
                Leyna "I... what do you want? I don't have much money..."
                YoungVillager "We don't want money, you see, we can't let our friend go around bragging to us about getting a blowjob from a beauty like you"
                YoungVillager "And we're just sitting here... so you know, we want you to do the same to us as you did to him"
                scene blackmail6
                Leyna "HOW? you have so little shame, how dare you? I refuse!"
                YoungVillager "Well, then I guess you don't mind so much... now when your husband gets back I'll show him the picture if you don't mind.."
                scene blackmail7
                Leyna "WAIT! wait... okay... okay damn it..."
                YoungVillager "Great, let's go to the alley"
                Leyna "Wait, right now?  But..."
                YoungVillager "Exactly, right now. And we have to hurry, they'll be right back. You don't want them to catch us in the act, do you?"
                Leyna "(Fucking son of a bitch).... of course"
                YoungVillager "Great, let's get it over with"
                scene blackmail8
                YoungVillager "Well, here we are"
                YoungVillager "Here you go, free buffet ahahaha"
                Leyna "Shut up... (fuck...)"
                scene blackmail9
                Leyna "(I can't believe I'm going to do this again in public)"
                YoungVillager "What are you waiting for? You don't want us to get caught, do you?"
                Leyna "I... okay"
                scene blackmail10
                Leyna "(My god, I don't think I can even fit in my mouth...I have to get this over with fast or it could go terribly wrong)"
                YoungVillager "Come on, don't make me wait any longer, I'm feeling your breath on my cock, don't worry, I'm sure we'll cum in no time"
                scene blackmail11
                YoungVillager "OOoooh! That feels so good, it's so warm in there. Keep it up"
                Leyna "(shut up, don't keep talking please..... why is my body behaving this way? i'm getting horny doing this)"
                YoungVillager "Hey! Don't forget about me, come on, suck my dick"
                Leyna "O..okay.."
                scene blackmail12
                YoungVillager3 "Uoh great, this is the best!"
                Leyna "(Doing this to two guys at the same time on the street...I've never done anything like this... but it feels so good..)"
                Leyna "(.. but, what am I saying? I'm not like this)"
                play sound "audio/Equip2.ogg" volume 0.9 noloop
                scene blackmail13
                Leyna "What are you doing?!"
                YoungVillager "You don't need this hahahaha besides, if I don't see something while you're blowing my friend, we'll never finish"
                YoungVillager3 "Good idea! since the last time you showed them to us,I have not been able to get them out of my head"
                Leyna "I..."
                scene blackmail14
                play bgs "audio/audio follar.ogg" loop volume 0.9
                YoungVillager3 "Who told you to stop sucking my dick? COME ON, GET IT OVER WITH"
                Leyna "Ugh!"
                YoungVillager "Wow! A deep throat! This girl has experience! She looks like a saint but she's a whore!"
                Leyna "(He's fucking my mouth! he's being too gross but... I haven't been this horny in a long time.. right now.."
                Leyna "..right now I just want to be fucked  for both of them)"
                YoungVillager3 "UOOo I'm coming!"
                YoungVillager "Yeah, me too!"
                stop bgs fadeout 1
                $ flash_screen(wait=True)
                scene blackmail15
                play sound "audio/Poison.ogg" volume 0.9 noloop
                $ flash_screen(wait=True)
                Leyna "!!!"
                YoungVillager "That was... incredible! I could go on all night!"
                YoungVillager3 "Yeah! Too bad we didn't fuck her, but some other time!"
                Leyna "There won't be another time! bring me something to clean me up."
                scene black with dissolve
                show blackmail16 with dissolve
                Johan "Here we are with the drink... ? Leyna? are you ok?"
                Leyna "Oh yes, I'm fine.. We were.."
                YoungVillager "W-we were looking for beers too, never too much hahaha, but we didn't find anything"
                Johan "(Leyna seems a little alarmed about something... it's just my imagination)"
                Leyna "..."
                Johan "Well, shall we drink a little, guys?"
                YoungVillager "Say no more! I'm very dry, I need a drink"
                Johan "Anyone would say you've done a marathon hahaha"
                YoungVillager "Yeah hahaha pretty much!"
                Leyna "..."
                scene black with dissolve
                hide blackmail15
                hide blackmail16
                # fade in
            if switch("corruption_low"):
                scene blackmail3
                YoungVillager "If I may say so, Leyna, you look very sexy today"
                Leyna "Oh, thanks"
                if bottle_event == 3:
                    YoungVillager "No, thanks to you, I must have jerked off ten times thinking about when you showed us your tits the other night"
                    Leyna "I don't think that needs to be said...."
                    YoungVillager "Oh yeah, of course I guess you're right, sorry"
                scene black with dissolve
                hide blackmail3
                show blackmail2 with dissolve
                "(FEW MOMENTS LATER..)"
                Johan "Well, here we are!"
                YoungVillager "Great, so let's not waste any more time and let's get drinking"
                scene black with dissolve
                hide blackmail2
                # fade in
                scene noblackmail1
                "AFTER A FEW BEERS.."
                YoungVillager "(Wow, leyna is so sexy! she has the perfect body..... damn, it sucks that she came with her husband on vacation!I could.... I'm sure I could"
                "... seduce her in some way.... I have to think about it, there has to be some way for me to lose my virginity with this goddess)"
                YoungVillager3 ".... and I saw his dick and he had it like a peanut hhahahahaaha"
                Leyna "Hahaahaha"
                YoungVillager "(Wait, is he talking about me?) hey asshole! We were 8 years old! Now I've got it so much bigger than you!"
                YoungVillager3 "In your dreams maybe! if you want we can compare right now"
                Johan "Hahahahaha hey come on guys no need...!!!!"
                scene noblackmail2
                Leyna "Wow!"
                YoungVillager "See, mine is bigger than yours!"
                YoungVillager3 "Well I see mine bigger! ... plus it's cold! Give me a second and you'll see how much bigger it is!"
                Johan "Come on guys! Stop showing off! There's a lady in front of you, this is no way to behave!"
                YoungVillager "Oh... you're right"
                scene noblackmail3
                YoungVillager3 "Right, Leyna is in front of us... we can ask her! Who has the biggest dick? Me, right?"
                Leyna "W-well! You both have it huge hehehe you don't have to worry so much"
                YoungVillager "OH? So we have it huge eh? Tthank you.... Bigger than Johan's?"
                Leyna "Well,then s..."
                Johan "Hey! You guys are going too far! (Shit, the alcohol is speaking for Leyna again) Keep that in your pants, come on"
                YoungVillager "Hmmm yeah sorry Johan! We stopped already"
                Leyna "...."
                scene black with dissolve
                hide noblackmail3
                # fade in
        "No":
            pass
    return

label GalleryHideAndSeek_1(menu_choice = None):
    "Hide and seek"
    "Do you want to see it?"
    menu:
        "Yes":
            if jail == 1:
                scene black with dissolve
                show revenge1 with dissolve
                Prisoner "... wait a second, that's her? I can't believe it. Well, she's going to find out, she's going to pay me back for the other day"
                scene revenge2
                Prisoner "I caught you bitch! Remember me?"
                Leyna "You... you are the prisoner from the other day! The one who tried to..."
                Prisoner "Exactly! The one who tried to spend some quality time with you! But you were too good for me, right?"
                Prisoner "Because of you I got locked up a lot more than I should have! And you're going to pay for it! You have to take responsibility for your actions!"
                Leyna "No! Stop!"
                Prisoner "You want me to stop? You fucking bitch! Now you'll see!"
                menu:
                    "Fight back!":
                        scene revenge3
                        play sound "audio/Blow3.ogg" volume 0.9 noloop
                        Leyna "YOU MOTHER FUCKER!"
                        Prisoner "Uogh!!!"
                        scene pantallanegro:
                            xsize 979
                            ysize 720
                        play sound "audio/Run.ogg" volume 0.9 noloop
                        pause
                        scene black with dissolve
                        hide pantallanegro
                        # fade in
                    "Surrender!":
                        Leyna "Ple-please do whatever you want, but don't hurt me"
                        scene revenge4
                        Prisoner "You stay still and let me do my job. Let's see those tits! I didn't get a good look at them the other day!"
                        "Prisioner: Wow! You have the biggest, most perfect tits I've ever seen!"
                        Prisoner "you couldn't expect anything to happen to you, walking around in these clothes, could you? what a bitch you are!"
                        Leyna "Please... don't do it"
                        scene revenge5
                        Prisoner "Shut up, let me touch them...incredible, you have an incredible body and now it's mine, I'm going to enjoy it to the fullest"
                        Leyna "!!!"
                        Prisoner "Wow your nipples are getting hard! You're such a bitch, you say no, but your body is telling me yes!"
                        Leyna "I--I.."
                        scene revenge6
                        Prisoner "And these panties you're wearing? who are they for? They barely cover anything!"
                        Leyna "....!!!"
                        Prisoner "Turn around!"
                        Leyna "No, wait!"
                        scene revenge7
                        Prisoner "It couldn't be any other way! the perfect ass! and... I can't believe it, you're soaking wet down there!"
                        Prisoner "Well I'm going to help you! I'm going to fuck you right here and right now you slut!"
                        Leyna "!!!"
                        Leyna "W-wait a second please!"
                        Prisoner "No way, I can't wait a second to fuck a goddess like you"
                        Leyna "(A-a goddess?.... why do I like this man talking to me like this? Why I'm enjoying this?)"
                        scene revenge8
                        Leyna "OOOhhhh it's- it's too big to fit!"
                        Prisoner "Wow you are making me even hornier than I was... besides, it's going to fit,it went in without a problem"
                        Leyna "Hmmmmm I.. I...."
                        Prisoner "Come on, you're wishing for it. I'm sorry, you want me to put it all the way in, don't you? You know, you just have to ask me, I want you to tell me"
                        Leyna "No...I would never..."
                        Prisoner "I'm going to stick it in you a little bit more, you want me to fuck you, say it, confess it now and I will do it"
                        Leyna "I... fuck me..."
                        Prisoner "What? I didn't hear you!"
                        Leyna "... fuck me.... please fuck me!"
                        Prisoner "Perfect! All you had to do was ask me, bitch!"
                        play music "audio/audio follar.ogg" loop volume 0.9
                        image revenge_webm = Movie(play="movies/revenge.webm", loop=True, size=(816, 459), ypos=83)
                        scene revenge_webm
                        pause
                        Leyna "HARDER! HARDER! FUCK MEEEE!!"
                        Prisoner "Oh! I'm going to cum! I'm going to cum!"
                        Leyna "Wait!!!! Not inside please!"
                        stop music fadeout 1
                        $ flash_screen(wait=True)
                        scene revenge9
                        play sound "audio/Poison.ogg" volume 0.9 noloop
                        $ flash_screen(wait=True)
                        Prisoner "OOOhhhhhh.... nice, it's been years since I've fucked.. and never with a goddess like you"
                        Leyna "This... this shouldn't have happened"
                        Prisoner "I'm sure you've never been fucked like this before, not even by your limp dick of a husband!"
                        scene revenge10
                        Leyna "Shut up... leave me alone, get out of here please!"
                        Prisoner "Tch! As you wish... if you ever want to come again, I'll be in town"
                        Leyna "...."
                        scene black with dissolve
                        hide revenge10
                        # fade in
            if jail == 0:
                scene black with dissolve
                show revenge1 with dissolve
                Prisoner "Wait a second... Who is that goddess? And look how she's dressed! Being here alone..."
                Prisoner "Oh I get it, one of my friends told me something about this... cruising or something like that right? I'm sure she wants to fuck"
                Prisoner "Great, I can't believe I'm so lucky. I haven't fuck in years"
                scene revenge2
                Prisoner "I caught you bitch! I didn't know there was such a horny girl in town, but I understand you, you just need a little action uh?"
                Leyna "Wha-what are you talking about? Please let go of me"
                Prisoner "Ohh I see, so you're into role playing too? Fine for me Come on bitch, come here I'm gonna stick it all the way in you"
                Leyna "No! Stop!"
                Prisoner "You want me to stop? You fucking bitch! Now you'll see!"
                menu:
                    "Fight back!":
                        scene revenge3
                        play sound "audio/Blow3.ogg" volume 0.9 noloop
                        Leyna "YOU MOTHER FUCKER!"
                        Prisoner "Uogh!!!"
                        scene pantallanegro:
                            xsize 979
                            ysize 720
                        play sound "audio/Run.ogg" volume 0.9 noloop
                        pause
                        scene black with dissolve
                        hide pantallanegro
                        # fade in
                    "Surrender!":
                        Leyna "Ple-please do whatever you want, but don't hurt me"
                        scene revenge4
                        Prisoner "You stay still and let me do my job. Let's see those tits!"
                        "Prisioner: Wow! You have the biggest, most perfect tits I've ever seen!"
                        Prisoner "you couldn't expect anything to happen to you, walking around in these clothes, could you? what a bitch you are!"
                        Leyna "Please... don't do it"
                        scene revenge5
                        Prisoner "Shut up, let me touch them...incredible, you have an incredible body and now it's mine, I'm going to enjoy it to the fullest"
                        Leyna "!!!"
                        Prisoner "Wow your nipples are getting hard! You're such a bitch, you say no, but your body is telling me yes!"
                        Leyna "I--I.."
                        scene revenge6
                        Prisoner "And these panties you're wearing? who are they for? They barely cover anything!"
                        Leyna "....!!!"
                        Prisoner "Turn around!"
                        Leyna "No, wait!"
                        scene revenge7
                        Prisoner "It couldn't be any other way! the perfect ass! and... I can't believe it, you're soaking wet down there!"
                        Prisoner "Well I'm going to help you! I'm going to fuck you right here and right now you slut!"
                        Leyna "!!!"
                        Leyna "W-wait a second please!"
                        Prisoner "No way, I can't wait a second to fuck a goddess like you"
                        Leyna "(A-a goddess?.... why do I like this man talking to me like this? Why I'm enjoying this?)"
                        scene revenge8
                        Leyna "OOOhhhh it's- it's too big to fit!"
                        Prisoner "Wow you are making me even hornier than I was... besides, it's going to fit,it went in without a problem"
                        Leyna "Hmmmmm I.. I...."
                        Prisoner "Come on, you're wishing for it. I'm sorry, you want me to put it all the way in, don't you? You know, you just have to ask me, I want you to tell me"
                        Leyna "No...I would never..."
                        Prisoner "I'm going to stick it in you a little bit more, you want me to fuck you, say it, confess it now and I will do it"
                        Leyna "I... fuck me..."
                        Prisoner "What? I didn't hear you!"
                        Leyna "... fuck me.... please fuck me!"
                        Prisoner "Perfect! All you had to do was ask me, bitch!"
                        play music "audio/audio follar.ogg" loop volume 0.9
                        image revenge_webm = Movie(play="movies/revenge.webm", loop=True, size=(816, 459), ypos=83)
                        scene revenge_webm
                        pause
                        Leyna "HARDER! HARDER! FUCK MEEEE!!"
                        Prisoner "Oh! I'm going to cum! I'm going to cum!"
                        Leyna "Wait!!!! Not inside please!"
                        stop music fadeout 1
                        $ flash_screen(wait=True)
                        scene revenge9
                        play sound "audio/Poison.ogg" volume 0.9 noloop
                        $ flash_screen(wait=True)
                        Prisoner "OOOhhhhhh.... nice, it's been years since I've fucked.. and never with a goddess like you"
                        Leyna "This... this shouldn't have happened"
                        Prisoner "I'm sure you've never been fucked like this before, not even by your limp dick of a husband! ... if you have one"
                        scene revenge10
                        Leyna "Shut up... leave me alone, get out of here please!"
                        Prisoner "Tch! As you wish... if you ever want to come again, I'll be in town"
                        Leyna "...."
                        scene black with dissolve
                        hide revenge10
                        # fade in
        "No":
            pass
    return

label GalleryHideAndSeek_2(menu_choice = None):
    "Hide and seek"
    "Do you want to see it?"
    menu:
        "Yes":
            if jail == 1:
                scene black with dissolve
                show revenge1 with dissolve
                Prisoner "... wait a second, that's her? I can't believe it. Well, she's going to find out, she's going to pay me back for the other day"
                scene revenge2
                Prisoner "I caught you bitch! Remember me?"
                Leyna "You... you are the prisoner from the other day! The one who tried to..."
                Prisoner "Exactly! The one who tried to spend some quality time with you! But you were too good for me, right?"
                Prisoner "Because of you I got locked up a lot more than I should have! And you're going to pay for it! You have to take responsibility for your actions!"
                Leyna "No! Stop!"
                Prisoner "You want me to stop? You fucking bitch! Now you'll see!"
                menu:
                    "Fight back!":
                        scene revenge3
                        play sound "audio/Blow3.ogg" volume 0.9 noloop
                        Leyna "YOU MOTHER FUCKER!"
                        Prisoner "Uogh!!!"
                        scene pantallanegro:
                            xsize 979
                            ysize 720
                        play sound "audio/Run.ogg" volume 0.9 noloop
                        pause
                        scene black with dissolve
                        hide pantallanegro
                        # fade in
                    "Surrender!":
                        Leyna "Ple-please do whatever you want, but don't hurt me"
                        scene revenge4
                        Prisoner "You stay still and let me do my job. Let's see those tits! I didn't get a good look at them the other day!"
                        "Prisioner: Wow! You have the biggest, most perfect tits I've ever seen!"
                        Prisoner "you couldn't expect anything to happen to you, walking around in these clothes, could you? what a bitch you are!"
                        Leyna "Please... don't do it"
                        scene revenge5
                        Prisoner "Shut up, let me touch them...incredible, you have an incredible body and now it's mine, I'm going to enjoy it to the fullest"
                        Leyna "!!!"
                        Prisoner "Wow your nipples are getting hard! You're such a bitch, you say no, but your body is telling me yes!"
                        Leyna "I--I.."
                        scene revenge6
                        Prisoner "And these panties you're wearing? who are they for? They barely cover anything!"
                        Leyna "....!!!"
                        Prisoner "Turn around!"
                        Leyna "No, wait!"
                        scene revenge7
                        Prisoner "It couldn't be any other way! the perfect ass! and... I can't believe it, you're soaking wet down there!"
                        Prisoner "Well I'm going to help you! I'm going to fuck you right here and right now you slut!"
                        Leyna "!!!"
                        Leyna "W-wait a second please!"
                        Prisoner "No way, I can't wait a second to fuck a goddess like you"
                        Leyna "(A-a goddess?.... why do I like this man talking to me like this? Why I'm enjoying this?)"
                        scene revenge8
                        Leyna "OOOhhhh it's- it's too big to fit!"
                        Prisoner "Wow you are making me even hornier than I was... besides, it's going to fit,it went in without a problem"
                        Leyna "Hmmmmm I.. I...."
                        Prisoner "Come on, you're wishing for it. I'm sorry, you want me to put it all the way in, don't you? You know, you just have to ask me, I want you to tell me"
                        Leyna "No...I would never..."
                        Prisoner "I'm going to stick it in you a little bit more, you want me to fuck you, say it, confess it now and I will do it"
                        Leyna "I... fuck me..."
                        Prisoner "What? I didn't hear you!"
                        Leyna "... fuck me.... please fuck me!"
                        Prisoner "Perfect! All you had to do was ask me, bitch!"
                        play music "audio/audio follar.ogg" loop volume 0.9
                        image revenge_webm = Movie(play="movies/revenge.webm", loop=True, size=(816, 459), ypos=83)
                        scene revenge_webm
                        pause
                        Leyna "HARDER! HARDER! FUCK MEEEE!!"
                        Prisoner "Oh! I'm going to cum! I'm going to cum!"
                        Leyna "Wait!!!! Not inside please!"
                        stop music fadeout 1
                        $ flash_screen(wait=True)
                        scene revenge9
                        play sound "audio/Poison.ogg" volume 0.9 noloop
                        $ flash_screen(wait=True)
                        Prisoner "OOOhhhhhh.... nice, it's been years since I've fucked.. and never with a goddess like you"
                        Leyna "This... this shouldn't have happened"
                        Prisoner "I'm sure you've never been fucked like this before, not even by your limp dick of a husband!"
                        scene revenge10
                        Leyna "Shut up... leave me alone, get out of here please!"
                        Prisoner "Tch! As you wish... if you ever want to come again, I'll be in town"
                        Leyna "...."
                        scene black with dissolve
                        hide revenge10
                        # fade in
            if jail == 0:
                scene black with dissolve
                show revenge1 with dissolve
                Prisoner "Wait a second... Who is that goddess? And look how she's dressed! Being here alone..."
                Prisoner "Oh I get it, one of my friends told me something about this... cruising or something like that right? I'm sure she wants to fuck"
                Prisoner "Great, I can't believe I'm so lucky. I haven't fuck in years"
                scene revenge2
                Prisoner "I caught you bitch! I didn't know there was such a horny girl in town, but I understand you, you just need a little action uh?"
                Leyna "Wha-what are you talking about? Please let go of me"
                Prisoner "Ohh I see, so you're into role playing too? Fine for me Come on bitch, come here I'm gonna stick it all the way in you"
                Leyna "No! Stop!"
                Prisoner "You want me to stop? You fucking bitch! Now you'll see!"
                menu:
                    "Fight back!":
                        scene revenge3
                        play sound "audio/Blow3.ogg" volume 0.9 noloop
                        Leyna "YOU MOTHER FUCKER!"
                        Prisoner "Uogh!!!"
                        scene pantallanegro:
                            xsize 979
                            ysize 720
                        play sound "audio/Run.ogg" volume 0.9 noloop
                        pause
                        scene black with dissolve
                        hide pantallanegro
                        # fade in
                    "Surrender!":
                        Leyna "Ple-please do whatever you want, but don't hurt me"
                        scene revenge4
                        Prisoner "You stay still and let me do my job. Let's see those tits!"
                        "Prisioner: Wow! You have the biggest, most perfect tits I've ever seen!"
                        Prisoner "you couldn't expect anything to happen to you, walking around in these clothes, could you? what a bitch you are!"
                        Leyna "Please... don't do it"
                        scene revenge5
                        Prisoner "Shut up, let me touch them...incredible, you have an incredible body and now it's mine, I'm going to enjoy it to the fullest"
                        Leyna "!!!"
                        Prisoner "Wow your nipples are getting hard! You're such a bitch, you say no, but your body is telling me yes!"
                        Leyna "I--I.."
                        scene revenge6
                        Prisoner "And these panties you're wearing? who are they for? They barely cover anything!"
                        Leyna "....!!!"
                        Prisoner "Turn around!"
                        Leyna "No, wait!"
                        scene revenge7
                        Prisoner "It couldn't be any other way! the perfect ass! and... I can't believe it, you're soaking wet down there!"
                        Prisoner "Well I'm going to help you! I'm going to fuck you right here and right now you slut!"
                        Leyna "!!!"
                        Leyna "W-wait a second please!"
                        Prisoner "No way, I can't wait a second to fuck a goddess like you"
                        Leyna "(A-a goddess?.... why do I like this man talking to me like this? Why I'm enjoying this?)"
                        scene revenge8
                        Leyna "OOOhhhh it's- it's too big to fit!"
                        Prisoner "Wow you are making me even hornier than I was... besides, it's going to fit,it went in without a problem"
                        Leyna "Hmmmmm I.. I...."
                        Prisoner "Come on, you're wishing for it. I'm sorry, you want me to put it all the way in, don't you? You know, you just have to ask me, I want you to tell me"
                        Leyna "No...I would never..."
                        Prisoner "I'm going to stick it in you a little bit more, you want me to fuck you, say it, confess it now and I will do it"
                        Leyna "I... fuck me..."
                        Prisoner "What? I didn't hear you!"
                        Leyna "... fuck me.... please fuck me!"
                        Prisoner "Perfect! All you had to do was ask me, bitch!"
                        play music "audio/audio follar.ogg" loop volume 0.9
                        image revenge_webm = Movie(play="movies/revenge.webm", loop=True, size=(816, 459), ypos=83)
                        scene revenge_webm
                        pause
                        Leyna "HARDER! HARDER! FUCK MEEEE!!"
                        Prisoner "Oh! I'm going to cum! I'm going to cum!"
                        Leyna "Wait!!!! Not inside please!"
                        stop music fadeout 1
                        $ flash_screen(wait=True)
                        scene revenge9
                        play sound "audio/Poison.ogg" volume 0.9 noloop
                        $ flash_screen(wait=True)
                        Prisoner "OOOhhhhhh.... nice, it's been years since I've fucked.. and never with a goddess like you"
                        Leyna "This... this shouldn't have happened"
                        Prisoner "I'm sure you've never been fucked like this before, not even by your limp dick of a husband! ... if you have one"
                        scene revenge10
                        Leyna "Shut up... leave me alone, get out of here please!"
                        Prisoner "Tch! As you wish... if you ever want to come again, I'll be in town"
                        Leyna "...."
                        scene black with dissolve
                        hide revenge10
                        # fade in
        "No":
            pass
    return

label GalleryRiverNight_1(menu_choice = None):
    "River Night"
    "Do you want to see it?"
    menu:
        "Yes":
            scene pantallanegro:
                xsize 979
                ysize 720
            "LATER IN THE RIVER ..."
            Villager "Come on, everyone without clothes, otherwise the goddess will get angry"
            Johan "hahahahahaha okay let's go"
            Leyna "Okay, but give me one more shot of beer first hahaha"
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            scene rioleyna1
            Leyna "Ahhh how nice, how refreshing... it may be the alcohol but the truth is that being like this without worrying so much is very ... liberalizing"
            Johan "Right? Now I feel a little bad for being angry in the past"
            scene rioleyna2
            Villager "Yesssss this is all tradition here! We have no problem seeing each other naked!"
            Leyna "It's certainly very different from how we behave in the city, but I guess it's cool"
            Villager2 "Hahahahaha man, here we are all happy to see each other, especially you Leyna! What a great body!"
            Johan "hahhaha you bet! Eeven though she is my wife, I still can't get used to seeing her like this"
            scene rioleyna3
            Villager2 "Dude! You sure are glad to see Leyna!"
            Johan "Hahahaha"
            Leyna "WOW! what a big dick (!!!!!!) fu-fuck did I say that out loud? Sorry...."
            Leyna "When I drink too much I'm not myself"
            Johan "Hahaha...(Wow I didn't expect that comment from Leyna ... even though she told the truth I can't help but feel jealous... I have a weird feeling in my stomach"
            "looking at this situation... I don't know if it's because of the alcohol but... well, don't think about it too much Johan)"
            scene rioleyna4
            Villager2 "Well Leyna don't worry here we are all friends and there is trust, isn't it Johan?"
            Johan "Of course! You can admire my wife's beauty all you want! After all it's only for me hahahaha"
            Villager2 "But man, don't tell us that, we'll die of envy! hahahaha"
            Leyna "Well, I think I'm going to take a bath guys!"
            scene rioleyna5
            Villager "Wait, you're going to go like that? You should strip completely naked or you'll get your panties wet and get cold"
            Leyna "I'm just a little embarrassed, guys"
            Villager "Don't worry, we are all adults here!"
            Villager2 "Yes, we're not going to see anything we haven't seen before"
            Leyna "I guess you are right"
            scene pantallanegro:
                xsize 979
                ysize 720
            Johan "W-well, I don't know..."
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            Johan "!!!!"
            Villager "Wow! Awesome! Leyna do you exercise or something?"
            Leyna "Well... I do go to the gym every week"
            Villager "Very well, let's see!"
            play sound "audio/Fall.ogg" volume 0.9 noloop
            Leyna "!!!"
            scene rioleyna6
            Villager "It really shows! You have a great ass! And what kind of exercises do you do at the gym?"
            Johan "Hey hey!"
            Villager "Some cycling perhaps?"
            scene rioleyna7
            Leyna "Y-yes some biking... and some rubber exercises"
            Johan "(They're ignoring me? It's like I'm not even here... and Leyna...)"
            Johan "(The penis of this man we met just is soo close to Leyna's pussy)"
            Villager2 "Wow! May I see it?"
            scene rioleyna8
            Villager "Of course, look at her thighs! She's a real sportswoman!"
            Leyna "hm!"
            Villager2 "YES... that ... firmer thighs!"
            scene rioleyna9
            Villager2 "You could teach us some exercise, the truth is that these last years I have neglected a lot my physique and I'm getting a lot of belly hahahaa"
            Villager "Yes! With this great body you have to know some really good exercises!"
            Leyna "W-well, you could..."
            Johan "(This situation is getting too long for my taste... but after the little speech about trust I said before, I don't want to yell at them now)"
            scene rioleyna10
            Villager2 "What? I'm sorry, but you speak very softly and I can't hear you"
            Leyna "!!! I.... I..."
            Johan "Ahem well Leyna... shall we take a bath?"
            scene rioleyna11
            Leyna "Y-yeah right (for a second I forgot Johan is here, thank good from where he is, he can't see that this man's penis is pressed on me)"
            Villager "Oh! yeah, we'd better go for a swim"
            Villager2 "Yes, you're right hahaha sorry Johan!"
            scene rioleyna12
            Leyna "!!!Oooh!"
            Villager2 "Oops! I slipped! We almost fell down Leyna! hahaha"
            Villager2 "Uf... my back is... my back is bad, hold me for a second"
            Johan "??? Are you okay?"
            Villager2 "Oh yes yes, just give me a second"
            scene rioleyna13
            Leyna "hmmmmm Ahhh... I... I..."
            Villager "What's wrong Leyna? Did you hurt yourself?"
            Leyna "(Johan is right there... and this man has stuck his dick all the way in... in front of my husband...)"
            Johan "Leyna?"
            scene rioleyna14
            "plop!"
            Villager2 "There you go... hahahah it's just that my back always gives me problems, everything ok Leyna? Sorry I fell on you"
            Leyna "(Heavy breathing) Ah ah ah ah.... yes ... all right... come on Johan... let's go for a swim"
            Johan "Sure! (for a second I thought that... anyway, it's just my imagination...)"
            scene black with dissolve
            hide rioleyna14
            # fade in
        "No":
            pass
    return

label GalleryFourthSessionWithThePhotographer_1(menu_choice = None):
    "Fourth session with the photographer"
    "Do you want to see it?"
    menu:
        "Yes":
            scene pantallanegro:
                xsize 979
                ysize 720
            "A FEW MOMENTS LATER..."
            Leyna "Here? this is a bit public, isn't it?"
            Villager "That's fine for me"
            Villager "For me neither, it's not much different from the festival"
            OldMan "Relax, No one comes through here"
            Leyna "If you say so..."
            OldMan "Well... everyone in your positions let's get started"
            scene mascara1
            OldMan "Perfect, you look great in the costumes... Now pose as we said before"
            Leyna "Yeah..."
            pause
            scene mascara2
            OldMan "Great!"
            OldMan "And now show us that perfect ass, and you two come closer, she doesn't bite"
            Leyna "..."
            pause
            scene mascara3
            OldMan "Perfect, very sexy Leyna, you are made for this, I don't know how you didn't think of being a model before"
            Leyna "I... thank you very much"
            Villager "YES, she has the best ass I've seen in a long time"
            Villager2 "Are you sure you're married? I would take you right now and..."
            Leyna "I get it..."
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "Well guys, next position"
            pause
            scene mascara4
            OldMan "NICE!"
            Villager "Yeah! great... what a pair of tits"
            Villager2 "YES, they are perfect"
            Leyna "...."
            Leyna "(They can't stop saying those kinds of things? I should be used to it in this town, but I can't help but getting a little excited by this attention)"
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "All right, now the good stuff starts, let's go"
            pause
            scene mascara5
            OldMan "Very good hold this way a little more"
            Villager "All the time you want, I could be like this all my life... how soft her tits are, I could come right now"
            Leyna "What?"
            Villager "Hahaha nothing, it was a joke"
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "Alright guys let's move on to the next pose"
            pause
            scene mascara6
            OldMan "Perfect..."
            Villager2 "Wow your ass is so close... I would kill to fuck you right now, as soon as I get home I'm going to masturbate with this in mind"
            Villager "Me too! You're perfect, wouldn't you like to leave your husband and come with me? I'm sure he doesn't have it as big as mine"
            Villager2 "Hey! get in line"
            Leyna "Guys... you don't have to say this kind of stuff please"
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            Villager "Come on... you should be used to it by now... plus you sure do love to be told these things. Why are you doing this kind of work if it is not the case?"
            Leyna "No I..."
            OldMan "Come on guys next position"
            Leyna "..."
            pause
            scene mascara7
            Villager "Oh this is perfect, so warm!"
            Villager2 "That's it, grab my dick, this is incredible"
            OldMan "Come on guys control yourselves"
            Villager "Yes, sorry"
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "Okay, the last position"
            pause
            scene mascara8
            OldMan "Great very sexy Leyna!"
            Leyna "...."
            Villager "It's definitely the best job I've ever had"
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "Okay, hold on a little longer, I'm going to get a little closer"
            Leyna "!!!"
            pause
            scene mascara9
            OldMan "Right, this angle is perfect!"
            Villager "Leyna right? I hope to see you at the festival and we can do another session, you and me alone"
            Leyna "Not a good idea, Sorry"
            OldMan "NO! it's a great idea, I'll talk to the magazine and see if they are interested"
            Leyna "In front of everybody? my husband..."
            OldMan "Don't worry, we will figure something out"
            Leyna "...."
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "Well guys we are done, great job! We will talk these days to see if we can make another session"
            Villager "Yes! I am looking forward to it"
            Villager2 "And me! it's been a lot of fun, pass me the pictures when you can, I'd like to have them!"
            OldMan "Of course"
            Leyna "(This has been a mistake? I hope Johan doesn't find out about this....)"
            scene black with dissolve
            hide mascara9
            # fade in
        "No":
            pass
    return

label GalleryHotspringsFlashback_1(menu_choice = None):
    "Hotsprings flashback"
    "Do you want to see it?"
    menu:
        "yes":
            scene black with dissolve
            show hotspringsjuntos6 with dissolve
            "THE LAST DAY LEYNA WENT TO WORK..."
            Villager "Hey... You're the new girl working here, right?"
            Leyna "Hmmm yes, it's me, do you need anything?"
            Villager "Yes, my friend and I have a problem, come with us and we'll show you, it's a little delicate"
            Leyna "Su-sure"
            scene flashback1
            Leyna "Tell me, what is the problem?"
            Villager "Well, you tell me!"
            Leyna "What?"
            Villager "As you heard!  explain to me why you have the facilities in such a bad condition, I don't know what kind of weeds you put in the water but..."
            Villager "I've got a rash! look! this is all your fault! especially yours as you're the one in charge of this!"
            Villager "I guess I'll have to talk to the manager and discuss your future in this job"
            Leyna "I-I, please don't! (I haven't been paid for the photo shoots yet...) I need the money... please... how can I make it up to you?"
            Villager "(I can't believe this is working!).... Well... if you get like that... I guess you could make it up to me..."
            Leyna "??? Sure! Tell me what do you need..."
            Villager "First of all, I want you to see what you've done! look closely at the rash I got here!"
            scene flashback2
            Villager "That's right, get down!"
            Leyna "(Do I always have to end up with someone's cock so close to my face?)... n-not seeing anything"
            Villager "Ehm... of course! because it's not there! it's here!"
            scene flashback3
            play sound "audio/Jump2.ogg" volume 0.9 noloop
            Leyna "AH!!"
            Villager "Do you see it now?"
            Leyna "(I still don't see anything, but I'd better play along so that this is over as soon as possible) Yes, I see it, Sorry, it's my fault"
            Leyna "(This is so humiliating...)"
            Villager "Exactly... I was thinking of talking to your manager! but seeing that you have recognized your mistakes and that you are willing to help us with this..."
            Villager "We can fix it right now! you only have to do one thing..."
            Leyna "Tell me..."
            Villager "Kiss me down there, one kiss is enough for me!"
            Leyna "A-a kiss? There? I..."
            Villager2 "Yes! and if I were you I'd hurry up, with how full this place is today they could see us at any moment!"
            Leyna "(!!! shit! he's right and... and Johan is on the other side of these curtains...if he would see me in this situation...  I don't know what would happen)"
            Leyna "Okay..."
            scene flashback4
            Villager "That's right, good girl"
            Villager2 "(What a fucker! Now I want some too.... Hehehehe I have an idea)"
            Villager2 "Oh boy, you've had a bath too, haven't you, girl? I'm the town doctor and I can see you've got a little problem down there too"
            Leyna "???"
            Villager2 "Yes, this looks bad, I'm going to inspect you a little bit..."
            scene flashback5
            play bgs "audio/audio follar.ogg" loop volume 0.9
            Leyna "Aahh..."
            Villager "You see? we all help each other here hahahaha"
            Villager2 "Exactly! and it looks like I'm helping you out quite a bit hehehe! you're dripping"
            pause
            scene flashback6
            stop bgs fadeout 1
            Leyna "Ah ah ah ah... D-don't keep going... (We could be seen at any moment... I can't go on with this... Johan is right there... but it feels soooo good)"
            if switch("infusion"):
                Leyna "...(I can't help it, I just want it to go on a little longer... I need it or I'll go crazy...)"
                scene flashback7
                Villager2 "I'm going to inspect you a little more thoroughly, sweetie..."
                Leyna "I... we shouldn't... my husband..."
                Villager2 "Oh... it will only take a few minutes, don't worry, it won't take long at all"
                Leyna "!!!"
                pause
                scene flashback8
                Villager2 "That's it...that's it, all the way to the deep end very good... wow You're really tight down there... You needed this, huh?"
                Leyna "Aahhh... (My God it's huge... it's going to break me in half... )... Yeah? ah ah ah"
                Villager "(What a son of a bitch, I could have thought of that myself...)"
                Villager2 "All right, ready? I'm going to help you really good"
                pause
                scene flashback9
                play bgs "audio/audio follar.ogg" loop volume 0.9
                Leyna "AH! AH! AH!"
                Villager2 "That's it! do you like it? you don't need to tell me I know you love it, bitch!"
                Leyna "Hmmmm!! YES YES!"
                Villager "Wow, You were right, this girl is a real slut"
                Villager2 "I told you! A girl dressed like that surrounded by men is just begging to be fucked!"
                Leyna "N-no! (Why does it make me so horny to be talked to like that? I would never...) ... AAAH!!! HMMM..."
                Villager2 "What's wrong? Your husband doesn't fuck you like he should? I'm sure that's it... well, don't worry, we'll take care of you, slut!"
                Leyna "S-stop... I... Ah ah ah!"
                pause
                scene flashback10
                play bgs "audio/audio follar.ogg" loop volume 0.9
                Villager3 "Hey, you wouldn't happen to have any spare towels lying around, would you? FUCK! WHAT THE FUCK IS GOING ON?"
                stop bgs fadeout 1
                Leyna "!!!"
                Villager "!!!! Oh Shit"
                Villager2 "Shit..."
                Leyna "Get off of me NOW!"
                "vILLAGER 2: Tch... Yeah yeah..."
                scene black with dissolve
                hide flashback10
                # fade in
            if not switch("infusion"):
                "lEYNA: Sto-stop... please stop..."
                Villager2 "What? no way, I'll help you right away and you'll be much better"
                Leyna "N-NO! I've done what you wanted, leave me alone! I have to keep working"
                Villager2 "Fuck... okay as you wish...."
                scene black with dissolve
                # fade in
        "No":
            pass
    return

label GalleryPhotoShootTogether_1(menu_choice = None):
    "photo shoot together"
    "Do you want to see it?"
    menu:
        "Yes":
            scene black with dissolve
            show fotoerotica1 with dissolve
            "A FEW MOMENTS LATER"
            Johan "(Fuck, I'm already regretting this..... well I'm here and I can control that nothing gets out of hand)"
            OldMan "Well, Leyna, have you already changed? perfect, please place yourself there"
            Johan "!!! Wow... (Why am I surprised? after all, I know what we came for!)"
            scene fotoerotica2
            OldMan "Sexy as always Leyna, that outfit looks perfect on you!"
            Leyna "Th-Thanks..."
            Johan "(It's true that she looks very sexy in those clothes...)"
            OldMan "I know you're a little nervous but you have to relax, you know, smile a little and pose for me, you're going to do great"
            Leyna "Yes..."
            scene fotoerotica3
            Leyna "Is this good?"
            OldMan "That's perfect Leyna"
            Johan "So far so good... God, couldn't it be like this all the time? I'm getting on my nerves and it hasn't even started yet!)"
            play sound "audio/Key.ogg" volume 0.9 noloop
            $ flash_screen(wait=True)
            OldMan "Perfect, let's move on to the next position"
            scene fotoerotica4
            OldMan "Keep up the good work Leyna you are doing very well"
            Leyna "Thanks"
            Johan "(She is much more relaxed than in the hotsprings, she even seems to be... enjoying it)"
            play sound "audio/Key.ogg" volume 0.9 noloop
            $ flash_screen(wait=True)
            scene fotoerotica5
            OldMan "Wow, super sexy, love it!"
            Leyna "Hahahaha"
            Johan "(Unbelievable, I'm even getting an erection with all this, if I were a teenager I'd go crazy to get pictures of Leyna...)"
            Johan "(I guess that's why the magazine loves it so much... all the wanker kids will be buying it)"
            play sound "audio/Key.ogg" volume 0.9 noloop
            $ flash_screen(wait=True)
            scene pantallanegro:
                xsize 816
                ysize 600
            OldMan "Perfect Leyna, we have finished with the solo poses"
            Leyna "..."
            OldMan "Now the boy with whom you will do the rest of the poses will come in"
            OldMan "Go ahead, boy, you can come in now"
            Leyna "!!!"
            Johan "(Fuck... the guy is huge... My stomach is turning...)"
            OldMan "Okay get in there with her"
            scene fotoerotica6
            OldMan "There, perfect!"
            OldMan "Okay, stay like this, a little romantic photo to start with"
            play sound "audio/Key.ogg" volume 0.9 noloop
            $ flash_screen(wait=True)
            OldMan "Great"
            Leyna "(Johan is right there, looking at us while all this is going on... I never thought I would be in a situation like this next to him.... am I getting excited?)"
            scene fotoerotica7
            Leyna "(I'm feeling it pressing against my ass... his huge... thing, it's hot and throbbing against me)"
            OldMan "All right, the time has come to start getting spicy, lift her bra, let that perfect body you have be seen"
            Johan "(Shit, here we go... Fuck why do I have an erection now? There's a guy touching my wife right under my nose...)"
            pause
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            scene fotoerotica8
            Leyna "Ooh (Shit, I couldn't help moaning when he kissed my neck.... What's wrong with me? I can barely control myself)"
            Johan "(Was that a moan?... no... it's my imagination)"
            play sound "audio/Key.ogg" volume 0.9 noloop
            $ flash_screen(wait=True)
            OldMan "Great... I'm speechless, very good!"
            OldMan "Let's go with the next position lift her, as I told you before"
            scene fotoerotica9
            Johan "!!! (the son of a bitch has a huge dick and he's already got a hard-on!)"
            Leyna "Wow... (He's rubbing me down there, just with his breathing he's already... stimulating me, I feel his breath on the back of my neck and the... down there)"
            play sound "audio/Key.ogg" volume 0.9 noloop
            $ flash_screen(wait=True)
            OldMan "Well, guys, it's time to show it all, Leyna, take your panties aside a little bit"
            Leyna "Al-alright"
            Johan "!!! (Shit, the time has come, I have been paralyzed with everything that is happening)"
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            scene fotoerotica10
            OldMan "That's right... You have a very nice pussy if I may say so Leyna"
            Leyna "Tha-thanks(His cock is rubbing my clitoris and I'm going to go crazy if we go on like this... for a second I forgot that Johan is here)"
            Johan "(Fuck, he's touching her pussy down there with his dick.... Why did I agree to this?)"
            play sound "audio/Key.ogg" volume 0.9 noloop
            $ flash_screen(wait=True)
            OldMan "Very good"
            OldMan "Well the time has come.... the penetration, in this position you are already perfect for the first picture, no need to change it"
            Johan "(WAIT, WHAT? THE PENETRATION?)"
            menu:
                "Intervene":
                    Johan "Hey! There's no way I'm going to let you fuck my wife right under my nose!"
                    OldMan "(Shit, I knew this guy was going to give us trouble) I see... well I guess we'll have to play with the camera angle"
                    OldMan "Leyna, please bend over and get your ass in the air"
                    Leyna "Alright!"
                    scene fotoerotica13
                    OldMan "Okay... so... tch! boy I can still see your dick from here, try to hide it somehow"
                    Villager "Sure, give me a second!"
                    Leyna "!!!"
                    scene fotoerotica14
                    OldMan "Wait wait wait! That's a good position too, hold on a second!"
                    play sound "audio/Key.ogg" volume 0.9 noloop
                    $ flash_screen(wait=True)
                    Leyna "Hmmmm (it keeps rubbing me as it moves)"
                    Villager "(This girl is very horny.... I think I have an idea and I'm sure her husband doesn't notice)"
                    OldMan "Okay kid, I'm going to go back to the position I was in before and as I said, try to hide it somehow so it doesn't show up in the picture"
                    Villager "Okay!"
                    scene fotoerotica15
                    Villager "Okay... okay... give me a moment to get myself well positioned"
                    Leyna "???"
                    pause
                    scene fotoerotica16
                    Villager "Yes... a little more, let's see..."
                    Leyna "Ah (He's sticking his dick in me! He's sticking it in front of Johan, but he doesn't seem to be noticing...)"
                    pause
                    scene fotoerotica17
                    Villager "Yeah! right there, perfect"
                    Leyna "AH! (shit, he put it all the way in me... with this alone I was about to squirt... fuck!)"
                    OldMan "Yes, it's perfect! thank you very much"
                    pause
                    scene fotoerotica18
                    Leyna "Ah ah ah ah (I find it hard to hold on, I feel it throbbing inside me... deep inside me)"
                    Leyna "(Let this end soon please... I don't think I can take much more)"
                    play sound "audio/Key.ogg" volume 0.9 noloop
                    $ flash_screen(wait=True)
                    OldMan "A perfect photo!"
                    pause
                    scene fotoerotica19
                    Johan "(from here I can't see very well what's going on or what they are saying... it certainly seems that he... no, I have already told them that they can't do that)"
                    OldMan "Wow we are having a spectacular photo shoot, well, time to move on to the cumshot"
                    Johan "The what?"
                    OldMan "well... you know, the cumshot... the finishing touch! we can't end this session without one!"
                    Johan "Do you want to cum on my wife's face? NO FUCKING WAY!"
                    OldMan "(Fuck! this guy is ruining my work) Well... I guess I can fix it in photoshop later"
                    OldMan "Leyna, get in position! on your knees!"
                    Leyna "!!! Yeah!"
                    scene fotoerotica21
                    OldMan "Very good"
                    play sound "audio/Key.ogg" volume 0.9 noloop
                    $ flash_screen(wait=True)
                    OldMan "That's it for today kids... it could have been better, but I'm sure the magazine will love it!"
                    OldMan "You can get dressed now, I will keep you posted during these days"
                    Leyna "Okay, thank you"
                    Villager "Yes count on me for anything you want hahahaha"
                    scene fotoerotica23
                    Johan "(What the hell just happened? How could I let them go to such extremes with Leyna? I ... What the hell is going on with me?)"
                    Johan "(And I have this disgusting erection that just won't go away, along with this horrible giddy feeling in my stomach.... Fuck)"
                    Johan "(I have to get out of here and get some fresh air)"
                    scene black with dissolve
                    hide fotoerotica23
                    # fade in
                "Say nothing":
                    Johan "(I... for some reason I'm paralyzed, I can't say a word, I'm nailed to the chair)"
                    Johan "(Like the old man said before, it's just a matter of getting it in for the photo and getting it out, right? But am I really going to let that happen?)"
                    Villager "All right, here I come"
                    Leyna "!!!"
                    pause
                    scene fotoerotica11
                    Leyna "Ah!"
                    Villager "Wow, that went in pretty easy... you're pretty wet down there huh?"
                    Leyna "Lo-lower your voice, my husband will hear you."
                    Villager "hehehehehe yeah sorry"
                    OldMan "All right, guys, hang in there for a second!"
                    pause
                    scene fotoerotica12
                    OldMan "Okay this angle is perfect"
                    Leyna "Ah ah ah... hmmmm"
                    play sound "audio/Key.ogg" volume 0.9 noloop
                    $ flash_screen(wait=True)
                    Johan "(My wife is being penetrated in front of my eyes and I... I'm standing here looking at everything, it feels unreal, I'm getting dizzy)"
                    OldMan "All right, let's move on to the next position"
                    OldMan "Leyna, turn around and bend over, that's perfect!"
                    scene fotoerotica18
                    OldMan "All right, hang in there for a little while"
                    Villager "Your pussy feels great... I don't think I can go much longer without cumming"
                    Leyna "D-don't do it ah ah ah that would be... terrible"
                    play sound "audio/Key.ogg" volume 0.9 noloop
                    $ flash_screen(wait=True)
                    OldMan "Okay guys, let's switch again, Leyna lean to one side"
                    Leyna "Ah ah alright"
                    scene fotoerotica20
                    OldMan "Great, this angle is magic, the magazine will pay us a lot for this!"
                    Johan "(From here I can see everything, that guy has a giant dick and he is inside Leyna, although they are not  moving, he is... inside my wife, I feel like vomiting)"
                    Johan "(I feel sick watching this)"
                    Leyna "(Even though we're not moving, it feels like it's getting to my core and I'm so excited, I can barely control myself... if Johan wasn't here)"
                    Leyna "(I don't know what could happen...)"
                    play sound "audio/Key.ogg" volume 0.9 noloop
                    $ flash_screen(wait=True)
                    Villager "I can hardly hold on any longer Old man!"
                    Johan "??? ( is he saying...)"
                    OldMan "Oh sure, Leyna get on your knees let's go with the cumshot!"
                    Johan "(Cumshot?)"
                    Leyna "O-okay"
                    scene fotoerotica21
                    OldMan "Perfect! OK, kiddo, anytime"
                    Villager "Yes! ah ahh!"
                    Johan "Wait..."
                    $ flash_screen(wait=True)
                    $ flash_screen(wait=True)
                    scene fotoerotica22
                    play sound "audio/Poison.ogg" volume 0.9 noloop
                    Villager "AAAhhh"
                    Johan "!!!!"
                    Leyna "Oh!"
                    play sound "audio/Key.ogg" volume 0.9 noloop
                    $ flash_screen(wait=True)
                    OldMan "Perfect! the photo came out great, very good job guys! with this we have enough for today, and I'll keep you informed of what the magazine tells me"
                    Leyna "...."
                    scene fotoerotica23
                    play sound "audio/Key.ogg" volume 0.9 noloop
                    $ flash_screen(wait=True)
                    Johan "(What the hell just happened? How could I let them go to such extremes with Leyna? I ... What the hell is going on with me?)"
                    Johan "(And I have this disgusting erection that just won't go away, along with this horrible giddy feeling in my stomach.... Fuck)"
                    OldMan "Okay, that's it, you guys wash up and we'll talk these days"
                    Leyna "Yeah"
                    Johan "..."
                    scene black with dissolve
                    hide fotoerotica23
                    # fade in
        "No":
            pass
    return

label GalleryJohanAndLeynaFuck_1(menu_choice = None):
    "Johan and Leyna fuck"
    "Do you want to see it?"
    menu:
        "Yes":
            scene johanfollar1
            play sound "audio/Close1.ogg" volume 0.9 noloop
            Leyna "Johan? what's wrong?"
            scene johanfollar2
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            Leyna "Johan?"
            Johan "(Look at her... this woman... she is perfect)"
            Johan "Hm..."
            scene johanfollar3
            Leyna "!!!"
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            scene johanfollar4
            Leyna "(He has taken off my clothes... in such a... manly way I don't think I've ever seen Johan like that)"
            Johan "(After everything that has happened today.... I cannot stay the same... Leyna is my wife, this beautiful woman is mine)"
            Johan "(Almost everyone in town wants to fuck her and rightly so. I didn't realize how lucky I am to be with a woman like this)"
            Johan "(I have to make an effort for her, to give my best to satisfy her.... but all these guys wanting to be with her, it's such a big pressure...)"
            Johan "(I feel so insecure... I can't stop thinking about what just happened at the photo shoot)"
            "(BEWARE The decision you make now will have repercussions at the end of the story)"
            menu:
                "I can't take the pressure":
                    scene johanfollar13
                    Johan "(Damn it, the pressure.... Why do I feel like this? it's like I have a crowd watching me)"
                    Johan "(After so many years together with her.... now I feel as if it is the first time I am going to fuck my wife)"
                    Johan "(I don't know if I'm feeling up to it!)"
                    scene johanfollar8
                    Leyna "!!! You're already going in? it's a bit... rushed"
                    Johan "...."
                    Johan "(Don't listen to her if I try hard enough... maybe .... maybe it's good enough)"
                    pause
                    scene johanfollar9
                    play bgs "audio/audio follar.ogg" loop volume 0.9
                    Leyna "!!!"
                    Johan "(I may have gone too fast... it's a little dry down there...)"
                    Johan "(Why can't I stop thinking about stupid things? I'm not where I should be)"
                    pause
                    scene fotoerotica8
                    $ flash_screen(wait=True)
                    Johan "(Shit why do I have to think about that now?)"
                    Leyna "Johan? are you okay? you feel a little... strange..."
                    hide fotoerotica8
                    Johan "Y-yes, I'm fine!"
                    Johan "Pu-put yourself like this!"
                    pause
                    scene johanfollar10
                    stop bgs fadeout 1
                    play bgs "audio/audio follar.ogg" loop volume 0.9
                    Johan "I like that!"
                    Leyna "Ah ah ah!"
                    Johan "(Looks like it's getting wet! very good, I just have to keep it up! and stop thinking so much!)"
                    scene fotoerotica18
                    Johan "(Shit, not again! Why do I have to be thinking about that shit all the time?)"
                    Johan "(What the fuck? I'm going to cum already... normally I last much longer)"
                    $ flash_screen(wait=True)
                    stop bgs fadeout 1
                    scene johanfollar11
                    $ flash_screen(wait=True)
                    Johan "AAAhh!"
                    Leyna "??? (Already? ... that's been a bit ...)"
                    Johan "(Fuck, I couldn't help it... Shit)"
                    scene johanfollar14
                    Leyna "That was... hahaha it was... well... I ehmmm I'm going rest a little bit... then we could go out for a while and have a drink if you want..."
                    Johan "Hmmm yes ... sure... (Why is the atmosphere so uncomfortable? fuck... this has been a disaster)"
                    Johan "Take a nap, I'll be downstairs waiting for you"
                    Leyna "See you in half an hour or so!"
                    Johan ".... Yeah, great..."
                    scene black with dissolve
                    hide johanfollar14
                    # fade in
                "NONSENSE! I will do my best!":
                    scene johanfollar5
                    Johan "(But what am I thinking? Leyna is my wife, among all the guys that tried to seduce her,she chose me)"
                    Johan "(I will try my best to give you the best sex of your life I don't have to think so much, just enjoy the moment)"
                    Leyna "Johan, are you okay?"
                    Johan "Me? yeah!"
                    scene johanfollar7
                    Leyna "Ah!"
                    Leyna "(He's!!! it's been a long time since he did this to me, he's doing it... very well... if he keeps on like this I'll be done soon)"
                    Leyna "Keep going... keep going... Oh my God..."
                    pause
                    scene johanfollar8
                    Johan "No, not yet"
                    Leyna "Why did you stop?"
                    Johan "Because I don't want you to cum yet, I'm going to make it last as long as I can!"
                    scene johanfollar9
                    play bgs "audio/audio follar.ogg" loop volume 0.9
                    Leyna "AH! ah! ah!"
                    Johan "Do you like it?"
                    Leyna "Hmmm!!"
                    Johan "Tell me you like it, leyna! or I'll stop!"
                    Leyna "(Johan has never talked dirty to me like that before ...) I like it! Don't stop please keep going!"
                    Johan "Very good, come here"
                    Leyna "!!!"
                    pause
                    scene johanfollar10
                    play bgs "audio/audio follar.ogg" loop volume 0.9
                    Johan "That's right!"
                    Leyna "Ahh! Keep going! Keep fucking me like this!"
                    Johan "You don't have to tell me, I won't stop until you cum!"
                    Leyna "AH!!! I'M GOING TO CUM!!"
                    Johan "ME TOO!"
                    pause
                    scene johanfollar11
                    stop bgs fadeout 1
                    $ flash_screen(wait=True)
                    $ flash_screen(wait=True)
                    Johan "AH!!"
                    Leyna "AAH! shit! (I can't stop shaking, it's the first orgasm I've had in months)"
                    pause
                    scene johanfollar12
                    Johan "What do you think?"
                    Leyna "Unbelievable... I don't know what's wrong with you today... but I wouldn't mind if you kept it up a little longer hahaha"
                    Johan "Well, no problem with that as long as you want it, we can do this every day hahaha"
                    Leyna "Hahaha well, every day... we'll see..."
                    Leyna "Shall we go for a drink?"
                    Johan "Sure! let's go to the bar for a beer!"
                    scene black with dissolve
                    hide johanfollar12
                    # fade in
        "No":
            pass
    return

label GalleryGameWithAlexa_1(menu_choice = None):
    "Game with Alexa"
    "Do you want to see it?"
    menu:
        "Yes":
            scene black with dissolve
            show apuesta1 with dissolve
            "A FEW BEERS LATER"
            Alexa "...And I told him \"Not even in your dreams\""
            Leyna "Hahahaha... By the way, didn't you guys have a meeting to teach Alexa a traditional game?"
            Villager "Oh... (Shit...) Ahem yes... well it's just that that game can only be played by three people"
            Alexa "AAah yeah? wow... Well no problem! I can show you a game I used to play in college!"
            scene apuesta2
            Villager "(Fuck this girl is hot...) Yeah yeah... we can play whatever you want..."
            Johan "(This guy could stop it, he's staring at my wife's tits with me in front of him...) And what does this game consist of?"
            scene apuesta3
            Alexa "It is quite simple, similar to truth or dare, but a little different"
            Alexa "It is not the one who is asked who decides whether he prefers to make truth or daring but the one who asks, for example..."
            Alexa "Let's say it's my turn and I tell you \"Johan... take off your pants\" then you should do it"
            Alexa "Or I could ask you... an awkward question and if you don't want to answer it you would have to do what I said"
            Johan "(That seems a bit...) What if I don't want to?"
            Alexa "Well, you lose the game hahahaha, come on let's go drink a few more beers and play"
            Leyna "Yes, it will be fun!"
            scene apuesta4
            "SEVERAL BEERS LATER"
            Alexa "Well let's get started!"
            Leyna "Hehehe I'm a little nervous"
            Johan "(And a little drunk too hahahaha)"
            Alexa "Well I'll start... let's see... let's start with something light hahaha"
            Alexa "Johan who do you think is in better shape me or Leyna?"
            menu:
                "Alexa":
                    Alexa "Wow I didn't expect that hahaha"
                    Leyna "Hey, I'm your wife!"
                    Johan "Hahahahaha sorry I have to be impartial and it looks like Alexa does a lot of sports"
                "Leyna":
                    Alexa "Oooh how sweet! very well said!"
                    Leyna "Hahahahaha it's favoritism! Alexa is in better shape than me, she does a lot of sport"
                    Johan "hahahaha"
            Alexa "Anyway... let's keep going!"
            Alexa "Leyna, it's your turn!"
            Leyna "Uy I don't know what to say... hmmm I don't know your name... but well, you"
            Villager "M-me?"
            Leyna "Yes hehehehehe I have noticed that there are not many women in the village.... are you a virgin?"
            Villager "!!! I... ehm.... Yes! I'm a virgin! I haven't been able to do much about it... (I was supposed to lose it today...)"
            Alexa "Wow! an honest man! that's a rare thing!"
            Leyna "Hahaha, don't worry, the day will come, don't get overwhelmed by the issue!"
            Villager ".... Right...."
            Leyna "W-well, it's your turn..."
            Villager "O-okay (what can I say?)"
            Villager "Come to think of it... Alexa, let's see if you have guts! show us your boobs!"
            Leyna "!!!"
            Johan "(I don't think she dares...)"
            scene apuesta5
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            Alexa "No problem, Trying to test me? hahahaha"
            Villager "Wow, I thought you wouldn't dare! People from out of town tend to be a little self-conscious about nudity...."
            Alexa "Well, I don't..."
            Johan "(You can say that...)"
            Leyna "Johan don't look so much hahahaha"
            Johan "Y-yeah sorry"
            scene apuesta6
            Villager "Well, man, now it's your turn"
            Villager2 "Yes! I've already thought about what I'm going to do"
            Villager2 "You've been a little hard on Alexa so I'm going to have to teach you a little lesson, get naked!"
            Villager "What? Come on, man, don't be an asshole!"
            Villager2 "Hey, the rules are the rules, Alexa hasn't had any problem, you're not going to chicken out, are you?"
            Villager "...Dickhead, very well as you wish"
            scene apuesta7
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            Leyna "WOW (Shit did I say that out loud?)"
            Alexa "Careful Leyna, don't stare so much hahaha"
            Leyna "I-I don't! ..."
            Johan "..."
            scene apuesta8
            Alexa "Well Johan, it's your turn, what do you have to say?"
            Johan "I... let's see let me think (shit I'm drawing a blank)"
            Johan "Let's see... Alexa, have you ever participated in a threesome?"
            Alexa "Well, we're starting to go strong, huh? Yes, I have participated in a couple of threesomes"
            Villager "Holy shit! nice..."
            Alexa "Hahahaha... Well now it's my turn, since you guys have been going so strong in the first round... let's see... Leyna"
            Leyna "!!! Ye-yeah?"
            Alexa "Take off your shirt"
            Leyna "Ah? I see..."
            Johan "(Shit...I guess it's fair, we've all seen Alexa and the other guy...I guess the rules are the rules)"
            scene apuesta9
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            Villager2 "Wow, you have the most beautiful tits I've ever seen in my life"
            Johan "!!! (You don't need to say that out loud, asshole)"
            Alexa "Hahaha yes, you are right"
            Alexa "Well Leyna, it's your turn..."
            Leyna "I, the truth is that I can't think of anything...."
            Alexa "You can always pass the turn..."
            Leyna "Yes, that's what I'm going to do..."
            Villager "Well... I guess it's my turn... let's see... Ahhh I can't think of anything right now either I'm drawing a blank with these views"
            Villager2 "Well, it's my turn... Leyna, how many men have you slept with?"
            "Leryna: !!! I-I... Ehmm... It seems a bit too personal for me..."
            Johan "???"
            Villager2 "You don't want to answer? fine, but you'll have to make a dare... let's see... My virgin friend here is desperate, so..."
            Villager2 "Leyna, suck his dick"
            Johan "Eh?"
            scene apuesta10
            play sound "audio/Jump1.ogg" volume 0.9 noloop
            Villager "Yes, it will be a great pleasure!"
            Leyna "Ah?!!"
            Alexa "Oh Wow! hahahaha"
            pause
            scene apuesta11
            Leyna "Ugh!"
            Johan "!!!Shit, before I could say anything, he's put his dick in her mouth!.... why am I not saying anything right now?)"
            Johan "(I've been entranced again by seeing this kind of thing...)"
            menu:
                "STOP!":
                    Johan "HEY! stay away from my wife!"
                    scene apuesta16
                    Leyna "!!!  (I've never seen Johan so angry before)"
                    Alexa "Come on, Johan don't get so angry, it's just a silly game"
                    scene apuesta15
                    Johan "I understand very well! but I can't allow something like this! I'm sorry guys, but we've had enough fun for today!"
                    Johan "(I'm a bit saturated between this and the photo shoot ... I just need a quiet fucking afternoon with my wife)"
                    Leyna "...Johan..."
                    Johan "Let's go Leyna, we need to go for a walk to sober up and then we'll see what we're going to do"
                    Leyna "Y-yes, you're right"
                    scene apuesta17
                    Alexa "It's a pity guys! Please don't be angry! we had no bad intentions! see you soon in town, couple!"
                    Johan "Yes, of course"
                    scene black with dissolve
                    hide apuesta17
                    # fade in
                "....":
                    scene apuesta12
                    Johan "(I'm just pinned to the floor, with nothing to say... while they do this to Leyna...)"
                    Villager "This feels amazing, all the way in!"
                    Villager2 "Enjoy it man, who knows when it might happen again!"
                    Johan "(They are saying these kinds of things with me in front of them!)"
                    Alexa "Hahahaha what an enthusiasm! keep up the good work kid!"
                    Leyna "!!!"
                    pause
                    scene apuesta13
                    play bgs "audio/audio follar.ogg" loop volume 0.9
                    Villager "Ah! Ah! like this! all the way down! swallow it whole!"
                    Villager2 "Fuck man! you're fucking her throat what a beast!"
                    Alexa "That's the way to do it!"
                    Johan "(what the hell is going on? what the hell are they talking about?... this is... this...)"
                    Johan "(My stomach is so upset that I feel like throwing up)"
                    pause
                    scene apuesta14
                    stop bgs fadeout 1
                    Leyna "Ah... Ah... Ah... I need to... breathe"
                    Villager "Come on, this is not over..."
                    Leyna "NO!... no... stop, this is too much, enough is enough!"
                    pause
                    scene apuesta16
                    Alexa "Oooh... are you going to leave it like that?"
                    Leyna "Y-yeah, game over... I've had enough for today"
                    Villager2 "What a bummer, man... you just went a little too far"
                    Villager "S-sorry"
                    Alexa "Don't worry, you have made it very well"
                    pause
                    scene apuesta17
                    Leyna "We are leaving now"
                    Johan "...Y-yes..."
                    Alexa "Oh, you're leaving already? too bad, we'll see you in town, couple..."
                    Leyna "... Yes, we'll see"
                    scene black with dissolve
                    hide apuesta17
                    # fade in
        "No":
            pass
    return

label GalleryGameWithAlexa_2(menu_choice = None):
    "Game with Alexa"
    "Do you want to see it?"
    menu:
        "Yes":
            scene black with dissolve
            show apuesta1 with dissolve
            "A FEW BEERS LATER"
            Alexa "...And I told him \"Not even in your dreams\""
            Leyna "Hahahaha... By the way, didn't you guys have a meeting to teach Alexa a traditional game?"
            Villager "Oh... (Shit...) Ahem yes... well it's just that that game can only be played by three people"
            Alexa "AAah yeah? wow... Well no problem! I can show you a game I used to play in college!"
            scene apuesta2
            Villager "(Fuck this girl is hot...) Yeah yeah... we can play whatever you want..."
            Johan "(This guy could stop it, he's staring at my wife's tits with me in front of him...) And what does this game consist of?"
            scene apuesta3
            Alexa "It is quite simple, similar to truth or dare, but a little different"
            Alexa "It is not the one who is asked who decides whether he prefers to make truth or daring but the one who asks, for example..."
            Alexa "Let's say it's my turn and I tell you \"Johan... take off your pants\" then you should do it"
            Alexa "Or I could ask you... an awkward question and if you don't want to answer it you would have to do what I said"
            Johan "(That seems a bit...) What if I don't want to?"
            Alexa "Well, you lose the game hahahaha, come on let's go drink a few more beers and play"
            Leyna "Yes, it will be fun!"
            scene apuesta4
            "SEVERAL BEERS LATER"
            Alexa "Well let's get started!"
            Leyna "Hehehe I'm a little nervous"
            Johan "(And a little drunk too hahahaha)"
            Alexa "Well I'll start... let's see... let's start with something light hahaha"
            Alexa "Johan who do you think is in better shape me or Leyna?"
            menu:
                "Alexa":
                    Alexa "Wow I didn't expect that hahaha"
                    Leyna "Hey, I'm your wife!"
                    Johan "Hahahahaha sorry I have to be impartial and it looks like Alexa does a lot of sports"
                "Leyna":
                    Alexa "Oooh how sweet! very well said!"
                    Leyna "Hahahahaha it's favoritism! Alexa is in better shape than me, she does a lot of sport"
                    Johan "hahahaha"
            Alexa "Anyway... let's keep going!"
            Alexa "Leyna, it's your turn!"
            Leyna "Uy I don't know what to say... hmmm I don't know your name... but well, you"
            Villager "M-me?"
            Leyna "Yes hehehehehe I have noticed that there are not many women in the village.... are you a virgin?"
            Villager "!!! I... ehm.... Yes! I'm a virgin! I haven't been able to do much about it... (I was supposed to lose it today...)"
            Alexa "Wow! an honest man! that's a rare thing!"
            Leyna "Hahaha, don't worry, the day will come, don't get overwhelmed by the issue!"
            Villager ".... Right...."
            Leyna "W-well, it's your turn..."
            Villager "O-okay (what can I say?)"
            Villager "Come to think of it... Alexa, let's see if you have guts! show us your boobs!"
            Leyna "!!!"
            Johan "(I don't think she dares...)"
            scene apuesta5
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            Alexa "No problem, Trying to test me? hahahaha"
            Villager "Wow, I thought you wouldn't dare! People from out of town tend to be a little self-conscious about nudity...."
            Alexa "Well, I don't..."
            Johan "(You can say that...)"
            Leyna "Johan don't look so much hahahaha"
            Johan "Y-yeah sorry"
            scene apuesta6
            Villager "Well, man, now it's your turn"
            Villager2 "Yes! I've already thought about what I'm going to do"
            Villager2 "You've been a little hard on Alexa so I'm going to have to teach you a little lesson, get naked!"
            Villager "What? Come on, man, don't be an asshole!"
            Villager2 "Hey, the rules are the rules, Alexa hasn't had any problem, you're not going to chicken out, are you?"
            Villager "...Dickhead, very well as you wish"
            scene apuesta7
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            Leyna "WOW (Shit did I say that out loud?)"
            Alexa "Careful Leyna, don't stare so much hahaha"
            Leyna "I-I don't! ..."
            Johan "..."
            scene apuesta8
            Alexa "Well Johan, it's your turn, what do you have to say?"
            Johan "I... let's see let me think (shit I'm drawing a blank)"
            Johan "Let's see... Alexa, have you ever participated in a threesome?"
            Alexa "Well, we're starting to go strong, huh? Yes, I have participated in a couple of threesomes"
            Villager "Holy shit! nice..."
            Alexa "Hahahaha... Well now it's my turn, since you guys have been going so strong in the first round... let's see... Leyna"
            Leyna "!!! Ye-yeah?"
            Alexa "Take off your shirt"
            Leyna "Ah? I see..."
            Johan "(Shit...I guess it's fair, we've all seen Alexa and the other guy...I guess the rules are the rules)"
            scene apuesta9
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            Villager2 "Wow, you have the most beautiful tits I've ever seen in my life"
            Johan "!!! (You don't need to say that out loud, asshole)"
            Alexa "Hahaha yes, you are right"
            Alexa "Well Leyna, it's your turn..."
            Leyna "I, the truth is that I can't think of anything...."
            Alexa "You can always pass the turn..."
            Leyna "Yes, that's what I'm going to do..."
            Villager "Well... I guess it's my turn... let's see... Ahhh I can't think of anything right now either I'm drawing a blank with these views"
            Villager2 "Well, it's my turn... Leyna, how many men have you slept with?"
            "Leryna: !!! I-I... Ehmm... It seems a bit too personal for me..."
            Johan "???"
            Villager2 "You don't want to answer? fine, but you'll have to make a dare... let's see... My virgin friend here is desperate, so..."
            Villager2 "Leyna, suck his dick"
            Johan "Eh?"
            scene apuesta10
            play sound "audio/Jump1.ogg" volume 0.9 noloop
            Villager "Yes, it will be a great pleasure!"
            Leyna "Ah?!!"
            Alexa "Oh Wow! hahahaha"
            pause
            scene apuesta11
            Leyna "Ugh!"
            Johan "!!!Shit, before I could say anything, he's put his dick in her mouth!.... why am I not saying anything right now?)"
            Johan "(I've been entranced again by seeing this kind of thing...)"
            menu:
                "STOP!":
                    Johan "HEY! stay away from my wife!"
                    scene apuesta16
                    Leyna "!!!  (I've never seen Johan so angry before)"
                    Alexa "Come on, Johan don't get so angry, it's just a silly game"
                    scene apuesta15
                    Johan "I understand very well! but I can't allow something like this! I'm sorry guys, but we've had enough fun for today!"
                    Johan "(I'm a bit saturated between this and the photo shoot ... I just need a quiet fucking afternoon with my wife)"
                    Leyna "...Johan..."
                    Johan "Let's go Leyna, we need to go for a walk to sober up and then we'll see what we're going to do"
                    Leyna "Y-yes, you're right"
                    scene apuesta17
                    Alexa "It's a pity guys! Please don't be angry! we had no bad intentions! see you soon in town, couple!"
                    Johan "Yes, of course"
                    scene black with dissolve
                    hide apuesta17
                    # fade in
                "....":
                    scene apuesta12
                    Johan "(I'm just pinned to the floor, with nothing to say... while they do this to Leyna...)"
                    Villager "This feels amazing, all the way in!"
                    Villager2 "Enjoy it man, who knows when it might happen again!"
                    Johan "(They are saying these kinds of things with me in front of them!)"
                    Alexa "Hahahaha what an enthusiasm! keep up the good work kid!"
                    Leyna "!!!"
                    pause
                    scene apuesta13
                    play bgs "audio/audio follar.ogg" loop volume 0.9
                    Villager "Ah! Ah! like this! all the way down! swallow it whole!"
                    Villager2 "Fuck man! you're fucking her throat what a beast!"
                    Alexa "That's the way to do it!"
                    Johan "(what the hell is going on? what the hell are they talking about?... this is... this...)"
                    Johan "(My stomach is so upset that I feel like throwing up)"
                    pause
                    scene apuesta14
                    stop bgs fadeout 1
                    Leyna "Ah... Ah... Ah... I need to... breathe"
                    Villager "Come on, this is not over..."
                    Leyna "NO!... no... stop, this is too much, enough is enough!"
                    pause
                    scene apuesta16
                    Alexa "Oooh... are you going to leave it like that?"
                    Leyna "Y-yeah, game over... I've had enough for today"
                    Villager2 "What a bummer, man... you just went a little too far"
                    Villager "S-sorry"
                    Alexa "Don't worry, you have made it very well"
                    pause
                    scene apuesta17
                    Leyna "We are leaving now"
                    Johan "...Y-yes..."
                    Alexa "Oh, you're leaving already? too bad, we'll see you in town, couple..."
                    Leyna "... Yes, we'll see"
                    scene black with dissolve
                    hide apuesta17
                    # fade in
        "No":
            pass
    return

label GalleryBarDay1_1(menu_choice = None):
    "Bar day1"
    "Do you want to see it?"
    menu:
        "Yes":
            Leyna "(A reputation in town?..)"
            scene black with dissolve
            if switch("corruption_average"):
                $ flash_screen(wait=True)
                show blackmail3 with dissolve
                Leyna "(Those two assholes didn't show the pictures to anyone, did they?)"
            if switch("corruption_low"):
                scene onsen9
                # fade in
                Leyna "(I guess that since I arrived in town I've drawn some unwanted attention)"
            scene trabajobar2
            Leyna "Well... then will you give me a chance?"
            Barman "Hmmm... what the hell could go wrong? ok let's give it a try"
            Leyna "Right now? ... ok sure, do you have a uniform?"
            Barman "Uniform? hahahahaha oh.... (Wait wait wait... A Sexy uniform is an excellent idea)"
            Barman "(The truth is that I just received those sexy clothes that I bought for my wife on Amazonian... maybe it will be suitable)"
            Leyna "???"
            Barman "Ahem yes of course... I'll give it to you right now, I have it back there, give me a second!"
            scene pantallanegro:
                xsize 979
                ysize 720
            Barman "Here you go! There is a warehouse back here where you can try it on!"
            Leyna "Hmmm this is a bit..."
            Barman "Is there any problem? it's the only one I have"
            Leyna "... no, no problem"
            scene trabajobar3
            Leyna "So this is the uniform eh? (Who am I kidding... obviously it was going to be something provocative...)"
            Leyna "Damn it... my tits are practically out in the open"
            scene trabajobar4
            Leyna "And I don't even have to bend down to be seen all the way down there..."
            Leyna "(I'm starting to regret coming here and we haven't even started yet...)"
            Leyna "(But until I get the money for the photos, I don't have a penny to spend, so I'll just have to put up with it)"
            scene trabajobar5
            Barman "Wow! it suits you perfectly!"
            Leyna "You think so?"
            Barman "Yes! you're certainly going to bring in a lot of clientele as soon as all the guys in town hear about it"
            Leyna "..."
            scene trabajobar6
            Barman "Perfect boobs!"
            Leyna "What?"
            Barman "Oh excuse me! did I say that out loud? sorry I got carried away with my excitement"
            Leyna "I-I see"
            scene pantallanegro:
                xsize 979
                ysize 720
            "A short time later"
            scene trabajobar8
            Johan "It's been a... complicated day, I needed to come to the bar to clear my head for a while"
            Johan "Nothing like a beer to take your mind off your troubles"
            scene trabajobar9
            Johan "It seems to be the same people as always"
            Johan "Although we've only been here a few days, I've started to get fond of this site"
            Johan "It has the charm of an old-fashioned village bar. there are no places like this in the city"
            Johan "There's an empty table over there, I'd better hurry up before someone takes it from me"
            scene trabajobar10
            Johan "!!!! (What the fuck?)"
            Johan "(That's Leyna? what's she doing here? I thought she had to go to the hotsprings to work)"
            Johan "(And what the hell is she doing dressed like that?)"
            scene trabajobar11
            Johan "(I can see everything! How can she be dressed like that, surrounded by drunks?)"
            Johan "(One thing is the festival and all the traditions of the of this place, especially if we go together... but alone?... I don't understand anything)"
            scene trabajobar12
            Leyna "Jo-johan?"
            Johan "Leyna, what is going on here?"
            Leyna "I-I didn't think you were coming... I, sorry..."
            Johan "Explain to me what is going on, why are you dressed like this?"
            Leyna "You see... you know that I got a little job at the Hotsprings..."
            "Johan. Yes... I thought you'd be there"
            Leyna "It's just... I couldn't continue that work... I had a bad work experience... with the customers... Do you understand?"
            Leyna "And you still haven't finished the work on the magazine... We're really short of money and staying here is still costing us money I thought..."
            Leyna "I thought that... I just wanted to help you get out of this situation... you're always the one who carries the burden"
            Johan "I'm... I'm sorry I shouldn't have been so... If I were a good husband, I would bring home all the money we needed and you wouldn't have to do this"
            Leyna "NO! don't worry, it's okay..."
            Johan "So, now you are a waitress here?"
            Leyna "Yes, I'm sorry I haven't told you anything, it's all been a bit sudden, it's my first day on the job"
            Johan "Oh! then I don't want to bother you anymore...please keep working"
            Leyna "Sure! Do you want me to pour you a beer?"
            Johan "Yes, thank you very much"
            scene trabajobar13
            "Minutes later"
            Johan "(Fuck now I feel guilty about this whole situation)"
            Johan "(But seriously... I think it's good that he wants to help with the situation...)"
            scene trabajobar14
            Johan "(But does she really have to dress like that to work as a waitress?)"
            Johan "(Fuck, you can see everything, seeing my wife dressed like this, surrounded by drunks..)"
            scene trabajobar15
            Johan "(Hey! what the hell is that guy doing? that's my wife!)"
            Johan "What kind of confidence is that? he's touching her hips! his hand... are very close to her ass!)"
            scene trabajobar16
            Johan "(and Leyna... she doesn't seem to care)"
            Johan "(she's smiling, as if nothing happened.... maybe I'm being too jealous?)"
            Johan "(Even so, I can't help but get upset... they are taking such confidences with my wife, who is practically naked)"
            Johan "(And he's touching her... after the photo shoot I should care less about something so mundane, but I'm still getting sick watching this)"
            scene black with dissolve
            # fade in
            scene trabajobar17
            Leyna "Good evening, sir! Would you like something to drink?"
            OldVillager "Oh! hello beautiful, you're new, aren't you? it was missing a beauty like you in this place!"
            Barman "Hey old man! don't overdo it, to complain so much I see you here every day!"
            OldVillager "Hey don't make a fool of me in front of the lady! honey give me a beer"
            scene trabajobar18
            YoungVillager "(This woman is always provoking the men of the village ... she does it on purpose,I'm sure she thinks we are all apes here)"
            YoungVillager "(Well, now you're going to find out!)"
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            scene trabajobar19
            Leyna "Ah?!"
            OldVillager "Ohh!! damn!"
            Johan "!!!!"
            scene trabajobar20
            Leyna "Oh s-sorry! I don't know what could have happened."
            OldVillager "Don't worry! if it's for me you can stay like this for as long as you like  hahahaha"
            Barman "Of course, I would like nothing more than for you to work like this. I'm sure you will attract many clients!"
            "johan: (Is that asshole serious? What kind of a job is this?)"
            scene trabajobar21
            Villager "Wow! I see the party is getting exciting!"
            "villager 2: Yes! the owner of the bar is absolutely right! you should be working like this!y ou've seen that nudity doesn't matter so much to us"
            Villager2 "But of course if a woman as sexy as you decided to work like this, we would come every day without fail!"
            Villager "Yes! please, stay like this all the time and I'll order you all the beers you want! I'll leave you a big tip too! I promise"
            Johan "(Why is Leyna so quiet?)"
            Johan "(is she thinking about it?)"
            if bet_together == 2:
                scene trabajobar22
                Leyna "Maybe I'll think about it but not now guys...."
                Johan "(WHAT?!..)"
                Villager "OOOh so you'll think about it? well that's almost a yes"
                Leyna "I make no promises..."
                Villager2 "Okay okay, let's hope you decide, you will have us as your number one fans"
                hide trabajobar22
            Leyna "Well... not right now guys... I'm going to get dressed"
            Barman "Too bad..."
            scene black with dissolve
            # fade in
            scene trabajobar23
            Leyna "(What a shame... And I'm sure Johan has seen it all)"
            Leyna "(I should be used to being seen semi-naked by now... but still...)"
            scene trabajobar24
            Leyna "(I can't help getting wet down there, I'm as red as a tomato.... I hope the customers haven't noticed)"
            Leyna "(Well let's finish with today's shift and let's see what the bartender says)"
            scene black with dissolve
            hide trabajobar24
            # fade in
        "No":
            pass
    return

label GalleryJohanAndAlexa_1(menu_choice = None):
    "Johan and Alexa?"
    "Do you want to see it?"
    menu:
        "Yes":
            scene pantallanegro:
                xsize 979
                ysize 720
            "Meanwhile Johan was on his way to continue his work"
            Johan "At the end I got nervous at the bar watching Leyna surrounded by men and being semi naked...."
            Johan "I've also drank more beer than I should..."
            Johan "... Anyway, let's finish with this interview and I'll be back with Leyna..."
            Johan "And tonight we could..."
            hide pantallanegro
            if johan_leyna_sex == 1:
                $ flash_screen(wait=True)
                scene fotoerotica8
                Johan "Shit, again...I can't help it...every time I think about fucking with Leyna these images come to my mind"
                hide fotoerotica8
            if johan_leyna_sex == 2:
                scene johanfollar9
                Johan "Hehehehehe that was good.... well tonight we'll see"
                hide johanfollar9
            Johan "Anyway, enough of this nonsense... I should go to the festival. I'm meeting the mayor for the interview"
            scene black with dissolve
            # fade in
            scene johanxalexa1
            Johan "Damn it... I've been waiting for half an hour already ..."
            Johan "And while I was waiting, I couldn't help but drink one of those infusions they make in this town"
            Johan "The guy who offered it to me has been very annoying"
            Johan "Now, in addition to being drunk, I feel very strange"
            scene johanxalexa2
            Alexa "Helloooo Johan..."
            Johan "!!!"
            scene johanxalexa3
            Alexa "What are you doing here alone Johaaaan?"
            Johan "(Wow, she's so close! she's touching me with her breasts)"
            Johan "(she looks like she's drunk or something... this girl never acts normal but today she's even weirder than ever...)"
            scene johanxalexa4
            Alexa "I don't know if it's the infusion or what... but today you're very attractive Johan..."
            Johan "O-oh? really? i uhmm.... thank you"
            Alexa "Why don't you come a little closer to me and give me a kiss?"
            Johan "I-I don't... (How good Alexa smells... I hadn't noticed but she is very pretty)"
            Alexa "Come on, come here, what's the problem?"
            Johan "I-I can't do that... you know I'm married"
            Alexa "Well..."
            scene johanxalexa5
            Johan "!!!!"
            Alexa "You're telling me no, but this one here is telling me yes..."
            Johan "Sto-stop..."
            Alexa "Oooh? how shy Johan"
            scene johanxalexa6
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            Alexa "Look how hard it is... that's for me?... you like me that much?"
            Johan "We shouldn't... anyone can see us... (I'm having trouble thinking clearly... what's happening to me? I want to fuck her with all my will)"
            Johan "But I can't do it, Leyna is my wife and she's perfect! besides... anyone could see us!)"
            Alexa "Come with me... let's go to a more private place..."
            Johan "I..."
            menu:
                "Go with Alexa":
                    Johan "C-Come on..."
                    scene black with dissolve
                    show johanxalexa7 with dissolve
                    Alexa "Here no one will see us, come on man, we are going to have a good time"
                    Johan "(God... am I really doing this?...I can't believe it... this all seems like a hallucination)"
                    scene johanxalexa8
                    Alexa "That's it, it's almost in... fuck me"
                    Johan "Ohhh you are so warm...."
                    Johan "I'm going to fuck you like you've never been fucked before..."
                    Alexa "Well, don't make me wait any longer"
                    scene johanxalexa9
                    play bgs "audio/audio follar.ogg" loop volume 0.9
                    Alexa "Yes! like this! go on, don't stop"
                    Johan "Ah ah ah!!!"
                    Alexa "Keep fucking me like that!"
                    pause
                    scene johanxalexa10
                    play bgs "audio/audio follar.ogg" loop volume 0.9
                    Alexa "That's it, break me in half..."
                    Alexa "Fuck me hard... anyone could see us at any time Johan ... do you like that?"
                    Johan "Ah ah ah ah, yes, I love it, let them see us while I fuck you, I don't care!"
                    Alexa "Aaaah I love it!"
                    pause
                    scene johanxalexa11
                    play bgs "audio/audio follar.ogg" loop volume 0.9
                    Johan "AH! I am about to..."
                    Alexa "Keep fucking me hard Johan!"
                    Alexa "Fuck me like the whore I am!!!"
                    Johan "AH AH AH I'm going to cum!"
                    Alexa "Cum inside my Johan, use me like a tissue"
                    Johan "ah ahaaah!!"
                    $ flash_screen(wait=True)
                    scene johanxalexa12
                    $ flash_screen(wait=True)
                    stop bgs fadeout 1
                    Johan "Aaaaaahhh...."
                    Alexa "Very good Johan... that's the way I like it..."
                    Johan "ah ah ah (WHAT THE HELL HAVE I DONE?)"
                    Johan "(I have to get out of here right now... I'm getting dizzy)"
                    Alexa "Shall we have a drink? I'm thirsty"
                    Johan "I-I can't, I have to go to work"
                    Alexa "Work?...I see"
                    scene black with dissolve
                    hide johanxalexa12
                    # fade in
                "No":
                    Johan "N-no, I can't do it, I'm married, s-sorry"
                    Alexa "Oh come on, wait don't leave"
                    Johan "I'm sorry..."
                    scene black with dissolve
                    # fade in
        "No":
            pass
    return

label GalleryBarDay2_1(menu_choice = None):
    "bar day2"
    "Do you want to see it?"
    menu:
        "Yes":
            scene trabajobar25
            Barman "Good morning Leyna, ready for another day of work?"
            Leyna "Yes... I'm going to change"
            Barman "have you thought about what we talked yesterday... about the uniform?"
            Leyna "(Wait was that serious?) I-I have to think about it a bit more"
            Barman "... Sure, think about it as much as you need to"
            scene trabajobar26
            Barman "Perfect! as beautiful as ever Leyna... but you seem a little tense, is something wrong?"
            Leyna "Oh n-no, I'm just a little nervous...."
            Barman "that's not good for business, I need you relaxed"
            Barman "Hmmm....I know! have a shot with me, a little rum will relax your your nerves"
            Leyna "Alcohol? I shouldn't..."
            Barman "Come on, listen to me Leyna, I have been working all my life in this business"
            scene trabajobar27
            Leyna "W-well, if you insist... there should be no problem"
            Barman "Perfect, one for you and one for me hahahaaha Cheers!"
            scene pantallanegro:
                xsize 979
                ysize 720
            "After a while and a few more shots..."
            scene trabajobar28
            Leyna "Oh! Shit!"
            Villager "HEY! FUCK"
            scene trabajobar29
            Leyna "I'm so sorry, are you all right?...ahh I left your pants all messed up"
            Villager "What the fuck are you doing! you should be more careful, look how you left m...!!!"
            scene trabajobar30
            Villager "(What a pair of tits!!!!!)"
            Leyna "I'm really sorry, I apologize from the bottom of my heart. I'll pick it all up right away"
            Villager "(She's drunk?... her breath smells of alcohol... but she's a real beauty...) N-nothing's wrong, honey, don't worry so much"
            Leyna "Sorry, I wish I could do something to make it up to you...."
            scene trabajobar31
            Barman "Well, why don't you do what we talked about yesterday? after this screw up you should make the customer's day and even more so after ruining his pants"
            Leyna "W-what we talked about yesterday? I..."
            Villager "What did you talk about yesterday?"
            Barman "Oh I don't know, Leyna, what do you think? we could lose a valued client..."
            scene trabajobar32
            "Leynha: W-well, I'll do it, but just for a moment..."
            Villager "Wh-what are you going to do?"
            Barman "Don't worry, you'll love it, you'll want to come every day"
            scene trabajobar33
            Leyna "Here you go... feel better now?"
            Villager "Holy shit!"
            Barman "Yes, they take your breath away huh? hahahaha"
            YoungVillager "WOW!"
            Leyna "hm?"
            scene trabajobar34
            Villager2 "I see you have finally listened to us and decided to work with your tits out in the open!"
            YoungVillager "With these views I'm going to stay here all afternoon hahahaha Well we have to celebrate that you have listened to us"
            Leyna "What?"
            scene trabajobar35
            YoungVillager "Come on guys a photo for the memory! it is a unique occasion hahahahaha"
            Villager2 "Yes! it's an excellent idea, pose for the camera!"
            Leyna "But..."
            YoungVillager "Come on beautiful, smile, you are very serious, you should be enjoying the moment, like us"
            YoungVillager "(whispering) your husband isn't around after all, is he? it would be a shame for him to join the party right now, wouldn't it?"
            Leyna "!!!"
            scene trabajobar36
            Leyna "O-okay guys, but just one photo and that's it, huh?"
            Villager3 "Yes yes, just one photo with you is enough"
            YoungVillager "Come on man take the picture, I'm going to frame it and hang it in my room so I can see this pair of tits every day when I wake up hahahahaha"
            pause
            scene trabajobar37
            Leyna "!!! aahh..."
            Villager3 "What a cute little moan... I think I'm falling in love with you"
            Leyna "Sto-stop"
            YoungVillager "Yeah man, don't overdo it, leave a little bit for the others"
            Leyna "Let go of me"
            Villager3 "Sorry, don't get mad, honey, I just couldn't resist"
            scene black with dissolve
            show trabajobar38 with dissolve
            Barman "Well, what do you say? will you work like this for the rest of the shift? you've already got all the customers happy"
            Barman "No matter how much you screw up, they'll forgive you"
            menu:
                "I will work like this":
                    scene trabajobar39
                    Leyna "You know what? I'm going to give this a try, it feels liberating and people are leaving lots of tips"
                    Barman "I'm glad to hear that! we'll get rich you and me Leyna! Hahahahaha"
                    Leyna "Hahaha well that remains to be seen, give me one more shot and I'm going to attend to those perverts"
                    Barman "That's how you talk!"
                    scene black with dissolve
                    show trabajobar40 with dissolve
                    Leyna "Well guys, what would you like to drink?"
                    YoungVillager "Three beers, beautiful"
                    Leyna "On the way!"
                    scene black with dissolve
                    show trabajobar42 with dissolve
                    Leyna "I leave them here guys"
                    YoungVillager "Hey, why don't you sit with us for a while?"
                    Leyna "Oh, I'm sorry I can't, I have to keep working"
                    YoungVillager "Oh come on..."
                    scene trabajobar43
                    YoungVillager "Stay a little longer, I'm sure you'll have a great time with us, we know how to treat a lady"
                    Leyna "!!!"
                    Leyna "Hey... you shouldn't..."
                    scene trabajobar45
                    Villager2 "Yes! stay with us honey, you're looking forward to it. I can see it in your face"
                    Villager3 "That's right, don't you want to have fun? you've worked so hard, everyone deserves a little break"
                    scene trabajobar46
                    YoungVillager "(whisper) you certainly look like you want to stay with us for a while, you're really happy down there"
                    YoungVillager "Why don't you sit down with us for a minute?"
                    pause
                    scene trabajobar48
                    Leyna "I-if it's just for a minute, I could stay..."
                    Villager2 "Great... come over here sit on my lap"
                    Leyna "On your lap?"
                    YoungVillager "yeah, haven't you heard my friend? go and sit with him, I'm sure you'll have a great time together hehehehehe"
                    Leyna "Yes.... yes, for sure"
                    scene black with dissolve
                    show trabajobar49 with dissolve
                    Leyna "Oh..."
                    Villager2 "Oh, I'm sorry, it seems to have slipped out... it's just that these pants are very tight... I'm sure you understand me, right?"
                    Leyna "Ri-right... with that big thing, it's very difficult. isn't it?"
                    Villager2 "Exactly..."
                    pause
                    scene trabajobar51
                    Leyna "He-hey stop moving around so much... you're lifting up my skirt..."
                    Villager2 "Me? it looks like you're the one who's moving honey you keep rubbing against my cock..."
                    Leyna "I... no"
                    pause
                    scene trabajobar50
                    Villager2 "What do you mean no? just look at your face, you're you've just felt my cock and you haven't been able to control yourself..."
                    Villager2 "You're eating me alive with your eyes"
                    pause
                    scene trabajobar52
                    Villager2 "Let me help you a little bit..."
                    Leyna "No...stop.."
                    Villager2 "Come on now, you're craving it, at this point you don't care if I fuck you in front of the whole bar"
                    Leyna "Hmmm"
                    pause
                    scene trabajobar54
                    Leyna "AAAhhhh..."
                    Villager2 "WOW... for how wet you are, it was hard to get in"
                    Villager2 "What do you think is as big as it looks?"
                    Leyna "Hmmm, s-stop you're going to break me in half"
                    pause
                    scene trabajobar55
                    Villager2 "And what would be the problem? Isn't that exactly what you want? coming to work dressed like that?"
                    Villager2 "Tell me... say it just once and I'll do it... tell me that you want me to fuck you right here in front of everybody"
                    Leyna ".... hmmm ah ah ah"
                    Villager2 "what are you waiting for? say it at once"
                    Leyna "Ah ah ah... fuck me... fuck me in front of everybody"
                    pause
                    scene trabajobar56
                    Villager2 "As you wish bitch"
                    Villager2 "Get ready"
                    YoungVillager "You heard her, fuck her like she deserves it"
                    Villager3 "hahahaha I can't believe this is happening! crazy!!!"
                    scene trabajobar58
                    play bgs "audio/audio follar.ogg" loop volume 0.9
                    Leyna "HMmmaaaa!!"
                    Villager2 "Do you like it bitch?! !"
                    "Young villager : wow hahahaahah"
                    pause
                    scene trabajobar57
                    play bgs "audio/audio follar.ogg" loop volume 0.9
                    Villager2 "come on bitch, you do it, I'm not going to do all the work"
                    Leyna "AH AH AH AH!!!!"
                    Villager2 "Watch her shake her ass! She's an expert!"
                    Villager3 "She's super horny, look at her! she's not even aware that the whole bar is watching!"
                    Barman "Hey you fucking savages, what the fuck are you doing to my waitress?"
                    YoungVillager "Now it's a little late to talk old man! enjoy the view like everyone else!"
                    Barman "Fucking kids"
                    pause
                    scene trabajobar59
                    play bgs "audio/audio follar.ogg" loop volume 0.9
                    Villager2 "Fuck, I can't hold on any longer, I'm going to cum inside this slut!"
                    YoungVillager "Hahahahaha yes, do it!"
                    Leyna "AH ah.. wait... wait don't come yet!"
                    Villager2 "AAAH here it goes!!"
                    $ flash_screen(wait=True)
                    scene trabajobar61
                    stop bgs fadeout 1
                    $ flash_screen(wait=True)
                    Villager2 "I couldn't take it anymore... I hadn't fucked for years!"
                    Villager2 "I've stuffed you like a turkey! you should thank me! hahahaha"
                    pause
                    scene trabajobar62
                    Leyna "AH ah ah... I can hardly move... y-you've cum inside me... ah ah ah..."
                    Villager2 "And if you don't get up soon, I'll do it again, beautiful"
                    Leyna "AH ah I'm going... I'm going..."
                    scene black with dissolve
                    hide trabajobar62
                    # fade in
                "No, I can't do it":
                    Leyna "I-I'm sorry but I can't do it at the moment, I don't feel comfortable"
                    Barman "Sure, don't worry, put your uniform back on and continue serving customers as before"
                    Leyna "Yes... thank you"
                    scene black with dissolve
                    show trabajobar41 with dissolve
                    Leyna "Well guys, what would you like to drink?"
                    YoungVillager "Three beers, beautiful"
                    Leyna "On the way!"
                    scene black with dissolve
                    show trabajobar42 with dissolve
                    Leyna "I leave them here guys"
                    YoungVillager "Hey, why don't you sit with us for a while?"
                    Leyna "Oh, I'm sorry I can't, I have to keep working"
                    YoungVillager "Oh come on..."
                    scene trabajobar43
                    YoungVillager "Stay a little longer, I'm sure you'll have a great time with us, we know how to treat a lady"
                    Leyna "!!!"
                    Leyna "Hey... you shouldn't..."
                    scene trabajobar47
                    Villager2 "Yes! stay with us honey, you're looking forward to it. I can see it in your face"
                    Villager3 "That's right, don't you want to have fun? you've worked so hard, everyone deserves a little break"
                    Leyna "I'm sorry guys, but I really can't, I have to keep working"
                    YoungVillager "Oh what a shame"
                    scene black with dissolve
                    show trabajobar63 with dissolve
                    YoungVillager "(whispering) I've got an idea, man... listen carefully"
                    Villager2 "!!! sure, tell me man"
                    scene trabajobar64
                    "A few minutes later"
                    Villager2 "Hey waitress, you brought me a broken jar!"
                    Leyna "Wh-what?"
                    Villager2 "You brought me a broken jar! look how you've left me! It's a mess! it's all messed up"
                    Leyna "Oh! Sorry! I'll pick it up right away"
                    scene trabajobar65
                    Leyna "I'll clean it right away"
                    Villager2 "Oh take your time hehehe in that position you are perfect"
                    Leyna "???"
                    scene trabajobar66
                    Villager2 "that's perfect! Stay close, honey, I'll be done in a second"
                    YoungVillager "Hahahaah You're crazy, man"
                    Leyna "What the hell?"
                    scene trabajobar67
                    play bgs "audio/audio follar.ogg" loop volume 0.9
                    Leyna "How can you have it so big? (but what am I saying, this stranger's dick is so close to my face and I...)"
                    Villager2 "Ufff I love it when you say that...I can feel your breath on my dick... stay very still..."
                    menu:
                        "Keep still":
                            Leyna "Ahh..."
                            Villager2 "That's it... I'm almost... I'm almost there"
                            $ flash_screen(wait=True)
                            stop bgs fadeout 1
                            scene trabajobar68
                            Villager2 "AAAAHhhh!"
                            Villager3 "The crazy fucker has done it, he has done it!"
                            Barman "Hey! what the hell are you doing to my waitress? Bunch of animals!"
                            Villager2 "AAAHh! sorry old man... I couldn't help it...."
                            Barman "Leyna, Come here! and clean yourself up"
                            Leyna "Ye-yeah"
                            scene pantallanegro:
                                xsize 979
                                ysize 720
                            "After that the shift went on in a relatively normal way"
                            scene black with dissolve
                            hide pantallanegro
                            # fade in
                        "nope":
                            Leyna "What the fuck are you talking about? Jerk off at home"
                            Leyna "(I'd better get up quickly before I get a cumshot on my face)"
                            scene pantallanegro:
                                xsize 979
                                ysize 720
                            "After that the shift went on in a relatively normal way"
                            scene black with dissolve
                            hide pantallanegro
                            # fade in
        "No":
            pass
    return

label GalleryTryingTheNewToy_1(menu_choice = None):
    "trying the new toy"
    "Do you want to see it?"
    menu:
        "Yes":
            scene dildo1
            Leyna "I should close the door, though... anyone could see me here"
            Leyna "Wow... looks like he also left me a lubricant I guess that makes sense"
            Leyna "... I can't believe I'm going to do this right now...."
            scene dildo2
            Leyna "It's... quite big... Is that okay with Johan? This thing is much bigger than his penis...."
            Leyna "Just thinking about what I'm going to do already makes me wet down there"
            Leyna "Well there is no point in waiting..."
            scene dildo3
            Leyna "I haven't even started and I'm already so horny....."
            Leyna "hmmmmm...."
            pause
            scene dildo4
            Leyna "will this fit?...it's so big...."
            Leyna "Let's do it little by little... I don't want to hurt myself"
            pause
            scene dildo5
            Leyna "Ahhh... little by little... hmmm... it hurts a little... but"
            Leyna "Ahhh... it's coming in... ohhh"
            pause
            scene dildo6
            Leyna "This is it... almost to the bottom... my god this feels... feels much better than I expected..."
            Leyna "I can't believe how good this feels... I'm going to cum... and I just put it in....."
            pause
            scene dildo7
            Leyna "AH!... this thing vibrates... and it's stimulating my clitoris while penetrating my ass..."
            Leyna "It feels amazing!.... AH ah ah ah!"
            Leyna "This... this is amazing"
            pause
            scene dildo8
            play bgs "audio/audio follar.ogg" loop volume 0.9
            Leyna "Ah ah ah!!! .... AAAHH!!!"
            Leyna "It hurts a little but .... feels amazing"
            Leyna "I'm going to cum! I'M CUMMING!!!"
            Leyna "aaaaahhhhH!!!"
            pause
            scene dildo9
            stop bgs fadeout 1
            Leyna "AAAAAAAAAHHH!!!"
            Leyna "I've already cum.... I haven't lasted at all, I've never cum so fast... this has been awesome"
            Leyna "I can't... I can't wait to do it again..."
            pause
            scene black with dissolve
            hide dildo9
            $ player_location = "Town2"
            # fade in
        "No":
            pass
    return

label GalleryAnalAtTheFoodStall_1(menu_choice = None):
    "Anal at the food stall"
    "Do you want to see it?"
    menu:
        "Yes":
            scene analcomida1
            Leyna "Hello sir, what do you need?"
            "Fat Villager: (WOw who is this girl? I was expecting the same guy as always) Ehm yeah, a beer and some marinated meat thanks"
            Leyna "Coming!"
            scene analcomida2
            Villager "Isn't that your wife?"
            Johan "Yes, it looks like she has already started working, don't tell her that we have already had a beer at the other stall or she will get angry"
            Villager "Hahahahaha easy, I've got your back"
            Johan "Well, let's have a drink with her"
            scene analcomida3
            Leyna "Oh Hi honey, have you been here long?"
            Johan "Hahaha no no no, we just got here ten minutes ago, just walking around"
            Leyna "Great, shall I put something on?"
            scene analcomida4
            Villager2 "Wow isn't that Leyna? I didn't know she was working at the food stall"
            Villager2 "Mother of God, is that the uniform they make her wear? She's practically naked! From here I can see practically everything!"
            scene analcomida5
            Villager2 "Wait a second... she's wearing a butt plug? Fuck!"
            Villager2 "I knew she was a bit of a slut, but to be dressed like that with a butt plug up your ass in public?"
            Villager2 "Just looking at it is making my dick hard"
            Villager2 "Although I have an idea... I should take advantage of this, besides, she has done it for a reason, right? I'm sure she's hoping that someone notices it"
            Villager2 "Yes, I'm going to make my move"
            pause
            scene analcomida6
            Leyna "AH!"
            Villager2 "Hey! what's up leyna? the boss told me to come and help you"
            Leyna "The boss?"
            Villager2 "Exactly, he told me that you probably need some help since you are new to all this"
            Leyna "I-I see"
            pause
            scene analcomida7
            Villager2 "Yeah... let's see what we have here?"
            Leyna "I-is touching the .... the guy is playing with my ass while Johan is there in front)"
            Leyna "(Whispering) What the hell are you doing? My husband is right here"
            scene analcomida8
            Villager2 "(Whispering) Come on, you've come out in public like this in front of everyone, you're asking for someone to help you with this right?"
            Villager2 "(whispering) Well, I have the balls to do it, and I don't give a damn if your husband is in front of me"
            Leyna "You..."
            Villager2 "Well guys, what can I put here?"
            Johan "I see you have a craft beer, right?"
            Villager2 "That's right, you want a pair?"
            Johan "Yes, thank you very much"
            Villager2 "Okay, I'm going to look for them, they should be down here"
            "..."
            Leyna "!!! (The bastard pulled out my butt plug! What the hell is he doing?)"
            Leyna "!!!!"
            scene analcomida9
            Leyna "Hmm! ah (H-he's eating my ass! in front of Johan and these guys!)"
            Leyna "(Don't they see it?... no... they are not seeing it...)"
            Leyna "(My God, why does it feel so good?)"
            pause
            scene analcomida10
            Johan "???"
            Johan "What's wrong? Where are the beers?"
            Leyna "AH! n-nothing"
            Leyna "The boss must have moved them or something (how long is he going to keep this up?...my god)"
            scene analcomida11
            play sound "audio/Equip2.ogg" volume 0.9 noloop
            Leyna "AH!!"
            Johan "!!!!"
            Villager "Wow, I certainly didn't expect that"
            Leyna "I-I'm mmm s-sorry guys it slipped and... ahh... I'll put it on right away"
            pause
            scene analcomida12
            Villager "No rush, take as much time as you need hahahahaha"
            Johan "Dude stop looking!"
            Villager "I'm sorry, I can't help it... my God, what a pair of tits your wife has!"
            Johan "For the love of God I'm right here"
            pause
            scene analcomida13
            Villager2 "Sorry guys, here are the beers"
            Leyna "(My God, thank goodness it's over, a little more and I wouldn't know how to hide anymore... wait)"
            Leyna "(When he took out his dick?... and he's pressing it  against my ass... he won't attempt to...)"
            Villager2 "Sorry Leyna I'm going to clean up the counter a little bit"
            Leyna "!!!"
            pause
            scene analcomida14
            Leyna "(I-I can't pull away he's holding me too tight and squeezing me against him)"
            Villager2 "The rag is over here, isn't it? It's just that everything is a bit dirty..."
            pause
            scene analcomida15
            Leyna "!!!! mmm"
            Villager2 "Where did he put the rag? your boss is a disaster hehehehehe"
            Leyna "(Whispering) Don't even think about it... hmmm ah... don't do that"
            Villager2 "(whispering) I'm sorry but I can't help it...I'll be discreet, don't worry"
            Johan "??? What's the matter?"
            Villager2 "Oh hahaha nothing relax, the owner is a disaster and keeps changing everything around"
            Johan "Hahahahaha I see, but the beer is very good"
            Villager2 "hahaha I see... it's our specialty"
            Leyna "(Is Johan blind? is he really not noticing anything?)"
            if switch("corruption_average"):
                menu:
                    "resist":
                        Leyna "(No! I can't let him do this to me in front of Johan! ... no matter how much I want to.... I have to control myself)"
                        Villager "(Ooooh the tip is already in... it's so hot) I'm going to fuck your tight asshole"
                        scene analalter3:
                            xsize 814
                            ysize 625
                        Villager "AAH!"
                        Johan "!!!!"
                        Villager2 "!!!! Dude, are you okay?"
                        scene analalter4:
                            xsize 814
                            ysize 625
                        Villager "Y-yeah, I'm fine, just a little cramp in my leg that's all"
                        Johan "I see, working in the service sector is very hard..."
                        scene analalter5:
                            xsize 814
                            ysize 625
                        Villager "You're telling me (this bitch...)"
                    "it feels so good...":
                        scene analcomida16
                        Leyna "!!!!! (He has put it in me! It's in!)"
                        Villager2 "(Whispering) Wow you must have been dilated down there and it went in really well.... uff feels like paradise...."
                        pause
                        scene analcomida17
                        Leyna "(He's sticking it all the way up my ass and they're all less than a meter away from me.... they're talking so quietly while this guy is fucking my ass)"
                        Leyna "(Johan's right in front of me... right there... and I'm getting my asshole drilled by a guy with a huge dick... my god... my god...)"
                        Leyna "(I can't take it anymore... I can't take it anymore... !!!!)"
                        pause
                        $ flash_screen(wait=True)
                        $ flash_screen(wait=True)
                        scene analcomida18
                        $ flash_screen(wait=True)
                        Leyna "AAAhh!!!"
                        Johan "Leyna?! Are you ok?!"
                        Villager "Wow something is going on with her for sure..."
                        Johan "Leyna, what's wrong?"
                        pause
                        scene analcomida19
                        Villager2 "Oh! it's a cramp, don't worry, I'm a physiotherapist, I'll fix it right away, it's just that she' been in the wrong posture for a long time"
                        Villager2 "Look, I hold his arms like this and with a couple of movements she will feel much better"
                        play bgs "audio/audio follar.ogg" loop volume 0.9
                        scene analcomida20
                        Leyna "Oh oh ooooh!!"
                        Villager2 "Yes, that seems to be where it hurts! UFf is hard for me... what a tense back!"
                        Johan "It does look like she' s feeling a bit of relief..."
                        Villager "Hey, you could give me another one later, I am also very tense from work"
                        pause
                        $ flash_screen(wait=True)
                        stop bgs fadeout 1
                        scene analcomida21
                        $ flash_screen(wait=True)
                        Villager2 "AAAh! now... now you should be much better...Right Leyna? are you feeling better?"
                        pause
                        scene analcomida22
                        Leyna "I-I... I... I... yes... I feel better..."
                        Leyna "(the son of a bitch leaves me halfway through...)"
                        Leyna "(First I let some teenagers blackmail me because I couldn't control myself, then I let them do all kinds of things to me in the bar and now this...)"
                        Leyna "(I don't know what kind of person I'm becoming, but it's getting harder to control myself)"
                        Leyna "You can let me go... thank you very much..."
                        Villager2 "Great! Well, I should get going... I think the boss told me..."
                        pause
                        scene analcomida23
                        Leyna "(whispering) after what you've done to me in front of everyone you might as well stay and help me the rest of the shift you son of a bitch"
                        Leyna "(whispering) or would you rather I talk to the police right now?"
                        Villager2 "!!! (Fuck that' s scary...) Of course... I'll stay as long as it takes..."
            if switch("corruption_low"):
                menu:
                    "resist":
                        Leyna "(No! I can't let him do this to me in front of Johan! ... no matter how much I want to.... I have to control myself)"
                        Villager "(Ooooh the tip is already in... it's so hot) I'm going to fuck your tight asshole"
                        scene analalter3:
                            xsize 814
                            ysize 625
                        Villager "AAH!"
                        Johan "!!!!"
                        Villager2 "!!!! Dude, are you okay?"
                        scene analalter4:
                            xsize 814
                            ysize 625
                        Villager "Y-yeah, I'm fine, just a little cramp in my leg that's all"
                        Johan "I see, working in the service sector is very hard..."
                        scene analalter5:
                            xsize 814
                            ysize 625
                        Villager "You're telling me (this bitch...)"
                    "it feels so good...":
                        scene analcomida16
                        Leyna "!!!!! (He has put it in me! It's in!)"
                        Villager2 "(Whispering) Wow you must have been dilated down there and it went in really well.... uff feels like paradise...."
                        pause
                        scene analcomida17
                        Leyna "(He's sticking it all the way up my ass and they're all less than a meter away from me.... they're talking so quietly while this guy is fucking my ass)"
                        Leyna "(Johan's right in front of me... right there... and I'm getting my asshole drilled by a guy with a huge dick... my god... my god...)"
                        Leyna "(I can't take it anymore... I can't take it anymore... !!!!)"
                        pause
                        $ flash_screen(wait=True)
                        $ flash_screen(wait=True)
                        scene analcomida18
                        $ flash_screen(wait=True)
                        Leyna "AAAhh!!!"
                        Johan "Leyna?! Are you ok?!"
                        Villager "Wow something is going on with her for sure..."
                        Johan "Leyna, what's wrong?"
                        pause
                        scene analcomida19
                        Villager2 "Oh! it's a cramp, don't worry, I'm a physiotherapist, I'll fix it right away, it's just that she' been in the wrong posture for a long time"
                        Villager2 "Look, I hold his arms like this and with a couple of movements she will feel much better"
                        play bgs "audio/audio follar.ogg" loop volume 0.9
                        scene analcomida20
                        Leyna "Oh oh ooooh!!"
                        Villager2 "Yes, that seems to be where it hurts! UFf is hard for me... what a tense back!"
                        Johan "It does look like she' s feeling a bit of relief..."
                        Villager "Hey, you could give me another one later, I am also very tense from work"
                        pause
                        $ flash_screen(wait=True)
                        stop bgs fadeout 1
                        scene analcomida21
                        $ flash_screen(wait=True)
                        Villager2 "AAAh! now... now you should be much better...Right Leyna? are you feeling better?"
                        pause
                        scene analcomida22
                        Leyna "I-I... I... I... yes... I feel better..."
                        Leyna "(the son of a bitch leaves me halfway through...)"
                        Leyna "You can let me go... thank you very much..."
                        Villager2 "Great! Well, I should get going... I think the boss told me..."
                        pause
                        scene analcomida23
                        Leyna "(whispering) after what you've done to me in front of everyone you might as well stay and help me the rest of the shift you son of a bitch"
                        Leyna "(whispering) or would you rather I talk to the police right now?"
                        Villager2 "!!! (Fuck that' s scary...) Of course... I'll stay as long as it takes..."
            scene analcomida24
            Leyna "Well guys... I see you've already finished your beers, would you like one more round?"
            Johan "Yes please! after this scary moment, I need to relax with another round"
            Leyna "Hahahahaha, coming right up"
            scene black with dissolve
            hide analcomida24
            # fade in
            scene analalter1:
                xsize 814
                ysize 625
            Villager "Here, I'll give you back what I took from you before"
            Leyna "!!!!!!!"
            scene analalter2:
                xsize 814
                ysize 625
            Leyna "OOoh!!!"
            Leyna "You..."
            Villager "I see you're still pretty sensitive down there hahahahahaha"
            Villager "Well, I'm going now, if you need me to relieve yourself, look for me, I'll be around here"
            Leyna "Not in your wildest dreams..."
            Villager "Well... your words and your actions don't match, honey"
            Leyna "Shu-shut up"
            scene black with dissolve
            hide analalter2
            # fade in
        "No":
            pass
    return

label GalleryNightPartyAtTheFestival_1(menu_choice = None):
    "Night party at the festival"
    "Do you want to see it?"
    menu:
        "Yes":
            scene festivalnoche1:
                xsize 814
                ysize 625
            Villager "Hey!"
            Leyna "!!! (shit, have They seen what's up my ass?)"
            Leyna "H-hey, what's up?"
            Villager "Don't you remember us? the other night we had a great time at the river with you and your husband"
            Leyna "O-oh Y-yes (That was when we got so drunk, wasn't it?... I can hardly remember what happened that night)"
            Leyna "I'm sorry, it's just that with all the drinking, that night..."
            Villager "Hahahahaha too bad, but I hear you, we were pretty drunk too"
            Leyna "Well..."
            Villager "You're not going to leave now, are you? This is when the best starts!"
            Leyna "Ah! n-no, don't worry, I have to change and I'll be right back"
            scene festivalnoche2:
                xsize 814
                ysize 625
            Villager "Change? what for? you're perfect to go through the festival like this"
            Leyna "Like this? but I'm practically naked..."
            Villager "Aren't we all? Look..."
            scene festivalnoche3:
                xsize 814
                ysize 625
            Villager "See? no shame, now I'm naked too, so you have nothing to be ashamed of"
            Leyna "I-It's just that my husband..."
            Villager "Johan? we just saw him back there, he's having a great time, he won't have time to get angry with the beer he's already drank"
            Leyna "W-well..."
            menu:
                "Go with current clothing":
                    Leyna "I guess you are right"
                    Villager "Exactly! let's go and have a drink with the others!"
                    Leyna "hahahaha Su-sure!"
                    scene festivalnoche4:
                        xsize 814
                        ysize 625
                    Villager "Here Leyna, have a beer"
                    Leyna "Thank you very much!"
                    scene festivalnoche5:
                        xsize 814
                        ysize 625
                    Leyna "Johan seems to be having a great time... I haven't seen him this relaxed for a long time"
                    Leyna "Is he dancing? hahahaha he must have had a lot of beers, he hates to dance"
                    Villager "Hey, aren't you going with your husband?"
                    Leyna "Yes, I'll be there in a moment... it looks like he's having a great time, I'm going to leave him alone for a little bit"
                    Villager "What a good wife! I wish you were married to me, a perfect woman in every way!"
                    Leyna "wow hahaha thanks"
                    scene pantallanegro:
                        xsize 979
                        ysize 720
                    "Some time later"
                    scene festivalnoche6:
                        xsize 814
                        ysize 625
                    Villager "Come on Leyna! keep the party going! hahahaha here's another beer!"
                    scene festivalnoche9:
                        xsize 814
                        ysize 625
                    Johan "(Le-leyna? I didn't even realize she was here.... my god she's still wearing the uniform from the food stand... it's .... very very revealing)"
                    Johan "(W-why didn't she come with me?.... I don't understand anything... I'd better go say hello and see what's going on)"
                    scene festivalnoche10:
                        xsize 814
                        ysize 625
                    Johan "Y-you..."
                    Alexa "Hey handsome... where are you going?"
                    Johan "I-I was going to..."
                    Alexa "Come have a beer with me!"
                    Johan "I don't know if I should... I'm already pretty drunk"
                    Alexa "Come on! and you call yourself a man?"
                    Johan "Of course! Give me that beer!"
                    Alexa "hahahaha that's the way I like it!"
                    scene pantallanegro:
                        xsize 979
                        ysize 720
                    "minutes later"
                    scene festivalnoche11:
                        xsize 814
                        ysize 625
                    Alexa "Heey Johan... let's dance"
                    Johan "I... I don't like to dance, Alexa..."
                    Alexa "Ohh come on Johan don't be shy we are going to have a great time...."
                    DrunkVillager "Yessssss, come on Johan a pretty girl is inviting you to dance... not accepting would be rude!"
                    DrunkVillager "E-hip!-exactly! Johan you are already the envy of the whole town, you have to dance with her!"
                    Johan "HeheHE hip! come on ... if you insist I can't refuse"
                    Villager "That's the way to talk, man"
                    scene festivalnoche12:
                        xsize 814
                        ysize 625
                    play music "audio/Psychedelic-Rock.ogg" loop volume 0.9
                    Alexa "Wow... it looks like you're getting a little happy down there"
                    Johan "W-well, tHat'S NorMal, IsN't iT? I'm A MaN aFfter All"
                    scene festivalnoche13:
                        xsize 814
                        ysize 625
                    Leyna "What! What is he doing? (my god... Johan is dancing in such a sexualized way with Alexa...)"
                    Leyna "I'm just really drunk, it's silly... or not! How dare you do that with another woman! Now you'll see!"
                    scene festivalnoche16:
                        xsize 814
                        ysize 625
                    Leyna "Hey you!"
                    Villager "M-me?"
                    Leyna "Y-yes you... let's dance come on"
                    DrunkVillager "OOOhh you lucky bastard"
                    Leyna "You want to dance too? come on, you come too!"
                    DrunkVillager "WOW! of course we will dance!"
                    scene festivalnoche17:
                        xsize 814
                        ysize 625
                    DrunkVillager "My God, you're sexy... wait a minute!"
                    DrunkVillager "(S-she's wearing a butt plug?... mother of god! She's a real nymphomaniac! Look at her going out in public like that!)"
                    scene festivalnoche19:
                        xsize 814
                        ysize 625
                    Villager "I-I'm sorry Leyna... I couldn't help but have an erection"
                    Leyna "N-no worries (is Johan watching?)"
                    scene festivalnoche17:
                        xsize 814
                        ysize 625
                    Johan "(My God, is that Leyna? What is she doing with those Villagers? I've never seen her dance like that with anyone.... I'm so drunk... it's hard for me to think..."
                    Johan "(Th-that guy is naked! and Leyna's backside is completely exposed... I'm getting dizzy...)"
                    scene black with dissolve
                    show festivalnoche20 with dissolve:
                        xsize 814
                        ysize 625
                    Johan "Uff I have definitely had too much to drink"
                    scene festivalnoche21:
                        xsize 814
                        ysize 625
                    Alexa "Take it easy, you're fine! Take a breath and we'll continue dancing some more"
                    Johan "Hahahaha yeah, you're right I'm fine"
                    "a little later"
                    scene festivalnoche22:
                        xsize 814
                        ysize 625
                    Johan "Wow how beautiful you are... although I feel a bit sick... I'm dizzy... where are we?"
                    Alexa "Where always silly, at the festival hahahaha"
                    Alexa "Why don't you give me a kiss? you'll feel better"
                    Johan "I-I can't, my wife has to be around...."
                    scene festivalnoche23:
                        xsize 814
                        ysize 625
                    Johan "Le-leyna? ahh... uff I'm really fucked up, I need to... I need to throw up"
                    Johan "I-Is that Leyna?"
                    Villager "Dude, are you okay?"
                    scene black with dissolve
                    show festivalnoche25 with dissolve:
                        xsize 814
                        ysize 625
                    Johan "Ufff I'm terrible... blueagggh... my god... blueeeghgghggh...."
                    Johan "I've never been like this before... bluueeeegh.... I'm going to die?.... blueueeeeeaaagagga"
                    if switch("corruption_average"):
                        scene festivalnoche26:
                            xsize 814
                            ysize 625
                        Johan "What's that? They're fucking a girl in the middle of the festival.... shit and I'm missing it"
                    if switch("corruption_low"):
                        scene festivalnoche26:
                            xsize 814
                            ysize 625
                        Johan "What's that? They're fucking a girl in the middle of the festival.... shit and I'm missing it"
                    Johan "When I tell Leyna she's going to be freaked out.... uff I think I need to throw up again...."
                    scene black with dissolve
                    show festivalnoche27 with dissolve:
                        xsize 814
                        ysize 625
                    Alexa "Are you ok Johan? you had me worried, you had been missing for quite a while"
                    Johan "Wow... you were worried about me... hehehehe you are so cute"
                    Alexa "Hehehee cute? it's been a while since I've heard that...."
                    scene festivalnoche28:
                        xsize 814
                        ysize 625
                    Johan "He-hey! I just threw up...you shouldn't kiss me... besides, I'm married"
                    Alexa "I don't care... let's make love right here, Johan..."
                    Johan "What?"
                    scene festivalnoche30:
                        xsize 814
                        ysize 625
                    Alexa "Yessssss... let's do it right now Johan, come on, I know you're looking forward to it"
                    menu:
                        "Fuck Alexa":
                            Johan "If you ask me that way... I can't say no to you honey"
                            Alexa "I knew you were dying for it...come on"
                            scene black with dissolve
                            show festivalnoche29 with dissolve:
                                xsize 814
                                ysize 625
                            play bgs "audio/audio follar.ogg" loop volume 0.9
                            Alexa "Like that... slowly... ahhh"
                            Alexa "Very good...."
                            Alexa "You certainly don't have as big a dick as the guys in this town, but at least you don't cum after 5 seconds"
                            Johan "Hehehehe I take it as a compliment"
                            Alexa "It is, let's go to a more comfortable place"
                            Johan "A more comfortable place?"
                            $ shake_screen()
                            $ flash_screen(wait=True)
                            stop bgs fadeout 1
                            Johan "I-I don't feel so good..."
                            scene pantallanegro:
                                xsize 979
                                ysize 720
                            Johan "OOohhhh"
                            Johan "My God!!! what is happening to me?"
                            Johan "What the hell was in the beers?"
                            Johan "I think ... yes ... I'm going to sleep ... I can't..."
                            scene black with dissolve
                            hide pantallanegro
                            stop music fadeout 1
                            # fade in
                        "I can't do it":
                            Johan "I-I'm sorry, I can't... I love Leyna"
                            Alexa "I see... too bad, you're a great guy... though your wife seems to be having a great time without you"
                            Johan "W-what?"
                            $ shake_screen()
                            $ flash_screen(wait=True)
                            stop bgs fadeout 1
                            Johan "I-I don't feel so good..."
                            scene pantallanegro:
                                xsize 979
                                ysize 720
                            Johan "OOohhhh"
                            Johan "My God!!! what is happening to me?"
                            Johan "What the hell was in the beers?"
                            Johan "I think ... yes ... I'm going to sleep ... I can't..."
                            scene black with dissolve
                            hide pantallanegro
                            stop music fadeout 1
                            # fade in
                "Change clothes":
                    Leyna "I-I'm sorry, but I'm still going to go change, I don't feel comfortable dressed like this"
                    Villager "Sure... okay, we'll wait for you here"
                    Leyna "Great, thank you very much"
                    scene festivalnoche7:
                        xsize 814
                        ysize 625
                    Villager "You've changed quickly"
                    Leyna "Hahahaha yeah, well... let's go ?"
                    Villager "Sure! here's a beer for you"
                    scene festivalnoche5:
                        xsize 814
                        ysize 625
                    Leyna "Johan seems to be having a great time... I haven't seen him this relaxed for a long time"
                    Leyna "Is he dancing? hahahaha he must have had a lot of beers, he hates to dance"
                    Villager "Hey, aren't you going with your husband?"
                    Leyna "Yes, I'll be there in a moment... it looks like he's having a great time, I'm going to leave him alone for a little bit"
                    Villager "What a good wife! I wish you were married to me, a perfect woman in every way!"
                    Leyna "wow hahaha thanks"
                    scene pantallanegro:
                        xsize 979
                        ysize 720
                    "Some time later"
                    scene festivalnoche7:
                        xsize 814
                        ysize 625
                    Villager "Come on Leyna! keep the party going! hahahaha here's another beer!"
                    scene festivalnoche8:
                        xsize 814
                        ysize 625
                    Johan "(Le-leyna? I didn't even realize she was here.... Good thing he changed his uniform before coming here)"
                    Johan "(W-why didn't she come with me?.... I don't understand anything... I'd better go say hello and see what's going on)"
                    scene festivalnoche10:
                        xsize 814
                        ysize 625
                    Johan "Y-you..."
                    Alexa "Hey handsome... where are you going?"
                    Johan "I-I was going to..."
                    Alexa "Come have a beer with me!"
                    Johan "I don't know if I should... I'm already pretty drunk"
                    Alexa "Come on! and you call yourself a man?"
                    Johan "Of course! Give me that beer!"
                    Alexa "hahahaha that's the way I like it!"
                    scene pantallanegro:
                        xsize 979
                        ysize 720
                    "minutes later"
                    scene festivalnoche11:
                        xsize 814
                        ysize 625
                    Alexa "Heey Johan... let's dance"
                    Johan "I... I don't like to dance, Alexa..."
                    Alexa "Ohh come on Johan don't be shy we are going to have a great time...."
                    DrunkVillager "Yessssss, come on Johan a pretty girl is inviting you to dance... not accepting would be rude!"
                    DrunkVillager "E-hip!-exactly! Johan you are already the envy of the whole town, you have to dance with her!"
                    Johan "HeheHE hip! come on ... if you insist I can't refuse"
                    Villager "That's the way to talk, man"
                    scene festivalnoche12:
                        xsize 814
                        ysize 625
                    play music "audio/Psychedelic-Rock.ogg" loop volume 0.9
                    Alexa "Wow... it looks like you're getting a little happy down there"
                    Johan "W-well, tHat'S NorMal, IsN't iT? I'm A MaN aFfter All"
                    scene festivalnoche14:
                        xsize 814
                        ysize 625
                    Leyna "What! What is he doing? (my god... Johan is dancing in such a sexualized way with Alexa...)"
                    Leyna "I'm just really drunk, it's silly... or not! How dare you do that with another woman! Now you'll see!"
                    scene festivalnoche15:
                        xsize 814
                        ysize 625
                    Leyna "Hey you!"
                    Villager "M-me?"
                    Leyna "Y-yes you... let's dance come on"
                    DrunkVillager "OOOhh you lucky bastard"
                    Leyna "You want to dance too? come on, you come too!"
                    DrunkVillager "WOW! of course we will dance!"
                    scene festivalnoche18:
                        xsize 814
                        ysize 625
                    DrunkVillager "My God, you're sexy..."
                    Villager "I-I'm sorry Leyna... I couldn't help but have an erection"
                    Leyna "N-no worries (is Johan watching?)"
                    Johan "(My God, is that Leyna? What is she doing with those Villagers? I've never seen her dance like that with anyone.... I'm so drunk... it's hard for me to think..."
                    Johan "(Th-that guy is naked!... I'm getting dizzy...)"
                    scene black with dissolve
                    show festivalnoche20 with dissolve:
                        xsize 814
                        ysize 625
                    Johan "Uff I have definitely had too much to drink"
                    scene festivalnoche21:
                        xsize 814
                        ysize 625
                    Alexa "Take it easy, you're fine! Take a breath and we'll continue dancing some more"
                    Johan "Hahahaha yeah, you're right I'm fine"
                    scene pantallanegro:
                        xsize 979
                        ysize 720
                    "a little later"
                    scene festivalnoche22:
                        xsize 814
                        ysize 625
                    Johan "Wow how beautiful you are... although I feel a bit sick... I'm dizzy... where are we?"
                    Alexa "Where always silly, at the festival hahahaha"
                    Alexa "Why don't you give me a kiss? you'll feel better"
                    Johan "I-I can't, my wife has to be around...."
                    scene festivalnoche24:
                        xsize 814
                        ysize 625
                    Johan "Le-leyna? ahh... uff I'm really fucked up, I need to... I need to throw up"
                    Johan "I-Is that Leyna?"
                    Villager "Dude, are you okay?"
                    scene black with dissolve
                    show festivalnoche25 with dissolve:
                        xsize 814
                        ysize 625
                    Johan "Ufff I'm terrible... blueagggh... my god... blueeeghgghggh...."
                    Johan "I've never been like this before... bluueeeegh.... I'm going to die?.... blueueeeeeaaagagga"
                    if switch("corruption_average"):
                        scene festivalnoche31:
                            xsize 814
                            ysize 625
                        Johan "What's that? it looks like there's a girl dancing topless.... shit and I'm missing it"
                    if switch("corruption_low"):
                        scene festivalnoche31:
                            xsize 814
                            ysize 625
                        Johan "What's that? it looks like there's a girl dancing topless.... shit and I'm missing it"
                    Johan "When I tell Leyna she's going to be freaked out.... uff I think I need to throw up again...."
                    scene black with dissolve
                    show festivalnoche27 with dissolve:
                        xsize 814
                        ysize 625
                    Alexa "Are you ok Johan? you had me worried, you had been missing for quite a while"
                    Johan "Wow... you were worried about me... hehehehe you are so cute"
                    Alexa "Hehehee cute? it's been a while since I've heard that...."
                    scene festivalnoche28:
                        xsize 814
                        ysize 625
                    Johan "He-hey! I just threw up...you shouldn't kiss me... besides, I'm married"
                    scene festivalnoche30:
                        xsize 814
                        ysize 625
                    Alexa "I don't care... let's make love right here, Johan..."
                    Johan "What?"
                    Alexa "Yessssss... let's do it right now Johan, come on, I know you're looking forward to it"
                    menu:
                        "Fuck Alexa":
                            Johan "If you ask me that way... I can't say no to you honey"
                            Alexa "I knew you were dying for it...come on"
                            scene black with dissolve
                            show festivalnoche29 with dissolve:
                                xsize 814
                                ysize 625
                            play bgs "audio/audio follar.ogg" loop volume 0.9
                            Alexa "Like that... slowly... ahhh"
                            Alexa "Very good...."
                            Alexa "You certainly don't have as big a dick as the guys in this town, but at least you don't cum after 5 seconds"
                            Johan "Hehehehe I take it as a compliment"
                            Alexa "It is, let's go to a more comfortable place"
                            Johan "A more comfortable place?"
                            $ shake_screen()
                            $ flash_screen(wait=True)
                            stop bgs fadeout 1
                            Johan "I-I don't feel so good..."
                            scene pantallanegro:
                                xsize 979
                                ysize 720
                            Johan "OOohhhh"
                            Johan "My God!!! what is happening to me?"
                            Johan "What the hell was in the beers?"
                            Johan "I think ... yes ... I'm going to sleep ... I can't..."
                            scene black with dissolve
                            hide pantallanegro
                            stop music fadeout 1
                            # fade in
                        "I can't do it":
                            Johan "I-I'm sorry, I can't... I love Leyna very much"
                            Alexa "I see... too bad, you're a great guy... though your wife seems to be having a great time without you"
                            Johan "W-what?"
                            $ shake_screen()
                            $ flash_screen(wait=True)
                            stop bgs fadeout 1
                            Johan "I-I don't feel so good..."
                            scene pantallanegro:
                                xsize 979
                                ysize 720
                            Johan "OOohhhh"
                            Johan "My God!!! what is happening to me?"
                            Johan "What the hell was in the beers?"
                            Johan "I think ... yes ... I'm going to sleep ... I can't..."
                            scene black with dissolve
                            hide pantallanegro
                            stop music fadeout 1
                            # fade in
        "No":
            pass
    return

label GalleryRiverWithAlexa2_1(menu_choice = None):
    "River with Alexa 2"
    "Do you want to see it?"
    menu:
        "Yes":
            Johan "Well, whatever, I guess it doesn't matter so much if they see our naked bodies... we are both adults and this is something natural"
            Leyna "Yes, you are right"
            scene black with dissolve
            show riosexo1 with dissolve
            Alexa "Hey! you finally came! I didn't know if you would come with how reserved you are about your bodies!"
            Johan "Reserved... (Well, I guess from her point of view it may seem so, although I think she is just too... open about it)"
            Leyna "Yes... I'm still not used to it, but with Johan here I feel more relaxed"
            Alexa "Great! Well, you know Johan, stay close to your wife hehehehehe"
            Alexa "Come and have a beer with us!"
            "Leyna. M-more beer?"
            Johan "I don't know how you can keep drinking, we've practically been partying for days"
            Alexa "Oh come on, don't overreact!"
            Alexa "Come on, take one!"
            Johan "Okay... but just one"
            scene riosexo2
            Johan "Well... I have to admit that you are right Alexa, with a couple of shots of beer I already feel much better"
            Alexa "I told you so! Between the beer and being naked here, one's spirits are raised no matter how bad one feels"
            pause
            scene riosexo3
            Villager "Hey! how are you guys? I haven't seen you for a couple of days..."
            Leyna "He-hello"
            Johan "Hey... hmmm How's it going?"
            Villager "Here we are, having a beer by the river, enjoying the holidays before the routine starts again"
            pause
            scene riosexo4
            Johan "(His penis is rubbing Leyna...) I see, I can't imagine this town living a normal life, does it change much when the festival is over?"
            Villager "Yes! too much, I wish it was like this all year round, but the truth is that once the festival is over, life here is normal and ordinary"
            Villager "I guess when the festival starts everyone goes a little crazy hahahaha"
            Leyna "Let's take a bath Johan"
            Johan "Oh, sure, it'll come in handy in this hot weather"
            Villager "Yeah! see you later! have fun, guys!"
            pause
            scene black with dissolve
            show riosexo5 with dissolve
            Johan "Who was that guy?"
            Leyna "... I don't know, it's a little difficult for me to differentiate the people of this town, we have met so many in the last few days..."
            Johan "Hahahaha you can say that again... I'm glad I'm not the only one"
            scene riosexo6
            Johan "Alexa... she always seems to be very comfortable naked and surrounded by guys... didn't she come to town with her husband?"
            Johan "I haven't seen him for days... I don't know what he will think of all this"
            Leyna "!!!... yeah... I guess they have some kind of open relationship... or so I hope"
            Johan "Yeah... I'm not so sure about that but okay...."
            Johan "Poor guy..."
            Leyna "!!!!... Y-yes"
            pause
            scene riosexo7
            Johan "Oh there you go... I knew something like this was about to happen"
            Johan "They're not going to do it in front of everyone, are they?"
            scene riosexo8
            Leyna "I-I don't know... I don't think so, right?"
            Johan "After everything I've seen, nothing surprises me anymore"
            pause
            scene riosexo9
            Johan "!!! (they are doing it in front of everyone)"
            Leyna "..."
            Leyna "(I-I'm starting to get horny watching this, I hope Johan doesn't notice....)"
            pause
            scene riosexo10
            Johan "(Fuck, they're not disguising shit, I'm embarrassed but I can't stop looking)"
            Johan "(Besides, I have it hard as a rock, I can't get out of the water like this)"
            Johan "(Although Leyna... hold on a second...)"
            Johan "(Leyna is red as a tomato... she seems to be very horny... I didn't know she liked this kind of things)"
            Johan "(Wait a minute... is she touching herself? I can't help but get even more excited seeing my wife like that...)"
            Johan "(... I can't help it... I must take advantage of this situation)"
            scene riosexo11
            Leyna "!!!!"
            Johan "Let me give you a hand with that...."
            Leyna "Johan..."
            pause
            scene riosexo12
            Leyna "Hmmmfff!"
            Johan "You sure are horny... you're on fire"
            Leyna "J-Johan!"
            Johan "Let me help you with that"
            Leyna "aaahh..."
            pause
            scene riosexo13
            Leyna "Johan... fuck me..."
            Johan "Here?.... very well, but let's try to disguise it a little bit"
            Leyna "Let me get on top..."
            scene riosexo14
            Johan "Oh!"
            Johan "I can see you were looking forward to it"
            Johan "God... you are so hot down there"
            Leyna "Ah... shut up and fuck me"
            Johan "Yeah..."
            scene riosexo17
            Leyna "Hmmmf... ahh"
            Johan "Ssshhhh shut up or they will hear us..."
            Leyna "I-I don't care... I don't care if they can hear us, just fuck me"
            if johan_leyna_sex == 1:
                Leyna "(Johan... he's feeling a bit weird... since the other day when we did it he got a bit nervous... now he's a bit clumsy)"
                Leyna "(I'm barely enjoying it...)"
                Leyna "F-faster..."
                Johan "I'm trying... there are so many people around"
                Johan "(I can't concentrate... I can't get out of my head everything that has been going on these last few days)"
                Leyna "(My God... he is doing terrible... what is happening to Johan lately? has he changed?... or is it me that has changed?)"
                pause
                scene riosexo18
                Villager "Hey... I see you need a hand"
                Leyna "Wait"
                Johan "???"
                Villager "Come on, I know you're looking forward to it, doing something like that in front of everybody"
                pause
                scene riosexo19
                play bgs "audio/audio follar.ogg" loop volume 0.9
                Johan "!!! what's going on? (I can't see anything from here... there's someone next to us?)"
                Leyna "Aghghgagagh!"
                Villager "Like this! I want to feel your tonsils!"
                Johan "(Wait, that sound! There's a guy sticking his dick in Leyna's mouth! While I'm here fucking her!)"
                Johan "H-hey! ... oh my god"
                scene riosexo20
                Johan "(L-Leyna's pussy is convulsing, she looks like she's about to have an orgasm right now! Holy cow it feels so good.... )"
                Johan "F-fuck!!"
                Johan "(H-he's fucking me! Leyna is moving like crazy!... FUCK!i'm going to cum! b-but there's a guy right there rubbing his dick in Leyna's mouth!)"
                Johan "(Shit, I can't take it anymore! I'm coming!)"
                Johan "AAHHH!"
                Leyna "(J-johan just cum? right now? while all this is going on?)"
                Johan "Ah ah ah!"
                pause
                scene riosexo21
                Johan "(Wait! There's really a guy here!)"
                Johan "H-Hey! get off of my wife right now Get out!"
                Villager "Oh come on, I'm about to finish"
                Johan "I told you to get out! get out now!"
                pause
                stop bgs fadeout 1
                scene riosexo22
                Villager "TCh! fuck man! ok ok, I'm leaving, next time don't fuck in public if you don't want someone else to join the party."
                Johan "Leave!"
                Villager "I'm leaving... I'll catch you around, honey"
                Leyna "Ah ah ah!"
                pause
                scene riosexo23
                Johan "What a waste of time... come on, let's go..."
                Leyna "Y-yes (waste of time? but you just cummed inside me... you came so fast... were you liking it johan?)"
                scene black with dissolve
                hide riosexo23
                # fade in
            if johan_leyna_sex == 2:
                scene riosexo16
                play bgs "audio/audio follar.ogg" loop volume 0.9
                Leyna "Oh!"
                Leyna "(My God, J-Johan is fucking me like that day...)"
                Leyna "M-my God... if you keep this up I-I'm going to cum..."
                Johan "Perfect! cum, that's what I want"
                Leyna "Ah.... hmmm...."
                pause
                scene riosexo18
                Villager "Hey guys, I see you're having a good time"
                Leyna "Hmmff?"
                Villager "Doing this here, I guess you want me to give you a hand, don't you?"
                Leyna "(Dios mio casi me la mete en la boca sin avisar)"
                stop bgs fadeout 1
                Johan "Hey! What the hell are you doing! Get out of the way right now!"
                Villager "D-don't you want some help?"
                Johan "N-no, we're fine, man, thanks, but back off, we'll take care of it ourselves"
                Villager "Since you were here doing it in front of the whole world I thought that..."
                Johan "You thought wrong"
                Villager "Okay guys, sorry"
                scene black with dissolve
                show riosexo24 with dissolve
                Leyna "Ah ah ah...."
                Leyna "Shall we continue?"
                Johan "Hehehehe Do you want to continue?"
                Leyna "Y-yes..."
                Johan "Then we continue"
                pause
                scene black with dissolve
                play bgs "audio/audio follar.ogg" loop volume 0.9
                show riosexo25 with dissolve
                "Minutes later"
                Leyna "Ah! ah! ah! M-my God... I'm cumming!"
                Johan "That's the way I like it, cum! come on! I want to see you writhing with pleasure!"
                Leyna "Ah ah! ah m-my god... so fast! you're drilling me"
                Johan "Ah! ah ah ah!"
                Leyna "Ooohh!!! ahh!!"
                Villager "(whispering) Jesus Christ, it didn't look like it but that guy is a fucking machine... now I understand why she's with him"
                Villager2 "(whispering) who would have thought..."
                Johan "That's how I like it"
                pause
                scene black with dissolve
                stop bgs fadeout 1
                show riosexo26 with dissolve
                Leyna "I-I see that you've cum too..."
                Johan "hahahaha yes, I couldn't help it"
                Johan "!!!!"
                Johan "Shit, everyone is watching us, let's get out of here and take a nice hot shower"
                Leyna "Yes, good idea"
                "Leyna. (My God I'm still shaking... it's going to be hard for me to get up... what a fuck he has given me... Johan has improved since we arrived)"
                scene black with dissolve
                hide riosexo18
                hide riosexo24
                hide riosexo25
                hide riosexo26
                # fade in
        "No":
            pass
    return

label GalleryPhotoshootInTheHotsprings_1(menu_choice = None):
    "Photoshoot in the hotsprings"
    "Do you want to see it?"
    menu:
        "Yes":
            scene pantallanegro:
                xsize 979
                ysize 720
            "Several minutes later"
            Leyna "This is the clothes I have to wear? it's a bit.... well, I'm surprised"
            Johan "??? show me"
            scene photohot1
            Leyna "After the last session I was expecting something more revealing, it's just a swimsuit"
            pause
            scene photohot2
            Johan "Well yes... although you look great hehehe (Thank God! what a relief!!! this session I imagine it won't be as explicit as the previous one!)"
            OldMan "Oh yes, I was surprised too, they sent it to me from the magazine, they told me it was a special swimsuit but to me it looks like an ordinary one"
            YoungVillager "Wow Leyna! as beautiful as always!"
            Leyna "!!!"
            scene photohot3
            Leyna "Y-you!"
            Johan "Oh, hey, you're the guy from the other day!"
            YoungVillager "In the flesh..."
            Leyna "What are you doing here?"
            scene photohot4
            YoungVillager "Well, I needed some money and the photographer told me that I fit the profile he was looking for, so why not?"
            Leyna "I-I see (I don't trust this guy, I hope he doesn't do anything stupid in front of Johan...)"
            YoungVillager "It will be a pleasure to work with you Leyna, of course it will be a new experience for me, so treat me well, ok?"
            Leyna "Sure, let's be professionals and let's work together to make this happen"
            Villager "Yeah!"
            scene photohot5
            Leyna "(This guy gives me the creeps, just by looking at his face you know he is not clean... but he is very persuasive... that time in the bar...)"
            Leyna "(If I had known I was going to end up in this situation this morning I would'nt have had a few beers with Alexa)"
            Leyna "(But the party atmosphere in this town is contagious... )"
            scene photohot6
            OldMan "Well, I see you are motivated for today! All right then, everyone go to your positions"
            OldMan "Let's start with you Leyna and then the guys will join us, Johan, from here you can see everything, if you want to get closer you can do it"
            OldMan "As long as you are not in the frame you can stand wherever you want, okay?"
            Johan "Sure..."
            OldMan "Okay, let's get started!"
            scene pantallanegro:
                xsize 979
                ysize 720
            OldMan "Very good Leyna put yourself there, perfect"
            scene photohot7
            OldMan "Okay, get down on your knees, let's start with some simple photos"
            Leyna "Okay..."
            scene photohot8
            Leyna "Is this position okay?"
            OldMan "That's perfect, stay still"
            Leyna "Yeah"
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "Perfect, now lean in and approach me"
            Leyna "All right..."
            pause
            scene photohot9
            Leyna "Something like this?"
            OldMan "Yes..."
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "Now squat down, like in those reggaeton videos that are so popular"
            Leyna "Okay, I'll give it a try (so far it doesn't look as erotic as usual... thank goodness)"
            pause
            scene photohot10
            Leyna "So-something like that? it's a little uncomfortable"
            OldMan "Great, hold on to that position for a bit!"
            YoungVillager "Wow, Hot!"
            Villager "Yes, from here we have spectacular views hahahaha"
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            pause
            scene photohot37
            Johan "(I don't find it funny when people talk about Leyna like that, especially in front of me)"
            Johan "(But at least it seems that today's session is less erotic than the previous one)"
            Johan "(Even Leyna seems to be starting to have a good time ... at least she's more relaxed than before,she seemed a bit tense)"
            Johan "(Although I don't know if I should be happy about it...)"
            OldMan "All right Leyna, get in the water, let's do the next position inside"
            Leyna "Okay"
            play sound "audio/Water1.ogg" volume 0.9 noloop
            Johan "!!!!"
            scene photohot11
            play music "audio/Dungeon3.ogg" loop volume 0.9
            Leyna "!!!"
            Leyna "I already imagined that it was not a normal swimsuit... it shows through everything"
            OldMan "Well, the magazine people hadn't told me anything, but it's better for us, otherwise the session would be very boring"
            OldMan "Look, stay as you are, it's a good position and I like your expression of surprise"
            Leyna "Sure, have it your way"
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "Perfect, now a small zoom to highlight the interesting parts"
            Johan "(Interesting parts?)"
            scene photohot12
            OldMan "Perfect, one more photo in this position and the kids can go in"
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "Okay, guys, come here, let's start with you"
            Villager "All right!"
            YoungVillager "Well, let's get started... I'm a little nervous"
            OldMan "Don't worry, you will do well, you are very young and you have a lot of energy"
            Johan "(what the hell does he mean by that... now that Leyna is showing practically everything I'm not liking this at all)"
            scene photohot13
            YoungVillager "Well, here we are, how do we get on?"
            OldMan "This way you are perfect for the first photo, stand still"
            Villager "Sure"
            Leyna "..."
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "Okay now both of you touch him on his belly and you pretend to kiss his neck"
            Villager "O-okay"
            Johan "!!!"
            Johan "(Shit, things are starting to get too spicy for my taste...should I stop it? but I don't want Leyna to lose her job because of me)"
            scene photohot14
            OldMan "That's it! very good, stay still"
            Leyna "(.... he was supposed to pretend he was kissing my neck, not really kissing it...this guy is taking advantage)"
            Leyna "(although it feels so good... I feel chills all over my spine and the back of my neck.... does it have something to do with the herbs they put in the water?)"
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "All right, that's enough, now, Leyna turn around and get your ass up"
            Leyna "! Su-sure"
            Johan "(what is he intending to do?)"
            OldMan "All right guys, time to bring out the artillery, take off your loincloths and get your dicks out, I want you to grab them and smack Leyna's ass with them"
            Johan "!!!! B-but!"
            scene photohot15
            Villager "Sure!"
            YoungVillager "It will be a pleasure! (Slap slap slap slap)"
            Leyna "!!! (They've already started hitting me with their dicks and Johan is right there... he seems to be a bit shocked with what's going on)"
            Villager "(Slap slap slap) Does this look good to you?"
            OldMan "Yes! I recorded a short video with the camera to send it to them, they wanted to make a gif for the web page"
            OldMan "Now, stand still"
            Villager "Yeah"
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "Great, Leyna, turn around"
            Leyna "O-okay"
            pause
            scene photohot16
            OldMan "Perfect, guys, stay like this! with your penises as close to her as possible"
            Villager "Glad to do it"
            Johan "(Shit... I would like nothing more than to stop this nonsense, control yourself Johan, don't be like this,  the previous one was worse...)"
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "You guys are doing great, what a stamina you have, I don't know how you can last so long with that erection"
            YoungVillager "Well, with Leyna in this position and so close to us we don't have to try very hard hahahaha"
            Villager "Yes! it's rare to see such a sexy woman even in a porn magazine"
            OldMan "Ah, youth is a wonderful thing!"
            Johan "(Shut the fuck up...)"
            OldMan "All right, now lift her up by her legs, it' s going to look great in the photo"
            pause
            scene photohot17
            Leyna "Oh!"
            Villager "Like this?"
            OldMan "That's perfect!"
            Villager "Miss, you weigh nothing"
            Leyna "hahahaha shut up, I know I've put on weight, don't suck up to me"
            Johan "(Leyna is laughing with them? are they flirting? Shit...)"
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "A spectacular photo"
            OldMan "Now take her down and... pull down her swimsuit, let those tits be seen well"
            Villager "Sure! it will be a pleasure"
            Johan "Wh-what?!"
            Leyna "!"
            scene photohot18
            Leyna "Ah! you-could warn before doing something like that!"
            Villager "Sorry"
            Leyna "N-no problem"
            OldMan "Perfect as always"
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "this is turning out to be a very good photo shoot, I'm sure the magazine will be very happy with your work"
            Leyna "Thanks..."
            OldMan "All right boy, lift Leyna's leg, it's time to turn it up a notch"
            pause
            scene photohot19
            OldMan "Very good, that position is perfect, hold it like that a little longer"
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "This is very good, now you have to move the lower part of the bathing suit a little bit so that her pussy is open to the air"
            Leyna "!!!!"
            Villager "Okay, I'm going to do it, okay Leyna?"
            Leyna "I-I don't know if I should..."
            OldMan "Come on Leyna, you can see practically everything, the magazine has asked us for it"
            Leyna "Well... okay"
            Johan "(Wait, she agrees just like that? in the previous session something similar and worse happened... but I'm not sure about it)"
            pause
            scene photohot20
            OldMan "Great"
            OldMan "From close it looks perfect, I'm going to take a good picture"
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "Please, place your member against Leyna's pussy, let it touch it lightly"
            Villager "Okay"
            pause
            scene photohot21
            Leyna "(I'm starting to get wet down there... I hope they don't notice, with all these fumes they might think it's just humidity...)"
            Villager "(Whispering) Wow, your pussy is so wet.... You get excited very fast, don't you?"
            Leyna "!!! (He noticed!)"
            $ flash_screen(wait=True)
            play sound "audio/Key.ogg" volume 0.9 noloop
            OldMan "a spectacular photo! let's advance a little more and introduce the tip little by little, I want to take a couple of photos of the process"
            Villager "Sure!"
            Johan "(Wait, what?! Stick it in? They're going to stick their dicks in my wife right here while they're photographing it?)"
            menu:
                "Say nothing":
                    scene photohot39
                    Johan "(It's like that time... I can't help but remain silent as I watch all this happen)"
                    Johan "(I feel like vomiting again, while I have a feeling of vertigo... but at the same time I have an uncontrollable erection)"
                    Johan "(I feel like a shithead and a coward)"
                    scene photohot23
                    $ flash_screen(wait=True)
                    play sound "audio/Key.ogg" volume 0.9 noloop
                    Leyna "Oh! hmmmm!"
                    Villager "It's going in like it's nothing... you're dripping"
                    Leyna "Shu-shut up"
                    Villager "(Whispering) Or what? your husband is right there looking like an idiot watching everything and he hasn't said a word"
                    Leyna "!!! I-I, don't talk like that about my hus..."
                    pause
                    scene photohot24
                    Leyna "HMMAAH!! MY GOD!"
                    Johan "(My wife just moaned?....)"
                    Villager "What were you saying? I didn't hear you"
                    Leyna "Ah ah ah! Ass-asshole"
                    $ flash_screen(wait=True)
                    play sound "audio/Key.ogg" volume 0.9 noloop
                    OldMan "You guys are doing great"
                    OldVillager "Now take it out, I want to take another picture from that angle"
                    Villager "... Sure, whatever you say"
                    pause
                    scene photohot25
                    Leyna "(I feel it deep inside of me.... feeling it so deep inside me I'm already about to cum)"
                    Villager "(Whispering) Too bad I have to take it out, isn't it? I can feel you contracting in there, you're about to cum, aren't you?"
                    Leyna "!!!! N-no"
                    Villager "Well then I'm going to take it out"
                    Leyna "!!! hmma"
                    scene photohot26
                    $ flash_screen(wait=True)
                    "Plop"
                    Leyna "Oh my god..."
                    OldMan "What a great sound, you were having a good time Leyna"
                    Johan "(Having a good time...? Leyna was enjoying it?)"
                    Johan "(Of course she was enjoying herself, just look at her face, she' s as red as a tomato and has an orgasmic expression...)"
                    Johan "(I should never have agreed to this)"
                    $ flash_screen(wait=True)
                    play sound "audio/Key.ogg" volume 0.9 noloop
                    OldMan "All right Leyna, climb on the young guy, let's go to the next position"
                    Leyna "Ah ah ah... O-okay..."
                    pause
                    scene photohot27
                    Leyna "Li-like this? Is that okay?"
                    OldMan "That's fine"
                    $ flash_screen(wait=True)
                    play sound "audio/Key.ogg" volume 0.9 noloop
                    OldMan "Do you have your dick pressed against his ass?"
                    Villager "Yes, I have it"
                    OldMan "All right, I'm going to take a picture from below"
                    pause
                    scene photohot28
                    OldMan "Yes... This angle is very good"
                    $ flash_screen(wait=True)
                    play sound "audio/Key.ogg" volume 0.9 noloop
                    OldMan "Of course the magazine is going to love it, but especially the next picture, guys...."
                    OldMan "I want both of you to stick it in her at the same time, one in each hole, be careful not to hurt Leyna, she is our star model"
                    Johan "(WHAT?! They're going to stick it in both sides?! I'm sure Leyna won't agree...)"
                    Leyna "W-what do you mean, one on each side?! that's too much, guys! you're going to break me in half!"
                    OldMan "No way lady! don't worry, the guys will be careful and besides... you'd be surprised how far a woman's body can go!"
                    Leyna "B-but!"
                    OldMan "Relax, think about what the magazine is going to pay us! When you get a new car, you will forget all this!"
                    Leyna "I..."
                    Johan "(It can't be... this can't be happening)"
                    pause
                    scene photohot29
                    $ flash_screen(wait=True)
                    Leyna "!!! OH MY GOD! OHHHH"
                    Villager "Hahahaha seems to be liking it"
                    YoungVillager "It's a pity we can't move... I wish we weren't working and we could have a good time"
                    $ flash_screen(wait=True)
                    play sound "audio/Key.ogg" volume 0.9 noloop
                    pause
                    scene photohot31
                    OldMan "Leyna everything ok?"
                    Leyna "Aaahh ah ahhh ...."
                    YoungVillager "I don't think she can talk right now, with two cocks deep inside her hahahaha"
                    Johan "(They are laughing, they are making fun of Leyna while they fuck her like animals.... well they are still, but nevertheless)"
                    Johan "(And here I am, looking like a fucking loser, unable to move and with my dick as hard as a rock...)"
                    Johan "(How could I let this happen? how could I let us get into this situation? after this... how am I going to look her in the eyes?)"
                    $ flash_screen(wait=True)
                    play sound "audio/Key.ogg" volume 0.9 noloop
                    OldMan "All right guys, that's enough, go down to Leyna and have her give you a titfuck, it'll be great for the end"
                    YoungVillager "A titfuck?! great!"
                    pause
                    scene photohot32
                    YoungVillager "Wow it feels amazing! keep it up Leyna and I'll be cumming in no time!"
                    Leyna "I-I see..."
                    $ flash_screen(wait=True)
                    play sound "audio/Key.ogg" volume 0.9 noloop
                    OldMan "Very well done guys, the photo came out spectacular"
                    YoungVillager "Well, we've got a real pro here.... my god, what a soft tits you have Leynar"
                    Villager "Hey I'm getting jealous, come here"
                    Leyna "???"
                    OldMan "Wai..."
                    pause
                    scene photohot33
                    play bgs "audio/audio follar.ogg" loop volume 0.9
                    OldMan "Oh well... I guess it's okay to let off some steam after all"
                    Leyna "???? AAuughggaah"
                    Villager "What are you saying? I can't hear you, Leyna"
                    $ flash_screen(wait=True)
                    play sound "audio/Key.ogg" volume 0.9 noloop
                    OldMan "It is certainly a good photo..."
                    Leyna "(I c-can't breathe)"
                    Villager "Oooh I'm going to cum... I've been holding it in for a long time!"
                    YoungVillager "Me too!"
                    Villager "Get ready Leyna here I come!"
                    Leyna "???"
                    $ flash_screen(wait=True)
                    scene photohot34
                    Leyna "Wh-what are you doing?"
                    Villager "Open your mouth Leyna! OPEN IT, IT'S COMING!"
                    Leyna "Ah?"
                    Johan "(You're not going to do it, are you? Leyna!)"
                    pause
                    scene photohot35
                    $ flash_screen(wait=True)
                    stop bgs fadeout 1
                    Villager "OOOooohh!!!!!"
                    YoungVillager "OOOoohh Shit!!"
                    Villager "A little more and my dick explodes!"
                    pause
                    scene photohot36
                    Leyna "Ah... ah ah ah...."
                    OldMan "Very good Leyna! stay like this!"
                    $ flash_screen(wait=True)
                    play sound "audio/Key.ogg" volume 0.9 noloop
                    OldMan "WWOW perfect! we will get paid a lot for this last picture very good idea guys!"
                    Villager "Thanks!"
                    YoungVillager "Look at her! she is like a work of art, I feel like a real artist!"
                    OldMan "Well with this we have finished"
                    OldMan "Leyna, there is a shower back there, I think you need it"
                    Villager "You're telling me..."
                    scene black with dissolve
                    hide photohot36
                    # fade in
                "Hey!!":
                    Johan "(I-I can't let that happen!)"
                    scene photohot40
                    Johan "Hey! stop right now!!!"
                    Leyna "!!!! (Johan!)"
                    OldMan "What? What are you saying?"
                    Johan "I said stop right now! I'm not going to let them fuck my wife right under my nose!"
                    OldMan "Fuck..."
                    Villager "Wow, the husband has grown some balls"
                    Johan "Shut the fuck up you dumb fuck!"
                    Villager "..."
                    Johan "Leyna get out of there right now, let's get out of here"
                    Leyna "Y-yeah"
                    OldMan "Do you even know what you are doing? it's a golden opportunity!"
                    Johan "I don't give a fuck, we're leaving... and forget about Leyna as a model for your fucking magazine"
                    OldMan "You're losing a lot of money right now...."
                    Johan "I don't care! But you'd better pay my wife for the sessions she's already done!"
                    Johan "My best friend in town is a hell of a lawyer and he can have your balls cut off in court if you don't pay us"
                    OldMan "!!! O-okay, don't get like that Johan, as soon as I get the money I'll give it to you"
                    Johan "All right, now we're leaving!"
                    Leyna "Y-yes"
                    scene black with dissolve
                    hide photohot40
                    # fade in
        "No":
            pass
    return

