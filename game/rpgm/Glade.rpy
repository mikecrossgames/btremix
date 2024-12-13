label GladeBG:
    $ set_transparency_backgrounds(["bg_glade"])
    $ set_map_backgrounds(["map_glade"])
    return

label GladeStart:
    call GladeBG from _call_GladeBG
    stop music
    stop bgs
    return

label GladeEnd:
    return

label GladeWelcomeToTheCumZoneBase:
    $ event_erased = False
    "Welcome to the cum zone"
    $ event_erased = True
    return event_erased

label GladeWelcomeToTheCumZone(play_event = True, trigger = None): # event
    if is_erased("GladeWelcomeToTheCumZone"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "GladeWelcomeToTheCumZoneBase", "GladeWelcomeToTheCumZone") from _call_GladeWelcomeToTheCumZone_PlayEvent
        return (1, "", "GladeWelcomeToTheCumZone")
    return None

label GladeToTown_0:
    call TransferPlayer("Town", "GladeEV002_0", 49, 32, direction=4) from _call_GladeEV002_0_TransferPlayer
    $ resolve_scene()
    return False

label GladeToTown_1:
    call TransferPlayer("Town2", "GladeEV002_1", 49, 32, direction=4) from _call_GladeEV002_1_TransferPlayer
    $ resolve_scene()
    return False

label GladeToTown(play_event = True, trigger = None): # event
    if is_erased("GladeToTown"):
        return None
    elif trigger == "event" and switch("third_day"):
        call PlayEvent(play_event, "GladeToTown_1", "GladeToTown") from _call_GladeToTown_1_PlayEvent
        return (0, "", "GladeToTown_1")
    elif trigger == "event":
        call PlayEvent(play_event, "GladeToTown_0", "GladeToTown") from _call_GladeToTown_0_PlayEvent
        return (0, "", "GladeToTown_0")
    return None

label GladeToTown_v2_0:
    call TransferPlayer("Town", "GladeEV003_0", 49, 33, direction=0) from _call_GladeEV003_0_TransferPlayer
    $ resolve_scene()
    return False

label GladeToTown_v2_1:
    call TransferPlayer("Town2", "GladeEV003_1", 49, 33, direction=0) from _call_GladeEV003_1_TransferPlayer
    $ resolve_scene()
    return False

label GladeToTown_v2(play_event = True, trigger = None): # event
    if is_erased("GladeToTown_v2"):
        return None
    elif trigger == "event" and switch("third_day"):
        call PlayEvent(play_event, "GladeToTown_v2_1", "GladeToTown_v2") from _call_GladeToTown_v2_1_PlayEvent
        return (0, "", "GladeToTown_v2_1")
    elif trigger == "event":
        call PlayEvent(play_event, "GladeToTown_v2_0", "GladeToTown_v2") from _call_GladeToTown_v2_0_PlayEvent
        return (0, "", "GladeToTown_v2_0")
    return None

label GladeImSureHeWontFindMeHereThisAreaIsALittleScaryAtNightThough_0(menu_choice = None):
    Leyna "I'm sure he won't find me here. This area is a little scary at night though"
    if jail == 1:
        $ fade_out()
        $ hiding_place = 2
        $ fade_in()
        $ resolve_scene()
        call PauseForBalloon("GladeEV004_0") from _call_GladeEV004_0_PauseForBalloon
        Prisoner "They finally got me out of the cell... because of that woman, they left me locked up for a couple of days longer than I should have been"
        Prisoner "If I see her around town, she's going to find out who I am"
        "Prisioner: I'm going to take the \"special package\" I have hidden around here and go back to the party with my friends"
        call Movement("GladeEV004_0", "Gladevengador", ["D","R","R","TURN_U"]) from _call_GladeEV004_0_Movement
        $ resolve_scene()
        call PauseForBalloon("GladeEV004_0") from _call_GladeEV004_0_PauseForBalloon_1
        $ show_picture(1, "revenge1")
        $ resolve_scene()
        Prisoner "... wait a second, that's her? I can't believe it. Well, she's going to find out, she's going to pay me back for the other day"
        $ show_picture(2, "revenge2")
        $ resolve_scene()
        Prisoner "I caught you bitch! Remember me?"
        Leyna "You... you are the prisoner from the other day! The one who tried to..."
        Prisoner "Exactly! The one who tried to spend some quality time with you! But you were too good for me, right?"
        Prisoner "Because of you I got locked up a lot more than I should have! And you're going to pay for it! You have to take responsibility for your actions!"
        Leyna "No! Stop!"
        Prisoner "You want me to stop? You fucking bitch! Now you'll see!"
        call GetChoice([_("Fight back! "), _("Surrender! ")], value=menu_choice, called_from="GladeEV004_0") from _call_GladeEV004_0_GetChoice
        $ menu_choice = _return
        if menu_choice == _("Fight back! "):
            $ menu_choice = None
            $ show_picture(3, "revenge3")
            call PlaySound("sound", "audio/Blow3.ogg", volume=0.9, no_loop=True) from _call_GladeEV004_0_PlaySound
            $ resolve_scene()
            Leyna "YOU MOTHER FUCKER!"
            Prisoner "Uogh!!!"
            $ show_picture(4, "pantallanegro", scale=(120, 120), width=816, height=600)
            call PlaySound("sound", "audio/Run.ogg", volume=0.9, no_loop=True) from _call_GladeEV004_0_PlaySound_1
            $ resolve_scene()
            pause
            $ fade_out()
            call TransferPlayer("TownFestivalNight", "GladeEV004_0", 49, 29, direction=4) from _call_GladeEV004_0_TransferPlayer
            $ erase_picture(1)
            $ erase_picture(2)
            $ erase_picture(3)
            $ erase_picture(4)
            $ fade_in()
            call Movement("GladeEV004_0", "player", ["L","L"]) from _call_GladeEV004_0_Movement_1
            $ resolve_scene()
            call PauseForBalloon("GladeEV004_0") from _call_GladeEV004_0_PauseForBalloon_2
            Leyna "Wow... Those two years training kyokushin karate have done me some good"
            $ hiding_place = 3
        elif menu_choice == _("Surrender! "):
            $ menu_choice = None
            Leyna "Ple-please do whatever you want, but don't hurt me"
            $ show_picture(3, "revenge4")
            $ resolve_scene()
            Prisoner "You stay still and let me do my job. Let's see those tits! I didn't get a good look at them the other day!"
            "Prisioner: Wow! You have the biggest, most perfect tits I've ever seen!"
            Prisoner "you couldn't expect anything to happen to you, walking around in these clothes, could you? what a bitch you are!"
            Leyna "Please... don't do it"
            $ show_picture(4, "revenge5")
            $ resolve_scene()
            Prisoner "Shut up, let me touch them...incredible, you have an incredible body and now it's mine, I'm going to enjoy it to the fullest"
            Leyna "!!!"
            Prisoner "Wow your nipples are getting hard! You're such a bitch, you say no, but your body is telling me yes!"
            Leyna "I--I.."
            $ show_picture(5, "revenge6")
            $ resolve_scene()
            Prisoner "And these panties you're wearing? who are they for? They barely cover anything!"
            Leyna "....!!!"
            Prisoner "Turn around!"
            Leyna "No, wait!"
            $ show_picture(6, "revenge7")
            $ resolve_scene()
            Prisoner "It couldn't be any other way! the perfect ass! and... I can't believe it, you're soaking wet down there!"
            Prisoner "Well I'm going to help you! I'm going to fuck you right here and right now you slut!"
            Leyna "!!!"
            Leyna "W-wait a second please!"
            Prisoner "No way, I can't wait a second to fuck a goddess like you"
            Leyna "(A-a goddess?.... why do I like this man talking to me like this? Why I'm enjoying this?)"
            $ show_picture(7, "revenge8")
            $ resolve_scene()
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
            call PlaySound("music", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_GladeEV004_0_PlaySound_2
            $ play_video_looped(1, "revenge_webm", "revenge.webm",width=1920,height=1080)
            $ resolve_scene()
            pause
            Leyna "HARDER! HARDER! FUCK MEEEE!!"
            Prisoner "Oh! I'm going to cum! I'm going to cum!"
            Leyna "Wait!!!! Not inside please!"
            stop music fadeout 1
            $ flash_screen([255,255,255,170], 60, True)
            $ show_picture(8, "revenge9")
            call PlaySound("sound", "audio/Poison.ogg", volume=0.9, no_loop=True) from _call_GladeEV004_0_PlaySound_3
            $ resolve_scene()
            $ flash_screen([255,255,255,170], 60, True)
            Prisoner "OOOhhhhhh.... nice, it's been years since I've fucked.. and never with a goddess like you"
            Leyna "This... this shouldn't have happened"
            Prisoner "I'm sure you've never been fucked like this before, not even by your limp dick of a husband!"
            $ show_picture(9, "revenge10")
            $ resolve_scene()
            Leyna "Shut up... leave me alone, get out of here please!"
            Prisoner "Tch! As you wish... if you ever want to come again, I'll be in town"
            Leyna "...."
            $ hiding_place = 4
            call GalleryViewed("revenge") from _call_GladeEV004_0_GalleryViewed
            $ fade_out()
            call TransferPlayer("TownFestivalNight", "GladeEV004_0", 49, 29, direction=4) from _call_GladeEV004_0_TransferPlayer_1
            $ erase_picture(1)
            $ erase_picture(2)
            $ erase_picture(3)
            $ erase_picture(4)
            $ erase_picture(5)
            $ erase_picture(6)
            $ erase_picture(7)
            $ erase_picture(8)
            $ erase_picture(9)
            $ fade_in()
            call Movement("GladeEV004_0", "player", ["L","L"]) from _call_GladeEV004_0_Movement_2
            $ resolve_scene()
            call PauseForBalloon("GladeEV004_0") from _call_GladeEV004_0_PauseForBalloon_3
            Leyna "How could this have happened... Since I got here, bad things have not stopped happening to me."
            Leyna "I don't recognize myself"
    if jail == 0:
        $ fade_out()
        $ hiding_place = 2
        $ fade_in()
        $ resolve_scene()
        call PauseForBalloon("GladeEV004_0") from _call_GladeEV004_0_PauseForBalloon_4
        Prisoner "They finally got me out of the cell... I shouldn't hit the party so hard, but it's not easy being an alpha male"
        "Prisioner: I'm going to take the \"special package\" I have hidden around here and go back to the party with my friends"
        call Movement("GladeEV004_0", "Gladevengador", ["D","R","R","TURN_U"]) from _call_GladeEV004_0_Movement_3
        $ resolve_scene()
        call PauseForBalloon("GladeEV004_0") from _call_GladeEV004_0_PauseForBalloon_5
        $ show_picture(1, "revenge1")
        $ resolve_scene()
        Prisoner "Wait a second... Who is that goddess? And look how she's dressed! Being here alone..."
        Prisoner "Oh I get it, one of my friends told me something about this... cruising or something like that right? I'm sure she wants to fuck"
        Prisoner "Great, I can't believe I'm so lucky. I haven't fuck in years"
        $ show_picture(2, "revenge2")
        $ resolve_scene()
        Prisoner "I caught you bitch! I didn't know there was such a horny girl in town, but I understand you, you just need a little action uh?"
        Leyna "Wha-what are you talking about? Please let go of me"
        Prisoner "Ohh I see, so you're into role playing too? Fine for me Come on bitch, come here I'm gonna stick it all the way in you"
        Leyna "No! Stop!"
        Prisoner "You want me to stop? You fucking bitch! Now you'll see!"
        call GetChoice([_("Fight back! "), _("Surrender! ")], value=menu_choice, called_from="GladeEV004_0") from _call_GladeEV004_0_GetChoice_1
        $ menu_choice = _return
        if menu_choice == _("Fight back! "):
            $ menu_choice = None
            $ show_picture(3, "revenge3")
            call PlaySound("sound", "audio/Blow3.ogg", volume=0.9, no_loop=True) from _call_GladeEV004_0_PlaySound_4
            $ resolve_scene()
            Leyna "YOU MOTHER FUCKER!"
            Prisoner "Uogh!!!"
            $ show_picture(4, "pantallanegro", scale=(120, 120), width=816, height=600)
            call PlaySound("sound", "audio/Run.ogg", volume=0.9, no_loop=True) from _call_GladeEV004_0_PlaySound_5
            $ resolve_scene()
            pause
            $ fade_out()
            call TransferPlayer("TownFestivalNight", "GladeEV004_0", 49, 29, direction=4) from _call_GladeEV004_0_TransferPlayer_2
            $ erase_picture(1)
            $ erase_picture(2)
            $ erase_picture(3)
            $ erase_picture(4)
            $ fade_in()
            call Movement("GladeEV004_0", "player", ["L","L"]) from _call_GladeEV004_0_Movement_4
            $ resolve_scene()
            call PauseForBalloon("GladeEV004_0") from _call_GladeEV004_0_PauseForBalloon_6
            Leyna "Wow... Those two years training kyokushin karate have done me some good"
            $ hiding_place = 3
        elif menu_choice == _("Surrender! "):
            $ menu_choice = None
            Leyna "Ple-please do whatever you want, but don't hurt me"
            $ show_picture(3, "revenge4")
            $ resolve_scene()
            Prisoner "You stay still and let me do my job. Let's see those tits!"
            "Prisioner: Wow! You have the biggest, most perfect tits I've ever seen!"
            Prisoner "you couldn't expect anything to happen to you, walking around in these clothes, could you? what a bitch you are!"
            Leyna "Please... don't do it"
            $ show_picture(4, "revenge5")
            $ resolve_scene()
            Prisoner "Shut up, let me touch them...incredible, you have an incredible body and now it's mine, I'm going to enjoy it to the fullest"
            Leyna "!!!"
            Prisoner "Wow your nipples are getting hard! You're such a bitch, you say no, but your body is telling me yes!"
            Leyna "I--I.."
            $ show_picture(5, "revenge6")
            $ resolve_scene()
            Prisoner "And these panties you're wearing? who are they for? They barely cover anything!"
            Leyna "....!!!"
            Prisoner "Turn around!"
            Leyna "No, wait!"
            $ show_picture(6, "revenge7")
            $ resolve_scene()
            Prisoner "It couldn't be any other way! the perfect ass! and... I can't believe it, you're soaking wet down there!"
            Prisoner "Well I'm going to help you! I'm going to fuck you right here and right now you slut!"
            Leyna "!!!"
            Leyna "W-wait a second please!"
            Prisoner "No way, I can't wait a second to fuck a goddess like you"
            Leyna "(A-a goddess?.... why do I like this man talking to me like this? Why I'm enjoying this?)"
            $ show_picture(7, "revenge8")
            $ resolve_scene()
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
            call PlaySound("music", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_GladeEV004_0_PlaySound_6
            $ play_video_looped(1, "revenge_webm", "revenge.webm",width=1920,height=1080)
            $ resolve_scene()
            pause
            Leyna "HARDER! HARDER! FUCK MEEEE!!"
            Prisoner "Oh! I'm going to cum! I'm going to cum!"
            Leyna "Wait!!!! Not inside please!"
            stop music fadeout 1
            $ flash_screen([255,255,255,170], 60, True)
            $ show_picture(8, "revenge9")
            call PlaySound("sound", "audio/Poison.ogg", volume=0.9, no_loop=True) from _call_GladeEV004_0_PlaySound_7
            $ resolve_scene()
            $ flash_screen([255,255,255,170], 60, True)
            Prisoner "OOOhhhhhh.... nice, it's been years since I've fucked.. and never with a goddess like you"
            Leyna "This... this shouldn't have happened"
            Prisoner "I'm sure you've never been fucked like this before, not even by your limp dick of a husband! ... if you have one"
            $ show_picture(9, "revenge10")
            $ resolve_scene()
            Leyna "Shut up... leave me alone, get out of here please!"
            Prisoner "Tch! As you wish... if you ever want to come again, I'll be in town"
            Leyna "...."
            $ hiding_place = 4
            call GalleryViewed("revenge") from _call_GladeEV004_0_GalleryViewed_1
            $ fade_out()
            call TransferPlayer("TownFestivalNight", "GladeEV004_0", 49, 29, direction=4) from _call_GladeEV004_0_TransferPlayer_3
            $ erase_picture(1)
            $ erase_picture(2)
            $ erase_picture(3)
            $ erase_picture(4)
            $ erase_picture(5)
            $ erase_picture(6)
            $ erase_picture(7)
            $ erase_picture(8)
            $ erase_picture(9)
            $ fade_in()
            call Movement("GladeEV004_0", "player", ["L","L"]) from _call_GladeEV004_0_Movement_5
            $ resolve_scene()
            call PauseForBalloon("GladeEV004_0") from _call_GladeEV004_0_PauseForBalloon_7
            Leyna "How could this have happened... Since I got here, bad things have not stopped happening to me."
            Leyna "I don't recognize myself"
    $ resolve_scene()
    return False

label GladeImSureHeWontFindMeHereThisAreaIsALittleScaryAtNightThough(play_event = True, trigger = None): # autorun
    if is_erased("GladeImSureHeWontFindMeHereThisAreaIsALittleScaryAtNightThough"):
        return None
    elif hiding_place >= 4:
        return None
    elif hiding_place >= 3:
        return None
    elif trigger == "autorun" and hiding_place >= 1:
        call PlayEvent(play_event, "GladeImSureHeWontFindMeHereThisAreaIsALittleScaryAtNightThough_0", "GladeImSureHeWontFindMeHereThisAreaIsALittleScaryAtNightThough") from _call_GladeImSureHeWontFindMeHereThisAreaIsALittleScaryAtNightThough_0_PlayEvent
        return (0, "", "GladeImSureHeWontFindMeHereThisAreaIsALittleScaryAtNightThough_0")
    return None

label Gladecontinuacionfestival_0:
    $ tint_screen((0, 0, 0, 0), 60, True)
    call Movement("Gladecontinuacionfestival_0", "player", ["TURN_D",["WAIT",60],"TURN_L",["WAIT",60],"TURN_90D_R",["WAIT",60],"TURN_D",["WAIT",60]]) from _call_Gladecontinuacionfestival_0_Movement
    $ resolve_scene()
    call PauseForBalloon("Gladecontinuacionfestival_0") from _call_Gladecontinuacionfestival_0_PauseForBalloon
    Johan "My God... I feel like a truck has passed over my head"
    Johan "I don't think I've ever had such a hangover... what the hell happened last night?"
    $ flash_screen([255,255,255,170], 60, True)
    $ show_picture(1, "festivalnoche5", width=814, height=625)
    $ resolve_scene()
    pause
    $ erase_picture(1)
    $ resolve_scene()
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
    $ resolve_scene()
    pause
    $ erase_picture(1)
    $ resolve_scene()
    call PauseForBalloon("Gladecontinuacionfestival_0") from _call_Gladecontinuacionfestival_0_PauseForBalloon_1
    Johan "Le-leyna? ... that happened? but... I think it was another girl, wasn't it?... ahhh I can hardly remember it"
    Johan "Shit, I feel helpless..."
    Johan "Although I think something important happened later... that I should remember... it's all so confusing..."
    $ flash_screen([255,255,255,170], 60, True)
    $ show_picture(1, "festivalnoche28", width=814, height=625)
    $ resolve_scene()
    pause
    $ erase_picture(1)
    $ resolve_scene()
    Johan "!!! Tha-that didn't really happen, did it?"
    Johan "What the hell have you done Johan? What the hell was going through your head? Always thinking with your dick..."
    Johan "Shit, I have to find Leyna... I don't even know how I ended up here..."
    Johan "At least I have my clothes on and not those ridiculous festival clothes"
    $ set_self_switch("Glade","Gladecontinuacionfestival","A",True)
    return False

label Gladecontinuacionfestival(play_event = True, trigger = None): # autorun
    if is_erased("Gladecontinuacionfestival"):
        return None
    elif self_switch("Glade","Gladecontinuacionfestival","A"):
        return None
    elif trigger == "autorun" and switch("party_at_festival"):
        call PlayEvent(play_event, "Gladecontinuacionfestival_0", "Gladecontinuacionfestival") from _call_Gladecontinuacionfestival_0_PlayEvent
        return (0, "", "Gladecontinuacionfestival_0")
    return None

