label Town2BG:
    $ set_transparency_backgrounds(["bg_town_south"])
    $ set_map_backgrounds(["map_town_south"])
    return

label Town2Start:
    call Town2BG from _call_Town2BG
    stop music
    stop bgs
    return

label Town2End:
    return

label Town2BoarInnBase:
    "Boar Inn"
    return False

label Town2BoarInn(play_event = True, trigger = None): # event
    if is_erased("Town2BoarInn"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2BoarInnBase", "Town2BoarInn") from _call_Town2BoarInn_PlayEvent
        return (1, "", "Town2BoarInn")
    return None

label Town2ToInnBase:
    call PlaySound("sound", "audio/Open1.ogg", volume=0.9, no_loop=True) from _call_Town2EV003_PlaySound
    call Movement("Town2EV003", "Town2EV003", ["TURN_L",["WAIT",3],"TURN_R",["WAIT",3],"TURN_U","THROUGH_ON"]) from _call_Town2EV003_Movement
    call Movement("Town2EV003", "player", ["FORWARD"]) from _call_Town2EV003_Movement_1
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_Town2EV003_PlaySound_1
    call TransferPlayer("Inn", "Town2EV003", 8, 12, direction=0) from _call_Town2EV003_TransferPlayer
    $ resolve_scene()
    return False

label Town2ToInn(play_event = True, trigger = None): # event
    if is_erased("Town2ToInn"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2ToInnBase", "Town2ToInn") from _call_Town2ToInn_PlayEvent
        return (1, "", "Town2ToInn")
    return None

label Town2ToRiverBase:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_Town2EV004_PlaySound
    call TransferPlayer("River", "Town2EV004", 0, 8, direction=6) from _call_Town2EV004_TransferPlayer
    $ resolve_scene()
    return False

label Town2ToRiver(play_event = True, trigger = None): # event
    if is_erased("Town2ToRiver"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2ToRiverBase", "Town2ToRiver") from _call_Town2ToRiver_PlayEvent
        return (0, "", "Town2ToRiver")
    return None

label Town2ToRiver_v2Base:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_Town2EV005_PlaySound
    call TransferPlayer("River", "Town2EV005", 0, 9, direction=6) from _call_Town2EV005_TransferPlayer
    $ resolve_scene()
    return False

label Town2ToRiver_v2(play_event = True, trigger = None): # event
    if is_erased("Town2ToRiver_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2ToRiver_v2Base", "Town2ToRiver_v2") from _call_Town2ToRiver_v2_PlayEvent
        return (0, "", "Town2ToRiver_v2")
    return None

label Town2CorruptionCounterBase:
    "CORRUPTION COUNTER"
    if corruption == 0:
        $ resolve_scene()
        "CORRUPTION POINTS: 0"
    if corruption == 1:
        "CORRUPTION POINTS: 1"
    if corruption == 2:
        "CORRUPTION POINTS: 2"
    if corruption == 3:
        "CORRUPTION POINTS: 3"
    if corruption == 4:
        "CORRUPTION POINTS: 4"
    if corruption == 5:
        "CORRUPTION POINTS: 5"
    if corruption == 6:
        "CORRUPTION POINTS: 6"
    if corruption == 7:
        "CORRUPTION POINTS: 7"
    if corruption == 8:
        "CORRUPTION POINTS: 8"
    if corruption == 9:
        "CORRUPTION POINTS: 9"
    if corruption == 10:
        "CORRUPTION POINTS: 10"
    if corruption == 11:
        "CORRUPTION POINTS: 11"
    if corruption == 12:
        "CORRUPTION POINTS: 12"
    if corruption == 13:
        "CORRUPTION POINTS: 13"
    if corruption == 14:
        "CORRUPTION POINTS: 14"
    if corruption == 15:
        "CORRUPTION POINTS: 15"
    $ resolve_scene()
    return False

label Town2CorruptionCounter(play_event = True, trigger = None): # event
    if is_erased("Town2CorruptionCounter"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2CorruptionCounterBase", "Town2CorruptionCounter") from _call_Town2CorruptionCounter_PlayEvent
        return (1, "", "Town2CorruptionCounter")
    return None

label Town2MapBase:
    "River -> Festival <- Hot springs <- Coal mine <-"
    return False

label Town2Map(play_event = True, trigger = None): # event
    if is_erased("Town2Map"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2MapBase", "Town2Map") from _call_Town2Map_PlayEvent
        return (1, "", "Town2Map")
    return None

label Town2ToBar2Base:
    call PlaySound("sound", "audio/Open1.ogg", volume=0.9, no_loop=True) from _call_Town2EV008_PlaySound
    call Movement("Town2EV008", "Town2EV008", ["TURN_L",["WAIT",3],"TURN_R",["WAIT",3],"TURN_U","THROUGH_ON"]) from _call_Town2EV008_Movement
    call Movement("Town2EV008", "player", ["FORWARD"]) from _call_Town2EV008_Movement_1
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_Town2EV008_PlaySound_1
    call TransferPlayer("Bar2", "Town2EV008", 8, 12, direction=8) from _call_Town2EV008_TransferPlayer
    $ resolve_scene()
    return False

label Town2ToBar2(play_event = True, trigger = None): # event
    if is_erased("Town2ToBar2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2ToBar2Base", "Town2ToBar2") from _call_Town2ToBar2_PlayEvent
        return (1, "", "Town2ToBar2")
    return None

label Town2ToFoodStoreBase:
    call PlaySound("sound", "audio/Open1.ogg", volume=0.9, no_loop=True) from _call_Town2EV009_PlaySound
    call Movement("Town2EV009", "Town2EV009", ["TURN_L",["WAIT",3],"TURN_R",["WAIT",3],"TURN_U","THROUGH_ON"]) from _call_Town2EV009_Movement
    call Movement("Town2EV009", "player", ["FORWARD"]) from _call_Town2EV009_Movement_1
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_Town2EV009_PlaySound_1
    call TransferPlayer("FoodStore", "Town2EV009", 10, 8, direction=4) from _call_Town2EV009_TransferPlayer
    $ resolve_scene()
    return False

label Town2ToFoodStore(play_event = True, trigger = None): # event
    if is_erased("Town2ToFoodStore"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2ToFoodStoreBase", "Town2ToFoodStore") from _call_Town2ToFoodStore_PlayEvent
        return (1, "", "Town2ToFoodStore")
    return None

label Town2ToFoodStore_v2Base:
    call PlaySound("sound", "audio/Open1.ogg", volume=0.9, no_loop=True) from _call_Town2EV010_PlaySound
    call Movement("Town2EV010", "Town2EV010", ["TURN_L",["WAIT",3],"TURN_R",["WAIT",3],"TURN_U","THROUGH_ON"]) from _call_Town2EV010_Movement
    call Movement("Town2EV010", "player", ["FORWARD"]) from _call_Town2EV010_Movement_1
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_Town2EV010_PlaySound_1
    call TransferPlayer("FoodStore", "Town2EV010", 10, 7, direction=4) from _call_Town2EV010_TransferPlayer
    $ resolve_scene()
    return False

label Town2ToFoodStore_v2(play_event = True, trigger = None): # event
    if is_erased("Town2ToFoodStore_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2ToFoodStore_v2Base", "Town2ToFoodStore_v2") from _call_Town2ToFoodStore_v2_PlayEvent
        return (1, "", "Town2ToFoodStore_v2")
    return None

label Town2ToClothingStoreBase:
    call PlaySound("sound", "audio/Open1.ogg", volume=0.9, no_loop=True) from _call_Town2EV011_PlaySound
    call Movement("Town2EV011", "Town2EV011", ["TURN_L",["WAIT",3],"TURN_R",["WAIT",3],"TURN_U","THROUGH_ON"]) from _call_Town2EV011_Movement
    call Movement("Town2EV011", "player", ["FORWARD"]) from _call_Town2EV011_Movement_1
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_Town2EV011_PlaySound_1
    call TransferPlayer("ClothingStore", "Town2EV011", 9, 7, direction=4) from _call_Town2EV011_TransferPlayer
    $ resolve_scene()
    return False

label Town2ToClothingStore(play_event = True, trigger = None): # event
    if is_erased("Town2ToClothingStore"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2ToClothingStoreBase", "Town2ToClothingStore") from _call_Town2ToClothingStore_PlayEvent
        return (1, "", "Town2ToClothingStore")
    return None

label Town2ToHouseInteriorBase:
    call PlaySound("sound", "audio/Open1.ogg", volume=0.9, no_loop=True) from _call_Town2EV012_PlaySound
    call Movement("Town2EV012", "Town2EV012", ["TURN_L",["WAIT",3],"TURN_R",["WAIT",3],"TURN_U","THROUGH_ON"]) from _call_Town2EV012_Movement
    call Movement("Town2EV012", "player", ["FORWARD"]) from _call_Town2EV012_Movement_1
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_Town2EV012_PlaySound_1
    call TransferPlayer("HouseInterior", "Town2EV012", 4, 12, direction=0) from _call_Town2EV012_TransferPlayer
    $ resolve_scene()
    return False

label Town2ToHouseInterior(play_event = True, trigger = None): # event
    if is_erased("Town2ToHouseInterior"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2ToHouseInteriorBase", "Town2ToHouseInterior") from _call_Town2ToHouseInterior_PlayEvent
        return (1, "", "Town2ToHouseInterior")
    return None

label Town2SeemsItsClosedBase:
    "Seems it's closed"
    return False

label Town2SeemsItsClosed(play_event = True, trigger = None): # event
    if is_erased("Town2SeemsItsClosed"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2SeemsItsClosedBase", "Town2SeemsItsClosed") from _call_Town2SeemsItsClosed_PlayEvent
        return (1, "", "Town2SeemsItsClosed")
    return None

label Town2NPCWorkersSon_0:
    $ elder_festival = 3
    $ resolve_scene()
    Johan "Hey boy!"
    Leyna "Your father sent us for the tools bag, he is waiting for you at the entrance of the festival.."
    $ resolve_scene()
    WorkersSon "Shit.. I went out last night and I haven't slept at all. He is very angry?"
    Johan "He looked angry. He has asked us to find you to collect the bag, so he can finish the job so, where is it?"
    WorkersSon "Sorry.. it's tight he-..."
    call Movement("Town2EV014_0", "Town2EV014", [["JUMP",0,0]]) from _call_Town2EV014_0_Movement
    $ resolve_scene()
    WorkersSon "Oh no! Where is the bag?"
    Leyna "What's wrong?"
    WorkersSon "I must have forgotten it at the grocery store, when I went to buy the last beer"
    Johan "It's okay. We know where the store is, we will go get them, and we will take them to your father"
    WorkersSon "Thank you so much. And please, if he asks you, just tell him that I was having lunch..."
    Johan "It's okay boy, don't worry"
    $ elder_festival = 4
    return False

label Town2NPCWorkersSon_1:
    WorkersSon "Sorry for the inconvenience"
    return False

label Town2NPCWorkersSon(play_event = True, trigger = None): # event
    if is_erased("Town2NPCWorkersSon"):
        return None
    elif elder_festival >= 5:
        return None
    elif trigger == "event" and elder_festival >= 4:
        call PlayEvent(play_event, "Town2NPCWorkersSon_1", "Town2NPCWorkersSon") from _call_Town2NPCWorkersSon_1_PlayEvent
        return (1, "", "Town2NPCWorkersSon_1")
    elif trigger == "event" and elder_festival >= 1:
        call PlayEvent(play_event, "Town2NPCWorkersSon_0", "Town2NPCWorkersSon") from _call_Town2NPCWorkersSon_0_PlayEvent
        return (1, "", "Town2NPCWorkersSon_0")
    return None

label Town2CastlePosterBase:
    "Closed for restoration."
    return False

label Town2CastlePoster(play_event = True, trigger = None): # event
    if is_erased("Town2CastlePoster"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2CastlePosterBase", "Town2CastlePoster") from _call_Town2CastlePoster_PlayEvent
        return (1, "", "Town2CastlePoster")
    return None

label Town2CastlePoster_v2Base:
    "Closed for restoration."
    return False

label Town2CastlePoster_v2(play_event = True, trigger = None): # event
    if is_erased("Town2CastlePoster_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2CastlePoster_v2Base", "Town2CastlePoster_v2") from _call_Town2CastlePoster_v2_PlayEvent
        return (1, "", "Town2CastlePoster_v2")
    return None

label Town2MeetPhotographer_0:
    call Movement("Town2MeetPhotographer_0", "Town2fotografo", [["JUMP",0,0]]) from _call_Town2MeetPhotographer_0_Movement
    $ resolve_scene()
    call PauseForBalloon("Town2MeetPhotographer_0") from _call_Town2MeetPhotographer_0_PauseForBalloon
    OldMan "HEY LEYNA!"
    Johan "Do you know this man?"
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Emmm..."
    call Movement("Town2MeetPhotographer_0", "Town2fotografo", ["D","D","D"]) from _call_Town2MeetPhotographer_0_Movement_1
    $ resolve_scene()
    OldMan "Leyna! Great news, the magazine is delighted with the photos and they cannot wait for the next session"
    $ erase_picture(1)
    $ show_transparent(2, "plano_mujer_timida", width=1600, height=900)
    $ resolve_scene()
    Leyna "...!"
    OldMan "We are doing a spectacular job ... Oh! Sorry, I didn't see you. Are you Leyna's husband?"
    Johan "Yes, and you are...?"
    OldMan "I'm the town's photographer"
    OldMan "Well, I won't bother you more, I'll be here as always. Speak to me so we can start with the session"
    $ erase_picture(2)
    call Movement("Town2MeetPhotographer_0", "Town2fotografo", ["U","U","U","TURN_D"]) from _call_Town2MeetPhotographer_0_Movement_2
    $ resolve_scene()
    call PauseForBalloon("Town2MeetPhotographer_0") from _call_Town2MeetPhotographer_0_PauseForBalloon_1
    Johan "The next session?... What's this, Leyna?"
    Leyna "Well... He offered me a job as a model and how we are doing so badly... I accepted it"
    Johan "What kind of modelling?"
    Leyna "Swimsuits and lingerie"
    Johan "Lingerie? I ... I understand Leyna, but why you haven't talked to me about it before?"
    Leyna "Sorry, it was yesterday and it was so fast ... I didn't want to bother you knowing that you were interviewing people"
    Johan "I have no problem looking for alternative sources of income, but posing in lingerie?..."
    "...You just met that man in this town lost in the middle of nowhere, I don't feel comfortable knowing that you're going to be half-naked alone with him..."
    "... I would like to be present at the next photoshoot and see what happens with my own eyes..."
    Leyna "I get it, thanks for supporting me on this Johan"
    $ set_switch("johan_photo", True)
    return False

label Town2MeetPhotographer(play_event = True, trigger = None): # event
    if is_erased("Town2MeetPhotographer"):
        return None
    elif switch("johan_photo"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2MeetPhotographer_0", "Town2MeetPhotographer") from _call_Town2MeetPhotographer_0_PlayEvent
        return (0, "", "Town2MeetPhotographer_0")
    return None

label Town2EV018_0:
    label Town2EV018_0_loop_1:
        $ resolve_scene()
        call PauseForBalloon("Town2EV018_0") from _call_Town2EV018_0_PauseForBalloon
        # jump Town2EV018_0_loop_1
    label Town2EV018_0_loop_1_end:
        pass
    $ elder_festival = 3
    $ resolve_scene()
    return False

label Town2EV018(play_event = True, trigger = None): # None-only parallel
    if is_erased("Town2EV018"):
        return None
    elif elder_festival >= 3:
        return None
    elif trigger == "parallel" and elder_festival >= 2:
        return None # Town2EV018_0 potentially infinite looping parallel
    return None

label Town2ToRiverEvent_0:
    Johan "We don't need to go back there for now."
    call Movement("Town2ToRiverEvent_0", "player", ["TURN_L","L"]) from _call_Town2ToRiverEvent_0_Movement
    $ resolve_scene()
    return False

label Town2ToRiverEvent_1(menu_choice = None):
    Johan "I don't know if I want to go in there, you know they force us to go naked... and I don't like the idea of them seeing you naked"
    Leyna "Well... since we arrived, they have already seen me naked, right? just because they see me again shouldn't be a problem"
    Johan "I guess you're right... but I guess I still don't like the idea of them seeing you naked, you're my wife"
    Leyna "You are right... I leave it up to you"
    call GetChoice([_("Enter the river"), _("I'm not ready")], value=menu_choice, called_from="Town2ToRiverEvent_1") from _call_Town2ToRiverEvent_1_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Enter the river"):
        $ menu_choice = None
        $ set_switch("river_3", True)
        call GalleryViewed("riosexo") from _call_Town2ToRiverEvent_1_GalleryViewed
        $ v0_7_3 = 1
        $ resolve_scene()
        Johan "Well, whatever, I guess it doesn't matter so much if they see our naked bodies... we are both adults and this is something natural"
        Leyna "Yes, you are right"
        $ fade_out()
        $ show_picture(1, "riosexo1")
        $ fade_in()
        $ resolve_scene()
        Alexa "Hey! you finally came! I didn't know if you would come with how reserved you are about your bodies!"
        Johan "Reserved... (Well, I guess from her point of view it may seem so, although I think she is just too... open about it)"
        Leyna "Yes... I'm still not used to it, but with Johan here I feel more relaxed"
        Alexa "Great! Well, you know Johan, stay close to your wife hehehehehe"
        Alexa "Come and have a beer with us!"
        "Leyna. M-more beer? "
        Johan "I don't know how you can keep drinking, we've practically been partying for days"
        Alexa "Oh come on, don't overreact!"
        Alexa "Come on, take one!"
        Johan "Okay... but just one"
        $ show_picture(2, "riosexo2")
        $ resolve_scene()
        Johan "Well... I have to admit that you are right Alexa, with a couple of shots of beer I already feel much better"
        Alexa "I told you so! Between the beer and being naked here, one's spirits are raised no matter how bad one feels"
        pause
        $ show_picture(3, "riosexo3")
        $ resolve_scene()
        Villager "Hey! how are you guys? I haven't seen you for a couple of days..."
        Leyna "He-hello"
        Johan "Hey... hmmm How's it going?"
        Villager "Here we are, having a beer by the river, enjoying the holidays before the routine starts again"
        pause
        $ show_picture(4, "riosexo4")
        $ resolve_scene()
        Johan "(His penis is rubbing Leyna...) I see, I can't imagine this town living a normal life, does it change much when the festival is over?"
        Villager "Yes! too much, I wish it was like this all year round, but the truth is that once the festival is over, life here is normal and ordinary"
        Villager "I guess when the festival starts everyone goes a little crazy hahahaha"
        Leyna "Let's take a bath Johan"
        Johan "Oh, sure, it'll come in handy in this hot weather"
        Villager "Yeah! see you later! have fun, guys!"
        pause
        $ fade_out()
        $ show_picture(5, "riosexo5")
        $ fade_in()
        $ resolve_scene()
        Johan "Who was that guy?"
        Leyna "... I don't know, it's a little difficult for me to differentiate the people of this town, we have met so many in the last few days..."
        Johan "Hahahaha you can say that again... I'm glad I'm not the only one"
        $ show_picture(6, "riosexo6")
        $ resolve_scene()
        Johan "Alexa... she always seems to be very comfortable naked and surrounded by guys... didn't she come to town with her husband?"
        Johan "I haven't seen him for days... I don't know what he will think of all this"
        Leyna "!!!... yeah... I guess they have some kind of open relationship... or so I hope"
        Johan "Yeah... I'm not so sure about that but okay...."
        Johan "Poor guy..."
        Leyna "!!!!... Y-yes"
        pause
        $ show_picture(7, "riosexo7")
        $ resolve_scene()
        Johan "Oh there you go... I knew something like this was about to happen"
        Johan "They're not going to do it in front of everyone, are they?"
        $ show_picture(8, "riosexo8")
        $ resolve_scene()
        Leyna "I-I don't know... I don't think so, right?"
        Johan "After everything I've seen, nothing surprises me anymore"
        pause
        $ show_picture(9, "riosexo9")
        $ resolve_scene()
        Johan "!!! (they are doing it in front of everyone)"
        Leyna "..."
        Leyna "(I-I'm starting to get horny watching this, I hope Johan doesn't notice....)"
        pause
        $ show_picture(10, "riosexo10")
        $ resolve_scene()
        Johan "(Fuck, they're not disguising shit, I'm embarrassed but I can't stop looking)"
        Johan "(Besides, I have it hard as a rock, I can't get out of the water like this)"
        Johan "(Although Leyna... hold on a second...)"
        Johan "(Leyna is red as a tomato... she seems to be very horny... I didn't know she liked this kind of things)"
        Johan "(Wait a minute... is she touching herself? I can't help but get even more excited seeing my wife like that...)"
        Johan "(... I can't help it... I must take advantage of this situation)"
        $ show_picture(11, "riosexo11")
        $ resolve_scene()
        Leyna "!!!!"
        Johan "Let me give you a hand with that...."
        Leyna "Johan..."
        pause
        $ show_picture(12, "riosexo12")
        $ resolve_scene()
        Leyna "Hmmmfff!"
        Johan "You sure are horny... you're on fire"
        Leyna "J-Johan!"
        Johan "Let me help you with that"
        Leyna "aaahh..."
        pause
        $ show_picture(13, "riosexo13")
        $ resolve_scene()
        Leyna "Johan... fuck me..."
        Johan "Here?.... very well, but let's try to disguise it a little bit"
        Leyna "Let me get on top..."
        $ show_picture(14, "riosexo14")
        $ resolve_scene()
        Johan "Oh!"
        Johan "I can see you were looking forward to it"
        Johan "God... you are so hot down there"
        Leyna "Ah... shut up and fuck me"
        Johan "Yeah..."
        $ show_picture(15, "riosexo17")
        $ resolve_scene()
        Leyna "Hmmmf... ahh"
        Johan "Ssshhhh shut up or they will hear us..."
        Leyna "I-I don't care... I don't care if they can hear us, just fuck me"
        if johan_leyna_sex == 1:
            $ resolve_scene()
            Leyna "(Johan... he's feeling a bit weird... since the other day when we did it he got a bit nervous... now he's a bit clumsy)"
            Leyna "(I'm barely enjoying it...)"
            Leyna "F-faster..."
            Johan "I'm trying... there are so many people around"
            Johan "(I can't concentrate... I can't get out of my head everything that has been going on these last few days)"
            Leyna "(My God... he is doing terrible... what is happening to Johan lately? has he changed?... or is it me that has changed?)"
            pause
            $ show_picture(16, "riosexo18")
            $ resolve_scene()
            Villager "Hey... I see you need a hand"
            Leyna "Wait"
            Johan "???"
            Villager "Come on, I know you're looking forward to it, doing something like that in front of everybody"
            pause
            $ show_picture(17, "riosexo19")
            call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2ToRiverEvent_1_PlaySound
            $ resolve_scene()
            Johan "!!! what's going on? (I can't see anything from here... there's someone next to us?)"
            Leyna "Aghghgagagh!"
            Villager "Like this! I want to feel your tonsils!"
            Johan "(Wait, that sound! There's a guy sticking his dick in Leyna's mouth! While I'm here fucking her!)"
            Johan "H-hey! ... oh my god"
            $ show_picture(18, "riosexo20")
            $ resolve_scene()
            Johan "(L-Leyna's pussy is convulsing, she looks like she's about to have an orgasm right now! Holy cow it feels so good.... )"
            Johan "F-fuck!!"
            Johan "(H-he's fucking me! Leyna is moving like crazy!... FUCK!i'm going to cum! b-but there's a guy right there rubbing his dick in Leyna's mouth!)"
            Johan "(Shit, I can't take it anymore! I'm coming!)"
            Johan "AAHHH!"
            Leyna "(J-johan just cum? right now? while all this is going on?)"
            Johan "Ah ah ah!"
            pause
            $ show_picture(19, "riosexo21")
            $ resolve_scene()
            Johan "(Wait! There's really a guy here!)"
            Johan "H-Hey! get off of my wife right now Get out!"
            Villager "Oh come on, I'm about to finish"
            Johan "I told you to get out! get out now!"
            pause
            stop bgs fadeout 1
            $ show_picture(20, "riosexo22")
            $ resolve_scene()
            Villager "TCh! fuck man! ok ok, I'm leaving, next time don't fuck in public if you don't want someone else to join the party."
            Johan "Leave!"
            Villager "I'm leaving... I'll catch you around, honey"
            Leyna "Ah ah ah!"
            pause
            $ show_picture(21, "riosexo23")
            $ resolve_scene()
            Johan "What a waste of time... come on, let's go..."
            Leyna "Y-yes (waste of time? but you just cummed inside me... you came so fast... were you liking it johan?)"
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
            $ erase_picture(19)
            $ erase_picture(20)
            $ erase_picture(21)
            call TransferPlayer("Town2", "Town2ToRiverEvent_1", 37, 23, direction=4) from _call_Town2ToRiverEvent_1_TransferPlayer
            $ fade_in()
            call Movement("Town2ToRiverEvent_1", "player", ["L","L","L"]) from _call_Town2ToRiverEvent_1_Movement
            call PlaySound("sound", "audio/Computer.ogg", volume=0.9, no_loop=True) from _call_Town2ToRiverEvent_1_PlaySound_1
            $ resolve_scene()
            call PauseForBalloon("Town2ToRiverEvent_1") from _call_Town2ToRiverEvent_1_PauseForBalloon
            Johan "!!! Was that your cell phone?"
            Leyna "Yes... Let's see...."
            Leyna "It's the photographer... he says he needs to see us right away"
            Johan "The photographer... (that guy again...)"
            Johan "Sure, let's see what he wants"
        if johan_leyna_sex == 2:
            $ show_picture(16, "riosexo16")
            call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2ToRiverEvent_1_PlaySound_2
            $ resolve_scene()
            Leyna "Oh!"
            Leyna "(My God, J-Johan is fucking me like that day...)"
            Leyna "M-my God... if you keep this up I-I'm going to cum..."
            Johan "Perfect! cum, that's what I want"
            Leyna "Ah.... hmmm...."
            pause
            $ show_picture(17, "riosexo18")
            $ resolve_scene()
            Villager "Hey guys, I see you're having a good time"
            Leyna "Hmmff?"
            Villager "Doing this here, I guess you want me to give you a hand, don't you?"
            Leyna "(Dios mio casi me la mete en la boca sin avisar)"
            stop bgs fadeout 1
            Johan "Hey! What the hell are you doing! Get out of the way right now!"
            Villager "D-don't you want some help?"
            Johan "N-no, we're fine, man, thanks, but back off, we'll take care of it ourselves"
            Villager "Since you were here doing it in front of the whole world I thought that..."
            Johan "You thought wrong"
            Villager "Okay guys, sorry"
            $ fade_out()
            $ show_picture(18, "riosexo24")
            $ fade_in()
            $ resolve_scene()
            Leyna "Ah ah ah...."
            Leyna "Shall we continue?"
            Johan "Hehehehe Do you want to continue?"
            Leyna "Y-yes..."
            Johan "Then we continue"
            pause
            $ fade_out()
            $ show_picture(19, "riosexo25")
            call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2ToRiverEvent_1_PlaySound_3
            $ fade_in()
            $ resolve_scene()
            "Minutes later"
            Leyna "Ah! ah! ah! M-my God... I'm cumming!"
            Johan "That's the way I like it, cum! come on! I want to see you writhing with pleasure!"
            Leyna "Ah ah! ah m-my god... so fast! you're drilling me"
            Johan "Ah! ah ah ah!"
            Leyna "Ooohh!!! ahh!!"
            Villager "(whispering) Jesus Christ, it didn't look like it but that guy is a fucking machine... now I understand why she's with him"
            Villager2 "(whispering) who would have thought..."
            Johan "That's how I like it"
            pause
            $ fade_out()
            stop bgs fadeout 1
            $ show_picture(20, "riosexo26")
            $ fade_in()
            $ resolve_scene()
            Leyna "I-I see that you've cum too..."
            Johan "hahahaha yes, I couldn't help it"
            Johan "!!!!"
            Johan "Shit, everyone is watching us, let's get out of here and take a nice hot shower"
            Leyna "Yes, good idea"
            "Leyna. (My God I'm still shaking... it's going to be hard for me to get up... what a fuck he has given me... Johan has improved since we arrived)"
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
            $ erase_picture(19)
            $ erase_picture(20)
            call TransferPlayer("Town2", "Town2ToRiverEvent_1", 37, 23, direction=4) from _call_Town2ToRiverEvent_1_TransferPlayer_1
            $ fade_in()
            call Movement("Town2ToRiverEvent_1", "player", ["L","L","L"]) from _call_Town2ToRiverEvent_1_Movement_1
            call PlaySound("sound", "audio/Computer.ogg", volume=0.9, no_loop=True) from _call_Town2ToRiverEvent_1_PlaySound_4
            $ resolve_scene()
            call PauseForBalloon("Town2ToRiverEvent_1") from _call_Town2ToRiverEvent_1_PauseForBalloon_1
            Johan "!!! was that your cell phone?"
            Leyna "Yes... let's see...."
            Leyna "It's the photographer... he says he needs to see us right away"
            Johan "The photographer... (that guy again...)"
            Johan "Sure, let's see what he wants"
    elif menu_choice == _("I'm not ready"):
        $ menu_choice = None
        $ resolve_scene()
        Johan "I'm sorry but I don't feel comfortable about this situation"
        "Leyna.{p}.. Sure, it makes sense, if you change your mind they will be on the river all day so we can come back whenever you want"
        Johan "Yeah..."
        call Movement("Town2ToRiverEvent_1", "player", ["L","L"]) from _call_Town2ToRiverEvent_1_Movement_2
    $ resolve_scene()
    return False

label Town2ToRiverEvent_2:
    Johan "We don't need to go back there for now."
    call Movement("Town2ToRiverEvent_2", "player", ["TURN_L","L"]) from _call_Town2ToRiverEvent_2_Movement
    $ resolve_scene()
    return False

label Town2ToRiverEvent(play_event = True, trigger = None): # event
    if is_erased("Town2ToRiverEvent"):
        return None
    elif trigger == "event" and switch("river_3"):
        call PlayEvent(play_event, "Town2ToRiverEvent_2", "Town2ToRiverEvent") from _call_Town2ToRiverEvent_2_PlayEvent
        return (0, "", "Town2ToRiverEvent_2")
    elif trigger == "event" and switch("party_at_festival"):
        call PlayEvent(play_event, "Town2ToRiverEvent_1", "Town2ToRiverEvent") from _call_Town2ToRiverEvent_1_PlayEvent
        return (0, "", "Town2ToRiverEvent_1")
    elif trigger == "event" and switch("third_day"):
        call PlayEvent(play_event, "Town2ToRiverEvent_0", "Town2ToRiverEvent") from _call_Town2ToRiverEvent_0_PlayEvent
        return (0, "", "Town2ToRiverEvent_0")
    return None

label Town2ToRiverEvent_v2_0:
    Johan "We don't need to go back there for now."
    call Movement("Town2ToRiverEvent_v2_0", "player", ["TURN_L","L"]) from _call_Town2ToRiverEvent_v2_0_Movement
    $ resolve_scene()
    return False

label Town2ToRiverEvent_v2_1(menu_choice = None):
    Johan "I don't know if I want to go in there, you know they force us to go naked... and I don't like the idea of them seeing you naked"
    Leyna "Well... since we arrived, they have already seen me naked, right? just because they see me again shouldn't be a problem"
    Johan "I guess you're right... but I guess I still don't like the idea of them seeing you naked, you're my wife"
    Leyna "You are right... I leave it up to you"
    call GetChoice([_("Enter the river"), _("I'm not ready")], value=menu_choice, called_from="Town2ToRiverEvent_v2_1") from _call_Town2ToRiverEvent_v2_1_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Enter the river"):
        $ menu_choice = None
        $ set_switch("river_3", True)
        call GalleryViewed("riosexo") from _call_Town2ToRiverEvent_v2_1_GalleryViewed
        $ v0_7_3 = 1
        $ resolve_scene()
        Johan "Well, whatever, I guess it doesn't matter so much if they see our naked bodies... we are both adults and this is something natural"
        Leyna "Yes, you are right"
        $ fade_out()
        $ show_picture(1, "riosexo1")
        $ fade_in()
        $ resolve_scene()
        Alexa "Hey! you finally came! I didn't know if you would come with how reserved you are about your bodies!"
        Johan "Reserved... (Well, I guess from her point of view it may seem so, although I think she is just too... open about it)"
        Leyna "Yes... I'm still not used to it, but with Johan here I feel more relaxed"
        Alexa "Great! Well, you know Johan, stay close to your wife hehehehehe"
        Alexa "Come and have a beer with us!"
        "Leyna. M-more beer? "
        Johan "I don't know how you can keep drinking, we've practically been partying for days"
        Alexa "Oh come on, don't overreact!"
        Alexa "Come on, take one!"
        Johan "Okay... but just one"
        $ show_picture(2, "riosexo2")
        $ resolve_scene()
        Johan "Well... I have to admit that you are right Alexa, with a couple of shots of beer I already feel much better"
        Alexa "I told you so! Between the beer and being naked here, one's spirits are raised no matter how bad one feels"
        pause
        $ show_picture(3, "riosexo3")
        $ resolve_scene()
        Villager "Hey! how are you guys? I haven't seen you for a couple of days..."
        Leyna "He-hello"
        Johan "Hey... hmmm How's it going?"
        Villager "Here we are, having a beer by the river, enjoying the holidays before the routine starts again"
        pause
        $ show_picture(4, "riosexo4")
        $ resolve_scene()
        Johan "(His penis is rubbing Leyna...) I see, I can't imagine this town living a normal life, does it change much when the festival is over?"
        Villager "Yes! too much, I wish it was like this all year round, but the truth is that once the festival is over, life here is normal and ordinary"
        Villager "I guess when the festival starts everyone goes a little crazy hahahaha"
        Leyna "Let's take a bath Johan"
        Johan "Oh, sure, it'll come in handy in this hot weather"
        Villager "Yeah! see you later! have fun, guys!"
        pause
        $ fade_out()
        $ show_picture(5, "riosexo5")
        $ fade_in()
        $ resolve_scene()
        Johan "Who was that guy?"
        Leyna "... I don't know, it's a little difficult for me to differentiate the people of this town, we have met so many in the last few days..."
        Johan "Hahahaha you can say that again... I'm glad I'm not the only one"
        $ show_picture(6, "riosexo6")
        $ resolve_scene()
        Johan "Alexa... she always seems to be very comfortable naked and surrounded by guys... didn't she come to town with her husband?"
        Johan "I haven't seen him for days... I don't know what he will think of all this"
        Leyna "!!!... yeah... I guess they have some kind of open relationship... or so I hope"
        Johan "Yeah... I'm not so sure about that but okay...."
        Johan "Poor guy..."
        Leyna "!!!!... Y-yes"
        pause
        $ show_picture(7, "riosexo7")
        $ resolve_scene()
        Johan "Oh there you go... I knew something like this was about to happen"
        Johan "They're not going to do it in front of everyone, are they?"
        $ show_picture(8, "riosexo8")
        $ resolve_scene()
        Leyna "I-I don't know... I don't think so, right?"
        Johan "After everything I've seen, nothing surprises me anymore"
        pause
        $ show_picture(9, "riosexo9")
        $ resolve_scene()
        Johan "!!! (they are doing it in front of everyone)"
        Leyna "..."
        Leyna "(I-I'm starting to get horny watching this, I hope Johan doesn't notice....)"
        pause
        $ show_picture(10, "riosexo10")
        $ resolve_scene()
        Johan "(Fuck, they're not disguising shit, I'm embarrassed but I can't stop looking)"
        Johan "(Besides, I have it hard as a rock, I can't get out of the water like this)"
        Johan "(Although Leyna... hold on a second...)"
        Johan "(Leyna is red as a tomato... she seems to be very horny... I didn't know she liked this kind of things)"
        Johan "(Wait a minute... is she touching herself? I can't help but get even more excited seeing my wife like that...)"
        Johan "(... I can't help it... I must take advantage of this situation)"
        $ show_picture(11, "riosexo11")
        $ resolve_scene()
        Leyna "!!!!"
        Johan "Let me give you a hand with that...."
        Leyna "Johan..."
        pause
        $ show_picture(12, "riosexo12")
        $ resolve_scene()
        Leyna "Hmmmfff!"
        Johan "You sure are horny... you're on fire"
        Leyna "J-Johan!"
        Johan "Let me help you with that"
        Leyna "aaahh..."
        pause
        $ show_picture(13, "riosexo13")
        $ resolve_scene()
        Leyna "Johan... fuck me..."
        Johan "Here?.... very well, but let's try to disguise it a little bit"
        Leyna "Let me get on top..."
        $ show_picture(14, "riosexo14")
        $ resolve_scene()
        Johan "Oh!"
        Johan "I can see you were looking forward to it"
        Johan "God... you are so hot down there"
        Leyna "Ah... shut up and fuck me"
        Johan "Yeah..."
        $ show_picture(15, "riosexo17")
        $ resolve_scene()
        Leyna "Hmmmf... ahh"
        Johan "Ssshhhh shut up or they will hear us..."
        Leyna "I-I don't care... I don't care if they can hear us, just fuck me"
        if johan_leyna_sex == 1:
            $ resolve_scene()
            Leyna "(Johan... he's feeling a bit weird... since the other day when we did it he got a bit nervous... now he's a bit clumsy)"
            Leyna "(I'm barely enjoying it...)"
            Leyna "F-faster..."
            Johan "I'm trying... there are so many people around"
            Johan "(I can't concentrate... I can't get out of my head everything that has been going on these last few days)"
            Leyna "(My God... he is doing terrible... what is happening to Johan lately? has he changed?... or is it me that has changed?)"
            pause
            $ show_picture(16, "riosexo18")
            $ resolve_scene()
            Villager "Hey... I see you need a hand"
            Leyna "Wait"
            Johan "???"
            Villager "Come on, I know you're looking forward to it, doing something like that in front of everybody"
            pause
            $ show_picture(17, "riosexo19")
            call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2ToRiverEvent_v2_1_PlaySound
            $ resolve_scene()
            Johan "!!! what's going on? (I can't see anything from here... there's someone next to us?)"
            Leyna "Aghghgagagh!"
            Villager "Like this! I want to feel your tonsils!"
            Johan "(Wait, that sound! There's a guy sticking his dick in Leyna's mouth! While I'm here fucking her!)"
            Johan "H-hey! ... oh my god"
            $ show_picture(18, "riosexo20")
            $ resolve_scene()
            Johan "(L-Leyna's pussy is convulsing, she looks like she's about to have an orgasm right now! Holy cow it feels so good.... )"
            Johan "F-fuck!!"
            Johan "(H-he's fucking me! Leyna is moving like crazy!... FUCK!i'm going to cum! b-but there's a guy right there rubbing his dick in Leyna's mouth!)"
            Johan "(Shit, I can't take it anymore! I'm coming!)"
            Johan "AAHHH!"
            Leyna "(J-johan just cum? right now? while all this is going on?)"
            Johan "Ah ah ah!"
            pause
            $ show_picture(19, "riosexo21")
            $ resolve_scene()
            Johan "(Wait! There's really a guy here!)"
            Johan "H-Hey! get off of my wife right now Get out!"
            Villager "Oh come on, I'm about to finish"
            Johan "I told you to get out! get out now!"
            pause
            stop bgs fadeout 1
            $ show_picture(20, "riosexo22")
            $ resolve_scene()
            Villager "TCh! fuck man! ok ok, I'm leaving, next time don't fuck in public if you don't want someone else to join the party."
            Johan "Leave!"
            Villager "I'm leaving... I'll catch you around, honey"
            Leyna "Ah ah ah!"
            pause
            $ show_picture(21, "riosexo23")
            $ resolve_scene()
            Johan "What a waste of time... come on, let's go..."
            Leyna "Y-yes (waste of time? but you just cummed inside me... you came so fast... were you liking it johan?)"
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
            $ erase_picture(19)
            $ erase_picture(20)
            $ erase_picture(21)
            call TransferPlayer("Town2", "Town2ToRiverEvent_v2_1", 37, 23, direction=4) from _call_Town2ToRiverEvent_v2_1_TransferPlayer
            $ fade_in()
            call Movement("Town2ToRiverEvent_v2_1", "player", ["L","L","L"]) from _call_Town2ToRiverEvent_v2_1_Movement
            call PlaySound("sound", "audio/Computer.ogg", volume=0.9, no_loop=True) from _call_Town2ToRiverEvent_v2_1_PlaySound_1
            $ resolve_scene()
            call PauseForBalloon("Town2ToRiverEvent_v2_1") from _call_Town2ToRiverEvent_v2_1_PauseForBalloon
            Johan "!!! Was that your cell phone?"
            Leyna "Yes... Let's see...."
            Leyna "It's the photographer... he says he needs to see us right away"
            Johan "The photographer... (that guy again...)"
            Johan "Sure, let's see what he wants"
        if johan_leyna_sex == 2:
            $ show_picture(16, "riosexo16")
            call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2ToRiverEvent_v2_1_PlaySound_2
            $ resolve_scene()
            Leyna "Oh!"
            Leyna "(My God, J-Johan is fucking me like that day...)"
            Leyna "M-my God... if you keep this up I-I'm going to cum..."
            Johan "Perfect! cum, that's what I want"
            Leyna "Ah.... hmmm...."
            pause
            $ show_picture(17, "riosexo18")
            $ resolve_scene()
            Villager "Hey guys, I see you're having a good time"
            Leyna "Hmmff?"
            Villager "Doing this here, I guess you want me to give you a hand, don't you?"
            Leyna "(Dios mio casi me la mete en la boca sin avisar)"
            stop bgs fadeout 1
            Johan "Hey! What the hell are you doing! Get out of the way right now!"
            Villager "D-don't you want some help?"
            Johan "N-no, we're fine, man, thanks, but back off, we'll take care of it ourselves"
            Villager "Since you were here doing it in front of the whole world I thought that..."
            Johan "You thought wrong"
            Villager "Okay guys, sorry"
            $ fade_out()
            $ show_picture(18, "riosexo24")
            $ fade_in()
            $ resolve_scene()
            Leyna "Ah ah ah...."
            Leyna "Shall we continue?"
            Johan "Hehehehe Do you want to continue?"
            Leyna "Y-yes..."
            Johan "Then we continue"
            pause
            $ fade_out()
            $ show_picture(19, "riosexo25")
            call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2ToRiverEvent_v2_1_PlaySound_3
            $ fade_in()
            $ resolve_scene()
            "Minutes later"
            Leyna "Ah! ah! ah! M-my God... I'm cumming!"
            Johan "That's the way I like it, cum! come on! I want to see you writhing with pleasure!"
            Leyna "Ah ah! ah m-my god... so fast! you're drilling me"
            Johan "Ah! ah ah ah!"
            Leyna "Ooohh!!! ahh!!"
            Villager "(whispering) Jesus Christ, it didn't look like it but that guy is a fucking machine... now I understand why she's with him"
            Villager2 "(whispering) who would have thought..."
            Johan "That's how I like it"
            pause
            $ fade_out()
            stop bgs fadeout 1
            $ show_picture(20, "riosexo26")
            $ fade_in()
            $ resolve_scene()
            Leyna "I-I see that you've cum too..."
            Johan "hahahaha yes, I couldn't help it"
            Johan "!!!!"
            Johan "Shit, everyone is watching us, let's get out of here and take a nice hot shower"
            Leyna "Yes, good idea"
            "Leyna. (My God I'm still shaking... it's going to be hard for me to get up... what a fuck he has given me... Johan has improved since we arrived)"
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
            $ erase_picture(19)
            $ erase_picture(20)
            call TransferPlayer("Town2", "Town2ToRiverEvent_v2_1", 37, 23, direction=4) from _call_Town2ToRiverEvent_v2_1_TransferPlayer_1
            $ fade_in()
            call Movement("Town2ToRiverEvent_v2_1", "player", ["L","L","L"]) from _call_Town2ToRiverEvent_v2_1_Movement_1
            call PlaySound("sound", "audio/Computer.ogg", volume=0.9, no_loop=True) from _call_Town2ToRiverEvent_v2_1_PlaySound_4
            $ resolve_scene()
            call PauseForBalloon("Town2ToRiverEvent_v2_1") from _call_Town2ToRiverEvent_v2_1_PauseForBalloon_1
            Johan "!!! was that your cell phone?"
            Leyna "Yes... let's see...."
            Leyna "It's the photographer... he says he needs to see us right away"
            Johan "The photographer... (that guy again...)"
            Johan "Sure, let's see what he wants"
    elif menu_choice == _("I'm not ready"):
        $ menu_choice = None
        $ resolve_scene()
        Johan "I'm sorry but I don't feel comfortable about this situation"
        "Leyna.{p}.. Sure, it makes sense, if you change your mind they will be on the river all day so we can come back whenever you want"
        Johan "Yeah..."
        call Movement("Town2ToRiverEvent_v2_1", "player", ["L","L"]) from _call_Town2ToRiverEvent_v2_1_Movement_2
    $ resolve_scene()
    return False

label Town2ToRiverEvent_v2_2:
    Johan "We don't need to go back there for now."
    call Movement("Town2ToRiverEvent_v2_2", "player", ["TURN_L","L"]) from _call_Town2ToRiverEvent_v2_2_Movement
    $ resolve_scene()
    return False

label Town2ToRiverEvent_v2(play_event = True, trigger = None): # event
    if is_erased("Town2ToRiverEvent_v2"):
        return None
    elif trigger == "event" and switch("river_3"):
        call PlayEvent(play_event, "Town2ToRiverEvent_v2_2", "Town2ToRiverEvent_v2") from _call_Town2ToRiverEvent_v2_2_PlayEvent
        return (0, "", "Town2ToRiverEvent_v2_2")
    elif trigger == "event" and switch("party_at_festival"):
        call PlayEvent(play_event, "Town2ToRiverEvent_v2_1", "Town2ToRiverEvent_v2") from _call_Town2ToRiverEvent_v2_1_PlayEvent
        return (0, "", "Town2ToRiverEvent_v2_1")
    elif trigger == "event" and switch("third_day"):
        call PlayEvent(play_event, "Town2ToRiverEvent_v2_0", "Town2ToRiverEvent_v2") from _call_Town2ToRiverEvent_v2_0_PlayEvent
        return (0, "", "Town2ToRiverEvent_v2_0")
    return None

label Town2NPCCop_0:
    call Movement("Town2NPCCop_0", "player", ["U","R","TURN_U"]) from _call_Town2NPCCop_0_Movement
    $ resolve_scene()
    $ show_transparent(1, "expresion_ilusion_mujer", width=1600, height=900)
    $ resolve_scene()
    "OHHH!!"
    Leyna "How beautiful, it looks so medieval"
    $ erase_picture(1)
    $ resolve_scene()
    Johan "We should look for the inn and leave the luggage"
    call Movement("Town2NPCCop_0", "player", ["U","U","U","L","L","L","L"]) from _call_Town2NPCCop_0_Movement_1
    $ resolve_scene()
    Policeman "Good morning couple. I see that you are new in town"
    Johan "Yes, we came to the festival"
    Policeman "On these dates, we receive many tourists, although it's worth visiting the town at any time of the year"
    "Anyway, if you need anything, you can find me here"
    Johan "Since you mention it, can you tell us how to get to the inn?"
    Policeman "Sure, you have to go straight to the end of the town and turn right, there it is!"
    Johan "Okey, thanks"
    call TransferPlayer("Town", "Town2NPCCop_0", 26, 23, direction=6) from _call_Town2NPCCop_0_TransferPlayer
    call Movement("Town2NPCCop_0", "player", ["R","R","U","U"]) from _call_Town2NPCCop_0_Movement_2
    call TransferPlayer("Inn", "Town2NPCCop_0", 8, 11, direction=0) from _call_Town2NPCCop_0_TransferPlayer_1
    $ resolve_scene()
    return False

label Town2NPCCop_1:
    if not switch("leyna_alone"):
        $ resolve_scene()
        Policeman "Everything alright?"
    if switch("leyna_alone"):
        Policeman "This is a safe town. But just in case, the police station is on the top of this path"
    $ resolve_scene()
    return False

label Town2NPCCop(play_event = True, trigger = None): # event, autorun
    if is_erased("Town2NPCCop"):
        return None
    elif (trigger == "any" or trigger == "event") and switch("inn_departure"):
        call PlayEvent(play_event, "Town2NPCCop_1", "Town2NPCCop") from _call_Town2NPCCop_1_PlayEvent
        return (1, "", "Town2NPCCop_1")
    elif (trigger == "any" or trigger == "autorun") and switch("introduction"):
        call PlayEvent(play_event, "Town2NPCCop_0", "Town2NPCCop") from _call_Town2NPCCop_0_PlayEvent
        return (1, "", "Town2NPCCop_0")
    return None

label Town2NPCtourist1Base:
    if not switch("leyna_alone"):
        $ resolve_scene()
        Tourist "This town is great. although there are very few women ..."
    if switch("leyna_alone"):
        Tourist "Can't wait to see you on the fest.. Maybe we can take some beers"
    $ resolve_scene()
    return False

label Town2NPCtourist1(play_event = True, trigger = None): # event
    if is_erased("Town2NPCtourist1"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2NPCtourist1Base", "Town2NPCtourist1") from _call_Town2NPCtourist1_PlayEvent
        return (1, "", "Town2NPCtourist1")
    return None

label Town2borrachoinconscienteBase:
    DrunkVillager "Uhhg... tits... come closer... (pass out)"
    return False

label Town2borrachoinconsciente(play_event = True, trigger = None): # event
    if is_erased("Town2borrachoinconsciente"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2borrachoinconscienteBase", "Town2borrachoinconsciente") from _call_Town2borrachoinconsciente_PlayEvent
        return (1, "", "Town2borrachoinconsciente")
    return None

label Town2StallBase:
    VillagerWoman "PANTIES!. UNDERPANTS!. LOW PRICES, WE PRACTICALLY GIVE IT AWAY. LADIES AND GENTLEMEN BUY NOW"
    return False

label Town2Stall(play_event = True, trigger = None): # event
    if is_erased("Town2Stall"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2StallBase", "Town2Stall") from _call_Town2Stall_PlayEvent
        return (1, "", "Town2Stall")
    return None

label Town2Merchant_0:
    VillagerMan "COATS! PANTS!. VERY LOW PRICES! WE ARE ALMOST GIVING IT AWAY. SIR, BUY NOW OR REGRET IT LATER"
    VillagerWoman "You wish ... that clothing is rubbish and very expensive..."
    VillagerMan "shut up old witch..."
    VillagerWoman "you shut up, helpless old man"
    $ set_self_switch("Town2","Town2Merchant","A",True)
    return False

label Town2Merchant_1:
    VillagerMan "COATS! PANTS!. VERY LOW PRICES! WE ARE ALMOST GIVING IT AWAY. SIR, BUY NOW OR REGRET IT LATER"
    return False

label Town2Merchant(play_event = True, trigger = None): # event
    if is_erased("Town2Merchant"):
        return None
    elif trigger == "event" and self_switch("Town2","Town2Merchant","A"):
        call PlayEvent(play_event, "Town2Merchant_1", "Town2Merchant") from _call_Town2Merchant_1_PlayEvent
        return (1, "", "Town2Merchant_1")
    elif trigger == "event":
        call PlayEvent(play_event, "Town2Merchant_0", "Town2Merchant") from _call_Town2Merchant_0_PlayEvent
        return (1, "", "Town2Merchant_0")
    return None

label Town2FleaMarketBase:
    VillagerGirl "FRUITS! VEGETABLES! ALL FRESH! RECENTLY BROUGHT FROM THE GARDEN!"
    return False

label Town2FleaMarket(play_event = True, trigger = None): # event
    if is_erased("Town2FleaMarket"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2FleaMarketBase", "Town2FleaMarket") from _call_Town2FleaMarket_PlayEvent
        return (1, "", "Town2FleaMarket")
    return None

label Town2NPCWomanAdviceBase:
    if not switch("leyna_alone"):
        $ resolve_scene()
        VillagerWoman "Men in this village are wild. I should have moved to the city, like my sister..."
    if switch("leyna_alone"):
        VillagerWoman "Between you and me.. men are rough here but, hehehe.. they know how to provoke a woman to do bad things..."
    $ resolve_scene()
    return False

label Town2NPCWomanAdvice(play_event = True, trigger = None): # event
    if is_erased("Town2NPCWomanAdvice"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2NPCWomanAdviceBase", "Town2NPCWomanAdvice") from _call_Town2NPCWomanAdvice_PlayEvent
        return (1, "", "Town2NPCWomanAdvice")
    return None

label Town2ToRiverEvent_v3_0:
    Johan "We don't need to go back there for now."
    call Movement("Town2ToRiverEvent_v3_0", "player", ["TURN_L","L"]) from _call_Town2ToRiverEvent_v3_0_Movement
    $ resolve_scene()
    return False

label Town2ToRiverEvent_v3_1(menu_choice = None):
    Johan "I don't know if I want to go in there, you know they force us to go naked... and I don't like the idea of them seeing you naked"
    Leyna "Well... since we arrived, they have already seen me naked, right? just because they see me again shouldn't be a problem"
    Johan "I guess you're right... but I guess I still don't like the idea of them seeing you naked, you're my wife"
    Leyna "You are right... I leave it up to you"
    call GetChoice([_("Enter the river"), _("I'm not ready")], value=menu_choice, called_from="Town2ToRiverEvent_v3_1") from _call_Town2ToRiverEvent_v3_1_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Enter the river"):
        $ menu_choice = None
        $ set_switch("river_3", True)
        call GalleryViewed("riosexo") from _call_Town2ToRiverEvent_v3_1_GalleryViewed
        $ v0_7_3 = 1
        $ resolve_scene()
        Johan "Well, whatever, I guess it doesn't matter so much if they see our naked bodies... we are both adults and this is something natural"
        Leyna "Yes, you are right"
        $ fade_out()
        $ show_picture(1, "riosexo1")
        $ fade_in()
        $ resolve_scene()
        Alexa "Hey! you finally came! I didn't know if you would come with how reserved you are about your bodies!"
        Johan "Reserved... (Well, I guess from her point of view it may seem so, although I think she is just too... open about it)"
        Leyna "Yes... I'm still not used to it, but with Johan here I feel more relaxed"
        Alexa "Great! Well, you know Johan, stay close to your wife hehehehehe"
        Alexa "Come and have a beer with us!"
        "Leyna. M-more beer? "
        Johan "I don't know how you can keep drinking, we've practically been partying for days"
        Alexa "Oh come on, don't overreact!"
        Alexa "Come on, take one!"
        Johan "Okay... but just one"
        $ show_picture(2, "riosexo2")
        $ resolve_scene()
        Johan "Well... I have to admit that you are right Alexa, with a couple of shots of beer I already feel much better"
        Alexa "I told you so! Between the beer and being naked here, one's spirits are raised no matter how bad one feels"
        pause
        $ show_picture(3, "riosexo3")
        $ resolve_scene()
        Villager "Hey! how are you guys? I haven't seen you for a couple of days..."
        Leyna "He-hello"
        Johan "Hey... hmmm How's it going?"
        Villager "Here we are, having a beer by the river, enjoying the holidays before the routine starts again"
        pause
        $ show_picture(4, "riosexo4")
        $ resolve_scene()
        Johan "(His penis is rubbing Leyna...) I see, I can't imagine this town living a normal life, does it change much when the festival is over?"
        Villager "Yes! too much, I wish it was like this all year round, but the truth is that once the festival is over, life here is normal and ordinary"
        Villager "I guess when the festival starts everyone goes a little crazy hahahaha"
        Leyna "Let's take a bath Johan"
        Johan "Oh, sure, it'll come in handy in this hot weather"
        Villager "Yeah! see you later! have fun, guys!"
        pause
        $ fade_out()
        $ show_picture(5, "riosexo5")
        $ fade_in()
        $ resolve_scene()
        Johan "Who was that guy?"
        Leyna "... I don't know, it's a little difficult for me to differentiate the people of this town, we have met so many in the last few days..."
        Johan "Hahahaha you can say that again... I'm glad I'm not the only one"
        $ show_picture(6, "riosexo6")
        $ resolve_scene()
        Johan "Alexa... she always seems to be very comfortable naked and surrounded by guys... didn't she come to town with her husband?"
        Johan "I haven't seen him for days... I don't know what he will think of all this"
        Leyna "!!!... yeah... I guess they have some kind of open relationship... or so I hope"
        Johan "Yeah... I'm not so sure about that but okay...."
        Johan "Poor guy..."
        Leyna "!!!!... Y-yes"
        pause
        $ show_picture(7, "riosexo7")
        $ resolve_scene()
        Johan "Oh there you go... I knew something like this was about to happen"
        Johan "They're not going to do it in front of everyone, are they?"
        $ show_picture(8, "riosexo8")
        $ resolve_scene()
        Leyna "I-I don't know... I don't think so, right?"
        Johan "After everything I've seen, nothing surprises me anymore"
        pause
        $ show_picture(9, "riosexo9")
        $ resolve_scene()
        Johan "!!! (they are doing it in front of everyone)"
        Leyna "..."
        Leyna "(I-I'm starting to get horny watching this, I hope Johan doesn't notice....)"
        pause
        $ show_picture(10, "riosexo10")
        $ resolve_scene()
        Johan "(Fuck, they're not disguising shit, I'm embarrassed but I can't stop looking)"
        Johan "(Besides, I have it hard as a rock, I can't get out of the water like this)"
        Johan "(Although Leyna... hold on a second...)"
        Johan "(Leyna is red as a tomato... she seems to be very horny... I didn't know she liked this kind of things)"
        Johan "(Wait a minute... is she touching herself? I can't help but get even more excited seeing my wife like that...)"
        Johan "(... I can't help it... I must take advantage of this situation)"
        $ show_picture(11, "riosexo11")
        $ resolve_scene()
        Leyna "!!!!"
        Johan "Let me give you a hand with that...."
        Leyna "Johan..."
        pause
        $ show_picture(12, "riosexo12")
        $ resolve_scene()
        Leyna "Hmmmfff!"
        Johan "You sure are horny... you're on fire"
        Leyna "J-Johan!"
        Johan "Let me help you with that"
        Leyna "aaahh..."
        pause
        $ show_picture(13, "riosexo13")
        $ resolve_scene()
        Leyna "Johan... fuck me..."
        Johan "Here?.... very well, but let's try to disguise it a little bit"
        Leyna "Let me get on top..."
        $ show_picture(14, "riosexo14")
        $ resolve_scene()
        Johan "Oh!"
        Johan "I can see you were looking forward to it"
        Johan "God... you are so hot down there"
        Leyna "Ah... shut up and fuck me"
        Johan "Yeah..."
        $ show_picture(15, "riosexo17")
        $ resolve_scene()
        Leyna "Hmmmf... ahh"
        Johan "Ssshhhh shut up or they will hear us..."
        Leyna "I-I don't care... I don't care if they can hear us, just fuck me"
        if johan_leyna_sex == 1:
            $ resolve_scene()
            Leyna "(Johan... he's feeling a bit weird... since the other day when we did it he got a bit nervous... now he's a bit clumsy)"
            Leyna "(I'm barely enjoying it...)"
            Leyna "F-faster..."
            Johan "I'm trying... there are so many people around"
            Johan "(I can't concentrate... I can't get out of my head everything that has been going on these last few days)"
            Leyna "(My God... he is doing terrible... what is happening to Johan lately? has he changed?... or is it me that has changed?)"
            pause
            $ show_picture(16, "riosexo18")
            $ resolve_scene()
            Villager "Hey... I see you need a hand"
            Leyna "Wait"
            Johan "???"
            Villager "Come on, I know you're looking forward to it, doing something like that in front of everybody"
            pause
            $ show_picture(17, "riosexo19")
            call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2ToRiverEvent_v3_1_PlaySound
            $ resolve_scene()
            Johan "!!! what's going on? (I can't see anything from here... there's someone next to us?)"
            Leyna "Aghghgagagh!"
            Villager "Like this! I want to feel your tonsils!"
            Johan "(Wait, that sound! There's a guy sticking his dick in Leyna's mouth! While I'm here fucking her!)"
            Johan "H-hey! ... oh my god"
            $ show_picture(18, "riosexo20")
            $ resolve_scene()
            Johan "(L-Leyna's pussy is convulsing, she looks like she's about to have an orgasm right now! Holy cow it feels so good.... )"
            Johan "F-fuck!!"
            Johan "(H-he's fucking me! Leyna is moving like crazy!... FUCK!i'm going to cum! b-but there's a guy right there rubbing his dick in Leyna's mouth!)"
            Johan "(Shit, I can't take it anymore! I'm coming!)"
            Johan "AAHHH!"
            Leyna "(J-johan just cum? right now? while all this is going on?)"
            Johan "Ah ah ah!"
            pause
            $ show_picture(19, "riosexo21")
            $ resolve_scene()
            Johan "(Wait! There's really a guy here!)"
            Johan "H-Hey! get off of my wife right now Get out!"
            Villager "Oh come on, I'm about to finish"
            Johan "I told you to get out! get out now!"
            pause
            stop bgs fadeout 1
            $ show_picture(20, "riosexo22")
            $ resolve_scene()
            Villager "TCh! fuck man! ok ok, I'm leaving, next time don't fuck in public if you don't want someone else to join the party."
            Johan "Leave!"
            Villager "I'm leaving... I'll catch you around, honey"
            Leyna "Ah ah ah!"
            pause
            $ show_picture(21, "riosexo23")
            $ resolve_scene()
            Johan "What a waste of time... come on, let's go..."
            Leyna "Y-yes (waste of time? but you just cummed inside me... you came so fast... were you liking it johan?)"
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
            $ erase_picture(19)
            $ erase_picture(20)
            $ erase_picture(21)
            call TransferPlayer("Town2", "Town2ToRiverEvent_v3_1", 37, 23, direction=4) from _call_Town2ToRiverEvent_v3_1_TransferPlayer
            $ fade_in()
            call Movement("Town2ToRiverEvent_v3_1", "player", ["L","L","L"]) from _call_Town2ToRiverEvent_v3_1_Movement
            call PlaySound("sound", "audio/Computer.ogg", volume=0.9, no_loop=True) from _call_Town2ToRiverEvent_v3_1_PlaySound_1
            $ resolve_scene()
            call PauseForBalloon("Town2ToRiverEvent_v3_1") from _call_Town2ToRiverEvent_v3_1_PauseForBalloon
            Johan "!!! Was that your cell phone?"
            Leyna "Yes... Let's see...."
            Leyna "It's the photographer... he says he needs to see us right away"
            Johan "The photographer... (that guy again...)"
            Johan "Sure, let's see what he wants"
        if johan_leyna_sex == 2:
            $ show_picture(16, "riosexo16")
            call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2ToRiverEvent_v3_1_PlaySound_2
            $ resolve_scene()
            Leyna "Oh!"
            Leyna "(My God, J-Johan is fucking me like that day...)"
            Leyna "M-my God... if you keep this up I-I'm going to cum..."
            Johan "Perfect! cum, that's what I want"
            Leyna "Ah.... hmmm...."
            pause
            $ show_picture(17, "riosexo18")
            $ resolve_scene()
            Villager "Hey guys, I see you're having a good time"
            Leyna "Hmmff?"
            Villager "Doing this here, I guess you want me to give you a hand, don't you?"
            Leyna "(Dios mio casi me la mete en la boca sin avisar)"
            stop bgs fadeout 1
            Johan "Hey! What the hell are you doing! Get out of the way right now!"
            Villager "D-don't you want some help?"
            Johan "N-no, we're fine, man, thanks, but back off, we'll take care of it ourselves"
            Villager "Since you were here doing it in front of the whole world I thought that..."
            Johan "You thought wrong"
            Villager "Okay guys, sorry"
            $ fade_out()
            $ show_picture(18, "riosexo24")
            $ fade_in()
            $ resolve_scene()
            Leyna "Ah ah ah...."
            Leyna "Shall we continue?"
            Johan "Hehehehe Do you want to continue?"
            Leyna "Y-yes..."
            Johan "Then we continue"
            pause
            $ fade_out()
            $ show_picture(19, "riosexo25")
            call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2ToRiverEvent_v3_1_PlaySound_3
            $ fade_in()
            $ resolve_scene()
            "Minutes later"
            Leyna "Ah! ah! ah! M-my God... I'm cumming!"
            Johan "That's the way I like it, cum! come on! I want to see you writhing with pleasure!"
            Leyna "Ah ah! ah m-my god... so fast! you're drilling me"
            Johan "Ah! ah ah ah!"
            Leyna "Ooohh!!! ahh!!"
            Villager "(whispering) Jesus Christ, it didn't look like it but that guy is a fucking machine... now I understand why she's with him"
            Villager2 "(whispering) who would have thought..."
            Johan "That's how I like it"
            pause
            $ fade_out()
            stop bgs fadeout 1
            $ show_picture(20, "riosexo26")
            $ fade_in()
            $ resolve_scene()
            Leyna "I-I see that you've cum too..."
            Johan "hahahaha yes, I couldn't help it"
            Johan "!!!!"
            Johan "Shit, everyone is watching us, let's get out of here and take a nice hot shower"
            Leyna "Yes, good idea"
            "Leyna. (My God I'm still shaking... it's going to be hard for me to get up... what a fuck he has given me... Johan has improved since we arrived)"
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
            $ erase_picture(19)
            $ erase_picture(20)
            call TransferPlayer("Town2", "Town2ToRiverEvent_v3_1", 37, 23, direction=4) from _call_Town2ToRiverEvent_v3_1_TransferPlayer_1
            $ fade_in()
            call Movement("Town2ToRiverEvent_v3_1", "player", ["L","L","L"]) from _call_Town2ToRiverEvent_v3_1_Movement_1
            call PlaySound("sound", "audio/Computer.ogg", volume=0.9, no_loop=True) from _call_Town2ToRiverEvent_v3_1_PlaySound_4
            $ resolve_scene()
            call PauseForBalloon("Town2ToRiverEvent_v3_1") from _call_Town2ToRiverEvent_v3_1_PauseForBalloon_1
            Johan "!!! was that your cell phone?"
            Leyna "Yes... let's see...."
            Leyna "It's the photographer... he says he needs to see us right away"
            Johan "The photographer... (that guy again...)"
            Johan "Sure, let's see what he wants"
    elif menu_choice == _("I'm not ready"):
        $ menu_choice = None
        $ resolve_scene()
        Johan "I'm sorry but I don't feel comfortable about this situation"
        "Leyna.{p}.. Sure, it makes sense, if you change your mind they will be on the river all day so we can come back whenever you want"
        Johan "Yeah..."
        call Movement("Town2ToRiverEvent_v3_1", "player", ["L","L"]) from _call_Town2ToRiverEvent_v3_1_Movement_2
    $ resolve_scene()
    return False

label Town2ToRiverEvent_v3_2:
    Johan "We don't need to go back there for now."
    call Movement("Town2ToRiverEvent_v3_2", "player", ["TURN_L","L"]) from _call_Town2ToRiverEvent_v3_2_Movement
    $ resolve_scene()
    return False

label Town2ToRiverEvent_v3(play_event = True, trigger = None): # event
    if is_erased("Town2ToRiverEvent_v3"):
        return None
    elif trigger == "event" and switch("river_3"):
        call PlayEvent(play_event, "Town2ToRiverEvent_v3_2", "Town2ToRiverEvent_v3") from _call_Town2ToRiverEvent_v3_2_PlayEvent
        return (0, "", "Town2ToRiverEvent_v3_2")
    elif trigger == "event" and switch("party_at_festival"):
        call PlayEvent(play_event, "Town2ToRiverEvent_v3_1", "Town2ToRiverEvent_v3") from _call_Town2ToRiverEvent_v3_1_PlayEvent
        return (0, "", "Town2ToRiverEvent_v3_1")
    elif trigger == "event" and switch("third_day"):
        call PlayEvent(play_event, "Town2ToRiverEvent_v3_0", "Town2ToRiverEvent_v3") from _call_Town2ToRiverEvent_v3_0_PlayEvent
        return (0, "", "Town2ToRiverEvent_v3_0")
    return None

label Town2LeynaJohanSex_0(menu_choice = None):
    call Movement("Town2LeynaJohanSex_0", "player", ["D","D","D","TURN_U"]) from _call_Town2LeynaJohanSex_0_Movement
    $ resolve_scene()
    call PauseForBalloon("Town2LeynaJohanSex_0") from _call_Town2LeynaJohanSex_0_PauseForBalloon
    Johan "(... why do I feel this way?... I can't stop thinking about what just happened)"
    Leyna "Johan? are you all right?"
    Johan "... Let's go to the Inn right now"
    Leyna "??? What? (he's acting really weird...he's worrying me...he's not going to.... break up with me, right?"
    Johan "Come with me"
    Leyna "Su-sure"
    call Movement("Town2LeynaJohanSex_0", "player", ["D","D","D"]) from _call_Town2LeynaJohanSex_0_Movement_1
    $ fade_out()
    call TransferPlayer("Inn", "Town2LeynaJohanSex_0", 8, 10, direction=8) from _call_Town2LeynaJohanSex_0_TransferPlayer
    $ fade_in()
    call Movement("Town2LeynaJohanSex_0", "player", ["U","U","U"]) from _call_Town2LeynaJohanSex_0_Movement_2
    $ fade_out()
    call TransferPlayer("InnRooms", "Town2LeynaJohanSex_0", 7, 17, direction=6) from _call_Town2LeynaJohanSex_0_TransferPlayer_1
    $ fade_in()
    call Movement("Town2LeynaJohanSex_0", "player", ["R","R","R","U","U"]) from _call_Town2LeynaJohanSex_0_Movement_3
    $ show_picture(1, "johanfollar1")
    call PlaySound("sound", "audio/Close1.ogg", volume=0.9, no_loop=True) from _call_Town2LeynaJohanSex_0_PlaySound
    $ resolve_scene()
    Leyna "Johan? what's wrong?"
    $ show_picture(2, "johanfollar2")
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_Town2LeynaJohanSex_0_PlaySound_1
    $ resolve_scene()
    Leyna "Johan?"
    Johan "(Look at her... this woman... she is perfect)"
    Johan "Hm..."
    $ show_picture(3, "johanfollar3")
    $ resolve_scene()
    Leyna "!!!"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_Town2LeynaJohanSex_0_PlaySound_2
    $ show_picture(4, "johanfollar4")
    $ resolve_scene()
    Leyna "(He has taken off my clothes... in such a... manly way I don't think I've ever seen Johan like that)"
    Johan "(After everything that has happened today.... I cannot stay the same... Leyna is my wife, this beautiful woman is mine)"
    Johan "(Almost everyone in town wants to fuck her and rightly so. I didn't realize how lucky I am to be with a woman like this)"
    Johan "(I have to make an effort for her, to give my best to satisfy her.... but all these guys wanting to be with her, it's such a big pressure...)"
    Johan "(I feel so insecure... I can't stop thinking about what just happened at the photo shoot)"
    "(BEWARE The decision you make now will have repercussions at the end of the story)"
    call GetChoice([_("I can't take the pressure"), _("NONSENSE! I will do my best! ")], value=menu_choice, called_from="Town2LeynaJohanSex_0") from _call_Town2LeynaJohanSex_0_GetChoice
    $ menu_choice = _return
    if menu_choice == _("I can't take the pressure"):
        $ menu_choice = None
        $ show_picture(5, "johanfollar13")
        $ resolve_scene()
        Johan "(Damn it, the pressure.... Why do I feel like this? it's like I have a crowd watching me)"
        Johan "(After so many years together with her.... now I feel as if it is the first time I am going to fuck my wife)"
        Johan "(I don't know if I'm feeling up to it!)"
        $ show_picture(6, "johanfollar8")
        $ resolve_scene()
        Leyna "!!! You're already going in? it's a bit... rushed"
        Johan "...."
        Johan "(Don't listen to her if I try hard enough... maybe .... maybe it's good enough)"
        pause
        $ show_picture(7, "johanfollar9")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2LeynaJohanSex_0_PlaySound_3
        $ resolve_scene()
        Leyna "!!!"
        Johan "(I may have gone too fast... it's a little dry down there...)"
        Johan "(Why can't I stop thinking about stupid things? I'm not where I should be)"
        pause
        $ show_picture(8, "fotoerotica8")
        $ resolve_scene()
        $ flash_screen([255,255,255,170], 60, True)
        Johan "(Shit why do I have to think about that now?)"
        Leyna "Johan? are you okay? you feel a little... strange..."
        $ erase_picture(8)
        $ resolve_scene()
        Johan "Y-yes, I'm fine!"
        Johan "Pu-put yourself like this!"
        pause
        $ show_picture(8, "johanfollar10")
        stop bgs fadeout 1
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2LeynaJohanSex_0_PlaySound_4
        $ resolve_scene()
        Johan "I like that!"
        Leyna "Ah ah ah!"
        Johan "(Looks like it's getting wet! very good, I just have to keep it up! and stop thinking so much!)"
        $ show_picture(9, "fotoerotica18")
        $ resolve_scene()
        Johan "(Shit, not again! Why do I have to be thinking about that shit all the time?)"
        Johan "(What the fuck? I'm going to cum already... normally I last much longer)"
        $ flash_screen([255,255,255,170], 60, True)
        stop bgs fadeout 1
        $ show_picture(10, "johanfollar11")
        $ resolve_scene()
        $ flash_screen([255,255,255,170], 60, True)
        Johan "AAAhh!"
        Leyna "??? (Already? ... that's been a bit ...)"
        Johan "(Fuck, I couldn't help it... Shit)"
        $ show_picture(11, "johanfollar14")
        $ resolve_scene()
        Leyna "That was... hahaha it was... well... I ehmmm I'm going rest a little bit... then we could go out for a while and have a drink if you want..."
        Johan "Hmmm yes ... sure... (Why is the atmosphere so uncomfortable? fuck... this has been a disaster)"
        Johan "Take a nap, I'll be downstairs waiting for you"
        Leyna "See you in half an hour or so!"
        Johan ".... Yeah, great..."
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
        $ set_switch("johan_and_leyna_sex", True)
        call GalleryViewed("johanfollar") from _call_Town2LeynaJohanSex_0_GalleryViewed
        $ johan_leyna_sex = 1
        $ erase_picture(11)
        call TransferPlayer("Town2", "Town2LeynaJohanSex_0", 28, 22, direction=2) from _call_Town2LeynaJohanSex_0_TransferPlayer_2
        $ fade_in()
        call Movement("Town2LeynaJohanSex_0", "player", ["D","D","TURN_U"]) from _call_Town2LeynaJohanSex_0_Movement_4
        $ resolve_scene()
        Leyna "Would you like a beer?"
        Johan "Yes, of course... (I really need some beer)"
        Leyna "Let's go to the bar then"
        Johan "Sure..."
    elif menu_choice == _("NONSENSE! I will do my best! "):
        $ menu_choice = None
        $ show_picture(5, "johanfollar5")
        $ resolve_scene()
        Johan "(But what am I thinking? Leyna is my wife, among all the guys that tried to seduce her,she chose me)"
        Johan "(I will try my best to give you the best sex of your life I don't have to think so much, just enjoy the moment)"
        Leyna "Johan, are you okay?"
        Johan "Me? yeah!"
        $ show_picture(6, "johanfollar7")
        $ resolve_scene()
        Leyna "Ah!"
        Leyna "(He's!!! it's been a long time since he did this to me, he's doing it... very well... if he keeps on like this I'll be done soon)"
        Leyna "Keep going... keep going... Oh my God..."
        pause
        $ show_picture(7, "johanfollar8")
        $ resolve_scene()
        Johan "No, not yet"
        Leyna "Why did you stop?"
        Johan "Because I don't want you to cum yet, I'm going to make it last as long as I can!"
        $ show_picture(8, "johanfollar9")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2LeynaJohanSex_0_PlaySound_5
        $ resolve_scene()
        Leyna "AH! ah! ah!"
        Johan "Do you like it?"
        Leyna "Hmmm!!"
        Johan "Tell me you like it, leyna! or I'll stop!"
        Leyna "(Johan has never talked dirty to me like that before ...) I like it! Don't stop please keep going!"
        Johan "Very good, come here"
        Leyna "!!!"
        pause
        $ show_picture(9, "johanfollar10")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2LeynaJohanSex_0_PlaySound_6
        $ resolve_scene()
        Johan "That's right!"
        Leyna "Ahh! Keep going! Keep fucking me like this!"
        Johan "You don't have to tell me, I won't stop until you cum!"
        Leyna "AH!!! I'M GOING TO CUM!!"
        Johan "ME TOO!"
        pause
        $ show_picture(10, "johanfollar11")
        stop bgs fadeout 1
        $ resolve_scene()
        $ flash_screen([255,255,255,170], 60, True)
        $ flash_screen([255,255,255,170], 60, True)
        Johan "AH!!"
        Leyna "AAH! shit! (I can't stop shaking, it's the first orgasm I've had in months)"
        pause
        $ show_picture(11, "johanfollar12")
        $ resolve_scene()
        Johan "What do you think?"
        Leyna "Unbelievable... I don't know what's wrong with you today... but I wouldn't mind if you kept it up a little longer hahaha"
        Johan "Well, no problem with that as long as you want it, we can do this every day hahaha"
        Leyna "Hahaha well, every day... we'll see..."
        Leyna "Shall we go for a drink?"
        Johan "Sure! let's go to the bar for a beer!"
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
        $ set_switch("johan_and_leyna_sex", True)
        call GalleryViewed("johanfollar") from _call_Town2LeynaJohanSex_0_GalleryViewed_1
        $ johan_leyna_sex = 2
        $ erase_picture(11)
        call TransferPlayer("Town2", "Town2LeynaJohanSex_0", 28, 22, direction=2) from _call_Town2LeynaJohanSex_0_TransferPlayer_3
        $ fade_in()
    $ resolve_scene()
    return False

label Town2LeynaJohanSex(play_event = True, trigger = None): # event
    if is_erased("Town2LeynaJohanSex"):
        return None
    elif switch("johan_and_leyna_sex"):
        return None
    elif trigger == "event" and switch("erotic_photos_together"):
        call PlayEvent(play_event, "Town2LeynaJohanSex_0", "Town2LeynaJohanSex") from _call_Town2LeynaJohanSex_0_PlayEvent
        return (0, "", "Town2LeynaJohanSex_0")
    return None

label Town2TABLON_0(menu_choice = None):
    "What to do today:"
    call GetChoice([_("Bar 1"), _("Market"), _("Villagers"), _("River 1")], value=menu_choice, called_from="Town2TABLON_0") from _call_Town2TABLON_0_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Bar 1"):
        $ menu_choice = None
        $ resolve_scene()
        "There is a sort of noisy-gloopy tavern in the southern part of town. There you will find the villagers in their natural habitat"
    elif menu_choice == _("Market"):
        $ menu_choice = None
        "The merchants take their stuff to the street, you should visit the west part of town"
    elif menu_choice == _("Villagers"):
        $ menu_choice = None
        "Be careful, sometimes there are undesirable people around the bar. If you want to avoid an uncomfortable situation, better not go there.."
    elif menu_choice == _("River 1"):
        $ menu_choice = None
        "The river is a place where the goddess is worshipped, you can get there by going out to the right of the town"
    return False

label Town2TABLON_1(menu_choice = None):
    "What to do today:"
    call GetChoice([_("Photographer 1"), _("Hotsprings"), _("Photographer 2"), _("Bar 2"), _("River 2")], value=menu_choice, called_from="Town2TABLON_1") from _call_Town2TABLON_1_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Photographer 1"):
        $ menu_choice = None
        $ resolve_scene()
        "The local photographer is willing to offer you a job, you can find it in the upper town"
    elif menu_choice == _("Hotsprings"):
        $ menu_choice = None
        "To take a relaxing bath you must go to the path that is on the left side of the city"
    elif menu_choice == _("Photographer 2"):
        $ menu_choice = None
        "Now that you are relaxed after the bath, you can go for the second round with the photographer"
    elif menu_choice == _("Bar 2"):
        $ menu_choice = None
        "The villagers may be a bit tough, but they know how to have a good time with a few beers"
    elif menu_choice == _("River 2"):
        $ menu_choice = None
        "Once you have talked to Alexa and you have enough corruption points, you can go back to the river"
    return False

label Town2TABLON_2(menu_choice = None):
    "What to do today:"
    call GetChoice([_("Photographer 3"), _("Worker's quest"), _("Dresser"), _("The dream"), _("Police station"), _("Night Party")], value=menu_choice, called_from="Town2TABLON_2") from _call_Town2TABLON_2_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Photographer 3"):
        $ menu_choice = None
        $ resolve_scene()
        "Johan may finds out you have posed for a stranger, what will he think about it?"
    elif menu_choice == _("Worker's quest"):
        $ menu_choice = None
        "Help the festival worker find his son. (Is on the left road)"
        "The son usually hangs around the bar, help him find the toolbag. Once you have it, go and talk with the worker again"
    elif menu_choice == _("Dresser"):
        $ menu_choice = None
        "Now that you've earned the favor of the worker, you only need to go buy the festival clothes at the store"
    elif menu_choice == _("The dream"):
        $ menu_choice = None
        "If you've followed all these steps, you should go to sleep, you deserve it!"
    elif menu_choice == _("Police station"):
        $ menu_choice = None
        "There's a dangerous prisoner arrested at the police station, better not go near there"
    elif menu_choice == _("Night Party"):
        $ menu_choice = None
        "Sometimes people go out to drink in the village when it gets dark"
    return False

label Town2TABLON_3(menu_choice = None):
    "What to do today:"
    call GetChoice([_("Police station"), _("Night Party"), _("Go to the festival")], value=menu_choice, called_from="Town2TABLON_3") from _call_Town2TABLON_3_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Police station"):
        $ menu_choice = None
        $ resolve_scene()
        "(IN CASE YOU HAVE MISSED THIS SCENE) There's a dangerous prisoner arrested at the police station, better not go near there"
    elif menu_choice == _("Night Party"):
        $ menu_choice = None
        "(IN CASE YOU HAVE MISSED THIS SCENE) Sometimes people go out to drink in the village when it gets dark"
    elif menu_choice == _("Go to the festival"):
        $ menu_choice = None
    return False

label Town2TABLON_4(menu_choice = None):
    "What to do today:"
    call GetChoice([_("Groceries store"), _("Bar"), _("Hot springs"), _("Flowers"), _("Come back to hotsprings"), _("Photographer")], value=menu_choice, called_from="Town2TABLON_4") from _call_Town2TABLON_4_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Groceries store"):
        $ menu_choice = None
        $ resolve_scene()
        "Try to speak with the old woman, maybe she has a job for you"
    elif menu_choice == _("Bar"):
        $ menu_choice = None
        "Try to speak with the Barman, maybe he has a job for you"
    elif menu_choice == _("Hot springs"):
        $ menu_choice = None
        "Try to speak with the receptionist, maybe she has a job for you"
    elif menu_choice == _("Flowers"):
        $ menu_choice = None
        "Once you speak with the receptionist, go get the flowers in the field"
    elif menu_choice == _("Come back to hotsprings"):
        $ menu_choice = None
        "Go give the receptionist the flowers and start your first day at work"
    elif menu_choice == _("Photographer"):
        $ menu_choice = None
        "Maybe the photographer has a new job for you"
    return False

label Town2TABLON_5:
    "You have to find the boy, try to find him in upper town"
    return False

label Town2TABLON_6:
    "maybe the photographer is interested in talking to you"
    "Are you sure you want to go to the river with Alexa? "
    "it's Leyna's day off from the bar, but you could go for a bite to eat if you want to"
    "After a long day, memories come back"
    return False

label Town2TABLON(play_event = True, trigger = None): # event
    if is_erased("Town2TABLON"):
        return None
    elif trigger == "event" and switch("party_at_festival"):
        call PlayEvent(play_event, "Town2TABLON_6", "Town2TABLON") from _call_Town2TABLON_6_PlayEvent
        return (0, "", "Town2TABLON_6")
    elif trigger == "event" and switch("find_youth"):
        call PlayEvent(play_event, "Town2TABLON_5", "Town2TABLON") from _call_Town2TABLON_5_PlayEvent
        return (1, "", "Town2TABLON_5")
    elif trigger == "event" and switch("leyna_dream_end"):
        call PlayEvent(play_event, "Town2TABLON_4", "Town2TABLON") from _call_Town2TABLON_4_PlayEvent
        return (1, "", "Town2TABLON_4")
    elif trigger == "event" and johan_dream >= 2:
        call PlayEvent(play_event, "Town2TABLON_3", "Town2TABLON") from _call_Town2TABLON_3_PlayEvent
        return (1, "", "Town2TABLON_3")
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "Town2TABLON_2", "Town2TABLON") from _call_Town2TABLON_2_PlayEvent
        return (1, "", "Town2TABLON_2")
    elif trigger == "event" and switch("finished_river_scene"):
        call PlayEvent(play_event, "Town2TABLON_1", "Town2TABLON") from _call_Town2TABLON_1_PlayEvent
        return (1, "", "Town2TABLON_1")
    elif trigger == "event":
        call PlayEvent(play_event, "Town2TABLON_0", "Town2TABLON") from _call_Town2TABLON_0_PlayEvent
        return (1, "", "Town2TABLON_0")
    return None

label Town2IHaveToFindThatGuy_0:
    Leyna "I have to find that guy"
    call Movement("Town2EV034_0", "player", ["D"]) from _call_Town2EV034_0_Movement
    $ resolve_scene()
    return False

label Town2IHaveToFindThatGuy(play_event = True, trigger = None): # event
    if is_erased("Town2IHaveToFindThatGuy"):
        return None
    elif ritual >= 2:
        return None
    elif trigger == "event" and switch("find_youth"):
        call PlayEvent(play_event, "Town2IHaveToFindThatGuy_0", "Town2IHaveToFindThatGuy") from _call_Town2IHaveToFindThatGuy_0_PlayEvent
        return (0, "", "Town2IHaveToFindThatGuy_0")
    return None

label Town2chicoencontrado_0(menu_choice = None):
    Leyna "I found you!"
    $ show_picture(1, "mamada1")
    $ resolve_scene()
    YoungVillager "Right and now comes the best part, go ahead and give me a kiss"
    $ show_picture(2, "mamada2")
    $ resolve_scene()
    Leyna "Well, a peck on the cheek"
    $ show_picture(3, "mamada3")
    $ resolve_scene()
    YoungVillager "No kiss on the cheek, the kiss has to be on the mouth, I'm not a child anymore, that's what tradition dictates"
    $ show_picture(4, "mamada4")
    $ resolve_scene()
    Leyna "(This town and its damn traditions)"
    Leyna "Let's get this over with I'll give you the kiss and we'll be back"
    YoungVillager "Great..."
    Leyna "(Well, it's just an innocent kiss Leyna)"
    $ show_picture(5, "mamada5")
    $ resolve_scene()
    Leyna "!!!!"
    Leyna "(This boy!!)"
    $ show_picture(6, "mamada6")
    $ resolve_scene()
    Leyna "(it's certainly not the first kiss he's given... it can't be)"
    Leyna "(I'm getting too excited with this kiss... I should stop now but... it's so... hard to stop now)"
    $ show_picture(7, "mamada7")
    $ resolve_scene()
    Leyna "... Stop... stop now"
    YoungVillager "Stop? why?"
    $ show_picture(8, "mamada8")
    $ resolve_scene()
    Leyna "Because I'm married! we have to go back now"
    YoungVillager "We can't go back now"
    Leyna "And why can't we?"
    $ show_picture(9, "mamada9")
    $ resolve_scene()
    YoungVillager "Look how I am now! I can't go around town like this"
    Leyna "Oh...."
    Leyna "(... Of course, it has to be huge...)"
    $ show_picture(10, "mamada10")
    $ resolve_scene()
    YoungVillager "And this is all your fault"
    Leyna "My fault?"
    $ show_picture(11, "mamada11")
    $ resolve_scene()
    YoungVillager "Of course, you enjoyed that kiss too, didn't you? I could tell, you're so sexy that my body can't control itself"
    Leyna "But..."
    YoungVillager "No! I can't go around town like this, what if my mother sees me? she'll think I'm a pervert!"
    YoungVillager "You have to take responsibility for your actions and help me with this"
    $ show_picture(12, "mamada12")
    $ resolve_scene()
    Leyna "Res-responsibility?"
    call GetChoice([_("Help him"), _("Don't help him")], value=menu_choice, called_from="Town2chicoencontrado_0") from _call_Town2chicoencontrado_0_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Help him"):
        $ menu_choice = None
        $ resolve_scene()
        Leyna "O...okay I will help you with this"
        call GalleryViewed("mamada") from _call_Town2chicoencontrado_0_GalleryViewed
        Leyna "I'll... I'll show you my body a little bit and you can... touch yourself"
        YoungVillager "... Well... go ahead"
        $ show_picture(13, "mamada13")
        $ resolve_scene()
        Leyna "(I can't believe I'm doing this in the middle of the street)"
        Leyna "Go on..."
        call PlaySound("music", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2chicoencontrado_0_PlaySound
        $ show_picture(14, "mamada15")
        $ resolve_scene()
        YoungVillager "..."
        YoungVillager "......"
        YoungVillager "............"
        $ show_picture(15, "mamada14")
        stop music fadeout 1
        call PlaySound("music", "audio/Town1.ogg", volume=0.9, no_loop=False) from _call_Town2chicoencontrado_0_PlaySound_1
        $ resolve_scene()
        Leyna "Are you done?"
        YoungVillager "AAAh I can't do this! you can't rush me with this! besides I've already seen boobs in magazines and stuff... this is not enough, you have to help me!"
        Leyna "Help you more?...."
        YoungVillager "Yeah... come on, you're a grown woman, you must have done this a hundred times..."
        Leyna "... Okay... I'll help you, let's get this over with before someone sees us"
        $ show_picture(16, "mamada16")
        $ resolve_scene()
        Leyna "God..."
        YoungVillager "Big, right?"
        Leyna "Don't... don't say anything"
        $ show_picture(17, "mamada17")
        $ resolve_scene()
        Leyna ".... ( Is so close to me... )"
        pause
        $ show_picture(18, "mamada18")
        stop music fadeout 1
        call PlaySound("music", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2chicoencontrado_0_PlaySound_2
        $ resolve_scene()
        YoungVillager "Ohhh yes, keep it up"
        Leyna "(I'm really wet down there... right now, we could fuck and no one would notice...)"
        Leyna "... you are taking too long..."
        YoungVillager "Sssshh...."
        YoungVillager "I'm almost there... I'm almost there"
        stop music fadeout 1
        if switch("infusion"):
            $ resolve_scene()
            Leyna "(If this keeps up we'll end up getting caught, I have to end this quickly)"
            Leyna "... I'll have to help you a little bit more ...."
            YoungVillager "???"
            $ show_picture(19, "mamada19")
            stop music fadeout 1
            call PlaySound("music", "audio/Town1.ogg", volume=0.9, no_loop=False) from _call_Town2chicoencontrado_0_PlaySound_3
            $ resolve_scene()
            YoungVillager "Oooh great!!!"
            Leyna "( It barely fits in my mouth...)"
            YoungVillager "This is the best thing that has ever happened to me!"
            Leyna "(My God, what am I doing? I've never behaved like this... but I'm so horny... it's hard to control myself)"
            stop music fadeout 1
            call PlaySound("music", "audio/audio follar.ogg", volume=0.15, no_loop=False) from _call_Town2chicoencontrado_0_PlaySound_4
            $ play_video_looped(1, "mamada_webm", "mamada.webm",width=1920,height=1080)
            $ resolve_scene()
            pause
            $ stop_video(1)
            $ show_picture(21, "mamada20")
            $ resolve_scene()
            Leyna "(It's still taking too long... maybe if I... put it inside me I'll finish sooner... maybe... maybe I'll have to fuck him...)"
            stop music fadeout 1
            call PlaySound("music", "audio/Town1.ogg", volume=0.9, no_loop=False) from _call_Town2chicoencontrado_0_PlaySound_5
            Leyna "Hey..."
            $ fade_out()
            $ fade_in()
        $ show_picture(22, "mamada21")
        $ resolve_scene()
        $ flash_screen([255,255,255,170], 60, True)
        YoungVillager "OOOoooh!!!"
        pause
        if switch("infusion"):
            $ resolve_scene()
            Leyna "(That's it... what was I about to do? was I going to fuck this guy in the middle of the street if I had gone a little bit longer?)"
        $ show_picture(23, "mamada22")
        $ resolve_scene()
        Leyna "(thank goodness it's over, although now I have to clean up this mess)"
        $ show_picture(24, "mamada23")
        $ resolve_scene()
        YoungVillager "Well, that's it... thank you very much!"
        Leyna "Stop being thankful... bring me something I can clean myself with! and fast!"
        YoungVillager "Y-yes sure! I'll be right back"
        Leyna "...."
        $ fade_out()
        $ show_picture(25, "mamada24")
        $ fade_in()
        $ resolve_scene()
        YoungVillager2 "I can't believe it! what a lucky son of a bitch!"
        YoungVillager3 "Some are born lucky and others like us are not.... But don't worry, I've taken pictures and I'll pass them on to you later!!"
        YoungVillager2 "Oh! so you took pictures! hahahaha I have an idea!"
        $ set_switch("corruption_average", True)
        stop music fadeout 1
        if not renpy.in_rollback():
            $ _saved_bgm = renpy.music.get_playing()
        play music "audio/Curse1.ogg" volume 0.5 noloop
        if _saved_bgm is not None and not renpy.in_rollback():
            queue music _saved_bgm
            $ _saved_bgm = None
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
        $ erase_picture(19)
        $ erase_picture(20)
        $ erase_picture(21)
        $ erase_picture(22)
        $ erase_picture(23)
        $ erase_picture(24)
        $ erase_picture(25)
    elif menu_choice == _("Don't help him"):
        $ menu_choice = None
        $ set_switch("corruption_low", True)
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
        $ show_picture(1, "mamada25")
        $ fade_in()
        $ resolve_scene()
        Leyna "NO... I cannot help you I am a married woman"
        YoungVillager "You're going to leave me like this? you can't do that"
        $ show_picture(2, "mamada26")
        $ resolve_scene()
        Leyna "Sorry I have to go!"
        YoungVillager "Wait!"
        $ fade_out()
        $ erase_picture(1)
        $ erase_picture(2)
    $ ritual = 1
    call TransferPlayer("Festival", "Town2chicoencontrado_0", 12, 1, direction=2) from _call_Town2chicoencontrado_0_TransferPlayer
    $ fade_in()
    $ set_switch("find_youth", False)
    $ resolve_scene()
    return False

label Town2chicoencontrado(play_event = True, trigger = None): # event
    if is_erased("Town2chicoencontrado"):
        return None
    elif ritual >= 2:
        return None
    elif trigger == "event" and switch("find_youth"):
        call PlayEvent(play_event, "Town2chicoencontrado_0", "Town2chicoencontrado") from _call_Town2chicoencontrado_0_PlayEvent
        return (1, "", "Town2chicoencontrado_0")
    return None

label Town2NPCCantWaitBase:
    if not switch("leyna_alone"):
        $ resolve_scene()
        Villager "I can't wait for the festival to start"
        "( it's my chance to take off my office suit and walk around naked, 0 regrets hehehe.. )"
    if switch("leyna_alone"):
        Villager "I don't go very often to the river cause it's a \"just dick area\""
    $ resolve_scene()
    return False

label Town2NPCCantWait(play_event = True, trigger = None): # event
    if is_erased("Town2NPCCantWait"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2NPCCantWaitBase", "Town2NPCCantWait") from _call_Town2NPCCantWait_PlayEvent
        return (1, "", "Town2NPCCantWait")
    return None

label Town2mafiosoBase:
    if not switch("leyna_alone"):
        $ resolve_scene()
        Thug "Don't bother me, I'm waiting for a clien... mmm ... a friend"
    if switch("leyna_alone"):
        Thug "A pretty girl like you shouldn't be alone in this part of town"
        "All I'm saying is that shit happens, you know.."
    $ resolve_scene()
    return False

label Town2mafioso(play_event = True, trigger = None): # event
    if is_erased("Town2mafioso"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2mafiosoBase", "Town2mafioso") from _call_Town2mafioso_PlayEvent
        return (1, "", "Town2mafioso")
    return None

label Town2borrachoBase:
    DrunkOldMan "p\@rT!y! ..hehehe..."
    return False

label Town2borracho(play_event = True, trigger = None): # event
    if is_erased("Town2borracho"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2borrachoBase", "Town2borracho") from _call_Town2borracho_PlayEvent
        return (1, "", "Town2borracho")
    return None

label Town2NPCVillagerBase:
    Villager "There's a lot to see in the town, I recommend you visit the river"
    return False

label Town2NPCVillager(play_event = True, trigger = None): # event
    if is_erased("Town2NPCVillager"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2NPCVillagerBase", "Town2NPCVillager") from _call_Town2NPCVillager_PlayEvent
        return (1, "", "Town2NPCVillager")
    return None

label Town2musicapueblo_0:
    call PlaySound("music", "audio/Town1.ogg", volume=0.9, no_loop=False) from _call_Town2musicapueblo_0_PlaySound
    $ resolve_scene()
    $ tint_screen((0, 0, 0, 0), 60, True)
    return False

label Town2musicapueblo_2:
    call PlaySound("music", "audio/Town1.ogg", volume=0.9, no_loop=False) from _call_Town2musicapueblo_2_PlaySound
    $ resolve_scene()
    return False

label Town2musicapueblo(play_event = True, trigger = None): # parallel
    if is_erased("Town2musicapueblo"):
        return None
    elif trigger == "parallel" and ritual >= 2:
        call PlayEvent(play_event, "Town2musicapueblo_2", "Town2musicapueblo") from _call_Town2musicapueblo_2_PlayEvent
        return (0, "", "Town2musicapueblo_2")
    elif switch("find_youth"):
        return None
    elif trigger == "parallel":
        call PlayEvent(play_event, "Town2musicapueblo_0", "Town2musicapueblo") from _call_Town2musicapueblo_0_PlayEvent
        return (0, "", "Town2musicapueblo_0")
    return None

label Town2ToPoliceStationBase:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_Town2ToPoliceStation_PlaySound
    call TransferPlayer("PoliceStation", "Town2ToPoliceStation", 14, 12, direction=8) from _call_Town2ToPoliceStation_TransferPlayer
    $ resolve_scene()
    return False

label Town2ToPoliceStation(play_event = True, trigger = None): # event
    if is_erased("Town2ToPoliceStation"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2ToPoliceStationBase", "Town2ToPoliceStation") from _call_Town2ToPoliceStation_PlayEvent
        return (0, "", "Town2ToPoliceStation")
    return None

label Town2ToPoliceStation_v2Base:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_Town2ToPoliceStation_v2_PlaySound
    call TransferPlayer("PoliceStation", "Town2ToPoliceStation_v2", 14, 12, direction=8) from _call_Town2ToPoliceStation_v2_TransferPlayer
    $ resolve_scene()
    return False

label Town2ToPoliceStation_v2(play_event = True, trigger = None): # event
    if is_erased("Town2ToPoliceStation_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2ToPoliceStation_v2Base", "Town2ToPoliceStation_v2") from _call_Town2ToPoliceStation_v2_PlayEvent
        return (0, "", "Town2ToPoliceStation_v2")
    return None

label Town2ToPoliceStation_v3Base:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_Town2ToPoliceStation_v3_PlaySound
    call TransferPlayer("PoliceStation", "Town2ToPoliceStation_v3", 15, 12, direction=8) from _call_Town2ToPoliceStation_v3_TransferPlayer
    $ resolve_scene()
    return False

label Town2ToPoliceStation_v3(play_event = True, trigger = None): # event
    if is_erased("Town2ToPoliceStation_v3"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2ToPoliceStation_v3Base", "Town2ToPoliceStation_v3") from _call_Town2ToPoliceStation_v3_PlayEvent
        return (0, "", "Town2ToPoliceStation_v3")
    return None

label Town2PolicePosterBase:
    "Police station of Goddess cliff. to serve and protect."
    return False

label Town2PolicePoster(play_event = True, trigger = None): # event
    if is_erased("Town2PolicePoster"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2PolicePosterBase", "Town2PolicePoster") from _call_Town2PolicePoster_PlayEvent
        return (1, "", "Town2PolicePoster")
    return None

label Town2DataCityPosterBase:
    "Upper town"
    return False

label Town2DataCityPoster(play_event = True, trigger = None): # event
    if is_erased("Town2DataCityPoster"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2DataCityPosterBase", "Town2DataCityPoster") from _call_Town2DataCityPoster_PlayEvent
        return (1, "", "Town2DataCityPoster")
    return None

label Town2PillarBase:
    "Goddess Cliff: where dreams are lived day by day."
    return False

label Town2Pillar(play_event = True, trigger = None): # event
    if is_erased("Town2Pillar"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2PillarBase", "Town2Pillar") from _call_Town2Pillar_PlayEvent
        return (1, "", "Town2Pillar")
    return None

label Town2chicofestival_0:
    YoungVillager "it's not me but if you want to kiss me, go ahead"
    Leyna "No, thanks"
    return False

label Town2chicofestival(play_event = True, trigger = None): # event
    if is_erased("Town2chicofestival"):
        return None
    elif ritual >= 2:
        return None
    elif trigger == "event" and switch("find_youth"):
        call PlayEvent(play_event, "Town2chicofestival_0", "Town2chicofestival") from _call_Town2chicofestival_0_PlayEvent
        return (1, "", "Town2chicofestival_0")
    return None

label Town2NPCAnotherFestivalBoy_0:
    YoungVillager "Hey! ready for the kiss?"
    Leyna "You are not the guy I have to find!"
    return False

label Town2NPCAnotherFestivalBoy(play_event = True, trigger = None): # event
    if is_erased("Town2NPCAnotherFestivalBoy"):
        return None
    elif ritual >= 2:
        return None
    elif trigger == "event" and switch("find_youth"):
        call PlayEvent(play_event, "Town2NPCAnotherFestivalBoy_0", "Town2NPCAnotherFestivalBoy") from _call_Town2NPCAnotherFestivalBoy_0_PlayEvent
        return (1, "", "Town2NPCAnotherFestivalBoy_0")
    return None

label Town2LeynaJohanSex_v2_0(menu_choice = None):
    call Movement("Town2LeynaJohanSex_v2_0", "player", ["D","D","D","TURN_U"]) from _call_Town2LeynaJohanSex_v2_0_Movement
    $ resolve_scene()
    call PauseForBalloon("Town2LeynaJohanSex_v2_0") from _call_Town2LeynaJohanSex_v2_0_PauseForBalloon
    Johan "(... why do I feel this way?... I can't stop thinking about what just happened)"
    Leyna "Johan? are you all right?"
    Johan "... Let's go to the Inn right now"
    Leyna "??? What? (he's acting really weird...he's worrying me...he's not going to.... break up with me, right?"
    Johan "Come with me"
    Leyna "Su-sure"
    call Movement("Town2LeynaJohanSex_v2_0", "player", ["D","D","D"]) from _call_Town2LeynaJohanSex_v2_0_Movement_1
    $ fade_out()
    call TransferPlayer("Inn", "Town2LeynaJohanSex_v2_0", 8, 10, direction=8) from _call_Town2LeynaJohanSex_v2_0_TransferPlayer
    $ fade_in()
    call Movement("Town2LeynaJohanSex_v2_0", "player", ["U","U","U"]) from _call_Town2LeynaJohanSex_v2_0_Movement_2
    $ fade_out()
    call TransferPlayer("InnRooms", "Town2LeynaJohanSex_v2_0", 7, 17, direction=6) from _call_Town2LeynaJohanSex_v2_0_TransferPlayer_1
    $ fade_in()
    call Movement("Town2LeynaJohanSex_v2_0", "player", ["R","R","R","U","U"]) from _call_Town2LeynaJohanSex_v2_0_Movement_3
    $ show_picture(1, "johanfollar1")
    call PlaySound("sound", "audio/Close1.ogg", volume=0.9, no_loop=True) from _call_Town2LeynaJohanSex_v2_0_PlaySound
    $ resolve_scene()
    Leyna "Johan? what's wrong?"
    $ show_picture(2, "johanfollar2")
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_Town2LeynaJohanSex_v2_0_PlaySound_1
    $ resolve_scene()
    Leyna "Johan?"
    Johan "(Look at her... this woman... she is perfect)"
    Johan "Hm..."
    $ show_picture(3, "johanfollar3")
    $ resolve_scene()
    Leyna "!!!"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_Town2LeynaJohanSex_v2_0_PlaySound_2
    $ show_picture(4, "johanfollar4")
    $ resolve_scene()
    Leyna "(He has taken off my clothes... in such a... manly way I don't think I've ever seen Johan like that)"
    Johan "(After everything that has happened today.... I cannot stay the same... Leyna is my wife, this beautiful woman is mine)"
    Johan "(Almost everyone in town wants to fuck her and rightly so. I didn't realize how lucky I am to be with a woman like this)"
    Johan "(I have to make an effort for her, to give my best to satisfy her.... but all these guys wanting to be with her, it's such a big pressure...)"
    Johan "(I feel so insecure... I can't stop thinking about what just happened at the photo shoot)"
    "(BEWARE The decision you make now will have repercussions at the end of the story)"
    call GetChoice([_("I can't take the pressure"), _("NONSENSE! I will do my best! ")], value=menu_choice, called_from="Town2LeynaJohanSex_v2_0") from _call_Town2LeynaJohanSex_v2_0_GetChoice
    $ menu_choice = _return
    if menu_choice == _("I can't take the pressure"):
        $ menu_choice = None
        $ show_picture(5, "johanfollar13")
        $ resolve_scene()
        Johan "(Damn it, the pressure.... Why do I feel like this? it's like I have a crowd watching me)"
        Johan "(After so many years together with her.... now I feel as if it is the first time I am going to fuck my wife)"
        Johan "(I don't know if I'm feeling up to it!)"
        $ show_picture(6, "johanfollar8")
        $ resolve_scene()
        Leyna "!!! You're already going in? it's a bit... rushed"
        Johan "...."
        Johan "(Don't listen to her if I try hard enough... maybe .... maybe it's good enough)"
        pause
        $ show_picture(7, "johanfollar9")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2LeynaJohanSex_v2_0_PlaySound_3
        $ resolve_scene()
        Leyna "!!!"
        Johan "(I may have gone too fast... it's a little dry down there...)"
        Johan "(Why can't I stop thinking about stupid things? I'm not where I should be)"
        pause
        $ show_picture(8, "fotoerotica8")
        $ resolve_scene()
        $ flash_screen([255,255,255,170], 60, True)
        Johan "(Shit why do I have to think about that now?)"
        Leyna "Johan? are you okay? you feel a little... strange..."
        $ erase_picture(8)
        $ resolve_scene()
        Johan "Y-yes, I'm fine!"
        Johan "Pu-put yourself like this!"
        pause
        $ show_picture(8, "johanfollar10")
        stop bgs fadeout 1
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2LeynaJohanSex_v2_0_PlaySound_4
        $ resolve_scene()
        Johan "I like that!"
        Leyna "Ah ah ah!"
        Johan "(Looks like it's getting wet! very good, I just have to keep it up! and stop thinking so much!)"
        $ show_picture(9, "fotoerotica18")
        $ resolve_scene()
        Johan "(Shit, not again! Why do I have to be thinking about that shit all the time?)"
        Johan "(What the fuck? I'm going to cum already... normally I last much longer)"
        $ flash_screen([255,255,255,170], 60, True)
        stop bgs fadeout 1
        $ show_picture(10, "johanfollar11")
        $ resolve_scene()
        $ flash_screen([255,255,255,170], 60, True)
        Johan "AAAhh!"
        Leyna "??? (Already? ... that's been a bit ...)"
        Johan "(Fuck, I couldn't help it... Shit)"
        $ show_picture(11, "johanfollar14")
        $ resolve_scene()
        Leyna "That was... hahaha it was... well... I ehmmm I'm going rest a little bit... then we could go out for a while and have a drink if you want..."
        Johan "Hmmm yes ... sure... (Why is the atmosphere so uncomfortable? fuck... this has been a disaster)"
        Johan "Take a nap, I'll be downstairs waiting for you"
        Leyna "See you in half an hour or so!"
        Johan ".... Yeah, great..."
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
        $ set_switch("johan_and_leyna_sex", True)
        call GalleryViewed("johanfollar") from _call_Town2LeynaJohanSex_v2_0_GalleryViewed
        $ johan_leyna_sex = 1
        $ erase_picture(11)
        call TransferPlayer("Town2", "Town2LeynaJohanSex_v2_0", 28, 22, direction=2) from _call_Town2LeynaJohanSex_v2_0_TransferPlayer_2
        $ fade_in()
        call Movement("Town2LeynaJohanSex_v2_0", "player", ["D","D","TURN_U"]) from _call_Town2LeynaJohanSex_v2_0_Movement_4
        $ resolve_scene()
        Leyna "Would you like a beer?"
        Johan "Yes, of course... (I really need some beer)"
        Leyna "Let's go to the bar then"
        Johan "Sure..."
    elif menu_choice == _("NONSENSE! I will do my best! "):
        $ menu_choice = None
        $ show_picture(5, "johanfollar5")
        $ resolve_scene()
        Johan "(But what am I thinking? Leyna is my wife, among all the guys that tried to seduce her,she chose me)"
        Johan "(I will try my best to give you the best sex of your life I don't have to think so much, just enjoy the moment)"
        Leyna "Johan, are you okay?"
        Johan "Me? yeah!"
        $ show_picture(6, "johanfollar7")
        $ resolve_scene()
        Leyna "Ah!"
        Leyna "(He's!!! it's been a long time since he did this to me, he's doing it... very well... if he keeps on like this I'll be done soon)"
        Leyna "Keep going... keep going... Oh my God..."
        pause
        $ show_picture(7, "johanfollar8")
        $ resolve_scene()
        Johan "No, not yet"
        Leyna "Why did you stop?"
        Johan "Because I don't want you to cum yet, I'm going to make it last as long as I can!"
        $ show_picture(8, "johanfollar9")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2LeynaJohanSex_v2_0_PlaySound_5
        $ resolve_scene()
        Leyna "AH! ah! ah!"
        Johan "Do you like it?"
        Leyna "Hmmm!!"
        Johan "Tell me you like it, leyna! or I'll stop!"
        Leyna "(Johan has never talked dirty to me like that before ...) I like it! Don't stop please keep going!"
        Johan "Very good, come here"
        Leyna "!!!"
        pause
        $ show_picture(9, "johanfollar10")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2LeynaJohanSex_v2_0_PlaySound_6
        $ resolve_scene()
        Johan "That's right!"
        Leyna "Ahh! Keep going! Keep fucking me like this!"
        Johan "You don't have to tell me, I won't stop until you cum!"
        Leyna "AH!!! I'M GOING TO CUM!!"
        Johan "ME TOO!"
        pause
        $ show_picture(10, "johanfollar11")
        stop bgs fadeout 1
        $ resolve_scene()
        $ flash_screen([255,255,255,170], 60, True)
        $ flash_screen([255,255,255,170], 60, True)
        Johan "AH!!"
        Leyna "AAH! shit! (I can't stop shaking, it's the first orgasm I've had in months)"
        pause
        $ show_picture(11, "johanfollar12")
        $ resolve_scene()
        Johan "What do you think?"
        Leyna "Unbelievable... I don't know what's wrong with you today... but I wouldn't mind if you kept it up a little longer hahaha"
        Johan "Well, no problem with that as long as you want it, we can do this every day hahaha"
        Leyna "Hahaha well, every day... we'll see..."
        Leyna "Shall we go for a drink?"
        Johan "Sure! let's go to the bar for a beer!"
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
        $ set_switch("johan_and_leyna_sex", True)
        call GalleryViewed("johanfollar") from _call_Town2LeynaJohanSex_v2_0_GalleryViewed_1
        $ johan_leyna_sex = 2
        $ erase_picture(11)
        call TransferPlayer("Town2", "Town2LeynaJohanSex_v2_0", 28, 22, direction=2) from _call_Town2LeynaJohanSex_v2_0_TransferPlayer_3
        $ fade_in()
    $ resolve_scene()
    return False

label Town2LeynaJohanSex_v2(play_event = True, trigger = None): # event
    if is_erased("Town2LeynaJohanSex_v2"):
        return None
    elif switch("johan_and_leyna_sex"):
        return None
    elif trigger == "event" and switch("erotic_photos_together"):
        call PlayEvent(play_event, "Town2LeynaJohanSex_v2_0", "Town2LeynaJohanSex_v2") from _call_Town2LeynaJohanSex_v2_0_PlayEvent
        return (0, "", "Town2LeynaJohanSex_v2_0")
    return None

label Town2LeynaJohanSex_v3_0(menu_choice = None):
    call Movement("Town2LeynaJohanSex_v3_0", "player", ["D","D","D","TURN_U"]) from _call_Town2LeynaJohanSex_v3_0_Movement
    $ resolve_scene()
    call PauseForBalloon("Town2LeynaJohanSex_v3_0") from _call_Town2LeynaJohanSex_v3_0_PauseForBalloon
    Johan "(... why do I feel this way?... I can't stop thinking about what just happened)"
    Leyna "Johan? are you all right?"
    Johan "... Let's go to the Inn right now"
    Leyna "??? What? (he's acting really weird...he's worrying me...he's not going to.... break up with me, right?"
    Johan "Come with me"
    Leyna "Su-sure"
    call Movement("Town2LeynaJohanSex_v3_0", "player", ["D","D","D"]) from _call_Town2LeynaJohanSex_v3_0_Movement_1
    $ fade_out()
    call TransferPlayer("Inn", "Town2LeynaJohanSex_v3_0", 8, 10, direction=8) from _call_Town2LeynaJohanSex_v3_0_TransferPlayer
    $ fade_in()
    call Movement("Town2LeynaJohanSex_v3_0", "player", ["U","U","U"]) from _call_Town2LeynaJohanSex_v3_0_Movement_2
    $ fade_out()
    call TransferPlayer("InnRooms", "Town2LeynaJohanSex_v3_0", 7, 17, direction=6) from _call_Town2LeynaJohanSex_v3_0_TransferPlayer_1
    $ fade_in()
    call Movement("Town2LeynaJohanSex_v3_0", "player", ["R","R","R","U","U"]) from _call_Town2LeynaJohanSex_v3_0_Movement_3
    $ show_picture(1, "johanfollar1")
    call PlaySound("sound", "audio/Close1.ogg", volume=0.9, no_loop=True) from _call_Town2LeynaJohanSex_v3_0_PlaySound
    $ resolve_scene()
    Leyna "Johan? what's wrong?"
    $ show_picture(2, "johanfollar2")
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_Town2LeynaJohanSex_v3_0_PlaySound_1
    $ resolve_scene()
    Leyna "Johan?"
    Johan "(Look at her... this woman... she is perfect)"
    Johan "Hm..."
    $ show_picture(3, "johanfollar3")
    $ resolve_scene()
    Leyna "!!!"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_Town2LeynaJohanSex_v3_0_PlaySound_2
    $ show_picture(4, "johanfollar4")
    $ resolve_scene()
    Leyna "(He has taken off my clothes... in such a... manly way I don't think I've ever seen Johan like that)"
    Johan "(After everything that has happened today.... I cannot stay the same... Leyna is my wife, this beautiful woman is mine)"
    Johan "(Almost everyone in town wants to fuck her and rightly so. I didn't realize how lucky I am to be with a woman like this)"
    Johan "(I have to make an effort for her, to give my best to satisfy her.... but all these guys wanting to be with her, it's such a big pressure...)"
    Johan "(I feel so insecure... I can't stop thinking about what just happened at the photo shoot)"
    "(BEWARE The decision you make now will have repercussions at the end of the story)"
    call GetChoice([_("I can't take the pressure"), _("NONSENSE! I will do my best! ")], value=menu_choice, called_from="Town2LeynaJohanSex_v3_0") from _call_Town2LeynaJohanSex_v3_0_GetChoice
    $ menu_choice = _return
    if menu_choice == _("I can't take the pressure"):
        $ menu_choice = None
        $ show_picture(5, "johanfollar13")
        $ resolve_scene()
        Johan "(Damn it, the pressure.... Why do I feel like this? it's like I have a crowd watching me)"
        Johan "(After so many years together with her.... now I feel as if it is the first time I am going to fuck my wife)"
        Johan "(I don't know if I'm feeling up to it!)"
        $ show_picture(6, "johanfollar8")
        $ resolve_scene()
        Leyna "!!! You're already going in? it's a bit... rushed"
        Johan "...."
        Johan "(Don't listen to her if I try hard enough... maybe .... maybe it's good enough)"
        pause
        $ show_picture(7, "johanfollar9")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2LeynaJohanSex_v3_0_PlaySound_3
        $ resolve_scene()
        Leyna "!!!"
        Johan "(I may have gone too fast... it's a little dry down there...)"
        Johan "(Why can't I stop thinking about stupid things? I'm not where I should be)"
        pause
        $ show_picture(8, "fotoerotica8")
        $ resolve_scene()
        $ flash_screen([255,255,255,170], 60, True)
        Johan "(Shit why do I have to think about that now?)"
        Leyna "Johan? are you okay? you feel a little... strange..."
        $ erase_picture(8)
        $ resolve_scene()
        Johan "Y-yes, I'm fine!"
        Johan "Pu-put yourself like this!"
        pause
        $ show_picture(8, "johanfollar10")
        stop bgs fadeout 1
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2LeynaJohanSex_v3_0_PlaySound_4
        $ resolve_scene()
        Johan "I like that!"
        Leyna "Ah ah ah!"
        Johan "(Looks like it's getting wet! very good, I just have to keep it up! and stop thinking so much!)"
        $ show_picture(9, "fotoerotica18")
        $ resolve_scene()
        Johan "(Shit, not again! Why do I have to be thinking about that shit all the time?)"
        Johan "(What the fuck? I'm going to cum already... normally I last much longer)"
        $ flash_screen([255,255,255,170], 60, True)
        stop bgs fadeout 1
        $ show_picture(10, "johanfollar11")
        $ resolve_scene()
        $ flash_screen([255,255,255,170], 60, True)
        Johan "AAAhh!"
        Leyna "??? (Already? ... that's been a bit ...)"
        Johan "(Fuck, I couldn't help it... Shit)"
        $ show_picture(11, "johanfollar14")
        $ resolve_scene()
        Leyna "That was... hahaha it was... well... I ehmmm I'm going rest a little bit... then we could go out for a while and have a drink if you want..."
        Johan "Hmmm yes ... sure... (Why is the atmosphere so uncomfortable? fuck... this has been a disaster)"
        Johan "Take a nap, I'll be downstairs waiting for you"
        Leyna "See you in half an hour or so!"
        Johan ".... Yeah, great..."
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
        $ set_switch("johan_and_leyna_sex", True)
        call GalleryViewed("johanfollar") from _call_Town2LeynaJohanSex_v3_0_GalleryViewed
        $ johan_leyna_sex = 1
        $ erase_picture(11)
        call TransferPlayer("Town2", "Town2LeynaJohanSex_v3_0", 28, 22, direction=2) from _call_Town2LeynaJohanSex_v3_0_TransferPlayer_2
        $ fade_in()
        call Movement("Town2LeynaJohanSex_v3_0", "player", ["D","D","TURN_U"]) from _call_Town2LeynaJohanSex_v3_0_Movement_4
        $ resolve_scene()
        Leyna "Would you like a beer?"
        Johan "Yes, of course... (I really need some beer)"
        Leyna "Let's go to the bar then"
        Johan "Sure..."
    elif menu_choice == _("NONSENSE! I will do my best! "):
        $ menu_choice = None
        $ show_picture(5, "johanfollar5")
        $ resolve_scene()
        Johan "(But what am I thinking? Leyna is my wife, among all the guys that tried to seduce her,she chose me)"
        Johan "(I will try my best to give you the best sex of your life I don't have to think so much, just enjoy the moment)"
        Leyna "Johan, are you okay?"
        Johan "Me? yeah!"
        $ show_picture(6, "johanfollar7")
        $ resolve_scene()
        Leyna "Ah!"
        Leyna "(He's!!! it's been a long time since he did this to me, he's doing it... very well... if he keeps on like this I'll be done soon)"
        Leyna "Keep going... keep going... Oh my God..."
        pause
        $ show_picture(7, "johanfollar8")
        $ resolve_scene()
        Johan "No, not yet"
        Leyna "Why did you stop?"
        Johan "Because I don't want you to cum yet, I'm going to make it last as long as I can!"
        $ show_picture(8, "johanfollar9")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2LeynaJohanSex_v3_0_PlaySound_5
        $ resolve_scene()
        Leyna "AH! ah! ah!"
        Johan "Do you like it?"
        Leyna "Hmmm!!"
        Johan "Tell me you like it, leyna! or I'll stop!"
        Leyna "(Johan has never talked dirty to me like that before ...) I like it! Don't stop please keep going!"
        Johan "Very good, come here"
        Leyna "!!!"
        pause
        $ show_picture(9, "johanfollar10")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2LeynaJohanSex_v3_0_PlaySound_6
        $ resolve_scene()
        Johan "That's right!"
        Leyna "Ahh! Keep going! Keep fucking me like this!"
        Johan "You don't have to tell me, I won't stop until you cum!"
        Leyna "AH!!! I'M GOING TO CUM!!"
        Johan "ME TOO!"
        pause
        $ show_picture(10, "johanfollar11")
        stop bgs fadeout 1
        $ resolve_scene()
        $ flash_screen([255,255,255,170], 60, True)
        $ flash_screen([255,255,255,170], 60, True)
        Johan "AH!!"
        Leyna "AAH! shit! (I can't stop shaking, it's the first orgasm I've had in months)"
        pause
        $ show_picture(11, "johanfollar12")
        $ resolve_scene()
        Johan "What do you think?"
        Leyna "Unbelievable... I don't know what's wrong with you today... but I wouldn't mind if you kept it up a little longer hahaha"
        Johan "Well, no problem with that as long as you want it, we can do this every day hahaha"
        Leyna "Hahaha well, every day... we'll see..."
        Leyna "Shall we go for a drink?"
        Johan "Sure! let's go to the bar for a beer!"
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
        $ set_switch("johan_and_leyna_sex", True)
        call GalleryViewed("johanfollar") from _call_Town2LeynaJohanSex_v3_0_GalleryViewed_1
        $ johan_leyna_sex = 2
        $ erase_picture(11)
        call TransferPlayer("Town2", "Town2LeynaJohanSex_v3_0", 28, 22, direction=2) from _call_Town2LeynaJohanSex_v3_0_TransferPlayer_3
        $ fade_in()
    $ resolve_scene()
    return False

label Town2LeynaJohanSex_v3(play_event = True, trigger = None): # event
    if is_erased("Town2LeynaJohanSex_v3"):
        return None
    elif switch("johan_and_leyna_sex"):
        return None
    elif trigger == "event" and switch("erotic_photos_together"):
        call PlayEvent(play_event, "Town2LeynaJohanSex_v3_0", "Town2LeynaJohanSex_v3") from _call_Town2LeynaJohanSex_v3_0_PlayEvent
        return (0, "", "Town2LeynaJohanSex_v3_0")
    return None

label Town2eventoflashback_0:
    call Movement("Town2eventoflashback_0", "player", ["TURN_U"]) from _call_Town2eventoflashback_0_Movement
    $ resolve_scene()
    Johan "I have to go for a walk alone... I need some air..."
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "!!! Of course... whatever you need Johan.... Don't take what has happened too harshly, we are all a bit drunk and we were playing"
    Johan "Y-yeah, sure... I'll see you in a bit, okay? don't worry, I'm fine"
    Leyna "Yes... see you in a little while..."
    $ fade_out()
    $ erase_picture(1)
    call ChangePartyMember("Johan", False) from _call_Town2eventoflashback_0_ChangePartyMember
    call Movement("Town2eventoflashback_0", "player", ["L","L","L"]) from _call_Town2eventoflashback_0_Movement_1
    $ fade_in()
    $ resolve_scene()
    call PauseForBalloon("Town2eventoflashback_0") from _call_Town2eventoflashback_0_PauseForBalloon
    Leyna "Fuck..."
    Leyna "I should go to work in the hotsprings... But after what happened... I don't know if I want to go again..."
    $ set_self_switch("Town2","Town2eventoflashback","A",True)
    return False

label Town2eventoflashback_1:
    call Movement("Town2eventoflashback_1", "player", ["TURN_U"]) from _call_Town2eventoflashback_1_Movement
    $ resolve_scene()
    Johan "I have to go for a walk alone... I need some air..."
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "!!! Of course... whatever you need Johan.... Don't take what has happened too harshly, we are all a bit drunk and we were playing"
    Johan "Y-yeah, sure... I'll see you in a bit, okay? don't worry, I'm fine"
    Leyna "Yes... see you in a little while..."
    $ fade_out()
    $ erase_picture(1)
    call ChangePartyMember("Johan", False) from _call_Town2eventoflashback_1_ChangePartyMember
    call Movement("Town2eventoflashback_1", "player", ["L","L","L"]) from _call_Town2eventoflashback_1_Movement_1
    $ fade_in()
    $ resolve_scene()
    call PauseForBalloon("Town2eventoflashback_1") from _call_Town2eventoflashback_1_PauseForBalloon
    Leyna "Fuck..."
    Leyna "I should go to work in the hotsprings... But after what happened... I don't know if I want to go again..."
    $ set_self_switch("Town2","Town2eventoflashback","A",True)
    return False

label Town2eventoflashback(play_event = True, trigger = None): # autorun
    if is_erased("Town2eventoflashback"):
        return None
    elif self_switch("Town2","Town2eventoflashback","A"):
        return None
    elif trigger == "autorun" and bet_together >= 2:
        call PlayEvent(play_event, "Town2eventoflashback_1", "Town2eventoflashback") from _call_Town2eventoflashback_1_PlayEvent
        return (0, "", "Town2eventoflashback_1")
    elif trigger == "autorun" and bet_together >= 1:
        call PlayEvent(play_event, "Town2eventoflashback_0", "Town2eventoflashback") from _call_Town2eventoflashback_0_PlayEvent
        return (0, "", "Town2eventoflashback_0")
    return None

label Town2NPCFountainGuyBase:
    OldVillager "I always come here to relax, it's a nice place..."
    return False

label Town2NPCFountainGuy(play_event = True, trigger = None): # event
    if is_erased("Town2NPCFountainGuy"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2NPCFountainGuyBase", "Town2NPCFountainGuy") from _call_Town2NPCFountainGuy_PlayEvent
        return (1, "", "Town2NPCFountainGuy")
    return None

label Town2hombrepaseando3Base:
    Villager "All work and no play makes jack a dull boy..."
    return False

label Town2hombrepaseando3(play_event = True, trigger = None): # event
    if is_erased("Town2hombrepaseando3"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2hombrepaseando3Base", "Town2hombrepaseando3") from _call_Town2hombrepaseando3_PlayEvent
        return (1, "", "Town2hombrepaseando3")
    return None

label Town2JohanIWasLookingForYou_1:
    call PauseForBalloon("Town2EV070_1") from _call_Town2EV070_1_PauseForBalloon
    call Movement("Town2EV070_1", "Town2Leyna", ["TURN_U","U"]) from _call_Town2EV070_1_Movement
    $ resolve_scene()
    Leyna "Johan! I was looking for you!"
    Johan "What a coincidence, me too, I have a gift for..."
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Wait! I also have something to tell you... the thing you gave me... ahem... I've already tried it"
    Johan "oh! i-i see... well... hmmm and well? what did you think?"
    Leyna "Well... I"
    $ erase_picture(1)
    $ show_transparent(1, "plano_mujer_sonrisa", width=1600, height=900)
    $ resolve_scene()
    Leyna "I liked it... I liked it very much"
    Johan "WOW REALLY?!"
    Leyna "Shhh! don't raise your voice so much, they will hear us"
    Johan "I'm s-sorry, I got carried away with the emotion"
    Johan "The truth is that I also wanted to tell you something related to... that"
    $ erase_picture(1)
    $ show_transparent(1, "expresion_neutral_mujer", width=1600, height=900)
    $ resolve_scene()
    Leyna "Tell me"
    Johan "You see... I bought you another toy..."
    Johan "You're supposed to wear it for quite a while to... ahem well... be ready for us to do it later... you know..."
    Leyna "Oh! I see... sure... it's a good idea... I see that you are excited about it hehehehehehe"
    Johan "yes! of course!"
    Leyna "Give me a second and I'll put it on right away, honey... I'll be right back"
    Johan "Of course! (WOw I can't believe this is happening)"
    $ fade_out()
    call TransferPlayer("Town2", "Town2EV070_1", 21, 24, direction=2) from _call_Town2EV070_1_TransferPlayer
    call SetEventLocation("Town2EV070_1", "Town2Leyna", 28, 24) from _call_Town2EV070_1_setloc
    $ erase_picture(1)
    $ fade_in()
    call Movement("Town2EV070_1", "Town2Leyna", ["L","L","L","L","L","L"]) from _call_Town2EV070_1_Movement_1
    call Movement("Town2EV070_1", "player", ["TURN_R"]) from _call_Town2EV070_1_Movement_2
    $ resolve_scene()
    call PauseForBalloon("Town2EV070_1") from _call_Town2EV070_1_PauseForBalloon_1
    Johan "Well?"
    Leyna "I-I've already put it on... it feels good... but the lube it came with... it feels a little weird... it makes me feel really weirdly warm in there"
    Johan "Oh! (I forgot about the herbs) don't worry, it's normal"
    Leyna "I see... so it's all good then"
    Johan "Great then! let's go to...."
    call SetEventLocation("Town2EV070_1", "Town2dueobar", 21, 18) from _call_Town2EV070_1_setloc_1
    call Movement("Town2EV070_1", "Town2dueobar", ["D","D","D","D","D","D"]) from _call_Town2EV070_1_Movement_3
    $ resolve_scene()
    call PauseForBalloon("Town2EV070_1") from _call_Town2EV070_1_PauseForBalloon_2
    Barman "Leyna! I've been looking for you!"
    call Movement("Town2EV070_1", "player", ["TURN_U"]) from _call_Town2EV070_1_Movement_4
    call Movement("Town2EV070_1", "Town2Leyna", ["TURN_U"]) from _call_Town2EV070_1_Movement_5
    $ resolve_scene()
    $ resolve_scene()
    call PauseForBalloon("Town2EV070_1") from _call_Town2EV070_1_PauseForBalloon_3
    Leyna "Boss? it's not time for my shift to start yet"
    Johan "??? (he is the owner of the bar)"
    Barman "I know, I'm sorry, but I have an emergency and I need your help with the food stand at the festival"
    Leyna "Just now? but I was with my husband...."
    Johan "Don't worry, honey, work comes first"
    Leyna "Yeah... I'm sorry Johan, you're right, I guess I'll have to go to the festival"
    Johan "Yes, I'm going to the inn to pick up my festival clothes and I'll be around for a drink with the guys to keep you company"
    Leyna "Okay, thank you"
    Barman "Perfect, thank you very much for understanding me guys, Leyna I have your uniform for the festival I will accompany you there"
    Leyna "Sure..."
    $ fade_out()
    call ChangePartyMember("Leyna", True) from _call_Town2EV070_1_ChangePartyMember
    call ChangePartyMember("Johan", False) from _call_Town2EV070_1_ChangePartyMember_1
    call TransferPlayer("Path", "Town2EV070_1", 5, 11, direction=4) from _call_Town2EV070_1_TransferPlayer_1
    $ fade_in()
    $ resolve_scene()
    Leyna "The boss has already entered the locker room but forgot to give me my uniform"
    Leyna "It's a good thing I'm wearing my festival clothes underneath so I can get in without a problem"
    Leyna "I guess I'm going to have to go into the locker room with the boss in it... anyway, it's certainly not the first dick I've seen since I've been in town"
    Leyna "I should play it down"
    $ fade_out()
    $ show_picture(1, "cambiandose1")
    $ fade_in()
    $ resolve_scene()
    Barman "Le-leyna? I didn't expect you to come in yet..."
    Leyna "I know... but you forgot to give me the uniform"
    "Barman. Shit! it's true, sorry, in my haste I forgot it"
    Barman "Here you have the uniform"
    Barman "Try it on and see how it looks on you"
    Leyna "Wh-what? here and now?"
    Barman "Hmmm so yes, what's the problem? Leyna I've already seen you naked... or at least almost naked for sure"
    Leyna "Yeah... but there are more people here"
    Barman "I didn't take you for such a shy girl... come on, we're all too old to worry about these things, aren't we?"
    Leyna "I guess you're right..."
    $ show_picture(2, "cambiandose2")
    $ resolve_scene()
    Leyna "(Shit, I forgot for a second that I'm wearing that toy)..."
    Leyna "(I'm going to have to be very careful not to let them notice)"
    Barman "Leyna? are you okay? you're making a very strange face"
    $ show_picture(3, "cambiandose3")
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_Town2EV070_1_PlaySound
    $ resolve_scene()
    Leyna "Y-yeah, I'm fine, don't worry..."
    Barman "(Boy is she doing it...I'll never get tired of looking at that pair of tits!)"
    Villager "(Fuck she is undressing herself in front of us, and we are here alone with her... is she some kind of nympho?)"
    $ show_picture(4, "cambiandose4")
    $ resolve_scene()
    Leyna "Hey, if you're going to stare, you could at least pretend you're not"
    Barman "So-sorry"
    Villager "Yeah sorry, it's just that the views are too good not to look at"
    Villager2 "You have to understand, not every day we have such a good show"
    Leyna "Yeah well... enjoy then"
    Villager "Yes hahaha that's what we will do"
    pause
    $ show_picture(5, "cambiandose5")
    $ resolve_scene()
    Leyna "Well, the show is over, the uniform suits me, how did you know what my size is?"
    Barman "I have a good eye for these things"
    $ show_picture(6, "cambiandose7")
    $ resolve_scene()
    Leyna "(Well it seems that no one has noticed, I have stuck my ass to the wall and no one should have seen anything)"
    Leyna "(I hope it doesn't show too much I still have to get to the food stand)"
    pause
    $ show_picture(7, "cambiandose8")
    $ resolve_scene()
    Leyna "(Although this damn uniform is too revealing even to go to the festival)"
    Leyna "(I'm practically naked and with my pussy in the air, any sudden movement and they will see everything)"
    Leyna "(My God, between everyone looking at me right now and the fact that I'm wearing this butt plug... I'm feeling too excited... this heat...)"
    if switch("corruption_average"):
        $ show_picture(8, "cambiandose9")
        $ resolve_scene()
        Leyna "What do you guys think? Do you like my new uniform?"
        Leyna "(what am I doing? why am I provoking them like this? ...I feel sexy but...most of all I am very horny...)"
        Villager "You look spectacularly sexy beautiful, later I will visit you at the food stand"
        Villager2 "Yes... and if you want to have a good time right now we can throw you a little party right here"
        Leyna "Keep dreaming guys... I'm a married woman"
        $ show_picture(9, "cambiandose10")
        $ resolve_scene()
        Leyna "See you guys"
        Barman "(Is that?... Jesus)"
    if switch("corruption_low"):
        $ show_picture(8, "cambiandose6")
        $ resolve_scene()
        Leyna "W-well I'm going now"
        Villager "Oh come on... Wouldn't you rather stay and have a good time with us? We know how to treat a girl like you"
        Leyna "A girl like me? n-no thank you very much, I'm married and I have to go to work at the food stand"
        Villager2 "Then we'll have to visit you at the food stand, with that uniform I'm getting hungry already"
        Leyna "Su-sure... stop by anytime"
        $ show_picture(9, "cambiandose10")
        $ resolve_scene()
        Leyna "(they don't seem to have noticed... that was too risky for my taste)"
        Leyna "(but the lubricant... is that what's making me so excited? or am I just changing?)"
        Leyna "(better not to think too much about it and go to the food stand as soon as possible)"
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
    call TransferPlayer("Festival", "Town2EV070_1", 12, 1, direction=0) from _call_Town2EV070_1_TransferPlayer_2
    $ butt_plug = 3
    $ fade_in()
    $ resolve_scene()
    Leyna "All right, I have to go to the food stand to start working!"
    call GalleryViewed("cambiandose") from _call_Town2EV070_1_GalleryViewed
    return False

label Town2JohanIWasLookingForYou(play_event = True, trigger = None): # autorun
    if is_erased("Town2JohanIWasLookingForYou"):
        return None
    elif butt_plug >= 3:
        return None
    elif trigger == "autorun" and butt_plug >= 2:
        call PlayEvent(play_event, "Town2JohanIWasLookingForYou_1", "Town2JohanIWasLookingForYou") from _call_Town2JohanIWasLookingForYou_1_PlayEvent
        return (0, "", "Town2JohanIWasLookingForYou_1")
    return None

label Town2ClothingSignBase:
    "Happy pig Clothes and accessories"
    return False

label Town2ClothingSign(play_event = True, trigger = None): # event
    if is_erased("Town2ClothingSign"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2ClothingSignBase", "Town2ClothingSign") from _call_Town2ClothingSign_PlayEvent
        return (1, "", "Town2ClothingSign")
    return None

label Town2StoreSignBase:
    "General goods."
    return False

label Town2StoreSign(play_event = True, trigger = None): # event
    if is_erased("Town2StoreSign"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2StoreSignBase", "Town2StoreSign") from _call_Town2StoreSign_PlayEvent
        return (1, "", "Town2StoreSign")
    return None

label Town2finalfiestafestival_0:
    call PauseForBalloon("Town2finalfiestafestival_0") from _call_Town2finalfiestafestival_0_PauseForBalloon
    Johan "My God, my head is killing me... I have to find Leyna, where is she?"
    $ fade_out()
    $ show_picture(1, "reencuentro1", width=814, height=624)
    $ fade_in()
    $ resolve_scene()
    "An hour later..."
    Johan "I've been looking for her for a long time, she wasn't in the inn room, where did she go?"
    Johan "I still can't quite remember what happened last night... and I don't know if I want to, both of us have done something we might regret"
    Johan "or nothing has happened... which I wish it were true"
    Johan "!!!!"
    Johan "Wait a second... that's Leyna! And she's with... Shit, she's with Alexa..."
    pause
    $ show_picture(2, "reencuentro2", width=814, height=624)
    $ resolve_scene()
    Johan "H-hey girls... I've been looking for you..."
    Leyna "Hi sweetie!"
    Alexa "Hey Johan! how's it going? how's your hangover? hahahaha"
    Johan "(Wow... they don't seem to be angry... in fact they seem quite happy... so surely nothing happened yesterday?)"
    Johan "(it must have been a bad dream... my god I feel so relieved, I don't know what would have happened if  all that I was imagining was true)"
    Johan "W-well, I feel like I've been run over by a car, but I'm okay I guess"
    Johan "And you, don't you have a hangover?"
    Alexa "Well... yes and no, we woke up shattered like you, but I have taught Leyna the trick of how to get rid of hangovers"
    Johan "The trick?"
    Alexa "Yeah! nothing like drinking a couple of beers and the hangover goes away hahahaha"
    Johan "Oh... I see... and the two of you have met in town?"
    Alexa "Oh no... yesterday I saw that your wife was quite drunk and I invited her to spend the night in my room... since you had disappeared, where were you?"
    Johan "I... I don't know, I woke up this morning in a field on the outskirts of town"
    Johan "So you are well Leyna?"
    $ show_picture(3, "reencuentro3", width=814, height=624)
    $ resolve_scene()
    Leyna "Hahaha yeah, I'm fine.... I'm still a little drunk and the beers we had with our friend didn't help hahaha"
    Johan "Friend?...ah, this guy?"
    $ erase_picture(3)
    $ resolve_scene()
    Villager "zzzzz...."
    Johan "It looks like he's out of action..."
    Alexa "Yes... our friend here is out cold... he hasn't been able to sleep much tonight hehehehehehe"
    Johan "???"
    Johan "I see... Well Leyna, will you come with me?"
    Leyna "Sure, let's go for a walk, at least I got a good night's sleep"
    Alexa "In a while I will go to the river to cool off, the cold water is also very good for the hangover, we will be almost all day out there, so come if you want to"
    Johan "Sure... we will consider it... let's go Leyna?"
    Leyna "Sure!"
    Alexa "Well guys, see you later"
    Leyna "Of course! see you later!"
    $ fade_out()
    $ erase_picture(1)
    $ erase_picture(2)
    call TransferPlayer("Town2", "Town2finalfiestafestival_0", 1, 21, direction=6) from _call_Town2finalfiestafestival_0_TransferPlayer
    call ChangePartyMember("Leyna", True) from _call_Town2finalfiestafestival_0_ChangePartyMember
    call Movement("Town2finalfiestafestival_0", "player", ["R","R"]) from _call_Town2finalfiestafestival_0_Movement
    $ fade_in()
    $ resolve_scene()
    Johan "Well, what could we do today?"
    Leyna "We can always go to the river with Alexa"
    Johan "I guess so"
    Leyna "You know what? Look, let's go to the river, I think we could both use a little hangover relief and a chance to clear our heads a bit"
    Johan "You are right"
    $ set_self_switch("Town2","Town2finalfiestafestival","A",True)
    return False

label Town2finalfiestafestival(play_event = True, trigger = None): # event
    if is_erased("Town2finalfiestafestival"):
        return None
    elif self_switch("Town2","Town2finalfiestafestival","A"):
        return None
    elif switch("river_3"):
        return None
    elif trigger == "event" and switch("party_at_festival"):
        call PlayEvent(play_event, "Town2finalfiestafestival_0", "Town2finalfiestafestival") from _call_Town2finalfiestafestival_0_PlayEvent
        return (0, "", "Town2finalfiestafestival_0")
    return None

label Town2finalfiestafestival_v2_0:
    call PauseForBalloon("Town2finalfiestafestival_v2_0") from _call_Town2finalfiestafestival_v2_0_PauseForBalloon
    Johan "My God, my head is killing me... I have to find Leyna, where is she?"
    $ fade_out()
    $ show_picture(1, "reencuentro1", width=814, height=624)
    $ fade_in()
    $ resolve_scene()
    "An hour later..."
    Johan "I've been looking for her for a long time, she wasn't in the inn room, where did she go?"
    Johan "I still can't quite remember what happened last night... and I don't know if I want to, both of us have done something we might regret"
    Johan "or nothing has happened... which I wish it were true"
    Johan "!!!!"
    Johan "Wait a second... that's Leyna! And she's with... Shit, she's with Alexa..."
    pause
    $ show_picture(2, "reencuentro2", width=814, height=624)
    $ resolve_scene()
    Johan "H-hey girls... I've been looking for you..."
    Leyna "Hi sweetie!"
    Alexa "Hey Johan! how's it going? how's your hangover? hahahaha"
    Johan "(Wow... they don't seem to be angry... in fact they seem quite happy... so surely nothing happened yesterday?)"
    Johan "(it must have been a bad dream... my god I feel so relieved, I don't know what would have happened if  all that I was imagining was true)"
    Johan "W-well, I feel like I've been run over by a car, but I'm okay I guess"
    Johan "And you, don't you have a hangover?"
    Alexa "Well... yes and no, we woke up shattered like you, but I have taught Leyna the trick of how to get rid of hangovers"
    Johan "The trick?"
    Alexa "Yeah! nothing like drinking a couple of beers and the hangover goes away hahahaha"
    Johan "Oh... I see... and the two of you have met in town?"
    Alexa "Oh no... yesterday I saw that your wife was quite drunk and I invited her to spend the night in my room... since you had disappeared, where were you?"
    Johan "I... I don't know, I woke up this morning in a field on the outskirts of town"
    Johan "So you are well Leyna?"
    $ show_picture(3, "reencuentro3", width=814, height=624)
    $ resolve_scene()
    Leyna "Hahaha yeah, I'm fine.... I'm still a little drunk and the beers we had with our friend didn't help hahaha"
    Johan "Friend?...ah, this guy?"
    $ erase_picture(3)
    $ resolve_scene()
    Villager "zzzzz...."
    Johan "It looks like he's out of action..."
    Alexa "Yes... our friend here is out cold... he hasn't been able to sleep much tonight hehehehehehe"
    Johan "???"
    Johan "I see... Well Leyna, will you come with me?"
    Leyna "Sure, let's go for a walk, at least I got a good night's sleep"
    Alexa "In a while I will go to the river to cool off, the cold water is also very good for the hangover, we will be almost all day out there, so come if you want to"
    Johan "Sure... we will consider it... let's go Leyna?"
    Leyna "Sure!"
    Alexa "Well guys, see you later"
    Leyna "Of course! see you later!"
    $ fade_out()
    $ erase_picture(1)
    $ erase_picture(2)
    call TransferPlayer("Town2", "Town2finalfiestafestival_v2_0", 1, 21, direction=6) from _call_Town2finalfiestafestival_v2_0_TransferPlayer
    call ChangePartyMember("Leyna", True) from _call_Town2finalfiestafestival_v2_0_ChangePartyMember
    call Movement("Town2finalfiestafestival_v2_0", "player", ["R","R"]) from _call_Town2finalfiestafestival_v2_0_Movement
    $ fade_in()
    $ resolve_scene()
    Johan "Well, what could we do today?"
    Leyna "We can always go to the river with Alexa"
    Johan "I guess so"
    Leyna "You know what? Look, let's go to the river, I think we could both use a little hangover relief and a chance to clear our heads a bit"
    Johan "You are right"
    $ set_self_switch("Town2","Town2finalfiestafestival_v2","A",True)
    return False

label Town2finalfiestafestival_v2(play_event = True, trigger = None): # event
    if is_erased("Town2finalfiestafestival_v2"):
        return None
    elif self_switch("Town2","Town2finalfiestafestival_v2","A"):
        return None
    elif switch("river_3"):
        return None
    elif trigger == "event" and switch("party_at_festival"):
        call PlayEvent(play_event, "Town2finalfiestafestival_v2_0", "Town2finalfiestafestival_v2") from _call_Town2finalfiestafestival_v2_0_PlayEvent
        return (0, "", "Town2finalfiestafestival_v2_0")
    return None

label Town2finalfiestafestival_v3_0:
    call PauseForBalloon("Town2finalfiestafestival_v3_0") from _call_Town2finalfiestafestival_v3_0_PauseForBalloon
    Johan "My God, my head is killing me... I have to find Leyna, where is she?"
    $ fade_out()
    $ show_picture(1, "reencuentro1", width=814, height=624)
    $ fade_in()
    $ resolve_scene()
    "An hour later..."
    Johan "I've been looking for her for a long time, she wasn't in the inn room, where did she go?"
    Johan "I still can't quite remember what happened last night... and I don't know if I want to, both of us have done something we might regret"
    Johan "or nothing has happened... which I wish it were true"
    Johan "!!!!"
    Johan "Wait a second... that's Leyna! And she's with... Shit, she's with Alexa..."
    pause
    $ show_picture(2, "reencuentro2", width=814, height=624)
    $ resolve_scene()
    Johan "H-hey girls... I've been looking for you..."
    Leyna "Hi sweetie!"
    Alexa "Hey Johan! how's it going? how's your hangover? hahahaha"
    Johan "(Wow... they don't seem to be angry... in fact they seem quite happy... so surely nothing happened yesterday?)"
    Johan "(it must have been a bad dream... my god I feel so relieved, I don't know what would have happened if  all that I was imagining was true)"
    Johan "W-well, I feel like I've been run over by a car, but I'm okay I guess"
    Johan "And you, don't you have a hangover?"
    Alexa "Well... yes and no, we woke up shattered like you, but I have taught Leyna the trick of how to get rid of hangovers"
    Johan "The trick?"
    Alexa "Yeah! nothing like drinking a couple of beers and the hangover goes away hahahaha"
    Johan "Oh... I see... and the two of you have met in town?"
    Alexa "Oh no... yesterday I saw that your wife was quite drunk and I invited her to spend the night in my room... since you had disappeared, where were you?"
    Johan "I... I don't know, I woke up this morning in a field on the outskirts of town"
    Johan "So you are well Leyna?"
    $ show_picture(3, "reencuentro3", width=814, height=624)
    $ resolve_scene()
    Leyna "Hahaha yeah, I'm fine.... I'm still a little drunk and the beers we had with our friend didn't help hahaha"
    Johan "Friend?...ah, this guy?"
    $ erase_picture(3)
    $ resolve_scene()
    Villager "zzzzz...."
    Johan "It looks like he's out of action..."
    Alexa "Yes... our friend here is out cold... he hasn't been able to sleep much tonight hehehehehehe"
    Johan "???"
    Johan "I see... Well Leyna, will you come with me?"
    Leyna "Sure, let's go for a walk, at least I got a good night's sleep"
    Alexa "In a while I will go to the river to cool off, the cold water is also very good for the hangover, we will be almost all day out there, so come if you want to"
    Johan "Sure... we will consider it... let's go Leyna?"
    Leyna "Sure!"
    Alexa "Well guys, see you later"
    Leyna "Of course! see you later!"
    $ fade_out()
    $ erase_picture(1)
    $ erase_picture(2)
    call TransferPlayer("Town2", "Town2finalfiestafestival_v3_0", 1, 21, direction=6) from _call_Town2finalfiestafestival_v3_0_TransferPlayer
    call ChangePartyMember("Leyna", True) from _call_Town2finalfiestafestival_v3_0_ChangePartyMember
    call Movement("Town2finalfiestafestival_v3_0", "player", ["R","R"]) from _call_Town2finalfiestafestival_v3_0_Movement
    $ fade_in()
    $ resolve_scene()
    Johan "Well, what could we do today?"
    Leyna "We can always go to the river with Alexa"
    Johan "I guess so"
    Leyna "You know what? Look, let's go to the river, I think we could both use a little hangover relief and a chance to clear our heads a bit"
    Johan "You are right"
    $ set_self_switch("Town2","Town2finalfiestafestival_v3","A",True)
    return False

label Town2finalfiestafestival_v3(play_event = True, trigger = None): # event
    if is_erased("Town2finalfiestafestival_v3"):
        return None
    elif self_switch("Town2","Town2finalfiestafestival_v3","A"):
        return None
    elif switch("river_3"):
        return None
    elif trigger == "event" and switch("party_at_festival"):
        call PlayEvent(play_event, "Town2finalfiestafestival_v3_0", "Town2finalfiestafestival_v3") from _call_Town2finalfiestafestival_v3_0_PlayEvent
        return (0, "", "Town2finalfiestafestival_v3_0")
    return None

label Town2ToPath_0:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_Town2EV079_0_PlaySound
    call TransferPlayer("Path", "Town2EV079_0", 36, 9, direction=4) from _call_Town2EV079_0_TransferPlayer
    $ resolve_scene()
    return False

label Town2ToPath_1:
    Leyna "I have to find that guy"
    return False

label Town2ToPath(play_event = True, trigger = None): # event
    if is_erased("Town2ToPath"):
        return None
    elif trigger == "event" and switch("find_youth"):
        call PlayEvent(play_event, "Town2ToPath_1", "Town2ToPath") from _call_Town2ToPath_1_PlayEvent
        return (0, "", "Town2ToPath_1")
    elif trigger == "event":
        call PlayEvent(play_event, "Town2ToPath_0", "Town2ToPath") from _call_Town2ToPath_0_PlayEvent
        return (0, "", "Town2ToPath_0")
    return None

label Town2ToPath_v2_0:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_Town2EV080_0_PlaySound
    call TransferPlayer("Path", "Town2EV080_0", 36, 10, direction=4) from _call_Town2EV080_0_TransferPlayer
    $ resolve_scene()
    return False

label Town2ToPath_v2_1:
    Leyna "I have to find that guy"
    return False

label Town2ToPath_v2(play_event = True, trigger = None): # event
    if is_erased("Town2ToPath_v2"):
        return None
    elif trigger == "event" and switch("find_youth"):
        call PlayEvent(play_event, "Town2ToPath_v2_1", "Town2ToPath_v2") from _call_Town2ToPath_v2_1_PlayEvent
        return (0, "", "Town2ToPath_v2_1")
    elif trigger == "event":
        call PlayEvent(play_event, "Town2ToPath_v2_0", "Town2ToPath_v2") from _call_Town2ToPath_v2_0_PlayEvent
        return (0, "", "Town2ToPath_v2_0")
    return None

label Town2fotografo_0:
    OldMan "... need anything?"
    return False

label Town2fotografo_1(menu_choice = None):
    OldMan "Well, are you ready to work?"
    Leyna "Yes, if you don't mind my husband will join us at this session"
    OldMan "Of course, no problem. You have a beautiful wife like few others, you are very lucky"
    Johan "Hahahaha I know ... Thanks"
    OldMan "The magazine has asked me for a session outside the studio, in an urban environment or something like that"
    "I've already picked the package with the set and I know a place near here where we could take good photos..."
    $ show_transparent(1, "expresion_gota", pos=(0, 65), scale=(90, 90))
    $ resolve_scene()
    Leyna "Wait ... in public?"
    OldMan "Yes, but don't worry, we will be in a place where nobody usually goes by and it would be a relatively quick session"
    Leyna "I don't know ... Johan, what do you think?"
    Johan "Well.. if it is going to be something fast and the pay is fine.. it is only lingerie, right?"
    OldMan "I see, straight to the point. Yes, the pay is quite good and it's only a job. Come on, it will only be a couple of photos"
    OldMan "Everyone wins"
    Leyna "Seen that way.."
    OldMan "Perfect, let's start"
    $ fade_out()
    $ erase_picture(1)
    call TransferPlayer("Town2", "Town2fotografo_1", 1, 43, direction=6) from _call_Town2fotografo_1_TransferPlayer
    call SetEventLocation("Town2fotografo_1", "Town2fotografo", 1, 42) from _call_Town2fotografo_1_setloc
    $ fade_in()
    $ resolve_scene()
    call PauseForBalloon("Town2fotografo_1") from _call_Town2fotografo_1_PauseForBalloon
    call Movement("Town2fotografo_1", "player", ["R","TURN_L"]) from _call_Town2fotografo_1_Movement
    $ show_picture(1, "publico1")
    $ resolve_scene()
    Johan "Are you sure you want to do this?"
    Leyna "Yes, I know it seems strange but once you start it's not that bad. He is a very professional man"
    Johan "Okay, let's start then"
    OldMan "Great"
    OldMan "Let's start with a natural pose and move forward on the go"
    $ show_picture(2, "publico2")
    $ resolve_scene()
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_1_PlaySound
    OldMan "Great, next one"
    pause
    $ show_picture(3, "publico3")
    $ resolve_scene()
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_1_PlaySound_1
    OldMan "Nice, unbutton the top of the blouse and change your posture"
    pause
    $ show_picture(4, "publico4")
    $ resolve_scene()
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_1_PlaySound_2
    OldMan "Very sexy! Let's continue"
    OldMan "Turn up the bottom of the blouse so we can see the lingerie"
    Johan "...!"
    pause
    $ show_picture(5, "publico5")
    $ resolve_scene()
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_1_PlaySound_3
    OldMan "Amazing! Now take off your blouse and perform a couple more poses"
    pause
    $ show_picture(6, "publico6")
    $ resolve_scene()
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_1_PlaySound_4
    Johan "(I... feel weird, seeing Leyna like that in public.)"
    OldMan "Okey, the next one"
    pause
    $ show_picture(7, "publico7")
    $ resolve_scene()
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_1_PlaySound_5
    OldMan "Great work Leyna!"
    Johan "(I feel butterflies in my stomach thinking that at any moment someone could come and see this whole situation)"
    pause
    Villager1 "Oh! Wow! What's going on here?"
    Johan "...!!!!"
    $ show_picture(8, "publico8")
    $ resolve_scene()
    Villager2 "Amazing! What is this, a pornographic session?"
    OldMan "Have a little respect, we are working! And it's for a fashion magazine, so behave!"
    Villager1 "Oh, okay relax, what a shame! (What a bad mood this old man has) You are a supermodel!"
    $ show_picture(9, "publico9")
    $ resolve_scene()
    Leyna "Thank you.."
    OldMan "Come on Leyna, a couple of poses more, smile a little.."
    Johan "(Wait, are these two going to continue here?)"
    $ show_picture(10, "publico10")
    $ resolve_scene()
    OldMan "You two stay where you are"
    Villager1 "Okay, no problem..."
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_1_PlaySound_6
    OldMan "(Muttering) Yes, this is what they were looking for. But ... I see, yes"
    Johan "(What is he saying?)"
    $ show_picture(11, "publico12")
    $ resolve_scene()
    Villager1 "(That ass is amazing...)"
    pause
    $ show_picture(12, "publico13")
    $ resolve_scene()
    OldMan "That's great Leyna!"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_1_PlaySound_7
    OldMan "The problem ... yes, they had already told me ..."
    Leyna "???"
    Leyna "Have we finished?"
    OldMan "No... not yet"
    OldMan "Boys! By chance, are you wearing the festival clothes underneath?"
    Villager1 "... Hmm. Yes, why?"
    OldMan "Would you be interested in posing with the girl?"
    OldMan "The magazine has asked me for more male intervention in the sessions, but my grandson is working right now and cannot come"
    Johan "!!!"
    call GetChoice([_("Intervene"), _("Stay quiet")], value=menu_choice, called_from="Town2fotografo_1") from _call_Town2fotografo_1_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Intervene"):
        $ menu_choice = None
        $ resolve_scene()
        Johan "Hey I think this is more than enough, it was supposed to be a quick session and that nobody was going to be around here"
        Leyna "(Johan...)"
        OldMan "True true, sorry. At my age, I keep letting myself go like a small child with the things I like"
        Johan "..."
        OldMan "Okay,  we have enough for today, I will talk to the magazine and I will contact you again if I need anything else"
        Johan "Right..."
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
        call TransferPlayer("Town2", "Town2fotografo_1", 28, 21, direction=2) from _call_Town2fotografo_1_TransferPlayer_1
        $ set_switch("johan_intervened", True)
        $ fade_in()
        call Movement("Town2fotografo_1", "player", ["D","D","TURN_U"]) from _call_Town2fotografo_1_Movement_1
        $ resolve_scene()
        Leyna "You see? I told you it's not so bad"
        Johan "Yeah well... In the end, it was a little weird. I'm still not completely convinced"
        Leyna "I know... Let's forget about this for a while and see what the day holds"
        Johan "Yeah"
        Leyna "Maybe we can go to the festival site and have a look"
        Johan "Sure, good idea! (I need to occupy my mind with something, and forget the sensation that I have felt before..)"
    elif menu_choice == _("Stay quiet"):
        $ menu_choice = None
        Villager1 "Will you pay us something?"
        OldMan "Of course!"
        Villager1 "Well then ... What are we waiting for?"
        OldMan "Great! Undress and get together with the girl"
        Villager2 "Okey!"
        $ show_picture(13, "publico14")
        $ resolve_scene()
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_1_PlaySound_8
        OldMan "Okay guys, I need a more dominant attitude on your part"
        Johan "(Dominant?)"
        pause
        $ show_picture(14, "publico15")
        $ resolve_scene()
        Villager1 "Like this?"
        OldMan "Not bad but... Both of you"
        Villager2 "Okey..."
        pause
        $ show_picture(15, "publico16")
        $ resolve_scene()
        Villager2 "What do you think like that?"
        OldMan "Like that is perfect!"
        Johan "(They are touching Leyna... I'm... getting an erection seeing this?... it must be because of the nerves)"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_1_PlaySound_9
        OldMan "Okay, I have enough for now with this"
        Villager1 "A-are you sure?"
        OldMan "Yes, let's see what the magazine thinks and I'll contact you two if I need something else"
        Villager2 "Great (easy money)"
        Johan "(Thank goodness it's already over...)"
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
        call TransferPlayer("Town2", "Town2fotografo_1", 28, 21, direction=2) from _call_Town2fotografo_1_TransferPlayer_2
        $ set_switch("johan_silent", True)
        $ fade_in()
        call Movement("Town2fotografo_1", "player", ["D","D","TURN_U"]) from _call_Town2fotografo_1_Movement_2
        $ resolve_scene()
        Leyna "You see? I told you it's not so bad"
        Johan "Yeah well... In the end, it was a little weird. I'm still not completely convinced"
        Leyna "I know... Let's forget about this for a while and see what the day holds"
        Johan "Yeah"
        Leyna "Maybe we can go to the festival site and have a look"
        Johan "Sure, good idea! (I need to occupy my mind with something, and forget the sensation that I have felt before..)"
    $ photograph_3 = 1
    call GalleryViewed("publico") from _call_Town2fotografo_1_GalleryViewed
    $ resolve_scene()
    return False

label Town2fotografo_4(menu_choice = None):
    OldMan "Good morning beautiful, the magazine has contacted me  and they are delighted with the last thing we sent"
    $ show_transparent(1, "expresion_gota")
    $ resolve_scene()
    Leyna "Ah... yes? that's interesting"
    OldMan "Well, yes, things are going much better than I expected, they have asked me for another session, I already have all the clothes... but"
    Leyna "But?"
    OldMan "Well... you know... they like the previous one so much that they have asked me for something similar... something spicy"
    Leyna "So something spicy, huh?"
    $ erase_picture(1)
    $ show_transparent(2, "plano_mujer_cartoon", width=1600, height=900)
    $ resolve_scene()
    OldMan "Yes ... with two men... and few clothes, you know"
    Leyna "I... I can't do that, my husband wouldn't be Okay with this"
    OldMan "I figured you'd say that... but I have to tell you that the wardrobe for this new session has a surprise... masks, you will all be wearing masks"
    OldMan "So you know, your identity would be safe, your husband doesn't have to know... it's not like we're going to do anything extreme, they're just photos"
    Leyna "I don't know..."
    call GetChoice([_("Do the session"), _("I need to think about it")], value=menu_choice, called_from="Town2fotografo_4") from _call_Town2fotografo_4_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Do the session"):
        $ menu_choice = None
        $ resolve_scene()
        Leyna "Well... I need the money, I'm not going to lie"
        Leyna "How erotic is this photo shoot going to be?"
        OldMan "Well, no big deal, even though they will be naked you will only wear provocative clothes... and the mask"
        Leyna "I see... Well, we can start whenever you want"
        OldMan "Great, let's go to my studio, change and go to the location where we will do the photo session, now I call the boys"
        Leyna "Yeah great..."
        $ show_picture(3, "pantallanegro", scale=(120, 120), width=816, height=600)
        $ erase_picture(2)
        $ resolve_scene()
        "A FEW MOMENTS LATER..."
        Leyna "Here? this is a bit public, isn't it?"
        Villager "That's fine for me"
        Villager "For me neither, it's not much different from the festival"
        OldMan "Relax, No one comes through here"
        Leyna "If you say so..."
        OldMan "Well... everyone in your positions let's get started"
        $ show_picture(4, "mascara1")
        $ resolve_scene()
        OldMan "Perfect, you look great in the costumes... Now pose as we said before"
        Leyna "Yeah..."
        pause
        $ show_picture(5, "mascara2")
        $ resolve_scene()
        OldMan "Great!"
        OldMan "And now show us that perfect ass, and you two come closer, she doesn't bite"
        Leyna "..."
        pause
        $ show_picture(6, "mascara3")
        $ resolve_scene()
        OldMan "Perfect, very sexy Leyna, you are made for this, I don't know how you didn't think of being a model before"
        Leyna "I... thank you very much"
        Villager "YES, she has the best ass I've seen in a long time"
        Villager2 "Are you sure you're married? I would take you right now and..."
        Leyna "I get it..."
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_4_PlaySound
        OldMan "Well guys, next position"
        pause
        $ show_picture(7, "mascara4")
        $ resolve_scene()
        OldMan "NICE!"
        Villager "Yeah! great... what a pair of tits"
        Villager2 "YES, they are perfect"
        Leyna "...."
        Leyna "(They can't stop saying those kinds of things? I should be used to it in this town, but I can't help but getting a little excited by this attention)"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_4_PlaySound_1
        OldMan "All right, now the good stuff starts, let's go"
        pause
        $ show_picture(8, "mascara5")
        $ resolve_scene()
        OldMan "Very good hold this way a little more"
        Villager "All the time you want, I could be like this all my life... how soft her tits are, I could come right now"
        Leyna "What?"
        Villager "Hahaha nothing, it was a joke"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_4_PlaySound_2
        OldMan "Alright guys let's move on to the next pose"
        pause
        $ show_picture(9, "mascara6")
        $ resolve_scene()
        OldMan "Perfect..."
        Villager2 "Wow your ass is so close... I would kill to fuck you right now, as soon as I get home I'm going to masturbate with this in mind"
        Villager "Me too! You're perfect, wouldn't you like to leave your husband and come with me? I'm sure he doesn't have it as big as mine"
        Villager2 "Hey! get in line"
        Leyna "Guys... you don't have to say this kind of stuff please"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_4_PlaySound_3
        Villager "Come on... you should be used to it by now... plus you sure do love to be told these things. Why are you doing this kind of work if it is not the case?"
        Leyna "No I..."
        OldMan "Come on guys next position"
        Leyna "..."
        pause
        $ show_picture(10, "mascara7")
        $ resolve_scene()
        Villager "Oh this is perfect, so warm!"
        Villager2 "That's it, grab my dick, this is incredible"
        OldMan "Come on guys control yourselves"
        Villager "Yes, sorry"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_4_PlaySound_4
        OldMan "Okay, the last position"
        pause
        $ show_picture(11, "mascara8")
        $ resolve_scene()
        OldMan "Great very sexy Leyna!"
        Leyna "...."
        Villager "It's definitely the best job I've ever had"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_4_PlaySound_5
        OldMan "Okay, hold on a little longer, I'm going to get a little closer"
        Leyna "!!!"
        pause
        $ show_picture(12, "mascara9")
        $ resolve_scene()
        OldMan "Right, this angle is perfect!"
        Villager "Leyna right? I hope to see you at the festival and we can do another session, you and me alone"
        Leyna "Not a good idea, Sorry"
        OldMan "NO! it's a great idea, I'll talk to the magazine and see if they are interested"
        Leyna "In front of everybody? my husband..."
        OldMan "Don't worry, we will figure something out"
        Leyna "...."
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_4_PlaySound_6
        OldMan "Well guys we are done, great job! We will talk these days to see if we can make another session"
        Villager "Yes! I am looking forward to it"
        Villager2 "And me! it's been a lot of fun, pass me the pictures when you can, I'd like to have them!"
        OldMan "Of course"
        Leyna "(This has been a mistake? I hope Johan doesn't find out about this....)"
        $ masks = 2
        call GalleryViewed("mascara") from _call_Town2fotografo_4_GalleryViewed
        $ fade_out()
        $ erase_picture(3)
        $ erase_picture(4)
        $ erase_picture(5)
        $ erase_picture(6)
        $ erase_picture(6)
        $ erase_picture(7)
        $ erase_picture(8)
        $ erase_picture(9)
        $ erase_picture(10)
        $ erase_picture(11)
        $ erase_picture(12)
        $ fade_in()
    elif menu_choice == _("I need to think about it"):
        $ menu_choice = None
        $ resolve_scene()
        Leyna "I have to think about it, I'm not sure if I'm going to do this"
        OldMan "Of course, I'll be waiting here if you change your mind"
        $ erase_picture(2)
        $ masks = 1
    $ resolve_scene()
    return False

label Town2fotografo_5(menu_choice = None):
    OldMan "Have you changed your mind?"
    call GetChoice([_("Yes"), _("No")], value=menu_choice, called_from="Town2fotografo_5") from _call_Town2fotografo_5_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Yes"):
        $ menu_choice = None
        $ resolve_scene()
        Leyna "Well... I need the money, I'm not going to lie"
        Leyna "How erotic is this photo shoot going to be?"
        OldMan "Well, no big deal, even though they will be naked you will only wear provocative clothes... and the mask"
        Leyna "I see... Well, we can start whenever you want"
        OldMan "Great, let's go to my studio, change and go to the location where we will do the photo session, now I call the boys"
        Leyna "Yeah great..."
        $ show_picture(3, "pantallanegro", scale=(120, 120), width=816, height=600)
        $ resolve_scene()
        "A FEW MOMENTS LATER..."
        Leyna "Here? this is a bit public, isn't it?"
        Villager "That's fine for me"
        Villager "For me neither, it's not much different from the festival"
        OldMan "Relax, No one comes through here"
        Leyna "If you say so..."
        OldMan "Well... everyone in your positions let's get started"
        $ show_picture(4, "mascara1")
        $ resolve_scene()
        OldMan "Perfect, you look great in the costumes... Now pose as we said before"
        Leyna "Yeah..."
        pause
        $ show_picture(5, "mascara2")
        $ resolve_scene()
        OldMan "Great!"
        OldMan "And now show us that perfect ass, and you two come closer, she doesn't bite"
        Leyna "..."
        pause
        $ show_picture(6, "mascara3")
        $ resolve_scene()
        OldMan "Perfect, very sexy Leyna, you are made for this, I don't know how you didn't think of being a model before"
        Leyna "I... thank you very much"
        Villager "YES, she has the best ass I've seen in a long time"
        Villager2 "Are you sure you're married? I would take you right now and..."
        Leyna "I get it..."
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_5_PlaySound
        OldMan "Well guys, next position"
        pause
        $ show_picture(7, "mascara4")
        $ resolve_scene()
        OldMan "NICE!"
        Villager "Yeah! great... what a pair of tits"
        Villager2 "YES, they are perfect"
        Leyna "...."
        Leyna "(They can't stop saying those kinds of things? I should be used to it in this town, but I can't help but getting a little excited by this attention)"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_5_PlaySound_1
        OldMan "All right, now the good stuff starts, let's go"
        pause
        $ show_picture(8, "mascara5")
        $ resolve_scene()
        OldMan "Very good hold this way a little more"
        Villager "All the time you want, I could be like this all my life... how soft her tits are, I could come right now"
        Leyna "What?"
        Villager "Hahaha nothing, it was a joke"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_5_PlaySound_2
        OldMan "Alright guys let's move on to the next pose"
        pause
        $ show_picture(9, "mascara6")
        $ resolve_scene()
        OldMan "Perfect..."
        Villager2 "Wow your ass is so close... I would kill to fuck you right now, as soon as I get home I'm going to masturbate with this in mind"
        Villager "Me too! You're perfect, wouldn't you like to leave your husband and come with me? I'm sure he doesn't have it as big as mine"
        Villager2 "Hey! get in line"
        Leyna "Guys... you don't have to say this kind of stuff please"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_5_PlaySound_3
        Villager "Come on... you should be used to it by now... plus you sure do love to be told these things. Why are you doing this kind of work if it is not the case?"
        Leyna "No I..."
        OldMan "Come on guys next position"
        Leyna "..."
        pause
        $ show_picture(10, "mascara7")
        $ resolve_scene()
        Villager "Oh this is perfect, so warm!"
        Villager2 "That's it, grab my dick, this is incredible"
        OldMan "Come on guys control yourselves"
        Villager "Yes, sorry"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_5_PlaySound_4
        OldMan "Okay, the last position"
        pause
        $ show_picture(11, "mascara8")
        $ resolve_scene()
        OldMan "Great very sexy Leyna!"
        Leyna "...."
        Villager "It's definitely the best job I've ever had"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_5_PlaySound_5
        OldMan "Okay, hold on a little longer, I'm going to get a little closer"
        Leyna "!!!"
        pause
        $ show_picture(12, "mascara9")
        $ resolve_scene()
        OldMan "Right, this angle is perfect!"
        Villager "Leyna right? I hope to see you at the festival and we can do another session, you and me alone"
        Leyna "Not a good idea, Sorry"
        OldMan "NO! it's a great idea, I'll talk to the magazine and see if they are interested"
        Leyna "In front of everybody? my husband..."
        OldMan "Don't worry, we will figure something out"
        Leyna "...."
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_5_PlaySound_6
        OldMan "Well guys we are done, great job! We will talk these days to see if we can make another session"
        Villager "Yes! I am looking forward to it"
        Villager2 "And me! it's been a lot of fun, pass me the pictures when you can, I'd like to have them!"
        OldMan "Of course"
        Leyna "(This has been a mistake? I hope Johan doesn't find out about this....)"
        $ masks = 2
        call GalleryViewed("mascara") from _call_Town2fotografo_5_GalleryViewed
        $ fade_out()
        $ erase_picture(3)
        $ erase_picture(4)
        $ erase_picture(5)
        $ erase_picture(6)
        $ erase_picture(6)
        $ erase_picture(7)
        $ erase_picture(8)
        $ erase_picture(9)
        $ erase_picture(10)
        $ erase_picture(11)
        $ erase_picture(12)
        $ fade_in()
    elif menu_choice == _("No"):
        $ menu_choice = None
        $ resolve_scene()
        Leyna "I have to think about it, I'm not sure if I'm going to do this"
        OldMan "Of course, I'll be waiting here if you change your mind"
    $ resolve_scene()
    return False

label Town2fotografo_6:
    OldMan "Stop by tomorrow to see if the magazine has said anything"
    return False

label Town2fotografo_9:
    Leyna "(Better to talk to him when I'm alone)"
    return False

label Town2fotografo_10(menu_choice = None):
    OldMan "Good evening Leyna, I wanted to talk to you... I... I didn't expect you to come with your husband."
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Yes, he has come to accompany me"
    OldMan "Ahem... well then, yes, the truth is that I have good news, as so far the magazine is very happy with you"
    OldMan "Very very happy! and they want to continue working with us, but of course... it is clear that readers want more from us"
    Leyna "More from us?"
    OldMan "Yes... they want us to make the photos more intense... let's say, a lot more intense"
    Johan "What do you mean exactly?"
    OldMan "Well... I mean... add in some sex"
    Johan "WHAT? no way!"
    OldMan "Come on come on relax Hmmm Johan right? Look this is just business, we're talking about something strictly professional"
    Johan "I will not let anyone fuck my wife!"
    OldMan "Well... \"FUCK\", that's a big word, remember it's a photo shoot not a porn video, will there be penetration? well... not necessarily"
    Johan "..."
    OldMan "And also in the hypothetical case that there would be, it would be a simple procedure, you know, put it in for the photo and take it out"
    OldMan "Johan... The magazine is crazy about your wife, they are willing to pay a huge sum of money for her exclusivity"
    Johan "Huge sum of money?"
    OldMan "(Nice, looks like I'm gaining their attention)"
    OldMan "Yes yes, huge! you are also a great couple, it is clear that your relationship is perfect and there is a lot of trust! you are not jealous of his work are you?"
    Johan "ME? JEALOUS? NO, NO WAY"
    OldMan "(Hehehe right where it hurts the most as far as I can see)"
    Johan "I... I don't know... I don't think it's a good idea... it's just too much..."
    OldMan "Think about it, Johan... it's a great opportunity"
    call GetChoice([_("Do it"), _("No fucking way")], value=menu_choice, called_from="Town2fotografo_10") from _call_Town2fotografo_10_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Do it"):
        $ menu_choice = None
        $ resolve_scene()
        Johan "I... it's ok, if Leyna agrees it's ok.... But I have to be present at all times!"
        call GalleryViewed("fotoerotica") from _call_Town2fotografo_10_GalleryViewed
        Leyna "!!!"
        OldMan "(Tch!) Sure Johan whatever you want, I have prepared the studio for this session, please come with me"
        Johan "Yeah...."
        $ fade_out()
        $ erase_picture(1)
        $ show_picture(1, "fotoerotica1")
        $ fade_in()
        $ resolve_scene()
        "A FEW MOMENTS LATER"
        Johan "(Fuck, I'm already regretting this..... well I'm here and I can control that nothing gets out of hand)"
        OldMan "Well, Leyna, have you already changed? perfect, please place yourself there"
        Johan "!!! Wow... (Why am I surprised? after all, I know what we came for!)"
        $ show_picture(2, "fotoerotica2")
        $ resolve_scene()
        OldMan "Sexy as always Leyna, that outfit looks perfect on you!"
        Leyna "Th-Thanks..."
        Johan "(It's true that she looks very sexy in those clothes...)"
        OldMan "I know you're a little nervous but you have to relax, you know, smile a little and pose for me, you're going to do great"
        Leyna "Yes..."
        $ show_picture(3, "fotoerotica3")
        $ resolve_scene()
        Leyna "Is this good?"
        OldMan "That's perfect Leyna"
        Johan "So far so good... God, couldn't it be like this all the time? I'm getting on my nerves and it hasn't even started yet!)"
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_10_PlaySound
        $ flash_screen([255,255,255,170], 60, True)
        OldMan "Perfect, let's move on to the next position"
        $ show_picture(4, "fotoerotica4")
        $ resolve_scene()
        OldMan "Keep up the good work Leyna you are doing very well"
        Leyna "Thanks"
        Johan "(She is much more relaxed than in the hotsprings, she even seems to be... enjoying it)"
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_10_PlaySound_1
        $ flash_screen([255,255,255,170], 60, True)
        $ show_picture(5, "fotoerotica5")
        $ resolve_scene()
        OldMan "Wow, super sexy, love it!"
        Leyna "Hahahaha"
        Johan "(Unbelievable, I'm even getting an erection with all this, if I were a teenager I'd go crazy to get pictures of Leyna...)"
        Johan "(I guess that's why the magazine loves it so much... all the wanker kids will be buying it)"
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_10_PlaySound_2
        $ flash_screen([255,255,255,170], 60, True)
        $ show_picture(6, "pantallanegro", width=816, height=600)
        $ resolve_scene()
        OldMan "Perfect Leyna, we have finished with the solo poses"
        Leyna "..."
        OldMan "Now the boy with whom you will do the rest of the poses will come in"
        OldMan "Go ahead, boy, you can come in now"
        Leyna "!!!"
        Johan "(Fuck... the guy is huge... My stomach is turning...)"
        OldMan "Okay get in there with her"
        $ show_picture(7, "fotoerotica6")
        $ resolve_scene()
        OldMan "There, perfect!"
        OldMan "Okay, stay like this, a little romantic photo to start with"
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_10_PlaySound_3
        $ flash_screen([255,255,255,170], 60, True)
        OldMan "Great"
        Leyna "(Johan is right there, looking at us while all this is going on... I never thought I would be in a situation like this next to him.... am I getting excited?)"
        $ show_picture(8, "fotoerotica7")
        $ resolve_scene()
        Leyna "(I'm feeling it pressing against my ass... his huge... thing, it's hot and throbbing against me)"
        OldMan "All right, the time has come to start getting spicy, lift her bra, let that perfect body you have be seen"
        Johan "(Shit, here we go... Fuck why do I have an erection now? There's a guy touching my wife right under my nose...)"
        pause
        call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_10_PlaySound_4
        $ show_picture(9, "fotoerotica8")
        $ resolve_scene()
        Leyna "Ooh (Shit, I couldn't help moaning when he kissed my neck.... What's wrong with me? I can barely control myself)"
        Johan "(Was that a moan?... no... it's my imagination)"
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_10_PlaySound_5
        $ flash_screen([255,255,255,170], 60, True)
        OldMan "Great... I'm speechless, very good!"
        OldMan "Let's go with the next position lift her, as I told you before"
        $ show_picture(10, "fotoerotica9")
        $ resolve_scene()
        Johan "!!! (the son of a bitch has a huge dick and he's already got a hard-on!)"
        Leyna "Wow... (He's rubbing me down there, just with his breathing he's already... stimulating me, I feel his breath on the back of my neck and the... down there)"
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_10_PlaySound_6
        $ flash_screen([255,255,255,170], 60, True)
        OldMan "Well, guys, it's time to show it all, Leyna, take your panties aside a little bit"
        Leyna "Al-alright"
        Johan "!!! (Shit, the time has come, I have been paralyzed with everything that is happening)"
        call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_10_PlaySound_7
        $ show_picture(11, "fotoerotica10")
        $ resolve_scene()
        OldMan "That's right... You have a very nice pussy if I may say so Leyna"
        Leyna "Tha-thanks(His cock is rubbing my clitoris and I'm going to go crazy if we go on like this... for a second I forgot that Johan is here)"
        Johan "(Fuck, he's touching her pussy down there with his dick.... Why did I agree to this?)"
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_10_PlaySound_8
        $ flash_screen([255,255,255,170], 60, True)
        OldMan "Very good"
        OldMan "Well the time has come.... the penetration, in this position you are already perfect for the first picture, no need to change it"
        Johan "(WAIT, WHAT? THE PENETRATION?)"
        call GetChoice([_("Intervene"), _("Say nothing")], value=menu_choice, called_from="Town2fotografo_10") from _call_Town2fotografo_10_GetChoice_1
        $ menu_choice = _return
        if menu_choice == _("Intervene"):
            $ menu_choice = None
            $ erotic_photos = 1
            $ resolve_scene()
            Johan "Hey! There's no way I'm going to let you fuck my wife right under my nose!"
            OldMan "(Shit, I knew this guy was going to give us trouble) I see... well I guess we'll have to play with the camera angle"
            OldMan "Leyna, please bend over and get your ass in the air"
            Leyna "Alright!"
            $ show_picture(12, "fotoerotica13")
            $ resolve_scene()
            OldMan "Okay... so... tch! boy I can still see your dick from here, try to hide it somehow"
            Villager "Sure, give me a second!"
            Leyna "!!!"
            $ show_picture(13, "fotoerotica14")
            $ resolve_scene()
            OldMan "Wait wait wait! That's a good position too, hold on a second!"
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_10_PlaySound_9
            $ flash_screen([255,255,255,170], 60, True)
            Leyna "Hmmmm (it keeps rubbing me as it moves)"
            Villager "(This girl is very horny.... I think I have an idea and I'm sure her husband doesn't notice)"
            OldMan "Okay kid, I'm going to go back to the position I was in before and as I said, try to hide it somehow so it doesn't show up in the picture"
            Villager "Okay!"
            $ show_picture(14, "fotoerotica15")
            $ resolve_scene()
            Villager "Okay... okay... give me a moment to get myself well positioned"
            Leyna "???"
            pause
            $ show_picture(15, "fotoerotica16")
            $ resolve_scene()
            Villager "Yes... a little more, let's see..."
            Leyna "Ah (He's sticking his dick in me! He's sticking it in front of Johan, but he doesn't seem to be noticing...)"
            pause
            $ show_picture(16, "fotoerotica17")
            $ resolve_scene()
            Villager "Yeah! right there, perfect"
            Leyna "AH! (shit, he put it all the way in me... with this alone I was about to squirt... fuck!)"
            OldMan "Yes, it's perfect! thank you very much"
            pause
            $ show_picture(17, "fotoerotica18")
            $ resolve_scene()
            Leyna "Ah ah ah ah (I find it hard to hold on, I feel it throbbing inside me... deep inside me)"
            Leyna "(Let this end soon please... I don't think I can take much more)"
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_10_PlaySound_10
            $ flash_screen([255,255,255,170], 60, True)
            OldMan "A perfect photo!"
            pause
            $ show_picture(18, "fotoerotica19")
            $ resolve_scene()
            Johan "(from here I can't see very well what's going on or what they are saying... it certainly seems that he... no, I have already told them that they can't do that)"
            OldMan "Wow we are having a spectacular photo shoot, well, time to move on to the cumshot"
            Johan "The what?"
            OldMan "well... you know, the cumshot... the finishing touch! we can't end this session without one!"
            Johan "Do you want to cum on my wife's face? NO FUCKING WAY!"
            OldMan "(Fuck! this guy is ruining my work) Well... I guess I can fix it in photoshop later"
            OldMan "Leyna, get in position! on your knees!"
            Leyna "!!! Yeah!"
            $ show_picture(19, "fotoerotica21")
            $ resolve_scene()
            OldMan "Very good"
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_10_PlaySound_11
            $ flash_screen([255,255,255,170], 60, True)
            OldMan "That's it for today kids... it could have been better, but I'm sure the magazine will love it!"
            OldMan "You can get dressed now, I will keep you posted during these days"
            Leyna "Okay, thank you"
            Villager "Yes count on me for anything you want hahahaha"
            $ show_picture(20, "fotoerotica23")
            $ resolve_scene()
            Johan "(What the hell just happened? How could I let them go to such extremes with Leyna? I ... What the hell is going on with me?)"
            Johan "(And I have this disgusting erection that just won't go away, along with this horrible giddy feeling in my stomach.... Fuck)"
            Johan "(I have to get out of here and get some fresh air)"
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
            $ erase_picture(19)
            $ set_switch("erotic_photos_together", True)
            $ erase_picture(20)
            call TransferPlayer("Town2", "Town2fotografo_10", 45, 12, direction=4) from _call_Town2fotografo_10_TransferPlayer
            $ fade_in()
            call Movement("Town2fotografo_10", "player", ["L","L","L"]) from _call_Town2fotografo_10_Movement
            $ resolve_scene()
            Johan "..."
            $ set_self_switch("Town2","Town2fotografo","B",True)
        elif menu_choice == _("Say nothing"):
            $ menu_choice = None
            $ erotic_photos = 2
            Johan "(I... for some reason I'm paralyzed, I can't say a word, I'm nailed to the chair)"
            Johan "(Like the old man said before, it's just a matter of getting it in for the photo and getting it out, right? But am I really going to let that happen?)"
            Villager "All right, here I come"
            Leyna "!!!"
            pause
            $ show_picture(12, "fotoerotica11")
            $ resolve_scene()
            Leyna "Ah!"
            Villager "Wow, that went in pretty easy... you're pretty wet down there huh?"
            Leyna "Lo-lower your voice, my husband will hear you."
            Villager "hehehehehe yeah sorry"
            OldMan "All right, guys, hang in there for a second!"
            pause
            $ show_picture(13, "fotoerotica12")
            $ resolve_scene()
            OldMan "Okay this angle is perfect"
            Leyna "Ah ah ah... hmmmm"
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_10_PlaySound_12
            $ flash_screen([255,255,255,170], 60, True)
            Johan "(My wife is being penetrated in front of my eyes and I... I'm standing here looking at everything, it feels unreal, I'm getting dizzy)"
            OldMan "All right, let's move on to the next position"
            OldMan "Leyna, turn around and bend over, that's perfect!"
            $ show_picture(14, "fotoerotica18")
            $ resolve_scene()
            OldMan "All right, hang in there for a little while"
            Villager "Your pussy feels great... I don't think I can go much longer without cumming"
            Leyna "D-don't do it ah ah ah that would be... terrible"
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_10_PlaySound_13
            $ flash_screen([255,255,255,170], 60, True)
            OldMan "Okay guys, let's switch again, Leyna lean to one side"
            Leyna "Ah ah alright"
            $ show_picture(15, "fotoerotica20")
            $ resolve_scene()
            OldMan "Great, this angle is magic, the magazine will pay us a lot for this!"
            Johan "(From here I can see everything, that guy has a giant dick and he is inside Leyna, although they are not  moving, he is... inside my wife, I feel like vomiting)"
            Johan "(I feel sick watching this)"
            Leyna "(Even though we're not moving, it feels like it's getting to my core and I'm so excited, I can barely control myself... if Johan wasn't here)"
            Leyna "(I don't know what could happen...)"
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_10_PlaySound_14
            $ flash_screen([255,255,255,170], 60, True)
            Villager "I can hardly hold on any longer Old man!"
            Johan "??? ( is he saying...)"
            OldMan "Oh sure, Leyna get on your knees let's go with the cumshot!"
            Johan "(Cumshot?)"
            Leyna "O-okay"
            $ show_picture(16, "fotoerotica21")
            $ resolve_scene()
            OldMan "Perfect! OK, kiddo, anytime"
            Villager "Yes! ah ahh!"
            Johan "Wait..."
            $ flash_screen([255,255,255,170], 60, True)
            $ flash_screen([255,255,255,170], 60, True)
            $ show_picture(17, "fotoerotica22")
            call PlaySound("sound", "audio/Poison.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_10_PlaySound_15
            $ resolve_scene()
            Villager "AAAhhh"
            Johan "!!!!"
            Leyna "Oh!"
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_10_PlaySound_16
            $ flash_screen([255,255,255,170], 60, True)
            OldMan "Perfect! the photo came out great, very good job guys! with this we have enough for today, and I'll keep you informed of what the magazine tells me"
            Leyna "...."
            $ show_picture(17, "fotoerotica23")
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_10_PlaySound_17
            $ resolve_scene()
            $ flash_screen([255,255,255,170], 60, True)
            Johan "(What the hell just happened? How could I let them go to such extremes with Leyna? I ... What the hell is going on with me?)"
            Johan "(And I have this disgusting erection that just won't go away, along with this horrible giddy feeling in my stomach.... Fuck)"
            OldMan "Okay, that's it, you guys wash up and we'll talk these days"
            Leyna "Yeah"
            Johan "..."
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
            $ set_switch("erotic_photos_together", True)
            $ erase_picture(17)
            call TransferPlayer("Town2", "Town2fotografo_10", 45, 12, direction=4) from _call_Town2fotografo_10_TransferPlayer_1
            $ fade_in()
            call Movement("Town2fotografo_10", "player", ["L","L","L"]) from _call_Town2fotografo_10_Movement_1
            $ resolve_scene()
            Johan "..."
            $ set_self_switch("Town2","Town2fotografo","B",True)
    elif menu_choice == _("No fucking way"):
        $ menu_choice = None
        $ erase_picture(1)
        $ resolve_scene()
        Johan "I'm sorry but I can't allow this"
        OldMan "I understand... but it's a golden opportunity, if you change your mind I'll be right here"
        Johan "Yeah..."
        $ set_self_switch("Town2","Town2fotografo","A",True)
    $ resolve_scene()
    return False

label Town2fotografo_11(menu_choice = None):
    OldMan "have you changed your mind?"
    call GetChoice([_("Do it"), _("No fucking way")], value=menu_choice, called_from="Town2fotografo_11") from _call_Town2fotografo_11_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Do it"):
        $ menu_choice = None
        $ resolve_scene()
        Johan "I... it's ok, if Leyna agrees it's ok.... But I have to be present at all times!"
        call GalleryViewed("fotoerotica") from _call_Town2fotografo_11_GalleryViewed
        Leyna "!!!"
        OldMan "(Tch!) Sure Johan whatever you want, I have prepared the studio for this session, please come with me"
        Johan "Yeah...."
        $ fade_out()
        $ show_picture(1, "fotoerotica1")
        $ fade_in()
        $ resolve_scene()
        "A FEW MOMENTS LATER"
        Johan "(Fuck, I'm already regretting this..... well I'm here and I can control that nothing gets out of hand)"
        OldMan "well Leyna, have you already changed? perfect, please place yourself there"
        Johan "!!! Wow... (Why am I surprised? after all, I knew what we were coming to!)"
        $ show_picture(2, "fotoerotica2")
        $ resolve_scene()
        OldMan "Sexy as always Leyna, that outfit looks perfect on you!"
        Leyna "Th-Thanks..."
        Johan "(It is true that she looks very sexy in those clothes...)"
        OldMan "I know you're a little nervous but you have to relax, you know, smile a little and pose for me, you're going to do great"
        Leyna "Yes..."
        $ show_picture(3, "fotoerotica3")
        $ resolve_scene()
        Leyna "Is this good?"
        OldMan "That's perfect Leyna"
        Johan "So far so good... God, couldn't it be like this all the time? I'm getting on my nerves and it hasn't even started yet!)"
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_11_PlaySound
        $ flash_screen([255,255,255,170], 60, True)
        OldMan "Perfect, let's move on to the next position"
        $ show_picture(4, "fotoerotica4")
        $ resolve_scene()
        OldMan "Keep up the good work Leyna you are doing very well"
        Leyna "Thanks"
        Johan "(She is much more relaxed than in the hotsprings, she even seems to be... enjoying it)"
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_11_PlaySound_1
        $ flash_screen([255,255,255,170], 60, True)
        $ show_picture(5, "fotoerotica5")
        $ resolve_scene()
        OldMan "Wow, super sexy, love it!"
        Leyna "Hahahaha"
        Johan "(Unbelievable, I'm even getting an erection with all this, if I were a teenager I'd go crazy to get pictures of Leyna...)"
        Johan "(I guess that's why the magazine loves it so much... all the wanker kids will be buying it)"
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_11_PlaySound_2
        $ flash_screen([255,255,255,170], 60, True)
        $ show_picture(6, "pantallanegro", width=816, height=600)
        $ resolve_scene()
        OldMan "Perfect Leyna, we have finished with the solo poses"
        Leyna "..."
        OldMan "Now the boy with whom you will do the rest of the poses will come in"
        OldMan "Go ahead, boy, you can come in now"
        Leyna "!!!"
        Johan "(Fuck... the guy is huge... My stomach is turning...)"
        OldMan "Okay get in there with her"
        $ show_picture(7, "fotoerotica6")
        $ resolve_scene()
        OldMan "There, perfect!"
        OldMan "Okay, stay like this, a little romantic photo to start with"
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_11_PlaySound_3
        $ flash_screen([255,255,255,170], 60, True)
        OldMan "Great"
        Leyna "(Johan is right there, looking at us while all this is going on... I never thought I would be in a situation like this next to him.... am I getting excited?)"
        $ show_picture(8, "fotoerotica7")
        $ resolve_scene()
        Leyna "(I'm feeling it pressing against my ass... her huge... thing, it's hot and throbbing against me)"
        OldMan "All right, the time has come to start getting spicy, lift her bra, let that perfect body you have be seen"
        Johan "(Shit, here we go... Fuck why do I have an erection now? There's a guy touching my wife right under my nose...)"
        pause
        call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_11_PlaySound_4
        $ show_picture(9, "fotoerotica8")
        $ resolve_scene()
        Leyna "Ooh (Shit, I couldn't help moaning when he kissed my neck.... What's wrong with me? I can barely control myself)"
        Johan "(Was that a moan?... no... it's my imagination)"
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_11_PlaySound_5
        $ flash_screen([255,255,255,170], 60, True)
        OldMan "Great... I'm speechless, very good guys!"
        OldMan "Let's go with the next position lift her as I told you"
        $ show_picture(10, "fotoerotica9")
        $ resolve_scene()
        Johan "!!! (the son of a bitch has a huge dick and he's already got a hard-on!)"
        Leyna "Wow... (He's rubbing me down there, just with his breathing he's already... stimulating me, I feel his breath on the back of my neck and the... down there)"
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_11_PlaySound_6
        $ flash_screen([255,255,255,170], 60, True)
        OldMan "Well, guys, it's time to show it all, Leyna, take your panties aside a little bit"
        Leyna "Al-alright"
        Johan "!!! (Shit, the time has come, I have been paralyzed with everything that is happening)"
        call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_11_PlaySound_7
        $ show_picture(11, "fotoerotica10")
        $ resolve_scene()
        OldMan "That's right... You have a very nice pussy if I may say so Leyna"
        Leyna "Tha-thanks(His cock is rubbing my clitoris and I'm going to go crazy if we go on like this... for a second I forgot that Johan is here)"
        Johan "(Fuck, he's touching him down there with his dick.... Why did I agree to this?)"
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_11_PlaySound_8
        $ flash_screen([255,255,255,170], 60, True)
        OldMan "Very good"
        OldMan "Well the time has come.... the penetration, in this position you are already perfect for the first picture, no need to change it"
        Johan "(WAIT, WHAT? THE PENETRATION?)"
        call GetChoice([_("Intervene"), _("Say nothing")], value=menu_choice, called_from="Town2fotografo_11") from _call_Town2fotografo_11_GetChoice_1
        $ menu_choice = _return
        if menu_choice == _("Intervene"):
            $ menu_choice = None
            $ erotic_photos = 1
            $ resolve_scene()
            Johan "Hey! There's no way I'm going to let you fuck my wife right under my nose!"
            OldMan "(Shit, I knew this guy was going to give us trouble) I see... well I guess we'll have to play with the camera angle"
            OldMan "Leyna, please bend over and get your ass in the air"
            Leyna "Alright!"
            $ show_picture(12, "fotoerotica13")
            $ resolve_scene()
            OldMan "Okay... so... tch! boy I can still see your dick from here, try to hide it somehow"
            Villager "Sure, give me a second!"
            Leyna "!!!"
            $ show_picture(13, "fotoerotica14")
            $ resolve_scene()
            OldMan "Wait wait wait! That's a good position too, hold on a second!"
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_11_PlaySound_9
            $ flash_screen([255,255,255,170], 60, True)
            Leyna "Hmmmm (it keeps rubbing me as it moves)"
            Villager "(This girl is very horny.... I think I have an idea and I'm sure her husband doesn't notice)"
            OldMan "Okay kid, I'm going to go back to the position I was in before and as I said, try to hide it somehow so it doesn't show up in the picture"
            Villager "Okay!"
            $ show_picture(14, "fotoerotica15")
            $ resolve_scene()
            Villager "Okay... okay... give me a moment to get myself well positioned"
            Leyna "???"
            pause
            $ show_picture(15, "fotoerotica16")
            $ resolve_scene()
            Villager "Yes... a little more, let's see..."
            Leyna "Ah (He's sticking his dick in me! He's sticking it in front of Johan, but he doesn't seem to be noticing...)"
            pause
            $ show_picture(16, "fotoerotica17")
            $ resolve_scene()
            Villager "Yeah! right there, perfect"
            Leyna "AH! (shit, he put it all the way in me... with this alone I was about to squirt... fuck!)"
            OldMan "Yes, it's perfect! thank you very much"
            pause
            $ show_picture(17, "fotoerotica18")
            $ resolve_scene()
            Leyna "Ah ah ah ah (I find it hard to hold on, I feel it throbbing inside me... deep inside me)"
            Leyna "(Let this end soon please... I don't think I can take much more)"
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_11_PlaySound_10
            $ flash_screen([255,255,255,170], 60, True)
            OldMan "A perfect photo!"
            pause
            $ show_picture(18, "fotoerotica19")
            $ resolve_scene()
            Johan "(from here I can't see very well what's going on or what they are saying... it certainly seems that he... no, I have already told them that they can't do that)"
            OldMan "Wow we are having a spectacular photo shoot, well, time to move on to the cumshot"
            Johan "The what?"
            OldMan "well... you know, the cumshot... the finishing touch! we can't end this session without one!"
            Johan "Do you want to cum on my wife's face? NO FUCKING WAY!"
            OldMan "(Fuck! this guy is ruining my work) Well... I guess I can fix it in photoshop later"
            OldMan "Leyna, get in position! on your knees!"
            Leyna "!!! Yeah!"
            $ show_picture(19, "fotoerotica21")
            $ resolve_scene()
            OldMan "Very good"
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_11_PlaySound_11
            $ flash_screen([255,255,255,170], 60, True)
            OldMan "That's it for today kids... it could have been better, but I'm sure the magazine will love it!"
            OldMan "You can get dressed now, I will keep you posted during these days"
            Leyna "Okay, thank you"
            Villager "Yes count on me for anything you want hahahaha"
            $ show_picture(20, "fotoerotica23")
            $ resolve_scene()
            Johan "(What the hell just happened? How could I let them go to such extremes with Leyna? I ... What the hell is going on with me?)"
            Johan "(And I have this disgusting erection that just won't go away, along with this horrible giddy feeling in my stomach.... Fuck)"
            Johan "(I have to get out of here and get some fresh air)"
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
            $ erase_picture(19)
            $ set_switch("erotic_photos_together", True)
            $ erase_picture(20)
            call TransferPlayer("Town2", "Town2fotografo_11", 45, 12, direction=4) from _call_Town2fotografo_11_TransferPlayer
            $ fade_in()
            call Movement("Town2fotografo_11", "player", ["L","L","L"]) from _call_Town2fotografo_11_Movement
            $ set_self_switch("Town2","Town2fotografo","B",True)
            $ resolve_scene()
            Johan "..."
        elif menu_choice == _("Say nothing"):
            $ menu_choice = None
            $ erotic_photos = 2
            Johan "(I... for some reason I'm paralyzed, I can't say a word, I'm nailed to the chair)"
            Johan "(Like the old man said before, it's just a matter of getting it in for the photo and getting it out, right? But am I really going to let that happen?)"
            Villager "All right, here I come"
            Leyna "!!!"
            pause
            $ show_picture(12, "fotoerotica11")
            $ resolve_scene()
            Leyna "Ah!"
            Villager "Wow, that went in pretty easy... you're pretty wet down there huh?"
            Leyna "Lo-lower your voice, my husband will hear you."
            Villager "hehehehehe yeah sorry"
            OldMan "All right, guys, hang in there for a second!"
            pause
            $ show_picture(13, "fotoerotica12")
            $ resolve_scene()
            OldMan "Okay this angle is perfect"
            Leyna "Ah ah ah... hmmmm"
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_11_PlaySound_12
            $ flash_screen([255,255,255,170], 60, True)
            Johan "(My wife is being penetrated in front of my eyes and I... I'm standing here looking at everything, it feels unreal, I'm getting dizzy)"
            OldMan "All right, let's move on to the next position"
            OldMan "Leyna, turn around and bend over, that's perfect!"
            $ show_picture(14, "fotoerotica18")
            $ resolve_scene()
            OldMan "All right, hang in there for a little while"
            Villager "Your pussy feels great... I don't think I can go much longer without cumming"
            Leyna "D-don't do it ah ah ah that would be... terrible"
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_11_PlaySound_13
            $ flash_screen([255,255,255,170], 60, True)
            OldMan "Okay guys, let's switch again, Leyna lean to one side"
            Leyna "Ah ah alright"
            $ show_picture(15, "fotoerotica20")
            $ resolve_scene()
            OldMan "Great, this angle is magic, the magazine will pay us a lot for this!"
            Johan "(From here I can see everything, that guy has a giant dick and he is inside Leyna, although they are not  moving, he is... inside my wife, I feel like vomiting)"
            Johan "(I feel sick watching this)"
            Leyna "(Even though we're not moving, it feels like it's getting to my core and I'm so excited, I can barely control myself... if Johan wasn't here)"
            Leyna "(I don't know what could happen...)"
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_11_PlaySound_14
            $ flash_screen([255,255,255,170], 60, True)
            Villager "I can hardly hold on any longer Old man!"
            Johan "??? ( is he saying...)"
            OldMan "Oh sure, Leyna get on your knees let's go with the cumshot!"
            Johan "(Cumshot?)"
            Leyna "O-okay"
            $ show_picture(16, "fotoerotica21")
            $ resolve_scene()
            OldMan "Perfect! OK, kiddo, anytime"
            Villager "Yes! ah ahh!"
            Johan "Wait..."
            $ flash_screen([255,255,255,170], 60, True)
            $ flash_screen([255,255,255,170], 60, True)
            $ show_picture(17, "fotoerotica22")
            call PlaySound("sound", "audio/Poison.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_11_PlaySound_15
            $ resolve_scene()
            Villager "AAAhhh"
            Johan "!!!!"
            Leyna "Oh!"
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_11_PlaySound_16
            $ flash_screen([255,255,255,170], 60, True)
            OldMan "Perfect! the photo came out great, very good job guys! with this we have enough for today, and I'll keep you informed of what the magazine tells me"
            Leyna "...."
            $ show_picture(17, "fotoerotica23")
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_11_PlaySound_17
            $ resolve_scene()
            $ flash_screen([255,255,255,170], 60, True)
            Johan "(What the hell just happened? How could I let them go to such extremes with Leyna? I ... What the hell is going on with me?)"
            Johan "(And I have this disgusting erection that just won't go away, along with this horrible giddy feeling in my stomach.... Fuck)"
            OldMan "Okay, that's it, you guys wash up and we'll talk these days"
            Leyna "Yeah"
            Johan "..."
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
            $ set_switch("erotic_photos_together", True)
            $ erase_picture(17)
            call TransferPlayer("Town2", "Town2fotografo_11", 45, 12, direction=4) from _call_Town2fotografo_11_TransferPlayer_1
            $ fade_in()
            call Movement("Town2fotografo_11", "player", ["L","L","L"]) from _call_Town2fotografo_11_Movement_1
            $ set_self_switch("Town2","Town2fotografo","B",True)
            $ resolve_scene()
            Johan "..."
    elif menu_choice == _("No fucking way"):
        $ menu_choice = None
        $ resolve_scene()
        Johan "I'm sorry but I can't allow this"
        OldMan "I understand... but it's a golden opportunity, if you change your mind I'll be right here"
        Johan "Yeah..."
    $ resolve_scene()
    return False

label Town2fotografo_12:
    OldMan "Stop by tomorrow to see if the magazine has said anything"
    return False

label Town2fotografo_13(menu_choice = None):
    OldMan "Great to see you guys!"
    Johan "OH... hey how's it going?"
    OldMan "Great! the magazine is looking forward to receiving more material from us!"
    Leyna "More material?"
    OldMan "Yes, they loved the last session we did! They want us to do one more like it... but they told me to make the most of the town"
    Johan "Make the most of the town? How do you want to do something like that?"
    OldMan "Well, my sister is the owner of the Hot springs and I have asked her if we can reserve it for today to do the session"
    Leyna "In the Hotsprings?..."
    OldMan "Yes! it will be very nice, with the right level of eroticism, mixed with traditional clothes, it will be a photo shoot that we will be very well paid"
    Leyna "W-well, if it's all right with Johan..."
    Johan "I..."
    call GetChoice([_("Okay, let's do it"), _("I can't do it")], value=menu_choice, called_from="Town2fotografo_13") from _call_Town2fotografo_13_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Okay, let's do it"):
        $ menu_choice = None
        $ resolve_scene()
        OldMan "Great! I see that you have already decided to continue with the project"
        Johan "Yes, well... But I have to be present"
        OldMan "I-I see... well I get it, she's your wife and all"
        Johan "Yeah, well you wanted us to go to the Hotsprings didn't you?"
        OldMan "Yes, I have already prepared everything, both the costumes and the boys are already waiting for us"
        Johan "(The boys... I guess it will be similar to the last time... I don't know if accepting all this was a good idea)"
        Leyna "Well, let's go"
        OldMan "Yes! better not to keep them waiting"
        $ fade_out()
        call TransferPlayer("HotSpringsExterior", "Town2fotografo_13", 11, 10, direction=8) from _call_Town2fotografo_13_TransferPlayer
        call Movement("Town2fotografo_13", "player", ["U"]) from _call_Town2fotografo_13_Movement
        $ fade_in()
        $ resolve_scene()
        Johan "Well... here we are... ( Jesus, what am I thinking, no matter how much I try to pretend that I'm ok with this...)"
        Johan "(I feel like it could be the worst decision of my life...)"
        Leyna "Yes, come on, they're waiting for us... Are you okay Johan? You have a very strange face, if you're not sure about this..."
        Johan "I-I'm not... but if it's okay with you, I don't want to stop you from working... even if I don't like the work..."
        Leyna "I see... I appreciate it Johan, that's very mature of you, not everyone would let his wife expose herself to such a situation"
        Johan "Hahahaha yeah, very mature...."
        Leyna "???... Well, let's go ?"
        Johan "Yeah..."
        $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
        $ resolve_scene()
        "Several minutes later"
        Leyna "This is the clothes I have to wear? it's a bit.... well, I'm surprised"
        Johan "??? show me"
        $ show_picture(2, "photohot1")
        $ resolve_scene()
        Leyna "After the last session I was expecting something more revealing, it's just a swimsuit"
        pause
        $ show_picture(3, "photohot2")
        $ resolve_scene()
        Johan "Well yes... although you look great hehehe (Thank God! what a relief!!! this session I imagine it won't be as explicit as the previous one!)"
        OldMan "Oh yes, I was surprised too, they sent it to me from the magazine, they told me it was a special swimsuit but to me it looks like an ordinary one"
        YoungVillager "Wow Leyna! as beautiful as always!"
        Leyna "!!!"
        $ show_picture(4, "photohot3")
        $ resolve_scene()
        Leyna "Y-you!"
        Johan "Oh, hey, you're the guy from the other day!"
        YoungVillager "In the flesh..."
        Leyna "What are you doing here?"
        $ show_picture(5, "photohot4")
        $ resolve_scene()
        YoungVillager "Well, I needed some money and the photographer told me that I fit the profile he was looking for, so why not?"
        Leyna "I-I see (I don't trust this guy, I hope he doesn't do anything stupid in front of Johan...)"
        YoungVillager "It will be a pleasure to work with you Leyna, of course it will be a new experience for me, so treat me well, ok?"
        Leyna "Sure, let's be professionals and let's work together to make this happen"
        Villager "Yeah!"
        $ show_picture(6, "photohot5")
        $ resolve_scene()
        Leyna "(This guy gives me the creeps, just by looking at his face you know he is not clean... but he is very persuasive... that time in the bar...)"
        Leyna "(If I had known I was going to end up in this situation this morning I would'nt have had a few beers with Alexa)"
        Leyna "(But the party atmosphere in this town is contagious... )"
        $ show_picture(7, "photohot6")
        $ resolve_scene()
        OldMan "Well, I see you are motivated for today! All right then, everyone go to your positions"
        OldMan "Let's start with you Leyna and then the guys will join us, Johan, from here you can see everything, if you want to get closer you can do it"
        OldMan "As long as you are not in the frame you can stand wherever you want, okay?"
        Johan "Sure..."
        OldMan "Okay, let's get started!"
        $ show_picture(8, "pantallanegro", scale=(120, 120), width=816, height=600)
        $ resolve_scene()
        OldMan "Very good Leyna put yourself there, perfect"
        $ show_picture(9, "photohot7")
        $ resolve_scene()
        OldMan "Okay, get down on your knees, let's start with some simple photos"
        Leyna "Okay..."
        $ show_picture(10, "photohot8")
        $ resolve_scene()
        Leyna "Is this position okay?"
        OldMan "That's perfect, stay still"
        Leyna "Yeah"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound
        OldMan "Perfect, now lean in and approach me"
        Leyna "All right..."
        pause
        $ show_picture(11, "photohot9")
        $ resolve_scene()
        Leyna "Something like this?"
        OldMan "Yes..."
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_1
        OldMan "Now squat down, like in those reggaeton videos that are so popular"
        Leyna "Okay, I'll give it a try (so far it doesn't look as erotic as usual... thank goodness)"
        pause
        $ show_picture(12, "photohot10")
        $ resolve_scene()
        Leyna "So-something like that? it's a little uncomfortable"
        OldMan "Great, hold on to that position for a bit!"
        YoungVillager "Wow, Hot!"
        Villager "Yes, from here we have spectacular views hahahaha"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_2
        pause
        $ show_picture(13, "photohot37")
        $ resolve_scene()
        Johan "(I don't find it funny when people talk about Leyna like that, especially in front of me)"
        Johan "(But at least it seems that today's session is less erotic than the previous one)"
        Johan "(Even Leyna seems to be starting to have a good time ... at least she's more relaxed than before,she seemed a bit tense)"
        Johan "(Although I don't know if I should be happy about it...)"
        OldMan "All right Leyna, get in the water, let's do the next position inside"
        Leyna "Okay"
        call PlaySound("sound", "audio/Water1.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_3
        Johan "!!!!"
        $ show_picture(14, "photohot11")
        call PlaySound("music", "audio/Dungeon3.ogg", volume=0.9, no_loop=False) from _call_Town2fotografo_13_PlaySound_4
        $ resolve_scene()
        Leyna "!!!"
        Leyna "I already imagined that it was not a normal swimsuit... it shows through everything"
        OldMan "Well, the magazine people hadn't told me anything, but it's better for us, otherwise the session would be very boring"
        OldMan "Look, stay as you are, it's a good position and I like your expression of surprise"
        Leyna "Sure, have it your way"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_5
        OldMan "Perfect, now a small zoom to highlight the interesting parts"
        Johan "(Interesting parts?)"
        $ show_picture(15, "photohot12")
        $ resolve_scene()
        OldMan "Perfect, one more photo in this position and the kids can go in"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_6
        OldMan "Okay, guys, come here, let's start with you"
        Villager "All right!"
        YoungVillager "Well, let's get started... I'm a little nervous"
        OldMan "Don't worry, you will do well, you are very young and you have a lot of energy"
        Johan "(what the hell does he mean by that... now that Leyna is showing practically everything I'm not liking this at all)"
        $ show_picture(16, "photohot13")
        $ resolve_scene()
        YoungVillager "Well, here we are, how do we get on?"
        OldMan "This way you are perfect for the first photo, stand still"
        Villager "Sure"
        Leyna "..."
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_7
        OldMan "Okay now both of you touch him on his belly and you pretend to kiss his neck"
        Villager "O-okay"
        Johan "!!!"
        Johan "(Shit, things are starting to get too spicy for my taste...should I stop it? but I don't want Leyna to lose her job because of me)"
        $ show_picture(17, "photohot14")
        $ resolve_scene()
        OldMan "That's it! very good, stay still"
        Leyna "(.... he was supposed to pretend he was kissing my neck, not really kissing it...this guy is taking advantage)"
        Leyna "(although it feels so good... I feel chills all over my spine and the back of my neck.... does it have something to do with the herbs they put in the water?)"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_8
        OldMan "All right, that's enough, now, Leyna turn around and get your ass up"
        Leyna "! Su-sure"
        Johan "(what is he intending to do?)"
        OldMan "All right guys, time to bring out the artillery, take off your loincloths and get your dicks out, I want you to grab them and smack Leyna's ass with them"
        Johan "!!!! B-but!"
        $ show_picture(18, "photohot15")
        $ resolve_scene()
        Villager "Sure!"
        YoungVillager "It will be a pleasure! (Slap slap slap slap)"
        Leyna "!!! (They've already started hitting me with their dicks and Johan is right there... he seems to be a bit shocked with what's going on)"
        Villager "(Slap slap slap) Does this look good to you?"
        OldMan "Yes! I recorded a short video with the camera to send it to them, they wanted to make a gif for the web page"
        OldMan "Now, stand still"
        Villager "Yeah"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_9
        OldMan "Great, Leyna, turn around"
        Leyna "O-okay"
        pause
        $ show_picture(19, "photohot16")
        $ resolve_scene()
        OldMan "Perfect, guys, stay like this! with your penises as close to her as possible"
        Villager "Glad to do it"
        Johan "(Shit... I would like nothing more than to stop this nonsense, control yourself Johan, don't be like this,  the previous one was worse...)"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_10
        OldMan "You guys are doing great, what a stamina you have, I don't know how you can last so long with that erection"
        YoungVillager "Well, with Leyna in this position and so close to us we don't have to try very hard hahahaha"
        Villager "Yes! it's rare to see such a sexy woman even in a porn magazine"
        OldMan "Ah, youth is a wonderful thing!"
        Johan "(Shut the fuck up...)"
        OldMan "All right, now lift her up by her legs, it' s going to look great in the photo"
        pause
        $ show_picture(20, "photohot17")
        $ resolve_scene()
        Leyna "Oh!"
        Villager "Like this?"
        OldMan "That's perfect!"
        Villager "Miss, you weigh nothing"
        Leyna "hahahaha shut up, I know I've put on weight, don't suck up to me"
        Johan "(Leyna is laughing with them? are they flirting? Shit...)"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_11
        OldMan "A spectacular photo"
        OldMan "Now take her down and... pull down her swimsuit, let those tits be seen well"
        Villager "Sure! it will be a pleasure"
        Johan "Wh-what?!"
        Leyna "!"
        $ show_picture(21, "photohot18")
        $ resolve_scene()
        Leyna "Ah! you-could warn before doing something like that!"
        Villager "Sorry"
        Leyna "N-no problem"
        OldMan "Perfect as always"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_12
        OldMan "this is turning out to be a very good photo shoot, I'm sure the magazine will be very happy with your work"
        Leyna "Thanks..."
        OldMan "All right boy, lift Leyna's leg, it's time to turn it up a notch"
        pause
        $ show_picture(22, "photohot19")
        $ resolve_scene()
        OldMan "Very good, that position is perfect, hold it like that a little longer"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_13
        OldMan "This is very good, now you have to move the lower part of the bathing suit a little bit so that her pussy is open to the air"
        Leyna "!!!!"
        Villager "Okay, I'm going to do it, okay Leyna?"
        Leyna "I-I don't know if I should..."
        OldMan "Come on Leyna, you can see practically everything, the magazine has asked us for it"
        Leyna "Well... okay"
        Johan "(Wait, she agrees just like that? in the previous session something similar and worse happened... but I'm not sure about it)"
        pause
        $ show_picture(23, "photohot20")
        $ resolve_scene()
        OldMan "Great"
        OldMan "From close it looks perfect, I'm going to take a good picture"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_14
        OldMan "Please, place your member against Leyna's pussy, let it touch it lightly"
        Villager "Okay"
        pause
        $ show_picture(24, "photohot21")
        $ resolve_scene()
        Leyna "(I'm starting to get wet down there... I hope they don't notice, with all these fumes they might think it's just humidity...)"
        Villager "(Whispering) Wow, your pussy is so wet.... You get excited very fast, don't you?"
        Leyna "!!! (He noticed!)"
        $ flash_screen([255,255,255,170], 60, True)
        call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_15
        OldMan "a spectacular photo! let's advance a little more and introduce the tip little by little, I want to take a couple of photos of the process"
        Villager "Sure!"
        Johan "(Wait, what?! Stick it in? They're going to stick their dicks in my wife right here while they're photographing it?)"
        call GetChoice([_("Say nothing"), _("Hey!!")], value=menu_choice, called_from="Town2fotografo_13") from _call_Town2fotografo_13_GetChoice_1
        $ menu_choice = _return
        if menu_choice == _("Say nothing"):
            $ menu_choice = None
            $ show_picture(25, "photohot39")
            $ resolve_scene()
            Johan "(It's like that time... I can't help but remain silent as I watch all this happen)"
            Johan "(I feel like vomiting again, while I have a feeling of vertigo... but at the same time I have an uncontrollable erection)"
            Johan "(I feel like a shithead and a coward)"
            $ show_picture(26, "photohot23")
            $ resolve_scene()
            $ flash_screen([255,255,255,170], 60, True)
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_16
            Leyna "Oh! hmmmm!"
            Villager "It's going in like it's nothing... you're dripping"
            Leyna "Shu-shut up"
            Villager "(Whispering) Or what? your husband is right there looking like an idiot watching everything and he hasn't said a word"
            Leyna "!!! I-I, don't talk like that about my hus..."
            pause
            $ show_picture(27, "photohot24")
            $ resolve_scene()
            Leyna "HMMAAH!! MY GOD!"
            Johan "(My wife just moaned?....)"
            Villager "What were you saying? I didn't hear you"
            Leyna "Ah ah ah! Ass-asshole"
            $ flash_screen([255,255,255,170], 60, True)
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_17
            OldMan "You guys are doing great"
            OldVillager "Now take it out, I want to take another picture from that angle"
            Villager "... Sure, whatever you say"
            pause
            $ show_picture(28, "photohot25")
            $ resolve_scene()
            Leyna "(I feel it deep inside of me.... feeling it so deep inside me I'm already about to cum)"
            Villager "(Whispering) Too bad I have to take it out, isn't it? I can feel you contracting in there, you're about to cum, aren't you?"
            Leyna "!!!! N-no"
            Villager "Well then I'm going to take it out"
            Leyna "!!! hmma"
            $ show_picture(29, "photohot26")
            $ resolve_scene()
            $ flash_screen([255,255,255,170], 60, True)
            "Plop"
            Leyna "Oh my god..."
            OldMan "What a great sound, you were having a good time Leyna"
            Johan "(Having a good time...? Leyna was enjoying it?)"
            Johan "(Of course she was enjoying herself, just look at her face, she' s as red as a tomato and has an orgasmic expression...)"
            Johan "(I should never have agreed to this)"
            $ flash_screen([255,255,255,170], 60, True)
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_18
            OldMan "All right Leyna, climb on the young guy, let's go to the next position"
            Leyna "Ah ah ah... O-okay..."
            pause
            $ show_picture(30, "photohot27")
            $ resolve_scene()
            Leyna "Li-like this? Is that okay?"
            OldMan "That's fine"
            $ flash_screen([255,255,255,170], 60, True)
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_19
            OldMan "Do you have your dick pressed against his ass?"
            Villager "Yes, I have it"
            OldMan "All right, I'm going to take a picture from below"
            pause
            $ show_picture(31, "photohot28")
            $ resolve_scene()
            OldMan "Yes... This angle is very good"
            $ flash_screen([255,255,255,170], 60, True)
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_20
            OldMan "Of course the magazine is going to love it, but especially the next picture, guys...."
            OldMan "I want both of you to stick it in her at the same time, one in each hole, be careful not to hurt Leyna, she is our star model"
            Johan "(WHAT?! They're going to stick it in both sides?! I'm sure Leyna won't agree...)"
            Leyna "W-what do you mean, one on each side?! that's too much, guys! you're going to break me in half!"
            OldMan "No way lady! don't worry, the guys will be careful and besides... you'd be surprised how far a woman's body can go!"
            Leyna "B-but!"
            OldMan "Relax, think about what the magazine is going to pay us! When you get a new car, you will forget all this!"
            Leyna "I..."
            Johan "(It can't be... this can't be happening)"
            pause
            $ show_picture(32, "photohot29")
            $ resolve_scene()
            $ flash_screen([255,255,255,170], 60, True)
            Leyna "!!! OH MY GOD! OHHHH"
            Villager "Hahahaha seems to be liking it"
            YoungVillager "It's a pity we can't move... I wish we weren't working and we could have a good time"
            $ flash_screen([255,255,255,170], 60, True)
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_21
            pause
            $ show_picture(33, "photohot31")
            $ resolve_scene()
            OldMan "Leyna everything ok?"
            Leyna "Aaahh ah ahhh ...."
            YoungVillager "I don't think she can talk right now, with two cocks deep inside her hahahaha"
            Johan "(They are laughing, they are making fun of Leyna while they fuck her like animals.... well they are still, but nevertheless)"
            Johan "(And here I am, looking like a fucking loser, unable to move and with my dick as hard as a rock...)"
            Johan "(How could I let this happen? how could I let us get into this situation? after this... how am I going to look her in the eyes?)"
            $ flash_screen([255,255,255,170], 60, True)
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_22
            OldMan "All right guys, that's enough, go down to Leyna and have her give you a titfuck, it'll be great for the end"
            YoungVillager "A titfuck?! great!"
            pause
            $ show_picture(34, "photohot32")
            $ resolve_scene()
            YoungVillager "Wow it feels amazing! keep it up Leyna and I'll be cumming in no time!"
            Leyna "I-I see..."
            $ flash_screen([255,255,255,170], 60, True)
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_23
            OldMan "Very well done guys, the photo came out spectacular"
            YoungVillager "Well, we've got a real pro here.... my god, what a soft tits you have Leynar"
            Villager "Hey I'm getting jealous, come here"
            Leyna "???"
            OldMan "Wai..."
            pause
            $ show_picture(35, "photohot33")
            call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2fotografo_13_PlaySound_24
            $ resolve_scene()
            OldMan "Oh well... I guess it's okay to let off some steam after all"
            Leyna "???? AAuughggaah"
            Villager "What are you saying? I can't hear you, Leyna"
            $ flash_screen([255,255,255,170], 60, True)
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_25
            OldMan "It is certainly a good photo..."
            Leyna "(I c-can't breathe)"
            Villager "Oooh I'm going to cum... I've been holding it in for a long time!"
            YoungVillager "Me too!"
            Villager "Get ready Leyna here I come!"
            Leyna "???"
            $ flash_screen([255,255,255,170], 60, True)
            $ show_picture(36, "photohot34")
            $ resolve_scene()
            Leyna "Wh-what are you doing?"
            Villager "Open your mouth Leyna! OPEN IT, IT'S COMING!"
            Leyna "Ah?"
            Johan "(You're not going to do it, are you? Leyna!)"
            pause
            $ show_picture(37, "photohot35")
            $ resolve_scene()
            $ flash_screen([255,255,255,170], 60, True)
            stop bgs fadeout 1
            Villager "OOOooohh!!!!!"
            YoungVillager "OOOoohh Shit!!"
            Villager "A little more and my dick explodes!"
            pause
            $ show_picture(38, "photohot36")
            $ resolve_scene()
            Leyna "Ah... ah ah ah...."
            OldMan "Very good Leyna! stay like this!"
            $ flash_screen([255,255,255,170], 60, True)
            call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_Town2fotografo_13_PlaySound_26
            OldMan "WWOW perfect! we will get paid a lot for this last picture very good idea guys!"
            Villager "Thanks!"
            YoungVillager "Look at her! she is like a work of art, I feel like a real artist!"
            OldMan "Well with this we have finished"
            OldMan "Leyna, there is a shower back there, I think you need it"
            Villager "You're telling me..."
            $ fade_out()
            $ set_switch("johan_does_nothing", True)
            call TransferPlayer("Path", "Town2fotografo_13", 19, 9, direction=0) from _call_Town2fotografo_13_TransferPlayer_1
            call Movement("Town2fotografo_13", "player", ["R","R","R","TURN_L"]) from _call_Town2fotografo_13_Movement_1
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
            $ erase_picture(36)
            $ erase_picture(37)
            $ erase_picture(38)
            $ set_self_switch("Town2","Town2fotografo","C",True)
            $ set_switch("hotsprings_photo_session", True)
            call GalleryViewed("photohot") from _call_Town2fotografo_13_GalleryViewed
            $ fade_in()
            $ resolve_scene()
            call PauseForBalloon("Town2fotografo_13") from _call_Town2fotografo_13_PauseForBalloon
            Leyna "Jo-johan?"
            Johan "Johan? JOHAN? What the hell have you done?!"
            Leyna "I..."
            Johan "I have seen it all! I saw how you were moaning with pleasure, you were loving it!"
            Leyna "B-but you... agreed"
            Johan "Yes, for a somewhat erotic session! Not to get fucked in every hole!"
            Johan "And to see your face... so lewd, enjoying it so much... it makes me sick!"
            Leyna "Johan, stop..."
            Johan "NO! How am I supposed to be able to keep looking at your face after this? How am I..."
            Leyna "JOHAN!"
            Johan "!!!!"
            Leyna "Johan listen to me... Yes, I enjoyed it, I'm sorry but I did it, it's normal, I'm a person and if I'm touched... there, I react, I'm sorry"
            Leyna "But that doesn't mean anything, do you understand? I..."
            if johan_leyna_sex == 2:
                $ resolve_scene()
                $ flash_screen([255,255,255,170], 60, True)
                $ show_picture(1, "johanfollar9")
                $ resolve_scene()
                Leyna "Look, I'll be honest with you... no matter how big their dicks are, you're the one that makes me cum when we do it"
                Leyna "What good does it do them to have the dick of a horse, if they are useless?"
                $ erase_picture(1)
            if johan_leyna_sex == 1:
                $ resolve_scene()
                Leyna "Yes, our sex has not been the best in the world, especially since we came to this town"
                Leyna "But I love you Johan, I love you more than I've ever loved anyone"
                Leyna "And no matter how many guys with horse dicks you put in front of me I'll still love you with madness"
                Leyna "Because life doesn't revolve around sex, Johan.... I'd rather have someone like you than a tripod with two brain cells"
            $ resolve_scene()
            Leyna "S-so please calm down"
            Leyna "Why don't we wipe the slate clean, Johan? Let's forget that today happened, okay?"
            Johan "I... I guess you're right... but I still feel like crap right now..."
            Leyna "Johan, I love you, that's all that matters, isn't it? at least that's all that matters to me"
            Johan "!!!!"
            Leyna "I want to spend the rest of my life with you... so let's just forget about all this, okay?"
            Johan "..."
            Leyna "Johan?"
            Johan "Yes... you are right"
            Leyna "You should take it down a notch... these things, you know..."
            Johan "I can't help but get jealous...."
            Leyna "Well... let's leave the subject, let's go Johan"
            Johan "Yes..."
        elif menu_choice == _("Hey!!"):
            $ menu_choice = None
            Johan "(I-I can't let that happen!)"
            $ show_picture(25, "photohot40")
            $ resolve_scene()
            Johan "Hey! stop right now!!!"
            Leyna "!!!! (Johan!)"
            OldMan "What? What are you saying?"
            Johan "I said stop right now! I'm not going to let them fuck my wife right under my nose!"
            OldMan "Fuck..."
            Villager "Wow, the husband has grown some balls"
            Johan "Shut the fuck up you dumb fuck!"
            Villager "..."
            Johan "Leyna get out of there right now, let's get out of here"
            Leyna "Y-yeah"
            OldMan "Do you even know what you are doing? it's a golden opportunity!"
            Johan "I don't give a fuck, we're leaving... and forget about Leyna as a model for your fucking magazine"
            OldMan "You're losing a lot of money right now...."
            Johan "I don't care! But you'd better pay my wife for the sessions she's already done!"
            Johan "My best friend in town is a hell of a lawyer and he can have your balls cut off in court if you don't pay us"
            OldMan "!!! O-okay, don't get like that Johan, as soon as I get the money I'll give it to you"
            Johan "All right, now we're leaving!"
            Leyna "Y-yes"
            $ fade_out()
            $ set_switch("johan_rejects", True)
            call TransferPlayer("Path", "Town2fotografo_13", 22, 9, direction=6) from _call_Town2fotografo_13_TransferPlayer_2
            call Movement("Town2fotografo_13", "player", ["R","R","TURN_L"]) from _call_Town2fotografo_13_Movement_2
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
            $ fade_in()
            $ resolve_scene()
            call PauseForBalloon("Town2fotografo_13") from _call_Town2fotografo_13_PauseForBalloon_1
            Johan "Fucking asshole!"
            Leyna "Johan..."
            Johan "WHAT?!"
            Leyna "!!!"
            Johan "Don't look at me like I'm crazy, I saw how you were enjoying it!"
            Leyna "Johan, how can you talk to me like that?"
            Johan "!!! I! ... (I'm yelling at Leyna, with so much anger.{p}...)"
            if johan_leyna_sex == 1:
                $ resolve_scene()
                $ flash_screen([255,255,255,170], 60, True)
                $ show_picture(1, "johanfollar6")
                $ resolve_scene()
                Johan "(Am I taking it out on her because I couldn't deliver that time?.... after seeing the size of that guy Was I intimidated?)"
            if johan_leyna_sex == 2:
                Johan "(I shouldn't get like this with Leyna... even though)"
                $ flash_screen([255,255,255,170], 60, True)
                $ show_picture(1, "johanfollar9")
                $ resolve_scene()
                Johan "(That time it was clear that we are very compatible, I know that I am able to satisfy Leyna better than any fucking hillbilly)"
            $ erase_picture(1)
            $ resolve_scene()
            Johan "I am very sorry Leyna... But I can't let them do that to you in front of me, I know it's your job and you could have earned a lot of money"
            Johan "But you are my wife and I love you! and if being jealous and not letting them do those things to you is bad then I am a horrible person"
            Johan "But that's just the way I am, I love you too much to see you like this, I'm sorry"
            Leyna "Oh Johan, don't be sorry, I love you! I'm sorry I took that job, I promise I won't do those photo shoots again!"
            Johan "!!!... Y-you're not upset?"
            Leyna "Of course not! with this you show me that you love me, in spite of all our problems... I know that you love me madly and that is enough for me"
            Johan "Leyna..."
            Leyna "Come on Johan, let's play it down and have a good time!"
            Johan "Yes!"
            $ set_self_switch("Town2","Town2fotografo","C",True)
            $ set_switch("hotsprings_photo_session", True)
            call GalleryViewed("photohot") from _call_Town2fotografo_13_GalleryViewed_1
    elif menu_choice == _("I can't do it"):
        $ menu_choice = None
        $ resolve_scene()
        OldMan "I see you are still so reserved on the subject of Leyna..."
        Johan "Well... it's normal, she's my wife after all"
        OldMan "Yes yes, your wife... well if you change your mind you know where I am, we have all day, but it is a unique opportunity... to let it pass would be..."
        Johan "I understand... I'm sorry Leyna, I need to think about it some more"
        Leyna "D-Don't worry Johan... I understand, I'm not so sure myself"
        Johan "I see... thank you"
    call PlaySound("music", "audio/Town1.ogg", volume=0.9, no_loop=False) from _call_Town2fotografo_13_PlaySound_27
    $ resolve_scene()
    return False

label Town2fotografo(play_event = True, trigger = None): # event
    if is_erased("Town2fotografo"):
        return None
    elif self_switch("Town2","Town2fotografo","C"):
        return None
    elif trigger == "event" and switch("river_3"):
        call PlayEvent(play_event, "Town2fotografo_13", "Town2fotografo") from _call_Town2fotografo_13_PlayEvent
        return (1, "", "Town2fotografo_13")
    elif trigger == "event" and self_switch("Town2","Town2fotografo","B"):
        call PlayEvent(play_event, "Town2fotografo_12", "Town2fotografo") from _call_Town2fotografo_12_PlayEvent
        return (0, "", "Town2fotografo_12")
    elif trigger == "event" and self_switch("Town2","Town2fotografo","A") and switch("hotsprings_together"):
        call PlayEvent(play_event, "Town2fotografo_11", "Town2fotografo") from _call_Town2fotografo_11_PlayEvent
        return (1, "", "Town2fotografo_11")
    elif trigger == "event" and switch("hotsprings_together"):
        call PlayEvent(play_event, "Town2fotografo_10", "Town2fotografo") from _call_Town2fotografo_10_PlayEvent
        return (1, "", "Town2fotografo_10")
    elif trigger == "event" and ritual >= 2:
        call PlayEvent(play_event, "Town2fotografo_9", "Town2fotografo") from _call_Town2fotografo_9_PlayEvent
        return (1, "", "Town2fotografo_9")
    elif switch("find_youth"):
        return None
    elif leyna_work >= 11:
        return None
    elif trigger == "event" and masks >= 2:
        call PlayEvent(play_event, "Town2fotografo_6", "Town2fotografo") from _call_Town2fotografo_6_PlayEvent
        return (1, "", "Town2fotografo_6")
    elif trigger == "event" and masks >= 1:
        call PlayEvent(play_event, "Town2fotografo_5", "Town2fotografo") from _call_Town2fotografo_5_PlayEvent
        return (1, "", "Town2fotografo_5")
    elif trigger == "event" and switch("leyna_dream_end"):
        call PlayEvent(play_event, "Town2fotografo_4", "Town2fotografo") from _call_Town2fotografo_4_PlayEvent
        return (1, "", "Town2fotografo_4")
    elif switch("johan_silent"):
        return None
    elif switch("johan_intervened"):
        return None
    elif trigger == "event" and switch("johan_photo"):
        call PlayEvent(play_event, "Town2fotografo_1", "Town2fotografo") from _call_Town2fotografo_1_PlayEvent
        return (1, "", "Town2fotografo_1")
    elif trigger == "event" and switch("third_day"):
        call PlayEvent(play_event, "Town2fotografo_0", "Town2fotografo") from _call_Town2fotografo_0_PlayEvent
        return (1, "", "Town2fotografo_0")
    return None

label Town2finalfiestafestival_v4_0:
    call PauseForBalloon("Town2finalfiestafestival_v4_0") from _call_Town2finalfiestafestival_v4_0_PauseForBalloon
    Johan "My God, my head is killing me... I have to find Leyna, where is she?"
    $ fade_out()
    $ show_picture(1, "reencuentro1", width=814, height=624)
    $ fade_in()
    $ resolve_scene()
    "An hour later..."
    Johan "I've been looking for her for a long time, she wasn't in the inn room, where did she go?"
    Johan "I still can't quite remember what happened last night... and I don't know if I want to, both of us have done something we might regret"
    Johan "or nothing has happened... which I wish it were true"
    Johan "!!!!"
    Johan "Wait a second... that's Leyna! And she's with... Shit, she's with Alexa..."
    pause
    $ show_picture(2, "reencuentro2", width=814, height=624)
    $ resolve_scene()
    Johan "H-hey girls... I've been looking for you..."
    Leyna "Hi sweetie!"
    Alexa "Hey Johan! how's it going? how's your hangover? hahahaha"
    Johan "(Wow... they don't seem to be angry... in fact they seem quite happy... so surely nothing happened yesterday?)"
    Johan "(it must have been a bad dream... my god I feel so relieved, I don't know what would have happened if  all that I was imagining was true)"
    Johan "W-well, I feel like I've been run over by a car, but I'm okay I guess"
    Johan "And you, don't you have a hangover?"
    Alexa "Well... yes and no, we woke up shattered like you, but I have taught Leyna the trick of how to get rid of hangovers"
    Johan "The trick?"
    Alexa "Yeah! nothing like drinking a couple of beers and the hangover goes away hahahaha"
    Johan "Oh... I see... and the two of you have met in town?"
    Alexa "Oh no... yesterday I saw that your wife was quite drunk and I invited her to spend the night in my room... since you had disappeared, where were you?"
    Johan "I... I don't know, I woke up this morning in a field on the outskirts of town"
    Johan "So you are well Leyna?"
    $ show_picture(3, "reencuentro3", width=814, height=624)
    $ resolve_scene()
    Leyna "Hahaha yeah, I'm fine.... I'm still a little drunk and the beers we had with our friend didn't help hahaha"
    Johan "Friend?...ah, this guy?"
    $ erase_picture(3)
    $ resolve_scene()
    Villager "zzzzz...."
    Johan "It looks like he's out of action..."
    Alexa "Yes... our friend here is out cold... he hasn't been able to sleep much tonight hehehehehehe"
    Johan "???"
    Johan "I see... Well Leyna, will you come with me?"
    Leyna "Sure, let's go for a walk, at least I got a good night's sleep"
    Alexa "In a while I will go to the river to cool off, the cold water is also very good for the hangover, we will be almost all day out there, so come if you want to"
    Johan "Sure... we will consider it... let's go Leyna?"
    Leyna "Sure!"
    Alexa "Well guys, see you later"
    Leyna "Of course! see you later!"
    $ fade_out()
    $ erase_picture(1)
    $ erase_picture(2)
    call TransferPlayer("Town2", "Town2finalfiestafestival_v4_0", 1, 21, direction=6) from _call_Town2finalfiestafestival_v4_0_TransferPlayer
    call ChangePartyMember("Leyna", True) from _call_Town2finalfiestafestival_v4_0_ChangePartyMember
    call Movement("Town2finalfiestafestival_v4_0", "player", ["R","R"]) from _call_Town2finalfiestafestival_v4_0_Movement
    $ fade_in()
    $ resolve_scene()
    Johan "Well, what could we do today?"
    Leyna "We can always go to the river with Alexa"
    Johan "I guess so"
    Leyna "You know what? Look, let's go to the river, I think we could both use a little hangover relief and a chance to clear our heads a bit"
    Johan "You are right"
    $ set_self_switch("Town2","Town2finalfiestafestival_v4","A",True)
    return False

label Town2finalfiestafestival_v4(play_event = True, trigger = None): # event
    if is_erased("Town2finalfiestafestival_v4"):
        return None
    elif self_switch("Town2","Town2finalfiestafestival_v4","A"):
        return None
    elif switch("river_3"):
        return None
    elif trigger == "event" and switch("party_at_festival"):
        call PlayEvent(play_event, "Town2finalfiestafestival_v4_0", "Town2finalfiestafestival_v4") from _call_Town2finalfiestafestival_v4_0_PlayEvent
        return (0, "", "Town2finalfiestafestival_v4_0")
    return None

label Town2ToGladeBase:
    call TransferPlayer("Glade", "Town2EV083", 0, 5, direction=6) from _call_Town2EV083_TransferPlayer
    $ resolve_scene()
    return False

label Town2ToGlade(play_event = True, trigger = None): # event
    if is_erased("Town2ToGlade"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2ToGladeBase", "Town2ToGlade") from _call_Town2ToGlade_PlayEvent
        return (0, "", "Town2ToGlade")
    return None

label Town2ToGlade_v2Base:
    call TransferPlayer("Glade", "Town2EV084", 0, 6, direction=6) from _call_Town2EV084_TransferPlayer
    $ resolve_scene()
    return False

label Town2ToGlade_v2(play_event = True, trigger = None): # event
    if is_erased("Town2ToGlade_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2ToGlade_v2Base", "Town2ToGlade_v2") from _call_Town2ToGlade_v2_PlayEvent
        return (0, "", "Town2ToGlade_v2")
    return None

label Town2finalfiestafestival_v5_0:
    call PauseForBalloon("Town2finalfiestafestival_v5_0") from _call_Town2finalfiestafestival_v5_0_PauseForBalloon
    Johan "My God, my head is killing me... I have to find Leyna, where is she?"
    $ fade_out()
    $ show_picture(1, "reencuentro1", width=814, height=624)
    $ fade_in()
    $ resolve_scene()
    "An hour later..."
    Johan "I've been looking for her for a long time, she wasn't in the inn room, where did she go?"
    Johan "I still can't quite remember what happened last night... and I don't know if I want to, both of us have done something we might regret"
    Johan "or nothing has happened... which I wish it were true"
    Johan "!!!!"
    Johan "Wait a second... that's Leyna! And she's with... Shit, she's with Alexa..."
    pause
    $ show_picture(2, "reencuentro2", width=814, height=624)
    $ resolve_scene()
    Johan "H-hey girls... I've been looking for you..."
    Leyna "Hi sweetie!"
    Alexa "Hey Johan! how's it going? how's your hangover? hahahaha"
    Johan "(Wow... they don't seem to be angry... in fact they seem quite happy... so surely nothing happened yesterday?)"
    Johan "(it must have been a bad dream... my god I feel so relieved, I don't know what would have happened if  all that I was imagining was true)"
    Johan "W-well, I feel like I've been run over by a car, but I'm okay I guess"
    Johan "And you, don't you have a hangover?"
    Alexa "Well... yes and no, we woke up shattered like you, but I have taught Leyna the trick of how to get rid of hangovers"
    Johan "The trick?"
    Alexa "Yeah! nothing like drinking a couple of beers and the hangover goes away hahahaha"
    Johan "Oh... I see... and the two of you have met in town?"
    Alexa "Oh no... yesterday I saw that your wife was quite drunk and I invited her to spend the night in my room... since you had disappeared, where were you?"
    Johan "I... I don't know, I woke up this morning in a field on the outskirts of town"
    Johan "So you are well Leyna?"
    $ show_picture(3, "reencuentro3", width=814, height=624)
    $ resolve_scene()
    Leyna "Hahaha yeah, I'm fine.... I'm still a little drunk and the beers we had with our friend didn't help hahaha"
    Johan "Friend?...ah, this guy?"
    $ erase_picture(3)
    $ resolve_scene()
    Villager "zzzzz...."
    Johan "It looks like he's out of action..."
    Alexa "Yes... our friend here is out cold... he hasn't been able to sleep much tonight hehehehehehe"
    Johan "???"
    Johan "I see... Well Leyna, will you come with me?"
    Leyna "Sure, let's go for a walk, at least I got a good night's sleep"
    Alexa "In a while I will go to the river to cool off, the cold water is also very good for the hangover, we will be almost all day out there, so come if you want to"
    Johan "Sure... we will consider it... let's go Leyna?"
    Leyna "Sure!"
    Alexa "Well guys, see you later"
    Leyna "Of course! see you later!"
    $ fade_out()
    $ erase_picture(1)
    $ erase_picture(2)
    call TransferPlayer("Town2", "Town2finalfiestafestival_v5_0", 1, 21, direction=6) from _call_Town2finalfiestafestival_v5_0_TransferPlayer
    call ChangePartyMember("Leyna", True) from _call_Town2finalfiestafestival_v5_0_ChangePartyMember
    call Movement("Town2finalfiestafestival_v5_0", "player", ["R","R"]) from _call_Town2finalfiestafestival_v5_0_Movement
    $ fade_in()
    $ resolve_scene()
    Johan "Well, what could we do today?"
    Leyna "We can always go to the river with Alexa"
    Johan "I guess so"
    Leyna "You know what? Look, let's go to the river, I think we could both use a little hangover relief and a chance to clear our heads a bit"
    Johan "You are right"
    $ set_self_switch("Town2","Town2finalfiestafestival_v5","A",True)
    return False

label Town2finalfiestafestival_v5(play_event = True, trigger = None): # event
    if is_erased("Town2finalfiestafestival_v5"):
        return None
    elif self_switch("Town2","Town2finalfiestafestival_v5","A"):
        return None
    elif switch("river_3"):
        return None
    elif trigger == "event" and switch("party_at_festival"):
        call PlayEvent(play_event, "Town2finalfiestafestival_v5_0", "Town2finalfiestafestival_v5") from _call_Town2finalfiestafestival_v5_0_PlayEvent
        return (0, "", "Town2finalfiestafestival_v5_0")
    return None

label Town2GraveBase:
    "Here lies Geralt of Rivia, the mercenary knight"
    return False

label Town2Grave(play_event = True, trigger = None): # event
    if is_erased("Town2Grave"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2GraveBase", "Town2Grave") from _call_Town2Grave_PlayEvent
        return (1, "", "Town2Grave")
    return None

label Town2Flashback_0:
    $ show_picture(1, "flash1")
    $ resolve_scene()
    Leyna "(I feel that things are getting out of control little by little... our relationship is gradually changing since we arrived in this town)"
    if switch("corruption_average"):
        $ resolve_scene()
        Leyna "(There have been some things that I deeply regret, but even so, I've been able to maintain a little bit of control, even though it is very difficult for me)"
    if switch("corruption_low"):
        Leyna "(As hard as it is for me, I have been able to keep the situation under control, although it is difficult with all the boys in town seducing me)"
    if switch("corruption_high"):
        Leyna "(I can hardly control myself, since I've come to this town I've been behaving like an out-of-control teenager....)"
        Leyna "(I've barely been able to turn down the guys who have been seducing me since I arrived and I've done things I thought I would never be able to do)"
    $ resolve_scene()
    Leyna "(Like yesterday at the festival....)"
    if festival_clothes == 1:
        $ show_picture(2, "festivalnoche23", width=814, height=625)
        $ resolve_scene()
        Leyna "(Things got out of control very, very quickly... it's a miracle Johan didn't realize what happened)"
        $ show_picture(3, "flash3")
        $ resolve_scene()
        Leyna "(Johan was just a few feet away and I... I was being fucked in the middle of a crowd)"
        Leyna "(Fortunately everyone was either extremely drunk or high on mushrooms...)"
        Leyna "(Including me... but I shouldn't make excuses I could have stopped the thing from going ahead.... But I didn't, because I was looking forward to it)"
        Leyna "(I wanted to be fucked like a bitch...)"
        pause
        $ show_picture(4, "flash4")
        $ resolve_scene()
        Leyna "(When I regained a minimum of my senses, I could not see Johan anywhere, for a second it crossed my mind that he had seen me...)"
        Leyna "(... And that, in anger, he had left the festival... but even so, at that moment, the only thing I wanted was... )"
        pause
        $ show_picture(5, "flash5")
        $ resolve_scene()
        Leyna "(That...)"
        "Layna. (So I got carried away... and went all the way with them)"
        Leyna "(I don't remember exactly what happened... I just remember that it was one of the best experiences of my life..."
        pause
        $ show_picture(6, "flash6")
        $ resolve_scene()
        Leyna "(Although I don't know if it was because of the herbs in the drink...)"
        Leyna "(Or because we really had a great time... but I had an amazing orgasm, I remember that...)"
        pause
        $ show_picture(7, "flash7")
        $ resolve_scene()
        Leyna "(Then... Alexa appeared and caught me in that situation... I didn't know how I was going to react)"
        pause
        $ show_picture(8, "pantallanegro", scale=(120, 120), width=816, height=600)
        $ resolve_scene()
        Leyna "(But she was extremely kind, got me out of there, took me to the inn's room and helped me clean up, then put me to bed and left me to sleep)"
        $ show_picture(9, "flash8")
        $ resolve_scene()
        "Leyna. (The next morning she was waiting for me downstairs with a cup of coffee and was accompanied by one of the guys from the village...)"
        Leyna "(She didn't say anything about last night, just smiled at me and talked about anything during the morning as if nothing had happened)"
        Leyna "(And then Johan arrived...)"
        $ show_picture(10, "flash2")
    if festival_clothes == 2:
        $ show_picture(2, "festivalnoche24", width=814, height=625)
        $ resolve_scene()
        Leyna "(Things got a little out of hand last night.... in the end not much happened, but it could have gotten out of hand in no time)"
        Leyna "(I saw Johan having a good time...  so I decided to have a good time myself)"
        pause
        $ show_picture(3, "flash9")
        $ resolve_scene()
        Leyna "(Let's say I got a little carried away by the atmosphere)"
        Leyna "(I danced a lot with the guys, they were horny and wanted to take advantage of the situation a little bit)"
        Leyna "(... well, what's the point of kidding myself, I let myself go a little bit)"
        Leyna "(I followed their lead... and provoked them a bit...)"
        pause
        $ show_picture(4, "flash10")
        $ resolve_scene()
        Leyna "(Maybe I provoked them too much... it was still fun to see how they behaved like teenagers and fought for my attention)"
        pause
        $ show_picture(5, "flash11")
        $ resolve_scene()
        Leyna "(They even made contests of... well)"
        Leyna "\"Wow, do you all have huge dicks in this town hahahaha is it because of the diet or what's going on here?\""
        pause
        $ show_picture(6, "flash12")
        $ resolve_scene()
        Leyna "(But there came a time when I was too drunk and anything could have happened...)"
        pause
        $ show_picture(7, "flash13")
        $ resolve_scene()
        Leyna "(But my boss from the bar showed up and really saved my ass... got the guys off my back)"
        $ show_picture(8, "flash14")
        $ resolve_scene()
        Leyna "(And take me to Alexa)"
        Barman "\"Hey you! she's your friend right? I've seen you together in town, Leyna is really drunk and she was surrounded by guys\""
        Alexa "\"Oh wow, thanks for bringing her, I'll take care of her, I'll take her to the inn right now\""
        $ fade_out()
        $ erase_picture(8)
        $ show_picture(8, "pantallanegro", scale=(120, 120), width=816, height=600)
        $ fade_in()
        $ resolve_scene()
        Leyna "(I barely remember what happened next, but it seems that Alexa took me to my room, helped me take a cold shower and laid me down on the bed)"
        $ show_picture(9, "flash8")
        $ resolve_scene()
        Leyna "(The next morning he was waiting for me with a local boy, coffee in hand, and we spent the rest of the morning together)"
        Leyna "(Until Johan came along)"
        $ show_picture(10, "flash2")
    $ resolve_scene()
    Leyna "(And now this situation happens...)"
    Leyna "(There are times when I feel as if Johan and I are drifting further and further apart as the days go by)"
    if johan_leyna_sex == 2:
        $ resolve_scene()
        Leyna "(But then we make love... and I realize that he is the one who knows me best... the only one who really makes me go crazy in bed)"
    if johan_leyna_sex == 1:
        Leyna "(And our situation in bed doesn't help.... Since we arrived, Johan is kind of lame, he is not what he used to be...)"
        Leyna "(He has never been spectacular in bed but he was good... but now he has become a slacker...he no longer has the energy he used to have....)"
        Leyna "(Will it be like this for the rest of our lives?...)"
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
    call TransferPlayer("Town2", "Town2Flashback_0", 18, 23, direction=0) from _call_Town2Flashback_0_TransferPlayer
    call Movement("Town2Flashback_0", "player", ["D","TURN_U"]) from _call_Town2Flashback_0_Movement
    $ fade_in()
    $ resolve_scene()
    Johan "Leyna? are you all right?"
    Leyna "Yes... I'm fine, I'm fine, I've just been numb thinking about my stuff"
    Johan "... Of course, the truth is that I have to go and talk to the mayor again, the festival is coming to an end"
    Johan "And I want to find out what's next so that I can finish my report for the magazine"
    Leyna "... Sure, then go talk to him, I'll take a walk around town"
    Johan "Yes... I won't be long, I'll see you in a little while"
    Leyna "Ok..."
    $ fade_out()
    call ChangePartyMember("Johan", False) from _call_Town2Flashback_0_ChangePartyMember
    $ fade_in()
    $ resolve_scene()
    Leyna "What should I do... I could stop by the bar to see how the boss is doing?"
    call GalleryViewed("flash") from _call_Town2Flashback_0_GalleryViewed
    $ set_self_switch("Town2","Town2Flashback","A",True)
    return False

label Town2Flashback(play_event = True, trigger = None): # autorun
    if is_erased("Town2Flashback"):
        return None
    elif self_switch("Town2","Town2Flashback","A"):
        return None
    elif trigger == "autorun" and switch("hotsprings_photo_session"):
        call PlayEvent(play_event, "Town2Flashback_0", "Town2Flashback") from _call_Town2Flashback_0_PlayEvent
        return (0, "", "Town2Flashback_0")
    return None

label Town2CorruptionFairy_0:
    $ event_erased = False
    $ fairy = 1
    $ resolve_scene()
    "Hello player! I want to introduce you to the corruption counter, this sculpture on my right"
    "Each time you win a corruption point, you will be able to see it here"
    "Some scenes require a minimum level of corruption"
    "so if you think you don't have it, come here and check it out"
    call ShowAnimation(117, "Town2CorruptionFairy", "Town2CorruptionFairy_0") from _call_Town2CorruptionFairy_0_ShowAnimation
    $ fairy = 2
    $ event_erased = True
    return event_erased

label Town2CorruptionFairy(play_event = True, trigger = None): # event
    if is_erased("Town2CorruptionFairy"):
        return None
    elif fairy >= 2:
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Town2CorruptionFairy_0", "Town2CorruptionFairy") from _call_Town2CorruptionFairy_0_PlayEvent
        return (1, "", "Town2CorruptionFairy_0")
    return None

label Town2EV090_0:
    label Town2EV090_0_loop_1:
        $ resolve_scene()
        call PauseForBalloon("Town2EV090_0") from _call_Town2EV090_0_PauseForBalloon
        # jump Town2EV090_0_loop_1
    label Town2EV090_0_loop_1_end:
        pass
    $ fairy = 1
    $ resolve_scene()
    return False

label Town2EV090(play_event = True, trigger = None): # None-only parallel
    if is_erased("Town2EV090"):
        return None
    elif fairy >= 1:
        return None
    elif trigger == "parallel":
        return None # Town2EV090_0 potentially infinite looping parallel
    return None

label unparalleledTown2EV091Base:
    $ tint_screen((0, 0, 0, 0), 60, True)
    return False

label Town2EV091Base:
    call ParallelAnimTintScreen(0, rgba=[0,0,0,0], interval=0) from _call_town2ev091base_ParallelTintScreen
    $ resolve_scene()
    return False

label Town2EV091(play_event = True, trigger = None): # parallel
    if is_erased("Town2EV091"):
        return None
    elif trigger == "parallel" and switch("second_river"):
        call PlayEvent(play_event, "Town2EV091Base", "Town2EV091") from _call_Town2EV091_PlayEvent
        return (0, "", "Town2EV091")
    return None

label Town2NPCPissedUpBase:
    Villager "..."
    return False

label Town2NPCPissedUp(play_event = True, trigger = None): # event
    if is_erased("Town2NPCPissedUp"):
        return None
    elif trigger == "event" and switch("festival_final"):
        call PlayEvent(play_event, "Town2NPCPissedUpBase", "Town2NPCPissedUp") from _call_Town2NPCPissedUp_PlayEvent
        return (1, "", "Town2NPCPissedUp")
    return None

label Town2AhBase:
    Villager "Ah?"
    return False

label Town2Ah(play_event = True, trigger = None): # event
    if is_erased("Town2Ah"):
        return None
    elif trigger == "event" and switch("festival_final"):
        call PlayEvent(play_event, "Town2AhBase", "Town2Ah") from _call_Town2Ah_PlayEvent
        return (1, "", "Town2Ah")
    return None

label Town2HeySweetieDoYouWantToHaveAGoodTime_0:
    $ show_picture(1, "callefinal1")
    $ resolve_scene()
    Villager "Hey sweetie! Do you want to have a good time?"
    Villager2 "Yeah hahahaha why don't you show us those great tits you have?"
    Leyna "hmmm?"
    Leyna "Want to see my boobs? .... hahahaha"
    Villager "????"
    pause
    $ show_picture(2, "callefinal2")
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_Town2EV094_0_PlaySound
    $ resolve_scene()
    Leyna "All right, here you go!"
    Villager "F-fuck she really took them out"
    Villager2 "My God... what a great pair of tits!"
    Leyna "Do you like them? hihihihihi you can touch them all you want...."
    Villager2 "What? really? cool..."
    Leyna "Yes really... you can do whatever you want with me! but only for a little while hihihihi"
    Villager2 "Is this bitch serious?"
    Villager "I don't know... but I don't care! this is too good an opportunity to pass up!"
    pause
    $ show_picture(3, "callefinal3")
    $ resolve_scene()
    Villager "Hmmf! fuck, they are so soft"
    Leyna "Ahhh... You' re doing great, big man... Do you like them?"
    Villager2 "Fuck what a bastard, she really meant it!"
    Villager2 "Wait... you said we can do whatever we want with you, right?... very well"
    pause
    $ show_picture(4, "callefinal4")
    $ resolve_scene()
    "Plas! "
    Leyna "I see that you like to go hard huh?....it is fine with me!"
    Villager2 "!!!  You're a real bitch! Now you'll see!"
    Villager "Hey wait, don't forget about me... so do what we want huh? very well I'm going to fuck you really good!"
    Leyna "Hihihi as you wish... I'm looking forward to it"
    Villager "!!! fuck... you're perfect"
    pause
    $ show_picture(5, "callefinal5")
    $ resolve_scene()
    Villager "Como here!"
    Leyna "AH! of course, as you wish"
    Villager2 "Hey they will see us"
    Villager "I don't care! I'll fuck this one right now!"
    Leyna "Yes please hehehehe"
    Villager2 "... Yes... let's fuck her!"
    pause
    $ show_picture(6, "callefinal6")
    $ resolve_scene()
    Villager "Ahhhh, It's so wet down there!"
    Villager2 "Hey man, I want some too"
    Villager "Weren't you ashamed because we were in public?"
    Villager3 "Nah I don't care! leave me some space!"
    Leyna "Come on, come on, don't fight, there's room for both of you hehehe"
    Villager "Fuck, I love this bitch"
    Villager2 "Here I come!"
    pause
    $ show_picture(7, "callefinal7")
    call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_Town2EV094_0_PlaySound_1
    $ resolve_scene()
    Villager "God, it feels so good!"
    Villager2 "Fuck, your ass feels like being in paradise it's so tight!"
    Leyna "Ah ah ah come on hit me harder! don't stop!"
    Villager "We don't plan to do that! I'm going to break you in half!"
    Leyna "AH ah ah ah!"
    Villager2 "F-fuck I'm gonna cum!"
    Leyna "What? already?"
    Villager "Y-yes, I can't do it anymore either! It's been so long since I've done it with a woman!"
    Leyna "...."
    pause
    $ show_picture(9, "callefinal8")
    $ resolve_scene()
    $ flash_screen([255,255,255,170], 60, False)
    Villagers "AAAAAHH!!!"
    Leyna "!!!! both of you at the same time! you're both in tune with each other hihihi"
    Villager "Ah ah fuck... this girl is a succubus"
    Leyna "Well... it was good, but you guys need to work on your stamina, you didn't make me cum hehehehehehe"
    Villager "!!!!"
    Villager2 "!!! I-I'll work on it, when you come back I'll be a real man for you!"
    Villager "Dude... have some dignity, do you want to marry her or something?"
    Villager2 "I-I... I wouldn't mind if she wants to, of course"
    Leyna "W-well, we'll see, maybe I'll come visit you one day, now I think I should go"
    call GalleryViewed("callefinal") from _call_Town2EV094_0_GalleryViewed
    Villager2 "S-sure..."
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
    $ set_self_switch("Town2","Town2HeySweetieDoYouWantToHaveAGoodTime","A",True)
    $ final_day = final_day + 1
    $ fade_in()
    $ resolve_scene()
    return False

label Town2HeySweetieDoYouWantToHaveAGoodTime(play_event = True, trigger = None): # event
    if is_erased("Town2HeySweetieDoYouWantToHaveAGoodTime"):
        return None
    elif self_switch("Town2","Town2HeySweetieDoYouWantToHaveAGoodTime","A"):
        return None
    elif trigger == "event" and switch("festival_final") and switch("corruption_high"):
        call PlayEvent(play_event, "Town2HeySweetieDoYouWantToHaveAGoodTime_0", "Town2HeySweetieDoYouWantToHaveAGoodTime") from _call_Town2HeySweetieDoYouWantToHaveAGoodTime_0_PlayEvent
        return (1, "", "Town2HeySweetieDoYouWantToHaveAGoodTime_0")
    return None

label Town2ToTownEntranceBase:
    call TransferPlayer("TownEntrance", "Town2EV095", 7, 0, direction=2) from _call_Town2EV095_TransferPlayer
    $ resolve_scene()
    return False

label Town2ToTownEntrance(play_event = True, trigger = None): # event
    if is_erased("Town2ToTownEntrance"):
        return None
    elif trigger == "event" and switch("festival_final"):
        call PlayEvent(play_event, "Town2ToTownEntranceBase", "Town2ToTownEntrance") from _call_Town2ToTownEntrance_PlayEvent
        return (0, "", "Town2ToTownEntrance")
    return None

label Town2ToTownEntrance_v2Base:
    call TransferPlayer("TownEntrance", "Town2EV096", 7, 0, direction=2) from _call_Town2EV096_TransferPlayer
    $ resolve_scene()
    return False

label Town2ToTownEntrance_v2(play_event = True, trigger = None): # event
    if is_erased("Town2ToTownEntrance_v2"):
        return None
    elif trigger == "event" and switch("festival_final"):
        call PlayEvent(play_event, "Town2ToTownEntrance_v2Base", "Town2ToTownEntrance_v2") from _call_Town2ToTownEntrance_v2_PlayEvent
        return (0, "", "Town2ToTownEntrance_v2")
    return None

label Town2ToTownEntrance_v3Base:
    call TransferPlayer("TownEntrance", "Town2EV097", 7, 0, direction=2) from _call_Town2EV097_TransferPlayer
    $ resolve_scene()
    return False

label Town2ToTownEntrance_v3(play_event = True, trigger = None): # event
    if is_erased("Town2ToTownEntrance_v3"):
        return None
    elif trigger == "event" and switch("festival_final"):
        call PlayEvent(play_event, "Town2ToTownEntrance_v3Base", "Town2ToTownEntrance_v3") from _call_Town2ToTownEntrance_v3_PlayEvent
        return (0, "", "Town2ToTownEntrance_v3")
    return None

label Town2ThinkIShouldGoToTheBusStopItShouldBeAboutToArrive_0:
    Leyna "think I should go to the bus stop, it should be about to arrive"
    $ set_self_switch("Town2","Town2ThinkIShouldGoToTheBusStopItShouldBeAboutToArrive","A",True)
    return False

label Town2ThinkIShouldGoToTheBusStopItShouldBeAboutToArrive(play_event = True, trigger = None): # autorun
    if is_erased("Town2ThinkIShouldGoToTheBusStopItShouldBeAboutToArrive"):
        return None
    elif self_switch("Town2","Town2ThinkIShouldGoToTheBusStopItShouldBeAboutToArrive","A"):
        return None
    elif trigger == "autorun" and final_day >= 2:
        call PlayEvent(play_event, "Town2ThinkIShouldGoToTheBusStopItShouldBeAboutToArrive_0", "Town2ThinkIShouldGoToTheBusStopItShouldBeAboutToArrive") from _call_Town2ThinkIShouldGoToTheBusStopItShouldBeAboutToArrive_0_PlayEvent
        return (0, "", "Town2ThinkIShouldGoToTheBusStopItShouldBeAboutToArrive_0")
    return None

