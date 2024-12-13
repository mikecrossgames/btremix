label FestivalFinaleBG:
    $ set_transparency_backgrounds(["bg_festival"])
    $ set_map_backgrounds(["map_festival"])
    return

label FestivalFinaleStart:
    call FestivalFinaleBG from _call_FestivalFinaleBG
    stop music
    stop bgs
    return

label FestivalFinaleEnd:
    return

label FestivalFinaleYoSlapBase:
    $ show_picture(1, "mini4")
    call GalleryViewed("mini4") from _call_FestivalFinaleEV006_GalleryViewed
    $ resolve_scene()
    Villager "Yo! (Slap!)"
    Leyna "Ah!"
    Villager "As beautiful as always Leyna!"
    Johan "Hey, cut it out!"
    Villager "Hehehehe sorry!"
    pause
    $ erase_picture(1)
    $ resolve_scene()
    return False

label FestivalFinaleYoSlap(play_event = True, trigger = None): # event
    if is_erased("FestivalFinaleYoSlap"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "FestivalFinaleYoSlapBase", "FestivalFinaleYoSlap") from _call_FestivalFinaleYoSlap_PlayEvent
        return (1, "", "FestivalFinaleYoSlap")
    return None

label FestivalFinaleHeyLeynaGoodToSeeYouHereBase:
    $ show_picture(1, "mini1")
    call GalleryViewed("mini1") from _call_FestivalFinaleEV007_GalleryViewed
    $ resolve_scene()
    DrunkVillager "Hey Leyna, good to see you here!"
    Leyna "AH?"
    Johan "What the hell are you doing? Let her go right now!"
    DrunkVillager "Hahahahaha relax, I just wanted to be able to touch them before you leave town! your wife has perfect tits!"
    Johan "Cut the crap!"
    pause
    $ erase_picture(1)
    $ resolve_scene()
    return False

label FestivalFinaleHeyLeynaGoodToSeeYouHere(play_event = True, trigger = None): # event
    if is_erased("FestivalFinaleHeyLeynaGoodToSeeYouHere"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "FestivalFinaleHeyLeynaGoodToSeeYouHereBase", "FestivalFinaleHeyLeynaGoodToSeeYouHere") from _call_FestivalFinaleHeyLeynaGoodToSeeYouHere_PlayEvent
        return (1, "", "FestivalFinaleHeyLeynaGoodToSeeYouHere")
    return None

label FestivalFinaleDoYouWantSomeMasksForTheFinalEventBase:
    Villager "Do you want some masks for the final event?"
    Johan "Masks? no thanks... (what do you need masks for?)"
    return False

label FestivalFinaleDoYouWantSomeMasksForTheFinalEvent(play_event = True, trigger = None): # event
    if is_erased("FestivalFinaleDoYouWantSomeMasksForTheFinalEvent"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "FestivalFinaleDoYouWantSomeMasksForTheFinalEventBase", "FestivalFinaleDoYouWantSomeMasksForTheFinalEvent") from _call_FestivalFinaleDoYouWantSomeMasksForTheFinalEvent_PlayEvent
        return (1, "", "FestivalFinaleDoYouWantSomeMasksForTheFinalEvent")
    return None

label FestivalFinaleHeyGoodToSeeYouLeynaEspeciallyInThisSituationHeheheheheBase:
    Villager "Hey good to see you leyna! especially in this situation hehehehehe"
    Leyna "H-hi"
    Johan "..."
    Villager "Come here give me a hug!"
    $ show_picture(1, "mini2")
    call GalleryViewed("mini2") from _call_FestivalFinaleEV009_GalleryViewed
    $ resolve_scene()
    Villager "Yes, let me give you a big hug"
    Leyna "hey! Let go of me... you're touching me with your..."
    Johan "Let her go!"
    Villager "Yes, I'm releasing it right now, but let me enjoy it a little longer"
    Johan "No! Let her go right now!"
    Villager "tch! okay"
    pause
    $ erase_picture(1)
    $ resolve_scene()
    return False

label FestivalFinaleHeyGoodToSeeYouLeynaEspeciallyInThisSituationHehehehehe(play_event = True, trigger = None): # event
    if is_erased("FestivalFinaleHeyGoodToSeeYouLeynaEspeciallyInThisSituationHehehehehe"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "FestivalFinaleHeyGoodToSeeYouLeynaEspeciallyInThisSituationHeheheheheBase", "FestivalFinaleHeyGoodToSeeYouLeynaEspeciallyInThisSituationHehehehehe") from _call_FestivalFinaleHeyGoodToSeeYouLeynaEspeciallyInThisSituationHehehehehe_PlayEvent
        return (1, "", "FestivalFinaleHeyGoodToSeeYouLeynaEspeciallyInThisSituationHehehehehe")
    return None

label FestivalFinaleOhLeynaIWasHopingToMeetYouIHaveSomethingToGiveYouBase:
    DrunkVillager "Oh Leyna, I was hoping to meet you, I have something to give you"
    Leyna "To me? okay, what do you want to give me"
    DrunkVillager "Oh my god you are so perfect, I am completely in love"
    $ show_picture(1, "mini5")
    call GalleryViewed("mini5") from _call_FestivalFinaleEV011_GalleryViewed
    $ resolve_scene()
    Johan "!!! Hey get off!"
    Leyna "Hmmmf"
    pause
    $ erase_picture(1)
    $ resolve_scene()
    DrunkVillager "Sorry but I had to do it, I couldn't keep it to myself"
    return False

label FestivalFinaleOhLeynaIWasHopingToMeetYouIHaveSomethingToGiveYou(play_event = True, trigger = None): # event
    if is_erased("FestivalFinaleOhLeynaIWasHopingToMeetYouIHaveSomethingToGiveYou"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "FestivalFinaleOhLeynaIWasHopingToMeetYouIHaveSomethingToGiveYouBase", "FestivalFinaleOhLeynaIWasHopingToMeetYouIHaveSomethingToGiveYou") from _call_FestivalFinaleOhLeynaIWasHopingToMeetYouIHaveSomethingToGiveYou_PlayEvent
        return (1, "", "FestivalFinaleOhLeynaIWasHopingToMeetYouIHaveSomethingToGiveYou")
    return None

label FestivalFinaleEV012Base:
    call PlaySound("music", "audio/Psychedelic-Rock.ogg", volume=0.9, no_loop=False) from _call_FestivalFinaleEV012_PlaySound
    $ resolve_scene()
    return False

label FestivalFinaleEV012(play_event = True, trigger = None): # parallel
    if is_erased("FestivalFinaleEV012"):
        return None
    elif trigger == "parallel":
        call PlayEvent(play_event, "FestivalFinaleEV012Base", "FestivalFinaleEV012") from _call_FestivalFinaleEV012_PlayEvent
        return (0, "", "FestivalFinaleEV012")
    return None

label FestivalFinaleWellHereWeAre_0:
    call Movement("FestivalFinaleEV013_0", "player", ["R","R","TURN_L"]) from _call_FestivalFinaleEV013_0_Movement
    $ resolve_scene()
    Johan "Well, here we are"
    Leyna "Yes... what could we do?"
    Johan "Well, let's go for a walk and see what we find, the mayor didn't give me much information"
    "Johan. He just told me that there was a big event at the end of the day to thank the fertility goddess for the good crops of the year and all that"
    Leyna "It's a little scary..."
    Johan "Hahhahaaha why? do you think we are in some horror movie where the whole town is conspiring to sacrifice us?"
    Leyna "Oh, shut up, I'm so scared, don't say things like that again...being naked, the truth is that I can't help but feel a little vulnerable"
    Johan "Don't worry, I'm here to protect you"
    Leyna "Oh my knight in white armor"
    Johan "Hmmm I like the sound of that"
    Leyna "Well, let's see what the festival has in store for us"
    $ set_self_switch("FestivalFinale","FestivalFinaleWellHereWeAre","A",True)
    return False

label FestivalFinaleWellHereWeAre(play_event = True, trigger = None): # autorun
    if is_erased("FestivalFinaleWellHereWeAre"):
        return None
    elif self_switch("FestivalFinale","FestivalFinaleWellHereWeAre","A"):
        return None
    elif trigger == "autorun":
        call PlayEvent(play_event, "FestivalFinaleWellHereWeAre_0", "FestivalFinaleWellHereWeAre") from _call_FestivalFinaleWellHereWeAre_0_PlayEvent
        return (0, "", "FestivalFinaleWellHereWeAre_0")
    return None

label FestivalFinaleHeyWhatsGoingOnHere_0:
    Johan "Hey what's going on here?"
    call GalleryViewed("duelo") from _call_FestivalFinaleEV014_0_GalleryViewed
    Villager "A traditional ritual, it is a kind of masculinity contest, it is difficult to explain, come closer if you want"
    Johan "Sure, thank you very much"
    OldVillager "Here we have two young people who have some personal problems they want to leave behind"
    OldVillager "To do so, they have decided to use the traditional way of the village and measure themselves in this men's endurance contest"
    Leyna "Hahaha this is fun"
    Johan "Yes, I wonder how they will be measured, a race perhaps?"
    OldVillager "Well, present your respective competition partners!"
    Villager1 "I have brought my wife to accompany me in this duel"
    OldVillager "Perfect, it is the right decision and you young man? have you got a duel partner?"
    Villager2 "(shit, I don't have a wife and I haven't been able to convince any of the few women who live in town, what the hell can I do)"
    Villager2 "!!! (that's Leyna? hahahaha perfect let's see...) I... yes I choose Leyna the tourist girl! she's right there!"
    $ show_picture(1, "duelo1")
    $ resolve_scene()
    Johan "!!!!"
    Leyna "!!!! W-what?"
    OldVillager "Very well, may the chosen one come forward!"
    Leyna "I-I... what's all this? I don't know if..."
    Villager2 "Of course he knows, I've explained it to him before (whispering) please do me this favor, I need to win this guy"
    Leyna ".... Y-yes I'm here I'll be this guy's partner for the duel"
    Johan "???? what the hell are you saying Leyna?"
    OldMan "Silence, young man! dare not interrupt this ancestral tradition or the wrath of the goddess will fall upon you!"
    Johan "!!!! B-but..."
    OldVillager "Well... let's start with the ritual, you know what it consists of, it is an endurance test, the first one to ejaculate will be the loser"
    Leyna "!!!! oh..."
    OldVillager "Girls, place your partner's member between your thighs and let him do the work"
    Johan "!!! But that's my...!"
    Villager3 "Quiet! this is important!"
    Johan "(Damn it! What the hell are they going to do?)"
    $ show_picture(2, "duelo2")
    $ resolve_scene()
    Leyna "oh!"
    OldVillager "Perfect! you are already in position! let the duel begin!"
    Villager2 "Sorry Leyna, I'll be careful"
    call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_FestivalFinaleEV014_0_PlaySound
    $ show_picture(3, "duelo3")
    $ resolve_scene()
    "flap flap flap flap"
    Johan "!!!!"
    Leyna "(He's rubbing against me down there with all his might...my god his penis is touching my....)"
    Leyna "mmmfa..."
    Villager2 "Did you just moan Leyna? (my god we just started and she's already dripping)"
    "Flap flap flap"
    pause
    $ show_picture(4, "duelo11")
    stop bgs fadeout 1
    $ resolve_scene()
    Johan "(How the fuck did we end up in this situation? This is all happening to my wife... in front of all these people who are watching)"
    Johan "(And there's practically nothing I can do about it, everyone seems to take this bullshit very seriously, if I say anything they might lynch me right here)"
    Villager2 "Good God Leyna... I have never been so close to you, you are the sexiest woman I have ever seen in my life... you are so soft"
    pause
    $ show_picture(5, "duelo4")
    $ resolve_scene()
    Leyna "Ah... C-callate... tu solo... mmmhaa callate e intenta aguantar"
    Leyna "(If this goes on for a long time I... I'm going to cum... in front of all these men and my husband...)"
    Villager2 "(My God... I can't hold back anymore I want to fuck her right here in front of the whole world... if I can only stick it in a couple of times I' ll die happy)"
    Villager2 "(I have to try, even if I lose the duel... I don't give a crap anymore)"
    pause
    $ show_picture(6, "duelo7")
    $ resolve_scene()
    Leyna "Y-you're not thinking of... don't even think about it"
    Villager2 "I'm sorry Leyna, I can't take it anymore...I have to... I have to...."
    Leyna "!!!"
    if switch("corruption_low"):
        $ resolve_scene()
        Leyna "(I can't allow it! I have to do something... I can't let him fuck me in front of everyone, especially in front of Johan!)"
        pause
        $ show_picture(7, "duelo5")
        $ resolve_scene()
        Leyna "mmmha! You won't be able to do that to me in front of everyone, you'll have to be satisfied with my thighs"
        Villager2 "Damn it...!!!! AH ... my god, I, I was about to cum inside of you...ah there's no other option... I will have to continue"
        pause
        $ show_picture(8, "duelo6")
        $ resolve_scene()
        Leyna "(He seems to have given up, but I can't be distracted ...for a second I...almost lost my mind, for a moment I wanted him to..."
        Leyna "... to fuck me in front of all these men)"
        "Cillager 2: F-fuck... I'm going to lose... fuck! "
        pause
        $ flash_screen([255,255,255,170], 60, True)
        $ flash_screen([255,255,255,170], 60, True)
        $ show_picture(9, "duelo10")
        $ resolve_scene()
        Villager2 "AAHhh!!! Shit!"
        Leyna "! oh!(he has cum! holy cow! what a quantity!)"
        Johan "(That son of a bitch has cum on my wife's thighs and I'm standing here watching like an asshole doing nothing)"
        OldVillager "Well, it looks like we have a winner! Sorry young man, it looks like you lost the contest"
        Villager2 "Yeah... what a bummer (well, at least I got to fuck Leyna's thighs, which wasn't bad at all)"
        OldVillager "Oh, young lady, you can go clean up back there"
        Leyna "Oh thanks"
        OldVillager "And now the loser will buy everyone else a good beer"
        Villager2 "hmmm Yes, come on guys this one goes on my account"
        Johan "(Well, at least I'm going to drink that beer, after all this shit I need it)"
        pause
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
        $ fade_in()
        $ resolve_scene()
        Leyna ".... (this is awkward, Johan says nothing)"
        Johan "(Shit, now what the hell do I say? I didn't do anything while all that was going on, I feel like a coward)"
        Johan "W-well, let's continue exploring the festival"
        Leyna "Yes..."
    if switch("corruption_average"):
        Leyna "(I can't allow it! I have to do something... I can't let him fuck me in front of everyone, especially in front of Johan!)"
        pause
        $ show_picture(7, "duelo5")
        $ resolve_scene()
        Leyna "mmmha! You won't be able to do that to me in front of everyone, you'll have to be satisfied with my thighs"
        Villager2 "Damn it...!!!! AH ... my god, I, I was about to cum inside of you...ah there's no other option... I will have to continue"
        pause
        $ show_picture(8, "duelo6")
        $ resolve_scene()
        Leyna "(He seems to have given up, but I can't be distracted ...for a second I...almost lost my mind, for a moment I wanted him to..."
        Leyna "... to fuck me in front of all these men)"
        "Cillager 2: F-fuck... I'm going to lose... fuck! "
        pause
        $ flash_screen([255,255,255,170], 60, True)
        $ flash_screen([255,255,255,170], 60, True)
        $ show_picture(9, "duelo10")
        $ resolve_scene()
        Villager2 "AAHhh!!! Shit!"
        Leyna "! oh!(he has cum! holy cow! what a quantity!)"
        Johan "(That son of a bitch has cum on my wife's thighs and I'm standing here watching like an asshole doing nothing)"
        OldVillager "Well, it looks like we have a winner! Sorry young man, it looks like you lost the contest"
        Villager2 "Yeah... what a bummer (well, at least I got to fuck Leyna's thighs, which wasn't bad at all)"
        OldVillager "Oh, young lady, you can go clean up back there"
        Leyna "Oh thanks"
        OldVillager "And now the loser will buy everyone else a good beer"
        Villager2 "hmmm Yes, come on guys this one goes on my account"
        Johan "(Well, at least I'm going to drink that beer, after all this shit I need it)"
        pause
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
        $ fade_in()
        $ resolve_scene()
        Leyna ".... (this is awkward, Johan says nothing)"
        Johan "(Shit, now what the hell do I say? I didn't do anything while all that was going on, I feel like a coward)"
        Johan "W-well, let's continue exploring the festival"
        Leyna "Yes..."
    if switch("corruption_high"):
        "Leyan: (He's going to stick it in front of all these people, in front of Johan and I... I want him to do it I-I can't stop him)"
        Villager2 "(Oh almost there! It's almost in!)"
        pause
        $ show_picture(7, "duelo8")
        $ resolve_scene()
        Villager2 "OOhh yeah"
        Leyna "Ah mmmha!"
        pause
        $ show_picture(8, "duelo9")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_FestivalFinaleEV014_0_PlaySound_1
        $ resolve_scene()
        "Flap flap flap"
        Villager2 "Jesus Christ your pussy feels so good!"
        Villager2 "I'll fuck you until I'm satisfied"
        Johan "!!! (H-he's fucking her? he just put it in!)"
        pause
        $ show_picture(9, "duelo12")
        $ resolve_scene()
        Johan "Hey!!"
        OldVillager "Hey, what did I tell you about interrupting the ritual?!"
        Johan "(shit I'm going to be lynched! I have to think of something....)"
        Johan "He's-he's... He's cheating, look at him!"
        OldVillager "What?"
        OldVillager "!!! Hey what do you think you're doing? stop right now!"
        Villager2 "No! just a little more I'm almost there"
        pause
        $ flash_screen([255,255,255,170], 60, True)
        $ flash_screen([255,255,255,170], 60, True)
        $ show_picture(10, "duelo10")
        stop bgs fadeout 1
        $ resolve_scene()
        "Plop"
        Villager2 "Ah!!"
        Leyna "Ah! my god!"
        Leyna "(W-what a lot... he must have been holding on for a long time)"
        OldMan "How dare you cheat in this contest? you will be automatically disqualified!"
        Villager2 "I don't care, I've been able to fuck this goddess, I don't care about anything"
        Johan "!!! Fucking asshole"
        Johan "Come on Leyna let's go"
        Leyna "Y-yes (god I've been so close to cumming... I can't take it anymore, I need a good orgasm)"
        pause
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
        $ fade_in()
        $ resolve_scene()
        Leyna ".... (this is awkward, Johan says nothing)"
        Johan "(Shit, now what the hell do I say? I didn't do anything while all that was going on, I feel like a coward)"
        Johan "W-well, let's continue exploring the festival"
        Leyna "Y-yes"
    $ set_self_switch("FestivalFinale","FestivalFinaleHeyWhatsGoingOnHere","A",True)
    $ final_festival = final_festival + 1
    $ resolve_scene()
    return False

label FestivalFinaleHeyWhatsGoingOnHere(play_event = True, trigger = None): # event
    if is_erased("FestivalFinaleHeyWhatsGoingOnHere"):
        return None
    elif self_switch("FestivalFinale","FestivalFinaleHeyWhatsGoingOnHere","A"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "FestivalFinaleHeyWhatsGoingOnHere_0", "FestivalFinaleHeyWhatsGoingOnHere") from _call_FestivalFinaleHeyWhatsGoingOnHere_0_PlayEvent
        return (1, "", "FestivalFinaleHeyWhatsGoingOnHere_0")
    return None

label FestivalFinaleevent_15_0:
    call Movement("FestivalFinaleevent_15_0", "player", ["TURN_R"]) from _call_FestivalFinaleevent_15_0_Movement
    $ resolve_scene()
    Leyna "Oh hello Mr. Photographer"
    call Movement("FestivalFinaleevent_15_0", "FestivalFinalefotografo", ["TURN_L"]) from _call_FestivalFinaleevent_15_0_Movement_1
    $ resolve_scene()
    call PauseForBalloon("FestivalFinaleevent_15_0") from _call_FestivalFinaleevent_15_0_PauseForBalloon
    OldMan "Oh! hi Leyna, did you come to see the last day of the festival?"
    call GalleryViewed("fotofestival") from _call_FestivalFinaleevent_15_0_GalleryViewed
    Leyna "Yes, we come to see how they decide to end this"
    OldMan "What a coincidence that we are meeting now"
    Johan "How so?"
    OldMan "Well, you see, as one of the village elders this year I have been put in charge of choosing the queen of this year's festivities"
    "Leyna. Queen of the festivities? "
    OldMan "Yes, it is usually given to the most beautiful woman in town that damn Beatriz has been winning 5 years in a row"
    OldMan "Of course we do not usually have much to choose from"
    OldMan "But you know what? fuck it, Leyna named you Queen of this year's festivities, you are by far, much more beautiful than that girl"
    Leyna "!!!! I... thank you very much! I don't know what to say!"
    OldMan "You don't have to say anything, accept this offering and let me take some pictures to commemorate the moment"
    Leyna "Sure!"
    Johan "But she's naked, taking pictures of her right now...."
    OldMan "Oh come on johan, don't worry, we keep them safe, you don't want to interrupt this ancestral tradition, do you?"
    Johan "Hmmm very well, do as you please!"
    OldMan "I will announce the event to the others"
    Johan "A-announce?"
    OldMan "Yes! I'll be right back"
    Johan "W-wait... ah shit..."
    $ fade_out()
    $ show_picture(1, "fotofestival1")
    $ fade_in()
    $ resolve_scene()
    OldMan "Well guys here you have the new queen of the festivities"
    call PlaySound("sound", "audio/Applause1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound
    Villagers "(cheering)"
    "Angry villager: Well, I don't agree, it's not even from the town"
    Villager1 "Oh come on, you're just mad because your wife isn't the winner!"
    Villager2 "That's right! It's already been five years in a row, get over it!"
    "Angry villager: Hmp! "
    OldMan "Well let's take the pictures!"
    Leyna "Sure! What position do you want me to be in?"
    OldMan "for now let's start with a more natural pose"
    $ show_picture(2, "fotofestival2")
    $ resolve_scene()
    Leyna "Is this okay?"
    OldMan "Yes perfect!"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Equip1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound_1
    Villager2 "Beauty!"
    call PlaySound("sound", "audio/Applause1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound_2
    "Villagers : (more cheering)"
    Johan "Hmmm (I don't know if I like this, I feel flattered in a strange way... but at the end of the day they are seeing my wife naked...)"
    OldMan "Perfect, let's see a couple of positions that are a little bit more intense, you know what to do Leyna like when we work in the studio"
    Leyna "V-vale, me da un poco de verguenza con tanta gente delante"
    Villager2 "Oh don't be ashamed! you are a goddess!"
    call PlaySound("sound", "audio/Applause1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound_3
    "Villagers : (more cheering)"
    Leyna "Hahahahaha okay guys, I'm going to pose like I learned!"
    OldMan "That's the way to talk!"
    pause
    $ show_picture(3, "fotofestival3")
    $ resolve_scene()
    Villagers "OOHHH!!"
    call PlaySound("sound", "audio/Applause1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound_4
    Villager2 "Impressive! you have a talent for this"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Equip1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound_5
    Leyna "Hehehehehe thank you very much"
    Johan "... (What's going on? Leyna seems to be having a great time... being the center of attention of all these stares)"
    Leyna "Well, do you want something a little bit more racy? let's see what you think of this Hehehehehehe"
    pause
    $ show_picture(4, "fotofestival4")
    $ resolve_scene()
    OldMan "Wow! impressive Leyna! very good keep it up!"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Equip1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound_6
    Villager3 "Holy God I'm getting a hard-on!"
    Villager2 "Yes, seeing this in person is much better than in magazines"
    "Johan. (Shit they are talking about my wife... but they are right, this is very exciting, I have an uncontrollable erection and we are here in public)"
    Villager "Hey old man, take a picture of me with the queen of the parties! I want one as a souvenir! When I show it to my brother he will die of envy!"
    pause
    $ show_picture(5, "fotofestival5")
    $ resolve_scene()
    Johan "H-hey!"
    OldMan "Very good! Smile Leyna!"
    Leyna "I... sure..."
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Equip1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound_7
    OldMan "Great job Leyna!"
    Villager "Yes, good job"
    Villager2 "Hey I want one too"
    Villager "Sure man, let's pose together"
    OldMan "Of course, it's an excellent idea!"
    pause
    $ show_picture(6, "fotofestival6")
    $ resolve_scene()
    Johan "!!! (this is getting out of control)"
    Villager "Come on Leyna Smile a little"
    Villager2 "Yes, cheer up that face!"
    pause
    $ show_picture(7, "fotofestival7")
    $ resolve_scene()
    "Slap slap slap"
    Leyna "(T-they're touching my face with their...) Y-yeah..."
    Leyna "(What the hell am I doing?)"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Equip1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound_8
    OldMan "Very nice photo!"
    Villager "I've come up with a great idea, grab our dicks, it'll look great in the photo"
    Johan "C-Come on, I think that's enough"
    Villager3 "Hey shut the fuck up, you're fucking up our festival"
    "Villager 4: Exactly, keep quiet "
    Leyna "..."
    if switch("corruption_low"):
        $ resolve_scene()
        Leyna "... I don't know guys I think that's enough"
        OldMan "Oh come on Leyna, one last photo!"
        Villagers "Yes, come on Leyna!"
        Leyna "O-okay one last picture but no grabbing anything down there, okay?"
        OldMan "Of course Leyna as you wish"
        Villager2 "Okay, since this is the last photo, let's do something spectacular"
        Leyna "S-sure"
        pause
        $ show_picture(8, "fotofestival22")
        $ resolve_scene()
        Leyna "!!! Wow"
        Villager2 "That's it! perfect,it will look great in the photo"
        Leyna "(Holy cow... his thing is touching me down there)"
        OldMan "A perfect pose guys stay there for a second"
        Villager2 "As long as you want"
        Johan ".... (this is too much)"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Equip1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound_9
        OldMan "Perfect the photo has been spectacular guys!"
        OldMan "you can now get her down"
        pause
        $ fade_out()
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(4)
        $ erase_picture(5)
        $ erase_picture(6)
        $ erase_picture(7)
        $ erase_picture(8)
        $ fade_in()
    if switch("corruption_average"):
        $ resolve_scene()
        Leyna "O-okay perfect"
        pause
        $ show_picture(8, "fotofestival10")
        $ resolve_scene()
        Villager2 "Oh, your hands are so warm, can we stay like this all afternoon? hahahaha"
        OldMan "This is going to look spectacular! stand still!"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Equip1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound_10
        Villager2 "You have small hands eh? hehehehehe"
        Leyna "hihihi I think it's more like you guys... you have your own things that are too big"
        Johan "!!!!"
        Villager2 "Hey, why don't you give a little kiss to our \"very big things\"? I think it would look great for the picture, don't you?"
        OldMan "Yes, I think you're right, it will be perfect for the photo!"
        Johan "You shouldn't..."
        Leyna "If you think it's a good idea..."
        pause
        $ show_picture(9, "fotofestival8")
        $ resolve_scene()
        "Muak"
        Johan "Leyna..."
        OldMan "Perfect!"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Equip1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound_11
        OldMan "The session is looking spectacular, we could even sell it to the magazine!"
        pause
        $ show_picture(10, "fotofestival10")
        $ resolve_scene()
        Leyna "do you think they would be interested?"
        OldMan "Yes, if we take a couple more pictures we could sell it"
        Johan "But we have already talked about it"
        Leyna "Well, perfect then, a couple more pictures and we're off, right Johan?"
        Johan "...."
        OldMan "Well let's move on to the next photo then"
        Villager2 "Oh! I think I have a good idea for a pose!"
        OldMan "Let's see then"
        pause
        $ show_picture(11, "fotofestival11")
        $ resolve_scene()
        OldMan "Hmmm that's a good picture! stand still!"
        "Rub rub rub"
        Leyna "(His penis keeps rubbing my clit...)"
        Leyna "(Whispering) H-hey, be careful, if you go on like this...."
        Villager2 "(Whispering) You're going to cum? that wouldn't be so bad, would it?"
        Leyna "My husband is right here..."
        Villager2 "And he's standing there quietly watching... your husband is a sucker who likes to watch his wife being fucked"
        Leyna "D-don't say that, I..."
        "Rub rub rub"
        Leyna "Hmmmaa"
        OldMan "Guys, stay still for a second, I'm trying to take the picture"
        Villager2 "Yeah, sorry"
        OldMan "Hmp!"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Equip1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound_12
        OldMan "All right guys, let's move on to the next photo"
        OldMan "Hold her"
        pause
        $ show_picture(12, "fotofestival14")
        $ resolve_scene()
        Villager2 "Is this good?"
        OldMan "Yes, that's perfect, stay still now, okay?"
        Leyna "Okay..."
        Villager2 "I thought you were heavier... in this position, we could fuck you right now in front of everybody and you wouldn't be able to do anything, right?"
        Leyna "What?"
        Villager2 "I am sure that if we started to fuck you right now you would only moan with pleasure and would do nothing to defend yourself"
        Villager2 "Even with your husband in front of you, you would just moan and cum with pleasure, wouldn't you? you're dripping down there, I can feel it, you're craving it"
        Leyna "S-shut up"
        Villager2 "Am I wrong? I should do it... here and now so that your husband can see what kind of woman you are"
        Leyna "N-no...please"
        Villager2 "Very well... but before the end of the festival I'm going to fuck you raw, I want you to know that"
        Leyna "..."
        pause
        $ show_picture(13, "fotofestival15")
        $ resolve_scene()
        Leyna "(I can't help it, since I got here I've been gradually becoming more submissive, you're right, you could fuck me right here and I wouldn't do anything...)"
        Leyna "(And that scares me... scares me into the kind of woman I'm becoming)"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Equip1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound_13
        OldMan "Great job guys!"
        OldMan "Leyna? are you ok?"
        Leyna "Yes... but I think I've had enough pictures for today"
        OldMan "B-but the magazine"
        Johan "I think you heard my wife... enough photos"
        OldMan "Okay, okay... but it's a shame with all the good material we were putting out"
        Leyna "I'm sorry... but let's go for a walk around the festival, okay?"
        OldMan "S-sure, enjoy"
        Villager2 "...."
        pause
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
        $ fade_in()
    if switch("corruption_high"):
        $ resolve_scene()
        Leyna "Sure, no problem!"
        pause
        $ show_picture(8, "fotofestival10")
        $ resolve_scene()
        Villager2 "Oh, your hands are so warm, can we stay like this all afternoon? hahahaha."
        OldMan "This is going to look spectacular! stand still!"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Equip1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound_14
        Villager2 "You have small hands eh? hehehehehe"
        Leyna "hihihi I think it's more like you guys... you have your own things that are too big"
        Johan "!!!!"
        Villager2 "Hey, why don't you give a little kiss to our \"very big things\"? I think it would look great for the picture, don't you?"
        OldMan "Yes, I think you're right, it will be perfect for the photo!"
        Johan "You shouldn't..."
        Leyna "If you think it's a good idea..."
        pause
        $ show_picture(9, "fotofestival8")
        $ resolve_scene()
        "Muak"
        Johan "Leyna..."
        OldMan "Perfect!"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Equip1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound_15
        OldMan "The session is looking spectacular, we could even sell it to the magazine!"
        pause
        $ show_picture(10, "fotofestival10")
        $ resolve_scene()
        Leyna "do you think they would be interested?"
        OldMan "Yes, if we take a couple more pictures we could sell it"
        Johan "But we have already talked about it"
        Leyna "Well, perfect then, a couple more pictures and we're off, right Johan?"
        Johan "...."
        OldMan "Well let's move on to the next photo then"
        Villager2 "At this point I think it would be a good idea to continue a little further on, for the sake of the photo session, right?"
        Leyna "???"
        Villager2 "Seeing that Leyna is so willing, I think she should put it in her mouth, don't you think? that way it would look good for the magazine and so on"
        OldMan "Well, it's a good idea, yes"
        Johan "I don't think that..."
        OldMan "Come on Johan, at this point what's the difference? it's just a few pictures, we have already talked about this on several occasions"
        OldMan "Think only of the money and your wife's future"
        Johan "...."
        OldMan "What do you think Leyna?"
        Leyna "I think... I think it's a good idea, I'm going to do it"
        pause
        $ show_picture(11, "fotofestival9")
        $ resolve_scene()
        Villager2 "Oof! you've gone straight... that feels really good, sorry but I think I could cum at any moment"
        OldMan "What are you 15 years old? hold on like a man"
        Villager2 "Y-yeah sorry, but with a beauty like that sucking my cock... it's hard to hold on"
        Johan "You're talking about my wife there, a little respect"
        Villager2 "Hehehehehe Yeah, sorry, your wife is eating my dick and since she is so beautiful it's hard for me to control my words"
        Johan "... (whispering) asshole"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Equip1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound_16
        OldMan "The photo is perfect"
        OldMan "Let's move on to the next photo"
        pause
        $ show_picture(12, "fotofestival11")
        $ resolve_scene()
        Leyna "Like this?"
        OldMan "That's perfect"
        Villager2 "(whispering) you sure are wet down there... I think I might slip inside without wanting to"
        Leyna ".... Ah ah ah"
        pause
        $ show_picture(13, "fotofestival12")
        $ resolve_scene()
        Villager2 "I am sure that if we started to fuck you right now you would only moan with pleasure and would do nothing to defend yourself"
        Villager2 "Even with your husband in front of you, you would just  moan and cum with pleasure, wouldn't you? you're dripping down there, I can feel it, you're craving it"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Equip1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound_17
        Leyna "S-shut up"
        Villager2 "Am I wrong? I should do it... here and now so that your husband can see what kind of woman you are"
        Leyna "...."
        Villager2 "You don't say anything? very well I take that as a yes"
        pause
        $ show_picture(14, "fotofestival13")
        $ resolve_scene()
        Leyna "!!!"
        Leyna "AAhhh...!"
        Johan "Leyna!"
        OldMan "Oh excellent idea"
        OldMan "this will be perfect, I was going to ask you anyway"
        Johan "This cannot continue"
        Villager2 "hey! shut up, we're working here, okay?"
        Villager2 "God your pussy feels so good"
        Leyna "Ah ah ah!"
        Johan "Leyna...."
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Equip1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound_18
        OldMan "All right, that's enough in that position, Leyna stand up and lean back a little bit"
        Leyna "Ah ah ah Yes..."
        pause
        $ show_picture(15, "fotofestival16")
        $ resolve_scene()
        Leyna "Like this?"
        OldMan "Yes, that's perfect, since we've come this far let's add some anal, it'll be quick"
        Johan "(Damn, there's a small crowd gathered here... and they're all seeing Leyna in this state)"
        Johan "(Wait, he said anal?)"
        pause
        $ show_picture(16, "fotofestival17")
        $ resolve_scene()
        Villager1 "All right, I'm going to do it"
        Leyna "B-be careful"
        Villager1 "(My God how sexy! I-I can't believe I' m doing this, since the first day I saw her around town I've been dreaming about something like this...)"
        Villager1 "S-sure, I'll be careful"
        pause
        $ show_picture(17, "fotofestival18")
        $ resolve_scene()
        Leyna "Hmmm!"
        Villager1 "Oh! that... feels so good... so tight..."
        pause
        $ show_picture(18, "fotofestival19")
        $ resolve_scene()
        "Plop! "
        Leyna "Ah!"
        Villager1 "S-sorry, it came out, I'll put it back in right away!"
        Leyna "Slow down, big guy"
        Villager1 "!!! God, you are perfect"
        pause
        $ show_picture(19, "fotofestival20")
        $ resolve_scene()
        Leyna "Ah!!! A-all right, it's inside"
        Johan "!!!! (She's enjoying it... she's definitely enjoying it)"
        OldMan "Very good, now try to put it in a little deeper"
        Villager1 "Sure!"
        pause
        $ show_picture(20, "fotofestival21")
        $ resolve_scene()
        Leyna "Oh my god!"
        OldMan "But not so much beast! take it out a little"
        Villager1 "Sorry!"
        OldMan "Yes, that's it, that's perfect"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Equip1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound_19
        OldMan "perfect picture as always"
        OldMan "now let's move on to the next photo"
        Villager2 "Yes, I'm missing all the fun here"
        OldMan "Very well, since you have so much energy, take it and raise it up in the air, focusing it towards the camera"
        Villager2 "All right!"
        pause
        $ show_picture(21, "fotofestival22")
        $ resolve_scene()
        Leyna "Oh!"
        Villager2 "Good?"
        OldMan "Yeah!"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Equip1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound_20
        OldMan "Great keep it up"
        Villager2 "All right, let's get to the good part"
        Leyna "!!! oh! you are so strong"
        Villager2 "now you will see..."
        pause
        $ show_picture(22, "fotofestival23")
        $ resolve_scene()
        Johan "!!!!"
        Leyna "hmmm..."
        Leyna "AAH! god..."
        Villager2 "You like it, don't you?"
        OldMan "A perfect image, this is what we have been asked in the magazine all this time"
        Johan "Take the picture quickly come on"
        Villager2 "tch"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Equip1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleevent_15_0_PlaySound_21
        OldMan "Very well perfect and now..."
        pause
        $ show_picture(23, "fotofestival24")
        $ resolve_scene()
        "Johan. I think that's enough, don't you? "
        OldMan "But we still have..."
        Johan "Come on Leyna let's go!"
        Leyna "Johan..."
        Villager2 "at this point, man..."
        Johan "Shut your mouth! Leyna let's go!"
        Villager2 "Hehehe as you say man, see you later Leyna"
        Leyna "Sure... See you guys"
        Johan "(\"see you guys?\" unbelievable...)"
        pause
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
        $ erase_picture(11)
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
    $ set_self_switch("FestivalFinale","FestivalFinaleevent_15","A",True)
    $ final_festival = final_festival + 1
    $ resolve_scene()
    return False

label FestivalFinaleevent_15(play_event = True, trigger = None): # event
    if is_erased("FestivalFinaleevent_15"):
        return None
    elif self_switch("FestivalFinale","FestivalFinaleevent_15","A"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "FestivalFinaleevent_15_0", "FestivalFinaleevent_15") from _call_FestivalFinaleevent_15_0_PlayEvent
        return (1, "", "FestivalFinaleevent_15_0")
    return None

label FestivalFinaleToCasinoFinale_1:
    $ fade_out()
    call TransferPlayer("CasinoFinale", "FestivalFinaleEV016_1", 8, 10, direction=0) from _call_FestivalFinaleEV016_1_TransferPlayer
    call Movement("FestivalFinaleEV016_1", "player", ["U"]) from _call_FestivalFinaleEV016_1_Movement
    $ fade_in()
    $ resolve_scene()
    return False

label FestivalFinaleToCasinoFinale(play_event = True, trigger = None): # event
    if is_erased("FestivalFinaleToCasinoFinale"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "FestivalFinaleToCasinoFinale_1", "FestivalFinaleToCasinoFinale") from _call_FestivalFinaleToCasinoFinale_1_PlayEvent
        return (1, "", "FestivalFinaleToCasinoFinale_1")
    return None

label FestivalFinaleAltavozPleaseComeToTheGameRoomTheFinalEventOfTheFestivalIsAboutToBegin_0:
    call PlaySound("sound", "audio/Bell1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleEV017_0_PlaySound
    $ resolve_scene()
    call PauseForBalloon("FestivalFinaleEV017_0") from _call_FestivalFinaleEV017_0_PauseForBalloon
    Johan "???"
    "Altavoz: Please come to the game room, the final event of the festival is about to begin"
    Johan "Oh! it looks like they're going to be wrapping this up, we should go"
    Leyna "Yeah..."
    $ set_self_switch("FestivalFinale","FestivalFinaleAltavozPleaseComeToTheGameRoomTheFinalEventOfTheFestivalIsAboutToBegin","A",True)
    return False

label FestivalFinaleAltavozPleaseComeToTheGameRoomTheFinalEventOfTheFestivalIsAboutToBegin(play_event = True, trigger = None): # autorun
    if is_erased("FestivalFinaleAltavozPleaseComeToTheGameRoomTheFinalEventOfTheFestivalIsAboutToBegin"):
        return None
    elif self_switch("FestivalFinale","FestivalFinaleAltavozPleaseComeToTheGameRoomTheFinalEventOfTheFestivalIsAboutToBegin","A"):
        return None
    elif trigger == "autorun" and final_festival >= 2:
        call PlayEvent(play_event, "FestivalFinaleAltavozPleaseComeToTheGameRoomTheFinalEventOfTheFestivalIsAboutToBegin_0", "FestivalFinaleAltavozPleaseComeToTheGameRoomTheFinalEventOfTheFestivalIsAboutToBegin") from _call_FestivalFinaleAltavozPleaseComeToTheGameRoomTheFinalEventOfTheFestivalIsAboutToBegin_0_PlayEvent
        return (0, "", "FestivalFinaleAltavozPleaseComeToTheGameRoomTheFinalEventOfTheFestivalIsAboutToBegin_0")
    return None

label FestivalFinaleToCasinoFinale_v2_1:
    $ fade_out()
    call TransferPlayer("CasinoFinale", "FestivalFinaleEV018_1", 8, 10, direction=0) from _call_FestivalFinaleEV018_1_TransferPlayer
    call Movement("FestivalFinaleEV018_1", "player", ["U"]) from _call_FestivalFinaleEV018_1_Movement
    $ fade_in()
    $ resolve_scene()
    return False

label FestivalFinaleToCasinoFinale_v2(play_event = True, trigger = None): # event
    if is_erased("FestivalFinaleToCasinoFinale_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "FestivalFinaleToCasinoFinale_v2_1", "FestivalFinaleToCasinoFinale_v2") from _call_FestivalFinaleToCasinoFinale_v2_1_PlayEvent
        return (1, "", "FestivalFinaleToCasinoFinale_v2_1")
    return None

label FestivalFinaleAMassageWait_0:
    Leyna "A massage? wait. I want to see the festival a little more before going, I'm sure that after the massage I'll want to go to rest a little"
    Johan "Yeah, you're right"
    return False

label FestivalFinaleAMassageWait_1:
    call PlaySound("sound", "audio/Open1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleEV023_1_PlaySound
    call Movement("FestivalFinaleEV023_1", "FestivalFinaleEV023", ["TURN_L",["WAIT",3],"TURN_R",["WAIT",3],"TURN_U","THROUGH_ON"]) from _call_FestivalFinaleEV023_1_Movement
    call Movement("FestivalFinaleEV023_1", "player", ["FORWARD"]) from _call_FestivalFinaleEV023_1_Movement_1
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_FestivalFinaleEV023_1_PlaySound_1
    call TransferPlayer("MassageParlor", "FestivalFinaleEV023_1", 7, 12, direction=0) from _call_FestivalFinaleEV023_1_TransferPlayer
    $ resolve_scene()
    return False

label FestivalFinaleAMassageWait_2:
    Leyna "W-we don't need to go back in there"
    return False

label FestivalFinaleAMassageWait_3:
    "Closed"
    return False

label FestivalFinaleAMassageWait(play_event = True, trigger = None): # event
    if is_erased("FestivalFinaleAMassageWait"):
        return None
    elif trigger == "event" and switch("johan_and_leyna_sex"):
        call PlayEvent(play_event, "FestivalFinaleAMassageWait_3", "FestivalFinaleAMassageWait") from _call_FestivalFinaleAMassageWait_3_PlayEvent
        return (1, "", "FestivalFinaleAMassageWait_3")
    elif trigger == "event" and (switch("massage_masturbation") or switch("massage_sex")):
        call PlayEvent(play_event, "FestivalFinaleAMassageWait_2", "FestivalFinaleAMassageWait") from _call_FestivalFinaleAMassageWait_2_PlayEvent
        return (1, "", "FestivalFinaleAMassageWait_2")
    elif trigger == "event" and food_stand >= 1:
        call PlayEvent(play_event, "FestivalFinaleAMassageWait_1", "FestivalFinaleAMassageWait") from _call_FestivalFinaleAMassageWait_1_PlayEvent
        return (1, "", "FestivalFinaleAMassageWait_1")
    elif trigger == "event" and switch("festival"):
        call PlayEvent(play_event, "FestivalFinaleAMassageWait_0", "FestivalFinaleAMassageWait") from _call_FestivalFinaleAMassageWait_0_PlayEvent
        return (1, "", "FestivalFinaleAMassageWait_0")
    return None

