label CasinoFinaleBG:
    $ set_transparency_backgrounds(["bg_casino"])
    $ set_map_backgrounds(["bg_casino"])
    return

label CasinoFinaleStart:
    call CasinoFinaleBG from _call_CasinoFinaleBG
    stop music
    stop bgs
    return

label CasinoFinaleEnd:
    return

label CasinoFinaleLooksLikeTheLastEventIsGoingToBeHereBase:
    $ show_picture(1, "orgia1")
    $ resolve_scene()
    Johan "Looks like the last event is going to be here, this place is much bigger than it looks from the outside"
    Leyna "yes, and it's crowded!"
    Johan "Stay close to me, okay?"
    $ show_picture(2, "orgia2")
    if switch("corruption_low"):
        $ resolve_scene()
        Leyna "Sure, I'll be by your side all this time"
        Johan "... thank you Leyna"
    if switch("corruption_average"):
        Leyna "I-I don't think there's any need to worry, what could happen?"
        Johan "Nothing... (or so I hope)"
    if switch("corruption_high"):
        Leyna "Well don't be like that, I'm sure we'll have a good time if it starts a fun activity I might not be able to help but join in hahahaha"
        Johan "...."
    $ show_picture(3, "orgia3")
    $ resolve_scene()
    Johan "!!!"
    Alexa "Hey Johan, I see you came to the last event"
    $ show_picture(4, "orgia4")
    $ resolve_scene()
    Johan "Alexa! ... you've come too... but of course why wouldn't you come and do it?"
    Alexa "Hahahahaha are you insinuating something? Well I have something to talk to you about, come with me for a second"
    Johan "But..."
    Alexa "Don't worry about Leyna, she'll be fine"
    Johan "If you say so... well come on, but make it quick"
    Alexa "Hehehehe I hope not"
    Johan "What?"
    Alexa "Nothing, let's go"
    $ fade_out()
    $ show_picture(5, "orgia6")
    $ fade_in()
    $ resolve_scene()
    Villager "Hey Leyna, I see you've decided to come!"
    Leyna "Oh Y-yeah"
    $ show_picture(6, "orgia7")
    $ resolve_scene()
    Leyna "I have come with... ah?"
    Leyna "Where has Johan gone?"
    YoungVillager "He'll be having fun over there, come with us Leyna! the ritual is about to begin!"
    Leyna "Ritual?"
    Villager2 "Yeah, well it's silly, but it'll be a lot of fun, you'll see"
    Leyna "W-well okay, I'll go with you"
    $ fade_out()
    $ show_picture(7, "orgia4")
    $ fade_in()
    $ resolve_scene()
    Johan "Well, Alexa, what did you want to tell me? You made me leave Leyna there all alone"
    Alexa "You'll know soon enough, I guess I liked you more than I should have Johan"
    Johan "What? look..."
    Alexa "Quiet...listen, it looks like it's about to start"
    Johan "???"
    OldVillager "Good afternoon everyone!"
    $ show_picture(8, "orgia8")
    call PlaySound("sound", "audio/Applause2.ogg", volume=0.9, no_loop=True) from _call_CasinoFinaleEV015_PlaySound
    $ resolve_scene()
    OldVillager "Hahaha I'm glad to see you all too"
    OldVillager "Well this is about to begin"
    OldVillager "Once again this year we celebrate the Goddess cliff festival in honour of our local fertility goddess"
    OldMan "We have been celebrating the festival for centuries and thanks to it our crops are fertile, our men are tall and strong"
    OldVillager "And we can lead a happy and fulfilled life in this village"
    OldMan "and as every year the time has come for the last ritual, one in which we will join the goddess of fertility to commune with her"
    call PlaySound("sound", "audio/Applause2.ogg", volume=0.9, no_loop=True) from _call_CasinoFinaleEV015_PlaySound_1
    OldVillager "Very well, I see that you are all ready for this last celebration, now we will all join together and enjoy the pleasure of love"
    Johan "???? Alexa... what does all this mean?"
    $ show_picture(9, "orgia9")
    $ resolve_scene()
    Johan "!!!! mmhhgf"
    pause
    $ show_picture(10, "orgia5")
    $ resolve_scene()
    Alexa "What do you think is going on Johan? Isn't it obvious... everyone... everyone here right now is going to make love like we've never made love before"
    Johan "T-Then Leyna is right there and she's going to...."
    Alexa "What do you think?"
    Johan "N-no... I have to... I have to stop it"
    Alexa "Well, I don't think you can do it, instead of trying in vain... why don't you stay with me and start the party?"
    Alexa "Of all people, I have chosen you to start with, I haven't even chosen my husband, do you understand? You're not my type but... I like you very much"
    Johan "Yeah... well I... I'm sorry but I can't, I have to get Leyna out of here by any means possible"
    Alexa "... you'll regret it, you should carry on as you have been doing and let yourself be carried away by this"
    Johan "No, I'm going to get my wife out of here and we'll go, bye"
    Alexa ".... fool...."
    $ show_picture(11, "orgia10")
    $ resolve_scene()
    Johan "Let me through!"
    Villager "??? Fucking wait your turn like everyone else!"
    $ show_picture(12, "orgia11")
    $ resolve_scene()
    Johan "Ah shit my nose!"
    $ show_picture(13, "orgia12")
    $ resolve_scene()
    Johan "I hope it's not broken, shit... I'm supposed to find my wife among all these people... fuck!"
    $ fade_out()
    $ show_picture(14, "orgia13")
    $ fade_in()
    $ resolve_scene()
    "johan: I-I don't see her anywhere.... "
    Johan "Where has she gone? ... damn... why did I decide to write about this damn town and its damn festival?"
    Johan "Since then weird things have been happening and our relationship .... shit I don't even want to think about it"
    Johan "I don't see her anywhere, again the situation is getting out of control... what can I do?"
    Johan "Is there anything I can do? At this stage Leyna... Leyna... where are you?"
    $ show_picture(15, "orgia14")
    $ resolve_scene()
    Barman "Johan? what are you doing lying there?"
    Johan "ah? oh you... I was trying to find Leyna... tried to stop it from happening... but I can't find her in all these people... I don't know what to do man..."
    Barman "... you should not have come to the last event Johan..."
    Johan "You're right... What am I supposed to do now? What am I supposed to do without Leyna?"
    Barman ".... come on get up, you can't stay like this"
    Johan "!!! b-but I... there's nothing I can..."
    Barman "Shut up, let's go get your wife, I can't see a man like this and do nothing, I'll help you get her out of here"
    Johan "!!! I-I don't know what to say... thank you very much"
    Barman "Save your thanks and let's get you out of here!"
    Johan "Yes!"
    $ show_picture(16, "orgia15")
    $ resolve_scene()
    Barman "Hey, get out of the way!"
    Villager "Ah? !!!! Oh sorry man, go ahead"
    Barman "Come on Johan over here!"
    Johan "Yes!"
    Barman "I-I think I see Leyna over there, let's hurry!"
    Johan "Yes, I see it too"
    Johan "!!!!"
    if switch("corruption_low"):
        $ show_picture(17, "orgia16")
        $ resolve_scene()
        Villager2 "Come on honey I know you want to do this"
        YoungVillager "Come on Leyna, let yourself go and suck our dicks"
        Leyna "no, leave me alone, I don't want to do any of this"
        Johan "Hey! leave her alone!"
        pause
        $ show_picture(18, "orgia17")
        $ resolve_scene()
        Villager2 "her husband the cuck has already arrived, it was taking too long already"
        YoungVillager "What are you doing here? Go and have a wank somewhere"
        Johan "Leave my wife alone, Leyna, we're getting out of here"
        YoungVillager "Bullshit you're leaving! She's staying here!"
        Johan "Get out of the way, you moron!"
        Villager2 "Don't touch my nephew"
        $ show_picture(19, "orgia18")
        $ resolve_scene()
        Leyna "Johan!"
        Barman "what the fuck are you doing motherfucker? come here"
        $ show_picture(20, "orgia19")
        $ resolve_scene()
        Villager2 "ah!"
        YoungVillager "What have you done to my uncle? you will regret this! you know what awaits you!"
        $ show_picture(21, "orgia20")
        $ resolve_scene()
        Barman "You want me to knock you unconscious too, you little punk? get out of my sight!"
        YoungVillager "Tch I'll get you for this, you old fucker"
        $ show_picture(22, "orgia21")
        $ resolve_scene()
        Johan "Th-thanks man, you saved my ass"
        Leyna "Yes, thank you very much for helping us"
        Barman "thank less, get out of here at once, this is not made for you, a couple from outside should never have to come to this place!"
        Johan "Y-yes, I don't know how to thank you."
        Barman "Well, thank me by having a drink before you go and never coming back to this shithole town again"
        Johan "Hahahaha ouch... my jaw hurts... yes, it's a deal"
        Barman "Hehehehehe right, get out of here"
        Leyna "Yes, thank you very much!"
        $ fade_out()
        call TransferPlayer("InnRooms", "CasinoFinaleEV015", 11, 10, direction=2) from _call_CasinoFinaleEV015_TransferPlayer
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
        $ erase_picture(17)
        $ erase_picture(18)
        $ erase_picture(19)
        $ erase_picture(20)
        $ erase_picture(21)
        $ erase_picture(22)
        $ erase_picture(16)
        $ fade_in()
        $ resolve_scene()
        "the following morning"
    if switch("corruption_average"):
        $ show_picture(17, "orgia22")
        $ resolve_scene()
        Johan "N-no... it can't be happening"
        Barman "Shit..."
        Johan "What the hell are you doing Leyna?"
        Leyna "J-johan?"
        Villager2 "Man! look who's husband is here! do you like what you see pussy?"
        YoungVillager "Hahahaha! we're having a great time with your wife!  look!"
        pause
        $ show_picture(18, "orgia23")
        $ resolve_scene()
        "Flap flap flap"
        Leyna "AAAaaah!!!"
        Johan "H-how could you do this to me? It's only been a few minutes and you... Oh, my God"
        Leyna "Johan... don't look... AAAHHHH! My god!"
        pause
        $ show_picture(19, "orgia24")
        $ resolve_scene()
        Johan "Shit... I'm out of here"
        Barman "Johan..."
        Johan "LET ME GO!"
        Barman "!!!!"
        pause
        $ show_picture(20, "orgia25")
        $ resolve_scene()
        Leyna "J-Johan!"
        Villager2 "At last that prick is leaving, come on, let's get on with it"
        Leyna "N-no..."
        YoungVillager "??? you were saying something? come on, here's something you need to put in your mouth"
        Leyna "I said no! leave me alone!"
        Villager2 "??? What the fuck are you saying? at this point stay here! come on let's go on!"
        Leyna "No! Let me go! Leave me alone!"
        Barman "Let her go"
        Villager2 "Yeah? and who's going to stop us from making him stay? you? you're nobody, you moron! get out of here before something bad happens to you!"
        pause
        $ show_picture(21, "orgia26")
        $ resolve_scene()
        Barman "Now you can never talk to me like that again, or at least not until you get your mouth reconstructed, you little shit"
        "YOung Villager: !!! Wh-what have you done? Do you even know whose son he is?"
        pause
        $ show_picture(22, "orgia20")
        $ resolve_scene()
        Barman "Yes, and if you don't want the same thing to happen to you, you can let the girl go"
        YoungVillager "O-okay, there's no need to get like that"
        $ show_picture(23, "orgia27")
        $ resolve_scene()
        Leyna "T-thanks boss"
        Barman "Don't thank me and go to your husband... but after what you've done... you've really fucked up, precious"
        Leyna "I-I... I know"
        Barman "Well, if you know that, you're already late in going after him if you still have any appreciation for your marriage"
        Leyna "Y-yes... Thank you very much"
        Barman "...Go"
        $ fade_out()
        call ChangePartyMember("Johan", False) from _call_CasinoFinaleEV015_ChangePartyMember
        call TransferPlayer("InnRooms", "CasinoFinaleEV015", 11, 10, direction=2) from _call_CasinoFinaleEV015_TransferPlayer_1
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
        $ fade_in()
        $ resolve_scene()
        "the following morning"
    if switch("corruption_high"):
        $ show_picture(17, "orgia22")
        $ resolve_scene()
        Johan "N-no... it can't be happening."
        Barman "shit..."
        Johan "What the hell are you doing Leyna?"
        Leyna "J-johan?"
        Villager2 "Man! look who's husband is here! do you like what you see pussy?"
        YoungVillager "Hahahaha! we're having a great time with your wife! look!"
        pause
        $ show_picture(18, "orgia23")
        $ resolve_scene()
        "Flap flap flap"
        Leyna "AAAaaah!!!"
        Johan "H-how could you do this to me? It's only been a few minutes and you... Oh, my God."
        Leyna "I.... AAhhh Yeah-keep it up!"
        pause
        $ show_picture(19, "orgia28")
        $ resolve_scene()
        Johan "You disgust me... I'm out of here"
        Barman "What a fucking mess..."
        pause
        $ show_picture(20, "orgia29")
        $ resolve_scene()
        Johan "How could this happen... I've been blind all this time, the signs were there but I couldn't believe it... it's just too much already"
        Johan "Tomorrow morning I will be leaving this town and if Leyna should show up at our house her things will be waiting for her at the door"
        Johan "Next to the divorce papers"
        Johan ".... I'm going to drink myself unconscious"
        "Meanwhile Leyna... "
        pause
        $ show_picture(21, "orgia30")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_CasinoFinaleEV015_PlaySound_2
        $ resolve_scene()
        Leyna "Ah ah ah!"
        Villager2 "Look at her! She doesn't even care that her husband is gone, she just wants to keep fucking!"
        if johan_leyna_sex == 1:
            $ resolve_scene()
            Leyna "No, I don't care, keep fucking me!"
        if johan_leyna_sex == 2:
            Leyna "Sh-shut up it's not true!"
        $ resolve_scene()
        Villager "Don't worry, we'll give you everything you want"
        Leyna "Aaahhh"
        Villager2 "Goodness gracious this has finally happened, everyone in the village has been waiting for it"
        Villager3 "Hey let me too, I want to too"
        "Villager 4: And me! "
        Leyna "Ahh there is enough for everyone"
        Villager2 "What a slut"
        pause
        $ fade_out()
        $ show_picture(22, "orgia31")
        $ fade_in()
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_CasinoFinaleEV015_PlaySound_3
        $ resolve_scene()
        Villager "Ugh yes! do you like it? let me hear from you"
        Leyna "I love it, don't stop! keep going!"
        Villager2 "Jesus Christ, this bitch is insatiable"
        Villager3 "Come on eat my cock right now"
        Leyna "hmfmmafagh"
        Villager3 "like this, up to the tonsils!"
        "Villager 4: Leave some for me I want some too! "
        Villager3 "You've got your wife right there, go to her or I'll go"
        "Villager 4: greedy bastard"
        pause
        $ fade_out()
        $ fade_in()
        $ resolve_scene()
        Villager "God I'm cumming!"
        Villager2 "Me too!"
        Villagers "Ahhhh"
        pause
        stop bgs fadeout 1
        $ show_picture(23, "orgia32")
        $ resolve_scene()
        Leyna "Oh my god... you've stuffed me like a turkey!"
        Villager3 "It's not over yet!"
        Leyna "Ah ah ah... I don't know if I can go on"
        Villager3 "You can"
        pause
        $ fade_out()
        $ show_picture(24, "corrupcionalta1")
        $ fade_in()
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_CasinoFinaleEV015_PlaySound_4
        $ resolve_scene()
        Leyna "Aaahhh!! god! you are breaking me in half!"
        "Villager3: See how you could go on, we are going to fuck you between all of us until you can't walk! "
        Leyna "AAh!!! Yes please, use me like the slut that I am"
        "Villager 4: Jesus, this bitch is insatiable! "
        pause
        $ show_picture(25, "corrupcionalta2")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_CasinoFinaleEV015_PlaySound_5
        $ resolve_scene()
        "Villager 4: Now you will see! "
        Leyna "OOOh!!! I...I can't go on any longer... i'm cumming!"
        "Villager 4: We will make you cum many times more, bitch!  "
        Leyna "Yes! yes! I've never been fucked like this! fuck me harder!"
        "Villager 4: W-wait! I'm going to cum! open your mouth bitch!"
        pause
        $ show_picture(26, "corrupcionalta3")
        $ resolve_scene()
        "Villager 4: Like that in your mouth, get ready, I've got a lot in store for you! "
        Villager3 "Yes, I'm going to fill your face with cum too, you slut!"
        Leyna "MMmf!"
        Villager3 "Thank goodness your husband is not around so we have you alone for the whole town"
        "Villager 4: That's what you wanted, isn't it, you fucking whore?"
        pause
        $ flash_screen([255,255,255,170], 60, True)
        $ flash_screen([255,255,255,170], 60, True)
        $ show_picture(27, "corrupcionalta4")
        $ resolve_scene()
        $ flash_screen([255,255,255,170], 60, False)
        "Villager 4: AAAhhh!! Fuck! "
        Villager3 "Here you go! all for you!"
        "Villager 4: Yes, enjoy! hahahaha"
        pause
        $ show_picture(28, "corrupcionalta5")
        $ resolve_scene()
        Leyna "A-are you finished?"
        Villager3 "Fuck, you want more?"
        "Villager 4: Yes, it is true that this girl is insatiable! "
        "Villager 4: Don't worry, guys! Here's someone who wants more! "
        Leyna "!!! I-I don't know if I can go on"
        "Villager 4: Yes you can, now you will see how you can honey"
        pause
        stop bgs fadeout 1
        $ show_picture(29, "pantallanegro", scale=(120, 120), width=816, height=600)
        $ resolve_scene()
        "Some time later"
        pause
        $ show_picture(30, "corrupcionalta6")
        $ resolve_scene()
        Villager "Hahahaha now I think it is satisfied!"
        Villager2 "Yeah, the bitch can't even move, she's just lying there shaking and can't get up"
        Leyna "Ah ah ah I ... I... ah ah ah i can't..."
        Villager "Hahahaha Don't worry, you can rest now, we all need a break"
        Villager2 "Yes, good night, bitch! You can come back whenever you want..."
        Leyna "Ahhh..."
        $ fade_out()
        call ChangePartyMember("Johan", False) from _call_CasinoFinaleEV015_ChangePartyMember_1
        call TransferPlayer("InnRooms", "CasinoFinaleEV015", 11, 10, direction=2) from _call_CasinoFinaleEV015_TransferPlayer_2
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
        $ fade_in()
        $ resolve_scene()
        "the following morning"
    $ set_switch("festival_final", True)
    call GalleryViewed("orgia") from _call_CasinoFinaleEV015_GalleryViewed
    $ resolve_scene()
    return False

label CasinoFinaleLooksLikeTheLastEventIsGoingToBeHere(play_event = True, trigger = None): # autorun
    if is_erased("CasinoFinaleLooksLikeTheLastEventIsGoingToBeHere"):
        return None
    elif trigger == "autorun":
        call PlayEvent(play_event, "CasinoFinaleLooksLikeTheLastEventIsGoingToBeHereBase", "CasinoFinaleLooksLikeTheLastEventIsGoingToBeHere") from _call_CasinoFinaleLooksLikeTheLastEventIsGoingToBeHere_PlayEvent
        return (0, "", "CasinoFinaleLooksLikeTheLastEventIsGoingToBeHere")
    return None

