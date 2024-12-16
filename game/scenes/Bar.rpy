label BarWetTShirt_0:
    play music "audio/Town2.ogg" loop volume 0.9
    pause 0.22
    Johan "Wow, this place is full of people, it may be a good chance to interview someone"
    show plano_mujer_sorpresa_lado:
        xsize 1600
        ysize 900
    Leyna "I don't know ... it seems that they're a bit out of control ..."
    Johan "Don't worry they're only partying, in my town they also get like this when it's the time of the summer festivals"
    hide plano_mujer_sorpresa_lado
    pause 0.26
    show expresion_neutral_mujer:
        xsize 1600
        ysize 900
    Leyna "Excuse me, can I talk to you for a sec..."
    pause 0.22
    Villager "OH WOW I've died? There's an angel in front of me"
    hide expresion_neutral_mujer
    show plano_mujer_cartoon:
        xsize 1600
        ysize 900
    Leyna "I... hahahaha thank you, I'm with my husband, It's our first time here"
    Villager "Your Husband?..."
    DrunkVillager "HEY JOHN COME HERE!"
    pause 0.2
    John "I can't right now, wait a second!"
    DrunkVillager "WHAT? COME ON!"
    hide plano_mujer_cartoon
    stop music fadeout 1
    pause 0.22
    call ShowAnimation(82, "Barleyna", "BarWetTShirt_0") from _call_BarWetTShirt_0_ShowAnimation
    play sound "audio/Absorb1.ogg" volume 0.9 noloop
    DrunkVillager "Oh shit, sorry... oh??"
    DrunkVillager "...!"
    pause 0.22
    "Crowd: ....."
    play music "audio/Dungeon3.ogg" loop volume 0.9
    scene escena_camisa_mojada_1:
        xsize 832
        ysize 450
    Leyna "(He has spilled the beer on me!...)"
    "Crowd: Uoooh!"
    DrunkVillager "(You can see everything!)"
    John "Incredible, this festival has started in a spectacular way!"
    pause
    scene escena_camisa_mojada_2:
        xsize 832
        ysize 450
    Leyna "Ah?"
    if switch("netorare"):
        Johan "(Shit, everyone is staring at her)"
    if switch("netorase"):
        Johan "(Everyone is looking at Leyna... and you can see everything through her t-shirt... it's like... the video I saw yesterday...)"
        Johan "(God am I... I'm enjoying this? I have to end this situation or.... maybe someone will notice)"
    pause
    scene escenas_camisa_mojada_3:
        xsize 832
        ysize 450
    Leyna "Do-don't look!"
    DrunkVillager "Yeah nah, I'm going to keep looking"
    Johan "We better leave for now, we'll be back another time"
    pause
    stop music fadeout 1
    hide escenas_camisa_mojada_3
    $ player_location = "Town"
    pause 0.26
    Johan "Wow that has been ... weird"
    Leyna "Yes, sorry. With the heat, I haven't put on a bra because it makes me uncomfortable"
    Johan "Don't worry, it's not your fault"
    Johan "Let's get back to the inn so you can change your clothes"
    $ set_switch("wet_shirt", True)
    $ set_switch("dry_shirt", True)
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    $ player_location = "Town"
    pause 0.24
    $ corruption = corruption + 1
    "CORRUPTION +1"
    return

label BarBJGame_0(menu_choice = None):
    Villager "Hmm sorry, I heard that your husband and you are writing an article about the town"
    show expresion_neutral_mujer:
        xsize 1600
        ysize 900
    Leyna "Oh... that's right"
    Villager "Why don't you have a drink with us so we can talk about it? By the way, I'm sorry about yesterday..."
    show plano_mujer_sorpresa_lado:
        xsize 1600
        ysize 900
    hide expresion_neutral_mujer
    "... it was an unpleasant accident and I don't want you to think badly of us"
    Leyna "(I shouldn't do it. I get drunk very quick )"
    Leyna "(I remember the day I went to party with my friends ... the alcohol makes me behave in a way... that I don't like)"
    Leyna "(But it's a good way to find out about the festival and meet the townspeople)"
    menu:
        "Yes":
            show plano_mujer_sonrisa:
                xsize 1600
                ysize 900
            hide plano_mujer_sorpresa_lado
            Leyna "Sure guys, I could ask you some questions while drinking a beer"
            Villager "(Wow, I didn't expect her to accept ... I've been told what happened in the river... It's true, this girl is very naive)"
            Villager "Great! Let me pay the first few rounds"
            Leyna "Wow, thank you!"
            scene black with dissolve
            hide plano_mujer_sonrisa
            $ player_location = "Bar"
            # fade in
            "(SEVERAL BEERS LATER... )"
            Villager "... So yes, we expose our bodies on the festival place to honour the fertility goddess. As you may have noticed, the nudity in this town"
            ".. is very accepted and we don't usually censure ourselves in that aspect, we see shyness as a lack of respect for our traditions"
            show plano_mujer_cartoon:
                xsize 1600
                ysize 900
            Leyna "I… I see..."
            Leyna "(Alcohol is affecting my head quite a bit ... I'm not thinking straight, I'd better go to the inn to take a nap)"
            Villager "Well, since you want to know about the traditions from this town, we can show you a game that we usually play here"
            show plano_mujer_sonrisa:
                xsize 1600
                ysize 900
            hide plano_mujer_cartoon
            Leyna "A game? Cool! It's a difficult one?"
            Villager "Oh no relax, take it easy, It is quite simple. We can play one round so you can learn and then we play seriously."
            Leyna "Nice, thank you!"
            Villager "It works with small bets, the usual is to go betting clothes until the loser is naked"
            show plano_mujer_sorpresa_lado:
                xsize 1600
                ysize 900
            hide plano_mujer_sonrisa
            Leyna "Betting clothes? hmmm ... That's a bit ..."
            Villager "Hey come on don't worry, let's play one round to see if you like it"
            scene black with dissolve
            hide plano_mujer_sorpresa_lado
            # fade in
            "(ONE ROUND AND A COUPLE OF BEERS LATER.. )"
            Villager "Well wow... You're quite good at this"
            show expresion_yuyu_mujer:
                xsize 1600
                ysize 900
            Leyna "Yeeeah... It's very fun guys!"
            Villager "(She is quite drunk, how little endurance this woman has)"
            Leyna "Well ... it's time for me to go, I think I'm going to get some sleep"
            Leyna "alcohol doesn't suit me, I would'nt like to do something that I regret later"
            Villager "Wait! Don't you want to play a real round?"
            Villager "After we have taught you this game it would be rude to leave so soon, plus we are having a good time!"
            Leyna "Oh! seen that way, I don't want to disrespect you or anything like that... Yeah, why not?"
            scene black with dissolve
            hide expresion_yuyu_mujer
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
                    $ player_location = "Town"
                    $ set_switch("gave_bj", True)
                    $ corruption = corruption + 3
                    # fade in
                    pause 0.24
                    show plano_mujer_timida:
                        xsize 1600
                        ysize 900
                    Leyna "..."
                    "What the hell have I done?... I can't let Johan find out about this ..."
                    "+ 3 CORRUPTION"
                    hide plano_mujer_timida
                "No, this is to much":
                    Leyna "Sorry guys, but I'm a married woman and I can't do this kind of thing..."
                    Villager "I see, don't worry, have a good time at the festival."
                    Villager "(I have time to seduce this girl little by little.. there's no reason to rush)"
                    scene black with dissolve
                    $ player_location = "Town"
                    # fade in
                    $ set_switch("no_bj", True)
                    pause 0.24
                    Leyna "Where do I go now?"
        "No":
            Leyna "Sorry guys maybe another time"
            Villager "Okay, if you change your mind you already know where to find us"
            pause 0.26
    return

