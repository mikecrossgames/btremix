label River2BG:
    $ set_transparency_backgrounds(["bg_river","midbg"])
    $ set_map_backgrounds(["map_river"])
    return

label River2Start:
    call River2BG from _call_River2BG
    stop music
    stop bgs
    return

label River2End:
    return

label River2ThisPlaceIsBeautifulBase:
    call Movement("River2EVENTORIO2", "River2ALEXA", ["TURN_U"]) from _call_River2EVENTORIO2_Movement
    $ resolve_scene()
    call PauseForBalloon("River2EVENTORIO2") from _call_River2EVENTORIO2_PauseForBalloon
    Alexa "This place is beautiful!"
    call Movement("River2EVENTORIO2", "player", ["TURN_U"]) from _call_River2EVENTORIO2_Movement_1
    $ resolve_scene()
    call PauseForBalloon("River2EVENTORIO2") from _call_River2EVENTORIO2_PauseForBalloon_1
    Leyna "Yeah..."
    $ show_picture(1, "rio17")
    $ resolve_scene()
    Alexa "I feel sooo liberated, it's also a great day and we have the perfect temperature to take a bath"
    Leyna "Can we... enter the river now? I don't like being exposed in front of all these people"
    Alexa "Okay okay..."
    $ erase_picture(1)
    call Movement("River2EVENTORIO2", "River2HOMBREEVENTOIZQUIERDA", ["TURN_L"]) from _call_River2EVENTORIO2_Movement_2
    $ resolve_scene()
    $ resolve_scene()
    call PauseForBalloon("River2EVENTORIO2") from _call_River2EVENTORIO2_PauseForBalloon_2
    Villager "I can't believe my eyes... look at those women! Hey come on, let's go and talk to them"
    Villager2 "Dude I'm married..."
    Villager "Exactly YOU'RE married, fucking whenever you want... But for me? It's been years since I fuck a girl and those two are the sexier fucking girls I've ever seen"
    Villager2 "(Whenever I want?...) Tch... Okay man, but don't be a creep, take it easy"
    Villager "Yeah, relax I'm a dandy! Those two will be on her knees in a blink of an eye"
    Villager2 "(Yeah right... and the \"no fucking in years\"?)"
    call Movement("River2EVENTORIO2", "River2HOMBREEVENTOIZQUIERDA", ["L","L","L","L","D","L","L","L","U","TURN_R"]) from _call_River2EVENTORIO2_Movement_3
    call Movement("River2EVENTORIO2", "River2HOMBREEVENTODERECHA", ["L","L","L","L"]) from _call_River2EVENTORIO2_Movement_4
    $ resolve_scene()
    call PauseForBalloon("River2EVENTORIO2") from _call_River2EVENTORIO2_PauseForBalloon_3
    $ show_picture(2, "rio18")
    $ resolve_scene()
    Villager "Hello ladies... I see you two are alone, can we join?"
    Alexa "Oh?... I think you can, sure"
    Leyna "Alexa? I thought we were going to be alone and relax for a while"
    Alexa "Come on Leyna, it's an opportunity to meet new people and have a good time, you worry too much"
    Leyna "..."
    Alexa "Come on guys let's go to the river and take a bath"
    $ show_picture(3, "rio19")
    $ resolve_scene()
    Alexa "Well... Tell me guys, you work in this town?"
    Villager "Yeah we are from this town and have been working in the coal mine all of our lives"
    Alexa "Oh? I suppose that's why you two are so muscular"
    Leyna "(Is she flirting with them?... Now I see why her husband is so jealous)"
    $ show_picture(4, "rio20")
    $ resolve_scene()
    Villager2 "I-I'm sorry about this, my friend is... too socially active I suppose"
    Leyna "Don't worry, it's just... I don't feel too comfortable being naked around you.. I'm married after all"
    Villager2 "Yeah I'm married too, don't worry about me I don't wanna do anything to you, I'm here to make sure my friend doesn't make something crazy"
    Leyna "Hahahaha"
    Villager "See?... I told you"
    Alexa "Wow..."
    Leyna "???"
    $ show_picture(5, "rio21")
    $ resolve_scene()
    Alexa "You're quite big... and sure you're happy to see me..."
    Villager "Hehehe I couldn't help myself... it's so lonely in this town, you know? Not enough woman for all of us"
    Alexa "I can see that... yeah"
    Leyna "(What the hell are they talking about?)"
    Villager2 "Soo..."
    $ erase_picture(5)
    $ resolve_scene()
    Leyna "Yeah?"
    Villager2 "You two are here for the festival or...?"
    Leyna "Oh no, I came with my husband to make an article about the traditions of this place, and enjoy the local food"
    Villager2 "So you didn't come with this girl?"
    Leyna "Alexa? No, I meet her today, it seems to have some problems with her husband and we... you know... came here to relax"
    Villager2 "She's married?... (poor guy) Well if you need to know something for your article you can ask me anything"
    Leyna "Okay thank you"
    $ show_picture(5, "rio22")
    $ resolve_scene()
    Alexa "You're right, it can't fit in my mouth hehehe. Your cock is huge..."
    Villager "Hehehe I told you so..."
    Alexa "Sshhh... be quiet"
    $ fade_out()
    $ erase_picture(5)
    $ fade_in()
    $ resolve_scene()
    "(A FEW MOMENTS LATER...)"
    Leyna "Hahahaaha you're right!"
    Villager "Shit, I can't hold it anymore, come here!"
    Alexa "Hmmmm"
    Villager2 "Hahahaha and I... WOAH what the fuck?!"
    $ show_picture(6, "rio23")
    call PlaySound("music", "audio/Dungeon3.ogg", volume=0.9, no_loop=False) from _call_River2EVENTORIO2_PlaySound
    $ resolve_scene()
    Alexa "I don't know..."
    Leyna "WHAT?! (are you fucking serious?)"
    Villager2 "Shit, man... you're crazy"
    pause
    $ show_picture(7, "rio24_movimiento")
    call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_River2EVENTORIO2_PlaySound_1
    $ resolve_scene()
    Alexa "Oh Oh  OOOHH!! FUCK ME! HARDER!"
    Villager "YOU LIKE THIS?!! FUCK YES!!"
    Leyna "(I can't believe this... ''trying to save my marriage'' my ass)"
    $ show_picture(8, "rio25")
    stop bgs fadeout 1
    $ resolve_scene()
    Leyna "(But... seems to be enjoying it so much)"
    Leyna "(I'm getting wet seeing all this .. I have to get out of here... I just... I'll stay a little longer ... so that nothing bad happens to Alexa)"
    Villager2 "(This girl is in shock looking at her friend being fucked in public ... maybe this whole situation is exciting her?)"
    Villager2 "(Maybe if I... NO! I'm married... but man this girl is too sexy and with all this situation my cock is hard. If we do it ... I don't think my wife finds out)"
    pause
    $ show_picture(9, "rio26")
    $ resolve_scene()
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
    $ fade_out()
    $ erase_picture(2)
    $ erase_picture(3)
    $ erase_picture(4)
    $ erase_picture(6)
    $ erase_picture(7)
    $ erase_picture(8)
    $ erase_picture(9)
    $ set_switch("second_river", True)
    call GalleryViewed("rio2") from _call_River2EVENTORIO2_GalleryViewed
    call TransferPlayer("Town", "River2EVENTORIO2", 47, 23, direction=4) from _call_River2EVENTORIO2_TransferPlayer
    $ fade_in()
    $ show_transparent(1, "expresion_yuyu_mujer", width=1600, height=900)
    $ resolve_scene()
    Leyna "WTF did just happen?"
    "This girl is definitely a bad influence, I was wrong about what I did at the bar, but I was completely drunk"
    $ erase_picture(1)
    $ show_transparent(2, "plano_mujer_timida", width=1600, height=900)
    $ resolve_scene()
    "I would never do something like that to Johan"
    $ erase_picture(2)
    $ show_transparent(3, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    "Speaking of which, I should go to the Inn, it's late and he is probably waiting for me"
    $ erase_picture(3)
    $ resolve_scene()
    return False

label River2ThisPlaceIsBeautiful(play_event = True, trigger = None): # autorun
    if is_erased("River2ThisPlaceIsBeautiful"):
        return None
    elif trigger == "autorun":
        call PlayEvent(play_event, "River2ThisPlaceIsBeautifulBase", "River2ThisPlaceIsBeautiful") from _call_River2ThisPlaceIsBeautiful_PlayEvent
        return (0, "", "River2ThisPlaceIsBeautiful")
    return None

