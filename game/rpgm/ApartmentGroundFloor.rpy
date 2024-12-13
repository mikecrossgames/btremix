label ApartmentGroundFloorCbajaending2:
    pause 0.2
    Johan "Leyna! I have already received the money for the article!"
    pause 0.32
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
    Johan "Oh... So John is coming to visit us?"
    Johan "(I never liked that guy... I know he's Leyna's friend since high school... but I can't stand him)"
    Leyna "What's wrong?"
    $ show_picture(2, "ending2")
    Johan "Oh... no, it's all right... Let's have a good time with them, we'll have a drink at the pub"
    Leyna "Yeah!"
    $ show_picture(3, "ending3")
    Johan "....."
    scene black with dissolve
    $ show_picture(4, "pantallanegro", scale=(120, 120), width=816, height=600)
    hide black with dissolve
    "A few days later..."
    play music "audio/Stay with me .ogg" loop volume 0.9
    $ show_picture(5, "cbajacont1")
    TV "Crime continues to multiply in Red Beach As we wonder why authorities continue to do nothing"
    Johan "The country is going to shit..."
    $ show_picture(6, "cbajacont2")
    Leyna "Johan! already dressed?"
    Johan "Yes, you're still in your pajamas? you should get ready, aren't we meeting your friends for dinner?"
    Leyna "Well... it's still a little early, and John has never been very punctual"
    $ show_picture(7, "cbajacont3")
    Leyna "Also... I thought you might want to... uhem... have a good time hehehe"
    Johan "A good time?... hmmm sounds good hehehe, why don't you come a little closer and explain me how we are going to have a good time?"
    Leyna "Hehehe Yeah..."
    $ show_picture(8, "cbajacont4")
    play sound "audio/Bell3.ogg" volume 0.9 noloop
    Leyna "!!!! Who could it be?"
    Johan "I don't know... but he came at the worst time"
    $ show_picture(9, "cbajacont5")
    play sound "audio/Door1.ogg" volume 0.9 noloop
    Johan "Oh! Hi guys! we didn't expect you so soon!"
    Leyna "!!!!"
    $ show_picture(10, "cbajacont6")
    John "Hello Johan, how is everything going?"
    Laura "Hello Johan!"
    $ show_picture(11, "cbajacont7")
    Leyna "Jhon!!!"
    Johan "!!!"
    pause
    $ show_picture(12, "cbajacont8")
    John "OH! wow Leyna! nice to see you too"
    Laura "..."
    pause
    $ show_picture(13, "cbajacont9")
    Leyna "How long has it been since we've seen each other? oh my! I was looking forward to having a drink with you and catching up! you look so handsome!"
    John "Yes, I was looking forward to it too... and you look beautiful too, Leyna"
    Leyna "Oh! shut up! you're going to make me blush!"
    Johan "( He hasn't even been here five minutes and they are already flirting )"
    $ show_picture(14, "cbajacont10")
    John "By the way, you are getting in great shape! Are you training?"
    Leyna "Oh ... hehehehe no big deal, I go to the gym a couple of days a week"
    Johan "(Take your hand off her, jerk...)"
    pause
    $ show_picture(15, "cbajacont11")
    Leyna "Well... and where are we going to have dinner? you always know some interesting place..."
    John "Oh I've booked a place you'll like..."
    Leyna "I'm sure..."
    Johan "!!! (Her tits!) EHEM! Leyna..."
    Leyna "Hmm?"
    Leyna "Oh!"
    pause
    $ show_picture(16, "cbajacont12")
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
    Johan "(Fuck... what a long night awaits me...)"
    "And so Leyna and Johan overcame a great test for their marriage... and lived happily ever after... or did they?"
    "It seems that Johan still has a couple of tests ahead of him in order to stay happily married to Leyna..."
    "That childhood friend of Leyna's seems to be on the prowl and in the city there are too many temptations to count!"
    "But that's a story for another time"
    "Anyway... the important thing is that right now the two of them are together and happy!"
    "Well... we have reached this point, the end of this little story, I hope you enjoyed it, although this is not the end of Bawdy Traditions"
    # "I will keep updating the game to improve it and expand the story a little more"
    "So we will see you soon and don't forget that this is not the end of Johan and Leyna's story"
    "Until then... see you soon in Bawdy Traditions 2"
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
    $ erase_picture(12)
    $ erase_picture(13)
    $ erase_picture(14)
    $ erase_picture(15)
    $ erase_picture(11)
    $ erase_picture(16)
    $ erase_picture(17)
    stop music fadeout 1
    stop bgs fadeout 1
    $ play_video_looped(1, "creditosdavid", "CREDITOSDAVID")
    hide black with dissolve
    pause
    pause
    $ stop_video(1)
    call ReturnToTitleScreen("ApartmentGroundFloorCbajaending2") from _call_ApartmentGroundFloorCbajaending2_ReturnToTitleScreen
    return

