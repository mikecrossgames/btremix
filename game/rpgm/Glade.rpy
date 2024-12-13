label GladeImSureHeWontFindMeHereThisAreaIsALittleScaryAtNightThough_0(menu_choice = None):
    Leyna "I'm sure he won't find me here. This area is a little scary at night though"
    if jail == 1:
        scene black with dissolve
        $ hiding_place = 2
        hide black with dissolve
        pause 0.2
        Prisoner "They finally got me out of the cell... because of that woman, they left me locked up for a couple of days longer than I should have been"
        Prisoner "If I see her around town, she's going to find out who I am"
        "Prisioner: I'm going to take the \"special package\" I have hidden around here and go back to the party with my friends"
        pause 0.28
        pause 0.2
        $ show_picture(1, "revenge1")
        Prisoner "... wait a second, that's her? I can't believe it. Well, she's going to find out, she's going to pay me back for the other day"
        $ show_picture(2, "revenge2")
        Prisoner "I caught you bitch! Remember me?"
        Leyna "You... you are the prisoner from the other day! The one who tried to..."
        Prisoner "Exactly! The one who tried to spend some quality time with you! But you were too good for me, right?"
        Prisoner "Because of you I got locked up a lot more than I should have! And you're going to pay for it! You have to take responsibility for your actions!"
        Leyna "No! Stop!"
        Prisoner "You want me to stop? You fucking bitch! Now you'll see!"
        call GetChoice([_("Fight back!"), _("Surrender!")], value=menu_choice, called_from="GladeEV004_0") from _call_GladeEV004_0_GetChoice
        $ menu_choice = _return
        if menu_choice == _("Fight back!"):
            $ menu_choice = None
            $ show_picture(3, "revenge3")
            play sound "audio/Blow3.ogg" volume 0.9 noloop
            Leyna "YOU MOTHER FUCKER!"
            Prisoner "Uogh!!!"
            $ show_picture(4, "pantallanegro", scale=(120, 120), width=816, height=600)
            play sound "audio/Run.ogg" volume 0.9 noloop
            pause
            scene black with dissolve
            # TransferPlayer: "TownFestivalNight"
            $ erase_picture(1)
            $ erase_picture(2)
            $ erase_picture(3)
            $ erase_picture(4)
            hide black with dissolve
            pause 0.24
            pause 0.2
            Leyna "Wow... Those two years training kyokushin karate have done me some good"
            $ hiding_place = 3
        elif menu_choice == _("Surrender!"):
            $ menu_choice = None
            Leyna "Ple-please do whatever you want, but don't hurt me"
            $ show_picture(3, "revenge4")
            Prisoner "You stay still and let me do my job. Let's see those tits! I didn't get a good look at them the other day!"
            "Prisioner: Wow! You have the biggest, most perfect tits I've ever seen!"
            Prisoner "you couldn't expect anything to happen to you, walking around in these clothes, could you? what a bitch you are!"
            Leyna "Please... don't do it"
            $ show_picture(4, "revenge5")
            Prisoner "Shut up, let me touch them...incredible, you have an incredible body and now it's mine, I'm going to enjoy it to the fullest"
            Leyna "!!!"
            Prisoner "Wow your nipples are getting hard! You're such a bitch, you say no, but your body is telling me yes!"
            Leyna "I--I.."
            $ show_picture(5, "revenge6")
            Prisoner "And these panties you're wearing? who are they for? They barely cover anything!"
            Leyna "....!!!"
            Prisoner "Turn around!"
            Leyna "No, wait!"
            $ show_picture(6, "revenge7")
            Prisoner "It couldn't be any other way! the perfect ass! and... I can't believe it, you're soaking wet down there!"
            Prisoner "Well I'm going to help you! I'm going to fuck you right here and right now you slut!"
            Leyna "!!!"
            Leyna "W-wait a second please!"
            Prisoner "No way, I can't wait a second to fuck a goddess like you"
            Leyna "(A-a goddess?.... why do I like this man talking to me like this? Why I'm enjoying this?)"
            $ show_picture(7, "revenge8")
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
            $ play_video_looped(1, "revenge_webm", "revenge.webm",width=1920,height=1080)
            pause
            Leyna "HARDER! HARDER! FUCK MEEEE!!"
            Prisoner "Oh! I'm going to cum! I'm going to cum!"
            Leyna "Wait!!!! Not inside please!"
            stop music fadeout 1
            $ flash_screen([255,255,255,170], 60, True)
            $ show_picture(8, "revenge9")
            play sound "audio/Poison.ogg" volume 0.9 noloop
            $ flash_screen([255,255,255,170], 60, True)
            Prisoner "OOOhhhhhh.... nice, it's been years since I've fucked.. and never with a goddess like you"
            Leyna "This... this shouldn't have happened"
            Prisoner "I'm sure you've never been fucked like this before, not even by your limp dick of a husband!"
            $ show_picture(9, "revenge10")
            Leyna "Shut up... leave me alone, get out of here please!"
            Prisoner "Tch! As you wish... if you ever want to come again, I'll be in town"
            Leyna "...."
            $ hiding_place = 4
            scene black with dissolve
            # TransferPlayer: "TownFestivalNight"
            $ erase_picture(1)
            $ erase_picture(2)
            $ erase_picture(3)
            $ erase_picture(4)
            $ erase_picture(5)
            $ erase_picture(6)
            $ erase_picture(7)
            $ erase_picture(8)
            $ erase_picture(9)
            hide black with dissolve
            pause 0.24
            pause 0.2
            Leyna "How could this have happened... Since I got here, bad things have not stopped happening to me."
            Leyna "I don't recognize myself"
    if jail == 0:
        scene black with dissolve
        $ hiding_place = 2
        hide black with dissolve
        pause 0.2
        Prisoner "They finally got me out of the cell... I shouldn't hit the party so hard, but it's not easy being an alpha male"
        "Prisioner: I'm going to take the \"special package\" I have hidden around here and go back to the party with my friends"
        pause 0.28
        pause 0.2
        $ show_picture(1, "revenge1")
        Prisoner "Wait a second... Who is that goddess? And look how she's dressed! Being here alone..."
        Prisoner "Oh I get it, one of my friends told me something about this... cruising or something like that right? I'm sure she wants to fuck"
        Prisoner "Great, I can't believe I'm so lucky. I haven't fuck in years"
        $ show_picture(2, "revenge2")
        Prisoner "I caught you bitch! I didn't know there was such a horny girl in town, but I understand you, you just need a little action uh?"
        Leyna "Wha-what are you talking about? Please let go of me"
        Prisoner "Ohh I see, so you're into role playing too? Fine for me Come on bitch, come here I'm gonna stick it all the way in you"
        Leyna "No! Stop!"
        Prisoner "You want me to stop? You fucking bitch! Now you'll see!"
        call GetChoice([_("Fight back!"), _("Surrender!")], value=menu_choice, called_from="GladeEV004_0") from _call_GladeEV004_0_GetChoice_1
        $ menu_choice = _return
        if menu_choice == _("Fight back!"):
            $ menu_choice = None
            $ show_picture(3, "revenge3")
            play sound "audio/Blow3.ogg" volume 0.9 noloop
            Leyna "YOU MOTHER FUCKER!"
            Prisoner "Uogh!!!"
            $ show_picture(4, "pantallanegro", scale=(120, 120), width=816, height=600)
            play sound "audio/Run.ogg" volume 0.9 noloop
            pause
            scene black with dissolve
            # TransferPlayer: "TownFestivalNight"
            $ erase_picture(1)
            $ erase_picture(2)
            $ erase_picture(3)
            $ erase_picture(4)
            hide black with dissolve
            pause 0.24
            pause 0.2
            Leyna "Wow... Those two years training kyokushin karate have done me some good"
            $ hiding_place = 3
        elif menu_choice == _("Surrender!"):
            $ menu_choice = None
            Leyna "Ple-please do whatever you want, but don't hurt me"
            $ show_picture(3, "revenge4")
            Prisoner "You stay still and let me do my job. Let's see those tits!"
            "Prisioner: Wow! You have the biggest, most perfect tits I've ever seen!"
            Prisoner "you couldn't expect anything to happen to you, walking around in these clothes, could you? what a bitch you are!"
            Leyna "Please... don't do it"
            $ show_picture(4, "revenge5")
            Prisoner "Shut up, let me touch them...incredible, you have an incredible body and now it's mine, I'm going to enjoy it to the fullest"
            Leyna "!!!"
            Prisoner "Wow your nipples are getting hard! You're such a bitch, you say no, but your body is telling me yes!"
            Leyna "I--I.."
            $ show_picture(5, "revenge6")
            Prisoner "And these panties you're wearing? who are they for? They barely cover anything!"
            Leyna "....!!!"
            Prisoner "Turn around!"
            Leyna "No, wait!"
            $ show_picture(6, "revenge7")
            Prisoner "It couldn't be any other way! the perfect ass! and... I can't believe it, you're soaking wet down there!"
            Prisoner "Well I'm going to help you! I'm going to fuck you right here and right now you slut!"
            Leyna "!!!"
            Leyna "W-wait a second please!"
            Prisoner "No way, I can't wait a second to fuck a goddess like you"
            Leyna "(A-a goddess?.... why do I like this man talking to me like this? Why I'm enjoying this?)"
            $ show_picture(7, "revenge8")
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
            $ play_video_looped(1, "revenge_webm", "revenge.webm",width=1920,height=1080)
            pause
            Leyna "HARDER! HARDER! FUCK MEEEE!!"
            Prisoner "Oh! I'm going to cum! I'm going to cum!"
            Leyna "Wait!!!! Not inside please!"
            stop music fadeout 1
            $ flash_screen([255,255,255,170], 60, True)
            $ show_picture(8, "revenge9")
            play sound "audio/Poison.ogg" volume 0.9 noloop
            $ flash_screen([255,255,255,170], 60, True)
            Prisoner "OOOhhhhhh.... nice, it's been years since I've fucked.. and never with a goddess like you"
            Leyna "This... this shouldn't have happened"
            Prisoner "I'm sure you've never been fucked like this before, not even by your limp dick of a husband! ... if you have one"
            $ show_picture(9, "revenge10")
            Leyna "Shut up... leave me alone, get out of here please!"
            Prisoner "Tch! As you wish... if you ever want to come again, I'll be in town"
            Leyna "...."
            $ hiding_place = 4
            scene black with dissolve
            # TransferPlayer: "TownFestivalNight"
            $ erase_picture(1)
            $ erase_picture(2)
            $ erase_picture(3)
            $ erase_picture(4)
            $ erase_picture(5)
            $ erase_picture(6)
            $ erase_picture(7)
            $ erase_picture(8)
            $ erase_picture(9)
            hide black with dissolve
            pause 0.24
            pause 0.2
            Leyna "How could this have happened... Since I got here, bad things have not stopped happening to me."
            Leyna "I don't recognize myself"
    return

label Gladecontinuacionfestival_0:
    $ tint_screen((0, 0, 0, 0), 60, True)
    pause 0.36
    pause 0.2
    Johan "My God... I feel like a truck has passed over my head"
    Johan "I don't think I've ever had such a hangover... what the hell happened last night?"
    $ flash_screen([255,255,255,170], 60, True)
    $ show_picture(1, "festivalnoche5", width=814, height=625)
    pause
    $ erase_picture(1)
    Johan "Ugh that happened right?...what a shame...with how bad I dance...anyway...the rest seems very blurry"
    Johan "Yes, it's true that I got very very drunk, but even so, it seems that I had more than just alcohol..."
    Johan "I have been drunk on other occasions and I had not behaved like this... and the next day I did not have this horrible condition"
    Johan ".... Although there's also the option that I'm getting older..."
    Johan "Hehehehehe although when you have a hangover no matter how bad you feel you feel like a teenager again...."
    Johan "Although... what happened the rest of the night?... I remember Leyna worked late at the food stand and then..."
    $ flash_screen([255,255,255,170], 60, True)
    if festival_clothes == 1:
        $ show_picture(1, "festivalnoche23", width=814, height=625)
    if festival_clothes == 2:
        $ show_picture(1, "festivalnoche31", width=814, height=625)
    pause
    $ erase_picture(1)
    pause 0.2
    Johan "Le-leyna? ... that happened? but... I think it was another girl, wasn't it?... ahhh I can hardly remember it"
    Johan "Shit, I feel helpless..."
    Johan "Although I think something important happened later... that I should remember... it's all so confusing..."
    $ flash_screen([255,255,255,170], 60, True)
    $ show_picture(1, "festivalnoche28", width=814, height=625)
    pause
    $ erase_picture(1)
    Johan "!!! Tha-that didn't really happen, did it?"
    Johan "What the hell have you done Johan? What the hell was going through your head? Always thinking with your dick..."
    Johan "Shit, I have to find Leyna... I don't even know how I ended up here..."
    Johan "At least I have my clothes on and not those ridiculous festival clothes"
    return

