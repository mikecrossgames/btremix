label Festivalworkerdentrofestival_0:
    Worker "Hey guys!"
    Johan "Hi! We already have the festival clothes"
    Worker "The opening will be tomorrow, at the moment there's nothing interesting here,but you can take a look"
    Leyna "Thank you! We won't bother you for long"
    Worker "Let me know when you're done, I have to close the access"
    $ elder_festival = 7
    return

label Festivalworkerdentrofestival_1:
    Worker "It's getting late, we must go now"
    Worker "Go to rest, see you tomorrow at the inauguration"
    Leyna "Thanks for everything"
    pause 0.26
    scene black with dissolve
    call SetPlayerLocation("Path") from _call_Festivalworkerdentrofestival_1_SetPlayerLocation
    # fade in
    $ elder_festival = 8
    return

label Festivalintrofestival_0:
    Leyna "Is he the worker we helped yesterday?"
    Johan "Yes! Let's talk with him and see if he can guide us a bit"
    pause 0.28
    Johan "Good morning!"
    Worker "Oh! Good morning couple, how can I help you?"
    Johan "We just arrived and it seems to be so many things to do that we don't know where to start"
    Worker "It's normal the first time, don't worry"
    Worker "Within an hour the inauguration rite will begin, where the \"lucky person\" will be chosen"
    Leyna "Lucky person?"
    Worker "Yes! It's said that everyone who touches it will have good luck for a whole year!"
    Johan "..."
    Worker "Anyway, there's still a while for that... I've to go for a fruit that grows in these mountains we usually eat it before the festival starts"
    Worker "Puts everyone ... let's say.. in a good mood Do you want to come with me?"
    Johan "Sure!"
    Worker "Perfect! Follow me then"
    pause 0.26
    scene black with dissolve
    call SetPlayerLocation("Mountains") from _call_Festivalintrofestival_0_SetPlayerLocation
    # fade in
    $ elder_festival = 10
    return

label Festivalintrosorteo_0:
    scene black with dissolve
    # fade in
    if switch("ate_the_fruit"):
        Leyna "(I feel... weird...are these the effects of the strange fruit?)"
    pause 0.24
    Worker "Okay guys, follow me. We're late for the opening"
    Leyna "Y..Yeah"
    pause 0.52
    pause 0.50
    scene black with dissolve
    call SetPlayerLocation("Casino") from _call_Festivalintrosorteo_0_SetPlayerLocation
    # fade in
    return

label FestivalFoodStand_0:
    Johan "Are you hungry? I'm starving.. Let's eat something here, it smells delicious"
    Leyna "Please!"
    pause 0.26
    scene puesto1
    Johan "This food is so good!"
    Leyna "I need the recipe to make it at home"
    scene black with dissolve
    hide puesto1
    # fade in
    WorkersSon "Hey dude, this is the woman I talked to you about"
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
        call ShowAnimation(1, "FestivalEV020", "FestivalEV020_0") from _call_FestivalEV020_0_ShowAnimation
        pause 0.6
        scene puesto10
        Johan "Well guys, see you over there then.."
        scene puesto19
        WorkersSon "Yeah! See you..."
        Leyna "Yeah, bye guys (that was close..)"
        hide puesto19
    scene black with dissolve
    # fade in
    pause 0.22
    Johan "Well, what can we do now?"
    Leyna "There is a massage stand near the casino, we should go there"
    $ food_stand = 1
    if switch("ate_the_fruit"):
        $ corruption = corruption + 5
    return

label FestivalPhotoSession_0:
    Johan "Hey.. Leyna, you were very sexy yesterday at the photoshoot.."
    Leyna "Oh... thanks (Why does he say that so suddenly?)"
    Johan "And I had thought ..."
    Leyna "Yes?"
    Johan "...why don't we do our own photo session? I would like to have pictures of you ... sexy pictures"
    Leyna "Oh! hahaha... Okay, why not? but.. not here,right? I-in front of everyone..."
    Johan "Oh! no! Not here... let's go to a secluded place"
    scene black with dissolve
    show festivalfotos1 with dissolve
    Leyna "Here, what do you think?.. I don't see anyone around"
    Johan "Yeah... I think it's perfect"
    scene festivalfotos2
    Leyna "Okay.. let's start then!"
    Johan "Okay, stay like that for a second, I want a cute photo"
    Leyna "Hahaha"
    $ flash_screen(wait=True)
    play sound "audio/Key.ogg" volume 0.9 noloop
    pause
    scene festivalfotos3
    Leyna "Like this?"
    Johan "Great... you're so beautiful"
    $ flash_screen(wait=True)
    play sound "audio/Key.ogg" volume 0.9 noloop
    pause
    scene festivalfotos4
    Johan "Nice..."
    $ flash_screen(wait=True)
    play sound "audio/Key.ogg" volume 0.9 noloop
    pause
    scene festivalfotos5
    Leyna "Look... take a photo now"
    Johan "Wow... so sexy..."
    $ flash_screen(wait=True)
    play sound "audio/Key.ogg" volume 0.9 noloop
    pause
    scene festivalfotos6
    Leyna "Do you like it?"
    Johan "I love it..."
    Johan "I'm getting hard"
    $ flash_screen(wait=True)
    play sound "audio/Key.ogg" volume 0.9 noloop
    pause
    scene festivalfotos7
    Leyna "Now is when the good part begins"
    Johan "I'm looking forward to it"
    scene festivalfotos8
    DrunkVillager "YyeaaH Me toO!"
    Johan "Hey! What are you doing? This is not a good time pal!"
    DrunkVillager "hEy! I'm Not tHe onEe dOinG tHis In puBlIc"
    Johan "No, but you are naked in public!"
    scene festivalfotos9
    DrunkVillager "HaVe yoOu ForGoTtenn WhEre You arRre?? ThiSs Is tHe FESTIVal PAL! anD I Ccan Do wHat I WanT"
    DrunkVillager "You, bEauTifUl, Are tHe LuCky pErSonN, rRiGht?"
    if switch("ate_the_fruit"):
        scene festivalfotos10
        Leyna "(His huge cock is so close to me... Why is it so hard for me to control myself?)"
        Leyna "Yes..."
        DrunkVillager "lEt Me ToUcH YOU tHEn, I waAnt GoOd LuCk LIke EveRyoNe eLsE"
        Leyna "Oke.."
        Johan "Hey! Stop this!"
        Johan "I told you it isn't a good time friend, you are very drunk, leave us alone!"
        Johan "Leyna, get up we're leaving"
        scene festivalfotos11
        Leyna "Ye-yeah"
        DrunkVillager "Oook sTaY WitH All ThE lUcK, GrEeDy BoY"
        Johan "Yeah yeah..."
        scene black with dissolve
        hide festivalfotos11
        call SetPlayerLocation("Festival") from _call_FestivalPhotoSession_0_SetPlayerLocation
        # fade in
        pause 0.28
        Johan "Moron!"
        Leyna "Don't worry, we'll have more chances to do it"
        Johan "... Yeah... you're right"
        Leyna "(Why I'm so horny?, at another time this situation would have scared me, but now ...)"
        Leyna "Let's eat something? I've seen a very delicious food stand"
        Johan "Yeah! I'm starving"
        $ set_switch("festival_photos", True)
    if not switch("ate_the_fruit"):
        Leyna "What?"
        DrunkVillager "lEt Me ToUcH YOU tHEn, I waAnt GoOd LuCk LIke EveRyoNe eLsE"
        Johan "Hey! Stop this!"
        Johan "I told you it isn't a good time friend, you are very drunk, leave us alone!"
        Johan "Leyna, get up we're leaving"
        scene festivalfotos11
        Leyna "Ye-yeah"
        DrunkVillager "Oook sTaY WitH All ThE lUcK, GrEeDy BoY"
        Johan "Yeah yeah..."
        scene black with dissolve
        hide festivalfotos11
        call SetPlayerLocation("Festival") from _call_FestivalPhotoSession_0_SetPlayerLocation_1
        # fade in
        pause 0.28
        Johan "Moron!"
        Leyna "Don't worry, we'll have more chances to do it"
        Johan "... Yeah... you're right"
        Leyna "Let's eat something? I've seen a very delicious food stand"
        Johan "Yeah! I'm starving"
        $ set_switch("festival_photos", True)
    if switch("ate_the_fruit"):
        $ corruption = corruption + 2
    return

label Festivaliniciacionadolescencia_0:
    pause 0.26
    pause 0.2
    Worker "Great to see you guys, you're just in time!"
    Johan "Just in time? for what?"
    Worker "Today a couple of the town's kids are coming of age and will be going through the rite of adulthood"
    Johan "Rite of adulthood? Sounds interesting, are we allowed to see it?"
    Worker "Of course! you are more than welcome! although you will probably have to participate in one way or another"
    Leyna "Participate?"
    Worker "Yes, relax! it will be any silly game, don't worry!"
    Johan "Exactly Leyna, don't worry, it's also a golden opportunity to see another tradition of the town"
    Leyna "Yeah..."
    scene black with dissolve
    show ritual1 with dissolve
    OldMan "Good morning townspeople and guests!"
    OldMan "Today we are gathered here to welcome these three young men into adulthood!"
    scene ritual2
    if bottle_event == 3:
        Leyna "Oh! ( those are the guys we drank with the other day!)"
    OldMan "As tradition dictates, the ritual will be divided into two parts, you know how it goes!"
    OldMan "We need three women to step forward!"
    scene ritual3
    "Woman: Well, I guess it's our turn this year...."
    OldMan "Hmmmm great but we are missing one! You Miss step forward without fear"
    scene ritual4
    Leyna "M-me? But... I don't know if..."
    OldMan "Relax, We know you're just visiting, but you don't have to worry, it's a ritual... you don't want to offend our traditions, do you?"
    Leyna "NO! no of course..."
    scene ritual5
    Johan "Leyna honey don't worry I'll be here at all times"
    Leyna "Yes, of course..."
    scene ritual6
    OldMan "Well, let the women get in front of the guys!"
    OldMan "Hand out the infusions to all participants"
    Leyna "Infusions?"
    OldMan "Oh yes! infusions made with the fruit that grows in these forests"
    if switch("ate_the_fruit"):
        Leyna "(That damn fruit again... I shouldn't be drinking that I know what kind of effect it has on the body)"
        Leyna "(But I don't want to disrespect all these people either)"
    if not switch("ate_the_fruit"):
        Leyna "(That fruit they talk so much about... well, what could go wrong?)"
    scene ritual7
    menu:
        "Drink the infusion":
            $ set_switch("infusion", True)
        "Pretend to drink":
            pass
    scene ritual8
    Leyna "...."
    scene ritual9
    OldMan "Very good! now comes the first test, this one is for the boys!"
    OldMan "Every man has to prove that he can protect his beloved so lift her up in the air and show your strength to the other guys!"
    scene ritual10
    "Joven: UUoo!!"
    Leyna "Oh!"
    scene ritual14
    Villager "How lucky are this year's boys! what beautiful women"
    Villager2 "Hey watch what you say, there's my wife!"
    Villager "I'm sorry, but with the lack of women in this town..."
    Johan "(...)"
    scene ritual11
    OldMan "Hang in there guys! hang in there!"
    OldMan "All right, girls, look your young men in the face, remember them, you will need that later on!"
    scene ritual12
    OldMan "You know what's coming next! the second test! the youngsters will have to hide in the town and their respective beloved will have to find them"
    OldMan "Once they have found them, they will have to give them the test of maturity and that's..."
    scene ritual13
    Leyna "(The test of maturity? I hope he's not just saying ...)"
    OldMan "A kiss!"
    scene ritual12
    Leyna "Oh... (a kiss? well... it's no big deal, just a kiss on the cheek)"
    OldMan "Well, let the kids run and hide in the village!"
    scene black with dissolve
    hide ritual12
    show pantallanegro with dissolve:
        xsize 979
        ysize 720
    OldMan "And now girls! look for them!"
    Leyna "(well let's get this over with, I'm hungry)"
    scene black with dissolve
    hide pantallanegro
    call SetPlayerLocation("Town2") from _call_Festivaliniciacionadolescencia_0_SetPlayerLocation
    # fade in
    $ set_switch("find_youth", True)
    Leyna "Well... let's find that young man and give him the damn kiss"
    return

label Festivaliniciacionadolescencia_2:
    pause 0.2
    pause 0.22
    pause 0.22
    Johan "Leyna! How did the ritual go?"
    Leyna "....Good...."
    Johan "??? Are you ok?"
    Leyna "Yes... let's take a walk"
    scene black with dissolve
    $ ritual = 2
    # fade in
    return

label FestivalButtPlugEvent_1:
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
                $ set_switch("corruption_maximum", True)
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
                $ set_switch("corruption_maximum", True)
    scene analcomida24
    Leyna "Well guys... I see you've already finished your beers, would you like one more round?"
    Johan "Yes please! after this scary moment, I need to relax with another round"
    Leyna "Hahahahaha, coming right up"
    scene black with dissolve
    $ butt_plug = 4
    hide analcomida24
    call SetPlayerLocation("Festival") from _call_FestivalButtPlugEvent_1_SetPlayerLocation
    # fade in
    play sound "audio/Crow.ogg" volume 0.9 noloop
    Leyna "Well, it's getting late, the other stalls are opening for the party tonight, we should be closing"
    Villager "Yes... (in the end she made me work for hours ... well I'm still in time to take revenge )"
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
    Leyna "Well... I've finished what I had to do, time to look for Johan, he should be here at the festival"
    scene black with dissolve
    call SetPlayerLocation("FestivalNight") from _call_FestivalButtPlugEvent_1_SetPlayerLocation_1
    # fade in
    Leyna "It seems that many of the food stall workers have not yet arrived"
    Leyna "I'm sure Johan is having a drink with his new friends, better go find him quickly before he drinks too much"
    Leyna "Shit, I can't go dressed like this, can I? and less so with this stuff stuffed in the back"
    Leyna "I should go back and change now that I have the opportunity"
    return

