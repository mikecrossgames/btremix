label TownNightBG:
    $ set_transparency_backgrounds(["bg_town_south_night"])
    $ set_map_backgrounds(["map_town_south_night"])
    return

label TownNightStart:
    call TownNightBG from _call_TownNightBG
    stop music
    stop bgs
    return

label TownNightEnd:
    return

label TownNightBoarInnBase:
    "Boar Inn"
    return False

label TownNightBoarInn(play_event = True, trigger = None): # event
    if is_erased("TownNightBoarInn"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightBoarInnBase", "TownNightBoarInn") from _call_TownNightBoarInn_PlayEvent
        return (1, "", "TownNightBoarInn")
    return None

label TownNightToInnNightBase:
    call PlaySound("sound", "audio/Open1.ogg", volume=0.9, no_loop=True) from _call_TownNightEV003_PlaySound
    call Movement("TownNightEV003", "TownNightEV003", ["TURN_L",["WAIT",3],"TURN_R",["WAIT",3],"TURN_U","THROUGH_ON"]) from _call_TownNightEV003_Movement
    call Movement("TownNightEV003", "player", ["FORWARD"]) from _call_TownNightEV003_Movement_1
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_TownNightEV003_PlaySound_1
    call TransferPlayer("InnNight", "TownNightEV003", 8, 12, direction=0) from _call_TownNightEV003_TransferPlayer
    $ resolve_scene()
    return False

label TownNightToInnNight(play_event = True, trigger = None): # event
    if is_erased("TownNightToInnNight"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightToInnNightBase", "TownNightToInnNight") from _call_TownNightToInnNight_PlayEvent
        return (1, "", "TownNightToInnNight")
    return None

label TownNightStoreClosedBase:
    "(Closed)"
    return False

label TownNightStoreClosed(play_event = True, trigger = None): # event
    if is_erased("TownNightStoreClosed"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightStoreClosedBase", "TownNightStoreClosed") from _call_TownNightStoreClosed_PlayEvent
        return (1, "", "TownNightStoreClosed")
    return None

label TownNightClosed_v2Base:
    "(Closed)"
    return False

label TownNightClosed_v2(play_event = True, trigger = None): # event
    if is_erased("TownNightClosed_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightClosed_v2Base", "TownNightClosed_v2") from _call_TownNightClosed_v2_PlayEvent
        return (1, "", "TownNightClosed_v2")
    return None

label TownNightCorruptionCounterBase:
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

label TownNightCorruptionCounter(play_event = True, trigger = None): # event
    if is_erased("TownNightCorruptionCounter"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightCorruptionCounterBase", "TownNightCorruptionCounter") from _call_TownNightCorruptionCounter_PlayEvent
        return (1, "", "TownNightCorruptionCounter")
    return None

label TownNightMapBase:
    "River -> Festival <- Hot springs <- Coal mine <-"
    return False

label TownNightMap(play_event = True, trigger = None): # event
    if is_erased("TownNightMap"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightMapBase", "TownNightMap") from _call_TownNightMap_PlayEvent
        return (1, "", "TownNightMap")
    return None

label TownNightClosed_v3Base:
    "(Closed)"
    return False

label TownNightClosed_v3(play_event = True, trigger = None): # event
    if is_erased("TownNightClosed_v3"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightClosed_v3Base", "TownNightClosed_v3") from _call_TownNightClosed_v3_PlayEvent
        return (1, "", "TownNightClosed_v3")
    return None

label TownNightClosed_v4Base:
    "(Closed)"
    return False

label TownNightClosed_v4(play_event = True, trigger = None): # event
    if is_erased("TownNightClosed_v4"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightClosed_v4Base", "TownNightClosed_v4") from _call_TownNightClosed_v4_PlayEvent
        return (1, "", "TownNightClosed_v4")
    return None

label TownNightClosed_v5Base:
    "(Closed)"
    return False

label TownNightClosed_v5(play_event = True, trigger = None): # event
    if is_erased("TownNightClosed_v5"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightClosed_v5Base", "TownNightClosed_v5") from _call_TownNightClosed_v5_PlayEvent
        return (1, "", "TownNightClosed_v5")
    return None

label TownNightSeemsItsClosedBase:
    "Seems it's closed"
    return False

label TownNightSeemsItsClosed(play_event = True, trigger = None): # event
    if is_erased("TownNightSeemsItsClosed"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightSeemsItsClosedBase", "TownNightSeemsItsClosed") from _call_TownNightSeemsItsClosed_PlayEvent
        return (1, "", "TownNightSeemsItsClosed")
    return None

label TownNightCastlePosterBase:
    "Closed for restoration."
    return False

label TownNightCastlePoster(play_event = True, trigger = None): # event
    if is_erased("TownNightCastlePoster"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightCastlePosterBase", "TownNightCastlePoster") from _call_TownNightCastlePoster_PlayEvent
        return (1, "", "TownNightCastlePoster")
    return None

label TownNightCastlePoster_v2Base:
    "Closed for restoration."
    return False

label TownNightCastlePoster_v2(play_event = True, trigger = None): # event
    if is_erased("TownNightCastlePoster_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightCastlePoster_v2Base", "TownNightCastlePoster_v2") from _call_TownNightCastlePoster_v2_PlayEvent
        return (1, "", "TownNightCastlePoster_v2")
    return None

label TownNightPoliceAsleepBase:
    "(They must be resting..)"
    return False

label TownNightPoliceAsleep(play_event = True, trigger = None): # event
    if is_erased("TownNightPoliceAsleep"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightPoliceAsleepBase", "TownNightPoliceAsleep") from _call_TownNightPoliceAsleep_PlayEvent
        return (0, "", "TownNightPoliceAsleep")
    return None

label TownNightTheyMustBeResting_v2Base:
    "(They must be resting..)"
    return False

label TownNightTheyMustBeResting_v2(play_event = True, trigger = None): # event
    if is_erased("TownNightTheyMustBeResting_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightTheyMustBeResting_v2Base", "TownNightTheyMustBeResting_v2") from _call_TownNightTheyMustBeResting_v2_PlayEvent
        return (0, "", "TownNightTheyMustBeResting_v2")
    return None

label TownNightTheyMustBeResting_v3Base:
    "(They must be resting..)"
    return False

label TownNightTheyMustBeResting_v3(play_event = True, trigger = None): # event
    if is_erased("TownNightTheyMustBeResting_v3"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightTheyMustBeResting_v3Base", "TownNightTheyMustBeResting_v3") from _call_TownNightTheyMustBeResting_v3_PlayEvent
        return (0, "", "TownNightTheyMustBeResting_v3")
    return None

label TownNightmusicapuebloBase:
    call PlaySound("music", "audio/Ship1.ogg", volume=0.6, no_loop=False) from _call_TownNightmusicapueblo_PlaySound
    $ resolve_scene()
    $ tint_screen((-68, -68, 0, 68), 60, True)
    return False

label TownNightmusicapueblo(play_event = True, trigger = None): # parallel
    if is_erased("TownNightmusicapueblo"):
        return None
    elif trigger == "parallel":
        call PlayEvent(play_event, "TownNightmusicapuebloBase", "TownNightmusicapueblo") from _call_TownNightmusicapueblo_PlayEvent
        return (0, "", "TownNightmusicapueblo")
    return None

label TownNightPolicePosterBase:
    "Police station of Goddess cliff. to serve and protect."
    return False

label TownNightPolicePoster(play_event = True, trigger = None): # event
    if is_erased("TownNightPolicePoster"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightPolicePosterBase", "TownNightPolicePoster") from _call_TownNightPolicePoster_PlayEvent
        return (1, "", "TownNightPolicePoster")
    return None

label TownNightDataCityPosterBase:
    "Upper town"
    return False

label TownNightDataCityPoster(play_event = True, trigger = None): # event
    if is_erased("TownNightDataCityPoster"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightDataCityPosterBase", "TownNightDataCityPoster") from _call_TownNightDataCityPoster_PlayEvent
        return (1, "", "TownNightDataCityPoster")
    return None

label TownNightPillarBase:
    "Goddess Cliff: where dreams are lived day by day."
    return False

label TownNightPillar(play_event = True, trigger = None): # event
    if is_erased("TownNightPillar"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightPillarBase", "TownNightPillar") from _call_TownNightPillar_PlayEvent
        return (1, "", "TownNightPillar")
    return None

label TownNightClothingSignBase:
    "Happy pig Clothes and accessories"
    return False

label TownNightClothingSign(play_event = True, trigger = None): # event
    if is_erased("TownNightClothingSign"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightClothingSignBase", "TownNightClothingSign") from _call_TownNightClothingSign_PlayEvent
        return (1, "", "TownNightClothingSign")
    return None

label TownNightStoreSignBase:
    "General goods."
    return False

label TownNightStoreSign(play_event = True, trigger = None): # event
    if is_erased("TownNightStoreSign"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightStoreSignBase", "TownNightStoreSign") from _call_TownNightStoreSign_PlayEvent
        return (1, "", "TownNightStoreSign")
    return None

label TownNightGraveBase:
    "Here lies Geralt of Rivia, the mercenary knight"
    return False

label TownNightGrave(play_event = True, trigger = None): # event
    if is_erased("TownNightGrave"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightGraveBase", "TownNightGrave") from _call_TownNightGrave_PlayEvent
        return (1, "", "TownNightGrave")
    return None

label TownNightNPCSleep_0:
    Villager "I need some sleep"
    return False

label TownNightNPCSleep_1:
    YoungVillager "..."
    return False

label TownNightNPCSleep(play_event = True, trigger = None): # event
    if is_erased("TownNightNPCSleep"):
        return None
    elif trigger == "event" and bottle_event >= 3:
        call PlayEvent(play_event, "TownNightNPCSleep_1", "TownNightNPCSleep") from _call_TownNightNPCSleep_1_PlayEvent
        return (1, "", "TownNightNPCSleep_1")
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightNPCSleep_0", "TownNightNPCSleep") from _call_TownNightNPCSleep_0_PlayEvent
        return (1, "", "TownNightNPCSleep_0")
    return None

label TownNightNPCParty_0:
    Villager "Don't stop the party!!"
    return False

label TownNightNPCParty_1:
    YoungVillager "What a beautiful night"
    return False

label TownNightNPCParty(play_event = True, trigger = None): # event
    if is_erased("TownNightNPCParty"):
        return None
    elif trigger == "event" and bottle_event >= 3:
        call PlayEvent(play_event, "TownNightNPCParty_1", "TownNightNPCParty") from _call_TownNightNPCParty_1_PlayEvent
        return (1, "", "TownNightNPCParty_1")
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightNPCParty_0", "TownNightNPCParty") from _call_TownNightNPCParty_0_PlayEvent
        return (1, "", "TownNightNPCParty_0")
    return None

label TownNightTABLON_0(menu_choice = None):
    "What to do today:"
    call GetChoice([_("Bar 1"), _("Market"), _("Villagers"), _("River 1")], value=menu_choice, called_from="TownNightTABLON_0") from _call_TownNightTABLON_0_GetChoice
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

label TownNightTABLON_1(menu_choice = None):
    "What to do today:"
    call GetChoice([_("Photographer 1"), _("Hotsprings"), _("Photographer 2"), _("Bar 2"), _("River 2")], value=menu_choice, called_from="TownNightTABLON_1") from _call_TownNightTABLON_1_GetChoice
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

label TownNightTABLON_2(menu_choice = None):
    "What to do today:"
    call GetChoice([_("Photographer 3"), _("Worker's quest"), _("Dresser"), _("The dream"), _("Police station"), _("Night Party")], value=menu_choice, called_from="TownNightTABLON_2") from _call_TownNightTABLON_2_GetChoice
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

label TownNightTABLON_3(menu_choice = None):
    "What to do today:"
    call GetChoice([_("Police station"), _("Night Party"), _("Go to the festival")], value=menu_choice, called_from="TownNightTABLON_3") from _call_TownNightTABLON_3_GetChoice
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

label TownNightTABLON_4(menu_choice = None):
    "What to do today:"
    call GetChoice([_("Groceries store"), _("Bar"), _("Hot springs"), _("Flowers"), _("Come back to hotsprings"), _("Photographer")], value=menu_choice, called_from="TownNightTABLON_4") from _call_TownNightTABLON_4_GetChoice
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

label TownNightTABLON_5:
    "You have to find the boy, try to find him in upper town"
    return False

label TownNightTABLON(play_event = True, trigger = None): # event
    if is_erased("TownNightTABLON"):
        return None
    elif trigger == "event" and switch("find_youth"):
        call PlayEvent(play_event, "TownNightTABLON_5", "TownNightTABLON") from _call_TownNightTABLON_5_PlayEvent
        return (1, "", "TownNightTABLON_5")
    elif trigger == "event" and switch("leyna_dream_end"):
        call PlayEvent(play_event, "TownNightTABLON_4", "TownNightTABLON") from _call_TownNightTABLON_4_PlayEvent
        return (1, "", "TownNightTABLON_4")
    elif trigger == "event" and johan_dream >= 2:
        call PlayEvent(play_event, "TownNightTABLON_3", "TownNightTABLON") from _call_TownNightTABLON_3_PlayEvent
        return (1, "", "TownNightTABLON_3")
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "TownNightTABLON_2", "TownNightTABLON") from _call_TownNightTABLON_2_PlayEvent
        return (1, "", "TownNightTABLON_2")
    elif trigger == "event" and switch("finished_river_scene"):
        call PlayEvent(play_event, "TownNightTABLON_1", "TownNightTABLON") from _call_TownNightTABLON_1_PlayEvent
        return (1, "", "TownNightTABLON_1")
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightTABLON_0", "TownNightTABLON") from _call_TownNightTABLON_0_PlayEvent
        return (1, "", "TownNightTABLON_0")
    return None

label TownNightNPCLoveIt_0:
    Villager "I love this time of the year"
    return False

label TownNightNPCLoveIt_1:
    YoungVillager2 "Thanks for the company"
    return False

label TownNightNPCLoveIt(play_event = True, trigger = None): # event
    if is_erased("TownNightNPCLoveIt"):
        return None
    elif trigger == "event" and bottle_event >= 3:
        call PlayEvent(play_event, "TownNightNPCLoveIt_1", "TownNightNPCLoveIt") from _call_TownNightNPCLoveIt_1_PlayEvent
        return (1, "", "TownNightNPCLoveIt_1")
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightNPCLoveIt_0", "TownNightNPCLoveIt") from _call_TownNightNPCLoveIt_0_PlayEvent
        return (1, "", "TownNightNPCLoveIt_0")
    return None

label TownNightNPCWhatALovelyNightBase:
    OldWoman "What a lovely night"
    Villager "Yes it is"
    return False

label TownNightNPCWhatALovelyNight(play_event = True, trigger = None): # event
    if is_erased("TownNightNPCWhatALovelyNight"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightNPCWhatALovelyNightBase", "TownNightNPCWhatALovelyNight") from _call_TownNightNPCWhatALovelyNight_PlayEvent
        return (1, "", "TownNightNPCWhatALovelyNight")
    return None

label TownNightWhatALovelyNight_v2Base:
    OldWoman "What a lovely night"
    Villager "Yes it is"
    return False

label TownNightWhatALovelyNight_v2(play_event = True, trigger = None): # event
    if is_erased("TownNightWhatALovelyNight_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightWhatALovelyNight_v2Base", "TownNightWhatALovelyNight_v2") from _call_TownNightWhatALovelyNight_v2_PlayEvent
        return (1, "", "TownNightWhatALovelyNight_v2")
    return None

label TownNightSorryWeAreClosingBase:
    Merchant "Sorry, we are closing"
    return False

label TownNightSorryWeAreClosing(play_event = True, trigger = None): # event
    if is_erased("TownNightSorryWeAreClosing"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightSorryWeAreClosingBase", "TownNightSorryWeAreClosing") from _call_TownNightSorryWeAreClosing_PlayEvent
        return (1, "", "TownNightSorryWeAreClosing")
    return None

label TownNightEhhhYouuuuuuuuu_0:
    call Movement("TownNightEV102_0", "TownNightEV094", [["JUMP",0,0]]) from _call_TownNightEV102_0_Movement
    $ resolve_scene()
    "ehhh youuuuuuuuu"
    call Movement("TownNightEV102_0", "player", ["TURN_L"]) from _call_TownNightEV102_0_Movement_1
    $ resolve_scene()
    Johan "Hm? are you talking to us?"
    YoungVillager "You are new around here right? if you have nothing to do you can have a drink with us"
    Johan "(They seem quite nice ...) Okey, why not?"
    YoungVillager "Great! but we have a problem, the shop owner is my Grandma and she doesn't want to sell us any alcohol..."
    "... But since he doesn't know you, you could stop by and grab a couple of bottles for us..."
    "... As it just closed, you will have to go in the morning ... We better meet you here tomorrow night"
    Johan "Ok, if we have some free time we'll stop by the store"
    YoungVillager "Great! Thanks!!!"
    $ bottle_event = 1
    return False

label TownNightEhhhYouuuuuuuuu_2(menu_choice = None):
    YoungVillager "Good night guys"
    Johan "We got the bottles! Your grandmother almost catches us"
    call PlaySound("sound", "audio/Recovery.ogg", volume=0.9, no_loop=True) from _call_TownNightEV102_2_PlaySound
    $ set_item("liqueur", False)
    YoungVillager "Thanks a lot guys!!! You saved the night"
    YoungVillager "Why don't you do the honours and start the bottle?"
    $ resolve_scene()
    call PauseForBalloon("TownNightEV102_2") from _call_TownNightEV102_2_PauseForBalloon
    Johan "Hahahaha thank you, let's get started"
    $ show_picture(1, "adolescentes1")
    $ resolve_scene()
    Johan "Wow this liquor is quite strong"
    YoungVillager "Hahahaha I know, in this town we make liquors quite strong"
    Leyna "So you have already tried it, huh?"
    YoungVillager "Mmm yes.. from time to time I take a little from my father, but it's not enough for all of us"
    YoungVillager "Hey, I don't know your names yet"
    Johan "Oh sure, I'm Johan and this is my wife Leyna"
    YoungVillager "A pleasure guys! Hey Leyna, don't you want to drink a couple of shots?"
    Leyna "Oh ... I don't know if I should ..."
    Johan "(Leyna feels bad about alcohol ... but a little shouldn't hurt)"
    YoungVillager "Came on! It's not a proper party if we don't all drink"
    Johan "He's right, come on Leyna, a little doesn't hurt"
    Leyna "If that's okay with you then ... why not?"
    YoungVillager "Great!"
    $ show_picture(2, "adolescentes2")
    $ resolve_scene()
    Johan "(Wow that's a pretty big drink)"
    YoungVillager "(Cool she's not playing, she almost drinks half a bottle in one go)"
    $ show_picture(3, "adolescentes3")
    $ resolve_scene()
    Leyna "Wow! It's strong but it's very good"
    YoungVillager2 "So tell me, are you here on vacation?"
    Leyna "Yes, we've come to do a report of the festival for a tourism magazine, we are from the capital"
    YoungVillager2 "Great, the capital! I've always wanted to go but my father makes me work every day in the fields and I don't have time for anything"
    YoungVillager "Yes, it must be great to live in the capital, surely there are many beautiful girls like you there"
    $ show_picture(4, "adolescentes4")
    $ resolve_scene()
    Leyna "Pretty girls? Hahaha thanks"
    YoungVillager "Here there are almost none and those who live here are already married or their parents have them out of our reach"
    Johan "Hahahahha a classic, Leyna's father was also very protective of her"
    YoungVillager2 "Ahh so in the capital they are also like that.. there is no hope guys! let's drink more"
    Johan "Hahahah perfect, but I have to control myself, that liquor is very strong and it is already going to my head!"
    YoungVillager "Well ... that's the idea isn't it? hahaha"
    Johan "You're right (although Leyna worries me, you can see in her face that she's quite drunk)"
    YoungVillager2 "Ahh !! Man, we're going to die without seeing a naked woman"
    Johan "Come on come on, it's not so bad, you will surely find your ideal woman and meanwhile you have internet to entertain you"
    YoungVillager "Internet? There is no connection here except in the town hall and there it's impossible to see anything"
    Johan "(Wow, teenagers without internet or girls ... poor guys I can't imagine how bad it would have been for me)"
    Johan "Come on guys don't get depressed, for sure it will be solved!"
    YoungVillager2 "It's easy for you to say, you are with a beautiful woman. Sure you do it every day!"
    Johan "(I wish I were...) Hahaha well it's not that simple.."
    YoungVillager "Right, if I had a wife like Leyna I would be fucking everyday day without stopping"
    $ show_picture(5, "adolescentes5")
    $ resolve_scene()
    Leyna "Hahaha what an impressive youth"
    YoungVillager2 "And.. this.. since you see them every day.. How are they?"
    Johan "... the boobs?"
    YoungVillager "Yes yes!"
    Johan "Well they are ... very pretty?"
    YoungVillager2 "Ahh very pretty and we will die without seeing some"
    YoungVillager "Hey ... couldn't you show us something Leyna? Just a a little to know how they are"
    Leyna "Ah?!"
    YoungVillager "Come on it will be only a second! You're beautiful! Just a little bit and we won't talk about it again"
    Johan "Wow, slow down!"
    YoungVillager "Oh! Of course if you give us permission Johan, let's go, we don't have internet and we are crazy to know a little"
    YoungVillager2 "Yes! And what if one day I do it with a woman and I haven't seen anything before? I will stay like a stone. How embarrassing.."
    Johan "Guys..."
    YoungVillager "Please it will only be a second"
    Johan "eh..."
    Leyna "If it's only for a second ..."
    Johan "Leyna?"
    Leyna "They're just kids, they're harmless! They give me a little pity"
    Johan "...(Leyna is clearly drunk ... well and I am too ... just a second? The truth is they also give me some pity ..)"
    Johan "(If she shows them something they will leave us alone with the subject ...)"
    call GetChoice([_("Yes"), _("No")], value=menu_choice, called_from="TownNightEV102_2") from _call_TownNightEV102_2_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Yes"):
        $ menu_choice = None
        $ resolve_scene()
        Johan "Okay guys, but just a second and that's it!"
        YoungVillager "REALLY?! Great, thank you very much!"
        YoungVillager2 "Incredible I can't believe it, thank you very much!"
        Leyna "Okay, just a little look and that's it"
        $ show_picture(6, "adolescentes6")
        $ resolve_scene()
        Leyna "Here they are!"
        YoungVillager "Wow!! Amazing!"
        YoungVillager2 "Great, I'm going to jerk off tonight, thank you very much!"
        Johan "Hey you don't have to tell us that"
        YoungVillager "Hey can I ... can I touch them?"
        Leyna "Ehm..."
        Johan "No way! Without touching, this has been enough!"
        YoungVillager "Sorry..."
        pause
        $ fade_out()
        $ erase_picture(6)
        $ erase_picture(5)
        $ erase_picture(4)
        $ fade_in()
        $ resolve_scene()
        "...A FEW DRINKS OF LIQUOR LATER..."
        Leyna "Well ... I think it's about time we go"
        YoungVillager2 "Oooh! Now that we were having a good time?"
        Johan "Relax, we'll see you around here"
        YoungVillager "I take your word, if you want to have a good time one day you know where we are"
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ bottle_event = 3
        call GalleryViewed("adolescentes") from _call_TownNightEV102_2_GalleryViewed
    elif menu_choice == _("No"):
        $ menu_choice = None
        $ resolve_scene()
        Johan "You're drunk, you don't know what you're saying"
        Johan "You're definitely not going to show your tits to these kids, sorry guys."
        Johan "We were having a good time but we should go"
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(4)
        $ erase_picture(5)
        $ erase_picture(6)
        $ bottle_event = 4
    $ resolve_scene()
    return False

label TownNightEhhhYouuuuuuuuu(play_event = True, trigger = None): # event
    if is_erased("TownNightEhhhYouuuuuuuuu"):
        return None
    elif bottle_event >= 4:
        return None
    elif bottle_event >= 3:
        return None
    elif trigger == "event" and bottle_event >= 2:
        call PlayEvent(play_event, "TownNightEhhhYouuuuuuuuu_2", "TownNightEhhhYouuuuuuuuu") from _call_TownNightEhhhYouuuuuuuuu_2_PlayEvent
        return (0, "", "TownNightEhhhYouuuuuuuuu_2")
    elif bottle_event >= 1:
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNightEhhhYouuuuuuuuu_0", "TownNightEhhhYouuuuuuuuu") from _call_TownNightEhhhYouuuuuuuuu_0_PlayEvent
        return (0, "", "TownNightEhhhYouuuuuuuuu_0")
    return None

