label ApartmentGroundFloorBG:
    $ set_transparency_backgrounds(["bg_apartment","darkbg"])
    $ set_map_backgrounds(["map_apartment"])
    return

label ApartmentGroundFloorStart:
    call ApartmentGroundFloorBG from _call_ApartmentGroundFloorBG
    stop music
    stop bgs
    return

label ApartmentGroundFloorEnd:
    return

label ApartmentGroundFloortelevisionBase:
    "There's only trash on TV. I guess that's why we only watch Netflix "
    return False

label ApartmentGroundFloortelevision(play_event = True, trigger = None): # event
    if is_erased("ApartmentGroundFloortelevision"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "ApartmentGroundFloortelevisionBase", "ApartmentGroundFloortelevision") from _call_ApartmentGroundFloortelevision_PlayEvent
        return (1, "", "ApartmentGroundFloortelevision")
    return None

label ApartmentGroundFloorarmarioBase:
    "Hmmm. I need new clothes."
    return False

label ApartmentGroundFloorarmario(play_event = True, trigger = None): # event
    if is_erased("ApartmentGroundFloorarmario"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "ApartmentGroundFloorarmarioBase", "ApartmentGroundFloorarmario") from _call_ApartmentGroundFloorarmario_PlayEvent
        return (1, "", "ApartmentGroundFloorarmario")
    return None

label ApartmentGroundFloorlavaboBase:
    call PlaySound("sound", "audio/Liquid.ogg", volume=0.9, no_loop=True) from _call_ApartmentGroundFloorlavabo_PlaySound
    $ resolve_scene()
    return False

label ApartmentGroundFloorlavabo(play_event = True, trigger = None): # event
    if is_erased("ApartmentGroundFloorlavabo"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "ApartmentGroundFloorlavaboBase", "ApartmentGroundFloorlavabo") from _call_ApartmentGroundFloorlavabo_PlayEvent
        return (1, "", "ApartmentGroundFloorlavabo")
    return None

label ApartmentGroundFloorCbajaending2Base:
    call PauseForBalloon("ApartmentGroundFloorCbajaending2") from _call_ApartmentGroundFloorCbajaending2_PauseForBalloon
    Johan "Leyna! I have already received the money for the article!"
    call Movement("ApartmentGroundFloorCbajaending2", "ApartmentGroundFloorNPCMUJER", ["TURN_L","L","L","L","L","L"]) from _call_ApartmentGroundFloorCbajaending2_Movement
    $ resolve_scene()
    Leyna "Oh! at last! I was beginning to worry about whether we would make ends meet"
    Johan "hahahaha I guess you won't have to worry much anymore"
    Leyna "??? Why?"
    Johan "The article seems to be doing quite well"
    Leyna "Great"
    Johan "And..."
    Leyna "And...?"
    Johan "That has made a lot of people want to go to the village, it is seen that they have already booked hundreds of people for next year's festival"
    Johan "The magazine takes a percentage of the money from the bookings, they are making a lot of money thanks to me"
    Johan "So thanks to this... I HAVE BEEN PROMOTED!"
    Leyna "!!! WOW! congratulations honey!!!"
    Johan "Hehehehehe yeah... now we shouldn't have a hard time with the money"
    Leyna "I am so happy! finally something really good happens to us!"
    Leyna "This is great we have to celebrate! John and his girlfriend were coming to visit us will visit us in a few days"
    Leyna "We can hang out with them and celebrate the good news!"
    $ show_picture(1, "ending1")
    $ resolve_scene()
    Johan "Oh... So John is coming to visit us?"
    Johan "(I never liked that guy... I know he's Leyna's friend since high school... but I can't stand him)"
    Leyna "What's wrong?"
    $ show_picture(2, "ending2")
    $ resolve_scene()
    Johan "Oh... no, it's all right... Let's have a good time with them, we'll have a drink at the pub"
    Leyna "Yeah!"
    $ show_picture(3, "ending3")
    $ resolve_scene()
    Johan "....."
    $ fade_out()
    $ show_picture(4, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ fade_in()
    $ resolve_scene()
    "A few days later..."
    call PlaySound("music", "audio/Stay with me .ogg", volume=0.9, no_loop=False) from _call_ApartmentGroundFloorCbajaending2_PlaySound
    $ show_picture(5, "cbajacont1")
    $ resolve_scene()
    TV "Crime continues to multiply in Red Beach As we wonder why authorities continue to do nothing"
    Johan "The country is going to shit..."
    $ show_picture(6, "cbajacont2")
    $ resolve_scene()
    Leyna "Johan! already dressed?"
    Johan "Yes, you're still in your pajamas? you should get ready, aren't we meeting your friends for dinner?"
    Leyna "Well... it's still a little early, and John has never been very punctual"
    $ show_picture(7, "cbajacont3")
    $ resolve_scene()
    Leyna "Also... I thought you might want to... uhem... have a good time hehehe"
    Johan "A good time?... hmmm sounds good hehehe, why don't you come a little closer and explain me how we are going to have a good time?"
    Leyna "Hehehe Yeah..."
    $ show_picture(8, "cbajacont4")
    call PlaySound("sound", "audio/Bell3.ogg", volume=0.9, no_loop=True) from _call_ApartmentGroundFloorCbajaending2_PlaySound_1
    $ resolve_scene()
    Leyna "!!!! Who could it be?"
    Johan "I don't know... but he came at the worst time"
    $ show_picture(9, "cbajacont5")
    call PlaySound("sound", "audio/Door1.ogg", volume=0.9, no_loop=True) from _call_ApartmentGroundFloorCbajaending2_PlaySound_2
    $ resolve_scene()
    Johan "Oh! Hi guys! we didn't expect you so soon!"
    Leyna "!!!!"
    $ show_picture(10, "cbajacont6")
    $ resolve_scene()
    John "Hello Johan, how is everything going?"
    Laura "Hello Johan!"
    $ show_picture(11, "cbajacont7")
    $ resolve_scene()
    Leyna "Jhon!!!"
    Johan "!!!"
    pause
    $ show_picture(12, "cbajacont8")
    $ resolve_scene()
    John "OH! wow Leyna! nice to see you too"
    Laura "..."
    pause
    $ show_picture(13, "cbajacont9")
    $ resolve_scene()
    Leyna "How long has it been since we've seen each other? oh my! I was looking forward to having a drink with you and catching up! you look so handsome!"
    John "Yes, I was looking forward to it too... and you look beautiful too, Leyna"
    Leyna "Oh! shut up! you're going to make me blush!"
    Johan "( He hasn't even been here five minutes and they are already flirting )"
    $ show_picture(14, "cbajacont10")
    $ resolve_scene()
    John "By the way, you are getting in great shape! Are you training?"
    Leyna "Oh ... hehehehe no big deal, I go to the gym a couple of days a week"
    Johan "(Take your hand off her, jerk...)"
    pause
    $ show_picture(15, "cbajacont11")
    $ resolve_scene()
    Leyna "Well... and where are we going to have dinner? you always know some interesting place..."
    John "Oh I've booked a place you'll like..."
    Leyna "I'm sure..."
    Johan "!!! (Her tits!) EHEM! Leyna..."
    Leyna "Hmm?"
    Leyna "Oh!"
    pause
    $ show_picture(16, "cbajacont12")
    $ resolve_scene()
    Leyna "OH! S-sorry I didn't realize that.... I'll be right back"
    John "Hahahaha Don't worry Leyna!"
    Laura "...."
    pause
    $ show_picture(17, "cbajacont13")
    label ApartmentGroundFloorCbajaending2_loop_1:
        if True:
            jump ApartmentGroundFloorCbajaending2_loop_1_end
        jump ApartmentGroundFloorCbajaending2_loop_1
    label ApartmentGroundFloorCbajaending2_loop_1_end:
        pass
    $ resolve_scene()
    Johan "(Fuck... what a long night awaits me...)"
    "And so Leyna and Johan overcame a great test for their marriage... and lived happily ever after... or did they?"
    call GalleryViewed("cbajacont") from _call_ApartmentGroundFloorCbajaending2_GalleryViewed
    "It seems that Johan still has a couple of tests ahead of him in order to stay happily married to Leyna... "
    "That childhood friend of Leyna's seems to be on the prowl and in the city there are too many temptations to count!"
    "But that's a story for another time"
    "Anyway... the important thing is that right now the two of them are together and happy! "
    "Well... we have reached this point, the end of this little story, I hope you enjoyed it, although this is not the end of Bawdy Traditions"
    # "I will keep updating the game to improve it and expand the story a little more"
    "So we will see you soon and don't forget that this is not the end of Johan and Leyna's story"
    "Until then... see you soon in Bawdy Traditions 2"
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
    $ erase_picture(12)
    $ erase_picture(13)
    $ erase_picture(14)
    $ erase_picture(15)
    $ erase_picture(11)
    $ erase_picture(16)
    $ erase_picture(17)
    stop music fadeout 1
    stop bgs fadeout 1
    $ play_video_looped(1, "creditosdavid_webm", "CREDITOSDAVID.webm")
    $ fade_in()
    $ resolve_scene()
    pause
    pause
    $ stop_video(1)
    call ReturnToTitleScreen("ApartmentGroundFloorCbajaending2") from _call_ApartmentGroundFloorCbajaending2_ReturnToTitleScreen
    $ resolve_scene()
    return False

label ApartmentGroundFloorCbajaending2(play_event = True, trigger = None): # autorun
    if is_erased("ApartmentGroundFloorCbajaending2"):
        return None
    elif trigger == "autorun" and switch("corruption_low") and switch("festival_final"):
        call PlayEvent(play_event, "ApartmentGroundFloorCbajaending2Base", "ApartmentGroundFloorCbajaending2") from _call_ApartmentGroundFloorCbajaending2_PlayEvent
        return (0, "", "ApartmentGroundFloorCbajaending2")
    return None

