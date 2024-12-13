label Bar2barman_1:
    Barman "Hello beautiful, what brings you here? I don't know if you should come around here by yourself... you know. Because of what happened to you last time"
    $ show_transparent(1, "expresion_yuyu_mujer", width=1600, height=900)
    Leyna "What? No... I don't know what you're talking about. Look, I'm here because I need a part-time job and I was wondering if you need someone here"
    Barman "Hmmm, honestly, a woman with those tits would attract a lot of customers"
    $ erase_picture(1)
    $ show_transparent(2, "expresion_enfado")
    Leyna "What's wrong with you? (this man is so blatant)"
    Barman "Sorry, sorry... I meant it in a good way"
    $ erase_picture(2)
    Barman "I'm sorry but there's not much to do here, people comes without complain because it is the only bar in town I can't afford to pay you... For now"
    $ show_transparent(3, "plano_mujer_timida", width=1600, height=900)
    Leyna "It's okay, I understand, it's a very small town. At this rate I don't think I'm needed anywhere"
    Barman "Well, I heard that the hot springs is looking for a new receptionist for these days, since the owner is involved with the festival"
    $ erase_picture(3)
    $ show_transparent(4, "expresion_ilusion_mujer", width=1600, height=900)
    Leyna "Great! So I'm going to go now and ask"
    $ erase_picture(4)
    $ leyna_work = 3
    return

label Bar2barman_3:
    $ show_picture(1, "trabajobar1")
    Barman "Good afternoon! I've already been told that you have started working in the hotsprings, congratulations!"
    Leyna "Yeah... ahem well... the truth is that I was coming to talk to you about it... I've left the work"
    Leyna "And I was coming back to ask you to hire me as a waitress"
    Barman "... WHAT? I told you I don't need any waitresses for now"
    Leyna "Please reconsider... I'm sure I could be of some help to you, besides... in the hotsprings..."
    Leyna "Let's just say that since I arrived, more clients than usual started coming, I don't want to be arrogant but..."
    Leyna "I'm not stupid or deaf and I hear what they say about me..."
    Barman "Hmmm... You're certainly earning a reputation in town... and a couple more clients wouldn't be bad for me actually..."
    Leyna "(A reputation in town?..)"
    scene black with dissolve
    $ erase_picture(1)
    if switch("corruption_average"):
        $ flash_screen([255,255,255,170], 60, True)
        $ show_picture(1, "blackmail3")
        hide black with dissolve
        Leyna "(Those two assholes didn't show the pictures to anyone, did they?)"
    if switch("corruption_low"):
        $ show_picture(1, "onsen9")
        hide black with dissolve
        Leyna "(I guess that since I arrived in town I've drawn some unwanted attention)"
    $ show_picture(2, "trabajobar2")
    Leyna "Well... then will you give me a chance?"
    Barman "Hmmm... what the hell could go wrong? ok let's give it a try"
    Leyna "Right now? ... ok sure, do you have a uniform?"
    Barman "Uniform? hahahahaha oh.... (Wait wait wait... A Sexy uniform is an excellent idea)"
    Barman "(The truth is that I just received those sexy clothes that I bought for my wife on Amazonian... maybe it will be suitable)"
    Leyna "???"
    Barman "Ahem yes of course... I'll give it to you right now, I have it back there, give me a second!"
    $ show_picture(3, "pantallanegro", scale=(120, 120), width=816, height=600)
    Barman "Here you go! There is a warehouse back here where you can try it on!"
    Leyna "Hmmm this is a bit..."
    Barman "Is there any problem? it's the only one I have"
    Leyna "... no, no problem"
    $ show_picture(4, "trabajobar3")
    Leyna "So this is the uniform eh? (Who am I kidding... obviously it was going to be something provocative...)"
    Leyna "Damn it... my tits are practically out in the open"
    $ show_picture(5, "trabajobar4")
    Leyna "And I don't even have to bend down to be seen all the way down there..."
    Leyna "(I'm starting to regret coming here and we haven't even started yet...)"
    Leyna "(But until I get the money for the photos, I don't have a penny to spend, so I'll just have to put up with it)"
    $ show_picture(6, "trabajobar5")
    Barman "Wow! it suits you perfectly!"
    Leyna "You think so?"
    Barman "Yes! you're certainly going to bring in a lot of clientele as soon as all the guys in town hear about it"
    Leyna "..."
    $ show_picture(7, "trabajobar6")
    Barman "Perfect boobs!"
    Leyna "What?"
    Barman "Oh excuse me! did I say that out loud? sorry I got carried away with my excitement"
    Leyna "I-I see"
    $ show_picture(8, "pantallanegro", scale=(120, 120), width=816, height=600)
    "A short time later"
    $ show_picture(9, "trabajobar8")
    Johan "It's been a... complicated day, I needed to come to the bar to clear my head for a while"
    Johan "Nothing like a beer to take your mind off your troubles"
    $ show_picture(10, "trabajobar9")
    Johan "It seems to be the same people as always"
    Johan "Although we've only been here a few days, I've started to get fond of this site"
    Johan "It has the charm of an old-fashioned village bar. there are no places like this in the city"
    Johan "There's an empty table over there, I'd better hurry up before someone takes it from me"
    $ show_picture(11, "trabajobar10")
    Johan "!!!! (What the fuck?)"
    Johan "(That's Leyna? what's she doing here? I thought she had to go to the hotsprings to work)"
    Johan "(And what the hell is she doing dressed like that?)"
    $ show_picture(12, "trabajobar11")
    Johan "(I can see everything! How can she be dressed like that, surrounded by drunks?)"
    Johan "(One thing is the festival and all the traditions of the of this place, especially if we go together... but alone?... I don't understand anything)"
    $ show_picture(13, "trabajobar12")
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
    $ show_picture(14, "trabajobar13")
    "Minutes later"
    Johan "(Fuck now I feel guilty about this whole situation)"
    Johan "(But seriously... I think it's good that he wants to help with the situation...)"
    $ show_picture(15, "trabajobar14")
    Johan "(But does she really have to dress like that to work as a waitress?)"
    Johan "(Fuck, you can see everything, seeing my wife dressed like this, surrounded by drunks..)"
    $ show_picture(16, "trabajobar15")
    Johan "(Hey! what the hell is that guy doing? that's my wife!)"
    Johan "What kind of confidence is that? he's touching her hips! his hand... are very close to her ass!)"
    $ show_picture(17, "trabajobar16")
    Johan "(and Leyna... she doesn't seem to care)"
    Johan "(she's smiling, as if nothing happened.... maybe I'm being too jealous?)"
    Johan "(Even so, I can't help but get upset... they are taking such confidences with my wife, who is practically naked)"
    Johan "(And he's touching her... after the photo shoot I should care less about something so mundane, but I'm still getting sick watching this)"
    scene black with dissolve
    hide black with dissolve
    $ show_picture(18, "trabajobar17")
    Leyna "Good evening, sir! Would you like something to drink?"
    OldVillager "Oh! hello beautiful, you're new, aren't you? it was missing a beauty like you in this place!"
    Barman "Hey old man! don't overdo it, to complain so much I see you here every day!"
    OldVillager "Hey don't make a fool of me in front of the lady! honey give me a beer"
    $ show_picture(19, "trabajobar18")
    YoungVillager "(This woman is always provoking the men of the village ... she does it on purpose,I'm sure she thinks we are all apes here)"
    YoungVillager "(Well, now you're going to find out!)"
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    $ show_picture(20, "trabajobar19")
    Leyna "Ah?!"
    OldVillager "Ohh!! damn!"
    Johan "!!!!"
    $ show_picture(21, "trabajobar20")
    Leyna "Oh s-sorry! I don't know what could have happened."
    OldVillager "Don't worry! if it's for me you can stay like this for as long as you like  hahahaha"
    Barman "Of course, I would like nothing more than for you to work like this. I'm sure you will attract many clients!"
    "johan: (Is that asshole serious? What kind of a job is this?)"
    $ show_picture(22, "trabajobar21")
    Villager "Wow! I see the party is getting exciting!"
    "villager 2: Yes! the owner of the bar is absolutely right! you should be working like this!y ou've seen that nudity doesn't matter so much to us"
    Villager2 "But of course if a woman as sexy as you decided to work like this, we would come every day without fail!"
    Villager "Yes! please, stay like this all the time and I'll order you all the beers you want! I'll leave you a big tip too! I promise"
    Johan "(Why is Leyna so quiet?)"
    Johan "(is she thinking about it?)"
    if bet_together == 2:
        $ show_picture(23, "trabajobar22")
        Leyna "Maybe I'll think about it but not now guys...."
        Johan "(WHAT?!..)"
        Villager "OOOh so you'll think about it? well that's almost a yes"
        Leyna "I make no promises..."
        Villager2 "Okay okay, let's hope you decide, you will have us as your number one fans"
        $ erase_picture(23)
    Leyna "Well... not right now guys... I'm going to get dressed"
    Barman "Too bad..."
    scene black with dissolve
    hide black with dissolve
    $ show_picture(23, "trabajobar23")
    Leyna "(What a shame... And I'm sure Johan has seen it all)"
    Leyna "(I should be used to being seen semi-naked by now... but still...)"
    $ show_picture(24, "trabajobar24")
    Leyna "(I can't help getting wet down there, I'm as red as a tomato.... I hope the customers haven't noticed)"
    Leyna "(Well let's finish with today's shift and let's see what the bartender says)"
    scene black with dissolve
    $ erase_picture(1)
    $ erase_picture(2)
    $ erase_picture(3)
    $ erase_picture(4)
    $ erase_picture(5)
    $ erase_picture(6)
    $ erase_picture(7)
    $ erase_picture(8)
    $ erase_picture(9)
    $ erase_picture(10)
    $ erase_picture(11)
    $ erase_picture(12)
    $ erase_picture(13)
    $ erase_picture(14)
    $ erase_picture(15)
    $ erase_picture(16)
    $ erase_picture(17)
    $ erase_picture(18)
    $ erase_picture(19)
    $ erase_picture(20)
    $ erase_picture(21)
    $ erase_picture(22)
    $ erase_picture(23)
    $ erase_picture(24)
    hide black with dissolve
    Leyna "Well... we have already finished the shift..."
    Barman "Yes... congratulations, you haven't done badly, the only thing that you are very nervous, try to relax a little bit and..."
    Leyna "Don't take what they tell you seriously"
    Leyna "Right..."
    Barman "See you tomorrow and... think about working topless it would be a spectacular idea for the business"
    Leyna "!!!... sure... I will think about it"
    $ bar_work = 1
    # TransferPlayer: "Town2"
    Leyna "Where has Johan gone?... anyway, I should go to the inn to rest, tomorrow I have another day of work"
    return

label Bar2barman_5(menu_choice = None):
    $ show_picture(1, "trabajobar25")
    Barman "Good morning Leyna, ready for another day of work?"
    Leyna "Yes... I'm going to change"
    Barman "have you thought about what we talked yesterday... about the uniform?"
    Leyna "(Wait was that serious?) I-I have to think about it a bit more"
    Barman "... Sure, think about it as much as you need to"
    $ show_picture(2, "trabajobar26")
    Barman "Perfect! as beautiful as ever Leyna... but you seem a little tense, is something wrong?"
    Leyna "Oh n-no, I'm just a little nervous...."
    Barman "that's not good for business, I need you relaxed"
    Barman "Hmmm....I know! have a shot with me, a little rum will relax your your nerves"
    Leyna "Alcohol? I shouldn't..."
    Barman "Come on, listen to me Leyna, I have been working all my life in this business"
    $ show_picture(4, "trabajobar27")
    Leyna "W-well, if you insist... there should be no problem"
    Barman "Perfect, one for you and one for me hahahaaha Cheers!"
    $ show_picture(5, "pantallanegro", scale=(120, 120), width=816, height=600)
    "After a while and a few more shots..."
    $ show_picture(6, "trabajobar28")
    Leyna "Oh! Shit!"
    Villager "HEY! FUCK"
    $ show_picture(7, "trabajobar29")
    Leyna "I'm so sorry, are you all right?...ahh I left your pants all messed up"
    Villager "What the fuck are you doing! you should be more careful, look how you left m...!!!"
    $ show_picture(8, "trabajobar30")
    Villager "(What a pair of tits!!!!!)"
    Leyna "I'm really sorry, I apologize from the bottom of my heart. I'll pick it all up right away"
    Villager "(She's drunk?... her breath smells of alcohol... but she's a real beauty...) N-nothing's wrong, honey, don't worry so much"
    Leyna "Sorry, I wish I could do something to make it up to you...."
    $ show_picture(9, "trabajobar31")
    Barman "Well, why don't you do what we talked about yesterday? after this screw up you should make the customer's day and even more so after ruining his pants"
    Leyna "W-what we talked about yesterday? I..."
    Villager "What did you talk about yesterday?"
    Barman "Oh I don't know, Leyna, what do you think? we could lose a valued client..."
    $ show_picture(10, "trabajobar32")
    "Leynha: W-well, I'll do it, but just for a moment..."
    Villager "Wh-what are you going to do?"
    Barman "Don't worry, you'll love it, you'll want to come every day"
    $ show_picture(11, "trabajobar33")
    Leyna "Here you go... feel better now?"
    Villager "Holy shit!"
    Barman "Yes, they take your breath away huh? hahahaha"
    YoungVillager "WOW!"
    Leyna "hm?"
    $ show_picture(12, "trabajobar34")
    Villager2 "I see you have finally listened to us and decided to work with your tits out in the open!"
    YoungVillager "With these views I'm going to stay here all afternoon hahahaha Well we have to celebrate that you have listened to us"
    Leyna "What?"
    $ show_picture(13, "trabajobar35")
    YoungVillager "Come on guys a photo for the memory! it is a unique occasion hahahahaha"
    Villager2 "Yes! it's an excellent idea, pose for the camera!"
    Leyna "But..."
    YoungVillager "Come on beautiful, smile, you are very serious, you should be enjoying the moment, like us"
    YoungVillager "(whispering) your husband isn't around after all, is he? it would be a shame for him to join the party right now, wouldn't it?"
    Leyna "!!!"
    $ show_picture(14, "trabajobar36")
    Leyna "O-okay guys, but just one photo and that's it, huh?"
    Villager3 "Yes yes, just one photo with you is enough"
    YoungVillager "Come on man take the picture, I'm going to frame it and hang it in my room so I can see this pair of tits every day when I wake up hahahahaha"
    pause
    $ show_picture(15, "trabajobar37")
    Leyna "!!! aahh..."
    Villager3 "What a cute little moan... I think I'm falling in love with you"
    Leyna "Sto-stop"
    YoungVillager "Yeah man, don't overdo it, leave a little bit for the others"
    Leyna "Let go of me"
    Villager3 "Sorry, don't get mad, honey, I just couldn't resist"
    scene black with dissolve
    $ show_picture(16, "trabajobar38")
    hide black with dissolve
    Barman "Well, what do you say? will you work like this for the rest of the shift? you've already got all the customers happy"
    Barman "No matter how much you screw up, they'll forgive you"
    call GetChoice([_("I will work like this"), _("No, I can't do it")], value=menu_choice, called_from="Bar2barman_5") from _call_Bar2barman_5_GetChoice
    $ menu_choice = _return
    if menu_choice == _("I will work like this"):
        $ menu_choice = None
        $ show_picture(17, "trabajobar39")
        Leyna "You know what? I'm going to give this a try, it feels liberating and people are leaving lots of tips"
        Barman "I'm glad to hear that! we'll get rich you and me Leyna! Hahahahaha"
        Leyna "Hahaha well that remains to be seen, give me one more shot and I'm going to attend to those perverts"
        Barman "That's how you talk!"
        scene black with dissolve
        $ show_picture(18, "trabajobar40")
        hide black with dissolve
        Leyna "Well guys, what would you like to drink?"
        YoungVillager "Three beers, beautiful"
        Leyna "On the way!"
        scene black with dissolve
        $ show_picture(19, "trabajobar42")
        hide black with dissolve
        Leyna "I leave them here guys"
        YoungVillager "Hey, why don't you sit with us for a while?"
        Leyna "Oh, I'm sorry I can't, I have to keep working"
        YoungVillager "Oh come on..."
        $ show_picture(20, "trabajobar43")
        YoungVillager "Stay a little longer, I'm sure you'll have a great time with us, we know how to treat a lady"
        Leyna "!!!"
        Leyna "Hey... you shouldn't..."
        $ show_picture(21, "trabajobar45")
        Villager2 "Yes! stay with us honey, you're looking forward to it. I can see it in your face"
        Villager3 "That's right, don't you want to have fun? you've worked so hard, everyone deserves a little break"
        $ show_picture(22, "trabajobar46")
        YoungVillager "(whisper) you certainly look like you want to stay with us for a while, you're really happy down there"
        YoungVillager "Why don't you sit down with us for a minute?"
        pause
        $ show_picture(23, "trabajobar48")
        Leyna "I-if it's just for a minute, I could stay..."
        Villager2 "Great... come over here sit on my lap"
        Leyna "On your lap?"
        YoungVillager "yeah, haven't you heard my friend? go and sit with him, I'm sure you'll have a great time together hehehehehe"
        Leyna "Yes.... yes, for sure"
        scene black with dissolve
        $ show_picture(24, "trabajobar49")
        hide black with dissolve
        Leyna "Oh..."
        Villager2 "Oh, I'm sorry, it seems to have slipped out... it's just that these pants are very tight... I'm sure you understand me, right?"
        Leyna "Ri-right... with that big thing, it's very difficult. isn't it?"
        Villager2 "Exactly..."
        pause
        $ show_picture(25, "trabajobar51")
        Leyna "He-hey stop moving around so much... you're lifting up my skirt..."
        Villager2 "Me? it looks like you're the one who's moving honey you keep rubbing against my cock..."
        Leyna "I... no"
        pause
        $ show_picture(26, "trabajobar50")
        Villager2 "What do you mean no? just look at your face, you're you've just felt my cock and you haven't been able to control yourself..."
        Villager2 "You're eating me alive with your eyes"
        pause
        $ show_picture(27, "trabajobar52")
        Villager2 "Let me help you a little bit..."
        Leyna "No...stop.."
        Villager2 "Come on now, you're craving it, at this point you don't care if I fuck you in front of the whole bar"
        Leyna "Hmmm"
        pause
        $ show_picture(28, "trabajobar54")
        Leyna "AAAhhhh..."
        Villager2 "WOW... for how wet you are, it was hard to get in"
        Villager2 "What do you think is as big as it looks?"
        Leyna "Hmmm, s-stop you're going to break me in half"
        pause
        $ show_picture(29, "trabajobar55")
        Villager2 "And what would be the problem? Isn't that exactly what you want? coming to work dressed like that?"
        Villager2 "Tell me... say it just once and I'll do it... tell me that you want me to fuck you right here in front of everybody"
        Leyna ".... hmmm ah ah ah"
        Villager2 "what are you waiting for? say it at once"
        Leyna "Ah ah ah... fuck me... fuck me in front of everybody"
        pause
        $ show_picture(30, "trabajobar56")
        Villager2 "As you wish bitch"
        Villager2 "Get ready"
        YoungVillager "You heard her, fuck her like she deserves it"
        Villager3 "hahahaha I can't believe this is happening! crazy!!!"
        $ show_picture(31, "trabajobar58")
        play bgs "audio/audio follar.ogg" loop volume 0.9
        Leyna "HMmmaaaa!!"
        Villager2 "Do you like it bitch?! !"
        "Young villager : wow hahahaahah"
        pause
        $ show_picture(32, "trabajobar57")
        play bgs "audio/audio follar.ogg" loop volume 0.9
        Villager2 "come on bitch, you do it, I'm not going to do all the work"
        Leyna "AH AH AH AH!!!!"
        Villager2 "Watch her shake her ass! She's an expert!"
        Villager3 "She's super horny, look at her! she's not even aware that the whole bar is watching!"
        "BArman: Hey you fucking savages, what the fuck are you doing to my waitress?"
        YoungVillager "Now it's a little late to talk old man! enjoy the view like everyone else!"
        Barman "Fucking kids"
        pause
        $ show_picture(33, "trabajobar59")
        play bgs "audio/audio follar.ogg" loop volume 0.9
        Villager2 "Fuck, I can't hold on any longer, I'm going to cum inside this slut!"
        YoungVillager "Hahahahaha yes, do it!"
        Leyna "AH ah.. wait... wait don't come yet!"
        Villager2 "AAAH here it goes!!"
        $ flash_screen([255,255,255,170], 60, True)
        $ show_picture(34, "trabajobar61")
        stop bgs fadeout 1
        $ flash_screen([255,255,255,170], 60, True)
        Villager2 "I couldn't take it anymore... I hadn't fucked for years!"
        Villager2 "I've stuffed you like a turkey! you should thank me! hahahaha"
        pause
        $ show_picture(35, "trabajobar62")
        Leyna "AH ah ah... I can hardly move... y-you've cum inside me... ah ah ah..."
        Villager2 "And if you don't get up soon, I'll do it again, beautiful"
        Leyna "AH ah I'm going... I'm going..."
        scene black with dissolve
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(4)
        $ erase_picture(5)
        $ erase_picture(6)
        $ erase_picture(7)
        $ erase_picture(8)
        $ erase_picture(9)
        $ erase_picture(10)
        $ erase_picture(11)
        $ erase_picture(12)
        $ erase_picture(13)
        $ erase_picture(14)
        $ erase_picture(15)
        $ erase_picture(16)
        $ erase_picture(17)
        $ erase_picture(18)
        $ erase_picture(19)
        $ erase_picture(20)
        $ erase_picture(21)
        $ erase_picture(22)
        $ erase_picture(23)
        $ erase_picture(24)
        $ erase_picture(25)
        $ erase_picture(26)
        $ erase_picture(27)
        $ erase_picture(28)
        $ erase_picture(29)
        $ erase_picture(30)
        $ erase_picture(31)
        $ erase_picture(32)
        $ erase_picture(33)
        $ erase_picture(34)
        $ erase_picture(35)
        hide black with dissolve
        "A while later"
        Barman "Ehmmm Leyna... Go-good job... see you tomorrow."
        Leyna "Yes... see you tomorrow"
        Barman "... Sure"
        # TransferPlayer: "Town2"
        pause 0.2
        Leyna "Now you've made it good Leyna... Half the town has seen you fucking with another man... If Johan doesn't find out, it will be a miracle"
        Leyna "What am I going to do?"
        scene black with dissolve
        # TransferPlayer: "Town2"
        hide black with dissolve
        "Some time later"
        Johan "Where is Leyna? Maybe she is still working I'll go to the bar to see what's going on"
        $ bar_work = 3
    elif menu_choice == _("No, I can't do it"):
        $ menu_choice = None
        Leyna "I-I'm sorry but I can't do it at the moment, I don't feel comfortable"
        Barman "Sure, don't worry, put your uniform back on and continue serving customers as before"
        Leyna "Yes... thank you"
        scene black with dissolve
        $ show_picture(18, "trabajobar41")
        hide black with dissolve
        Leyna "Well guys, what would you like to drink?"
        YoungVillager "Three beers, beautiful"
        Leyna "On the way!"
        scene black with dissolve
        $ show_picture(19, "trabajobar42")
        hide black with dissolve
        Leyna "I leave them here guys"
        YoungVillager "Hey, why don't you sit with us for a while?"
        Leyna "Oh, I'm sorry I can't, I have to keep working"
        YoungVillager "Oh come on..."
        $ show_picture(20, "trabajobar43")
        YoungVillager "Stay a little longer, I'm sure you'll have a great time with us, we know how to treat a lady"
        Leyna "!!!"
        Leyna "Hey... you shouldn't..."
        $ show_picture(21, "trabajobar47")
        Villager2 "Yes! stay with us honey, you're looking forward to it. I can see it in your face"
        Villager3 "That's right, don't you want to have fun? you've worked so hard, everyone deserves a little break"
        Leyna "I'm sorry guys, but I really can't, I have to keep working"
        YoungVillager "Oh what a shame"
        scene black with dissolve
        $ show_picture(22, "trabajobar63")
        hide black with dissolve
        YoungVillager "(whispering) I've got an idea, man... listen carefully"
        Villager2 "!!! sure, tell me man"
        $ show_picture(23, "trabajobar64")
        "A few minutes later"
        Villager2 "Hey waitress, you brought me a broken jar!"
        Leyna "Wh-what?"
        Villager2 "You brought me a broken jar! look how you've left me! It's a mess! it's all messed up"
        Leyna "Oh! Sorry! I'll pick it up right away"
        $ show_picture(24, "trabajobar65")
        Leyna "I'll clean it right away"
        Villager2 "Oh take your time hehehe in that position you are perfect"
        Leyna "???"
        $ show_picture(25, "trabajobar66")
        Villager2 "that's perfect! Stay close, honey, I'll be done in a second"
        YoungVillager "Hahahaah You're crazy, man"
        Leyna "What the hell?"
        $ show_picture(26, "trabajobar67")
        play bgs "audio/audio follar.ogg" loop volume 0.9
        Leyna "How can you have it so big? (but what am I saying, this stranger's dick is so close to my face and I...)"
        Villager2 "Ufff I love it when you say that...I can feel your breath on my dick... stay very still..."
        call GetChoice([_("Keep still"), _("nope")], value=menu_choice, called_from="Bar2barman_5") from _call_Bar2barman_5_GetChoice_1
        $ menu_choice = _return
        if menu_choice == _("Keep still"):
            $ menu_choice = None
            Leyna "Ahh..."
            Villager2 "That's it... I'm almost... I'm almost there"
            $ flash_screen([255,255,255,170], 60, True)
            stop bgs fadeout 1
            $ show_picture(27, "trabajobar68")
            Villager2 "AAAAHhhh!"
            Villager3 "The crazy fucker has done it, he has done it!"
            Barman "Hey! what the hell are you doing to my waitress? Bunch of animals!"
            Villager2 "AAAHh! sorry old man... I couldn't help it...."
            "BArman: Leyna, Come here! and clean yourself up"
            Leyna "Ye-yeah"
            $ show_picture(28, "pantallanegro", scale=(120, 120), width=816, height=600)
            "After that the shift went on in a relatively normal way"
            scene black with dissolve
            $ erase_picture(1)
            $ erase_picture(2)
            $ erase_picture(3)
            $ erase_picture(4)
            $ erase_picture(5)
            $ erase_picture(6)
            $ erase_picture(7)
            $ erase_picture(8)
            $ erase_picture(9)
            $ erase_picture(10)
            $ erase_picture(11)
            $ erase_picture(12)
            $ erase_picture(13)
            $ erase_picture(14)
            $ erase_picture(15)
            $ erase_picture(16)
            $ erase_picture(17)
            $ erase_picture(18)
            $ erase_picture(19)
            $ erase_picture(20)
            $ erase_picture(21)
            $ erase_picture(22)
            $ erase_picture(23)
            $ erase_picture(24)
            $ erase_picture(25)
            $ erase_picture(26)
            $ erase_picture(27)
            $ erase_picture(28)
            hide black with dissolve
            Barman "Ehmmm Leyna... Go-good job... see you tomorrow."
            Leyna "Yes... see you tomorrow"
            Barman "... Sure"
            # TransferPlayer: "Town2"
            pause 0.2
            Leyna "That was a bit of an experience... anyway, I'm going to rest and and tomorrow will be another day"
            scene black with dissolve
            # TransferPlayer: "Town2"
            hide black with dissolve
            "Some time later"
            Johan "Where is Leyna? Maybe she is still working I'll go to the bar to see what's going on"
            $ bar_work = 3
        elif menu_choice == _("nope"):
            $ menu_choice = None
            Leyna "What the fuck are you talking about? Jerk off at home"
            Leyna "(I'd better get up quickly before I get a cumshot on my face)"
            $ show_picture(27, "pantallanegro", scale=(120, 120), width=816, height=600)
            "After that the shift went on in a relatively normal way"
            scene black with dissolve
            $ erase_picture(1)
            $ erase_picture(2)
            $ erase_picture(3)
            $ erase_picture(4)
            $ erase_picture(5)
            $ erase_picture(6)
            $ erase_picture(7)
            $ erase_picture(8)
            $ erase_picture(9)
            $ erase_picture(10)
            $ erase_picture(11)
            $ erase_picture(12)
            $ erase_picture(13)
            $ erase_picture(14)
            $ erase_picture(15)
            $ erase_picture(16)
            $ erase_picture(17)
            $ erase_picture(18)
            $ erase_picture(19)
            $ erase_picture(20)
            $ erase_picture(21)
            $ erase_picture(22)
            $ erase_picture(23)
            $ erase_picture(24)
            $ erase_picture(25)
            $ erase_picture(26)
            $ erase_picture(27)
            hide black with dissolve
            Barman "Ehmmm Leyna... Go-good job... see you tomorrow."
            Leyna "Yes... see you tomorrow"
            Barman "... Sure"
            # TransferPlayer: "Town2"
            pause 0.2
            Leyna "That was a bit of an experience... anyway, I'm going to rest and and tomorrow will be another day"
            scene black with dissolve
            # TransferPlayer: "Town2"
            hide black with dissolve
            "Some time later"
            Johan "Where is Leyna? Maybe she is still working I'll go to the bar to see what's going on"
            $ bar_work = 3
    return

label Bar2WowGuysWhatACoincidence_0(menu_choice = None):
    pause 0.24
    pause 0.2
    Alexa "Wow guys! what a coincidence!"
    Leyna "!!!"
    Johan "(It's the girl from the other night right?...shit I don't remember her name)"
    Johan "Hey... hmmm what's up?"
    Alexa "Great! my husband is with his friends on an excursion but I just felt like... having a drink and a good time with the guys in town hahaha"
    Johan "Hahaha... I see... well, we are going to have a beer here too... so we'll see you around"
    Alexa "Here? all by yourselves? how boring! why don't you guys come with us?  We thought we'd go to the inn and have a some beers! they were going to show me a game!"
    Johan "Oh! n-no need, we don't want to bother you"
    Villager "Right... I guess the owner of the inn might be annoyed if we bring a lot of people to the room"
    Alexa "Nonsense! Johan you never bother! and besides, I've made friends with the owner of the inn, I don't think he'll mind!"
    Leyna "(How many \"friends\" is Alexa making?)"
    Alexa "Come on, that's all, come with us! We will have a great time!"
    Johan "... Sure, why not? (Can Leyna and I have a quiet afternoon?)"
    Leyna "... Okay, let's have a drink..."
    Villager "(Damn, what a bummer... I thought we were going to... well whatever, another time, anyway this girl is also beautiful ... but she comes with her husband)"
    scene black with dissolve
    $ show_picture(1, "apuesta1")
    hide black with dissolve
    "A FEW BEERS LATER"
    Alexa "...And I told him \"Not even in your dreams\""
    Leyna "Hahahaha... By the way, didn't you guys have a meeting to teach Alexa a traditional game?"
    Villager "Oh... (Shit...) Ahem yes... well it's just that that game can only be played by three people"
    Alexa "AAah yeah? wow... Well no problem! I can show you a game I used to play in college!"
    $ show_picture(2, "apuesta2")
    Villager "(Fuck this girl is hot...) Yeah yeah... we can play whatever you want..."
    Johan "(This guy could stop it, he's staring at my wife's tits with me in front of him...) And what does this game consist of?"
    $ show_picture(3, "apuesta3")
    Alexa "It is quite simple, similar to truth or dare, but a little different"
    Alexa "It is not the one who is asked who decides whether he prefers to make truth or daring but the one who asks, for example..."
    Alexa "Let's say it's my turn and I tell you \"Johan... take off your pants\" then you should do it"
    Alexa "Or I could ask you... an awkward question and if you don't want to answer it you would have to do what I said"
    Johan "(That seems a bit...) What if I don't want to?"
    Alexa "Well, you lose the game hahahaha, come on let's go drink a few more beers and play"
    Leyna "Yes, it will be fun!"
    $ show_picture(4, "apuesta4")
    "SEVERAL BEERS LATER"
    Alexa "Well let's get started!"
    Leyna "Hehehe I'm a little nervous"
    Johan "(And a little drunk too hahahaha)"
    Alexa "Well I'll start... let's see... let's start with something light hahaha"
    Alexa "Johan who do you think is in better shape me or Leyna?"
    call GetChoice([_("Alexa"), _("Leyna")], value=menu_choice, called_from="Bar2EV012_0") from _call_Bar2EV012_0_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Alexa"):
        $ menu_choice = None
        Alexa "Wow I didn't expect that hahaha"
        Leyna "Hey, I'm your wife!"
        Johan "Hahahahaha sorry I have to be impartial and it looks like Alexa does a lot of sports"
    elif menu_choice == _("Leyna"):
        $ menu_choice = None
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
    $ show_picture(5, "apuesta5")
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    Alexa "No problem, Trying to test me? hahahaha"
    Villager "Wow, I thought you wouldn't dare! People from out of town tend to be a little self-conscious about nudity...."
    Alexa "Well, I don't..."
    Johan "(You can say that...)"
    Leyna "Johan don't look so much hahahaha"
    Johan "Y-yeah sorry"
    $ show_picture(6, "apuesta6")
    Villager "Well, man, now it's your turn"
    Villager2 "Yes! I've already thought about what I'm going to do"
    Villager2 "You've been a little hard on Alexa so I'm going to have to teach you a little lesson, get naked!"
    Villager "What? Come on, man, don't be an asshole!"
    Villager2 "Hey, the rules are the rules, Alexa hasn't had any problem, you're not going to chicken out, are you?"
    Villager "...Dickhead, very well as you wish"
    $ show_picture(7, "apuesta7")
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    Leyna "WOW (Shit did I say that out loud?)"
    Alexa "Careful Leyna, don't stare so much hahaha"
    Leyna "I-I don't! ..."
    Johan "..."
    $ show_picture(9, "apuesta8")
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
    $ show_picture(9, "apuesta9")
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
    $ show_picture(10, "apuesta10")
    play sound "audio/Jump1.ogg" volume 0.9 noloop
    Villager "Yes, it will be a great pleasure!"
    Leyna "Ah?!!"
    Alexa "Oh Wow! hahahaha"
    pause
    $ show_picture(11, "apuesta11")
    Leyna "Ugh!"
    Johan "!!!Shit, before I could say anything, he's put his dick in her mouth!.... why am I not saying anything right now?)"
    Johan "(I've been entranced again by seeing this kind of thing...)"
    call GetChoice([_("STOP!"), _("....")], value=menu_choice, called_from="Bar2EV012_0") from _call_Bar2EV012_0_GetChoice_1
    $ menu_choice = _return
    if menu_choice == _("STOP!"):
        $ menu_choice = None
        $ bet_together = 1
        Johan "HEY! stay away from my wife!"
        $ show_picture(12, "apuesta16")
        Leyna "!!!  (I've never seen Johan so angry before)"
        Alexa "Come on, Johan don't get so angry, it's just a silly game"
        $ show_picture(13, "apuesta15")
        Johan "I understand very well! but I can't allow something like this! I'm sorry guys, but we've had enough fun for today!"
        Johan "(I'm a bit saturated between this and the photo shoot ... I just need a quiet fucking afternoon with my wife)"
        Leyna "...Johan..."
        Johan "Let's go Leyna, we need to go for a walk to sober up and then we'll see what we're going to do"
        Leyna "Y-yes, you're right"
        $ show_picture(14, "apuesta17")
        Alexa "It's a pity guys! Please don't be angry! we had no bad intentions! see you soon in town, couple!"
        Johan "Yes, of course"
        scene black with dissolve
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(4)
        $ erase_picture(5)
        $ erase_picture(6)
        $ erase_picture(7)
        $ erase_picture(8)
        $ erase_picture(9)
        $ erase_picture(10)
        $ erase_picture(11)
        $ erase_picture(12)
        $ erase_picture(13)
        $ erase_picture(14)
        # TransferPlayer: "Town2"
        hide black with dissolve
        pause 0.24
        pause 0.2
        Leyna "... (Johan hasn't said a word since we've been gone ... I hope it hasn't affected him too much)"
    elif menu_choice == _("...."):
        $ menu_choice = None
        $ show_picture(12, "apuesta12")
        $ bet_together = 2
        Johan "(I'm just pinned to the floor, with nothing to say... while they do this to Leyna...)"
        Villager "This feels amazing, all the way in!"
        Villager2 "Enjoy it man, who knows when it might happen again!"
        Johan "(They are saying these kinds of things with me in front of them!)"
        Alexa "Hahahaha what an enthusiasm! keep up the good work kid!"
        Leyna "!!!"
        pause
        $ show_picture(13, "apuesta13")
        play bgs "audio/audio follar.ogg" loop volume 0.9
        Villager "Ah! Ah! like this! all the way down! swallow it whole!"
        Villager2 "Fuck man! you're fucking her throat what a beast!"
        Alexa "That's the way to do it!"
        Johan "(what the hell is going on? what the hell are they talking about?... this is... this...)"
        Johan "(My stomach is so upset that I feel like throwing up)"
        pause
        $ show_picture(14, "apuesta14")
        stop bgs fadeout 1
        Leyna "Ah... Ah... Ah... I need to... breathe"
        Villager "Come on, this is not over..."
        Leyna "NO!... no... stop, this is too much, enough is enough!"
        pause
        $ show_picture(15, "apuesta16")
        Alexa "Oooh... are you going to leave it like that?"
        Leyna "Y-yeah, game over... I've had enough for today"
        Villager2 "What a bummer, man... you just went a little too far"
        Villager "S-sorry"
        Alexa "Don't worry, you have made it very well"
        pause
        $ show_picture(16, "apuesta17")
        Leyna "We are leaving now"
        Johan "...Y-yes..."
        Alexa "Oh, you're leaving already? too bad, we'll see you in town, couple..."
        Leyna "... Yes, we'll see"
        scene black with dissolve
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(4)
        $ erase_picture(5)
        $ erase_picture(6)
        $ erase_picture(7)
        $ erase_picture(8)
        $ erase_picture(9)
        $ erase_picture(10)
        $ erase_picture(11)
        $ erase_picture(12)
        $ erase_picture(13)
        $ erase_picture(14)
        $ erase_picture(15)
        $ erase_picture(16)
        # TransferPlayer: "Town2"
        hide black with dissolve
        pause 0.24
        pause 0.2
        Leyna "... (Johan hasn't said a word since we've been gone ... I hope it hasn't affected him too much)"
    return

label Bar2Eventoanal1_0:
    pause 0.36
    pause 0.2
    Johan "It seems that Leyna has already finished her shift..."
    Johan "Well, since I'm here... it wouldn't hurt me to have a beer"
    pause 0.28
    scene black with dissolve
    hide black with dissolve
    Villager "Good afternoon! You are the tourist who came with his wife on vacation, right?"
    Johan "Yes, that's me, what's up?"
    Villager "Oh nothing, since your wife started working at the bar, this place is much more pleasant"
    Johan "Wow... thank you..."
    Villager "Would you mind if I have a drink with you?"
    Johan "It doesn't matter, go ahead!"
    Villager "Great, you're on me! we have a home brew that is spectacular"
    Johan "Hahahaha thank you very much"
    scene black with dissolve
    hide black with dissolve
    "Several beers later..."
    Villager "... And I told my wife, well better late than never!"
    Johan "Hahahaha Wow, and what did she tell you?"
    Villager "He said yes! and since then we haven't stopped doing it! Of course it has improved our sex life a lot!"
    Johan "Wow... So anal sex is as good as they say?"
    Villager "Of course! after a while we both get bored of doing the same thing all the time, variety is the spice of life!"
    Johan "Wow... I wish Leyna would do it... but I'm not sure she'll say yes"
    Villager "Oh, as young as you are, I thought you might be doing it, since kids nowadays are so open-minded and stuff ...."
    Johan "I always thought about it but... I guess I never had the courage to ask for it"
    Villager "Well, you should! What could go wrong? In the worst case, he'll say no, it's okay!"
    Villager "If you try it, I have an extra dildo, when I ordered it they brought me an extra one by mistake... if you want I can give it to you as a gift"
    Johan "Wow... well... yeah... what the hell? I'm sure it's because I'm drunk but I feel confident to tell her"
    Villager "Now you're talking!"
    Villager "Come home with me and I'll give you the dildo"
    Johan "Great, let's go!"
    scene black with dissolve
    # TransferPlayer: "Town2"
    hide black with dissolve
    Johan "Well I got it... I get nervous just thinking about telling Leyna.... Hahaha I look like a teenager"
    Johan "What a nice man... There are good people in this town..."
    scene black with dissolve
    # TransferPlayer: "Town2"
    pause 0.26
    hide black with dissolve
    Johan "Leyna! I've been looking all over for you, where have you been?"
    Leyna "Oh I was just walking around, I needed a walk and some fresh air...work has left me exhausted"
    Johan "I see... well, it's normal to be tired, it's been a long time since you've worked on something so physical"
    Johan "Why don't we go to the inn? there's something I want to talk to you about"
    Leyna "Sure (Someone in the village may have said something to him?, I hope not ....)"
    Johan "Great! let's go to our room"
    $ bar_work = 4
    return

label Bar2LeynaWeWereLookingForYou_0(menu_choice = None):
    pause 0.22
    pause 0.2
    Alexa "Leyna! We were looking for you!"
    Leyna "Me? well Johan and I were just doing some things"
    Alexa "Yeah... we were at the river and suddenly you disappeared... and we were having so much fun hehehehehehe"
    Leyna "Yeah... hahaha.... we are not very used to that kind of fun"
    Alexa "Well, never mind, I was here with a couple of friends and a guy invited us to his house to play a game of cards"
    Alexa "You know, have a few beers and play for a while before going to the festival in the afternoon"
    Leyna "More beers?...I don't know Alexa, I'm drinking too much lately"
    Alexa "Relax! like everyone else! the festival is coming to an end, tomorrow is the last day, we have to make the most of the last moment"
    Alexa "You and I don't know if we are going to come back to this town so we might as well enjoy the experience while it lasts, right?"
    Alexa "In our daily life, we will have time to recover and not go out partying"
    Leyna "well.... I guess you're right"
    Alexa "See? I knew you would agree with me"
    Alexa "Come with us for a few beers and let's play a card game, it will be fun!"
    Leyna "Well, I have to wait for johan, he went to talk to the mayor but he will be back soon"
    Alexa "Oh... I see, right, well we're on our way, come with us"
    Leyna "Okay"
    scene black with dissolve
    $ show_picture(1, "poker1")
    hide black with dissolve
    Leyna "Oh my! you've already finished, it was very fast"
    Johan "... Yes, there are not many activities left in the festival, tomorrow will be the last day"
    Leyna "What a pity... well soon we will be back home, I hope the magazine likes the work you have done"
    Johan "Yes... I hope so too"
    Johan "and... you're already with alexa? I guess there's not much to do in town"
    Leyna "no... I met her at the bar... she says to go with her to a friend's house for a drink and a game of cards"
    Johan "(yet another friend?) hmmm well lately we've been drinking a lot but I guess we have to enjoy the experience while it lasts"
    Johan "After all, we will soon be back in the city"
    Leyna "Yes, that's just what Alexa told me a few minutes ago"
    Alexa "Well Johan, are you joining us or are you too busy? we can always be alone with your wife hahahahahaha"
    Johan "!!!! N-no! of course I'm joining!"
    Alexa "Well, let's leave the chatter for later, our friend is waiting for us"
    Villager "Yes! beers are waiting for us"
    Leyna "Hehehehehe well come on, let's not keep them waiting"
    Johan "Hahahaha"
    $ show_picture(2, "poker2")
    "Minutes later"
    Leyna "(Shit, this guy again, if I had known it was his house I wouldn't have come)"
    YoungVillager "Well, I'm off to get the beers"
    Villager1 "Yes! I'm thirsty"
    scene black with dissolve
    hide black with dissolve
    "A time and several beers later"
    Alexa "Well, let's play cards, shall we?"
    Villager "OH! yes I forgot about it"
    $ show_picture(3, "poker3")
    Johan "Cards? is it some kind of weird game?"
    YoungVillager "Nah no way, it's a normal card game"
    Johan "Oh great, let's play"
    YoungVillager "Perfect!"
    scene black with dissolve
    $ show_picture(4, "poker4")
    hide black with dissolve
    "Minutes later"
    YoungVillager "Well, those are the rules of the game"
    "Johna: Sounds good!"
    Leyna "Yes, it sounds like fun"
    Villager "Hahahahaha nothing like a few beers and a game of cards to forget all your problems"
    Alexa "...."
    $ show_picture(5, "poker5")
    "Some time and several more beers later"
    Leyna "Hahahahahaha looks like I won!"
    Villager2 "Hey, you're pretty good at this game"
    Leyna "Thank you!"
    $ show_picture(6, "poker6")
    Alexa "..."
    YoungVillager "Everything okay alexa?"
    Alexa "meh"
    Villager "What's the matter?"
    Alexa "This game is a bit boring I'm not going to lie to you"
    Johan "Boring? it's not so bad"
    Alexa "Come on guys, we're all adults now, I think we should add some excitement"
    YoungVillager "Well if you can think of a more exciting game, we are open to play it"
    Johan "..."
    Alexa "Well, I can think of another card game that is a little more exciting"
    Alexa "I played it a lot in college"
    Alexa "A mixed strip poker"
    Leyna "Oh..."
    Johan "I don't think that ..."
    $ show_picture(7, "poker7")
    Alexa "Come on johan, don't be a killjoy"
    Alexa "It will be exciting, we must have a good time before the festival ends and we return home"
    Johan "...."
    Leyna "Don't worry Johan, I'm sure it will be fun"
    Johan "If it's okay with you, I guess it's no problem"
    Alexa "Great! let's get started then"
    $ show_picture(8, "poker8")
    "Several minutes later"
    Alexa "Wow Johan, you're pretty bad at this aren't you?"
    Johan "Yes... the truth is that I'm not good at card games, but I'm surprised to see how good Leyna is"
    Leyna "Hahahahaha I guess I am very lucky"
    $ show_picture(9, "poker9")
    Johan "luck? not just luck, I only have the underpants left hahahahahah"
    Leyna "And soon you will have nothing left"
    Villager "(It is true that she is good at playing this game, I have to concentrate and think about how to beat her, any excuse is good to see what a great body she has)"
    $ show_picture(10, "poker10")
    Alexa "You look very focused hehehehehe"
    Villager "I-I? Well, I've come to win, in a little while you'll both be naked in front of me"
    Alexa "Hahahahaha"
    Johan "...."
    $ show_picture(11, "poker11")
    "Several beers later"
    Alexa "Well there goes my t-shirt hahahaaha"
    Villager2 "finally things are getting interesting!"
    Villager "yes...(although Leyna is still winning, we still haven't managed to get her to take anything off)"
    $ show_picture(12, "poker12")
    Leyna "what did you say? that we were going to be naked in front of you? hehehehehe"
    Villager "Hey the game is not over yet, I still have all my clothes on"
    Leyna "Hehehehe that is about to change"
    Johan "(I know that giggle, Leyna is pretty drunk...)"
    Villager "We'll see about that"
    scene black with dissolve
    $ show_picture(13, "poker13")
    hide black with dissolve
    Leyna "UUUh! I win, come on t-shirt off hahahaha"
    Alexa "Hahahaa well done, teach him a lesson"
    Villager "Very well... (shit...)"
    Johan "(She's good, although she is quite drunk, she is playing very well)"
    YoungVillager "Shit, she's humiliating us..."
    scene black with dissolve
    $ show_picture(14, "poker14")
    hide black with dissolve
    Villager "Come on!! this one is mine!"
    Leyna "Ahhh Shit"
    YoungVillager "Well done!"
    Villager2 "Things get interesting"
    Villager "Come on, T-shirt off"
    Leyna "Yes... this time you have won, but this has just begun"
    $ show_picture(15, "poker15")
    Villager "Ooh! I'll never get tired of looking at that pair of tits!"
    Johan ".... (shit no need to get like that... we're all drunk and courtesy is lacking)"
    YoungVillager "Leyna, I wish you would stay and live in this town forever"
    Leyna "I'm sure you're looking forward to it perverts hehehehe"
    Villager2 "Yeah..."
    $ show_picture(16, "poker16")
    Johan "I'm going to get another beer..."
    Leyna "Oh bring me one too"
    Johan "Are you sure?"
    Leyna "Come on man don't be a party pooper hahahaha"
    Alexa "Hahaha  Well said!"
    Johan "Whatever ... (I'm already a little drunk but... fuck it, if she can have a good time I can have a good time too)"
    scene black with dissolve
    $ show_picture(17, "poker17")
    hide black with dissolve
    Villager "(I only have the underpants left...)"
    Leyna "(Only my panties are left...)"
    Villager "Well, things are getting interesting"
    Alexa "Yes, I think we all only have the underwear left"
    Johan "Yeah..."
    Leyna "Let's continue, I still have to beat you"
    Villager "We'll see who wins, I'm looking forward to seeing it all"
    Leyna "Hihihi not even in your best dreams"
    scene black with dissolve
    $ show_picture(18, "poker18")
    hide black with dissolve
    Villager "Shit"
    Leyna "See? I told you I'd beat you"
    Villager "hmmm"
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    $ show_picture(19, "poker19")
    Leyna "!!! ( So close!) Y-you sure seem to be happy to see me!"
    Johan "!!!"
    Villager "I can't accept it, let's keep playing!"
    $ show_picture(20, "poker20")
    Leyna "Hahahahaha accept defeat... you have nothing left to take away from yourself"
    Alexa "Well... we can keep playing, but we'll gamble with small acts of bravery"
    Johan "L-little acts of bravery? ( Shit I can't hardly talk because I'm so drunk?"
    Alexa "Yeah... hehehe you know... if I win you touch me \"there\" or you get \"that way\"... nothing extreme, small silly things"
    Johan "I-I don't think it's..."
    $ show_picture(21, "poker21")
    Leyna "Fine with me! If you want to keep humiliating yourself go ahead hahahaha"
    Johan "(Leyna is ignoring me completely...)"
    Villager "Perfect! let's go on then!"
    Johan "(W-what's going on?... I have a feeling that the situation is getting out of control)"
    scene black with dissolve
    $ show_picture(22, "poker22")
    hide black with dissolve
    Villager "Good! now we're even! come on, I want you to take those panties off!"
    Leyna "Shit... well that's fair enough, enjoy the show"
    Johan "!!! (\"enjoy the show?\" Leyna doesn't look like her usual self, I can hardly recognize her with that kind of behavior)"
    $ show_picture(23, "poker23")
    Villager "It is as beautiful as I imagined it would be"
    Villager "Look! you can see how happy I am to see it!"
    $ show_picture(24, "poker24")
    Villager2 "And me! mother of God, I already have enough fap material for several months!"
    Leyna "I-I see..."
    Alexa "Well let's keep playing!"
    Villager "Yeah!"
    scene black with dissolve
    $ show_picture(25, "poker25")
    hide black with dissolve
    Villager "Let's go!!!! beat you again Leyna... you seem to be a little distracted, aren't you?"
    Leyna "I-I don't know what you're talking about... well what's the price?"
    Villager "Let's see .... I'm going to hit you with my penis on your tits... no big deal huh?"
    Johan "What?!"
    $ show_picture(26, "poker26")
    Alexa "Come on Johan! it's not a big deal, it's silly! it's just a game!"
    Leyna "Yes... it's silly... come on let's get it over with, next time I'll win, prepare for humiliation"
    Villager "Perfect! I'll get started"
    $ show_picture(27, "poker27")
    "slap slap slap"
    Leyna "Hmm"
    Villager "Wow you are very hot, do you have a fever?"
    Leyna "N-no... it will be the alcohol"
    "slap slap slap"
    Villager "How soft your tits are"
    Leyna "Sh-shut up"
    "Slap slap slap"
    Villager2 "Ah I'm envious..."
    Villager "Yes... I could be like this all day"
    Johan "W-well, I think that's enough"
    Leyna "Yeah, I can't wait to beat you, you're gonna pay for this one hehehehe"
    "VillageR: Okay okay... I'll stop, now let's keep playing"
    scene black with dissolve
    $ show_picture(28, "poker28")
    hide black with dissolve
    Leyna "Come on! see? I told you I was going to win the next round!"
    Villager "Shit... okay what do you want me to do"
    Leyna "Let's see... have you seen the anime Dragon Orb X?"
    Villager "Yeah... Of course, who hasn't?"
    Leyna "Remember the special team? I want you to do the poses for everyone right now"
    Villager "....  really?...."
    Leyna "Hahahaha yes really"
    Villager "... Shit... all right"
    $ show_picture(29, "poker29")
    Alexa "hahahahahahhaha!!!"
    YoungVillager "Hahahahhahaha!!"
    pause
    $ show_picture(30, "poker30")
    "Johan. Hahahahaha (shit, I couldn't help laughing... as much as I don't like this whole situation, the truth is that I'm starting to enjoy it)"
    Leyna "Hahahahaha very good! have you ever thought of dedicating to this?"
    "VillageR: Shut up (I'll keep this one, next time you'll find out)"
    Leyna "W-well it was great, get ready for the next round I have more prepared for you"
    Villager "... Yeah well... we'll see..."
    Villager "let's keep playing..."
    pause
    scene black with dissolve
    $ show_picture(31, "poker25")
    hide black with dissolve
    Villager "HAhahahahahaha I win again! what were you saying? that you were going to humiliate me?"
    Leyna "..."
    Villager "You have to admit that I'm better than you at this game"
    Leyna "You just got lucky... Well, what do you want as punishment?"
    Villager "All right... sit on my lap"
    Leyna "What?"
    Villager "Sitting on my lap, no big deal, right?"
    Leyna "B-but we are naked"
    Villager "Oh come on, it's no big deal"
    Johan "!!! B-but..."
    Villager "Your wife has made a fool of me in front of everyone, I'm just asking her to sit on my lap"
    Johan "..."
    Leyna "All right, I'll sit on your lap, I think it's just silly"
    Villager "Perfect"
    pause
    $ show_picture(32, "poker31")
    Villager "Ooh great, these views are going to stay with me for the rest of my life"
    Leyna "hmmm"
    Leyna "!!! (He's trying...) hmmmm"
    call GetChoice([_("sit down"), _("avoid the dick")], value=menu_choice, called_from="Bar2EV014_0") from _call_Bar2EV014_0_GetChoice
    $ menu_choice = _return
    if menu_choice == _("sit down"):
        $ menu_choice = None
        Johan "???"
        Leyna "(I-I should stop it... it's... it's so big...)"
        pause
        $ show_picture(33, "poker32")
        Leyna "Mmmha!...."
        Johan "??? (That was a moan?)"
        Villager "Oof... perfect... now I've got some good... views"
        Leyna "E-enjoy while it lasts big guy"
        Leyna "(whispering) ah ah ah"
        Villager2 "I wish I was in that chair, I have to get better at this game"
        YoungVillager "Yes! I' m so envious!"
        Alexa "The game is really getting exciting now"
        pause
        $ show_picture(34, "poker34")
        Johan "W-well, shall we continue playing?"
        Leyna "!! Y-yes, you've had enough, haven't you, big guy?"
        Villager "No, but let's keep on playing hehehe"
        pause
        $ show_picture(35, "poker35")
        "Plop"
        Villager "Oh my God... I like this game more and more by the minute"
        pause
        scene black with dissolve
        $ show_picture(36, "poker25")
        hide black with dissolve
        Villager "It seems that you are really getting nervous Leyna"
        Leyna "W-what are you saying?"
        Villager "What am I saying? I'm back to win another round"
        Leyna "!!! Shit..."
        Villager "don't be sad, this is fun, we are having a good time, right? let's see... what could be your punishment for losing? ...."
        Villager "Yes! earlier I hit you in the tits... now I'll hit you in the pussy, lean against the table with your ass in the air"
        Leyna "!!!.... okay, as you say"
        pause
        $ show_picture(37, "poker37")
        Johan "... (shit... I want to avoid all of this but... between my drunkenness and ... my body reacts by itself, I have an incredible erection...)"
        Johan "(I don't want to get up and let them see it)"
        pause
        $ show_picture(38, "poker36")
        Villager "Wow, perfect! let's start with this"
        Leyna "Don't get too excited, eh?"
        Villager "I will be a gentleman"
        pause
        $ show_picture(39, "poker38")
        play music "audio/Dungeon3.ogg" loop volume 0.9
        "Flap flap flap"
        Leyna "Hmmma!"
        Johan "(that's definitely a moan... is .... enjoying it? )"
        "Flap flap flap"
        Villager "My God... you're dripping down there, honey"
        Leyna "S-shut up"
        Alexa "It looks like you both are having a great time"
        Johan "(shit I wish I didn't have this erection, I should get up and control what's going on... and I'm dizzy from the beers I've had)"
        "flap flap flap"
        pause
        $ show_picture(40, "poker39")
        Leyna "!!!"
        Villager "Ups sorry..."
        $ erase_picture(40)
        "flap flap flap"
        Villager "That's better? although as wet as you are, I could slip in there without wanting to hehehehe"
        Alexa "(whispering) do it"
        Leyna "!!! H-hey..."
        Villager ".... my god... I don't think I can control myself  you know?"
        pause
        $ show_picture(40, "poker40")
        "!!!!"
        Leyna "HmmmaaaA!!! My god!"
        Johan "(its-enough of all this! I have to get up and see that nothing is happening)"
        pause
        $ show_picture(41, "poker41")
        Johan "!!!! (shit, I'm drunk, I can barely stand up)"
        pause
        $ show_picture(42, "poker42")
        Johan "(I-I have to get closer, I can't see anything from here)"
        pause
        $ show_picture(43, "poker43")
        Johan "!!!!(H-he's in! he's got it in!)"
        Villager "Ups sorry man, it seems that I have put it in your wife! it was unintentionally I swear"
        pause
        $ show_picture(44, "poker45")
        Alexa "Hi Johan... Has the cat got your tongue?"
        Alexa "Or do you like what you see? ...."
        Villager "He certainly seems to like what he sees, look at his cock!"
        Johan "I n-no"
        pause
        $ show_picture(45, "poker44")
        play bgs "audio/audio follar.ogg" loop volume 0.9
        Villager "Do you like it, man?"
        "Flap flap flap!!!!"
        Leyna "AAAH!! GOD!!"
        Villager "Do you like to have your wife fucked in front of you?!"
        Johan "S-stop!"
        "Flap flap flap!!"
        Leyna "OH MY GOD!!! YOU ARE BREAKING ME IN HALF!"
        Villager "Watch me tear your wife's pussy apart!"
        stop bgs fadeout 1
        pause
        $ show_picture(46, "poker46")
        Johan "S-stop! Stop at once!"
        "!!!!"
        pause
        $ show_picture(47, "poker47")
        Villager "Hey! want to fight?"
        Alexa "Hey! calm down! let's all calm down... it looks like this has gotten out of hand"
        pause
        $ show_picture(48, "poker48")
        Johan "L-leyna... Leyna? l-let's get out of here! now!"
        YoungVillager "Hahahaha You're drunk Johan you can barely speak"
        Villager2 "Hey Leyna, if you don't want to leave you don't have to, you can stay with us...."
        Leyna "n-no... I'm leaving... I'm leaving with my husband .... I've had enough"
        pause
        scene black with dissolve
        $ show_picture(49, "poker49")
        hide black with dissolve
        "Half an hour later"
        Johan "W-what's going on..."
        Leyna "N-nothing Johan, rest, we are already in the inn... you, just rest...."
        Leyna "Tomorrow will be the end of the festival and we will return home"
        Johan "Yes... I'm looking forward to going home..."
        "Leyna. Me too Johan, me too...."
        pause
        scene black with dissolve
        $ leyna_poker = 1
        stop music fadeout 1
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(4)
        $ erase_picture(5)
        $ erase_picture(6)
        $ erase_picture(7)
        $ erase_picture(8)
        $ erase_picture(9)
        $ erase_picture(10)
        $ erase_picture(11)
        $ erase_picture(12)
        $ erase_picture(13)
        $ erase_picture(14)
        $ erase_picture(15)
        $ erase_picture(16)
        $ erase_picture(17)
        $ erase_picture(18)
        $ erase_picture(19)
        $ erase_picture(20)
        $ erase_picture(21)
        $ erase_picture(22)
        $ erase_picture(23)
        $ erase_picture(24)
        $ erase_picture(25)
        $ erase_picture(26)
        $ erase_picture(27)
        $ erase_picture(28)
        $ erase_picture(29)
        $ erase_picture(30)
        $ erase_picture(31)
        $ erase_picture(32)
        $ erase_picture(33)
        $ erase_picture(35)
        $ erase_picture(34)
        $ erase_picture(36)
        $ erase_picture(37)
        $ erase_picture(38)
        $ erase_picture(39)
        $ erase_picture(40)
        $ erase_picture(41)
        $ erase_picture(42)
        $ erase_picture(43)
        $ erase_picture(44)
        $ erase_picture(45)
        $ erase_picture(46)
        $ erase_picture(47)
        $ erase_picture(48)
        $ erase_picture(49)
        $ set_switch("bet_2", True)
        # TransferPlayer: "InnRooms"
        hide black with dissolve
    elif menu_choice == _("avoid the dick"):
        $ menu_choice = None
        Johan "???"
        Leyna "(I-I should stop it...it's...it's so big....)"
        pause
        $ show_picture(33, "poker33")
        Villager "Oof... perfect... now I've got some good... views"
        Leyna "E-enjoy while it lasts big guy"
        Villager2 "I wish I was in that chair, I have to get better at this game"
        YoungVillager "Yeah!"
        Alexa "Now the game is really getting exciting!"
        pause
        $ show_picture(34, "poker34")
        Johan "W-well, shall we continue playing?"
        Leyna "!!Y-yes, you've had enough, haven't you, big guy?"
        Villager "No, but let's keep on playing hehehe"
        Villager "Oh my God... I like this game more and more by the minute"
        pause
        scene black with dissolve
        $ show_picture(35, "poker25")
        hide black with dissolve
        Villager "It looks like you are really getting nervous Leyna"
        Leyna "W-what are you saying?"
        Villager "What am I saying? I'm back to win another round"
        Leyna "!!! Shit..."
        Villager "Don't be sad, this is fun, we're having a good time, right? let's see... what could be your punishment for losing? ...."
        Villager "Yes! before I hit you in the tits... now I'll hit you in the pussy, lean against the table with your ass in the air"
        Leyna "!!!.... ok"
        pause
        $ show_picture(36, "poker37")
        Johan "... (shit... I want to avoid all of this but... between my drunkenness and ... my body reacts by itself, I have an incredible erection...)"
        Johan "(I don't want to get up and let them see it)"
        pause
        $ show_picture(37, "poker36")
        Villager "Wow, perfect! let's start with this"
        Leyna "Don't get too excited, eh?"
        Villager "I will be a gentleman"
        pause
        $ show_picture(38, "poker38")
        play music "audio/Dungeon3.ogg" loop volume 0.9
        "Flap flap flap"
        Leyna "Hmmma!"
        Johan "(that's definitely a moan... is .... enjoying it? )"
        "Flap flap flap"
        Villager "My God... you're dripping down there, honey"
        Leyna "S-shut up"
        Alexa "It looks like you both are having a great time"
        Johan "(Shit I wish I didn't have this erection, I should get up and control what's going on... and I'm dizzy from all the beers I've had)"
        "flap flap flap"
        pause
        $ show_picture(38, "poker39")
        Leyna "!!!"
        Villager "Ups Sorry..."
        pause
        $ erase_picture(38)
        "flap flap flap"
        Villager "That's better? although as wet as you are, I could slip in there without wanting to hehehehe"
        Alexa "(whispering) do it"
        Leyna "!!! N-no, I think you've had enough... and so have I!"
        Alexa "What? You really want to leave? we're having a good time"
        pause
        $ show_picture(39, "poker37")
        Leyna "Segura... come on Johan let's go"
        Johan "Y-yes... although I-I'm going to need a little help I can barely move"
        YoungVillager "Hahahahaha you're so drunk Johan you can barely speak"
        Villager2 "Hey Leyna, if you don't want to leave you don't have to you can stay with us...."
        Leyna "N-no... I'm leaving... I'm leaving with my husband .... I've had enough"
        pause
        scene black with dissolve
        $ show_picture(40, "poker49")
        hide black with dissolve
        "Half an hour later"
        Johan "W-what's going on..."
        Leyna "N-nothing Johan, rest, we're already at the inn... you just rest..."
        Leyna "Tomorrow will be the end of the festival and we will return home"
        Johan "Yes... I'm looking forward to going home..."
        "Leyna. Me too Johan, me too...."
        pause
        scene black with dissolve
        stop music fadeout 1
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(4)
        $ erase_picture(5)
        $ erase_picture(6)
        $ erase_picture(7)
        $ erase_picture(8)
        $ erase_picture(9)
        $ erase_picture(10)
        $ erase_picture(11)
        $ erase_picture(12)
        $ erase_picture(13)
        $ erase_picture(14)
        $ erase_picture(15)
        $ erase_picture(16)
        $ erase_picture(17)
        $ erase_picture(18)
        $ erase_picture(19)
        $ erase_picture(20)
        $ erase_picture(21)
        $ erase_picture(22)
        $ erase_picture(23)
        $ erase_picture(24)
        $ erase_picture(25)
        $ erase_picture(26)
        $ erase_picture(27)
        $ erase_picture(28)
        $ erase_picture(29)
        $ erase_picture(30)
        $ erase_picture(31)
        $ erase_picture(32)
        $ erase_picture(33)
        $ erase_picture(35)
        $ erase_picture(34)
        $ erase_picture(36)
        $ erase_picture(37)
        $ erase_picture(38)
        $ erase_picture(39)
        $ erase_picture(40)
        $ leyna_poker = 2
        $ set_switch("bet_2", True)
        # TransferPlayer: "InnRooms"
        hide black with dissolve
    return

label Bar2ToBar2_0:
    scene black with dissolve
    # TransferPlayer: "Bar2"
    pause 0.24
    hide black with dissolve
    pause 0.2
    Barman "Hey guys! You're already here in the morning, you're really in the mood to party"
    Johan "Hahahaha no, we just came for a quiet breakfast, I'll have a coffee"
    Leyna "Yes... me too and some toast please"
    Barman "Coming up"
    scene black with dissolve
    $ show_picture(1, "desayuno1")
    hide black with dissolve
    Barman "It's a shame that you don't stay in town, Leyna! since you came here many more people have been coming to the bar"
    Leyna "!!! I-I see"
    Johan "Yes! Leyna is a very hard working girl"
    $ show_picture(2, "desayuno3")
    Villager "You betcha!"
    Villager2 "Yes, Leyna we will miss you very much, this town will not be the same without you"
    Leyna "!!!! I-I see... thanks guys"
    Johan "Hahahahaha in such a short time we have made many friends"
    Leyna "Ye-yeah"
    Barman "Well, I hope you have a good time on your last day in town, when are you going to leave?"
    Johan "The day after tomorrow in the morning, we will take the bus that leaves at 7:00 am"
    Barman "Oh well stop by before you go and I'll invite you to a couple of beers"
    Johan "Sure"
    Villager "Well, we'll let you have breakfast in peace"
    $ show_picture(3, "desayuno4")
    Villager "(whispering) see you this afternoon Leyna, we are going to have a great time"
    Leyna "!!!"
    $ show_picture(4, "desayuno5")
    Johan "Wow... I'm going to miss this town, it's been a very intense couple of days, we haven't partied like this since we were teenagers"
    Leyna "Yes... although I miss our home a little bit"
    Johan "Me too, although this experience has taught me that we were starting to behave like two old people"
    Johan "When we get back to the city we should hang out with our friends a little more"
    Leyna "... Yes, you're right, a little extra fun in our lives would do us a lot of good"
    Johan "Well let's have breakfast and then see what we do, we still have time before the last events of the festival start"
    scene black with dissolve
    $ show_picture(5, "desayuno6")
    hide black with dissolve
    YoungVillager "Hey Leyna!"
    Leyna "!!! G-Good morning"
    Johan "Hey good morning"
    YoungVillager "I've been told that you will be leaving soon"
    Johan "Yes, shortly after the festival"
    $ show_picture(6, "desayuno7")
    YoungVillager "I see... Well Johan, did you like the village?"
    Leyna "!!! (is he going to try?)"
    Johan "Yes, it is a charming town and the people are very friendly"
    YoungVillager "Before you go, I have to show you ....."
    $ show_picture(7, "desayuno8")
    Leyna "(He's trying to stick his dick in me right here? in front of Johan?)"
    Johan "... Oh I would love to..."
    Leyna "!!!"
    $ show_picture(8, "desayuno9")
    if switch("corruption_low"):
        pause
        Leyna "(I can't allow it! but I don't want to cause problems for Johan)"
        pause
        $ show_picture(9, "desayuno19")
        YoungVillager "!!! Ouch!"
        Leyna "Ups Sorry, I'm going to the bathroom, did I hurt you?"
        YoungVillager "N-no, don't worry, I'm fine"
        $ show_picture(10, "desayuno6")
        Johan "(Did he have his dick out?... no, that' s just my imagination)"
        YoungVillager "Well guys, it's been a pleasure and we'll see you at the festival"
        Johan "Sure... see you soon"
        scene black with dissolve
        $ show_picture(11, "desayuno18")
        hide black with dissolve
        Johan "Well, you want to go for a ride? we should go to the festival grounds and see if they're building anything special for the last day"
        Leyna "I don't think it's a good idea, we should let them work"
        Johan "It's okay, I have the mayor's permission and it will be good for the article to see what they are doing to prepare everything"
        Leyna "If you think it's a good idea..."
        Johan "Yes, Yes, let's go to the festival"
        scene black with dissolve
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(4)
        $ erase_picture(5)
        $ erase_picture(6)
        $ erase_picture(7)
        $ erase_picture(8)
        $ erase_picture(9)
        $ erase_picture(10)
        $ erase_picture(11)
        $ set_switch("last_bar", True)
        # TransferPlayer: "Town2"
        hide black with dissolve
    if switch("corruption_high"):
        Villager "Hey Johan, I want to ask you a couple of questions about the article...."
        Johan "Oh Sure"
        Villager "Tell me... do you think you could put my online business in there somewhere?"
        pause
        $ show_picture(9, "desayuno8")
        Leyna "You... (whispering) stop..."
        YoungVillager "I'm not going to do it, I know you're wishing it"
        Leyna "...."
        pause
        $ show_picture(10, "desayuno10")
        "Flap flap flap"
        YoungVillager "See? you're dripping"
        Johan "I don't know man... I'd have to check it out"
        pause
        $ show_picture(11, "desayuno11")
        Leyna "!!! (Johan is right next to us)"
        Leyna "(whispering) stop it, we're going to get caught"
        pause
        $ show_picture(12, "desayuno12")
        YoungVillager "I will take that risk"
        Leyna "Hmmmmf...!"
        pause
        $ show_picture(13, "desayuno14")
        Johan "??? Everything okay Leyna?"
        Leyna "Y-yes everything's fine... fine"
        YoungVillager "(whispering) See? I told you you were looking forward to it"
        pause
        $ show_picture(14, "desayuno13")
        play bgs "audio/audio follar.ogg" loop volume 0.9
        Leyna "Ah... (My God if Johan catches us, it would be the end... but it feels so good... every day I care less and less if they see us or not... I just want to...)"
        Leyna "... mmf mmmf mmf..."
        YoungVillager "(Whispering) Hey... be quiet or we'll get caught by your husband hehehehehe"
        Leyna "Sh-shut up..."
        "Flap flap flap"
        Leyna "(whispering) Br-brake down a little, you're going too fast"
        YoungVillager "(whispering) uff now I can't slow down... I'm going to cum..."
        Leyna "(whispering) Wh-what? stop... not here please"
        pause
        $ show_picture(15, "desayuno15")
        "flap flap flap"
        Leyna "Hmmmmff!"
        Leyna "(it seems that Johan is talking about work and doesn't realize anything)"
        YoungVillager "My God... you're perfect, I can't take it anymore"
        Leyna "!!!!"
        pause
        $ flash_screen([255,255,255,170], 60, True)
        $ flash_screen([255,255,255,170], 60, True)
        $ show_picture(16, "desayuno16")
        stop bgs fadeout 1
        YoungVillager "ahh... I was looking forward to it, I couldn't let you leave town without doing this"
        Leyna "...."
        Leyna "(has he cum already?... I wanted... I wanted more...)"
        YoungVillager "??? Well, see you at the festival"
        pause
        $ show_picture(17, "desayuno17")
        Leyna "(Whispering) W-wait, you're going to leave me like this?"
        YoungVillager "Well, if you want to repeat..."
        Leyna "I-I didn't mean that..."
        YoungVillager "Well then, I'll see you later"
        Leyna "!!! (nasty fucker)"
        Villager "Thank you Johan, let's talk, I leave you my phone number"
        Johan "Sure"
        $ show_picture(18, "desayuno18")
        Johan "Leyna? you look a little... heated"
        Leyna "Y-yeah I'm fine, I'm going to go to the bathroom for a second, I'll be right out"
        Johan "Great, I'll wait for you outside and we'll go to the festival"
        Leyna "Okay"
        scene black with dissolve
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(4)
        $ erase_picture(5)
        $ erase_picture(6)
        $ erase_picture(7)
        $ erase_picture(8)
        $ erase_picture(9)
        $ erase_picture(10)
        $ erase_picture(11)
        $ erase_picture(12)
        $ erase_picture(13)
        $ erase_picture(14)
        $ erase_picture(15)
        $ erase_picture(16)
        $ erase_picture(17)
        $ erase_picture(18)
        $ set_switch("last_bar", True)
        # TransferPlayer: "Town2"
        hide black with dissolve
    if switch("corruption_average"):
        pause
        Leyna "(I can't allow it! but I don't want to cause problems for Johan)"
        pause
        $ show_picture(9, "desayuno19")
        YoungVillager "!!! Ouch!"
        Leyna "Ups Sorry, I'm going to the bathroom, did I hurt you?"
        YoungVillager "N-no, don't worry, I'm fine"
        $ show_picture(10, "desayuno6")
        Johan "(Did he have his dick out?... no, that' s just my imagination)"
        YoungVillager "Well guys, it's been a pleasure and we'll see you at the festival"
        Johan "Sure... see you soon"
        scene black with dissolve
        $ show_picture(11, "desayuno18")
        hide black with dissolve
        Johan "Well, you want to go for a ride? we should go to the festival grounds and see if they're building anything special for the last day"
        Leyna "I don't think it's a good idea, we should let them work"
        Johan "It's okay, I have the mayor's permission and it will be good for the article to see what they are doing to prepare everything"
        Leyna "If you think it's a good idea..."
        Johan "Yes, Yes, let's go to the festival"
        scene black with dissolve
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(4)
        $ erase_picture(5)
        $ erase_picture(6)
        $ erase_picture(7)
        $ erase_picture(8)
        $ erase_picture(9)
        $ erase_picture(10)
        $ erase_picture(11)
        $ set_switch("last_bar", True)
        # TransferPlayer: "Town2"
        hide black with dissolve
    return

label Bar2LeynawhatAreYouDoingHereIThoughtYouWereLeavingTownThisMorning_0:
    scene black with dissolve
    $ show_picture(1, "barfinal1")
    hide black with dissolve
    Barman "Leyna?...what are you doing here? I thought you were leaving town this morning?"
    Leyna "I'm going to leave in a while, Johan is probably waiting for the bus at the exit of the village... waiting for me"
    Barman "Waiting for you... I don't know Leyna, after yesterday I would not be so sure..."
    Leyna "Yeah... I guess you're right... I guess that's why I've come here, at this point..."
    pause
    $ show_picture(2, "barfinal2")
    Leyna "You've helped me a lot these last few days... giving me work... you've been so good to me"
    Barman "L-leyna?"
    Leyna "Come on... I just came to return the favor... you are the only one in town who hasn't tried anything with me..."
    Leyna "But I feel the sexual tension... how you look at me..."
    Barman "I... no..."
    pause
    $ show_picture(3, "barfinal3")
    Leyna "Who are you trying to fool... just by approaching you and talking to you about it, you're already excited, your pants are about to burst"
    Barman "L-leyna there are customers in front of us... we should not..."
    Leyna "Since when has that been a problem in this town?"
    $ show_picture(4, "pantallanegro", scale=(120, 120), width=816, height=600)
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    Leyna "See? I knew it..."
    pause
    $ show_picture(6, "barfinal5")
    Leyna "Look at you... this must be very uncomfortable..."
    Barman "Leyna...."
    Leyna "You don't need to say anything... my goodness, everyone in this town has a huge dick, but you take the prize, you have the biggest dick I've ever seen"
    Leyna "It must be very uncomfortable to go like that... let me help you with this"
    pause
    $ show_picture(7, "barfinal6")
    Leyna "Hmmmm..."
    Leyna "My God... I can't fit in my mouth"
    Villager "Fuck, I' m so envious, Leyna is sucking your dick..."
    Barman "Aahhh..."
    Leyna "I can't do much more with this monster between your legs...."
    Leyna "I wonder if I'll fit down there?....."
    pause
    $ show_picture(8, "barfinal7")
    Leyna "Let's give it a try..."
    Barman "W-what... here in front of everybody?"
    Villager "Come on boss! either you do it or I do it!"
    Leyna "Come on, don't make me wait, you know you're looking forward to it"
    Barman "All right... here I come"
    pause
    $ show_picture(9, "barfinal8")
    Barman "Ahh... you're burning up... it's so tight..."
    Leyna "Come on, I can't wait any longer... put it all the way in me"
    Barman "All right, get ready"
    Leyna "Ahhh."
    pause
    $ show_picture(10, "barfinal9")
    play bgs "audio/audio follar.ogg" loop volume 0.9
    Leyna "Aaah!!"
    Villager "Fuck! the whole town will hear you! hahahaha"
    Barman "Fuck! how good you feel Leyna! you have the best pussy I've ever felt in my life!"
    Leyna "Ah ah ah! THANK YOU... now shut up and keep on fucking me"
    Barman "Yes! ah!!"
    pause
    $ show_picture(11, "barfinal10")
    play bgs "audio/audio follar.ogg" loop volume 0.9
    Leyna "AAahhh!! Ah!!! G-God F-fuck me! Daddy Fuck me!"
    Villager "Shit... I've got a hard-on... I could jerk off watching this..."
    Leyna "Keep it up! hard! please give me more!!!!"
    Barman "You want me to go harder? very well! now you'll see!"
    Leyna "!!!! W-what are you going to..."
    pause
    $ show_picture(12, "barfinal11")
    Leyna "Fuuuuck!!!! AAAH!!!!!"
    Barman "You like it, bitch? this is what you wanted, right?!"
    Leyna "Yes daddy, I-i love it!!!! Ah! ah! ah! ah! give me... h-hard!"
    Villager "What a fucking energy!"
    Leyna "My God! You're impaling me!.... Fuuuck!!!"
    Leyna "Ah ah ah !! I-I'm going to C-cum!!!"
    Barman "Me too!!...god I can't take it anymore!!!"
    pause
    $ flash_screen([255,255,255,170], 60, True)
    $ flash_screen([255,255,255,170], 60, True)
    $ show_picture(13, "barfinal12")
    $ flash_screen([255,255,255,170], 60, False)
    $ shake_screen(5, 5, 60)
    Barman "Fuck!... ahhhhh"
    Leyna "AAAAhhh!!! ...."
    Leyna "Ah ah ah...  W-we came at the same time... it never happened to me before with anyone else hihihi"
    Barman "Ah ah ah..."
    Leyna "Well... I'm leaving, I wanted to return the favor for everything you've done for me"
    Barman "W-what? and that's it?"
    Leyna "Yes... I may come back someday to visit you"
    Barman "... God... what a woman..."
    $ final_day = final_day + 1
    scene black with dissolve
    $ erase_picture(1)
    $ erase_picture(2)
    $ erase_picture(3)
    $ erase_picture(4)
    $ erase_picture(5)
    $ erase_picture(6)
    $ erase_picture(7)
    $ erase_picture(8)
    $ erase_picture(9)
    $ erase_picture(10)
    $ erase_picture(11)
    $ erase_picture(12)
    $ erase_picture(13)
    # TransferPlayer: "Town2"
    hide black with dissolve
    return

