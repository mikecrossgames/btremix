label BarBG:
    $ set_transparency_backgrounds(["bg_bar"])
    $ set_map_backgrounds(["map_bar"])
    return

label BarStart:
    call BarBG from _call_BarBG
    stop music
    stop bgs
    return

label BarEnd:
    return

label BarToTownBase:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_BarEV001_PlaySound
    call TransferPlayer("Town", "BarEV001", 25, 46, direction=2) from _call_BarEV001_TransferPlayer
    $ resolve_scene()
    return False

label BarToTown(play_event = True, trigger = None): # event
    if is_erased("BarToTown"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "BarToTownBase", "BarToTown") from _call_BarToTown_PlayEvent
        return (0, "", "BarToTown")
    return None

label BarbarmanBase:
    Barman "Need anything?"
    return False

label Barbarman(play_event = True, trigger = None): # event
    if is_erased("Barbarman"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "BarbarmanBase", "Barbarman") from _call_Barbarman_PlayEvent
        return (1, "", "Barbarman")
    return None

label BarNPCMachineBase:
    Villager "This shit has swallowed a coin and won't get me the sandwich."
    return False

label BarNPCMachine(play_event = True, trigger = None): # event
    if is_erased("BarNPCMachine"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "BarNPCMachineBase", "BarNPCMachine") from _call_BarNPCMachine_PlayEvent
        return (1, "", "BarNPCMachine")
    return None

label BarNPCAbusiveBase:
    Villager "Fuck off..."
    return False

label BarNPCAbusive(play_event = True, trigger = None): # event
    if is_erased("BarNPCAbusive"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "BarNPCAbusiveBase", "BarNPCAbusive") from _call_BarNPCAbusive_PlayEvent
        return (1, "", "BarNPCAbusive")
    return None

label BarNPCBuyDrinkBase:
    Villager "Do you want a beer? I pay."
    return False

label BarNPCBuyDrink(play_event = True, trigger = None): # event
    if is_erased("BarNPCBuyDrink"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "BarNPCBuyDrinkBase", "BarNPCBuyDrink") from _call_BarNPCBuyDrink_PlayEvent
        return (1, "", "BarNPCBuyDrink")
    return None

label BarNPCOldDrunkBase:
    DrunkVillager "... too much ... beer..."
    return False

label BarNPCOldDrunk(play_event = True, trigger = None): # event
    if is_erased("BarNPCOldDrunk"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "BarNPCOldDrunkBase", "BarNPCOldDrunk") from _call_BarNPCOldDrunk_PlayEvent
        return (1, "", "BarNPCOldDrunk")
    return None

label BarNPCDadComplainsBase:
    Villager "My father is complaining all day long"
    return False

label BarNPCDadComplains(play_event = True, trigger = None): # event
    if is_erased("BarNPCDadComplains"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "BarNPCDadComplainsBase", "BarNPCDadComplains") from _call_BarNPCDadComplains_PlayEvent
        return (1, "", "BarNPCDadComplains")
    return None

label BarNPCBadFoodBase:
    Villager "The food in this club is terrible..."
    return False

label BarNPCBadFood(play_event = True, trigger = None): # event
    if is_erased("BarNPCBadFood"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "BarNPCBadFoodBase", "BarNPCBadFood") from _call_BarNPCBadFood_PlayEvent
        return (1, "", "BarNPCBadFood")
    return None

label BarNPCthug1Base:
    DrunkVillager "More beer at the festival tomorrow, guys!"
    return False

label BarNPCthug1(play_event = True, trigger = None): # event
    if is_erased("BarNPCthug1"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "BarNPCthug1Base", "BarNPCthug1") from _call_BarNPCthug1_PlayEvent
        return (1, "", "BarNPCthug1")
    return None

label BarNPCthug2Base:
    DrunkVillager "I've been drinking for two days ... holidays are great!!!"
    return False

label BarNPCthug2(play_event = True, trigger = None): # event
    if is_erased("BarNPCthug2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "BarNPCthug2Base", "BarNPCthug2") from _call_BarNPCthug2_PlayEvent
        return (1, "", "BarNPCthug2")
    return None

label BarNPCthug3_0:
    DrunkVillager "Thanks for the show"
    Johan "(...let him be, he's drunk)"
    return False

label BarNPCthug3_1:
    DrunkVillager "Are you coming for more, honey?"
    return False

label BarNPCthug3(play_event = True, trigger = None): # event
    if is_erased("BarNPCthug3"):
        return None
    elif trigger == "event" and switch("leyna_alone"):
        call PlayEvent(play_event, "BarNPCthug3_1", "BarNPCthug3") from _call_BarNPCthug3_1_PlayEvent
        return (1, "", "BarNPCthug3_1")
    elif trigger == "event":
        call PlayEvent(play_event, "BarNPCthug3_0", "BarNPCthug3") from _call_BarNPCthug3_0_PlayEvent
        return (1, "", "BarNPCthug3_0")
    return None

label BarNPCthug4Base:
    DrunkVillager "I'm sorry about what happened."
    $ show_transparent(1, "plano_mujer_timida", width=1600, height=900)
    $ resolve_scene()
    Leyna "Don't worry"
    DrunkVillager "(Shit, I have to fuck her somehow..)"
    $ erase_picture(1)
    $ resolve_scene()
    return False

label BarNPCthug4(play_event = True, trigger = None): # event
    if is_erased("BarNPCthug4"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "BarNPCthug4Base", "BarNPCthug4") from _call_BarNPCthug4_PlayEvent
        return (1, "", "BarNPCthug4")
    return None

label BarNPCthug5Base:
    DrunkVillager "We need more women in this town"
    return False

label BarNPCthug5(play_event = True, trigger = None): # event
    if is_erased("BarNPCthug5"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "BarNPCthug5Base", "BarNPCthug5") from _call_BarNPCthug5_PlayEvent
        return (1, "", "BarNPCthug5")
    return None

label BarWetTShirt_0:
    call ChangePartyMember("Leyna", False) from _call_BarWetTShirt_0_ChangePartyMember
    call PlaySound("music", "audio/Town2.ogg", volume=0.9, no_loop=False) from _call_BarWetTShirt_0_PlaySound
    call Movement("BarWetTShirt_0", "player", ["U"]) from _call_BarWetTShirt_0_Movement
    $ resolve_scene()
    Johan "Wow, this place is full of people, it may be a good chance to interview someone"
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "I don't know ... it seems that they're a bit out of control ..."
    Johan "Don't worry they're only partying, in my town they also get like this when it's the time of the summer festivals"
    $ erase_picture(1)
    call Movement("BarWetTShirt_0", "Barleyna", ["U","U","L"]) from _call_BarWetTShirt_0_Movement_1
    $ show_transparent(2, "expresion_neutral_mujer", width=1600, height=900)
    $ resolve_scene()
    Leyna "Excuse me, can I talk to you for a sec..."
    call Movement("BarWetTShirt_0", "BarNPCthug4", ["TURN_R"]) from _call_BarWetTShirt_0_Movement_2
    $ resolve_scene()
    Villager "OH WOW I've died? There's an angel in front of me"
    $ erase_picture(2)
    $ show_transparent(2, "plano_mujer_cartoon", width=1600, height=900)
    $ resolve_scene()
    Leyna "I... hahahaha thank you, I'm with my husband, It's our first time here"
    Villager "Your Husband?..."
    DrunkVillager "HEY JOHN COME HERE!"
    $ resolve_scene()
    call PauseForBalloon("BarWetTShirt_0") from _call_BarWetTShirt_0_PauseForBalloon
    John "I can't right now, wait a second!"
    $ resolve_scene()
    DrunkVillager "WHAT? COME ON!"
    $ erase_picture(2)
    stop music fadeout 1
    call Movement("BarWetTShirt_0", "BarNPCthug2", ["TURN_D"]) from _call_BarWetTShirt_0_Movement_3
    $ resolve_scene()
    call ShowAnimation(82, "Barleyna", "BarWetTShirt_0") from _call_BarWetTShirt_0_ShowAnimation
    call PlaySound("sound", "audio/Absorb1.ogg", volume=0.9, no_loop=True) from _call_BarWetTShirt_0_PlaySound_1
    DrunkVillager "Oh shit, sorry... oh??"
    $ resolve_scene()
    DrunkVillager "...!"
    call Movement("BarWetTShirt_0", "BarNPCthug1", ["TURN_D"]) from _call_BarWetTShirt_0_Movement_4
    $ resolve_scene()
    $ resolve_scene()
    $ resolve_scene()
    $ resolve_scene()
    "Crowd: ....."
    call PlaySound("music", "audio/Dungeon3.ogg", volume=0.9, no_loop=False) from _call_BarWetTShirt_0_PlaySound_2
    $ show_picture(3, "escena_camisa_mojada_1", scale=(52, 50), width=1600, height=900)
    $ resolve_scene()
    Leyna "(He has spilled the beer on me!...)"
    "Crowd: Uoooh!"
    DrunkVillager "(You can see everything!)"
    John "Incredible, this festival has started in a spectacular way!"
    pause
    $ show_picture(4, "escena_camisa_mojada_2", scale=(52, 50), width=1600, height=900)
    $ resolve_scene()
    Leyna "Ah?"
    Johan "(Shit, everyone is staring at her)"
    pause
    $ show_picture(5, "escenas_camisa_mojada_3", scale=(52, 50), width=1600, height=900)
    $ resolve_scene()
    Leyna "Do-don't look!"
    DrunkVillager "Yeah nah, I'm going to keep looking"
    Johan "We better leave for now, we'll be back another time"
    pause
    stop music fadeout 1
    $ erase_picture(4)
    $ erase_picture(3)
    $ erase_picture(5)
    call TransferPlayer("Town", "BarWetTShirt_0", 24, 46, direction=4) from _call_BarWetTShirt_0_TransferPlayer
    call Movement("BarWetTShirt_0", "player", ["L","L","TURN_R"]) from _call_BarWetTShirt_0_Movement_5
    call ChangePartyMember("Leyna", True) from _call_BarWetTShirt_0_ChangePartyMember_1
    $ resolve_scene()
    Johan "Wow that has been ... weird"
    Leyna "Yes, sorry. With the heat, I haven't put on a bra because it makes me uncomfortable"
    Johan "Don't worry, it's not your fault"
    Johan "Let's get back to the inn so you can change your clothes"
    $ set_switch("wet_shirt", True)
    call GalleryViewed("escena_camisa_mojada") from _call_BarWetTShirt_0_GalleryViewed
    $ set_switch("dry_shirt", True)
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_BarWetTShirt_0_PlaySound_3
    call TransferPlayer("Town", "BarWetTShirt_0", 28, 21, direction=2) from _call_BarWetTShirt_0_TransferPlayer_1
    call Movement("BarWetTShirt_0", "player", ["D","D"]) from _call_BarWetTShirt_0_Movement_6
    $ corruption = corruption + 1
    $ resolve_scene()
    "CORRUPTION +1"
    return False

label BarWetTShirt(play_event = True, trigger = None): # autorun
    if is_erased("BarWetTShirt"):
        return None
    elif switch("wet_shirt"):
        return None
    elif trigger == "autorun":
        call PlayEvent(play_event, "BarWetTShirt_0", "BarWetTShirt") from _call_BarWetTShirt_0_PlayEvent
        return (0, "", "BarWetTShirt_0")
    return None

label BarBJGame_0(menu_choice = None):
    Villager "Hmm sorry, I heard that your husband and you are writing an article about the town"
    $ show_transparent(1, "expresion_neutral_mujer", width=1600, height=900)
    $ resolve_scene()
    Leyna "Oh... that's right"
    Villager "Why don't you have a drink with us so we can talk about it? By the way, I'm sorry about yesterday..."
    $ show_transparent(2, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ erase_picture(1)
    $ resolve_scene()
    "... it was an unpleasant accident and I don't want you to think badly of us"
    Leyna "(I shouldn't do it. I get drunk very quick )"
    Leyna "(I remember the day I went to party with my friends ... the alcohol makes me behave in a way... that I don't like)"
    Leyna "(But it's a good way to find out about the festival and meet the townspeople)"
    call GetChoice([_("Yes"), _("No")], value=menu_choice, called_from="BarBJGame_0") from _call_BarBJGame_0_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Yes"):
        $ menu_choice = None
        $ show_transparent(3, "plano_mujer_sonrisa", width=1600, height=900)
        $ erase_picture(2)
        $ resolve_scene()
        Leyna "Sure guys, I could ask you some questions while drinking a beer"
        Villager "(Wow, I didn't expect her to accept ... I've been told what happened in the river... It's true, this girl is very naive)"
        Villager "Great! Let me pay the first few rounds"
        Leyna "Wow, thank you!"
        $ fade_out()
        $ erase_picture(3)
        call SetEventLocation("BarBJGame_0", "BarNPCthug5", 14, 4) from _call_BarBJGame_0_setloc
        call SetEventLocation("BarBJGame_0", "BarNPCthug1", 12, 4) from _call_BarBJGame_0_setloc_1
        call TransferPlayer("Bar", "BarBJGame_0", 13, 4, direction=2) from _call_BarBJGame_0_TransferPlayer
        call SetEventLocation("BarBJGame_0", "BarNPCthug2", 12, 5) from _call_BarBJGame_0_setloc_2
        $ fade_in()
        $ resolve_scene()
        "(SEVERAL BEERS LATER... )"
        Villager "... So yes, we expose our bodies on the festival place to honour the fertility goddess. As you may have noticed, the nudity in this town"
        ".. is very accepted and we don't usually censure ourselves in that aspect, we see shyness as a lack of respect for our traditions"
        $ show_transparent(4, "plano_mujer_cartoon", width=1600, height=900)
        $ resolve_scene()
        Leyna "I… I see..."
        Leyna "(Alcohol is affecting my head quite a bit ... I'm not thinking straight, I'd better go to the inn to take a nap)"
        Villager "Well, since you want to know about the traditions from this town, we can show you a game that we usually play here"
        $ show_transparent(5, "plano_mujer_sonrisa", width=1600, height=900)
        $ erase_picture(4)
        $ resolve_scene()
        Leyna "A game? Cool! It's a difficult one?"
        Villager "Oh no relax, take it easy, It is quite simple. We can play one round so you can learn and then we play seriously."
        Leyna "Nice, thank you!"
        Villager "It works with small bets, the usual is to go betting clothes until the loser is naked"
        $ show_transparent(6, "plano_mujer_sorpresa_lado", width=1600, height=900)
        $ erase_picture(5)
        $ resolve_scene()
        Leyna "Betting clothes? hmmm ... That's a bit ..."
        Villager "Hey come on don't worry, let's play one round to see if you like it"
        $ fade_out()
        $ erase_picture(6)
        $ fade_in()
        $ resolve_scene()
        "(ONE ROUND AND A COUPLE OF BEERS LATER.. ) "
        Villager "Well wow... You're quite good at this"
        $ show_transparent(7, "expresion_yuyu_mujer", width=1600, height=900)
        $ resolve_scene()
        Leyna "Yeeeah... It's very fun guys!"
        Villager "(She is quite drunk, how little endurance this woman has)"
        Leyna "Well ... it's time for me to go, I think I'm going to get some sleep"
        Leyna "alcohol doesn't suit me, I would'nt like to do something that I regret later"
        Villager "Wait! Don't you want to play a real round?"
        Villager "After we have taught you this game it would be rude to leave so soon, plus we are having a good time!"
        Leyna "Oh! seen that way, I don't want to disrespect you or anything like that... Yeah, why not?"
        $ fade_out()
        $ show_picture(8, "bar2", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
        $ erase_picture(7)
        $ fade_in()
        $ resolve_scene()
        Leyna "Hey! I'm getting pretty good at this!"
        Villager "(Too good I would say ... at this rate we won't see anything)"
        Villager "Hahahahaha, Don't get too cocky, girl..."
        $ fade_out()
        $ erase_picture(8)
        $ show_picture(9, "bar3", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
        $ fade_in()
        call PlaySound("sound", "audio/Miss.ogg", volume=0.9, no_loop=True) from _call_BarBJGame_0_PlaySound
        $ resolve_scene()
        "(A FEW MINUTES LATER ...)"
        Leyna "What were you saying?"
        Villager "(What the hell is going on? Why is she so good at this?)"
        Villager2 "(Aaah, all hope is lost...)"
        Leyna "Hahahahaha it seems like I've won guys, if you excuse me I'm going to go to the Inn..."
        Villager "Wait wait! After this humiliation, I need one last chance. You have removed us all our clothes already"
        "... so the bet will be different, let's see ... Yes! I have 300 dollars on me. I'll bet all in the next round!"
        $ show_picture(10, "bar4", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
        $ resolve_scene()
        Leyna "300!!!?..."
        Leyna "(That's a lot of money to earn in such a short time ... and Johan and I need it ... but)"
        Leyna "Sorry guys but I don't have that much money on me. I can't match the bet"
        Villager "Well ... 300 is a lot, right, maybe you could do something of equal value, right?"
        Leyna "Equal value?..."
        Villager "Yes ... if I win you have to make me ejaculate. There are almost no women in this town and I am quite in need of female contact"
        Leyna "Ejaculate?!!"
        Leyna "(I can't do that but... I've won all the rounds so far and.. 300 could come in handy to pay for travel expenses)"
        call GetChoice([_("Okey I'll do it"), _("No, this is to much")], value=menu_choice, called_from="BarBJGame_0") from _call_BarBJGame_0_GetChoice_1
        $ menu_choice = _return
        if menu_choice == _("Okey I'll do it"):
            $ menu_choice = None
            $ resolve_scene()
            Leyna "Okey ... Okey, let's do it"
            Villager "Nice!"
            Villager "(It's time to use my last trick)"
            $ fade_out()
            $ erase_picture(9)
            $ erase_picture(10)
            $ show_picture(11, "bar5", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
            $ fade_in()
            call PlaySound("sound", "audio/Attack2.ogg", volume=0.9, no_loop=True) from _call_BarBJGame_0_PlaySound_1
            $ resolve_scene()
            Villager "YEAH!! I WON!!"
            Leyna "What..."
            Leyna "(Oh no no no..)"
            Villager "It seems luck is no longer on your side"
            Villager "(HELL YES!! I CAN'T BELIEVE THIS IS HAPPENING)"
            Villager2 "(He did it! The absolute madman!!)"
            Villager "Very good... well ... you can do it as you want, As long as I cum there is no problem"
            $ fade_out()
            $ erase_picture(11)
            $ show_picture(12, "bar6", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
            $ fade_in()
            call PlaySound("music", "audio/Dungeon3.ogg", volume=0.9, no_loop=False) from _call_BarBJGame_0_PlaySound_2
            $ resolve_scene()
            Leyna "Hmmm I see ... but ... I'm married and ..."
            Villager "Come on, you just have to make me come, it will take just a minute, a bet's a bet"
            Villager "A woman hasn't touched me for centuries, I will not last at all!"
            pause
            $ show_picture(13, "bar7", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
            $ resolve_scene()
            Leyna "(It's so close...)"
            $ play_video_looped(1, "paja_webm", "paja.webm",width=1080,height=608)
            $ resolve_scene()
            pause
            $ stop_video(1)
            $ show_picture(14, "bar8", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
            $ resolve_scene()
            Leyna "(Why is this taking so long?...)"
            $ play_video_looped(1, "paja_webm", "paja.webm",width=1080,height=608)
            $ resolve_scene()
            pause
            Villager "(Endure... ENDURE!!! It's been soo long)"
            Villager "(I don't know when next time will be, I have to enjoy it as much as possible)"
            $ stop_video(1)
            $ show_picture(15, "bar9", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
            $ resolve_scene()
            Villager "You know... If you do it this way you won't get it. At this rate, we can be here all afternoon"
            pause
            $ show_picture(16, "bar10", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
            $ resolve_scene()
            Leyna "(Maybe... maybe if I use my mouth?)"
            pause
            call PlaySound("sound", "audio/Poison.ogg", volume=0.9, no_loop=True) from _call_BarBJGame_0_PlaySound_3
            $ show_picture(17, "bar11", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
            $ resolve_scene()
            Villager "(YES! But... I can't hold it anymore)"
            pause
            call PlaySound("sound", "audio/Poison.ogg", volume=0.9, no_loop=True) from _call_BarBJGame_0_PlaySound_4
            $ show_picture(18, "bar12", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
            $ resolve_scene()
            Villager2 "(Oh she's really going to do it!)"
            pause
            call PlaySound("sound", "audio/Poison.ogg", volume=0.9, no_loop=True) from _call_BarBJGame_0_PlaySound_5
            $ show_picture(19, "bar13", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
            $ resolve_scene()
            Villager "Almost there..."
            Leyna "hmm?..."
            Villager "OOOooohh!!!"
            Leyna "(!!!)"
            $ flash_screen([255,255,255,170], 60, True)
            call PlaySound("sound", "audio/Poison.ogg", volume=0.9, no_loop=True) from _call_BarBJGame_0_PlaySound_6
            $ flash_screen([255,255,255,170], 60, True)
            $ fade_out()
            $ erase_picture(12)
            $ erase_picture(14)
            $ erase_picture(15)
            $ erase_picture(13)
            $ erase_picture(16)
            $ erase_picture(17)
            $ erase_picture(18)
            $ erase_picture(19)
            $ show_picture(20, "bar14", pos=(-125, 0), scale=(69, 69), width=1600, height=900)
            $ fade_in()
            $ resolve_scene()
            Leyna "AAaah?!!!"
            Villager "Sorry. It's been so long since a woman touched me that I couldn't help it"
            Leyna "It's.. it's all over my face ..."
            Villager "Relax, I bring you a rag to clean yourself"
            Leyna "Than... thanks. I have to go now or I will pass out.."
            "It has been..................... fun? Bye"
            $ fade_out()
            $ erase_picture(20)
            call TransferPlayer("Town", "BarBJGame_0", 25, 46, direction=4) from _call_BarBJGame_0_TransferPlayer_1
            $ set_switch("gave_bj", True)
            $ corruption = corruption + 3
            $ fade_in()
            call Movement("BarBJGame_0", "player", ["L","L"]) from _call_BarBJGame_0_Movement
            $ show_transparent(1, "plano_mujer_timida", width=1600, height=900)
            $ resolve_scene()
            Leyna "..."
            "What the hell have I done?... I can't let Johan find out about this ..."
            call GalleryViewed("bar") from _call_BarBJGame_0_GalleryViewed
            "+ 3 CORRUPTION "
            $ erase_picture(1)
        elif menu_choice == _("No, this is to much"):
            $ menu_choice = None
            $ resolve_scene()
            Leyna "Sorry guys, but I'm a married woman and I can't do this kind of thing..."
            Villager "I see, don't worry, have a good time at the festival."
            Villager "(I have time to seduce this girl little by little.. there's no reason to rush)"
            $ fade_out()
            $ erase_picture(9)
            $ erase_picture(10)
            call TransferPlayer("Town", "BarBJGame_0", 25, 46, direction=4) from _call_BarBJGame_0_TransferPlayer_2
            $ fade_in()
            $ set_switch("no_bj", True)
            call Movement("BarBJGame_0", "player", ["L","L"]) from _call_BarBJGame_0_Movement_1
            $ resolve_scene()
            Leyna "Where do I go now?"
    elif menu_choice == _("No"):
        $ menu_choice = None
        $ resolve_scene()
        Leyna "Sorry guys maybe another time"
        Villager "Okay, if you change your mind you already know where to find us"
        $ erase_picture(2)
        call Movement("BarBJGame_0", "player", ["TURN_D","D","D"]) from _call_BarBJGame_0_Movement_2
    $ resolve_scene()
    return False

label BarBJGame(play_event = True, trigger = None): # event
    if is_erased("BarBJGame"):
        return None
    elif switch("no_bj"):
        return None
    elif switch("gave_bj"):
        return None
    elif trigger == "event" and switch("leyna_alone"):
        call PlayEvent(play_event, "BarBJGame_0", "BarBJGame") from _call_BarBJGame_0_PlayEvent
        return (0, "", "BarBJGame_0")
    return None

