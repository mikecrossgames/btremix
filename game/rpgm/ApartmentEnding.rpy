label ApartmentEndingBG:
    $ set_transparency_backgrounds(["bg_apartment","darkbg"])
    $ set_map_backgrounds(["map_apartment"])
    return

label ApartmentEndingStart:
    call ApartmentEndingBG from _call_ApartmentEndingBG
    stop music
    stop bgs
    return

label ApartmentEndingEnd:
    return

label ApartmentEndingCbajaending2Base:
    call PauseForBalloon("ApartmentEndingCbajaending2") from _call_ApartmentEndingCbajaending2_PauseForBalloon
    $ show_picture(1, "ending18")
    $ resolve_scene()
    Johan "S-shit..."
    Johan "Certainly my life has ended up going totally to shit...."
    Johan "But hey, what did I expect? I couldn't be late to the newsroom every day and expect not to get fired hehehehe"
    $ show_picture(2, "ending19")
    $ resolve_scene()
    Johan "I-I guess I just like beer too much... too much..."
    $ show_picture(3, "ending20")
    $ resolve_scene()
    Johan "I wonder... I wonder how it's going to work out for... her"
    Johan "Shit I'm pathetic... even after everything I can't help but think about her Hahahahaha my god"
    pause
    $ fade_out()
    $ show_picture(4, "ending29")
    $ fade_in()
    $ resolve_scene()
    "That same night at the bar..."
    Johan "Ahh... this beer is perfect"
    Unknown "Pour me a white martini, please"
    Barman "Miss"
    $ show_picture(5, "ending30")
    $ resolve_scene()
    Johan "???"
    Johan "(Wow what a woman... what a great body!)"
    Johan "!!! (shit I can't believe it)"
    $ show_picture(6, "ending31")
    $ resolve_scene()
    Leyna "Johan?"
    if johan_leyna_sex == 2:
        label ApartmentEndingCbajaending2_loop_1:
            if True:
                jump ApartmentEndingCbajaending2_loop_1_end
            jump ApartmentEndingCbajaending2_loop_1
        label ApartmentEndingCbajaending2_loop_1_end:
            pass
        $ resolve_scene()
        Johan "Leyna... I had mistaken you for a model"
        $ show_picture(7, "ending32")
        $ resolve_scene()
        Leyna "hahahahaha... How are you doing?"
        Johan "Well... I'm fine, I'm still in the magazine"
        $ show_picture(8, "ending33")
        $ resolve_scene()
        Leyna "I see... I'm... I'm fine too"
        Johan "I'm glad, you look as beautiful as ever"
        $ show_picture(9, "ending34")
        $ resolve_scene()
        Leyna "Hahahaha I guess so... hey... do you think we could..."
        Johan "meet some day?"
        Leyna "!!!... Y-yeah... you know, just to catch up and stuff..."
        Johan ".... Yeah, I guess we could meet up sometime... to catch up and stuff"
        Leyna "... Great"
        $ fade_out()
        $ show_picture(10, "calta1cont1")
        $ fade_in()
        $ resolve_scene()
        Leyna "Well... I'm here"
        Johan "I'll be finished in a minute beautiful... Wow!"
        $ show_picture(11, "calta1cont2")
        $ resolve_scene()
        Johan "My God, you look beautiful!"
        Leyna "Hahahahaha well... I guess the occasion deserves it"
        Johan "Wow... now I feel bad for not keeping up with you, I'm a mess"
        Leyna "Hahahaha don't worry... for me you're going perfectly well"
        Johan "... (Fuck... shit I'm still completely in love with her)"
        Johan "W-well, I don't want to keep you waiting any longer, let's go to dinner!"
        Leyna "Yeah..."
        $ show_picture(12, "calta1cont3")
        $ resolve_scene()
        "That same night, a little later"
        Leyna "It was a beautiful date Johan"
        Johan "Yes... I've always wanted to go to that restaurant with you"
        Leyna "!!! I... I see"
        Johan "H-hey do you think you could..."
        $ show_picture(13, "calta1cont4")
        $ resolve_scene()
        Leyna "Come up home with you..."
        Johan "...."
        Leyna "I think... I think I could... Johan... let's go home together... maybe we could have one more drink together..."
        Johan "Yes... I think it's a good idea..."
        Johan "(Fuck my heart is going a mile a minute... I feel like a teenager on his first date)"
        $ fade_out()
        $ show_picture(14, "calta1cont5")
        $ fade_in()
        $ resolve_scene()
        Leyna "Hahaha gosh, the apartment is exactly the same"
        Johan "hahaha yes... why change something that is perfect?"
        Leyna "Yes... you are right"
        pause
        $ show_picture(15, "calta1cont6")
        $ resolve_scene()
        Leyna "Johan... you are far away... why don't you come closer? i want to tell you something..."
        Johan "Glup... Yeah..."
        Leyna "hehehehe..."
        $ fade_out()
        $ show_picture(16, "calta1cont7")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_ApartmentEndingCbajaending2_PlaySound
        $ fade_in()
        $ resolve_scene()
        Leyna "Ah ah ah god! fuck me! fuck me!"
        Johan "Ah ah ah Yes! Fuck!"
        Leyna "Fuuuck!!"
        pause
        $ show_picture(17, "calta1cont8")
        $ resolve_scene()
        Leyna "My God! I'm going to cum"
        Johan "No! not yet... I'm not done yet!"
        Leyna "!!! Ahhh (fuck... when did he get so good at fucking? ... god)"
        Johan "Ah ah ah ah!"
        pause
        $ show_picture(18, "calta1cont9")
        $ resolve_scene()
        Leyna "S-shit! .... I'm cumming! I'm cumming!"
        Johan "!!! F-fuck! ah ah ah, jesus!"
        pause
        call PlaySound("music", "audio/Stay with me .ogg", volume=0.9, no_loop=False) from _call_ApartmentEndingCbajaending2_PlaySound_1
        "It seems that Leyna and Johan have not yet forgotten about their relationship"
        call GalleryViewed("calta2") from _call_ApartmentEndingCbajaending2_GalleryViewed
        "Johan even seems to want to give Leyna another chance! I wonder if it will work? I guess time will tell..."
        "I think it is an opportunity to redirect his life and be happy again... but what do I know? "
        "What seems certain is that they will meet again and maybe they will start over, from scratch... maybe this is the opportunity they needed to improve their relationship "
        "Although things have to change for both of them to end up happy, Johan has to put a little more effort into the relationship and Leyna.... Well, Leyna has to learn to control herself a little bit more"
        "but I am sure they will learn from their mistakes and will be able to bring this relationship to a successful conclusion"
        "Let's hope they do well in their lives "
        "Well... we have reached this point, the end of this little story, I hope you enjoyed it, although this is not the end of Bawdy Traditions"
        # "I will keep updating the game to improve it and expand the story a little more"
        "So we will see you soon and don't forget that this is not the end of Johan and Leyna's story, you will see them in Bawdy Traditions 2"
        "See you soon! "
        $ fade_out()
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
        stop music fadeout 1
        stop bgs fadeout 1
        $ play_video_looped(1, "creditosdavid_webm", "CREDITOSDAVID.webm")
        $ fade_in()
        $ resolve_scene()
        pause
        pause
        $ stop_video(1)
        call ReturnToTitleScreen("ApartmentEndingCbajaending2") from _call_ApartmentEndingCbajaending2_ReturnToTitleScreen
    if johan_leyna_sex == 1:
        label ApartmentEndingCbajaending2_loop_2:
            if True:
                jump ApartmentEndingCbajaending2_loop_2_end
            jump ApartmentEndingCbajaending2_loop_2
        label ApartmentEndingCbajaending2_loop_2_end:
            pass
        $ show_picture(7, "ending35")
        $ resolve_scene()
        Johan "L-leyna..."
        Johan "(I can't believe it... after all this time and he shows up in this fucking place...)"
        Johan "(God... she looks beautiful...)"
        Johan "(Shit shit shit shit)"
        Johan "H-hey..."
        Leyna "... Johan? what are you doing here?"
        $ show_picture(8, "ending36")
        $ resolve_scene()
        Johan "W-well... I was just having a drink... you know to take the stress off and stuff hehehehehe...."
        Leyna "Oh... I see, how are you doing?"
        Johan "Well I guess... and you?"
        Leyna "Good good..."
        $ show_picture(9, "ending37")
        $ resolve_scene()
        Unknown "Honey..."
        Leyna "Oh! Yeah?"
        Johan "!!! (honey? that's his new ?.... shit)"
        Unknown "The guys have already called me, they are in the bar next door, let's get out of here"
        Leyna "Of course... Well Johan... I'm glad you're well"
        Johan "Y-yeah..."
        $ show_picture(10, "ending38")
        $ resolve_scene()
        Johan "... (This seems like a nightmare... how the hell did we end up like this?)"
        $ fade_out()
        $ show_picture(11, "calta2cont4")
        $ fade_in()
        $ resolve_scene()
        "Days later..."
        Johan "Aaah... finally at home... what a shitty day"
        Johan "W-well... What the hell... I'm going to jerk off..."
        Johan "Let's see... pornhut... most viewed videos"
        $ show_picture(12, "calta2cont5")
        $ resolve_scene()
        Johan "AH!!"
        Johan "I-It can't be... it has to be my fucking imagination"
        Johan "this can't be real..."
        "CLICK"
        $ show_picture(13, "calta2cont1")
        $ resolve_scene()
        Unknown "Hi guys, here we have a new girl who wants to try a new experience... Hi honey, what's your name?"
        Leyna "Hi guys! My name is Leyna hahahaha"
        Unknown "Wow Leyna eh? what a beautiful name, you are a real beauty Leyna, I don't think we have ever had a girl like you in the studio"
        Unknown "You look like a model!"
        Leyna "hahahaha Thank you very much!"
        Unknown "And tell me Leyna... to what have you come?"
        Leyna "Well... I came to fuck two big black cocks"
        Unknown "WOw! straight to the point eh? very well then let's not wait any longer, come on guys don't make her wait!"
        pause
        $ show_picture(14, "calta2cont6")
        $ resolve_scene()
        Johan "!!! No..."
        Leyna "Ah ah ah my god you are driving me crazy!"
        Unknown "do you like it bitch?! we will fuck you until you can't stand up bitch!"
        Leyna "Yes Please!"
        $ show_picture(15, "calta2cont2")
        $ resolve_scene()
        Leyna "Oh my god! Ah ah ah"
        Unknown "fuck this bitch is crazy! look how she moans!"
        Unknown "Ahhahahaha! You've never been fucked like that, have you, slut?"
        Leyna "Ah ah ah! No!Never! Fuck me harder! Harder!"
        Unknown "Fuck this bitch is insatiable!"
        Johan "... god... why? why can't I help it?... shit... screw this..."
        pause
        $ show_picture(16, "calta2cont7")
        $ resolve_scene()
        Johan "Ah ah ah..."
        Leyna "OOoohhh Oh my god! fuuuck!!"
        Unknown "Keep it up! Fuck this whore! Show her how it's done!"
        Johan "Fuck..."
        $ show_picture(17, "calta2cont3")
        $ resolve_scene()
        Leyna "God! God! I'm cumming! I'm cumming!!!!"
        Unknown "Cum as much as you want! We will keep fucking you until we're fed up!"
        Leyna "Yes! please! Aaaaahh!!!"
        Unknown "Fuck! I want this crazy bitch in the studio every week!"
        Leyna "Do you like it? do you like my pussy? Ah ah ah ah!!!"
        Unknown "Shit!"
        Johan "Aaaahh..."
        pause
        $ show_picture(18, "calta2cont8")
        $ resolve_scene()
        Johan "S-shit... I've cum"
        Johan "I cum watching them do this to my ex-wife"
        Johan "Ah... God I'm such a shitty person... hahaha... I couldn't have fallen any lower...."
        call PlaySound("music", "audio/Stay with me .ogg", volume=0.9, no_loop=False) from _call_ApartmentEndingCbajaending2_PlaySound_2
        "it seems that things are not working out well for Johan, and at this rate he looks like he is going to fall headlong into alcoholism"
        call GalleryViewed("calta1") from _call_ApartmentEndingCbajaending2_GalleryViewed_1
        "Although there is still time to get his life back on track"
        "on the other hand Leyna seems to be very happy with her new life..."
        "I suppose that the photographs taken of her in the village opened up a new market for her to work in..."
        "What seems certain is that the two will never meet again in their lives... although there are times when that is the best thing to do... isn't it? "
        "Perhaps if Johan had put more effort into his relationship and not taken things for granted, things would have worked out better for him"
        "At the end of the day, the devil is in the details... or so they say"
        "Well... we have reached this point, the end of this little story, I hope you enjoyed it, although this is not the end of Bawdy Traditions"
        # "I will keep updating the game to improve it and expand the story a little more"
        "So we will see you soon and don't forget that this is not the end of Johan and Leyna's story, you will see them in Bawdy Traditions 2"
        "See you soon! "
        $ fade_out()
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
        stop music fadeout 1
        stop bgs fadeout 1
        $ play_video_looped(1, "creditosdavid_webm", "CREDITOSDAVID.webm")
        $ fade_in()
        $ resolve_scene()
        pause
        pause
        $ stop_video(1)
        call ReturnToTitleScreen("ApartmentEndingCbajaending2") from _call_ApartmentEndingCbajaending2_ReturnToTitleScreen_1
    call ReturnToTitleScreen("ApartmentEndingCbajaending2") from _call_ApartmentEndingCbajaending2_ReturnToTitleScreen_2
    $ resolve_scene()
    return False

label ApartmentEndingCbajaending2(play_event = True, trigger = None): # autorun
    if is_erased("ApartmentEndingCbajaending2"):
        return None
    elif trigger == "autorun" and switch("corruption_high") and switch("festival_final"):
        call PlayEvent(play_event, "ApartmentEndingCbajaending2Base", "ApartmentEndingCbajaending2") from _call_ApartmentEndingCbajaending2_PlayEvent
        return (0, "", "ApartmentEndingCbajaending2")
    return None

label ApartmentEndingORDENADORBase:
    "You have a new message !"
    $ resolve_scene()
    Johan "oh this is perfect!"
    call Movement("ApartmentEndingORDENADOR", "ApartmentEndingCbajaending2", ["L","L","L","L","L"]) from _call_ApartmentEndingORDENADOR_Movement
    $ resolve_scene()
    Leyna "What is it?"
    Johan "Honey, I think this is a good idea for the article."
    $ show_transparent(1, "expresion_neutral_mujer", width=1600, height=900)
    $ resolve_scene()
    "It's a small town lost in the mountains, very traditional, with ancient festivities that take place in the summer"
    "We could go and make an article about it."
    $ erase_picture(1)
    $ show_transparent(2, "expresion_ilusion_mujer", width=1600, height=900)
    $ resolve_scene()
    Leyna "Great! We could enjoy and relax a little, it's been a long time since we took a vacation."
    $ erase_picture(2)
    call Movement("ApartmentEndingORDENADOR", "player", ["TURN_R"]) from _call_ApartmentEndingORDENADOR_Movement_1
    $ resolve_scene()
    Johan "Yeah, they have hot springs, a beautiful river and they all seem very rustic and friendly"
    "We'll have a great time while we work"
    $ resolve_scene()
    Leyna "It seems that the food is great, country food, I can't wait"
    Johan "Well then, it's decided! Pack your bags while I book a room in the village hostel."
    call Movement("ApartmentEndingORDENADOR", "player", ["TURN_U"]) from _call_ApartmentEndingORDENADOR_Movement_2
    call Movement("ApartmentEndingORDENADOR", "ApartmentEndingCbajaending2", ["D","D","D","D","D","L","L","L","L","L","L","L","U","U","U","U","U"]) from _call_ApartmentEndingORDENADOR_Movement_3
    stop music fadeout 1
    $ set_switch("introduction", False)
    call TransferPlayer("TownEntrance", "ApartmentEndingORDENADOR", 3, 5, direction=2) from _call_ApartmentEndingORDENADOR_TransferPlayer
    $ resolve_scene()
    return False

label ApartmentEndingORDENADOR(play_event = True, trigger = None): # event
    if is_erased("ApartmentEndingORDENADOR"):
        return None
    elif trigger == "event" and switch("introduction"):
        call PlayEvent(play_event, "ApartmentEndingORDENADORBase", "ApartmentEndingORDENADOR") from _call_ApartmentEndingORDENADOR_PlayEvent
        return (1, "", "ApartmentEndingORDENADOR")
    return None

label ApartmentEndingtelevisionBase:
    "There's only trash on TV. I guess that's why we only watch Netflix "
    return False

label ApartmentEndingtelevision(play_event = True, trigger = None): # event
    if is_erased("ApartmentEndingtelevision"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "ApartmentEndingtelevisionBase", "ApartmentEndingtelevision") from _call_ApartmentEndingtelevision_PlayEvent
        return (1, "", "ApartmentEndingtelevision")
    return None

label ApartmentEndingarmarioBase:
    "Hmmm. I need new clothes."
    return False

label ApartmentEndingarmario(play_event = True, trigger = None): # event
    if is_erased("ApartmentEndingarmario"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "ApartmentEndingarmarioBase", "ApartmentEndingarmario") from _call_ApartmentEndingarmario_PlayEvent
        return (1, "", "ApartmentEndingarmario")
    return None

label ApartmentEndinglavaboBase:
    call PlaySound("sound", "audio/Liquid.ogg", volume=0.9, no_loop=True) from _call_ApartmentEndinglavabo_PlaySound
    $ resolve_scene()
    return False

label ApartmentEndinglavabo(play_event = True, trigger = None): # event
    if is_erased("ApartmentEndinglavabo"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "ApartmentEndinglavaboBase", "ApartmentEndinglavabo") from _call_ApartmentEndinglavabo_PlayEvent
        return (1, "", "ApartmentEndinglavabo")
    return None

label ApartmentEndingpuerta_0:
    "Wait. I have to talk to my wife"
    call Movement("ApartmentEndingpuerta_0", "player", ["TURN_U","U"]) from _call_ApartmentEndingpuerta_0_Movement
    $ resolve_scene()
    return False

label ApartmentEndingpuerta_1:
    " Wait. I have to look the new mail"
    call Movement("ApartmentEndingpuerta_1", "player", ["TURN_U","U"]) from _call_ApartmentEndingpuerta_1_Movement
    $ resolve_scene()
    return False

label ApartmentEndingpuerta(play_event = True, trigger = None): # event
    if is_erased("ApartmentEndingpuerta"):
        return None
    elif trigger == "event" and switch("introduction"):
        call PlayEvent(play_event, "ApartmentEndingpuerta_1", "ApartmentEndingpuerta") from _call_ApartmentEndingpuerta_1_PlayEvent
        return (0, "", "ApartmentEndingpuerta_1")
    elif trigger == "event":
        call PlayEvent(play_event, "ApartmentEndingpuerta_0", "ApartmentEndingpuerta") from _call_ApartmentEndingpuerta_0_PlayEvent
        return (0, "", "ApartmentEndingpuerta_0")
    return None

label ApartmentEndingCbajaending2_v2Base:
    call PauseForBalloon("ApartmentEndingCbajaending2_v2") from _call_ApartmentEndingCbajaending2_v2_PauseForBalloon
    $ show_picture(1, "ending18")
    $ resolve_scene()
    Johan "S-shit..."
    Johan "Certainly my life has ended up going totally to shit...."
    Johan "But well, what did I expect? I couldn't be late to the newsroom every day and expect not to get fired hehehehe"
    $ show_picture(2, "ending19")
    $ resolve_scene()
    Johan "I-I guess I like beer too much... too much..."
    Johan "I hope they call me from the bar tonight to go to work... if not .... I'm screwed"
    $ show_picture(3, "ending20")
    $ resolve_scene()
    Johan "I wonder... I wonder how she's doing?"
    Johan "Shit I'm pathetic... even after everything I can't help but think about her Hahahahaha my god..."
    pause
    $ fade_out()
    $ show_picture(4, "ending21")
    $ fade_in()
    $ resolve_scene()
    "That same night at the bar..."
    "Johan. (Fuck I'm exhausted... I can't wait for the shift to end and go to sleep, and on top of that there are no customers, I'm bored out of my mind)"
    call PlaySound("sound", "audio/Door1.ogg", volume=0.9, no_loop=True) from _call_ApartmentEndingCbajaending2_v2_PlaySound
    Johan "Oh (finally someone arrives...)"
    $ show_picture(5, "ending22")
    $ resolve_scene()
    Johan "!!!! (F-fuck... no shit... Fuck me...)"
    Johan "(I can't believe it... after all this time and she shows up in this fucking place? I-I don't want him to see me working here)"
    Johan "(God... she looks beautiful...)"
    $ show_picture(6, "ending23")
    $ resolve_scene()
    Johan "(I'm going to turn around before she sees me)"
    Leyna "Excuse me..."
    Johan "(Shit shit shit)"
    Leyna "Do you hear me? excuse me!"
    $ show_picture(7, "ending24")
    $ resolve_scene()
    Johan "H-hey..."
    Leyna "... Johan? what are you doing here?"
    Johan "W-well... I work here now"
    $ show_picture(8, "ending25")
    $ resolve_scene()
    Leyna "Oh... I see, how are you doing?"
    Johan "Well I guess... and you?"
    Leyna "Good good..."
    $ show_picture(9, "ending26")
    $ resolve_scene()
    Unknown "Honey..."
    Leyna "Oh! Yeah?"
    Johan "!!! (honey? that's his new ?.... shit)"
    Unknown "The guys have already called me, they are in the bar next door, let's get out of here"
    $ show_picture(10, "ending27")
    $ resolve_scene()
    Leyna "Of course... Well Johan... I'm glad you're well"
    Johan "Y-yes..."
    $ show_picture(11, "ending28")
    $ resolve_scene()
    Johan "... (This seems like a nightmare... how the hell did we end up like this?)"
    Unknown "Waiter! Hey waiter! Another beer over here!"
    Johan "!!! Shit..."
    $ fade_out()
    $ show_picture(12, "cmedia4cont1")
    $ fade_in()
    label ApartmentEndingCbajaending2_v2_loop_1:
        if True:
            jump ApartmentEndingCbajaending2_v2_loop_1_end
        jump ApartmentEndingCbajaending2_v2_loop_1
    label ApartmentEndingCbajaending2_v2_loop_1_end:
        pass
    $ resolve_scene()
    "Days later... "
    Johan "Shit, when I was on my way to work I couldn't believe my eyes..."
    Johan "But it's true... Fuck..."
    $ show_picture(13, "cmedia4cont3")
    $ resolve_scene()
    "\"The new star of the lingerie catwalks allows us to interview her exclusively (...)\""
    "\"Leyna: Yes... I had an interesting... experience a few months ago and I said to myself why not? so I started in this career.\""
    "\"Interviewer: Wow, and if it's not too much of an indiscretion, can I ask you about your love life Leyna? Any boyfriends?\""
    "\"Leyna: Hahahaha well... I recently started a relationship.... but I guess you'll know all the details soon enough hahahahaha\"."
    $ show_picture(14, "cmedia4cont2")
    $ resolve_scene()
    Johan "Shit ... shit.... shit...."
    Johan "What have I done?... fuck..."
    call PlaySound("music", "audio/Stay with me .ogg", volume=0.9, no_loop=False) from _call_ApartmentEndingCbajaending2_v2_PlaySound_1
    "Johan does not seem to be doing very well, he does not seem very happy in his new job and everything seems to indicate that he is going to fall headlong into alcoholism"
    "Leyna, on the other hand, seems happy with her new life as a lingerie model"
    "Let's hope that Johan can redirect his life and rededicate himself to something he likes... there's still time... there's always time"
    "What seems certain is that the two will never meet again in their lives... although there are times when that is the best thing to do... isn't it? "
    "It seems that Johan has not been able to maintain his relationship with the person he loved, he became too trusting and neglected his relationship to the point where it ended forever"
    "Sometimes when we take something for granted and believe that we have already achieved it, we tend to neglect it, causing us to lose it in the end"
    "This is the end of this little story, although you may want to try again and get a happier ending for both of them"
    "Although that's your decision of course... for my part it has been a pleasure to live this little adventure with you, we will see each other soon... "
    "At the end of the day, there is still a lot to tell... "
    $ fade_out()
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
    stop music fadeout 1
    stop bgs fadeout 1
    $ play_video_looped(1, "creditosdavid_webm", "CREDITOSDAVID.webm")
    $ fade_in()
    $ resolve_scene()
    pause
    pause
    $ stop_video(1)
    call ReturnToTitleScreen("ApartmentEndingCbajaending2_v2") from _call_ApartmentEndingCbajaending2_v2_ReturnToTitleScreen
    $ resolve_scene()
    return False

label ApartmentEndingCbajaending2_v2(play_event = True, trigger = None): # autorun
    if is_erased("ApartmentEndingCbajaending2_v2"):
        return None
    elif trigger == "autorun" and switch("corruption_average") and switch("festival_final"):
        call PlayEvent(play_event, "ApartmentEndingCbajaending2_v2Base", "ApartmentEndingCbajaending2_v2") from _call_ApartmentEndingCbajaending2_v2_PlayEvent
        return (0, "", "ApartmentEndingCbajaending2_v2")
    return None

