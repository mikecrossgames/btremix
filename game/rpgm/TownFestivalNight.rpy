label TownFestivalNightBG:
    $ set_transparency_backgrounds(["bg_town_south_night"])
    $ set_map_backgrounds(["map_town_south_night"])
    return

label TownFestivalNightStart:
    call TownFestivalNightBG from _call_TownFestivalNightBG
    stop music
    stop bgs
    return

label TownFestivalNightEnd:
    return

label TownFestivalNightBoarInnBase:
    "Boar Inn"
    return False

label TownFestivalNightBoarInn(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightBoarInn"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightBoarInnBase", "TownFestivalNightBoarInn") from _call_TownFestivalNightBoarInn_PlayEvent
        return (1, "", "TownFestivalNightBoarInn")
    return None

label TownFestivalNightToInnNightBase:
    call PlaySound("sound", "audio/Open1.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV003_PlaySound
    call Movement("TownFestivalNightEV003", "TownFestivalNightEV003", ["TURN_L",["WAIT",3],"TURN_R",["WAIT",3],"TURN_U","THROUGH_ON"]) from _call_TownFestivalNightEV003_Movement
    call Movement("TownFestivalNightEV003", "player", ["FORWARD"]) from _call_TownFestivalNightEV003_Movement_1
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV003_PlaySound_1
    call TransferPlayer("InnNight", "TownFestivalNightEV003", 8, 12, direction=0) from _call_TownFestivalNightEV003_TransferPlayer
    $ resolve_scene()
    return False

label TownFestivalNightToInnNight(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightToInnNight"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightToInnNightBase", "TownFestivalNightToInnNight") from _call_TownFestivalNightToInnNight_PlayEvent
        return (1, "", "TownFestivalNightToInnNight")
    return None

label TownFestivalNightStoreClosedBase:
    "(Closed)"
    return False

label TownFestivalNightStoreClosed(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightStoreClosed"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightStoreClosedBase", "TownFestivalNightStoreClosed") from _call_TownFestivalNightStoreClosed_PlayEvent
        return (1, "", "TownFestivalNightStoreClosed")
    return None

label TownFestivalNightClosed_v2Base:
    "(Closed)"
    return False

label TownFestivalNightClosed_v2(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightClosed_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightClosed_v2Base", "TownFestivalNightClosed_v2") from _call_TownFestivalNightClosed_v2_PlayEvent
        return (1, "", "TownFestivalNightClosed_v2")
    return None

label TownFestivalNightimpedimentoBase:
    Johan "We still have things to do!"
    call Movement("TownFestivalNightimpedimento", "player", ["D","D"]) from _call_TownFestivalNightimpedimento_Movement
    $ resolve_scene()
    return False

label TownFestivalNightimpedimento(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightimpedimento"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightimpedimentoBase", "TownFestivalNightimpedimento") from _call_TownFestivalNightimpedimento_PlayEvent
        return (0, "", "TownFestivalNightimpedimento")
    return None

label TownFestivalNightMapBase:
    "River -> Festival <- Hot springs <- Coal mine <-"
    return False

label TownFestivalNightMap(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightMap"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightMapBase", "TownFestivalNightMap") from _call_TownFestivalNightMap_PlayEvent
        return (1, "", "TownFestivalNightMap")
    return None

label TownFestivalNightClosed_v3Base:
    "(Closed)"
    return False

label TownFestivalNightClosed_v3(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightClosed_v3"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightClosed_v3Base", "TownFestivalNightClosed_v3") from _call_TownFestivalNightClosed_v3_PlayEvent
        return (1, "", "TownFestivalNightClosed_v3")
    return None

label TownFestivalNightClosed_v4Base:
    "(Closed)"
    return False

label TownFestivalNightClosed_v4(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightClosed_v4"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightClosed_v4Base", "TownFestivalNightClosed_v4") from _call_TownFestivalNightClosed_v4_PlayEvent
        return (1, "", "TownFestivalNightClosed_v4")
    return None

label TownFestivalNightClosed_v5Base:
    "(Closed)"
    return False

label TownFestivalNightClosed_v5(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightClosed_v5"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightClosed_v5Base", "TownFestivalNightClosed_v5") from _call_TownFestivalNightClosed_v5_PlayEvent
        return (1, "", "TownFestivalNightClosed_v5")
    return None

label TownFestivalNightSeemsItsClosedBase:
    "Seems it's closed"
    return False

label TownFestivalNightSeemsItsClosed(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightSeemsItsClosed"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightSeemsItsClosedBase", "TownFestivalNightSeemsItsClosed") from _call_TownFestivalNightSeemsItsClosed_PlayEvent
        return (1, "", "TownFestivalNightSeemsItsClosed")
    return None

label TownFestivalNightCastlePosterBase:
    "Closed for restoration."
    return False

label TownFestivalNightCastlePoster(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightCastlePoster"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightCastlePosterBase", "TownFestivalNightCastlePoster") from _call_TownFestivalNightCastlePoster_PlayEvent
        return (1, "", "TownFestivalNightCastlePoster")
    return None

label TownFestivalNightCastlePoster_v2Base:
    "Closed for restoration."
    return False

label TownFestivalNightCastlePoster_v2(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightCastlePoster_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightCastlePoster_v2Base", "TownFestivalNightCastlePoster_v2") from _call_TownFestivalNightCastlePoster_v2_PlayEvent
        return (1, "", "TownFestivalNightCastlePoster_v2")
    return None

label TownFestivalNightPoliceAsleepBase:
    "(They must be resting..)"
    return False

label TownFestivalNightPoliceAsleep(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightPoliceAsleep"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightPoliceAsleepBase", "TownFestivalNightPoliceAsleep") from _call_TownFestivalNightPoliceAsleep_PlayEvent
        return (0, "", "TownFestivalNightPoliceAsleep")
    return None

label TownFestivalNightTheyMustBeResting_v2Base:
    "(They must be resting..)"
    return False

label TownFestivalNightTheyMustBeResting_v2(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightTheyMustBeResting_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightTheyMustBeResting_v2Base", "TownFestivalNightTheyMustBeResting_v2") from _call_TownFestivalNightTheyMustBeResting_v2_PlayEvent
        return (0, "", "TownFestivalNightTheyMustBeResting_v2")
    return None

label TownFestivalNightTheyMustBeResting_v3Base:
    "(They must be resting..)"
    return False

label TownFestivalNightTheyMustBeResting_v3(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightTheyMustBeResting_v3"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightTheyMustBeResting_v3Base", "TownFestivalNightTheyMustBeResting_v3") from _call_TownFestivalNightTheyMustBeResting_v3_PlayEvent
        return (0, "", "TownFestivalNightTheyMustBeResting_v3")
    return None

label TownFestivalNightmusicapuebloBase:
    call PlaySound("music", "audio/Ship1.ogg", volume=0.6, no_loop=False) from _call_TownFestivalNightmusicapueblo_PlaySound
    $ resolve_scene()
    $ tint_screen((-68, -68, 0, 68), 60, True)
    return False

label TownFestivalNightmusicapueblo(play_event = True, trigger = None): # parallel
    if is_erased("TownFestivalNightmusicapueblo"):
        return None
    elif trigger == "parallel":
        call PlayEvent(play_event, "TownFestivalNightmusicapuebloBase", "TownFestivalNightmusicapueblo") from _call_TownFestivalNightmusicapueblo_PlayEvent
        return (0, "", "TownFestivalNightmusicapueblo")
    return None

label TownFestivalNightPolicePosterBase:
    "Police station of Goddess cliff. to serve and protect."
    return False

label TownFestivalNightPolicePoster(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightPolicePoster"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightPolicePosterBase", "TownFestivalNightPolicePoster") from _call_TownFestivalNightPolicePoster_PlayEvent
        return (1, "", "TownFestivalNightPolicePoster")
    return None

label TownFestivalNightDataCityPosterBase:
    "Upper town"
    return False

label TownFestivalNightDataCityPoster(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightDataCityPoster"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightDataCityPosterBase", "TownFestivalNightDataCityPoster") from _call_TownFestivalNightDataCityPoster_PlayEvent
        return (1, "", "TownFestivalNightDataCityPoster")
    return None

label TownFestivalNightPillarBase:
    "Goddess Cliff: where dreams are lived day by day."
    return False

label TownFestivalNightPillar(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightPillar"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightPillarBase", "TownFestivalNightPillar") from _call_TownFestivalNightPillar_PlayEvent
        return (1, "", "TownFestivalNightPillar")
    return None

label TownFestivalNightClothingSignBase:
    "Happy pig Clothes and accessories"
    return False

label TownFestivalNightClothingSign(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightClothingSign"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightClothingSignBase", "TownFestivalNightClothingSign") from _call_TownFestivalNightClothingSign_PlayEvent
        return (1, "", "TownFestivalNightClothingSign")
    return None

label TownFestivalNightStoreSignBase:
    "General goods."
    return False

label TownFestivalNightStoreSign(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightStoreSign"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightStoreSignBase", "TownFestivalNightStoreSign") from _call_TownFestivalNightStoreSign_PlayEvent
        return (1, "", "TownFestivalNightStoreSign")
    return None

label TownFestivalNightCorruptionCounterBase:
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

label TownFestivalNightCorruptionCounter(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightCorruptionCounter"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightCorruptionCounterBase", "TownFestivalNightCorruptionCounter") from _call_TownFestivalNightCorruptionCounter_PlayEvent
        return (1, "", "TownFestivalNightCorruptionCounter")
    return None

label TownFestivalNightGraveBase:
    "Here lies Geralt of Rivia, the mercenary knight"
    return False

label TownFestivalNightGrave(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightGrave"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightGraveBase", "TownFestivalNightGrave") from _call_TownFestivalNightGrave_PlayEvent
        return (1, "", "TownFestivalNightGrave")
    return None

label TownFestivalNightNPCWhatALovelyNightBase:
    OldWoman "What a lovely night"
    Villager "Yes it is"
    return False

label TownFestivalNightNPCWhatALovelyNight(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightNPCWhatALovelyNight"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightNPCWhatALovelyNightBase", "TownFestivalNightNPCWhatALovelyNight") from _call_TownFestivalNightNPCWhatALovelyNight_PlayEvent
        return (1, "", "TownFestivalNightNPCWhatALovelyNight")
    return None

label TownFestivalNightWhatALovelyNight_v2Base:
    OldWoman "What a lovely night"
    Villager "Yes it is"
    return False

label TownFestivalNightWhatALovelyNight_v2(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightWhatALovelyNight_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightWhatALovelyNight_v2Base", "TownFestivalNightWhatALovelyNight_v2") from _call_TownFestivalNightWhatALovelyNight_v2_PlayEvent
        return (1, "", "TownFestivalNightWhatALovelyNight_v2")
    return None

label TownFestivalNightOooohThisBeerIsGreatHeheheheBase:
    Villager "Ooooh this beer is great hehehehe"
    return False

label TownFestivalNightOooohThisBeerIsGreatHehehehe(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightOooohThisBeerIsGreatHehehehe"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightOooohThisBeerIsGreatHeheheheBase", "TownFestivalNightOooohThisBeerIsGreatHehehehe") from _call_TownFestivalNightOooohThisBeerIsGreatHehehehe_PlayEvent
        return (1, "", "TownFestivalNightOooohThisBeerIsGreatHehehehe")
    return None

label TownFestivalNightGoodNightCoupleBase:
    OldMan "Good night couple!"
    return False

label TownFestivalNightGoodNightCouple(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightGoodNightCouple"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightGoodNightCoupleBase", "TownFestivalNightGoodNightCouple") from _call_TownFestivalNightGoodNightCouple_PlayEvent
        return (1, "", "TownFestivalNightGoodNightCouple")
    return None

label TownFestivalNightTheFoodIsGoodButTheWineCouldBeBetterBase:
    Villager "The food is good but the wine could be better"
    return False

label TownFestivalNightTheFoodIsGoodButTheWineCouldBeBetter(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightTheFoodIsGoodButTheWineCouldBeBetter"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightTheFoodIsGoodButTheWineCouldBeBetterBase", "TownFestivalNightTheFoodIsGoodButTheWineCouldBeBetter") from _call_TownFestivalNightTheFoodIsGoodButTheWineCouldBeBetter_PlayEvent
        return (1, "", "TownFestivalNightTheFoodIsGoodButTheWineCouldBeBetter")
    return None

label TownFestivalNightThisFoodIsAmazingYouHaveToTryThisBase:
    Villager "This food is amazing! You have to try this"
    return False

label TownFestivalNightThisFoodIsAmazingYouHaveToTryThis(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightThisFoodIsAmazingYouHaveToTryThis"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightThisFoodIsAmazingYouHaveToTryThisBase", "TownFestivalNightThisFoodIsAmazingYouHaveToTryThis") from _call_TownFestivalNightThisFoodIsAmazingYouHaveToTryThis_PlayEvent
        return (1, "", "TownFestivalNightThisFoodIsAmazingYouHaveToTryThis")
    return None

label TownFestivalNightGodBlessThisFestivitieHeheheBase:
    Villager "God bless this festivitie hehehe"
    return False

label TownFestivalNightGodBlessThisFestivitieHehehe(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightGodBlessThisFestivitieHehehe"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightGodBlessThisFestivitieHeheheBase", "TownFestivalNightGodBlessThisFestivitieHehehe") from _call_TownFestivalNightGodBlessThisFestivitieHehehe_PlayEvent
        return (1, "", "TownFestivalNightGodBlessThisFestivitieHehehe")
    return None

label TownFestivalNightHeyLeaveMeAlonePleaseBase:
    Villager "Hey leave me alone please"
    return False

label TownFestivalNightHeyLeaveMeAlonePlease(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightHeyLeaveMeAlonePlease"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightHeyLeaveMeAlonePleaseBase", "TownFestivalNightHeyLeaveMeAlonePlease") from _call_TownFestivalNightHeyLeaveMeAlonePlease_PlayEvent
        return (1, "", "TownFestivalNightHeyLeaveMeAlonePlease")
    return None

label TownFestivalNightIOverdidItWithTheLiquorMyWifeIsGoingToKillMeBase:
    OldVillager "I overdid it with the liquor... my wife is going to kill me"
    return False

label TownFestivalNightIOverdidItWithTheLiquorMyWifeIsGoingToKillMe(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightIOverdidItWithTheLiquorMyWifeIsGoingToKillMe"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightIOverdidItWithTheLiquorMyWifeIsGoingToKillMeBase", "TownFestivalNightIOverdidItWithTheLiquorMyWifeIsGoingToKillMe") from _call_TownFestivalNightIOverdidItWithTheLiquorMyWifeIsGoingToKillMe_PlayEvent
        return (1, "", "TownFestivalNightIOverdidItWithTheLiquorMyWifeIsGoingToKillMe")
    return None

label TownFestivalNightWhereTheHellHaveMyFriendsGoneBase:
    Tourist "Where the hell have my friends gone?"
    return False

label TownFestivalNightWhereTheHellHaveMyFriendsGone(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightWhereTheHellHaveMyFriendsGone"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightWhereTheHellHaveMyFriendsGoneBase", "TownFestivalNightWhereTheHellHaveMyFriendsGone") from _call_TownFestivalNightWhereTheHellHaveMyFriendsGone_PlayEvent
        return (1, "", "TownFestivalNightWhereTheHellHaveMyFriendsGone")
    return None

label TownFestivalNightShhhhImMeetingAVeryCuteTouristBase:
    YoungVillager "Shhhh I'm meeting a very cute tourist"
    return False

label TownFestivalNightShhhhImMeetingAVeryCuteTourist(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightShhhhImMeetingAVeryCuteTourist"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightShhhhImMeetingAVeryCuteTouristBase", "TownFestivalNightShhhhImMeetingAVeryCuteTourist") from _call_TownFestivalNightShhhhImMeetingAVeryCuteTourist_PlayEvent
        return (1, "", "TownFestivalNightShhhhImMeetingAVeryCuteTourist")
    return None

label TownFestivalNightUgghghhhBase:
    Villager ".... ugghghhh"
    return False

label TownFestivalNightUgghghhh(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightUgghghhh"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightUgghghhhBase", "TownFestivalNightUgghghhh") from _call_TownFestivalNightUgghghhh_PlayEvent
        return (1, "", "TownFestivalNightUgghghhh")
    return None

label TownFestivalNightPartyyyyBase:
    Villager "PaRtyyYY"
    return False

label TownFestivalNightPartyyyy(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightPartyyyy"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightPartyyyyBase", "TownFestivalNightPartyyyy") from _call_TownFestivalNightPartyyyy_PlayEvent
        return (1, "", "TownFestivalNightPartyyyy")
    return None

label TownFestivalNightMinesBiggerBase:
    NakedVillager "Mine's bigger!"
    return False

label TownFestivalNightMinesBigger(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightMinesBigger"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightMinesBiggerBase", "TownFestivalNightMinesBigger") from _call_TownFestivalNightMinesBigger_PlayEvent
        return (1, "", "TownFestivalNightMinesBigger")
    return None

label TownFestivalNightNoMinesWaaaayBiggerPalBase:
    NakedVillager "NO! Mine's waaaay bigger pal!"
    Johan "What the fuck?"
    return False

label TownFestivalNightNoMinesWaaaayBiggerPal(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightNoMinesWaaaayBiggerPal"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightNoMinesWaaaayBiggerPalBase", "TownFestivalNightNoMinesWaaaayBiggerPal") from _call_TownFestivalNightNoMinesWaaaayBiggerPal_PlayEvent
        return (1, "", "TownFestivalNightNoMinesWaaaayBiggerPal")
    return None

label TownFestivalNighteventoblackmail_0:
    call Movement("TownFestivalNighteventoblackmail_0", "TownFestivalNightadolescente2", [["JUMP",0,0]]) from _call_TownFestivalNighteventoblackmail_0_Movement
    $ show_picture(1, "blackmail1")
    $ resolve_scene()
    "ehhh youuuuuuuuu"
    Johan "Hm? are you talking to us?"
    YoungVillager "You are new around here right? She is the lucky person this year, and the one of the adulhood festivities"
    YoungVillager "Do you want to have some beers with us?"
    $ show_picture(2, "blackmail2")
    $ resolve_scene()
    Johan "Yeah.. (They seem quite nice ...) Okey, why not? We are Johan and Leyna"
    Leyna "(Fuck, those kids are the ones of festivity..)"
    YoungVillager "Great! But we have a problem, we ran out of beers"
    YoungVillager2 "But I have a bottle left at home. Hey, will you come with me? So you can carry the bottle around town without me getting caught"
    YoungVillager2 "Because you are an adult.."
    Johan "Oh, sure, no problem"
    Leyna "Great, I'm coming too"
    Johan "Don’t worry, wait for me here and relax a bit at the bonfire"
    Leyna "Oh... sure..."
    $ fade_out()
    $ erase_picture(1)
    $ erase_picture(2)
    call ChangePartyMember("Johan", False) from _call_TownFestivalNighteventoblackmail_0_ChangePartyMember
    call SetEventLocation("TownFestivalNighteventoblackmail_0", "TownFestivalNightadolescente3", 7, 20) from _call_TownFestivalNighteventoblackmail_0_setloc
    call TransferPlayer("TownFestivalNight", "TownFestivalNighteventoblackmail_0", 18, 37, direction=4) from _call_TownFestivalNighteventoblackmail_0_TransferPlayer
    $ fade_in()
    if switch("corruption_average"):
        $ resolve_scene()
        YoungVillager "Wow Leyna, I have to say that today you look even more beautiful than usual, if that's possible"
        $ resolve_scene()
        call PauseForBalloon("TownFestivalNighteventoblackmail_0") from _call_TownFestivalNighteventoblackmail_0_PauseForBalloon
        Leyna "Thank you (What does he want?...)"
        $ show_picture(1, "blackmail3")
        $ resolve_scene()
        YoungVillager "So... what do you think about our festival?"
        Leyna "Mmmm... well, I guess"
        YoungVillager "Ah... great yeah... hey, look at this cool picture"
        Leyna "Well, let's see..!!!!!!!!!!! Th-this is.. H-how?"
        $ show_picture(2, "blackmail4")
        $ resolve_scene()
        Leyna "WHATTT?!!"
        Leyna "How... where did you get that picture?"
        YoungVillager "I took it... yes, we caught you in the act, you don't want your husband to see this picture, do you?"
        Leyna "What? Of course not!"
        YoungVillager "Well if you don't want that to happen, you will listen to us"
        $ show_picture(3, "blackmail5")
        $ resolve_scene()
        Leyna "I... what do you want? I don't have much money..."
        YoungVillager "We don't want money, you see, we can't let our friend go around bragging to us about getting a blowjob from a beauty like you"
        YoungVillager "And we're just sitting here... so you know, we want you to do the same to us as you did to him"
        $ show_picture(4, "blackmail6")
        $ resolve_scene()
        Leyna "HOW? you have so little shame, how dare you? I refuse!"
        YoungVillager "Well, then I guess you don't mind so much... now when your husband gets back I'll show him the picture if you don't mind.."
        $ show_picture(5, "blackmail7")
        $ resolve_scene()
        Leyna "WAIT! wait... okay... okay damn it..."
        YoungVillager "Great, let's go to the alley"
        Leyna "Wait, right now?  But..."
        YoungVillager "Exactly, right now. And we have to hurry, they'll be right back. You don't want them to catch us in the act, do you?"
        Leyna "(Fucking son of a bitch).... of course"
        YoungVillager "Great, let's get it over with"
        $ show_picture(6, "blackmail8")
        $ resolve_scene()
        YoungVillager "Well, here we are"
        YoungVillager "Here you go, free buffet ahahaha"
        Leyna "Shut up... (fuck...)"
        $ show_picture(7, "blackmail9")
        $ resolve_scene()
        Leyna "(I can't believe I'm going to do this again in public)"
        YoungVillager "What are you waiting for? You don't want us to get caught, do you?"
        Leyna "I... okay"
        $ show_picture(8, "blackmail10")
        $ resolve_scene()
        Leyna "(My god, I don't think I can even fit in my mouth...I have to get this over with fast or it could go terribly wrong)"
        YoungVillager "Come on, don't make me wait any longer, I'm feeling your breath on my cock, don't worry, I'm sure we'll cum in no time"
        $ show_picture(9, "blackmail11")
        $ resolve_scene()
        YoungVillager "OOoooh! That feels so good, it's so warm in there. Keep it up"
        Leyna "(shut up, don't keep talking please..... why is my body behaving this way? i'm getting horny doing this)"
        YoungVillager "Hey! Don't forget about me, come on, suck my dick"
        Leyna "O..okay.."
        $ show_picture(10, "blackmail12")
        $ resolve_scene()
        YoungVillager3 "Uoh great, this is the best!"
        Leyna "(Doing this to two guys at the same time on the street...I've never done anything like this... but it feels so good..)"
        Leyna "(.. but, what am I saying? I'm not like this)"
        call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNighteventoblackmail_0_PlaySound
        $ show_picture(11, "blackmail13")
        $ resolve_scene()
        Leyna "What are you doing?!"
        YoungVillager "You don't need this hahahaha besides, if I don't see something while you're blowing my friend, we'll never finish"
        YoungVillager3 "Good idea! since the last time you showed them to us,I have not been able to get them out of my head"
        Leyna "I..."
        $ show_picture(12, "blackmail14")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_TownFestivalNighteventoblackmail_0_PlaySound_1
        $ resolve_scene()
        YoungVillager3 "Who told you to stop sucking my dick? COME ON, GET IT OVER WITH"
        Leyna "Ugh!"
        YoungVillager "Wow! A deep throat! This girl has experience! She looks like a saint but she's a whore!"
        Leyna "(He's fucking my mouth! he's being too gross but... I haven't been this horny in a long time.. right now.."
        Leyna "..right now I just want to be fucked  for both of them)"
        YoungVillager3 "UOOo I'm coming!"
        YoungVillager "Yeah, me too!"
        stop bgs fadeout 1
        $ flash_screen([255,255,255,170], 60, True)
        $ show_picture(13, "blackmail15")
        call PlaySound("sound", "audio/Poison.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNighteventoblackmail_0_PlaySound_2
        $ resolve_scene()
        $ flash_screen([255,255,255,170], 60, True)
        Leyna "!!!"
        YoungVillager "That was... incredible! I could go on all night!"
        YoungVillager3 "Yeah! Too bad we didn't fuck her, but some other time!"
        Leyna "There won't be another time! bring me something to clean me up."
        $ fade_out()
        $ show_picture(14, "blackmail16")
        $ fade_in()
        $ resolve_scene()
        Johan "Here we are with the drink... ? Leyna? are you ok?"
        Leyna "Oh yes, I'm fine.. We were.."
        YoungVillager "W-we were looking for beers too, never too much hahaha, but we didn't find anything"
        Johan "(Leyna seems a little alarmed about something... it's just my imagination)"
        Leyna "..."
        Johan "Well, shall we drink a little, guys?"
        YoungVillager "Say no more! I'm very dry, I need a drink"
        Johan "Anyone would say you've done a marathon hahaha"
        YoungVillager "Yeah hahaha pretty much!"
        Leyna "..."
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
        call ChangePartyMember("Johan", True) from _call_TownFestivalNighteventoblackmail_0_ChangePartyMember_1
        call TransferPlayer("TownFestivalNight", "TownFestivalNighteventoblackmail_0", 18, 38, direction=4) from _call_TownFestivalNighteventoblackmail_0_TransferPlayer_1
        call Movement("TownFestivalNighteventoblackmail_0", "player", ["U","TURN_L"]) from _call_TownFestivalNighteventoblackmail_0_Movement_1
        $ fade_in()
        $ resolve_scene()
        YoungVillager2 "I must say that your wife looks beautiful today, Johan"
        Johan "Yes, I have the sexiest wife in the world, of course!"
        YoungVillager "Ahhhhhhhhhh how envious you make me"
        Johan "Come on, come on, don't worry, you'll get a good wife in due time"
        YoungVillager "I'm not so sure... but in the meantime, we can enjoy Leyna's company"
        Johan "Hey don't go overboard, you're talking about my wife hahaha"
        YoungVillager "Yes, sorry I don't mean to be rude. Well, let's enjoy the night, there is still a lot of partying left"
        YoungVillager2 "Well said!"
        $ fade_out()
        $ fade_in()
        $ resolve_scene()
        "(FEW MOMENTS LATER..)"
        Johan "Well guys, we're leaving now"
        YoungVillager "Sure! Have fun"
        $ blackmail = 1
        call GalleryViewed("blackmail") from _call_TownFestivalNighteventoblackmail_0_GalleryViewed
        call Movement("TownFestivalNighteventoblackmail_0", "player", ["R","R"]) from _call_TownFestivalNighteventoblackmail_0_Movement_2
    if switch("corruption_low"):
        $ show_picture(1, "blackmail3")
        $ resolve_scene()
        YoungVillager "If I may say so, Leyna, you look very sexy today"
        Leyna "Oh, thanks"
        if bottle_event == 3:
            $ resolve_scene()
            YoungVillager "No, thanks to you, I must have jerked off ten times thinking about when you showed us your tits the other night"
            Leyna "I don't think that needs to be said...."
            YoungVillager "Oh yeah, of course I guess you're right, sorry"
        $ fade_out()
        $ erase_picture(1)
        $ show_picture(1, "blackmail2")
        $ fade_in()
        $ resolve_scene()
        "(FEW MOMENTS LATER..)"
        Johan "Well, here we are!"
        YoungVillager "Great, so let's not waste any more time and let's get drinking"
        $ fade_out()
        $ erase_picture(1)
        $ fade_in()
        $ show_picture(1, "noblackmail1")
        $ resolve_scene()
        "AFTER A FEW BEERS.."
        YoungVillager "(Wow, leyna is so sexy! she has the perfect body..... damn, it sucks that she came with her husband on vacation!I could.... I'm sure I could"
        "... seduce her in some way.... I have to think about it, there has to be some way for me to lose my virginity with this goddess)"
        YoungVillager3 ".... and I saw his dick and he had it like a peanut hhahahahaaha"
        Leyna "Hahaahaha"
        YoungVillager "(Wait, is he talking about me?) hey asshole! We were 8 years old! Now I've got it so much bigger than you!"
        YoungVillager3 "In your dreams maybe! if you want we can compare right now"
        Johan "Hahahahaha hey come on guys no need...!!!!"
        $ show_picture(2, "noblackmail2")
        $ resolve_scene()
        Leyna "Wow!"
        YoungVillager "See, mine is bigger than yours!"
        YoungVillager3 "Well I see mine bigger! ... plus it's cold! Give me a second and you'll see how much bigger it is!"
        Johan "Come on guys! Stop showing off! There's a lady in front of you, this is no way to behave!"
        YoungVillager "Oh... you're right"
        $ show_picture(3, "noblackmail3")
        $ resolve_scene()
        YoungVillager3 "Right, Leyna is in front of us... we can ask her! Who has the biggest dick? Me, right?"
        Leyna "W-well! You both have it huge hehehe you don't have to worry so much"
        YoungVillager "OH? So we have it huge eh? Tthank you.... Bigger than Johan's?"
        Leyna "Well,then s..."
        Johan "Hey! You guys are going too far! (Shit, the alcohol is speaking for Leyna again) Keep that in your pants, come on"
        YoungVillager "Hmmm yeah sorry Johan! We stopped already"
        Leyna "...."
        $ fade_out()
        call ChangePartyMember("Johan", True) from _call_TownFestivalNighteventoblackmail_0_ChangePartyMember_2
        call TransferPlayer("TownFestivalNight", "TownFestivalNighteventoblackmail_0", 18, 38, direction=4) from _call_TownFestivalNighteventoblackmail_0_TransferPlayer_2
        call Movement("TownFestivalNighteventoblackmail_0", "player", ["U","TURN_L"]) from _call_TownFestivalNighteventoblackmail_0_Movement_3
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ fade_in()
        $ resolve_scene()
        Johan "Well guys, we're leaving now"
        YoungVillager "Sure! Have fun"
        $ blackmail = 2
        call GalleryViewed("noblackmail") from _call_TownFestivalNighteventoblackmail_0_GalleryViewed_1
        call Movement("TownFestivalNighteventoblackmail_0", "player", ["R","R"]) from _call_TownFestivalNighteventoblackmail_0_Movement_4
    $ resolve_scene()
    return False

label TownFestivalNighteventoblackmail_1:
    $ show_picture(1, "blackmail1")
    $ resolve_scene()
    YoungVillager "Hey! What's up guys? You going out tonight? Do you want to join us for a drink? We had a great time the other day"
    Johan "Sure, guys, we can stay for a while"
    Leyna "... (Shit, this is the last situation I wanted)"
    $ show_picture(2, "blackmail2")
    $ resolve_scene()
    YoungVillager2 "We've run out of liquor, but I have a bottle left at home. Johan, will you come with me? So you can carry the bottle around town without me getting caught"
    Johan "Oh, sure, no problem"
    Leyna "Great, I'm coming too"
    Johan "Don’t worry, wait for me here and relax a bit at the bonfire"
    Leyna "Oh... sure..."
    $ fade_out()
    $ erase_picture(1)
    $ erase_picture(2)
    call ChangePartyMember("Johan", False) from _call_TownFestivalNighteventoblackmail_1_ChangePartyMember
    call SetEventLocation("TownFestivalNighteventoblackmail_1", "TownFestivalNightadolescente3", 7, 20) from _call_TownFestivalNighteventoblackmail_1_setloc
    call TransferPlayer("TownFestivalNight", "TownFestivalNighteventoblackmail_1", 18, 37, direction=4) from _call_TownFestivalNighteventoblackmail_1_TransferPlayer
    $ fade_in()
    if switch("corruption_average"):
        $ resolve_scene()
        YoungVillager "Wow Leyna, I have to say that today you look even more beautiful than usual, if that's possible"
        $ resolve_scene()
        call PauseForBalloon("TownFestivalNighteventoblackmail_1") from _call_TownFestivalNighteventoblackmail_1_PauseForBalloon
        Leyna "Thank you (What does he want?...)"
        $ show_picture(1, "blackmail3")
        $ resolve_scene()
        YoungVillager "So... what do you think about our festival?"
        Leyna "Mmmm... well, I guess"
        YoungVillager "Ah... great yeah... hey, look at this cool picture"
        Leyna "Well, let's see..!!!!!!!!!!! Th-this is.. H-how?"
        $ show_picture(2, "blackmail4")
        $ resolve_scene()
        Leyna "WHATTT?!!"
        Leyna "How... where did you get that picture?"
        YoungVillager "I took it... yes, we caught you in the act, you don't want your husband to see this picture, do you?"
        Leyna "What? Of course not!"
        YoungVillager "Well if you don't want that to happen, you will listen to us"
        $ show_picture(3, "blackmail5")
        $ resolve_scene()
        Leyna "I... what do you want? I don't have much money..."
        YoungVillager "We don't want money, you see, we can't let our friend go around bragging to us about getting a blowjob from a beauty like you"
        YoungVillager "And we're just sitting here... so you know, we want you to do the same to us as you did to him"
        $ show_picture(4, "blackmail6")
        $ resolve_scene()
        Leyna "HOW? you have so little shame, how dare you? I refuse!"
        YoungVillager "Well, then I guess you don't mind so much... now when your husband gets back I'll show him the picture if you don't mind.."
        $ show_picture(5, "blackmail7")
        $ resolve_scene()
        Leyna "WAIT! wait... okay... okay damn it..."
        YoungVillager "Great, let's go to the alley"
        Leyna "Wait, right now?  But..."
        YoungVillager "Exactly, right now. And we have to hurry, they'll be right back. You don't want them to catch us in the act, do you?"
        Leyna "(Fucking son of a bitch).... of course"
        YoungVillager "Great, let's get it over with"
        $ show_picture(6, "blackmail8")
        $ resolve_scene()
        YoungVillager "Well, here we are"
        YoungVillager "Here you go, free buffet ahahaha"
        Leyna "Shut up... (fuck...)"
        $ show_picture(7, "blackmail9")
        $ resolve_scene()
        Leyna "(I can't believe I'm going to do this again in public)"
        YoungVillager "What are you waiting for? You don't want us to get caught, do you?"
        Leyna "I... okay"
        $ show_picture(8, "blackmail10")
        $ resolve_scene()
        Leyna "(My god, I don't think I can even fit in my mouth...I have to get this over with fast or it could go terribly wrong)"
        YoungVillager "Come on, don't make me wait any longer, I'm feeling your breath on my cock, don't worry, I'm sure we'll cum in no time"
        $ show_picture(9, "blackmail11")
        $ resolve_scene()
        YoungVillager "OOoooh! That feels so good, it's so warm in there. Keep it up"
        Leyna "(shut up, don't keep talking please..... why is my body behaving this way? i'm getting horny doing this)"
        YoungVillager "Hey! Don't forget about me, come on, suck my dick"
        Leyna "O..okay.."
        $ show_picture(10, "blackmail12")
        $ resolve_scene()
        YoungVillager3 "Uoh great, this is the best!"
        Leyna "(Doing this to two guys at the same time on the street...I've never done anything like this... but it feels so good..)"
        Leyna "(.. but, what am I saying? I'm not like this)"
        call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNighteventoblackmail_1_PlaySound
        $ show_picture(11, "blackmail13")
        $ resolve_scene()
        Leyna "What are you doing?!"
        YoungVillager "You don't need this hahahaha besides, if I don't see something while you're blowing my friend, we'll never finish"
        YoungVillager3 "Good idea! since the last time you showed them to us,I have not been able to get them out of my head"
        Leyna "I..."
        $ show_picture(12, "blackmail14")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_TownFestivalNighteventoblackmail_1_PlaySound_1
        $ resolve_scene()
        YoungVillager3 "Who told you to stop sucking my dick? COME ON, GET IT OVER WITH"
        Leyna "Ugh!"
        YoungVillager "Wow! A deep throat! This girl has experience! She looks like a saint but she's a whore!"
        Leyna "(He's fucking my mouth! he's being too gross but... I haven't been this horny in a long time.. right now.."
        Leyna "..right now I just want to be fucked  for both of them)"
        YoungVillager3 "UOOo I'm coming!"
        YoungVillager "Yeah, me too!"
        stop bgs fadeout 1
        $ flash_screen([255,255,255,170], 60, True)
        $ show_picture(13, "blackmail15")
        call PlaySound("sound", "audio/Poison.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNighteventoblackmail_1_PlaySound_2
        $ resolve_scene()
        $ flash_screen([255,255,255,170], 60, True)
        Leyna "!!!"
        YoungVillager "That was... incredible! I could go on all night!"
        YoungVillager3 "Yeah! Too bad we didn't fuck her, but some other time!"
        Leyna "There won't be another time! bring me something to clean me up."
        $ fade_out()
        $ show_picture(14, "blackmail16")
        $ fade_in()
        $ resolve_scene()
        Johan "Here we are with the drink... ? Leyna? are you ok?"
        Leyna "Oh yes, I'm fine.. We were.."
        YoungVillager "W-we were looking for beers too, never too much hahaha, but we didn't find anything"
        Johan "(Leyna seems a little alarmed about something... it's just my imagination)"
        Leyna "..."
        Johan "Well, shall we drink a little, guys?"
        YoungVillager "Say no more! I'm very dry, I need a drink"
        Johan "Anyone would say you've done a marathon hahaha"
        YoungVillager "Yeah hahaha pretty much!"
        Leyna "..."
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
        call ChangePartyMember("Johan", True) from _call_TownFestivalNighteventoblackmail_1_ChangePartyMember_1
        call TransferPlayer("TownFestivalNight", "TownFestivalNighteventoblackmail_1", 18, 38, direction=4) from _call_TownFestivalNighteventoblackmail_1_TransferPlayer_1
        call Movement("TownFestivalNighteventoblackmail_1", "player", ["U","TURN_L"]) from _call_TownFestivalNighteventoblackmail_1_Movement
        $ fade_in()
        $ resolve_scene()
        YoungVillager2 "I must say that your wife looks beautiful today, Johan"
        Johan "Yes, I have the sexiest wife in the world, of course!"
        YoungVillager "Ahhhhhhhhhh how envious you make me"
        Johan "Come on, come on, don't worry, you'll get a good wife in due time"
        YoungVillager "I'm not so sure... but in the meantime, we can enjoy Leyna's company"
        Johan "Hey don't go overboard, you're talking about my wife hahaha"
        YoungVillager "Yes, sorry I don't mean to be rude. Well, let's enjoy the night, there is still a lot of partying left"
        YoungVillager2 "Well said!"
        $ fade_out()
        $ fade_in()
        $ resolve_scene()
        "(FEW MOMENTS LATER..)"
        Johan "Well guys, we're leaving now"
        YoungVillager "Sure! Have fun"
        $ blackmail = 1
        call GalleryViewed("blackmail") from _call_TownFestivalNighteventoblackmail_1_GalleryViewed
        call Movement("TownFestivalNighteventoblackmail_1", "player", ["R","R"]) from _call_TownFestivalNighteventoblackmail_1_Movement_1
    if switch("corruption_low"):
        $ show_picture(1, "blackmail3")
        $ resolve_scene()
        YoungVillager "If I may say so, Leyna, you look very sexy today"
        Leyna "Oh, thanks"
        if bottle_event == 3:
            $ resolve_scene()
            YoungVillager "No, thanks to you, I must have jerked off ten times thinking about when you showed us your tits the other night"
            Leyna "I don't think that needs to be said...."
            YoungVillager "Oh yeah, of course I guess you're right, sorry"
        $ fade_out()
        $ erase_picture(1)
        $ show_picture(1, "blackmail2")
        $ fade_in()
        $ resolve_scene()
        "(FEW MOMENTS LATER..)"
        Johan "Well, here we are!"
        YoungVillager "Great, so let's not waste any more time and let's get drinking"
        $ fade_out()
        $ erase_picture(1)
        $ fade_in()
        $ show_picture(1, "noblackmail1")
        $ resolve_scene()
        "AFTER A FEW BEERS.."
        YoungVillager "(Wow, leyna is so sexy! she has the perfect body..... damn, it sucks that she came with her husband on vacation!I could.... I'm sure I could"
        "... seduce her in some way.... I have to think about it, there has to be some way for me to lose my virginity with this goddess)"
        YoungVillager3 ".... and I saw his dick and he had it like a peanut hhahahahaaha"
        Leyna "Hahaahaha"
        YoungVillager "(Wait, is he talking about me?) hey asshole! We were 8 years old! Now I've got it so much bigger than you!"
        YoungVillager3 "In your dreams maybe! if you want we can compare right now"
        Johan "Hahahahaha hey come on guys no need...!!!!"
        $ show_picture(2, "noblackmail2")
        $ resolve_scene()
        Leyna "Wow!"
        YoungVillager "See, mine is bigger than yours!"
        YoungVillager3 "Well I see mine bigger! ... plus it's cold! Give me a second and you'll see how much bigger it is!"
        Johan "Come on guys! Stop showing off! There's a lady in front of you, this is no way to behave!"
        YoungVillager "Oh... you're right"
        $ show_picture(3, "noblackmail3")
        $ resolve_scene()
        YoungVillager3 "Right, Leyna is in front of us... we can ask her! Who has the biggest dick? Me, right?"
        Leyna "W-well! You both have it huge hehehe you don't have to worry so much"
        YoungVillager "OH? So we have it huge eh? Tthank you.... Bigger than Johan's?"
        Leyna "Well,then s..."
        Johan "Hey! You guys are going too far! (Shit, the alcohol is speaking for Leyna again) Keep that in your pants, come on"
        YoungVillager "Hmmm yeah sorry Johan! We stopped already"
        Leyna "...."
        $ fade_out()
        call ChangePartyMember("Johan", True) from _call_TownFestivalNighteventoblackmail_1_ChangePartyMember_2
        call TransferPlayer("TownFestivalNight", "TownFestivalNighteventoblackmail_1", 18, 38, direction=4) from _call_TownFestivalNighteventoblackmail_1_TransferPlayer_2
        call Movement("TownFestivalNighteventoblackmail_1", "player", ["U","TURN_L"]) from _call_TownFestivalNighteventoblackmail_1_Movement_2
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ fade_in()
        $ resolve_scene()
        Johan "Well guys, we're leaving now"
        YoungVillager "Sure! Have fun"
        $ blackmail = 2
        call GalleryViewed("noblackmail") from _call_TownFestivalNighteventoblackmail_1_GalleryViewed_1
        call Movement("TownFestivalNighteventoblackmail_1", "player", ["R","R"]) from _call_TownFestivalNighteventoblackmail_1_Movement_3
    $ resolve_scene()
    return False

label TownFestivalNighteventoblackmail_2:
    $ show_picture(1, "blackmail1")
    $ resolve_scene()
    YoungVillager "Hey! What's up guys? You going out tonight? Do you want to join us for a drink? We had a great time the other day"
    Johan "Sure, guys, we can stay for a while"
    Leyna "... (Shit, this is the last situation I wanted)"
    $ show_picture(2, "blackmail2")
    $ resolve_scene()
    YoungVillager2 "We've run out of liquor, but I have a bottle left at home. Johan, will you come with me? So you can carry the bottle around town without me getting caught"
    Johan "Oh, sure, no problem"
    Leyna "Great, I'm coming too"
    Johan "Don’t worry, wait for me here and relax a bit at the bonfire"
    Leyna "Oh... sure..."
    $ fade_out()
    $ erase_picture(1)
    $ erase_picture(2)
    call ChangePartyMember("Johan", False) from _call_TownFestivalNighteventoblackmail_2_ChangePartyMember
    call SetEventLocation("TownFestivalNighteventoblackmail_2", "TownFestivalNightadolescente3", 7, 20) from _call_TownFestivalNighteventoblackmail_2_setloc
    call TransferPlayer("TownFestivalNight", "TownFestivalNighteventoblackmail_2", 18, 37, direction=4) from _call_TownFestivalNighteventoblackmail_2_TransferPlayer
    $ fade_in()
    if switch("corruption_average"):
        $ resolve_scene()
        YoungVillager "Wow Leyna, I have to say that today you look even more beautiful than usual, if that's possible"
        $ resolve_scene()
        call PauseForBalloon("TownFestivalNighteventoblackmail_2") from _call_TownFestivalNighteventoblackmail_2_PauseForBalloon
        Leyna "Thank you (What does he want?...)"
        $ show_picture(1, "blackmail3")
        $ resolve_scene()
        YoungVillager "So... what do you think about our festival?"
        Leyna "Mmmm... well, I guess"
        YoungVillager "Ah... great yeah... hey, look at this cool picture"
        Leyna "Well, let's see..!!!!!!!!!!! Th-this is.. H-how?"
        $ show_picture(2, "blackmail4")
        $ resolve_scene()
        Leyna "WHATTT?!!"
        Leyna "How... where did you get that picture?"
        YoungVillager "I took it... yes, we caught you in the act, you don't want your husband to see this picture, do you?"
        Leyna "What? Of course not!"
        YoungVillager "Well if you don't want that to happen, you will listen to us"
        $ show_picture(3, "blackmail5")
        $ resolve_scene()
        Leyna "I... what do you want? I don't have much money..."
        YoungVillager "We don't want money, you see, we can't let our friend go around bragging to us about getting a blowjob from a beauty like you"
        YoungVillager "And we're just sitting here... so you know, we want you to do the same to us as you did to him"
        $ show_picture(4, "blackmail6")
        $ resolve_scene()
        Leyna "HOW? you have so little shame, how dare you? I refuse!"
        YoungVillager "Well, then I guess you don't mind so much... now when your husband gets back I'll show him the picture if you don't mind.."
        $ show_picture(5, "blackmail7")
        $ resolve_scene()
        Leyna "WAIT! wait... okay... okay damn it..."
        YoungVillager "Great, let's go to the alley"
        Leyna "Wait, right now?  But..."
        YoungVillager "Exactly, right now. And we have to hurry, they'll be right back. You don't want them to catch us in the act, do you?"
        Leyna "(Fucking son of a bitch).... of course"
        YoungVillager "Great, let's get it over with"
        $ show_picture(6, "blackmail8")
        $ resolve_scene()
        YoungVillager "Well, here we are"
        YoungVillager "Here you go, free buffet ahahaha"
        Leyna "Shut up... (fuck...)"
        $ show_picture(7, "blackmail9")
        $ resolve_scene()
        Leyna "(I can't believe I'm going to do this again in public)"
        YoungVillager "What are you waiting for? You don't want us to get caught, do you?"
        Leyna "I... okay"
        $ show_picture(8, "blackmail10")
        $ resolve_scene()
        Leyna "(My god, I don't think I can even fit in my mouth...I have to get this over with fast or it could go terribly wrong)"
        YoungVillager "Come on, don't make me wait any longer, I'm feeling your breath on my cock, don't worry, I'm sure we'll cum in no time"
        $ show_picture(9, "blackmail11")
        $ resolve_scene()
        YoungVillager "OOoooh! That feels so good, it's so warm in there. Keep it up"
        Leyna "(shut up, don't keep talking please..... why is my body behaving this way? i'm getting horny doing this)"
        YoungVillager "Hey! Don't forget about me, come on, suck my dick"
        Leyna "O..okay.."
        $ show_picture(10, "blackmail12")
        $ resolve_scene()
        YoungVillager3 "Uoh great, this is the best!"
        Leyna "(Doing this to two guys at the same time on the street...I've never done anything like this... but it feels so good..)"
        Leyna "(.. but, what am I saying? I'm not like this)"
        call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNighteventoblackmail_2_PlaySound
        $ show_picture(11, "blackmail13")
        $ resolve_scene()
        Leyna "What are you doing?!"
        YoungVillager "You don't need this hahahaha besides, if I don't see something while you're blowing my friend, we'll never finish"
        YoungVillager3 "Good idea! since the last time you showed them to us,I have not been able to get them out of my head"
        Leyna "I..."
        $ show_picture(12, "blackmail14")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_TownFestivalNighteventoblackmail_2_PlaySound_1
        $ resolve_scene()
        YoungVillager3 "Who told you to stop sucking my dick? COME ON, GET IT OVER WITH"
        Leyna "Ugh!"
        YoungVillager "Wow! A deep throat! This girl has experience! She looks like a saint but she's a whore!"
        Leyna "(He's fucking my mouth! he's being too gross but... I haven't been this horny in a long time.. right now.."
        Leyna "..right now I just want to be fucked  for both of them)"
        YoungVillager3 "UOOo I'm coming!"
        YoungVillager "Yeah, me too!"
        stop bgs fadeout 1
        $ flash_screen([255,255,255,170], 60, True)
        $ show_picture(13, "blackmail15")
        call PlaySound("sound", "audio/Poison.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNighteventoblackmail_2_PlaySound_2
        $ resolve_scene()
        $ flash_screen([255,255,255,170], 60, True)
        Leyna "!!!"
        YoungVillager "That was... incredible! I could go on all night!"
        YoungVillager3 "Yeah! Too bad we didn't fuck her, but some other time!"
        Leyna "There won't be another time! bring me something to clean me up."
        $ fade_out()
        $ show_picture(14, "blackmail16")
        $ fade_in()
        $ resolve_scene()
        Johan "Here we are with the drink... ? Leyna? are you ok?"
        Leyna "Oh yes, I'm fine.. We were.."
        YoungVillager "W-we were looking for beers too, never too much hahaha, but we didn't find anything"
        Johan "(Leyna seems a little alarmed about something... it's just my imagination)"
        Leyna "..."
        Johan "Well, shall we drink a little, guys?"
        YoungVillager "Say no more! I'm very dry, I need a drink"
        Johan "Anyone would say you've done a marathon hahaha"
        YoungVillager "Yeah hahaha pretty much!"
        Leyna "..."
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
        call ChangePartyMember("Johan", True) from _call_TownFestivalNighteventoblackmail_2_ChangePartyMember_1
        call TransferPlayer("TownFestivalNight", "TownFestivalNighteventoblackmail_2", 18, 38, direction=4) from _call_TownFestivalNighteventoblackmail_2_TransferPlayer_1
        call Movement("TownFestivalNighteventoblackmail_2", "player", ["U","TURN_L"]) from _call_TownFestivalNighteventoblackmail_2_Movement
        $ fade_in()
        $ resolve_scene()
        YoungVillager2 "I must say that your wife looks beautiful today, Johan"
        Johan "Yes, I have the sexiest wife in the world, of course!"
        YoungVillager "Ahhhhhhhhhh how envious you make me"
        Johan "Come on, come on, don't worry, you'll get a good wife in due time"
        YoungVillager "I'm not so sure... but in the meantime, we can enjoy Leyna's company"
        Johan "Hey don't go overboard, you're talking about my wife hahaha"
        YoungVillager "Yes, sorry I don't mean to be rude. Well, let's enjoy the night, there is still a lot of partying left"
        YoungVillager2 "Well said!"
        $ fade_out()
        $ fade_in()
        $ resolve_scene()
        "(FEW MOMENTS LATER..)"
        Johan "Well guys, we're leaving now"
        YoungVillager "Sure! Have fun"
        $ blackmail = 1
        call GalleryViewed("blackmail") from _call_TownFestivalNighteventoblackmail_2_GalleryViewed
        call Movement("TownFestivalNighteventoblackmail_2", "player", ["R","R"]) from _call_TownFestivalNighteventoblackmail_2_Movement_1
    if switch("corruption_low"):
        $ show_picture(1, "blackmail3")
        $ resolve_scene()
        YoungVillager "If I may say so, Leyna, you look very sexy today"
        Leyna "Oh, thanks"
        if bottle_event == 3:
            $ resolve_scene()
            YoungVillager "No, thanks to you, I must have jerked off ten times thinking about when you showed us your tits the other night"
            Leyna "I don't think that needs to be said...."
            YoungVillager "Oh yeah, of course I guess you're right, sorry"
        $ fade_out()
        $ erase_picture(1)
        $ show_picture(1, "blackmail2")
        $ fade_in()
        $ resolve_scene()
        "(FEW MOMENTS LATER..)"
        Johan "Well, here we are!"
        YoungVillager "Great, so let's not waste any more time and let's get drinking"
        $ fade_out()
        $ erase_picture(1)
        $ fade_in()
        $ show_picture(1, "noblackmail1")
        $ resolve_scene()
        "AFTER A FEW BEERS.."
        YoungVillager "(Wow, leyna is so sexy! she has the perfect body..... damn, it sucks that she came with her husband on vacation!I could.... I'm sure I could"
        "... seduce her in some way.... I have to think about it, there has to be some way for me to lose my virginity with this goddess)"
        YoungVillager3 ".... and I saw his dick and he had it like a peanut hhahahahaaha"
        Leyna "Hahaahaha"
        YoungVillager "(Wait, is he talking about me?) hey asshole! We were 8 years old! Now I've got it so much bigger than you!"
        YoungVillager3 "In your dreams maybe! if you want we can compare right now"
        Johan "Hahahahaha hey come on guys no need...!!!!"
        $ show_picture(2, "noblackmail2")
        $ resolve_scene()
        Leyna "Wow!"
        YoungVillager "See, mine is bigger than yours!"
        YoungVillager3 "Well I see mine bigger! ... plus it's cold! Give me a second and you'll see how much bigger it is!"
        Johan "Come on guys! Stop showing off! There's a lady in front of you, this is no way to behave!"
        YoungVillager "Oh... you're right"
        $ show_picture(3, "noblackmail3")
        $ resolve_scene()
        YoungVillager3 "Right, Leyna is in front of us... we can ask her! Who has the biggest dick? Me, right?"
        Leyna "W-well! You both have it huge hehehe you don't have to worry so much"
        YoungVillager "OH? So we have it huge eh? Tthank you.... Bigger than Johan's?"
        Leyna "Well,then s..."
        Johan "Hey! You guys are going too far! (Shit, the alcohol is speaking for Leyna again) Keep that in your pants, come on"
        YoungVillager "Hmmm yeah sorry Johan! We stopped already"
        Leyna "...."
        $ fade_out()
        call ChangePartyMember("Johan", True) from _call_TownFestivalNighteventoblackmail_2_ChangePartyMember_2
        call TransferPlayer("TownFestivalNight", "TownFestivalNighteventoblackmail_2", 18, 38, direction=4) from _call_TownFestivalNighteventoblackmail_2_TransferPlayer_2
        call Movement("TownFestivalNighteventoblackmail_2", "player", ["U","TURN_L"]) from _call_TownFestivalNighteventoblackmail_2_Movement_2
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ fade_in()
        $ resolve_scene()
        Johan "Well guys, we're leaving now"
        YoungVillager "Sure! Have fun"
        $ blackmail = 2
        call GalleryViewed("noblackmail") from _call_TownFestivalNighteventoblackmail_2_GalleryViewed_1
        call Movement("TownFestivalNighteventoblackmail_2", "player", ["R","R"]) from _call_TownFestivalNighteventoblackmail_2_Movement_3
    $ resolve_scene()
    return False

label TownFestivalNighteventoblackmail(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNighteventoblackmail"):
        return None
    elif blackmail >= 2:
        return None
    elif blackmail >= 1:
        return None
    elif trigger == "event" and bottle_event >= 4:
        call PlayEvent(play_event, "TownFestivalNighteventoblackmail_2", "TownFestivalNighteventoblackmail") from _call_TownFestivalNighteventoblackmail_2_PlayEvent
        return (0, "", "TownFestivalNighteventoblackmail_2")
    elif trigger == "event" and bottle_event >= 3:
        call PlayEvent(play_event, "TownFestivalNighteventoblackmail_1", "TownFestivalNighteventoblackmail") from _call_TownFestivalNighteventoblackmail_1_PlayEvent
        return (0, "", "TownFestivalNighteventoblackmail_1")
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNighteventoblackmail_0", "TownFestivalNighteventoblackmail") from _call_TownFestivalNighteventoblackmail_0_PlayEvent
        return (0, "", "TownFestivalNighteventoblackmail_0")
    return None

label TownFestivalNighteventoescondite_0:
    Alexa "Leyna?"
    Leyna "Ho, Alexa... Good evening"
    Johan "Do you know them? (The girl looks familiar, but I don't remember from what)"
    Leyna "Hmmm... yes... Alexa and I.. well...."
    Alexa "We've seen each other around town a couple of times, the other day... we had tea together"
    "Leyna; Yes... exactly"
    Johan "Great, are you tourists too?"
    Alexa "Yes, I came with my husband. My cousin told me about this town some time ago and we decided to come with some friends"
    Johan "Wow great, nice to meet you guys"
    Husband "The pleasure is ours"
    Johan "Actually we were thinking of having dinner around here, do you know any place with homemade food?"
    Alexa "Yeah, right where we are now. During the holidays they have set up this kind of outdoor dining area where they serve you homemade food"
    Johan "Great.. but it looks like there's no space for us. For now we'll wait for a while and see if any tables gets empty"
    Alexa "Oh no no, that's not necessary. You can sit with us"
    Johan "Really?"
    Leyna "I don't know...we don't want to disturb"
    Alexa "Nonsense! It's no bother at all. Please join us"
    Johan "Well, if it's no problem, the truth is I'm starving"
    Husband "No more talk. Have a seat"
    $ fade_out()
    call ChangePartyMember("Leyna", False) from _call_TownFestivalNighteventoescondite_0_ChangePartyMember
    call TransferPlayer("TownFestivalNight", "TownFestivalNighteventoescondite_0", 19, 29, direction=4) from _call_TownFestivalNighteventoescondite_0_TransferPlayer
    $ hiding_place = 1
    $ fade_in()
    $ resolve_scene()
    call PauseForBalloon("TownFestivalNighteventoescondite_0") from _call_TownFestivalNighteventoescondite_0_PauseForBalloon
    Leyna "Wow, the food is delicious! And they have craft beer that is also very good... although a little strong, I'm already pretty drunk"
    Johan "Hip* you betcha!"
    Alexa "Hahaha yeah, by the way I've been told by some couples in town that they're going to play a game of hide and seek in a little while"
    Alexa "My husband and I have signed up, what do you say, will you join us?"
    Johan "Oh good idea, I feel like playing a game"
    Leyna "Sure, it will be fun. Plus we'll play with several couples, how romantic!"
    Alexa "Great! As soon as you finish your beers, let's go there, I've been told that men have to look for their partners. I'm sure it will be fun..."
    Johan "Great!"
    $ fade_out()
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ fade_in()
    $ resolve_scene()
    Johan "Everyone hide! We'll give you five minutes and come out to look for you!"
    Leyna "Hahaha this is going to be fun, if you haven't found us in half an hour, we'll meet you at the square."
    Husband "Yes, good idea"
    $ fade_out()
    call ChangePartyMember("Leyna", True) from _call_TownFestivalNighteventoescondite_0_ChangePartyMember_1
    call ChangePartyMember("Johan", False) from _call_TownFestivalNighteventoescondite_0_ChangePartyMember_2
    call TransferPlayer("Glade", "TownFestivalNighteventoescondite_0", 8, 5, direction=4) from _call_TownFestivalNighteventoescondite_0_TransferPlayer_1
    $ resolve_scene()
    $ tint_screen((-68, -68, 0, 68), 60, True)
    $ erase_picture(1)
    $ fade_in()
    $ resolve_scene()
    return False

label TownFestivalNighteventoescondite_1:
    Alexa "Leyna?"
    Leyna "Ho, Alexa... Good evening"
    Johan "Do you know them? (The girl looks familiar, but I don't remember from what)"
    Leyna "Hmmm... yes... Alexa and I.. well...."
    Alexa "We've seen each other around town a couple of times, the other day... we had tea together"
    "Leyna; Yes... exactly"
    Johan "Great, are you tourists too?"
    Alexa "Yes, I came with my husband. My cousin told me about this town some time ago and we decided to come with some friends"
    Johan "Wow great, nice to meet you guys"
    Husband "The pleasure is ours"
    Johan "Actually we were thinking of having dinner around here, do you know any place with homemade food?"
    Alexa "Yeah, right where we are now. During the holidays they have set up this kind of outdoor dining area where they serve you homemade food"
    Johan "Great.. but it looks like there's no space for us. For now we'll wait for a while and see if any tables gets empty"
    Alexa "Oh no no, that's not necessary. You can sit with us"
    Johan "Really?"
    Leyna "I don't know...we don't want to disturb"
    Alexa "Nonsense! It's no bother at all. Please join us"
    Johan "Well, if it's no problem, the truth is I'm starving"
    Husband "No more talk. Have a seat"
    $ fade_out()
    call ChangePartyMember("Leyna", False) from _call_TownFestivalNighteventoescondite_1_ChangePartyMember
    call TransferPlayer("TownFestivalNight", "TownFestivalNighteventoescondite_1", 19, 29, direction=4) from _call_TownFestivalNighteventoescondite_1_TransferPlayer
    $ hiding_place = 1
    $ fade_in()
    $ resolve_scene()
    call PauseForBalloon("TownFestivalNighteventoescondite_1") from _call_TownFestivalNighteventoescondite_1_PauseForBalloon
    Leyna "Wow, the food is delicious! And they have craft beer that is also very good... although a little strong, I'm already pretty drunk"
    Johan "Hip* you betcha!"
    Alexa "Hahaha yeah, by the way I've been told by some couples in town that they're going to play a game of hide and seek in a little while"
    Alexa "My husband and I have signed up, what do you say, will you join us?"
    Johan "Oh good idea, I feel like playing a game"
    Leyna "Sure, it will be fun. Plus we'll play with several couples, how romantic!"
    Alexa "Great! As soon as you finish your beers, let's go there, I've been told that men have to look for their partners. I'm sure it will be fun..."
    Johan "Great!"
    $ fade_out()
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ fade_in()
    $ resolve_scene()
    Johan "Everyone hide! We'll give you five minutes and come out to look for you!"
    Leyna "Hahaha this is going to be fun, if you haven't found us in half an hour, we'll meet you at the square."
    Husband "Yes, good idea"
    $ fade_out()
    call ChangePartyMember("Leyna", True) from _call_TownFestivalNighteventoescondite_1_ChangePartyMember_1
    call ChangePartyMember("Johan", False) from _call_TownFestivalNighteventoescondite_1_ChangePartyMember_2
    call TransferPlayer("Glade", "TownFestivalNighteventoescondite_1", 8, 5, direction=4) from _call_TownFestivalNighteventoescondite_1_TransferPlayer_1
    $ resolve_scene()
    $ tint_screen((-68, -68, 0, 68), 60, True)
    $ erase_picture(1)
    $ fade_in()
    $ resolve_scene()
    return False

label TownFestivalNighteventoescondite(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNighteventoescondite"):
        return None
    elif trigger == "event" and blackmail >= 2:
        call PlayEvent(play_event, "TownFestivalNighteventoescondite_1", "TownFestivalNighteventoescondite") from _call_TownFestivalNighteventoescondite_1_PlayEvent
        return (0, "", "TownFestivalNighteventoescondite_1")
    elif trigger == "event" and blackmail >= 1:
        call PlayEvent(play_event, "TownFestivalNighteventoescondite_0", "TownFestivalNighteventoescondite") from _call_TownFestivalNighteventoescondite_0_PlayEvent
        return (0, "", "TownFestivalNighteventoescondite_0")
    return None

label TownFestivalNightHesDrunkAgainMyHusbandCantHoldHisLiquorBase:
    Wife "He's drunk again, my husband can't hold his liquor"
    return False

label TownFestivalNightHesDrunkAgainMyHusbandCantHoldHisLiquor(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightHesDrunkAgainMyHusbandCantHoldHisLiquor"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFestivalNightHesDrunkAgainMyHusbandCantHoldHisLiquorBase", "TownFestivalNightHesDrunkAgainMyHusbandCantHoldHisLiquor") from _call_TownFestivalNightHesDrunkAgainMyHusbandCantHoldHisLiquor_PlayEvent
        return (1, "", "TownFestivalNightHesDrunkAgainMyHusbandCantHoldHisLiquor")
    return None

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_0:
    call PauseForBalloon("TownFestivalNightEV136_0") from _call_TownFestivalNightEV136_0_PauseForBalloon
    Leyna "I should look for Johan, this game has gone longer than I'd like"
    $ fade_out()
    $ set_switch("final_hideout", True)
    call GalleryViewed("rioleyna") from _call_TownFestivalNightEV136_0_GalleryViewed
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV136_0", 15, 10, direction=4) from _call_TownFestivalNightEV136_0_TransferPlayer
    $ fade_in()
    call Movement("TownFestivalNightEV136_0", "player", ["L","L","L","L","L","U","U","L","L","L"]) from _call_TownFestivalNightEV136_0_Movement
    call Movement("TownFestivalNightEV136_0", "TownFestivalNightjohan2", ["TURN_R"]) from _call_TownFestivalNightEV136_0_Movement_1
    $ resolve_scene()
    call PauseForBalloon("TownFestivalNightEV136_0") from _call_TownFestivalNightEV136_0_PauseForBalloon_1
    Johan "Leyna! I was starting to worry, I couldn't find you anywhere, everything all right?"
    Leyna "Hmm yes... everything... everything is fine! Well... Shall we go to sleep? I'm exhausted"
    Johan "Exhausted? But the night just started! We met some villagers and they invited us for a drink!"
    Alexa "Exactly Leyna! I'm sure you'll have a great time! Let's have a few beers and I'm sure you'll get over your tiredness!"
    Leyna "I don't feel like it guys..."
    Johan "Come on Leyna, it will be fun, we have worked hard these days, we deserve a night out!"
    Leyna "Okay guys... let's have a couple of beers"
    Alexa "Good!! We're meeting them for a drink nearby"
    $ fade_out()
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV136_0", 44, 39, direction=2) from _call_TownFestivalNightEV136_0_TransferPlayer_1
    call SetEventLocation("TownFestivalNightEV136_0", "TownFestivalNightalexa2", 43, 39) from _call_TownFestivalNightEV136_0_setloc
    call SetEventLocation("TownFestivalNightEV136_0", "TownFestivalNightmarido2", 43, 40) from _call_TownFestivalNightEV136_0_setloc_1
    call SetEventLocation("TownFestivalNightEV136_0", "TownFestivalNightjohan2", 45, 39) from _call_TownFestivalNightEV136_0_setloc_2
    $ fade_in()
    $ resolve_scene()
    Alexa "We are here! Did you get the beers?"
    Villager "Yes, we have plenty for the whole night"
    Johan "Great! It's been years since I've been out partying!"
    Villager2 "(Wow how lucky we are! We finally convinced the two tourist girls to come and drink! we have to make the most of it)"
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(SEVERAL BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "No, but seriously Johan, your wife is beautiful, I don't know how you can live in peace"
    Johan "Well (ugh I'm so drunk) let's see... I believe that the most important thing in a relationship is trust and I ... I trust Leyna completely"
    Villager "Very well said... but of course, all the festivals in this town revolve around showing off your body..."
    Villager "Aren't you worried that all the men in town will see your wife's body?"
    Leyna "W-well my body..."
    Johan "NO! I'm not worried, we were all born naked and it's completely natural!"
    Alexa "Very well said! You are absolutely right"
    AlexasHusband "..."
    Villager2 "Yeah! If you have a good body, what better than to show it off, right?"
    Johan "Well... also not..."
    Villager "Johan... you are a wise man!"
    Johan "O-okey Thank you hahaha..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(MANY MORE BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "BUah I'm pretty fucked up already... Do you know what I'm really interested in right now?"
    Leyna "Wh-hip-what do you feel like?"
    Villager "I feel like fucking"
    Leyna "!!!"
    Villager "HAHAHAHAAHA No... I really feel like going to the river to take a bath... are you in?"
    Alexa "Sure, why not? That way we can sober up a little bit"
    Johan "Yes, a cold bath would be great for me right now!"
    Leyna "But... in the river, we would all have to undress"
    Johan "Shit, true..."
    Villager "Well, as you said, it's completely natural right?"
    Johan "Well, yes..."
    Villager2 "And besides, there's trust, right Johan? It's just taking a bath and all..."
    Johan "Well, I guess you're right"
    Leyna "If JoHan AgRees, I hAve no probLem..."
    Villager "Great! (she seems to be quite drunk)"
    Johan "YES! I'm looking forward to going back to the river"
    Villager "Ehm... ahem yes, the river of course..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "LATER IN THE RIVER ..."
    Villager "Come on, everyone without clothes, otherwise the goddess will get angry"
    Johan "hahahahahaha okay let's go"
    Leyna "Okay, but give me one more shot of beer first hahaha"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV136_0_PlaySound
    $ show_picture(2, "rioleyna1")
    $ resolve_scene()
    Leyna "Ahhh how nice, how refreshing... it may be the alcohol but the truth is that being like this without worrying so much is very ... liberalizing"
    Johan "Right? Now I feel a little bad for being angry in the past"
    $ show_picture(3, "rioleyna2")
    $ resolve_scene()
    Villager "Yesssss this is all tradition here! We have no problem seeing each other naked!"
    Leyna "It's certainly very different from how we behave in the city, but I guess it's cool"
    Villager2 "Hahahahaha man, here we are all happy to see each other, especially you Leyna! What a great body!"
    Johan "hahhaha you bet! Eeven though she is my wife, I still can't get used to seeing her like this"
    $ show_picture(4, "rioleyna3")
    $ resolve_scene()
    Villager2 "Dude! You sure are glad to see Leyna!"
    Johan "Hahahaha"
    Leyna "WOW! what a big dick (!!!!!!) fu-fuck did I say that out loud? Sorry...."
    Leyna "When I drink too much I'm not myself"
    Johan "Hahaha...(Wow I didn't expect that comment from Leyna ... even though she told the truth I can't help but feel jealous... I have a weird feeling in my stomach"
    "looking at this situation... I don't know if it's because of the alcohol but... well, don't think about it too much Johan)"
    $ show_picture(5, "rioleyna4")
    $ resolve_scene()
    Villager2 "Well Leyna don't worry here we are all friends and there is trust, isn't it Johan?"
    Johan "Of course! You can admire my wife's beauty all you want! After all it's only for me hahahaha"
    Villager2 "But man, don't tell us that, we'll die of envy! hahahaha"
    Leyna "Well, I think I'm going to take a bath guys!"
    $ show_picture(6, "rioleyna5")
    $ resolve_scene()
    Villager "Wait, you're going to go like that? You should strip completely naked or you'll get your panties wet and get cold"
    Leyna "I'm just a little embarrassed, guys"
    Villager "Don't worry, we are all adults here!"
    Villager2 "Yes, we're not going to see anything we haven't seen before"
    Leyna "I guess you are right"
    $ show_picture(6, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    Johan "W-well, I don't know..."
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV136_0_PlaySound_1
    Johan "!!!!"
    Villager "Wow! Awesome! Leyna do you exercise or something?"
    Leyna "Well... I do go to the gym every week"
    Villager "Very well, let's see!"
    call PlaySound("sound", "audio/Fall.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV136_0_PlaySound_2
    Leyna "!!!"
    $ show_picture(7, "rioleyna6")
    $ resolve_scene()
    Villager "It really shows! You have a great ass! And what kind of exercises do you do at the gym?"
    Johan "Hey hey!"
    Villager "Some cycling perhaps?"
    $ show_picture(8, "rioleyna7")
    $ resolve_scene()
    Leyna "Y-yes some biking... and some rubber exercises"
    Johan "(They're ignoring me? It's like I'm not even here... and Leyna...)"
    Johan "(The penis of this man we met just is soo close to Leyna's pussy)"
    Villager2 "Wow! May I see it?"
    $ show_picture(9, "rioleyna8")
    $ resolve_scene()
    Villager "Of course, look at her thighs! She's a real sportswoman!"
    Leyna "hm!"
    Villager2 "YES... that ... firmer thighs!"
    $ show_picture(10, "rioleyna9")
    $ resolve_scene()
    Villager2 "You could teach us some exercise, the truth is that these last years I have neglected a lot my physique and I'm getting a lot of belly hahahaa"
    Villager "Yes! With this great body you have to know some really good exercises!"
    Leyna "W-well, you could..."
    Johan "(This situation is getting too long for my taste... but after the little speech about trust I said before, I don't want to yell at them now)"
    $ show_picture(11, "rioleyna10")
    $ resolve_scene()
    Villager2 "What? I'm sorry, but you speak very softly and I can't hear you"
    Leyna "!!! I.... I..."
    Johan "Ahem well Leyna... shall we take a bath?"
    $ show_picture(12, "rioleyna11")
    $ resolve_scene()
    Leyna "Y-yeah right (for a second I forgot Johan is here, thank good from where he is, he can't see that this man's penis is pressed on me)"
    Villager "Oh! yeah, we'd better go for a swim"
    Villager2 "Yes, you're right hahaha sorry Johan!"
    $ show_picture(13, "rioleyna12")
    $ resolve_scene()
    Leyna "!!!Oooh!"
    Villager2 "Oops! I slipped! We almost fell down Leyna! hahaha"
    Villager2 "Uf... my back is... my back is bad, hold me for a second"
    Johan "??? Are you okay?"
    Villager2 "Oh yes yes, just give me a second"
    $ show_picture(14, "rioleyna13")
    $ resolve_scene()
    Leyna "hmmmmm Ahhh... I... I..."
    Villager "What's wrong Leyna? Did you hurt yourself?"
    Leyna "(Johan is right there... and this man has stuck his dick all the way in... in front of my husband...)"
    Johan "Leyna?"
    $ show_picture(15, "rioleyna14")
    $ resolve_scene()
    "plop! "
    Villager2 "There you go... hahahah it's just that my back always gives me problems, everything ok Leyna? Sorry I fell on you"
    Leyna "(Heavy breathing) Ah ah ah ah.... yes ... all right... come on Johan... let's go for a swim"
    Johan "Sure! (for a second I thought that... anyway, it's just my imagination...)"
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
    call ChangePartyMember("Johan", True) from _call_TownFestivalNightEV136_0_ChangePartyMember
    call TransferPlayer("TownNight", "TownFestivalNightEV136_0", 47, 23, direction=4) from _call_TownFestivalNightEV136_0_TransferPlayer_2
    $ fade_in()
    call Movement("TownFestivalNightEV136_0", "player", ["L","L","L","TURN_R"]) from _call_TownFestivalNightEV136_0_Movement_2
    $ resolve_scene()
    Johan "It looks like everyone has already gone to sleep... We better go to sleep too"
    Leyna "Yes... you are right"
    $ fade_out()
    call TransferPlayer("Town2", "TownFestivalNightEV136_0", 28, 22, direction=0) from _call_TownFestivalNightEV136_0_TransferPlayer_3
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ fade_in()
    $ resolve_scene()
    "The next morning..."
    $ erase_picture(1)
    call Movement("TownFestivalNightEV136_0", "player", ["D","TURN_U"]) from _call_TownFestivalNightEV136_0_Movement_3
    $ resolve_scene()
    Johan "My God, I have a terrible hangover, I can hardly remember what happened yesterday"
    Johan "... We were on the river with some guys, right? I hope we didn't do anything crazy"
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Oh hahaha... Right... no, relax we didn't do anything crazy...I don't remember much either...I also have a good hangover hahaha"
    Johan "Yeah... Well, what do you feel like doing today?"
    Leyna "The truth is that I should stop by my work at the hotsprings... but I can come by later"
    Johan "Don't worry, I could use a hot bath, I could walk you over there and take a bath and then I'll do some time while you finish up"
    Leyna "You don't have to if you don't want to..."
    Johan "Don't worry! It's not a problem!"
    Leyna "W-well, let's go there"
    $ erase_picture(1)
    $ resolve_scene()
    return False

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_1:
    call PauseForBalloon("TownFestivalNightEV136_1") from _call_TownFestivalNightEV136_1_PauseForBalloon
    Leyna "I should look for Johan, this game has gone longer than I'd like"
    $ fade_out()
    $ set_switch("final_hideout", True)
    call GalleryViewed("rioleyna") from _call_TownFestivalNightEV136_1_GalleryViewed
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV136_1", 15, 10, direction=4) from _call_TownFestivalNightEV136_1_TransferPlayer
    $ fade_in()
    call Movement("TownFestivalNightEV136_1", "player", ["L","L","L","L","L","U","U","L","L","L"]) from _call_TownFestivalNightEV136_1_Movement
    call Movement("TownFestivalNightEV136_1", "TownFestivalNightjohan2", ["TURN_R"]) from _call_TownFestivalNightEV136_1_Movement_1
    $ resolve_scene()
    call PauseForBalloon("TownFestivalNightEV136_1") from _call_TownFestivalNightEV136_1_PauseForBalloon_1
    Johan "Leyna! I was starting to worry, I couldn't find you anywhere, everything all right?"
    Leyna "Hmm yes... everything... everything is fine! Well... Shall we go to sleep? I'm exhausted"
    Johan "Exhausted? But the night just started! We met some villagers and they invited us for a drink!"
    Alexa "Exactly Leyna! I'm sure you'll have a great time! Let's have a few beers and I'm sure you'll get over your tiredness!"
    Leyna "I don't feel like it guys..."
    Johan "Come on Leyna, it will be fun, we have worked hard these days, we deserve a night out!"
    Leyna "Okay guys... let's have a couple of beers"
    Alexa "Good!! We're meeting them for a drink nearby"
    $ fade_out()
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV136_1", 44, 39, direction=2) from _call_TownFestivalNightEV136_1_TransferPlayer_1
    call SetEventLocation("TownFestivalNightEV136_1", "TownFestivalNightalexa2", 43, 39) from _call_TownFestivalNightEV136_1_setloc
    call SetEventLocation("TownFestivalNightEV136_1", "TownFestivalNightmarido2", 43, 40) from _call_TownFestivalNightEV136_1_setloc_1
    call SetEventLocation("TownFestivalNightEV136_1", "TownFestivalNightjohan2", 45, 39) from _call_TownFestivalNightEV136_1_setloc_2
    $ fade_in()
    $ resolve_scene()
    Alexa "We are here! Did you get the beers?"
    Villager "Yes, we have plenty for the whole night"
    Johan "Great! It's been years since I've been out partying!"
    Villager2 "(Wow how lucky we are! We finally convinced the two tourist girls to come and drink! we have to make the most of it)"
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(SEVERAL BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "No, but seriously Johan, your wife is beautiful, I don't know how you can live in peace"
    Johan "Well (ugh I'm so drunk) let's see... I believe that the most important thing in a relationship is trust and I ... I trust Leyna completely"
    Villager "Very well said... but of course, all the festivals in this town revolve around showing off your body..."
    Villager "Aren't you worried that all the men in town will see your wife's body?"
    Leyna "W-well my body..."
    Johan "NO! I'm not worried, we were all born naked and it's completely natural!"
    Alexa "Very well said! You are absolutely right"
    AlexasHusband "..."
    Villager2 "Yeah! If you have a good body, what better than to show it off, right?"
    Johan "Well... also not..."
    Villager "Johan... you are a wise man!"
    Johan "O-okey Thank you hahaha..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(MANY MORE BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "BUah I'm pretty fucked up already... Do you know what I'm really interested in right now?"
    Leyna "Wh-hip-what do you feel like?"
    Villager "I feel like fucking"
    Leyna "!!!"
    Villager "HAHAHAHAAHA No... I really feel like going to the river to take a bath... are you in?"
    Alexa "Sure, why not? That way we can sober up a little bit"
    Johan "Yes, a cold bath would be great for me right now!"
    Leyna "But... in the river, we would all have to undress"
    Johan "Shit, true..."
    Villager "Well, as you said, it's completely natural right?"
    Johan "Well, yes..."
    Villager2 "And besides, there's trust, right Johan? It's just taking a bath and all..."
    Johan "Well, I guess you're right"
    Leyna "If JoHan AgRees, I hAve no probLem..."
    Villager "Great! (she seems to be quite drunk)"
    Johan "YES! I'm looking forward to going back to the river"
    Villager "Ehm... ahem yes, the river of course..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "LATER IN THE RIVER ..."
    Villager "Come on, everyone without clothes, otherwise the goddess will get angry"
    Johan "hahahahahaha okay let's go"
    Leyna "Okay, but give me one more shot of beer first hahaha"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV136_1_PlaySound
    $ show_picture(2, "rioleyna1")
    $ resolve_scene()
    Leyna "Ahhh how nice, how refreshing... it may be the alcohol but the truth is that being like this without worrying so much is very ... liberalizing"
    Johan "Right? Now I feel a little bad for being angry in the past"
    $ show_picture(3, "rioleyna2")
    $ resolve_scene()
    Villager "Yesssss this is all tradition here! We have no problem seeing each other naked!"
    Leyna "It's certainly very different from how we behave in the city, but I guess it's cool"
    Villager2 "Hahahahaha man, here we are all happy to see each other, especially you Leyna! What a great body!"
    Johan "hahhaha you bet! Eeven though she is my wife, I still can't get used to seeing her like this"
    $ show_picture(4, "rioleyna3")
    $ resolve_scene()
    Villager2 "Dude! You sure are glad to see Leyna!"
    Johan "Hahahaha"
    Leyna "WOW! what a big dick (!!!!!!) fu-fuck did I say that out loud? Sorry...."
    Leyna "When I drink too much I'm not myself"
    Johan "Hahaha...(Wow I didn't expect that comment from Leyna ... even though she told the truth I can't help but feel jealous... I have a weird feeling in my stomach"
    "looking at this situation... I don't know if it's because of the alcohol but... well, don't think about it too much Johan)"
    $ show_picture(5, "rioleyna4")
    $ resolve_scene()
    Villager2 "Well Leyna don't worry here we are all friends and there is trust, isn't it Johan?"
    Johan "Of course! You can admire my wife's beauty all you want! After all it's only for me hahahaha"
    Villager2 "But man, don't tell us that, we'll die of envy! hahahaha"
    Leyna "Well, I think I'm going to take a bath guys!"
    $ show_picture(6, "rioleyna5")
    $ resolve_scene()
    Villager "Wait, you're going to go like that? You should strip completely naked or you'll get your panties wet and get cold"
    Leyna "I'm just a little embarrassed, guys"
    Villager "Don't worry, we are all adults here!"
    Villager2 "Yes, we're not going to see anything we haven't seen before"
    Leyna "I guess you are right"
    $ show_picture(6, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    Johan "W-well, I don't know..."
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV136_1_PlaySound_1
    Johan "!!!!"
    Villager "Wow! Awesome! Leyna do you exercise or something?"
    Leyna "Well... I do go to the gym every week"
    Villager "Very well, let's see!"
    call PlaySound("sound", "audio/Fall.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV136_1_PlaySound_2
    Leyna "!!!"
    $ show_picture(7, "rioleyna6")
    $ resolve_scene()
    Villager "It really shows! You have a great ass! And what kind of exercises do you do at the gym?"
    Johan "Hey hey!"
    Villager "Some cycling perhaps?"
    $ show_picture(8, "rioleyna7")
    $ resolve_scene()
    Leyna "Y-yes some biking... and some rubber exercises"
    Johan "(They're ignoring me? It's like I'm not even here... and Leyna...)"
    Johan "(The penis of this man we met just is soo close to Leyna's pussy)"
    Villager2 "Wow! May I see it?"
    $ show_picture(9, "rioleyna8")
    $ resolve_scene()
    Villager "Of course, look at her thighs! She's a real sportswoman!"
    Leyna "hm!"
    Villager2 "YES... that ... firmer thighs!"
    $ show_picture(10, "rioleyna9")
    $ resolve_scene()
    Villager2 "You could teach us some exercise, the truth is that these last years I have neglected a lot my physique and I'm getting a lot of belly hahahaa"
    Villager "Yes! With this great body you have to know some really good exercises!"
    Leyna "W-well, you could..."
    Johan "(This situation is getting too long for my taste... but after the little speech about trust I said before, I don't want to yell at them now)"
    $ show_picture(11, "rioleyna10")
    $ resolve_scene()
    Villager2 "What? I'm sorry, but you speak very softly and I can't hear you"
    Leyna "!!! I.... I..."
    Johan "Ahem well Leyna... shall we take a bath?"
    $ show_picture(12, "rioleyna11")
    $ resolve_scene()
    Leyna "Y-yeah right (for a second I forgot Johan is here, thank good from where he is, he can't see that this man's penis is pressed on me)"
    Villager "Oh! yeah, we'd better go for a swim"
    Villager2 "Yes, you're right hahaha sorry Johan!"
    $ show_picture(13, "rioleyna12")
    $ resolve_scene()
    Leyna "!!!Oooh!"
    Villager2 "Oops! I slipped! We almost fell down Leyna! hahaha"
    Villager2 "Uf... my back is... my back is bad, hold me for a second"
    Johan "??? Are you okay?"
    Villager2 "Oh yes yes, just give me a second"
    $ show_picture(14, "rioleyna13")
    $ resolve_scene()
    Leyna "hmmmmm Ahhh... I... I..."
    Villager "What's wrong Leyna? Did you hurt yourself?"
    Leyna "(Johan is right there... and this man has stuck his dick all the way in... in front of my husband...)"
    Johan "Leyna?"
    $ show_picture(15, "rioleyna14")
    $ resolve_scene()
    "plop! "
    Villager2 "There you go... hahahah it's just that my back always gives me problems, everything ok Leyna? Sorry I fell on you"
    Leyna "(Heavy breathing) Ah ah ah ah.... yes ... all right... come on Johan... let's go for a swim"
    Johan "Sure! (for a second I thought that... anyway, it's just my imagination...)"
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
    call ChangePartyMember("Johan", True) from _call_TownFestivalNightEV136_1_ChangePartyMember
    call TransferPlayer("TownNight", "TownFestivalNightEV136_1", 47, 23, direction=4) from _call_TownFestivalNightEV136_1_TransferPlayer_2
    $ fade_in()
    call Movement("TownFestivalNightEV136_1", "player", ["L","L","L","TURN_R"]) from _call_TownFestivalNightEV136_1_Movement_2
    $ resolve_scene()
    Johan "It looks like everyone has already gone to sleep... We better go to sleep too"
    Leyna "Yes... you are right"
    $ fade_out()
    call TransferPlayer("Town2", "TownFestivalNightEV136_1", 28, 22, direction=0) from _call_TownFestivalNightEV136_1_TransferPlayer_3
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ fade_in()
    $ resolve_scene()
    "The next morning..."
    $ erase_picture(1)
    call Movement("TownFestivalNightEV136_1", "player", ["D","TURN_U"]) from _call_TownFestivalNightEV136_1_Movement_3
    $ resolve_scene()
    Johan "My God, I have a terrible hangover, I can hardly remember what happened yesterday"
    Johan "... We were on the river with some guys, right? I hope we didn't do anything crazy"
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Oh hahaha... Right... no, relax we didn't do anything crazy...I don't remember much either...I also have a good hangover hahaha"
    Johan "Yeah... Well, what do you feel like doing today?"
    Leyna "The truth is that I should stop by my work at the hotsprings... but I can come by later"
    Johan "Don't worry, I could use a hot bath, I could walk you over there and take a bath and then I'll do some time while you finish up"
    Leyna "You don't have to if you don't want to..."
    Johan "Don't worry! It's not a problem!"
    Leyna "W-well, let's go there"
    $ erase_picture(1)
    $ resolve_scene()
    return False

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike"):
        return None
    elif trigger == "event" and hiding_place >= 4:
        call PlayEvent(play_event, "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_1", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike") from _call_TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_1_PlayEvent
        return (0, "", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_1")
    elif trigger == "event" and hiding_place >= 3:
        call PlayEvent(play_event, "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_0", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike") from _call_TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_0_PlayEvent
        return (0, "", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_0")
    return None

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v2_0:
    call PauseForBalloon("TownFestivalNightEV143_0") from _call_TownFestivalNightEV143_0_PauseForBalloon
    Leyna "I should look for Johan, this game has gone longer than I'd like"
    $ fade_out()
    $ set_switch("final_hideout", True)
    call GalleryViewed("rioleyna") from _call_TownFestivalNightEV143_0_GalleryViewed
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV143_0", 15, 10, direction=4) from _call_TownFestivalNightEV143_0_TransferPlayer
    $ fade_in()
    call Movement("TownFestivalNightEV143_0", "player", ["L","L","L","L","L","U","U","L","L","L"]) from _call_TownFestivalNightEV143_0_Movement
    call Movement("TownFestivalNightEV143_0", "TownFestivalNightjohan2", ["TURN_R"]) from _call_TownFestivalNightEV143_0_Movement_1
    $ resolve_scene()
    call PauseForBalloon("TownFestivalNightEV143_0") from _call_TownFestivalNightEV143_0_PauseForBalloon_1
    Johan "Leyna! I was starting to worry, I couldn't find you anywhere, everything all right?"
    Leyna "Hmm yes... everything... everything is fine! Well... Shall we go to sleep? I'm exhausted"
    Johan "Exhausted? But the night just started! We met some villagers and they invited us for a drink!"
    Alexa "Exactly Leyna! I'm sure you'll have a great time! Let's have a few beers and I'm sure you'll get over your tiredness!"
    Leyna "I don't feel like it guys..."
    Johan "Come on Leyna, it will be fun, we have worked hard these days, we deserve a night out!"
    Leyna "Okay guys... let's have a couple of beers"
    Alexa "Good!! We're meeting them for a drink nearby"
    $ fade_out()
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV143_0", 44, 39, direction=2) from _call_TownFestivalNightEV143_0_TransferPlayer_1
    call SetEventLocation("TownFestivalNightEV143_0", "TownFestivalNightalexa2", 43, 39) from _call_TownFestivalNightEV143_0_setloc
    call SetEventLocation("TownFestivalNightEV143_0", "TownFestivalNightmarido2", 43, 40) from _call_TownFestivalNightEV143_0_setloc_1
    call SetEventLocation("TownFestivalNightEV143_0", "TownFestivalNightjohan2", 45, 39) from _call_TownFestivalNightEV143_0_setloc_2
    $ fade_in()
    $ resolve_scene()
    Alexa "We are here! Did you get the beers?"
    Villager "Yes, we have plenty for the whole night"
    Johan "Great! It's been years since I've been out partying!"
    Villager2 "(Wow how lucky we are! We finally convinced the two tourist girls to come and drink! we have to make the most of it)"
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(SEVERAL BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "No, but seriously Johan, your wife is beautiful, I don't know how you can live in peace"
    Johan "Well (ugh I'm so drunk) let's see... I believe that the most important thing in a relationship is trust and I ... I trust Leyna completely"
    Villager "Very well said... but of course, all the festivals in this town revolve around showing off your body..."
    Villager "Aren't you worried that all the men in town will see your wife's body?"
    Leyna "W-well my body..."
    Johan "NO! I'm not worried, we were all born naked and it's completely natural!"
    Alexa "Very well said! You are absolutely right"
    AlexasHusband "..."
    Villager2 "Yeah! If you have a good body, what better than to show it off, right?"
    Johan "Well... also not..."
    Villager "Johan... you are a wise man!"
    Johan "O-okey Thank you hahaha..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(MANY MORE BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "BUah I'm pretty fucked up already... Do you know what I'm really interested in right now?"
    Leyna "Wh-hip-what do you feel like?"
    Villager "I feel like fucking"
    Leyna "!!!"
    Villager "HAHAHAHAAHA No... I really feel like going to the river to take a bath... are you in?"
    Alexa "Sure, why not? That way we can sober up a little bit"
    Johan "Yes, a cold bath would be great for me right now!"
    Leyna "But... in the river, we would all have to undress"
    Johan "Shit, true..."
    Villager "Well, as you said, it's completely natural right?"
    Johan "Well, yes..."
    Villager2 "And besides, there's trust, right Johan? It's just taking a bath and all..."
    Johan "Well, I guess you're right"
    Leyna "If JoHan AgRees, I hAve no probLem..."
    Villager "Great! (she seems to be quite drunk)"
    Johan "YES! I'm looking forward to going back to the river"
    Villager "Ehm... ahem yes, the river of course..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "LATER IN THE RIVER ..."
    Villager "Come on, everyone without clothes, otherwise the goddess will get angry"
    Johan "hahahahahaha okay let's go"
    Leyna "Okay, but give me one more shot of beer first hahaha"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV143_0_PlaySound
    $ show_picture(2, "rioleyna1")
    $ resolve_scene()
    Leyna "Ahhh how nice, how refreshing... it may be the alcohol but the truth is that being like this without worrying so much is very ... liberalizing"
    Johan "Right? Now I feel a little bad for being angry in the past"
    $ show_picture(3, "rioleyna2")
    $ resolve_scene()
    Villager "Yesssss this is all tradition here! We have no problem seeing each other naked!"
    Leyna "It's certainly very different from how we behave in the city, but I guess it's cool"
    Villager2 "Hahahahaha man, here we are all happy to see each other, especially you Leyna! What a great body!"
    Johan "hahhaha you bet! Eeven though she is my wife, I still can't get used to seeing her like this"
    $ show_picture(4, "rioleyna3")
    $ resolve_scene()
    Villager2 "Dude! You sure are glad to see Leyna!"
    Johan "Hahahaha"
    Leyna "WOW! what a big dick (!!!!!!) fu-fuck did I say that out loud? Sorry...."
    Leyna "When I drink too much I'm not myself"
    Johan "Hahaha...(Wow I didn't expect that comment from Leyna ... even though she told the truth I can't help but feel jealous... I have a weird feeling in my stomach"
    "looking at this situation... I don't know if it's because of the alcohol but... well, don't think about it too much Johan)"
    $ show_picture(5, "rioleyna4")
    $ resolve_scene()
    Villager2 "Well Leyna don't worry here we are all friends and there is trust, isn't it Johan?"
    Johan "Of course! You can admire my wife's beauty all you want! After all it's only for me hahahaha"
    Villager2 "But man, don't tell us that, we'll die of envy! hahahaha"
    Leyna "Well, I think I'm going to take a bath guys!"
    $ show_picture(6, "rioleyna5")
    $ resolve_scene()
    Villager "Wait, you're going to go like that? You should strip completely naked or you'll get your panties wet and get cold"
    Leyna "I'm just a little embarrassed, guys"
    Villager "Don't worry, we are all adults here!"
    Villager2 "Yes, we're not going to see anything we haven't seen before"
    Leyna "I guess you are right"
    $ show_picture(6, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    Johan "W-well, I don't know..."
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV143_0_PlaySound_1
    Johan "!!!!"
    Villager "Wow! Awesome! Leyna do you exercise or something?"
    Leyna "Well... I do go to the gym every week"
    Villager "Very well, let's see!"
    call PlaySound("sound", "audio/Fall.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV143_0_PlaySound_2
    Leyna "!!!"
    $ show_picture(7, "rioleyna6")
    $ resolve_scene()
    Villager "It really shows! You have a great ass! And what kind of exercises do you do at the gym?"
    Johan "Hey hey!"
    Villager "Some cycling perhaps?"
    $ show_picture(8, "rioleyna7")
    $ resolve_scene()
    Leyna "Y-yes some biking... and some rubber exercises"
    Johan "(They're ignoring me? It's like I'm not even here... and Leyna...)"
    Johan "(The penis of this man we met just is soo close to Leyna's pussy)"
    Villager2 "Wow! May I see it?"
    $ show_picture(9, "rioleyna8")
    $ resolve_scene()
    Villager "Of course, look at her thighs! She's a real sportswoman!"
    Leyna "hm!"
    Villager2 "YES... that ... firmer thighs!"
    $ show_picture(10, "rioleyna9")
    $ resolve_scene()
    Villager2 "You could teach us some exercise, the truth is that these last years I have neglected a lot my physique and I'm getting a lot of belly hahahaa"
    Villager "Yes! With this great body you have to know some really good exercises!"
    Leyna "W-well, you could..."
    Johan "(This situation is getting too long for my taste... but after the little speech about trust I said before, I don't want to yell at them now)"
    $ show_picture(11, "rioleyna10")
    $ resolve_scene()
    Villager2 "What? I'm sorry, but you speak very softly and I can't hear you"
    Leyna "!!! I.... I..."
    Johan "Ahem well Leyna... shall we take a bath?"
    $ show_picture(12, "rioleyna11")
    $ resolve_scene()
    Leyna "Y-yeah right (for a second I forgot Johan is here, thank good from where he is, he can't see that this man's penis is pressed on me)"
    Villager "Oh! yeah, we'd better go for a swim"
    Villager2 "Yes, you're right hahaha sorry Johan!"
    $ show_picture(13, "rioleyna12")
    $ resolve_scene()
    Leyna "!!!Oooh!"
    Villager2 "Oops! I slipped! We almost fell down Leyna! hahaha"
    Villager2 "Uf... my back is... my back is bad, hold me for a second"
    Johan "??? Are you okay?"
    Villager2 "Oh yes yes, just give me a second"
    $ show_picture(14, "rioleyna13")
    $ resolve_scene()
    Leyna "hmmmmm Ahhh... I... I..."
    Villager "What's wrong Leyna? Did you hurt yourself?"
    Leyna "(Johan is right there... and this man has stuck his dick all the way in... in front of my husband...)"
    Johan "Leyna?"
    $ show_picture(15, "rioleyna14")
    $ resolve_scene()
    "plop! "
    Villager2 "There you go... hahahah it's just that my back always gives me problems, everything ok Leyna? Sorry I fell on you"
    Leyna "(Heavy breathing) Ah ah ah ah.... yes ... all right... come on Johan... let's go for a swim"
    Johan "Sure! (for a second I thought that... anyway, it's just my imagination...)"
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
    call ChangePartyMember("Johan", True) from _call_TownFestivalNightEV143_0_ChangePartyMember
    call TransferPlayer("TownNight", "TownFestivalNightEV143_0", 47, 23, direction=4) from _call_TownFestivalNightEV143_0_TransferPlayer_2
    $ fade_in()
    call Movement("TownFestivalNightEV143_0", "player", ["L","L","L","TURN_R"]) from _call_TownFestivalNightEV143_0_Movement_2
    $ resolve_scene()
    Johan "It looks like everyone has already gone to sleep... We better go to sleep too"
    Leyna "Yes... you are right"
    $ fade_out()
    call TransferPlayer("Town2", "TownFestivalNightEV143_0", 28, 22, direction=0) from _call_TownFestivalNightEV143_0_TransferPlayer_3
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ fade_in()
    $ resolve_scene()
    "The next morning..."
    $ erase_picture(1)
    call Movement("TownFestivalNightEV143_0", "player", ["D","TURN_U"]) from _call_TownFestivalNightEV143_0_Movement_3
    $ resolve_scene()
    Johan "My God, I have a terrible hangover, I can hardly remember what happened yesterday"
    Johan "... We were on the river with some guys, right? I hope we didn't do anything crazy"
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Oh hahaha... Right... no, relax we didn't do anything crazy...I don't remember much either...I also have a good hangover hahaha"
    Johan "Yeah... Well, what do you feel like doing today?"
    Leyna "The truth is that I should stop by my work at the hotsprings... but I can come by later"
    Johan "Don't worry, I could use a hot bath, I could walk you over there and take a bath and then I'll do some time while you finish up"
    Leyna "You don't have to if you don't want to..."
    Johan "Don't worry! It's not a problem!"
    Leyna "W-well, let's go there"
    $ erase_picture(1)
    $ resolve_scene()
    return False

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v2_1:
    call PauseForBalloon("TownFestivalNightEV143_1") from _call_TownFestivalNightEV143_1_PauseForBalloon
    Leyna "I should look for Johan, this game has gone longer than I'd like"
    $ fade_out()
    $ set_switch("final_hideout", True)
    call GalleryViewed("rioleyna") from _call_TownFestivalNightEV143_1_GalleryViewed
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV143_1", 15, 10, direction=4) from _call_TownFestivalNightEV143_1_TransferPlayer
    $ fade_in()
    call Movement("TownFestivalNightEV143_1", "player", ["L","L","L","L","L","U","U","L","L","L"]) from _call_TownFestivalNightEV143_1_Movement
    call Movement("TownFestivalNightEV143_1", "TownFestivalNightjohan2", ["TURN_R"]) from _call_TownFestivalNightEV143_1_Movement_1
    $ resolve_scene()
    call PauseForBalloon("TownFestivalNightEV143_1") from _call_TownFestivalNightEV143_1_PauseForBalloon_1
    Johan "Leyna! I was starting to worry, I couldn't find you anywhere, everything all right?"
    Leyna "Hmm yes... everything... everything is fine! Well... Shall we go to sleep? I'm exhausted"
    Johan "Exhausted? But the night just started! We met some villagers and they invited us for a drink!"
    Alexa "Exactly Leyna! I'm sure you'll have a great time! Let's have a few beers and I'm sure you'll get over your tiredness!"
    Leyna "I don't feel like it guys..."
    Johan "Come on Leyna, it will be fun, we have worked hard these days, we deserve a night out!"
    Leyna "Okay guys... let's have a couple of beers"
    Alexa "Good!! We're meeting them for a drink nearby"
    $ fade_out()
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV143_1", 44, 39, direction=2) from _call_TownFestivalNightEV143_1_TransferPlayer_1
    call SetEventLocation("TownFestivalNightEV143_1", "TownFestivalNightalexa2", 43, 39) from _call_TownFestivalNightEV143_1_setloc
    call SetEventLocation("TownFestivalNightEV143_1", "TownFestivalNightmarido2", 43, 40) from _call_TownFestivalNightEV143_1_setloc_1
    call SetEventLocation("TownFestivalNightEV143_1", "TownFestivalNightjohan2", 45, 39) from _call_TownFestivalNightEV143_1_setloc_2
    $ fade_in()
    $ resolve_scene()
    Alexa "We are here! Did you get the beers?"
    Villager "Yes, we have plenty for the whole night"
    Johan "Great! It's been years since I've been out partying!"
    Villager2 "(Wow how lucky we are! We finally convinced the two tourist girls to come and drink! we have to make the most of it)"
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(SEVERAL BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "No, but seriously Johan, your wife is beautiful, I don't know how you can live in peace"
    Johan "Well (ugh I'm so drunk) let's see... I believe that the most important thing in a relationship is trust and I ... I trust Leyna completely"
    Villager "Very well said... but of course, all the festivals in this town revolve around showing off your body..."
    Villager "Aren't you worried that all the men in town will see your wife's body?"
    Leyna "W-well my body..."
    Johan "NO! I'm not worried, we were all born naked and it's completely natural!"
    Alexa "Very well said! You are absolutely right"
    AlexasHusband "..."
    Villager2 "Yeah! If you have a good body, what better than to show it off, right?"
    Johan "Well... also not..."
    Villager "Johan... you are a wise man!"
    Johan "O-okey Thank you hahaha..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(MANY MORE BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "BUah I'm pretty fucked up already... Do you know what I'm really interested in right now?"
    Leyna "Wh-hip-what do you feel like?"
    Villager "I feel like fucking"
    Leyna "!!!"
    Villager "HAHAHAHAAHA No... I really feel like going to the river to take a bath... are you in?"
    Alexa "Sure, why not? That way we can sober up a little bit"
    Johan "Yes, a cold bath would be great for me right now!"
    Leyna "But... in the river, we would all have to undress"
    Johan "Shit, true..."
    Villager "Well, as you said, it's completely natural right?"
    Johan "Well, yes..."
    Villager2 "And besides, there's trust, right Johan? It's just taking a bath and all..."
    Johan "Well, I guess you're right"
    Leyna "If JoHan AgRees, I hAve no probLem..."
    Villager "Great! (she seems to be quite drunk)"
    Johan "YES! I'm looking forward to going back to the river"
    Villager "Ehm... ahem yes, the river of course..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "LATER IN THE RIVER ..."
    Villager "Come on, everyone without clothes, otherwise the goddess will get angry"
    Johan "hahahahahaha okay let's go"
    Leyna "Okay, but give me one more shot of beer first hahaha"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV143_1_PlaySound
    $ show_picture(2, "rioleyna1")
    $ resolve_scene()
    Leyna "Ahhh how nice, how refreshing... it may be the alcohol but the truth is that being like this without worrying so much is very ... liberalizing"
    Johan "Right? Now I feel a little bad for being angry in the past"
    $ show_picture(3, "rioleyna2")
    $ resolve_scene()
    Villager "Yesssss this is all tradition here! We have no problem seeing each other naked!"
    Leyna "It's certainly very different from how we behave in the city, but I guess it's cool"
    Villager2 "Hahahahaha man, here we are all happy to see each other, especially you Leyna! What a great body!"
    Johan "hahhaha you bet! Eeven though she is my wife, I still can't get used to seeing her like this"
    $ show_picture(4, "rioleyna3")
    $ resolve_scene()
    Villager2 "Dude! You sure are glad to see Leyna!"
    Johan "Hahahaha"
    Leyna "WOW! what a big dick (!!!!!!) fu-fuck did I say that out loud? Sorry...."
    Leyna "When I drink too much I'm not myself"
    Johan "Hahaha...(Wow I didn't expect that comment from Leyna ... even though she told the truth I can't help but feel jealous... I have a weird feeling in my stomach"
    "looking at this situation... I don't know if it's because of the alcohol but... well, don't think about it too much Johan)"
    $ show_picture(5, "rioleyna4")
    $ resolve_scene()
    Villager2 "Well Leyna don't worry here we are all friends and there is trust, isn't it Johan?"
    Johan "Of course! You can admire my wife's beauty all you want! After all it's only for me hahahaha"
    Villager2 "But man, don't tell us that, we'll die of envy! hahahaha"
    Leyna "Well, I think I'm going to take a bath guys!"
    $ show_picture(6, "rioleyna5")
    $ resolve_scene()
    Villager "Wait, you're going to go like that? You should strip completely naked or you'll get your panties wet and get cold"
    Leyna "I'm just a little embarrassed, guys"
    Villager "Don't worry, we are all adults here!"
    Villager2 "Yes, we're not going to see anything we haven't seen before"
    Leyna "I guess you are right"
    $ show_picture(6, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    Johan "W-well, I don't know..."
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV143_1_PlaySound_1
    Johan "!!!!"
    Villager "Wow! Awesome! Leyna do you exercise or something?"
    Leyna "Well... I do go to the gym every week"
    Villager "Very well, let's see!"
    call PlaySound("sound", "audio/Fall.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV143_1_PlaySound_2
    Leyna "!!!"
    $ show_picture(7, "rioleyna6")
    $ resolve_scene()
    Villager "It really shows! You have a great ass! And what kind of exercises do you do at the gym?"
    Johan "Hey hey!"
    Villager "Some cycling perhaps?"
    $ show_picture(8, "rioleyna7")
    $ resolve_scene()
    Leyna "Y-yes some biking... and some rubber exercises"
    Johan "(They're ignoring me? It's like I'm not even here... and Leyna...)"
    Johan "(The penis of this man we met just is soo close to Leyna's pussy)"
    Villager2 "Wow! May I see it?"
    $ show_picture(9, "rioleyna8")
    $ resolve_scene()
    Villager "Of course, look at her thighs! She's a real sportswoman!"
    Leyna "hm!"
    Villager2 "YES... that ... firmer thighs!"
    $ show_picture(10, "rioleyna9")
    $ resolve_scene()
    Villager2 "You could teach us some exercise, the truth is that these last years I have neglected a lot my physique and I'm getting a lot of belly hahahaa"
    Villager "Yes! With this great body you have to know some really good exercises!"
    Leyna "W-well, you could..."
    Johan "(This situation is getting too long for my taste... but after the little speech about trust I said before, I don't want to yell at them now)"
    $ show_picture(11, "rioleyna10")
    $ resolve_scene()
    Villager2 "What? I'm sorry, but you speak very softly and I can't hear you"
    Leyna "!!! I.... I..."
    Johan "Ahem well Leyna... shall we take a bath?"
    $ show_picture(12, "rioleyna11")
    $ resolve_scene()
    Leyna "Y-yeah right (for a second I forgot Johan is here, thank good from where he is, he can't see that this man's penis is pressed on me)"
    Villager "Oh! yeah, we'd better go for a swim"
    Villager2 "Yes, you're right hahaha sorry Johan!"
    $ show_picture(13, "rioleyna12")
    $ resolve_scene()
    Leyna "!!!Oooh!"
    Villager2 "Oops! I slipped! We almost fell down Leyna! hahaha"
    Villager2 "Uf... my back is... my back is bad, hold me for a second"
    Johan "??? Are you okay?"
    Villager2 "Oh yes yes, just give me a second"
    $ show_picture(14, "rioleyna13")
    $ resolve_scene()
    Leyna "hmmmmm Ahhh... I... I..."
    Villager "What's wrong Leyna? Did you hurt yourself?"
    Leyna "(Johan is right there... and this man has stuck his dick all the way in... in front of my husband...)"
    Johan "Leyna?"
    $ show_picture(15, "rioleyna14")
    $ resolve_scene()
    "plop! "
    Villager2 "There you go... hahahah it's just that my back always gives me problems, everything ok Leyna? Sorry I fell on you"
    Leyna "(Heavy breathing) Ah ah ah ah.... yes ... all right... come on Johan... let's go for a swim"
    Johan "Sure! (for a second I thought that... anyway, it's just my imagination...)"
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
    call ChangePartyMember("Johan", True) from _call_TownFestivalNightEV143_1_ChangePartyMember
    call TransferPlayer("TownNight", "TownFestivalNightEV143_1", 47, 23, direction=4) from _call_TownFestivalNightEV143_1_TransferPlayer_2
    $ fade_in()
    call Movement("TownFestivalNightEV143_1", "player", ["L","L","L","TURN_R"]) from _call_TownFestivalNightEV143_1_Movement_2
    $ resolve_scene()
    Johan "It looks like everyone has already gone to sleep... We better go to sleep too"
    Leyna "Yes... you are right"
    $ fade_out()
    call TransferPlayer("Town2", "TownFestivalNightEV143_1", 28, 22, direction=0) from _call_TownFestivalNightEV143_1_TransferPlayer_3
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ fade_in()
    $ resolve_scene()
    "The next morning..."
    $ erase_picture(1)
    call Movement("TownFestivalNightEV143_1", "player", ["D","TURN_U"]) from _call_TownFestivalNightEV143_1_Movement_3
    $ resolve_scene()
    Johan "My God, I have a terrible hangover, I can hardly remember what happened yesterday"
    Johan "... We were on the river with some guys, right? I hope we didn't do anything crazy"
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Oh hahaha... Right... no, relax we didn't do anything crazy...I don't remember much either...I also have a good hangover hahaha"
    Johan "Yeah... Well, what do you feel like doing today?"
    Leyna "The truth is that I should stop by my work at the hotsprings... but I can come by later"
    Johan "Don't worry, I could use a hot bath, I could walk you over there and take a bath and then I'll do some time while you finish up"
    Leyna "You don't have to if you don't want to..."
    Johan "Don't worry! It's not a problem!"
    Leyna "W-well, let's go there"
    $ erase_picture(1)
    $ resolve_scene()
    return False

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v2(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v2"):
        return None
    elif trigger == "event" and hiding_place >= 4:
        call PlayEvent(play_event, "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v2_1", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v2") from _call_TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v2_1_PlayEvent
        return (0, "", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v2_1")
    elif trigger == "event" and hiding_place >= 3:
        call PlayEvent(play_event, "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v2_0", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v2") from _call_TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v2_0_PlayEvent
        return (0, "", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v2_0")
    return None

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v3_0:
    call PauseForBalloon("TownFestivalNightEV144_0") from _call_TownFestivalNightEV144_0_PauseForBalloon
    Leyna "I should look for Johan, this game has gone longer than I'd like"
    $ fade_out()
    $ set_switch("final_hideout", True)
    call GalleryViewed("rioleyna") from _call_TownFestivalNightEV144_0_GalleryViewed
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV144_0", 15, 10, direction=4) from _call_TownFestivalNightEV144_0_TransferPlayer
    $ fade_in()
    call Movement("TownFestivalNightEV144_0", "player", ["L","L","L","L","L","U","U","L","L","L"]) from _call_TownFestivalNightEV144_0_Movement
    call Movement("TownFestivalNightEV144_0", "TownFestivalNightjohan2", ["TURN_R"]) from _call_TownFestivalNightEV144_0_Movement_1
    $ resolve_scene()
    call PauseForBalloon("TownFestivalNightEV144_0") from _call_TownFestivalNightEV144_0_PauseForBalloon_1
    Johan "Leyna! I was starting to worry, I couldn't find you anywhere, everything all right?"
    Leyna "Hmm yes... everything... everything is fine! Well... Shall we go to sleep? I'm exhausted"
    Johan "Exhausted? But the night just started! We met some villagers and they invited us for a drink!"
    Alexa "Exactly Leyna! I'm sure you'll have a great time! Let's have a few beers and I'm sure you'll get over your tiredness!"
    Leyna "I don't feel like it guys..."
    Johan "Come on Leyna, it will be fun, we have worked hard these days, we deserve a night out!"
    Leyna "Okay guys... let's have a couple of beers"
    Alexa "Good!! We're meeting them for a drink nearby"
    $ fade_out()
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV144_0", 44, 39, direction=2) from _call_TownFestivalNightEV144_0_TransferPlayer_1
    call SetEventLocation("TownFestivalNightEV144_0", "TownFestivalNightalexa2", 43, 39) from _call_TownFestivalNightEV144_0_setloc
    call SetEventLocation("TownFestivalNightEV144_0", "TownFestivalNightmarido2", 43, 40) from _call_TownFestivalNightEV144_0_setloc_1
    call SetEventLocation("TownFestivalNightEV144_0", "TownFestivalNightjohan2", 45, 39) from _call_TownFestivalNightEV144_0_setloc_2
    $ fade_in()
    $ resolve_scene()
    Alexa "We are here! Did you get the beers?"
    Villager "Yes, we have plenty for the whole night"
    Johan "Great! It's been years since I've been out partying!"
    Villager2 "(Wow how lucky we are! We finally convinced the two tourist girls to come and drink! we have to make the most of it)"
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(SEVERAL BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "No, but seriously Johan, your wife is beautiful, I don't know how you can live in peace"
    Johan "Well (ugh I'm so drunk) let's see... I believe that the most important thing in a relationship is trust and I ... I trust Leyna completely"
    Villager "Very well said... but of course, all the festivals in this town revolve around showing off your body..."
    Villager "Aren't you worried that all the men in town will see your wife's body?"
    Leyna "W-well my body..."
    Johan "NO! I'm not worried, we were all born naked and it's completely natural!"
    Alexa "Very well said! You are absolutely right"
    AlexasHusband "..."
    Villager2 "Yeah! If you have a good body, what better than to show it off, right?"
    Johan "Well... also not..."
    Villager "Johan... you are a wise man!"
    Johan "O-okey Thank you hahaha..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(MANY MORE BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "BUah I'm pretty fucked up already... Do you know what I'm really interested in right now?"
    Leyna "Wh-hip-what do you feel like?"
    Villager "I feel like fucking"
    Leyna "!!!"
    Villager "HAHAHAHAAHA No... I really feel like going to the river to take a bath... are you in?"
    Alexa "Sure, why not? That way we can sober up a little bit"
    Johan "Yes, a cold bath would be great for me right now!"
    Leyna "But... in the river, we would all have to undress"
    Johan "Shit, true..."
    Villager "Well, as you said, it's completely natural right?"
    Johan "Well, yes..."
    Villager2 "And besides, there's trust, right Johan? It's just taking a bath and all..."
    Johan "Well, I guess you're right"
    Leyna "If JoHan AgRees, I hAve no probLem..."
    Villager "Great! (she seems to be quite drunk)"
    Johan "YES! I'm looking forward to going back to the river"
    Villager "Ehm... ahem yes, the river of course..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "LATER IN THE RIVER ..."
    Villager "Come on, everyone without clothes, otherwise the goddess will get angry"
    Johan "hahahahahaha okay let's go"
    Leyna "Okay, but give me one more shot of beer first hahaha"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV144_0_PlaySound
    $ show_picture(2, "rioleyna1")
    $ resolve_scene()
    Leyna "Ahhh how nice, how refreshing... it may be the alcohol but the truth is that being like this without worrying so much is very ... liberalizing"
    Johan "Right? Now I feel a little bad for being angry in the past"
    $ show_picture(3, "rioleyna2")
    $ resolve_scene()
    Villager "Yesssss this is all tradition here! We have no problem seeing each other naked!"
    Leyna "It's certainly very different from how we behave in the city, but I guess it's cool"
    Villager2 "Hahahahaha man, here we are all happy to see each other, especially you Leyna! What a great body!"
    Johan "hahhaha you bet! Eeven though she is my wife, I still can't get used to seeing her like this"
    $ show_picture(4, "rioleyna3")
    $ resolve_scene()
    Villager2 "Dude! You sure are glad to see Leyna!"
    Johan "Hahahaha"
    Leyna "WOW! what a big dick (!!!!!!) fu-fuck did I say that out loud? Sorry...."
    Leyna "When I drink too much I'm not myself"
    Johan "Hahaha...(Wow I didn't expect that comment from Leyna ... even though she told the truth I can't help but feel jealous... I have a weird feeling in my stomach"
    "looking at this situation... I don't know if it's because of the alcohol but... well, don't think about it too much Johan)"
    $ show_picture(5, "rioleyna4")
    $ resolve_scene()
    Villager2 "Well Leyna don't worry here we are all friends and there is trust, isn't it Johan?"
    Johan "Of course! You can admire my wife's beauty all you want! After all it's only for me hahahaha"
    Villager2 "But man, don't tell us that, we'll die of envy! hahahaha"
    Leyna "Well, I think I'm going to take a bath guys!"
    $ show_picture(6, "rioleyna5")
    $ resolve_scene()
    Villager "Wait, you're going to go like that? You should strip completely naked or you'll get your panties wet and get cold"
    Leyna "I'm just a little embarrassed, guys"
    Villager "Don't worry, we are all adults here!"
    Villager2 "Yes, we're not going to see anything we haven't seen before"
    Leyna "I guess you are right"
    $ show_picture(6, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    Johan "W-well, I don't know..."
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV144_0_PlaySound_1
    Johan "!!!!"
    Villager "Wow! Awesome! Leyna do you exercise or something?"
    Leyna "Well... I do go to the gym every week"
    Villager "Very well, let's see!"
    call PlaySound("sound", "audio/Fall.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV144_0_PlaySound_2
    Leyna "!!!"
    $ show_picture(7, "rioleyna6")
    $ resolve_scene()
    Villager "It really shows! You have a great ass! And what kind of exercises do you do at the gym?"
    Johan "Hey hey!"
    Villager "Some cycling perhaps?"
    $ show_picture(8, "rioleyna7")
    $ resolve_scene()
    Leyna "Y-yes some biking... and some rubber exercises"
    Johan "(They're ignoring me? It's like I'm not even here... and Leyna...)"
    Johan "(The penis of this man we met just is soo close to Leyna's pussy)"
    Villager2 "Wow! May I see it?"
    $ show_picture(9, "rioleyna8")
    $ resolve_scene()
    Villager "Of course, look at her thighs! She's a real sportswoman!"
    Leyna "hm!"
    Villager2 "YES... that ... firmer thighs!"
    $ show_picture(10, "rioleyna9")
    $ resolve_scene()
    Villager2 "You could teach us some exercise, the truth is that these last years I have neglected a lot my physique and I'm getting a lot of belly hahahaa"
    Villager "Yes! With this great body you have to know some really good exercises!"
    Leyna "W-well, you could..."
    Johan "(This situation is getting too long for my taste... but after the little speech about trust I said before, I don't want to yell at them now)"
    $ show_picture(11, "rioleyna10")
    $ resolve_scene()
    Villager2 "What? I'm sorry, but you speak very softly and I can't hear you"
    Leyna "!!! I.... I..."
    Johan "Ahem well Leyna... shall we take a bath?"
    $ show_picture(12, "rioleyna11")
    $ resolve_scene()
    Leyna "Y-yeah right (for a second I forgot Johan is here, thank good from where he is, he can't see that this man's penis is pressed on me)"
    Villager "Oh! yeah, we'd better go for a swim"
    Villager2 "Yes, you're right hahaha sorry Johan!"
    $ show_picture(13, "rioleyna12")
    $ resolve_scene()
    Leyna "!!!Oooh!"
    Villager2 "Oops! I slipped! We almost fell down Leyna! hahaha"
    Villager2 "Uf... my back is... my back is bad, hold me for a second"
    Johan "??? Are you okay?"
    Villager2 "Oh yes yes, just give me a second"
    $ show_picture(14, "rioleyna13")
    $ resolve_scene()
    Leyna "hmmmmm Ahhh... I... I..."
    Villager "What's wrong Leyna? Did you hurt yourself?"
    Leyna "(Johan is right there... and this man has stuck his dick all the way in... in front of my husband...)"
    Johan "Leyna?"
    $ show_picture(15, "rioleyna14")
    $ resolve_scene()
    "plop! "
    Villager2 "There you go... hahahah it's just that my back always gives me problems, everything ok Leyna? Sorry I fell on you"
    Leyna "(Heavy breathing) Ah ah ah ah.... yes ... all right... come on Johan... let's go for a swim"
    Johan "Sure! (for a second I thought that... anyway, it's just my imagination...)"
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
    call ChangePartyMember("Johan", True) from _call_TownFestivalNightEV144_0_ChangePartyMember
    call TransferPlayer("TownNight", "TownFestivalNightEV144_0", 47, 23, direction=4) from _call_TownFestivalNightEV144_0_TransferPlayer_2
    $ fade_in()
    call Movement("TownFestivalNightEV144_0", "player", ["L","L","L","TURN_R"]) from _call_TownFestivalNightEV144_0_Movement_2
    $ resolve_scene()
    Johan "It looks like everyone has already gone to sleep... We better go to sleep too"
    Leyna "Yes... you are right"
    $ fade_out()
    call TransferPlayer("Town2", "TownFestivalNightEV144_0", 28, 22, direction=0) from _call_TownFestivalNightEV144_0_TransferPlayer_3
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ fade_in()
    $ resolve_scene()
    "The next morning..."
    $ erase_picture(1)
    call Movement("TownFestivalNightEV144_0", "player", ["D","TURN_U"]) from _call_TownFestivalNightEV144_0_Movement_3
    $ resolve_scene()
    Johan "My God, I have a terrible hangover, I can hardly remember what happened yesterday"
    Johan "... We were on the river with some guys, right? I hope we didn't do anything crazy"
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Oh hahaha... Right... no, relax we didn't do anything crazy...I don't remember much either...I also have a good hangover hahaha"
    Johan "Yeah... Well, what do you feel like doing today?"
    Leyna "The truth is that I should stop by my work at the hotsprings... but I can come by later"
    Johan "Don't worry, I could use a hot bath, I could walk you over there and take a bath and then I'll do some time while you finish up"
    Leyna "You don't have to if you don't want to..."
    Johan "Don't worry! It's not a problem!"
    Leyna "W-well, let's go there"
    $ erase_picture(1)
    $ resolve_scene()
    return False

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v3_1:
    call PauseForBalloon("TownFestivalNightEV144_1") from _call_TownFestivalNightEV144_1_PauseForBalloon
    Leyna "I should look for Johan, this game has gone longer than I'd like"
    $ fade_out()
    $ set_switch("final_hideout", True)
    call GalleryViewed("rioleyna") from _call_TownFestivalNightEV144_1_GalleryViewed
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV144_1", 15, 10, direction=4) from _call_TownFestivalNightEV144_1_TransferPlayer
    $ fade_in()
    call Movement("TownFestivalNightEV144_1", "player", ["L","L","L","L","L","U","U","L","L","L"]) from _call_TownFestivalNightEV144_1_Movement
    call Movement("TownFestivalNightEV144_1", "TownFestivalNightjohan2", ["TURN_R"]) from _call_TownFestivalNightEV144_1_Movement_1
    $ resolve_scene()
    call PauseForBalloon("TownFestivalNightEV144_1") from _call_TownFestivalNightEV144_1_PauseForBalloon_1
    Johan "Leyna! I was starting to worry, I couldn't find you anywhere, everything all right?"
    Leyna "Hmm yes... everything... everything is fine! Well... Shall we go to sleep? I'm exhausted"
    Johan "Exhausted? But the night just started! We met some villagers and they invited us for a drink!"
    Alexa "Exactly Leyna! I'm sure you'll have a great time! Let's have a few beers and I'm sure you'll get over your tiredness!"
    Leyna "I don't feel like it guys..."
    Johan "Come on Leyna, it will be fun, we have worked hard these days, we deserve a night out!"
    Leyna "Okay guys... let's have a couple of beers"
    Alexa "Good!! We're meeting them for a drink nearby"
    $ fade_out()
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV144_1", 44, 39, direction=2) from _call_TownFestivalNightEV144_1_TransferPlayer_1
    call SetEventLocation("TownFestivalNightEV144_1", "TownFestivalNightalexa2", 43, 39) from _call_TownFestivalNightEV144_1_setloc
    call SetEventLocation("TownFestivalNightEV144_1", "TownFestivalNightmarido2", 43, 40) from _call_TownFestivalNightEV144_1_setloc_1
    call SetEventLocation("TownFestivalNightEV144_1", "TownFestivalNightjohan2", 45, 39) from _call_TownFestivalNightEV144_1_setloc_2
    $ fade_in()
    $ resolve_scene()
    Alexa "We are here! Did you get the beers?"
    Villager "Yes, we have plenty for the whole night"
    Johan "Great! It's been years since I've been out partying!"
    Villager2 "(Wow how lucky we are! We finally convinced the two tourist girls to come and drink! we have to make the most of it)"
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(SEVERAL BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "No, but seriously Johan, your wife is beautiful, I don't know how you can live in peace"
    Johan "Well (ugh I'm so drunk) let's see... I believe that the most important thing in a relationship is trust and I ... I trust Leyna completely"
    Villager "Very well said... but of course, all the festivals in this town revolve around showing off your body..."
    Villager "Aren't you worried that all the men in town will see your wife's body?"
    Leyna "W-well my body..."
    Johan "NO! I'm not worried, we were all born naked and it's completely natural!"
    Alexa "Very well said! You are absolutely right"
    AlexasHusband "..."
    Villager2 "Yeah! If you have a good body, what better than to show it off, right?"
    Johan "Well... also not..."
    Villager "Johan... you are a wise man!"
    Johan "O-okey Thank you hahaha..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(MANY MORE BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "BUah I'm pretty fucked up already... Do you know what I'm really interested in right now?"
    Leyna "Wh-hip-what do you feel like?"
    Villager "I feel like fucking"
    Leyna "!!!"
    Villager "HAHAHAHAAHA No... I really feel like going to the river to take a bath... are you in?"
    Alexa "Sure, why not? That way we can sober up a little bit"
    Johan "Yes, a cold bath would be great for me right now!"
    Leyna "But... in the river, we would all have to undress"
    Johan "Shit, true..."
    Villager "Well, as you said, it's completely natural right?"
    Johan "Well, yes..."
    Villager2 "And besides, there's trust, right Johan? It's just taking a bath and all..."
    Johan "Well, I guess you're right"
    Leyna "If JoHan AgRees, I hAve no probLem..."
    Villager "Great! (she seems to be quite drunk)"
    Johan "YES! I'm looking forward to going back to the river"
    Villager "Ehm... ahem yes, the river of course..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "LATER IN THE RIVER ..."
    Villager "Come on, everyone without clothes, otherwise the goddess will get angry"
    Johan "hahahahahaha okay let's go"
    Leyna "Okay, but give me one more shot of beer first hahaha"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV144_1_PlaySound
    $ show_picture(2, "rioleyna1")
    $ resolve_scene()
    Leyna "Ahhh how nice, how refreshing... it may be the alcohol but the truth is that being like this without worrying so much is very ... liberalizing"
    Johan "Right? Now I feel a little bad for being angry in the past"
    $ show_picture(3, "rioleyna2")
    $ resolve_scene()
    Villager "Yesssss this is all tradition here! We have no problem seeing each other naked!"
    Leyna "It's certainly very different from how we behave in the city, but I guess it's cool"
    Villager2 "Hahahahaha man, here we are all happy to see each other, especially you Leyna! What a great body!"
    Johan "hahhaha you bet! Eeven though she is my wife, I still can't get used to seeing her like this"
    $ show_picture(4, "rioleyna3")
    $ resolve_scene()
    Villager2 "Dude! You sure are glad to see Leyna!"
    Johan "Hahahaha"
    Leyna "WOW! what a big dick (!!!!!!) fu-fuck did I say that out loud? Sorry...."
    Leyna "When I drink too much I'm not myself"
    Johan "Hahaha...(Wow I didn't expect that comment from Leyna ... even though she told the truth I can't help but feel jealous... I have a weird feeling in my stomach"
    "looking at this situation... I don't know if it's because of the alcohol but... well, don't think about it too much Johan)"
    $ show_picture(5, "rioleyna4")
    $ resolve_scene()
    Villager2 "Well Leyna don't worry here we are all friends and there is trust, isn't it Johan?"
    Johan "Of course! You can admire my wife's beauty all you want! After all it's only for me hahahaha"
    Villager2 "But man, don't tell us that, we'll die of envy! hahahaha"
    Leyna "Well, I think I'm going to take a bath guys!"
    $ show_picture(6, "rioleyna5")
    $ resolve_scene()
    Villager "Wait, you're going to go like that? You should strip completely naked or you'll get your panties wet and get cold"
    Leyna "I'm just a little embarrassed, guys"
    Villager "Don't worry, we are all adults here!"
    Villager2 "Yes, we're not going to see anything we haven't seen before"
    Leyna "I guess you are right"
    $ show_picture(6, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    Johan "W-well, I don't know..."
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV144_1_PlaySound_1
    Johan "!!!!"
    Villager "Wow! Awesome! Leyna do you exercise or something?"
    Leyna "Well... I do go to the gym every week"
    Villager "Very well, let's see!"
    call PlaySound("sound", "audio/Fall.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV144_1_PlaySound_2
    Leyna "!!!"
    $ show_picture(7, "rioleyna6")
    $ resolve_scene()
    Villager "It really shows! You have a great ass! And what kind of exercises do you do at the gym?"
    Johan "Hey hey!"
    Villager "Some cycling perhaps?"
    $ show_picture(8, "rioleyna7")
    $ resolve_scene()
    Leyna "Y-yes some biking... and some rubber exercises"
    Johan "(They're ignoring me? It's like I'm not even here... and Leyna...)"
    Johan "(The penis of this man we met just is soo close to Leyna's pussy)"
    Villager2 "Wow! May I see it?"
    $ show_picture(9, "rioleyna8")
    $ resolve_scene()
    Villager "Of course, look at her thighs! She's a real sportswoman!"
    Leyna "hm!"
    Villager2 "YES... that ... firmer thighs!"
    $ show_picture(10, "rioleyna9")
    $ resolve_scene()
    Villager2 "You could teach us some exercise, the truth is that these last years I have neglected a lot my physique and I'm getting a lot of belly hahahaa"
    Villager "Yes! With this great body you have to know some really good exercises!"
    Leyna "W-well, you could..."
    Johan "(This situation is getting too long for my taste... but after the little speech about trust I said before, I don't want to yell at them now)"
    $ show_picture(11, "rioleyna10")
    $ resolve_scene()
    Villager2 "What? I'm sorry, but you speak very softly and I can't hear you"
    Leyna "!!! I.... I..."
    Johan "Ahem well Leyna... shall we take a bath?"
    $ show_picture(12, "rioleyna11")
    $ resolve_scene()
    Leyna "Y-yeah right (for a second I forgot Johan is here, thank good from where he is, he can't see that this man's penis is pressed on me)"
    Villager "Oh! yeah, we'd better go for a swim"
    Villager2 "Yes, you're right hahaha sorry Johan!"
    $ show_picture(13, "rioleyna12")
    $ resolve_scene()
    Leyna "!!!Oooh!"
    Villager2 "Oops! I slipped! We almost fell down Leyna! hahaha"
    Villager2 "Uf... my back is... my back is bad, hold me for a second"
    Johan "??? Are you okay?"
    Villager2 "Oh yes yes, just give me a second"
    $ show_picture(14, "rioleyna13")
    $ resolve_scene()
    Leyna "hmmmmm Ahhh... I... I..."
    Villager "What's wrong Leyna? Did you hurt yourself?"
    Leyna "(Johan is right there... and this man has stuck his dick all the way in... in front of my husband...)"
    Johan "Leyna?"
    $ show_picture(15, "rioleyna14")
    $ resolve_scene()
    "plop! "
    Villager2 "There you go... hahahah it's just that my back always gives me problems, everything ok Leyna? Sorry I fell on you"
    Leyna "(Heavy breathing) Ah ah ah ah.... yes ... all right... come on Johan... let's go for a swim"
    Johan "Sure! (for a second I thought that... anyway, it's just my imagination...)"
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
    call ChangePartyMember("Johan", True) from _call_TownFestivalNightEV144_1_ChangePartyMember
    call TransferPlayer("TownNight", "TownFestivalNightEV144_1", 47, 23, direction=4) from _call_TownFestivalNightEV144_1_TransferPlayer_2
    $ fade_in()
    call Movement("TownFestivalNightEV144_1", "player", ["L","L","L","TURN_R"]) from _call_TownFestivalNightEV144_1_Movement_2
    $ resolve_scene()
    Johan "It looks like everyone has already gone to sleep... We better go to sleep too"
    Leyna "Yes... you are right"
    $ fade_out()
    call TransferPlayer("Town2", "TownFestivalNightEV144_1", 28, 22, direction=0) from _call_TownFestivalNightEV144_1_TransferPlayer_3
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ fade_in()
    $ resolve_scene()
    "The next morning..."
    $ erase_picture(1)
    call Movement("TownFestivalNightEV144_1", "player", ["D","TURN_U"]) from _call_TownFestivalNightEV144_1_Movement_3
    $ resolve_scene()
    Johan "My God, I have a terrible hangover, I can hardly remember what happened yesterday"
    Johan "... We were on the river with some guys, right? I hope we didn't do anything crazy"
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Oh hahaha... Right... no, relax we didn't do anything crazy...I don't remember much either...I also have a good hangover hahaha"
    Johan "Yeah... Well, what do you feel like doing today?"
    Leyna "The truth is that I should stop by my work at the hotsprings... but I can come by later"
    Johan "Don't worry, I could use a hot bath, I could walk you over there and take a bath and then I'll do some time while you finish up"
    Leyna "You don't have to if you don't want to..."
    Johan "Don't worry! It's not a problem!"
    Leyna "W-well, let's go there"
    $ erase_picture(1)
    $ resolve_scene()
    return False

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v3(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v3"):
        return None
    elif trigger == "event" and hiding_place >= 4:
        call PlayEvent(play_event, "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v3_1", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v3") from _call_TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v3_1_PlayEvent
        return (0, "", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v3_1")
    elif trigger == "event" and hiding_place >= 3:
        call PlayEvent(play_event, "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v3_0", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v3") from _call_TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v3_0_PlayEvent
        return (0, "", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v3_0")
    return None

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v4_0:
    call PauseForBalloon("TownFestivalNightEV145_0") from _call_TownFestivalNightEV145_0_PauseForBalloon
    Leyna "I should look for Johan, this game has gone longer than I'd like"
    $ fade_out()
    $ set_switch("final_hideout", True)
    call GalleryViewed("rioleyna") from _call_TownFestivalNightEV145_0_GalleryViewed
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV145_0", 15, 10, direction=4) from _call_TownFestivalNightEV145_0_TransferPlayer
    $ fade_in()
    call Movement("TownFestivalNightEV145_0", "player", ["L","L","L","L","L","U","U","L","L","L"]) from _call_TownFestivalNightEV145_0_Movement
    call Movement("TownFestivalNightEV145_0", "TownFestivalNightjohan2", ["TURN_R"]) from _call_TownFestivalNightEV145_0_Movement_1
    $ resolve_scene()
    call PauseForBalloon("TownFestivalNightEV145_0") from _call_TownFestivalNightEV145_0_PauseForBalloon_1
    Johan "Leyna! I was starting to worry, I couldn't find you anywhere, everything all right?"
    Leyna "Hmm yes... everything... everything is fine! Well... Shall we go to sleep? I'm exhausted"
    Johan "Exhausted? But the night just started! We met some villagers and they invited us for a drink!"
    Alexa "Exactly Leyna! I'm sure you'll have a great time! Let's have a few beers and I'm sure you'll get over your tiredness!"
    Leyna "I don't feel like it guys..."
    Johan "Come on Leyna, it will be fun, we have worked hard these days, we deserve a night out!"
    Leyna "Okay guys... let's have a couple of beers"
    Alexa "Good!! We're meeting them for a drink nearby"
    $ fade_out()
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV145_0", 44, 39, direction=2) from _call_TownFestivalNightEV145_0_TransferPlayer_1
    call SetEventLocation("TownFestivalNightEV145_0", "TownFestivalNightalexa2", 43, 39) from _call_TownFestivalNightEV145_0_setloc
    call SetEventLocation("TownFestivalNightEV145_0", "TownFestivalNightmarido2", 43, 40) from _call_TownFestivalNightEV145_0_setloc_1
    call SetEventLocation("TownFestivalNightEV145_0", "TownFestivalNightjohan2", 45, 39) from _call_TownFestivalNightEV145_0_setloc_2
    $ fade_in()
    $ resolve_scene()
    Alexa "We are here! Did you get the beers?"
    Villager "Yes, we have plenty for the whole night"
    Johan "Great! It's been years since I've been out partying!"
    Villager2 "(Wow how lucky we are! We finally convinced the two tourist girls to come and drink! we have to make the most of it)"
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(SEVERAL BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "No, but seriously Johan, your wife is beautiful, I don't know how you can live in peace"
    Johan "Well (ugh I'm so drunk) let's see... I believe that the most important thing in a relationship is trust and I ... I trust Leyna completely"
    Villager "Very well said... but of course, all the festivals in this town revolve around showing off your body..."
    Villager "Aren't you worried that all the men in town will see your wife's body?"
    Leyna "W-well my body..."
    Johan "NO! I'm not worried, we were all born naked and it's completely natural!"
    Alexa "Very well said! You are absolutely right"
    AlexasHusband "..."
    Villager2 "Yeah! If you have a good body, what better than to show it off, right?"
    Johan "Well... also not..."
    Villager "Johan... you are a wise man!"
    Johan "O-okey Thank you hahaha..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(MANY MORE BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "BUah I'm pretty fucked up already... Do you know what I'm really interested in right now?"
    Leyna "Wh-hip-what do you feel like?"
    Villager "I feel like fucking"
    Leyna "!!!"
    Villager "HAHAHAHAAHA No... I really feel like going to the river to take a bath... are you in?"
    Alexa "Sure, why not? That way we can sober up a little bit"
    Johan "Yes, a cold bath would be great for me right now!"
    Leyna "But... in the river, we would all have to undress"
    Johan "Shit, true..."
    Villager "Well, as you said, it's completely natural right?"
    Johan "Well, yes..."
    Villager2 "And besides, there's trust, right Johan? It's just taking a bath and all..."
    Johan "Well, I guess you're right"
    Leyna "If JoHan AgRees, I hAve no probLem..."
    Villager "Great! (she seems to be quite drunk)"
    Johan "YES! I'm looking forward to going back to the river"
    Villager "Ehm... ahem yes, the river of course..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "LATER IN THE RIVER ..."
    Villager "Come on, everyone without clothes, otherwise the goddess will get angry"
    Johan "hahahahahaha okay let's go"
    Leyna "Okay, but give me one more shot of beer first hahaha"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV145_0_PlaySound
    $ show_picture(2, "rioleyna1")
    $ resolve_scene()
    Leyna "Ahhh how nice, how refreshing... it may be the alcohol but the truth is that being like this without worrying so much is very ... liberalizing"
    Johan "Right? Now I feel a little bad for being angry in the past"
    $ show_picture(3, "rioleyna2")
    $ resolve_scene()
    Villager "Yesssss this is all tradition here! We have no problem seeing each other naked!"
    Leyna "It's certainly very different from how we behave in the city, but I guess it's cool"
    Villager2 "Hahahahaha man, here we are all happy to see each other, especially you Leyna! What a great body!"
    Johan "hahhaha you bet! Eeven though she is my wife, I still can't get used to seeing her like this"
    $ show_picture(4, "rioleyna3")
    $ resolve_scene()
    Villager2 "Dude! You sure are glad to see Leyna!"
    Johan "Hahahaha"
    Leyna "WOW! what a big dick (!!!!!!) fu-fuck did I say that out loud? Sorry...."
    Leyna "When I drink too much I'm not myself"
    Johan "Hahaha...(Wow I didn't expect that comment from Leyna ... even though she told the truth I can't help but feel jealous... I have a weird feeling in my stomach"
    "looking at this situation... I don't know if it's because of the alcohol but... well, don't think about it too much Johan)"
    $ show_picture(5, "rioleyna4")
    $ resolve_scene()
    Villager2 "Well Leyna don't worry here we are all friends and there is trust, isn't it Johan?"
    Johan "Of course! You can admire my wife's beauty all you want! After all it's only for me hahahaha"
    Villager2 "But man, don't tell us that, we'll die of envy! hahahaha"
    Leyna "Well, I think I'm going to take a bath guys!"
    $ show_picture(6, "rioleyna5")
    $ resolve_scene()
    Villager "Wait, you're going to go like that? You should strip completely naked or you'll get your panties wet and get cold"
    Leyna "I'm just a little embarrassed, guys"
    Villager "Don't worry, we are all adults here!"
    Villager2 "Yes, we're not going to see anything we haven't seen before"
    Leyna "I guess you are right"
    $ show_picture(6, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    Johan "W-well, I don't know..."
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV145_0_PlaySound_1
    Johan "!!!!"
    Villager "Wow! Awesome! Leyna do you exercise or something?"
    Leyna "Well... I do go to the gym every week"
    Villager "Very well, let's see!"
    call PlaySound("sound", "audio/Fall.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV145_0_PlaySound_2
    Leyna "!!!"
    $ show_picture(7, "rioleyna6")
    $ resolve_scene()
    Villager "It really shows! You have a great ass! And what kind of exercises do you do at the gym?"
    Johan "Hey hey!"
    Villager "Some cycling perhaps?"
    $ show_picture(8, "rioleyna7")
    $ resolve_scene()
    Leyna "Y-yes some biking... and some rubber exercises"
    Johan "(They're ignoring me? It's like I'm not even here... and Leyna...)"
    Johan "(The penis of this man we met just is soo close to Leyna's pussy)"
    Villager2 "Wow! May I see it?"
    $ show_picture(9, "rioleyna8")
    $ resolve_scene()
    Villager "Of course, look at her thighs! She's a real sportswoman!"
    Leyna "hm!"
    Villager2 "YES... that ... firmer thighs!"
    $ show_picture(10, "rioleyna9")
    $ resolve_scene()
    Villager2 "You could teach us some exercise, the truth is that these last years I have neglected a lot my physique and I'm getting a lot of belly hahahaa"
    Villager "Yes! With this great body you have to know some really good exercises!"
    Leyna "W-well, you could..."
    Johan "(This situation is getting too long for my taste... but after the little speech about trust I said before, I don't want to yell at them now)"
    $ show_picture(11, "rioleyna10")
    $ resolve_scene()
    Villager2 "What? I'm sorry, but you speak very softly and I can't hear you"
    Leyna "!!! I.... I..."
    Johan "Ahem well Leyna... shall we take a bath?"
    $ show_picture(12, "rioleyna11")
    $ resolve_scene()
    Leyna "Y-yeah right (for a second I forgot Johan is here, thank good from where he is, he can't see that this man's penis is pressed on me)"
    Villager "Oh! yeah, we'd better go for a swim"
    Villager2 "Yes, you're right hahaha sorry Johan!"
    $ show_picture(13, "rioleyna12")
    $ resolve_scene()
    Leyna "!!!Oooh!"
    Villager2 "Oops! I slipped! We almost fell down Leyna! hahaha"
    Villager2 "Uf... my back is... my back is bad, hold me for a second"
    Johan "??? Are you okay?"
    Villager2 "Oh yes yes, just give me a second"
    $ show_picture(14, "rioleyna13")
    $ resolve_scene()
    Leyna "hmmmmm Ahhh... I... I..."
    Villager "What's wrong Leyna? Did you hurt yourself?"
    Leyna "(Johan is right there... and this man has stuck his dick all the way in... in front of my husband...)"
    Johan "Leyna?"
    $ show_picture(15, "rioleyna14")
    $ resolve_scene()
    "plop! "
    Villager2 "There you go... hahahah it's just that my back always gives me problems, everything ok Leyna? Sorry I fell on you"
    Leyna "(Heavy breathing) Ah ah ah ah.... yes ... all right... come on Johan... let's go for a swim"
    Johan "Sure! (for a second I thought that... anyway, it's just my imagination...)"
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
    call ChangePartyMember("Johan", True) from _call_TownFestivalNightEV145_0_ChangePartyMember
    call TransferPlayer("TownNight", "TownFestivalNightEV145_0", 47, 23, direction=4) from _call_TownFestivalNightEV145_0_TransferPlayer_2
    $ fade_in()
    call Movement("TownFestivalNightEV145_0", "player", ["L","L","L","TURN_R"]) from _call_TownFestivalNightEV145_0_Movement_2
    $ resolve_scene()
    Johan "It looks like everyone has already gone to sleep... We better go to sleep too"
    Leyna "Yes... you are right"
    $ fade_out()
    call TransferPlayer("Town2", "TownFestivalNightEV145_0", 28, 22, direction=0) from _call_TownFestivalNightEV145_0_TransferPlayer_3
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ fade_in()
    $ resolve_scene()
    "The next morning..."
    $ erase_picture(1)
    call Movement("TownFestivalNightEV145_0", "player", ["D","TURN_U"]) from _call_TownFestivalNightEV145_0_Movement_3
    $ resolve_scene()
    Johan "My God, I have a terrible hangover, I can hardly remember what happened yesterday"
    Johan "... We were on the river with some guys, right? I hope we didn't do anything crazy"
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Oh hahaha... Right... no, relax we didn't do anything crazy...I don't remember much either...I also have a good hangover hahaha"
    Johan "Yeah... Well, what do you feel like doing today?"
    Leyna "The truth is that I should stop by my work at the hotsprings... but I can come by later"
    Johan "Don't worry, I could use a hot bath, I could walk you over there and take a bath and then I'll do some time while you finish up"
    Leyna "You don't have to if you don't want to..."
    Johan "Don't worry! It's not a problem!"
    Leyna "W-well, let's go there"
    $ erase_picture(1)
    $ resolve_scene()
    return False

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v4_1:
    call PauseForBalloon("TownFestivalNightEV145_1") from _call_TownFestivalNightEV145_1_PauseForBalloon
    Leyna "I should look for Johan, this game has gone longer than I'd like"
    $ fade_out()
    $ set_switch("final_hideout", True)
    call GalleryViewed("rioleyna") from _call_TownFestivalNightEV145_1_GalleryViewed
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV145_1", 15, 10, direction=4) from _call_TownFestivalNightEV145_1_TransferPlayer
    $ fade_in()
    call Movement("TownFestivalNightEV145_1", "player", ["L","L","L","L","L","U","U","L","L","L"]) from _call_TownFestivalNightEV145_1_Movement
    call Movement("TownFestivalNightEV145_1", "TownFestivalNightjohan2", ["TURN_R"]) from _call_TownFestivalNightEV145_1_Movement_1
    $ resolve_scene()
    call PauseForBalloon("TownFestivalNightEV145_1") from _call_TownFestivalNightEV145_1_PauseForBalloon_1
    Johan "Leyna! I was starting to worry, I couldn't find you anywhere, everything all right?"
    Leyna "Hmm yes... everything... everything is fine! Well... Shall we go to sleep? I'm exhausted"
    Johan "Exhausted? But the night just started! We met some villagers and they invited us for a drink!"
    Alexa "Exactly Leyna! I'm sure you'll have a great time! Let's have a few beers and I'm sure you'll get over your tiredness!"
    Leyna "I don't feel like it guys..."
    Johan "Come on Leyna, it will be fun, we have worked hard these days, we deserve a night out!"
    Leyna "Okay guys... let's have a couple of beers"
    Alexa "Good!! We're meeting them for a drink nearby"
    $ fade_out()
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV145_1", 44, 39, direction=2) from _call_TownFestivalNightEV145_1_TransferPlayer_1
    call SetEventLocation("TownFestivalNightEV145_1", "TownFestivalNightalexa2", 43, 39) from _call_TownFestivalNightEV145_1_setloc
    call SetEventLocation("TownFestivalNightEV145_1", "TownFestivalNightmarido2", 43, 40) from _call_TownFestivalNightEV145_1_setloc_1
    call SetEventLocation("TownFestivalNightEV145_1", "TownFestivalNightjohan2", 45, 39) from _call_TownFestivalNightEV145_1_setloc_2
    $ fade_in()
    $ resolve_scene()
    Alexa "We are here! Did you get the beers?"
    Villager "Yes, we have plenty for the whole night"
    Johan "Great! It's been years since I've been out partying!"
    Villager2 "(Wow how lucky we are! We finally convinced the two tourist girls to come and drink! we have to make the most of it)"
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(SEVERAL BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "No, but seriously Johan, your wife is beautiful, I don't know how you can live in peace"
    Johan "Well (ugh I'm so drunk) let's see... I believe that the most important thing in a relationship is trust and I ... I trust Leyna completely"
    Villager "Very well said... but of course, all the festivals in this town revolve around showing off your body..."
    Villager "Aren't you worried that all the men in town will see your wife's body?"
    Leyna "W-well my body..."
    Johan "NO! I'm not worried, we were all born naked and it's completely natural!"
    Alexa "Very well said! You are absolutely right"
    AlexasHusband "..."
    Villager2 "Yeah! If you have a good body, what better than to show it off, right?"
    Johan "Well... also not..."
    Villager "Johan... you are a wise man!"
    Johan "O-okey Thank you hahaha..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(MANY MORE BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "BUah I'm pretty fucked up already... Do you know what I'm really interested in right now?"
    Leyna "Wh-hip-what do you feel like?"
    Villager "I feel like fucking"
    Leyna "!!!"
    Villager "HAHAHAHAAHA No... I really feel like going to the river to take a bath... are you in?"
    Alexa "Sure, why not? That way we can sober up a little bit"
    Johan "Yes, a cold bath would be great for me right now!"
    Leyna "But... in the river, we would all have to undress"
    Johan "Shit, true..."
    Villager "Well, as you said, it's completely natural right?"
    Johan "Well, yes..."
    Villager2 "And besides, there's trust, right Johan? It's just taking a bath and all..."
    Johan "Well, I guess you're right"
    Leyna "If JoHan AgRees, I hAve no probLem..."
    Villager "Great! (she seems to be quite drunk)"
    Johan "YES! I'm looking forward to going back to the river"
    Villager "Ehm... ahem yes, the river of course..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "LATER IN THE RIVER ..."
    Villager "Come on, everyone without clothes, otherwise the goddess will get angry"
    Johan "hahahahahaha okay let's go"
    Leyna "Okay, but give me one more shot of beer first hahaha"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV145_1_PlaySound
    $ show_picture(2, "rioleyna1")
    $ resolve_scene()
    Leyna "Ahhh how nice, how refreshing... it may be the alcohol but the truth is that being like this without worrying so much is very ... liberalizing"
    Johan "Right? Now I feel a little bad for being angry in the past"
    $ show_picture(3, "rioleyna2")
    $ resolve_scene()
    Villager "Yesssss this is all tradition here! We have no problem seeing each other naked!"
    Leyna "It's certainly very different from how we behave in the city, but I guess it's cool"
    Villager2 "Hahahahaha man, here we are all happy to see each other, especially you Leyna! What a great body!"
    Johan "hahhaha you bet! Eeven though she is my wife, I still can't get used to seeing her like this"
    $ show_picture(4, "rioleyna3")
    $ resolve_scene()
    Villager2 "Dude! You sure are glad to see Leyna!"
    Johan "Hahahaha"
    Leyna "WOW! what a big dick (!!!!!!) fu-fuck did I say that out loud? Sorry...."
    Leyna "When I drink too much I'm not myself"
    Johan "Hahaha...(Wow I didn't expect that comment from Leyna ... even though she told the truth I can't help but feel jealous... I have a weird feeling in my stomach"
    "looking at this situation... I don't know if it's because of the alcohol but... well, don't think about it too much Johan)"
    $ show_picture(5, "rioleyna4")
    $ resolve_scene()
    Villager2 "Well Leyna don't worry here we are all friends and there is trust, isn't it Johan?"
    Johan "Of course! You can admire my wife's beauty all you want! After all it's only for me hahahaha"
    Villager2 "But man, don't tell us that, we'll die of envy! hahahaha"
    Leyna "Well, I think I'm going to take a bath guys!"
    $ show_picture(6, "rioleyna5")
    $ resolve_scene()
    Villager "Wait, you're going to go like that? You should strip completely naked or you'll get your panties wet and get cold"
    Leyna "I'm just a little embarrassed, guys"
    Villager "Don't worry, we are all adults here!"
    Villager2 "Yes, we're not going to see anything we haven't seen before"
    Leyna "I guess you are right"
    $ show_picture(6, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    Johan "W-well, I don't know..."
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV145_1_PlaySound_1
    Johan "!!!!"
    Villager "Wow! Awesome! Leyna do you exercise or something?"
    Leyna "Well... I do go to the gym every week"
    Villager "Very well, let's see!"
    call PlaySound("sound", "audio/Fall.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV145_1_PlaySound_2
    Leyna "!!!"
    $ show_picture(7, "rioleyna6")
    $ resolve_scene()
    Villager "It really shows! You have a great ass! And what kind of exercises do you do at the gym?"
    Johan "Hey hey!"
    Villager "Some cycling perhaps?"
    $ show_picture(8, "rioleyna7")
    $ resolve_scene()
    Leyna "Y-yes some biking... and some rubber exercises"
    Johan "(They're ignoring me? It's like I'm not even here... and Leyna...)"
    Johan "(The penis of this man we met just is soo close to Leyna's pussy)"
    Villager2 "Wow! May I see it?"
    $ show_picture(9, "rioleyna8")
    $ resolve_scene()
    Villager "Of course, look at her thighs! She's a real sportswoman!"
    Leyna "hm!"
    Villager2 "YES... that ... firmer thighs!"
    $ show_picture(10, "rioleyna9")
    $ resolve_scene()
    Villager2 "You could teach us some exercise, the truth is that these last years I have neglected a lot my physique and I'm getting a lot of belly hahahaa"
    Villager "Yes! With this great body you have to know some really good exercises!"
    Leyna "W-well, you could..."
    Johan "(This situation is getting too long for my taste... but after the little speech about trust I said before, I don't want to yell at them now)"
    $ show_picture(11, "rioleyna10")
    $ resolve_scene()
    Villager2 "What? I'm sorry, but you speak very softly and I can't hear you"
    Leyna "!!! I.... I..."
    Johan "Ahem well Leyna... shall we take a bath?"
    $ show_picture(12, "rioleyna11")
    $ resolve_scene()
    Leyna "Y-yeah right (for a second I forgot Johan is here, thank good from where he is, he can't see that this man's penis is pressed on me)"
    Villager "Oh! yeah, we'd better go for a swim"
    Villager2 "Yes, you're right hahaha sorry Johan!"
    $ show_picture(13, "rioleyna12")
    $ resolve_scene()
    Leyna "!!!Oooh!"
    Villager2 "Oops! I slipped! We almost fell down Leyna! hahaha"
    Villager2 "Uf... my back is... my back is bad, hold me for a second"
    Johan "??? Are you okay?"
    Villager2 "Oh yes yes, just give me a second"
    $ show_picture(14, "rioleyna13")
    $ resolve_scene()
    Leyna "hmmmmm Ahhh... I... I..."
    Villager "What's wrong Leyna? Did you hurt yourself?"
    Leyna "(Johan is right there... and this man has stuck his dick all the way in... in front of my husband...)"
    Johan "Leyna?"
    $ show_picture(15, "rioleyna14")
    $ resolve_scene()
    "plop! "
    Villager2 "There you go... hahahah it's just that my back always gives me problems, everything ok Leyna? Sorry I fell on you"
    Leyna "(Heavy breathing) Ah ah ah ah.... yes ... all right... come on Johan... let's go for a swim"
    Johan "Sure! (for a second I thought that... anyway, it's just my imagination...)"
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
    call ChangePartyMember("Johan", True) from _call_TownFestivalNightEV145_1_ChangePartyMember
    call TransferPlayer("TownNight", "TownFestivalNightEV145_1", 47, 23, direction=4) from _call_TownFestivalNightEV145_1_TransferPlayer_2
    $ fade_in()
    call Movement("TownFestivalNightEV145_1", "player", ["L","L","L","TURN_R"]) from _call_TownFestivalNightEV145_1_Movement_2
    $ resolve_scene()
    Johan "It looks like everyone has already gone to sleep... We better go to sleep too"
    Leyna "Yes... you are right"
    $ fade_out()
    call TransferPlayer("Town2", "TownFestivalNightEV145_1", 28, 22, direction=0) from _call_TownFestivalNightEV145_1_TransferPlayer_3
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ fade_in()
    $ resolve_scene()
    "The next morning..."
    $ erase_picture(1)
    call Movement("TownFestivalNightEV145_1", "player", ["D","TURN_U"]) from _call_TownFestivalNightEV145_1_Movement_3
    $ resolve_scene()
    Johan "My God, I have a terrible hangover, I can hardly remember what happened yesterday"
    Johan "... We were on the river with some guys, right? I hope we didn't do anything crazy"
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Oh hahaha... Right... no, relax we didn't do anything crazy...I don't remember much either...I also have a good hangover hahaha"
    Johan "Yeah... Well, what do you feel like doing today?"
    Leyna "The truth is that I should stop by my work at the hotsprings... but I can come by later"
    Johan "Don't worry, I could use a hot bath, I could walk you over there and take a bath and then I'll do some time while you finish up"
    Leyna "You don't have to if you don't want to..."
    Johan "Don't worry! It's not a problem!"
    Leyna "W-well, let's go there"
    $ erase_picture(1)
    $ resolve_scene()
    return False

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v4(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v4"):
        return None
    elif trigger == "event" and hiding_place >= 4:
        call PlayEvent(play_event, "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v4_1", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v4") from _call_TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v4_1_PlayEvent
        return (0, "", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v4_1")
    elif trigger == "event" and hiding_place >= 3:
        call PlayEvent(play_event, "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v4_0", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v4") from _call_TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v4_0_PlayEvent
        return (0, "", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v4_0")
    return None

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v5_0:
    call PauseForBalloon("TownFestivalNightEV146_0") from _call_TownFestivalNightEV146_0_PauseForBalloon
    Leyna "I should look for Johan, this game has gone longer than I'd like"
    $ fade_out()
    $ set_switch("final_hideout", True)
    call GalleryViewed("rioleyna") from _call_TownFestivalNightEV146_0_GalleryViewed
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV146_0", 15, 10, direction=4) from _call_TownFestivalNightEV146_0_TransferPlayer
    $ fade_in()
    call Movement("TownFestivalNightEV146_0", "player", ["L","L","L","L","L","U","U","L","L","L"]) from _call_TownFestivalNightEV146_0_Movement
    call Movement("TownFestivalNightEV146_0", "TownFestivalNightjohan2", ["TURN_R"]) from _call_TownFestivalNightEV146_0_Movement_1
    $ resolve_scene()
    call PauseForBalloon("TownFestivalNightEV146_0") from _call_TownFestivalNightEV146_0_PauseForBalloon_1
    Johan "Leyna! I was starting to worry, I couldn't find you anywhere, everything all right?"
    Leyna "Hmm yes... everything... everything is fine! Well... Shall we go to sleep? I'm exhausted"
    Johan "Exhausted? But the night just started! We met some villagers and they invited us for a drink!"
    Alexa "Exactly Leyna! I'm sure you'll have a great time! Let's have a few beers and I'm sure you'll get over your tiredness!"
    Leyna "I don't feel like it guys..."
    Johan "Come on Leyna, it will be fun, we have worked hard these days, we deserve a night out!"
    Leyna "Okay guys... let's have a couple of beers"
    Alexa "Good!! We're meeting them for a drink nearby"
    $ fade_out()
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV146_0", 44, 39, direction=2) from _call_TownFestivalNightEV146_0_TransferPlayer_1
    call SetEventLocation("TownFestivalNightEV146_0", "TownFestivalNightalexa2", 43, 39) from _call_TownFestivalNightEV146_0_setloc
    call SetEventLocation("TownFestivalNightEV146_0", "TownFestivalNightmarido2", 43, 40) from _call_TownFestivalNightEV146_0_setloc_1
    call SetEventLocation("TownFestivalNightEV146_0", "TownFestivalNightjohan2", 45, 39) from _call_TownFestivalNightEV146_0_setloc_2
    $ fade_in()
    $ resolve_scene()
    Alexa "We are here! Did you get the beers?"
    Villager "Yes, we have plenty for the whole night"
    Johan "Great! It's been years since I've been out partying!"
    Villager2 "(Wow how lucky we are! We finally convinced the two tourist girls to come and drink! we have to make the most of it)"
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(SEVERAL BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "No, but seriously Johan, your wife is beautiful, I don't know how you can live in peace"
    Johan "Well (ugh I'm so drunk) let's see... I believe that the most important thing in a relationship is trust and I ... I trust Leyna completely"
    Villager "Very well said... but of course, all the festivals in this town revolve around showing off your body..."
    Villager "Aren't you worried that all the men in town will see your wife's body?"
    Leyna "W-well my body..."
    Johan "NO! I'm not worried, we were all born naked and it's completely natural!"
    Alexa "Very well said! You are absolutely right"
    AlexasHusband "..."
    Villager2 "Yeah! If you have a good body, what better than to show it off, right?"
    Johan "Well... also not..."
    Villager "Johan... you are a wise man!"
    Johan "O-okey Thank you hahaha..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(MANY MORE BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "BUah I'm pretty fucked up already... Do you know what I'm really interested in right now?"
    Leyna "Wh-hip-what do you feel like?"
    Villager "I feel like fucking"
    Leyna "!!!"
    Villager "HAHAHAHAAHA No... I really feel like going to the river to take a bath... are you in?"
    Alexa "Sure, why not? That way we can sober up a little bit"
    Johan "Yes, a cold bath would be great for me right now!"
    Leyna "But... in the river, we would all have to undress"
    Johan "Shit, true..."
    Villager "Well, as you said, it's completely natural right?"
    Johan "Well, yes..."
    Villager2 "And besides, there's trust, right Johan? It's just taking a bath and all..."
    Johan "Well, I guess you're right"
    Leyna "If JoHan AgRees, I hAve no probLem..."
    Villager "Great! (she seems to be quite drunk)"
    Johan "YES! I'm looking forward to going back to the river"
    Villager "Ehm... ahem yes, the river of course..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "LATER IN THE RIVER ..."
    Villager "Come on, everyone without clothes, otherwise the goddess will get angry"
    Johan "hahahahahaha okay let's go"
    Leyna "Okay, but give me one more shot of beer first hahaha"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV146_0_PlaySound
    $ show_picture(2, "rioleyna1")
    $ resolve_scene()
    Leyna "Ahhh how nice, how refreshing... it may be the alcohol but the truth is that being like this without worrying so much is very ... liberalizing"
    Johan "Right? Now I feel a little bad for being angry in the past"
    $ show_picture(3, "rioleyna2")
    $ resolve_scene()
    Villager "Yesssss this is all tradition here! We have no problem seeing each other naked!"
    Leyna "It's certainly very different from how we behave in the city, but I guess it's cool"
    Villager2 "Hahahahaha man, here we are all happy to see each other, especially you Leyna! What a great body!"
    Johan "hahhaha you bet! Eeven though she is my wife, I still can't get used to seeing her like this"
    $ show_picture(4, "rioleyna3")
    $ resolve_scene()
    Villager2 "Dude! You sure are glad to see Leyna!"
    Johan "Hahahaha"
    Leyna "WOW! what a big dick (!!!!!!) fu-fuck did I say that out loud? Sorry...."
    Leyna "When I drink too much I'm not myself"
    Johan "Hahaha...(Wow I didn't expect that comment from Leyna ... even though she told the truth I can't help but feel jealous... I have a weird feeling in my stomach"
    "looking at this situation... I don't know if it's because of the alcohol but... well, don't think about it too much Johan)"
    $ show_picture(5, "rioleyna4")
    $ resolve_scene()
    Villager2 "Well Leyna don't worry here we are all friends and there is trust, isn't it Johan?"
    Johan "Of course! You can admire my wife's beauty all you want! After all it's only for me hahahaha"
    Villager2 "But man, don't tell us that, we'll die of envy! hahahaha"
    Leyna "Well, I think I'm going to take a bath guys!"
    $ show_picture(6, "rioleyna5")
    $ resolve_scene()
    Villager "Wait, you're going to go like that? You should strip completely naked or you'll get your panties wet and get cold"
    Leyna "I'm just a little embarrassed, guys"
    Villager "Don't worry, we are all adults here!"
    Villager2 "Yes, we're not going to see anything we haven't seen before"
    Leyna "I guess you are right"
    $ show_picture(6, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    Johan "W-well, I don't know..."
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV146_0_PlaySound_1
    Johan "!!!!"
    Villager "Wow! Awesome! Leyna do you exercise or something?"
    Leyna "Well... I do go to the gym every week"
    Villager "Very well, let's see!"
    call PlaySound("sound", "audio/Fall.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV146_0_PlaySound_2
    Leyna "!!!"
    $ show_picture(7, "rioleyna6")
    $ resolve_scene()
    Villager "It really shows! You have a great ass! And what kind of exercises do you do at the gym?"
    Johan "Hey hey!"
    Villager "Some cycling perhaps?"
    $ show_picture(8, "rioleyna7")
    $ resolve_scene()
    Leyna "Y-yes some biking... and some rubber exercises"
    Johan "(They're ignoring me? It's like I'm not even here... and Leyna...)"
    Johan "(The penis of this man we met just is soo close to Leyna's pussy)"
    Villager2 "Wow! May I see it?"
    $ show_picture(9, "rioleyna8")
    $ resolve_scene()
    Villager "Of course, look at her thighs! She's a real sportswoman!"
    Leyna "hm!"
    Villager2 "YES... that ... firmer thighs!"
    $ show_picture(10, "rioleyna9")
    $ resolve_scene()
    Villager2 "You could teach us some exercise, the truth is that these last years I have neglected a lot my physique and I'm getting a lot of belly hahahaa"
    Villager "Yes! With this great body you have to know some really good exercises!"
    Leyna "W-well, you could..."
    Johan "(This situation is getting too long for my taste... but after the little speech about trust I said before, I don't want to yell at them now)"
    $ show_picture(11, "rioleyna10")
    $ resolve_scene()
    Villager2 "What? I'm sorry, but you speak very softly and I can't hear you"
    Leyna "!!! I.... I..."
    Johan "Ahem well Leyna... shall we take a bath?"
    $ show_picture(12, "rioleyna11")
    $ resolve_scene()
    Leyna "Y-yeah right (for a second I forgot Johan is here, thank good from where he is, he can't see that this man's penis is pressed on me)"
    Villager "Oh! yeah, we'd better go for a swim"
    Villager2 "Yes, you're right hahaha sorry Johan!"
    $ show_picture(13, "rioleyna12")
    $ resolve_scene()
    Leyna "!!!Oooh!"
    Villager2 "Oops! I slipped! We almost fell down Leyna! hahaha"
    Villager2 "Uf... my back is... my back is bad, hold me for a second"
    Johan "??? Are you okay?"
    Villager2 "Oh yes yes, just give me a second"
    $ show_picture(14, "rioleyna13")
    $ resolve_scene()
    Leyna "hmmmmm Ahhh... I... I..."
    Villager "What's wrong Leyna? Did you hurt yourself?"
    Leyna "(Johan is right there... and this man has stuck his dick all the way in... in front of my husband...)"
    Johan "Leyna?"
    $ show_picture(15, "rioleyna14")
    $ resolve_scene()
    "plop! "
    Villager2 "There you go... hahahah it's just that my back always gives me problems, everything ok Leyna? Sorry I fell on you"
    Leyna "(Heavy breathing) Ah ah ah ah.... yes ... all right... come on Johan... let's go for a swim"
    Johan "Sure! (for a second I thought that... anyway, it's just my imagination...)"
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
    call ChangePartyMember("Johan", True) from _call_TownFestivalNightEV146_0_ChangePartyMember
    call TransferPlayer("TownNight", "TownFestivalNightEV146_0", 47, 23, direction=4) from _call_TownFestivalNightEV146_0_TransferPlayer_2
    $ fade_in()
    call Movement("TownFestivalNightEV146_0", "player", ["L","L","L","TURN_R"]) from _call_TownFestivalNightEV146_0_Movement_2
    $ resolve_scene()
    Johan "It looks like everyone has already gone to sleep... We better go to sleep too"
    Leyna "Yes... you are right"
    $ fade_out()
    call TransferPlayer("Town2", "TownFestivalNightEV146_0", 28, 22, direction=0) from _call_TownFestivalNightEV146_0_TransferPlayer_3
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ fade_in()
    $ resolve_scene()
    "The next morning..."
    $ erase_picture(1)
    call Movement("TownFestivalNightEV146_0", "player", ["D","TURN_U"]) from _call_TownFestivalNightEV146_0_Movement_3
    $ resolve_scene()
    Johan "My God, I have a terrible hangover, I can hardly remember what happened yesterday"
    Johan "... We were on the river with some guys, right? I hope we didn't do anything crazy"
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Oh hahaha... Right... no, relax we didn't do anything crazy...I don't remember much either...I also have a good hangover hahaha"
    Johan "Yeah... Well, what do you feel like doing today?"
    Leyna "The truth is that I should stop by my work at the hotsprings... but I can come by later"
    Johan "Don't worry, I could use a hot bath, I could walk you over there and take a bath and then I'll do some time while you finish up"
    Leyna "You don't have to if you don't want to..."
    Johan "Don't worry! It's not a problem!"
    Leyna "W-well, let's go there"
    $ erase_picture(1)
    $ resolve_scene()
    return False

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v5_1:
    call PauseForBalloon("TownFestivalNightEV146_1") from _call_TownFestivalNightEV146_1_PauseForBalloon
    Leyna "I should look for Johan, this game has gone longer than I'd like"
    $ fade_out()
    $ set_switch("final_hideout", True)
    call GalleryViewed("rioleyna") from _call_TownFestivalNightEV146_1_GalleryViewed
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV146_1", 15, 10, direction=4) from _call_TownFestivalNightEV146_1_TransferPlayer
    $ fade_in()
    call Movement("TownFestivalNightEV146_1", "player", ["L","L","L","L","L","U","U","L","L","L"]) from _call_TownFestivalNightEV146_1_Movement
    call Movement("TownFestivalNightEV146_1", "TownFestivalNightjohan2", ["TURN_R"]) from _call_TownFestivalNightEV146_1_Movement_1
    $ resolve_scene()
    call PauseForBalloon("TownFestivalNightEV146_1") from _call_TownFestivalNightEV146_1_PauseForBalloon_1
    Johan "Leyna! I was starting to worry, I couldn't find you anywhere, everything all right?"
    Leyna "Hmm yes... everything... everything is fine! Well... Shall we go to sleep? I'm exhausted"
    Johan "Exhausted? But the night just started! We met some villagers and they invited us for a drink!"
    Alexa "Exactly Leyna! I'm sure you'll have a great time! Let's have a few beers and I'm sure you'll get over your tiredness!"
    Leyna "I don't feel like it guys..."
    Johan "Come on Leyna, it will be fun, we have worked hard these days, we deserve a night out!"
    Leyna "Okay guys... let's have a couple of beers"
    Alexa "Good!! We're meeting them for a drink nearby"
    $ fade_out()
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV146_1", 44, 39, direction=2) from _call_TownFestivalNightEV146_1_TransferPlayer_1
    call SetEventLocation("TownFestivalNightEV146_1", "TownFestivalNightalexa2", 43, 39) from _call_TownFestivalNightEV146_1_setloc
    call SetEventLocation("TownFestivalNightEV146_1", "TownFestivalNightmarido2", 43, 40) from _call_TownFestivalNightEV146_1_setloc_1
    call SetEventLocation("TownFestivalNightEV146_1", "TownFestivalNightjohan2", 45, 39) from _call_TownFestivalNightEV146_1_setloc_2
    $ fade_in()
    $ resolve_scene()
    Alexa "We are here! Did you get the beers?"
    Villager "Yes, we have plenty for the whole night"
    Johan "Great! It's been years since I've been out partying!"
    Villager2 "(Wow how lucky we are! We finally convinced the two tourist girls to come and drink! we have to make the most of it)"
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(SEVERAL BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "No, but seriously Johan, your wife is beautiful, I don't know how you can live in peace"
    Johan "Well (ugh I'm so drunk) let's see... I believe that the most important thing in a relationship is trust and I ... I trust Leyna completely"
    Villager "Very well said... but of course, all the festivals in this town revolve around showing off your body..."
    Villager "Aren't you worried that all the men in town will see your wife's body?"
    Leyna "W-well my body..."
    Johan "NO! I'm not worried, we were all born naked and it's completely natural!"
    Alexa "Very well said! You are absolutely right"
    AlexasHusband "..."
    Villager2 "Yeah! If you have a good body, what better than to show it off, right?"
    Johan "Well... also not..."
    Villager "Johan... you are a wise man!"
    Johan "O-okey Thank you hahaha..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(MANY MORE BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "BUah I'm pretty fucked up already... Do you know what I'm really interested in right now?"
    Leyna "Wh-hip-what do you feel like?"
    Villager "I feel like fucking"
    Leyna "!!!"
    Villager "HAHAHAHAAHA No... I really feel like going to the river to take a bath... are you in?"
    Alexa "Sure, why not? That way we can sober up a little bit"
    Johan "Yes, a cold bath would be great for me right now!"
    Leyna "But... in the river, we would all have to undress"
    Johan "Shit, true..."
    Villager "Well, as you said, it's completely natural right?"
    Johan "Well, yes..."
    Villager2 "And besides, there's trust, right Johan? It's just taking a bath and all..."
    Johan "Well, I guess you're right"
    Leyna "If JoHan AgRees, I hAve no probLem..."
    Villager "Great! (she seems to be quite drunk)"
    Johan "YES! I'm looking forward to going back to the river"
    Villager "Ehm... ahem yes, the river of course..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "LATER IN THE RIVER ..."
    Villager "Come on, everyone without clothes, otherwise the goddess will get angry"
    Johan "hahahahahaha okay let's go"
    Leyna "Okay, but give me one more shot of beer first hahaha"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV146_1_PlaySound
    $ show_picture(2, "rioleyna1")
    $ resolve_scene()
    Leyna "Ahhh how nice, how refreshing... it may be the alcohol but the truth is that being like this without worrying so much is very ... liberalizing"
    Johan "Right? Now I feel a little bad for being angry in the past"
    $ show_picture(3, "rioleyna2")
    $ resolve_scene()
    Villager "Yesssss this is all tradition here! We have no problem seeing each other naked!"
    Leyna "It's certainly very different from how we behave in the city, but I guess it's cool"
    Villager2 "Hahahahaha man, here we are all happy to see each other, especially you Leyna! What a great body!"
    Johan "hahhaha you bet! Eeven though she is my wife, I still can't get used to seeing her like this"
    $ show_picture(4, "rioleyna3")
    $ resolve_scene()
    Villager2 "Dude! You sure are glad to see Leyna!"
    Johan "Hahahaha"
    Leyna "WOW! what a big dick (!!!!!!) fu-fuck did I say that out loud? Sorry...."
    Leyna "When I drink too much I'm not myself"
    Johan "Hahaha...(Wow I didn't expect that comment from Leyna ... even though she told the truth I can't help but feel jealous... I have a weird feeling in my stomach"
    "looking at this situation... I don't know if it's because of the alcohol but... well, don't think about it too much Johan)"
    $ show_picture(5, "rioleyna4")
    $ resolve_scene()
    Villager2 "Well Leyna don't worry here we are all friends and there is trust, isn't it Johan?"
    Johan "Of course! You can admire my wife's beauty all you want! After all it's only for me hahahaha"
    Villager2 "But man, don't tell us that, we'll die of envy! hahahaha"
    Leyna "Well, I think I'm going to take a bath guys!"
    $ show_picture(6, "rioleyna5")
    $ resolve_scene()
    Villager "Wait, you're going to go like that? You should strip completely naked or you'll get your panties wet and get cold"
    Leyna "I'm just a little embarrassed, guys"
    Villager "Don't worry, we are all adults here!"
    Villager2 "Yes, we're not going to see anything we haven't seen before"
    Leyna "I guess you are right"
    $ show_picture(6, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    Johan "W-well, I don't know..."
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV146_1_PlaySound_1
    Johan "!!!!"
    Villager "Wow! Awesome! Leyna do you exercise or something?"
    Leyna "Well... I do go to the gym every week"
    Villager "Very well, let's see!"
    call PlaySound("sound", "audio/Fall.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV146_1_PlaySound_2
    Leyna "!!!"
    $ show_picture(7, "rioleyna6")
    $ resolve_scene()
    Villager "It really shows! You have a great ass! And what kind of exercises do you do at the gym?"
    Johan "Hey hey!"
    Villager "Some cycling perhaps?"
    $ show_picture(8, "rioleyna7")
    $ resolve_scene()
    Leyna "Y-yes some biking... and some rubber exercises"
    Johan "(They're ignoring me? It's like I'm not even here... and Leyna...)"
    Johan "(The penis of this man we met just is soo close to Leyna's pussy)"
    Villager2 "Wow! May I see it?"
    $ show_picture(9, "rioleyna8")
    $ resolve_scene()
    Villager "Of course, look at her thighs! She's a real sportswoman!"
    Leyna "hm!"
    Villager2 "YES... that ... firmer thighs!"
    $ show_picture(10, "rioleyna9")
    $ resolve_scene()
    Villager2 "You could teach us some exercise, the truth is that these last years I have neglected a lot my physique and I'm getting a lot of belly hahahaa"
    Villager "Yes! With this great body you have to know some really good exercises!"
    Leyna "W-well, you could..."
    Johan "(This situation is getting too long for my taste... but after the little speech about trust I said before, I don't want to yell at them now)"
    $ show_picture(11, "rioleyna10")
    $ resolve_scene()
    Villager2 "What? I'm sorry, but you speak very softly and I can't hear you"
    Leyna "!!! I.... I..."
    Johan "Ahem well Leyna... shall we take a bath?"
    $ show_picture(12, "rioleyna11")
    $ resolve_scene()
    Leyna "Y-yeah right (for a second I forgot Johan is here, thank good from where he is, he can't see that this man's penis is pressed on me)"
    Villager "Oh! yeah, we'd better go for a swim"
    Villager2 "Yes, you're right hahaha sorry Johan!"
    $ show_picture(13, "rioleyna12")
    $ resolve_scene()
    Leyna "!!!Oooh!"
    Villager2 "Oops! I slipped! We almost fell down Leyna! hahaha"
    Villager2 "Uf... my back is... my back is bad, hold me for a second"
    Johan "??? Are you okay?"
    Villager2 "Oh yes yes, just give me a second"
    $ show_picture(14, "rioleyna13")
    $ resolve_scene()
    Leyna "hmmmmm Ahhh... I... I..."
    Villager "What's wrong Leyna? Did you hurt yourself?"
    Leyna "(Johan is right there... and this man has stuck his dick all the way in... in front of my husband...)"
    Johan "Leyna?"
    $ show_picture(15, "rioleyna14")
    $ resolve_scene()
    "plop! "
    Villager2 "There you go... hahahah it's just that my back always gives me problems, everything ok Leyna? Sorry I fell on you"
    Leyna "(Heavy breathing) Ah ah ah ah.... yes ... all right... come on Johan... let's go for a swim"
    Johan "Sure! (for a second I thought that... anyway, it's just my imagination...)"
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
    call ChangePartyMember("Johan", True) from _call_TownFestivalNightEV146_1_ChangePartyMember
    call TransferPlayer("TownNight", "TownFestivalNightEV146_1", 47, 23, direction=4) from _call_TownFestivalNightEV146_1_TransferPlayer_2
    $ fade_in()
    call Movement("TownFestivalNightEV146_1", "player", ["L","L","L","TURN_R"]) from _call_TownFestivalNightEV146_1_Movement_2
    $ resolve_scene()
    Johan "It looks like everyone has already gone to sleep... We better go to sleep too"
    Leyna "Yes... you are right"
    $ fade_out()
    call TransferPlayer("Town2", "TownFestivalNightEV146_1", 28, 22, direction=0) from _call_TownFestivalNightEV146_1_TransferPlayer_3
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ fade_in()
    $ resolve_scene()
    "The next morning..."
    $ erase_picture(1)
    call Movement("TownFestivalNightEV146_1", "player", ["D","TURN_U"]) from _call_TownFestivalNightEV146_1_Movement_3
    $ resolve_scene()
    Johan "My God, I have a terrible hangover, I can hardly remember what happened yesterday"
    Johan "... We were on the river with some guys, right? I hope we didn't do anything crazy"
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Oh hahaha... Right... no, relax we didn't do anything crazy...I don't remember much either...I also have a good hangover hahaha"
    Johan "Yeah... Well, what do you feel like doing today?"
    Leyna "The truth is that I should stop by my work at the hotsprings... but I can come by later"
    Johan "Don't worry, I could use a hot bath, I could walk you over there and take a bath and then I'll do some time while you finish up"
    Leyna "You don't have to if you don't want to..."
    Johan "Don't worry! It's not a problem!"
    Leyna "W-well, let's go there"
    $ erase_picture(1)
    $ resolve_scene()
    return False

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v5(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v5"):
        return None
    elif trigger == "event" and hiding_place >= 4:
        call PlayEvent(play_event, "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v5_1", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v5") from _call_TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v5_1_PlayEvent
        return (0, "", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v5_1")
    elif trigger == "event" and hiding_place >= 3:
        call PlayEvent(play_event, "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v5_0", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v5") from _call_TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v5_0_PlayEvent
        return (0, "", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v5_0")
    return None

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v6_0:
    call PauseForBalloon("TownFestivalNightEV147_0") from _call_TownFestivalNightEV147_0_PauseForBalloon
    Leyna "I should look for Johan, this game has gone longer than I'd like"
    $ fade_out()
    $ set_switch("final_hideout", True)
    call GalleryViewed("rioleyna") from _call_TownFestivalNightEV147_0_GalleryViewed
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV147_0", 15, 10, direction=4) from _call_TownFestivalNightEV147_0_TransferPlayer
    $ fade_in()
    call Movement("TownFestivalNightEV147_0", "player", ["L","L","L","L","L","U","U","L","L","L"]) from _call_TownFestivalNightEV147_0_Movement
    call Movement("TownFestivalNightEV147_0", "TownFestivalNightjohan2", ["TURN_R"]) from _call_TownFestivalNightEV147_0_Movement_1
    $ resolve_scene()
    call PauseForBalloon("TownFestivalNightEV147_0") from _call_TownFestivalNightEV147_0_PauseForBalloon_1
    Johan "Leyna! I was starting to worry, I couldn't find you anywhere, everything all right?"
    Leyna "Hmm yes... everything... everything is fine! Well... Shall we go to sleep? I'm exhausted"
    Johan "Exhausted? But the night just started! We met some villagers and they invited us for a drink!"
    Alexa "Exactly Leyna! I'm sure you'll have a great time! Let's have a few beers and I'm sure you'll get over your tiredness!"
    Leyna "I don't feel like it guys..."
    Johan "Come on Leyna, it will be fun, we have worked hard these days, we deserve a night out!"
    Leyna "Okay guys... let's have a couple of beers"
    Alexa "Good!! We're meeting them for a drink nearby"
    $ fade_out()
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV147_0", 44, 39, direction=2) from _call_TownFestivalNightEV147_0_TransferPlayer_1
    call SetEventLocation("TownFestivalNightEV147_0", "TownFestivalNightalexa2", 43, 39) from _call_TownFestivalNightEV147_0_setloc
    call SetEventLocation("TownFestivalNightEV147_0", "TownFestivalNightmarido2", 43, 40) from _call_TownFestivalNightEV147_0_setloc_1
    call SetEventLocation("TownFestivalNightEV147_0", "TownFestivalNightjohan2", 45, 39) from _call_TownFestivalNightEV147_0_setloc_2
    $ fade_in()
    $ resolve_scene()
    Alexa "We are here! Did you get the beers?"
    Villager "Yes, we have plenty for the whole night"
    Johan "Great! It's been years since I've been out partying!"
    Villager2 "(Wow how lucky we are! We finally convinced the two tourist girls to come and drink! we have to make the most of it)"
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(SEVERAL BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "No, but seriously Johan, your wife is beautiful, I don't know how you can live in peace"
    Johan "Well (ugh I'm so drunk) let's see... I believe that the most important thing in a relationship is trust and I ... I trust Leyna completely"
    Villager "Very well said... but of course, all the festivals in this town revolve around showing off your body..."
    Villager "Aren't you worried that all the men in town will see your wife's body?"
    Leyna "W-well my body..."
    Johan "NO! I'm not worried, we were all born naked and it's completely natural!"
    Alexa "Very well said! You are absolutely right"
    AlexasHusband "..."
    Villager2 "Yeah! If you have a good body, what better than to show it off, right?"
    Johan "Well... also not..."
    Villager "Johan... you are a wise man!"
    Johan "O-okey Thank you hahaha..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(MANY MORE BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "BUah I'm pretty fucked up already... Do you know what I'm really interested in right now?"
    Leyna "Wh-hip-what do you feel like?"
    Villager "I feel like fucking"
    Leyna "!!!"
    Villager "HAHAHAHAAHA No... I really feel like going to the river to take a bath... are you in?"
    Alexa "Sure, why not? That way we can sober up a little bit"
    Johan "Yes, a cold bath would be great for me right now!"
    Leyna "But... in the river, we would all have to undress"
    Johan "Shit, true..."
    Villager "Well, as you said, it's completely natural right?"
    Johan "Well, yes..."
    Villager2 "And besides, there's trust, right Johan? It's just taking a bath and all..."
    Johan "Well, I guess you're right"
    Leyna "If JoHan AgRees, I hAve no probLem..."
    Villager "Great! (she seems to be quite drunk)"
    Johan "YES! I'm looking forward to going back to the river"
    Villager "Ehm... ahem yes, the river of course..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "LATER IN THE RIVER ..."
    Villager "Come on, everyone without clothes, otherwise the goddess will get angry"
    Johan "hahahahahaha okay let's go"
    Leyna "Okay, but give me one more shot of beer first hahaha"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV147_0_PlaySound
    $ show_picture(2, "rioleyna1")
    $ resolve_scene()
    Leyna "Ahhh how nice, how refreshing... it may be the alcohol but the truth is that being like this without worrying so much is very ... liberalizing"
    Johan "Right? Now I feel a little bad for being angry in the past"
    $ show_picture(3, "rioleyna2")
    $ resolve_scene()
    Villager "Yesssss this is all tradition here! We have no problem seeing each other naked!"
    Leyna "It's certainly very different from how we behave in the city, but I guess it's cool"
    Villager2 "Hahahahaha man, here we are all happy to see each other, especially you Leyna! What a great body!"
    Johan "hahhaha you bet! Eeven though she is my wife, I still can't get used to seeing her like this"
    $ show_picture(4, "rioleyna3")
    $ resolve_scene()
    Villager2 "Dude! You sure are glad to see Leyna!"
    Johan "Hahahaha"
    Leyna "WOW! what a big dick (!!!!!!) fu-fuck did I say that out loud? Sorry...."
    Leyna "When I drink too much I'm not myself"
    Johan "Hahaha...(Wow I didn't expect that comment from Leyna ... even though she told the truth I can't help but feel jealous... I have a weird feeling in my stomach"
    "looking at this situation... I don't know if it's because of the alcohol but... well, don't think about it too much Johan)"
    $ show_picture(5, "rioleyna4")
    $ resolve_scene()
    Villager2 "Well Leyna don't worry here we are all friends and there is trust, isn't it Johan?"
    Johan "Of course! You can admire my wife's beauty all you want! After all it's only for me hahahaha"
    Villager2 "But man, don't tell us that, we'll die of envy! hahahaha"
    Leyna "Well, I think I'm going to take a bath guys!"
    $ show_picture(6, "rioleyna5")
    $ resolve_scene()
    Villager "Wait, you're going to go like that? You should strip completely naked or you'll get your panties wet and get cold"
    Leyna "I'm just a little embarrassed, guys"
    Villager "Don't worry, we are all adults here!"
    Villager2 "Yes, we're not going to see anything we haven't seen before"
    Leyna "I guess you are right"
    $ show_picture(6, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    Johan "W-well, I don't know..."
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV147_0_PlaySound_1
    Johan "!!!!"
    Villager "Wow! Awesome! Leyna do you exercise or something?"
    Leyna "Well... I do go to the gym every week"
    Villager "Very well, let's see!"
    call PlaySound("sound", "audio/Fall.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV147_0_PlaySound_2
    Leyna "!!!"
    $ show_picture(7, "rioleyna6")
    $ resolve_scene()
    Villager "It really shows! You have a great ass! And what kind of exercises do you do at the gym?"
    Johan "Hey hey!"
    Villager "Some cycling perhaps?"
    $ show_picture(8, "rioleyna7")
    $ resolve_scene()
    Leyna "Y-yes some biking... and some rubber exercises"
    Johan "(They're ignoring me? It's like I'm not even here... and Leyna...)"
    Johan "(The penis of this man we met just is soo close to Leyna's pussy)"
    Villager2 "Wow! May I see it?"
    $ show_picture(9, "rioleyna8")
    $ resolve_scene()
    Villager "Of course, look at her thighs! She's a real sportswoman!"
    Leyna "hm!"
    Villager2 "YES... that ... firmer thighs!"
    $ show_picture(10, "rioleyna9")
    $ resolve_scene()
    Villager2 "You could teach us some exercise, the truth is that these last years I have neglected a lot my physique and I'm getting a lot of belly hahahaa"
    Villager "Yes! With this great body you have to know some really good exercises!"
    Leyna "W-well, you could..."
    Johan "(This situation is getting too long for my taste... but after the little speech about trust I said before, I don't want to yell at them now)"
    $ show_picture(11, "rioleyna10")
    $ resolve_scene()
    Villager2 "What? I'm sorry, but you speak very softly and I can't hear you"
    Leyna "!!! I.... I..."
    Johan "Ahem well Leyna... shall we take a bath?"
    $ show_picture(12, "rioleyna11")
    $ resolve_scene()
    Leyna "Y-yeah right (for a second I forgot Johan is here, thank good from where he is, he can't see that this man's penis is pressed on me)"
    Villager "Oh! yeah, we'd better go for a swim"
    Villager2 "Yes, you're right hahaha sorry Johan!"
    $ show_picture(13, "rioleyna12")
    $ resolve_scene()
    Leyna "!!!Oooh!"
    Villager2 "Oops! I slipped! We almost fell down Leyna! hahaha"
    Villager2 "Uf... my back is... my back is bad, hold me for a second"
    Johan "??? Are you okay?"
    Villager2 "Oh yes yes, just give me a second"
    $ show_picture(14, "rioleyna13")
    $ resolve_scene()
    Leyna "hmmmmm Ahhh... I... I..."
    Villager "What's wrong Leyna? Did you hurt yourself?"
    Leyna "(Johan is right there... and this man has stuck his dick all the way in... in front of my husband...)"
    Johan "Leyna?"
    $ show_picture(15, "rioleyna14")
    $ resolve_scene()
    "plop! "
    Villager2 "There you go... hahahah it's just that my back always gives me problems, everything ok Leyna? Sorry I fell on you"
    Leyna "(Heavy breathing) Ah ah ah ah.... yes ... all right... come on Johan... let's go for a swim"
    Johan "Sure! (for a second I thought that... anyway, it's just my imagination...)"
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
    call ChangePartyMember("Johan", True) from _call_TownFestivalNightEV147_0_ChangePartyMember
    call TransferPlayer("TownNight", "TownFestivalNightEV147_0", 47, 23, direction=4) from _call_TownFestivalNightEV147_0_TransferPlayer_2
    $ fade_in()
    call Movement("TownFestivalNightEV147_0", "player", ["L","L","L","TURN_R"]) from _call_TownFestivalNightEV147_0_Movement_2
    $ resolve_scene()
    Johan "It looks like everyone has already gone to sleep... We better go to sleep too"
    Leyna "Yes... you are right"
    $ fade_out()
    call TransferPlayer("Town2", "TownFestivalNightEV147_0", 28, 22, direction=0) from _call_TownFestivalNightEV147_0_TransferPlayer_3
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ fade_in()
    $ resolve_scene()
    "The next morning..."
    $ erase_picture(1)
    call Movement("TownFestivalNightEV147_0", "player", ["D","TURN_U"]) from _call_TownFestivalNightEV147_0_Movement_3
    $ resolve_scene()
    Johan "My God, I have a terrible hangover, I can hardly remember what happened yesterday"
    Johan "... We were on the river with some guys, right? I hope we didn't do anything crazy"
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Oh hahaha... Right... no, relax we didn't do anything crazy...I don't remember much either...I also have a good hangover hahaha"
    Johan "Yeah... Well, what do you feel like doing today?"
    Leyna "The truth is that I should stop by my work at the hotsprings... but I can come by later"
    Johan "Don't worry, I could use a hot bath, I could walk you over there and take a bath and then I'll do some time while you finish up"
    Leyna "You don't have to if you don't want to..."
    Johan "Don't worry! It's not a problem!"
    Leyna "W-well, let's go there"
    $ erase_picture(1)
    $ resolve_scene()
    return False

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v6_1:
    call PauseForBalloon("TownFestivalNightEV147_1") from _call_TownFestivalNightEV147_1_PauseForBalloon
    Leyna "I should look for Johan, this game has gone longer than I'd like"
    $ fade_out()
    $ set_switch("final_hideout", True)
    call GalleryViewed("rioleyna") from _call_TownFestivalNightEV147_1_GalleryViewed
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV147_1", 15, 10, direction=4) from _call_TownFestivalNightEV147_1_TransferPlayer
    $ fade_in()
    call Movement("TownFestivalNightEV147_1", "player", ["L","L","L","L","L","U","U","L","L","L"]) from _call_TownFestivalNightEV147_1_Movement
    call Movement("TownFestivalNightEV147_1", "TownFestivalNightjohan2", ["TURN_R"]) from _call_TownFestivalNightEV147_1_Movement_1
    $ resolve_scene()
    call PauseForBalloon("TownFestivalNightEV147_1") from _call_TownFestivalNightEV147_1_PauseForBalloon_1
    Johan "Leyna! I was starting to worry, I couldn't find you anywhere, everything all right?"
    Leyna "Hmm yes... everything... everything is fine! Well... Shall we go to sleep? I'm exhausted"
    Johan "Exhausted? But the night just started! We met some villagers and they invited us for a drink!"
    Alexa "Exactly Leyna! I'm sure you'll have a great time! Let's have a few beers and I'm sure you'll get over your tiredness!"
    Leyna "I don't feel like it guys..."
    Johan "Come on Leyna, it will be fun, we have worked hard these days, we deserve a night out!"
    Leyna "Okay guys... let's have a couple of beers"
    Alexa "Good!! We're meeting them for a drink nearby"
    $ fade_out()
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV147_1", 44, 39, direction=2) from _call_TownFestivalNightEV147_1_TransferPlayer_1
    call SetEventLocation("TownFestivalNightEV147_1", "TownFestivalNightalexa2", 43, 39) from _call_TownFestivalNightEV147_1_setloc
    call SetEventLocation("TownFestivalNightEV147_1", "TownFestivalNightmarido2", 43, 40) from _call_TownFestivalNightEV147_1_setloc_1
    call SetEventLocation("TownFestivalNightEV147_1", "TownFestivalNightjohan2", 45, 39) from _call_TownFestivalNightEV147_1_setloc_2
    $ fade_in()
    $ resolve_scene()
    Alexa "We are here! Did you get the beers?"
    Villager "Yes, we have plenty for the whole night"
    Johan "Great! It's been years since I've been out partying!"
    Villager2 "(Wow how lucky we are! We finally convinced the two tourist girls to come and drink! we have to make the most of it)"
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(SEVERAL BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "No, but seriously Johan, your wife is beautiful, I don't know how you can live in peace"
    Johan "Well (ugh I'm so drunk) let's see... I believe that the most important thing in a relationship is trust and I ... I trust Leyna completely"
    Villager "Very well said... but of course, all the festivals in this town revolve around showing off your body..."
    Villager "Aren't you worried that all the men in town will see your wife's body?"
    Leyna "W-well my body..."
    Johan "NO! I'm not worried, we were all born naked and it's completely natural!"
    Alexa "Very well said! You are absolutely right"
    AlexasHusband "..."
    Villager2 "Yeah! If you have a good body, what better than to show it off, right?"
    Johan "Well... also not..."
    Villager "Johan... you are a wise man!"
    Johan "O-okey Thank you hahaha..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(MANY MORE BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "BUah I'm pretty fucked up already... Do you know what I'm really interested in right now?"
    Leyna "Wh-hip-what do you feel like?"
    Villager "I feel like fucking"
    Leyna "!!!"
    Villager "HAHAHAHAAHA No... I really feel like going to the river to take a bath... are you in?"
    Alexa "Sure, why not? That way we can sober up a little bit"
    Johan "Yes, a cold bath would be great for me right now!"
    Leyna "But... in the river, we would all have to undress"
    Johan "Shit, true..."
    Villager "Well, as you said, it's completely natural right?"
    Johan "Well, yes..."
    Villager2 "And besides, there's trust, right Johan? It's just taking a bath and all..."
    Johan "Well, I guess you're right"
    Leyna "If JoHan AgRees, I hAve no probLem..."
    Villager "Great! (she seems to be quite drunk)"
    Johan "YES! I'm looking forward to going back to the river"
    Villager "Ehm... ahem yes, the river of course..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "LATER IN THE RIVER ..."
    Villager "Come on, everyone without clothes, otherwise the goddess will get angry"
    Johan "hahahahahaha okay let's go"
    Leyna "Okay, but give me one more shot of beer first hahaha"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV147_1_PlaySound
    $ show_picture(2, "rioleyna1")
    $ resolve_scene()
    Leyna "Ahhh how nice, how refreshing... it may be the alcohol but the truth is that being like this without worrying so much is very ... liberalizing"
    Johan "Right? Now I feel a little bad for being angry in the past"
    $ show_picture(3, "rioleyna2")
    $ resolve_scene()
    Villager "Yesssss this is all tradition here! We have no problem seeing each other naked!"
    Leyna "It's certainly very different from how we behave in the city, but I guess it's cool"
    Villager2 "Hahahahaha man, here we are all happy to see each other, especially you Leyna! What a great body!"
    Johan "hahhaha you bet! Eeven though she is my wife, I still can't get used to seeing her like this"
    $ show_picture(4, "rioleyna3")
    $ resolve_scene()
    Villager2 "Dude! You sure are glad to see Leyna!"
    Johan "Hahahaha"
    Leyna "WOW! what a big dick (!!!!!!) fu-fuck did I say that out loud? Sorry...."
    Leyna "When I drink too much I'm not myself"
    Johan "Hahaha...(Wow I didn't expect that comment from Leyna ... even though she told the truth I can't help but feel jealous... I have a weird feeling in my stomach"
    "looking at this situation... I don't know if it's because of the alcohol but... well, don't think about it too much Johan)"
    $ show_picture(5, "rioleyna4")
    $ resolve_scene()
    Villager2 "Well Leyna don't worry here we are all friends and there is trust, isn't it Johan?"
    Johan "Of course! You can admire my wife's beauty all you want! After all it's only for me hahahaha"
    Villager2 "But man, don't tell us that, we'll die of envy! hahahaha"
    Leyna "Well, I think I'm going to take a bath guys!"
    $ show_picture(6, "rioleyna5")
    $ resolve_scene()
    Villager "Wait, you're going to go like that? You should strip completely naked or you'll get your panties wet and get cold"
    Leyna "I'm just a little embarrassed, guys"
    Villager "Don't worry, we are all adults here!"
    Villager2 "Yes, we're not going to see anything we haven't seen before"
    Leyna "I guess you are right"
    $ show_picture(6, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    Johan "W-well, I don't know..."
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV147_1_PlaySound_1
    Johan "!!!!"
    Villager "Wow! Awesome! Leyna do you exercise or something?"
    Leyna "Well... I do go to the gym every week"
    Villager "Very well, let's see!"
    call PlaySound("sound", "audio/Fall.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV147_1_PlaySound_2
    Leyna "!!!"
    $ show_picture(7, "rioleyna6")
    $ resolve_scene()
    Villager "It really shows! You have a great ass! And what kind of exercises do you do at the gym?"
    Johan "Hey hey!"
    Villager "Some cycling perhaps?"
    $ show_picture(8, "rioleyna7")
    $ resolve_scene()
    Leyna "Y-yes some biking... and some rubber exercises"
    Johan "(They're ignoring me? It's like I'm not even here... and Leyna...)"
    Johan "(The penis of this man we met just is soo close to Leyna's pussy)"
    Villager2 "Wow! May I see it?"
    $ show_picture(9, "rioleyna8")
    $ resolve_scene()
    Villager "Of course, look at her thighs! She's a real sportswoman!"
    Leyna "hm!"
    Villager2 "YES... that ... firmer thighs!"
    $ show_picture(10, "rioleyna9")
    $ resolve_scene()
    Villager2 "You could teach us some exercise, the truth is that these last years I have neglected a lot my physique and I'm getting a lot of belly hahahaa"
    Villager "Yes! With this great body you have to know some really good exercises!"
    Leyna "W-well, you could..."
    Johan "(This situation is getting too long for my taste... but after the little speech about trust I said before, I don't want to yell at them now)"
    $ show_picture(11, "rioleyna10")
    $ resolve_scene()
    Villager2 "What? I'm sorry, but you speak very softly and I can't hear you"
    Leyna "!!! I.... I..."
    Johan "Ahem well Leyna... shall we take a bath?"
    $ show_picture(12, "rioleyna11")
    $ resolve_scene()
    Leyna "Y-yeah right (for a second I forgot Johan is here, thank good from where he is, he can't see that this man's penis is pressed on me)"
    Villager "Oh! yeah, we'd better go for a swim"
    Villager2 "Yes, you're right hahaha sorry Johan!"
    $ show_picture(13, "rioleyna12")
    $ resolve_scene()
    Leyna "!!!Oooh!"
    Villager2 "Oops! I slipped! We almost fell down Leyna! hahaha"
    Villager2 "Uf... my back is... my back is bad, hold me for a second"
    Johan "??? Are you okay?"
    Villager2 "Oh yes yes, just give me a second"
    $ show_picture(14, "rioleyna13")
    $ resolve_scene()
    Leyna "hmmmmm Ahhh... I... I..."
    Villager "What's wrong Leyna? Did you hurt yourself?"
    Leyna "(Johan is right there... and this man has stuck his dick all the way in... in front of my husband...)"
    Johan "Leyna?"
    $ show_picture(15, "rioleyna14")
    $ resolve_scene()
    "plop! "
    Villager2 "There you go... hahahah it's just that my back always gives me problems, everything ok Leyna? Sorry I fell on you"
    Leyna "(Heavy breathing) Ah ah ah ah.... yes ... all right... come on Johan... let's go for a swim"
    Johan "Sure! (for a second I thought that... anyway, it's just my imagination...)"
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
    call ChangePartyMember("Johan", True) from _call_TownFestivalNightEV147_1_ChangePartyMember
    call TransferPlayer("TownNight", "TownFestivalNightEV147_1", 47, 23, direction=4) from _call_TownFestivalNightEV147_1_TransferPlayer_2
    $ fade_in()
    call Movement("TownFestivalNightEV147_1", "player", ["L","L","L","TURN_R"]) from _call_TownFestivalNightEV147_1_Movement_2
    $ resolve_scene()
    Johan "It looks like everyone has already gone to sleep... We better go to sleep too"
    Leyna "Yes... you are right"
    $ fade_out()
    call TransferPlayer("Town2", "TownFestivalNightEV147_1", 28, 22, direction=0) from _call_TownFestivalNightEV147_1_TransferPlayer_3
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ fade_in()
    $ resolve_scene()
    "The next morning..."
    $ erase_picture(1)
    call Movement("TownFestivalNightEV147_1", "player", ["D","TURN_U"]) from _call_TownFestivalNightEV147_1_Movement_3
    $ resolve_scene()
    Johan "My God, I have a terrible hangover, I can hardly remember what happened yesterday"
    Johan "... We were on the river with some guys, right? I hope we didn't do anything crazy"
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Oh hahaha... Right... no, relax we didn't do anything crazy...I don't remember much either...I also have a good hangover hahaha"
    Johan "Yeah... Well, what do you feel like doing today?"
    Leyna "The truth is that I should stop by my work at the hotsprings... but I can come by later"
    Johan "Don't worry, I could use a hot bath, I could walk you over there and take a bath and then I'll do some time while you finish up"
    Leyna "You don't have to if you don't want to..."
    Johan "Don't worry! It's not a problem!"
    Leyna "W-well, let's go there"
    $ erase_picture(1)
    $ resolve_scene()
    return False

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v6(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v6"):
        return None
    elif trigger == "event" and hiding_place >= 4:
        call PlayEvent(play_event, "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v6_1", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v6") from _call_TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v6_1_PlayEvent
        return (0, "", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v6_1")
    elif trigger == "event" and hiding_place >= 3:
        call PlayEvent(play_event, "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v6_0", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v6") from _call_TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v6_0_PlayEvent
        return (0, "", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v6_0")
    return None

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v7_0:
    call PauseForBalloon("TownFestivalNightEV148_0") from _call_TownFestivalNightEV148_0_PauseForBalloon
    Leyna "I should look for Johan, this game has gone longer than I'd like"
    $ fade_out()
    $ set_switch("final_hideout", True)
    call GalleryViewed("rioleyna") from _call_TownFestivalNightEV148_0_GalleryViewed
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV148_0", 15, 10, direction=4) from _call_TownFestivalNightEV148_0_TransferPlayer
    $ fade_in()
    call Movement("TownFestivalNightEV148_0", "player", ["L","L","L","L","L","U","U","L","L","L"]) from _call_TownFestivalNightEV148_0_Movement
    call Movement("TownFestivalNightEV148_0", "TownFestivalNightjohan2", ["TURN_R"]) from _call_TownFestivalNightEV148_0_Movement_1
    $ resolve_scene()
    call PauseForBalloon("TownFestivalNightEV148_0") from _call_TownFestivalNightEV148_0_PauseForBalloon_1
    Johan "Leyna! I was starting to worry, I couldn't find you anywhere, everything all right?"
    Leyna "Hmm yes... everything... everything is fine! Well... Shall we go to sleep? I'm exhausted"
    Johan "Exhausted? But the night just started! We met some villagers and they invited us for a drink!"
    Alexa "Exactly Leyna! I'm sure you'll have a great time! Let's have a few beers and I'm sure you'll get over your tiredness!"
    Leyna "I don't feel like it guys..."
    Johan "Come on Leyna, it will be fun, we have worked hard these days, we deserve a night out!"
    Leyna "Okay guys... let's have a couple of beers"
    Alexa "Good!! We're meeting them for a drink nearby"
    $ fade_out()
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV148_0", 44, 39, direction=2) from _call_TownFestivalNightEV148_0_TransferPlayer_1
    call SetEventLocation("TownFestivalNightEV148_0", "TownFestivalNightalexa2", 43, 39) from _call_TownFestivalNightEV148_0_setloc
    call SetEventLocation("TownFestivalNightEV148_0", "TownFestivalNightmarido2", 43, 40) from _call_TownFestivalNightEV148_0_setloc_1
    call SetEventLocation("TownFestivalNightEV148_0", "TownFestivalNightjohan2", 45, 39) from _call_TownFestivalNightEV148_0_setloc_2
    $ fade_in()
    $ resolve_scene()
    Alexa "We are here! Did you get the beers?"
    Villager "Yes, we have plenty for the whole night"
    Johan "Great! It's been years since I've been out partying!"
    Villager2 "(Wow how lucky we are! We finally convinced the two tourist girls to come and drink! we have to make the most of it)"
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(SEVERAL BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "No, but seriously Johan, your wife is beautiful, I don't know how you can live in peace"
    Johan "Well (ugh I'm so drunk) let's see... I believe that the most important thing in a relationship is trust and I ... I trust Leyna completely"
    Villager "Very well said... but of course, all the festivals in this town revolve around showing off your body..."
    Villager "Aren't you worried that all the men in town will see your wife's body?"
    Leyna "W-well my body..."
    Johan "NO! I'm not worried, we were all born naked and it's completely natural!"
    Alexa "Very well said! You are absolutely right"
    AlexasHusband "..."
    Villager2 "Yeah! If you have a good body, what better than to show it off, right?"
    Johan "Well... also not..."
    Villager "Johan... you are a wise man!"
    Johan "O-okey Thank you hahaha..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(MANY MORE BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "BUah I'm pretty fucked up already... Do you know what I'm really interested in right now?"
    Leyna "Wh-hip-what do you feel like?"
    Villager "I feel like fucking"
    Leyna "!!!"
    Villager "HAHAHAHAAHA No... I really feel like going to the river to take a bath... are you in?"
    Alexa "Sure, why not? That way we can sober up a little bit"
    Johan "Yes, a cold bath would be great for me right now!"
    Leyna "But... in the river, we would all have to undress"
    Johan "Shit, true..."
    Villager "Well, as you said, it's completely natural right?"
    Johan "Well, yes..."
    Villager2 "And besides, there's trust, right Johan? It's just taking a bath and all..."
    Johan "Well, I guess you're right"
    Leyna "If JoHan AgRees, I hAve no probLem..."
    Villager "Great! (she seems to be quite drunk)"
    Johan "YES! I'm looking forward to going back to the river"
    Villager "Ehm... ahem yes, the river of course..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "LATER IN THE RIVER ..."
    Villager "Come on, everyone without clothes, otherwise the goddess will get angry"
    Johan "hahahahahaha okay let's go"
    Leyna "Okay, but give me one more shot of beer first hahaha"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV148_0_PlaySound
    $ show_picture(2, "rioleyna1")
    $ resolve_scene()
    Leyna "Ahhh how nice, how refreshing... it may be the alcohol but the truth is that being like this without worrying so much is very ... liberalizing"
    Johan "Right? Now I feel a little bad for being angry in the past"
    $ show_picture(3, "rioleyna2")
    $ resolve_scene()
    Villager "Yesssss this is all tradition here! We have no problem seeing each other naked!"
    Leyna "It's certainly very different from how we behave in the city, but I guess it's cool"
    Villager2 "Hahahahaha man, here we are all happy to see each other, especially you Leyna! What a great body!"
    Johan "hahhaha you bet! Eeven though she is my wife, I still can't get used to seeing her like this"
    $ show_picture(4, "rioleyna3")
    $ resolve_scene()
    Villager2 "Dude! You sure are glad to see Leyna!"
    Johan "Hahahaha"
    Leyna "WOW! what a big dick (!!!!!!) fu-fuck did I say that out loud? Sorry...."
    Leyna "When I drink too much I'm not myself"
    Johan "Hahaha...(Wow I didn't expect that comment from Leyna ... even though she told the truth I can't help but feel jealous... I have a weird feeling in my stomach"
    "looking at this situation... I don't know if it's because of the alcohol but... well, don't think about it too much Johan)"
    $ show_picture(5, "rioleyna4")
    $ resolve_scene()
    Villager2 "Well Leyna don't worry here we are all friends and there is trust, isn't it Johan?"
    Johan "Of course! You can admire my wife's beauty all you want! After all it's only for me hahahaha"
    Villager2 "But man, don't tell us that, we'll die of envy! hahahaha"
    Leyna "Well, I think I'm going to take a bath guys!"
    $ show_picture(6, "rioleyna5")
    $ resolve_scene()
    Villager "Wait, you're going to go like that? You should strip completely naked or you'll get your panties wet and get cold"
    Leyna "I'm just a little embarrassed, guys"
    Villager "Don't worry, we are all adults here!"
    Villager2 "Yes, we're not going to see anything we haven't seen before"
    Leyna "I guess you are right"
    $ show_picture(6, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    Johan "W-well, I don't know..."
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV148_0_PlaySound_1
    Johan "!!!!"
    Villager "Wow! Awesome! Leyna do you exercise or something?"
    Leyna "Well... I do go to the gym every week"
    Villager "Very well, let's see!"
    call PlaySound("sound", "audio/Fall.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV148_0_PlaySound_2
    Leyna "!!!"
    $ show_picture(7, "rioleyna6")
    $ resolve_scene()
    Villager "It really shows! You have a great ass! And what kind of exercises do you do at the gym?"
    Johan "Hey hey!"
    Villager "Some cycling perhaps?"
    $ show_picture(8, "rioleyna7")
    $ resolve_scene()
    Leyna "Y-yes some biking... and some rubber exercises"
    Johan "(They're ignoring me? It's like I'm not even here... and Leyna...)"
    Johan "(The penis of this man we met just is soo close to Leyna's pussy)"
    Villager2 "Wow! May I see it?"
    $ show_picture(9, "rioleyna8")
    $ resolve_scene()
    Villager "Of course, look at her thighs! She's a real sportswoman!"
    Leyna "hm!"
    Villager2 "YES... that ... firmer thighs!"
    $ show_picture(10, "rioleyna9")
    $ resolve_scene()
    Villager2 "You could teach us some exercise, the truth is that these last years I have neglected a lot my physique and I'm getting a lot of belly hahahaa"
    Villager "Yes! With this great body you have to know some really good exercises!"
    Leyna "W-well, you could..."
    Johan "(This situation is getting too long for my taste... but after the little speech about trust I said before, I don't want to yell at them now)"
    $ show_picture(11, "rioleyna10")
    $ resolve_scene()
    Villager2 "What? I'm sorry, but you speak very softly and I can't hear you"
    Leyna "!!! I.... I..."
    Johan "Ahem well Leyna... shall we take a bath?"
    $ show_picture(12, "rioleyna11")
    $ resolve_scene()
    Leyna "Y-yeah right (for a second I forgot Johan is here, thank good from where he is, he can't see that this man's penis is pressed on me)"
    Villager "Oh! yeah, we'd better go for a swim"
    Villager2 "Yes, you're right hahaha sorry Johan!"
    $ show_picture(13, "rioleyna12")
    $ resolve_scene()
    Leyna "!!!Oooh!"
    Villager2 "Oops! I slipped! We almost fell down Leyna! hahaha"
    Villager2 "Uf... my back is... my back is bad, hold me for a second"
    Johan "??? Are you okay?"
    Villager2 "Oh yes yes, just give me a second"
    $ show_picture(14, "rioleyna13")
    $ resolve_scene()
    Leyna "hmmmmm Ahhh... I... I..."
    Villager "What's wrong Leyna? Did you hurt yourself?"
    Leyna "(Johan is right there... and this man has stuck his dick all the way in... in front of my husband...)"
    Johan "Leyna?"
    $ show_picture(15, "rioleyna14")
    $ resolve_scene()
    "plop! "
    Villager2 "There you go... hahahah it's just that my back always gives me problems, everything ok Leyna? Sorry I fell on you"
    Leyna "(Heavy breathing) Ah ah ah ah.... yes ... all right... come on Johan... let's go for a swim"
    Johan "Sure! (for a second I thought that... anyway, it's just my imagination...)"
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
    call ChangePartyMember("Johan", True) from _call_TownFestivalNightEV148_0_ChangePartyMember
    call TransferPlayer("TownNight", "TownFestivalNightEV148_0", 47, 23, direction=4) from _call_TownFestivalNightEV148_0_TransferPlayer_2
    $ fade_in()
    call Movement("TownFestivalNightEV148_0", "player", ["L","L","L","TURN_R"]) from _call_TownFestivalNightEV148_0_Movement_2
    $ resolve_scene()
    Johan "It looks like everyone has already gone to sleep... We better go to sleep too"
    Leyna "Yes... you are right"
    $ fade_out()
    call TransferPlayer("Town2", "TownFestivalNightEV148_0", 28, 22, direction=0) from _call_TownFestivalNightEV148_0_TransferPlayer_3
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ fade_in()
    $ resolve_scene()
    "The next morning..."
    $ erase_picture(1)
    call Movement("TownFestivalNightEV148_0", "player", ["D","TURN_U"]) from _call_TownFestivalNightEV148_0_Movement_3
    $ resolve_scene()
    Johan "My God, I have a terrible hangover, I can hardly remember what happened yesterday"
    Johan "... We were on the river with some guys, right? I hope we didn't do anything crazy"
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Oh hahaha... Right... no, relax we didn't do anything crazy...I don't remember much either...I also have a good hangover hahaha"
    Johan "Yeah... Well, what do you feel like doing today?"
    Leyna "The truth is that I should stop by my work at the hotsprings... but I can come by later"
    Johan "Don't worry, I could use a hot bath, I could walk you over there and take a bath and then I'll do some time while you finish up"
    Leyna "You don't have to if you don't want to..."
    Johan "Don't worry! It's not a problem!"
    Leyna "W-well, let's go there"
    $ erase_picture(1)
    $ resolve_scene()
    return False

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v7_1:
    call PauseForBalloon("TownFestivalNightEV148_1") from _call_TownFestivalNightEV148_1_PauseForBalloon
    Leyna "I should look for Johan, this game has gone longer than I'd like"
    $ fade_out()
    $ set_switch("final_hideout", True)
    call GalleryViewed("rioleyna") from _call_TownFestivalNightEV148_1_GalleryViewed
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV148_1", 15, 10, direction=4) from _call_TownFestivalNightEV148_1_TransferPlayer
    $ fade_in()
    call Movement("TownFestivalNightEV148_1", "player", ["L","L","L","L","L","U","U","L","L","L"]) from _call_TownFestivalNightEV148_1_Movement
    call Movement("TownFestivalNightEV148_1", "TownFestivalNightjohan2", ["TURN_R"]) from _call_TownFestivalNightEV148_1_Movement_1
    $ resolve_scene()
    call PauseForBalloon("TownFestivalNightEV148_1") from _call_TownFestivalNightEV148_1_PauseForBalloon_1
    Johan "Leyna! I was starting to worry, I couldn't find you anywhere, everything all right?"
    Leyna "Hmm yes... everything... everything is fine! Well... Shall we go to sleep? I'm exhausted"
    Johan "Exhausted? But the night just started! We met some villagers and they invited us for a drink!"
    Alexa "Exactly Leyna! I'm sure you'll have a great time! Let's have a few beers and I'm sure you'll get over your tiredness!"
    Leyna "I don't feel like it guys..."
    Johan "Come on Leyna, it will be fun, we have worked hard these days, we deserve a night out!"
    Leyna "Okay guys... let's have a couple of beers"
    Alexa "Good!! We're meeting them for a drink nearby"
    $ fade_out()
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV148_1", 44, 39, direction=2) from _call_TownFestivalNightEV148_1_TransferPlayer_1
    call SetEventLocation("TownFestivalNightEV148_1", "TownFestivalNightalexa2", 43, 39) from _call_TownFestivalNightEV148_1_setloc
    call SetEventLocation("TownFestivalNightEV148_1", "TownFestivalNightmarido2", 43, 40) from _call_TownFestivalNightEV148_1_setloc_1
    call SetEventLocation("TownFestivalNightEV148_1", "TownFestivalNightjohan2", 45, 39) from _call_TownFestivalNightEV148_1_setloc_2
    $ fade_in()
    $ resolve_scene()
    Alexa "We are here! Did you get the beers?"
    Villager "Yes, we have plenty for the whole night"
    Johan "Great! It's been years since I've been out partying!"
    Villager2 "(Wow how lucky we are! We finally convinced the two tourist girls to come and drink! we have to make the most of it)"
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(SEVERAL BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "No, but seriously Johan, your wife is beautiful, I don't know how you can live in peace"
    Johan "Well (ugh I'm so drunk) let's see... I believe that the most important thing in a relationship is trust and I ... I trust Leyna completely"
    Villager "Very well said... but of course, all the festivals in this town revolve around showing off your body..."
    Villager "Aren't you worried that all the men in town will see your wife's body?"
    Leyna "W-well my body..."
    Johan "NO! I'm not worried, we were all born naked and it's completely natural!"
    Alexa "Very well said! You are absolutely right"
    AlexasHusband "..."
    Villager2 "Yeah! If you have a good body, what better than to show it off, right?"
    Johan "Well... also not..."
    Villager "Johan... you are a wise man!"
    Johan "O-okey Thank you hahaha..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(MANY MORE BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "BUah I'm pretty fucked up already... Do you know what I'm really interested in right now?"
    Leyna "Wh-hip-what do you feel like?"
    Villager "I feel like fucking"
    Leyna "!!!"
    Villager "HAHAHAHAAHA No... I really feel like going to the river to take a bath... are you in?"
    Alexa "Sure, why not? That way we can sober up a little bit"
    Johan "Yes, a cold bath would be great for me right now!"
    Leyna "But... in the river, we would all have to undress"
    Johan "Shit, true..."
    Villager "Well, as you said, it's completely natural right?"
    Johan "Well, yes..."
    Villager2 "And besides, there's trust, right Johan? It's just taking a bath and all..."
    Johan "Well, I guess you're right"
    Leyna "If JoHan AgRees, I hAve no probLem..."
    Villager "Great! (she seems to be quite drunk)"
    Johan "YES! I'm looking forward to going back to the river"
    Villager "Ehm... ahem yes, the river of course..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "LATER IN THE RIVER ..."
    Villager "Come on, everyone without clothes, otherwise the goddess will get angry"
    Johan "hahahahahaha okay let's go"
    Leyna "Okay, but give me one more shot of beer first hahaha"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV148_1_PlaySound
    $ show_picture(2, "rioleyna1")
    $ resolve_scene()
    Leyna "Ahhh how nice, how refreshing... it may be the alcohol but the truth is that being like this without worrying so much is very ... liberalizing"
    Johan "Right? Now I feel a little bad for being angry in the past"
    $ show_picture(3, "rioleyna2")
    $ resolve_scene()
    Villager "Yesssss this is all tradition here! We have no problem seeing each other naked!"
    Leyna "It's certainly very different from how we behave in the city, but I guess it's cool"
    Villager2 "Hahahahaha man, here we are all happy to see each other, especially you Leyna! What a great body!"
    Johan "hahhaha you bet! Eeven though she is my wife, I still can't get used to seeing her like this"
    $ show_picture(4, "rioleyna3")
    $ resolve_scene()
    Villager2 "Dude! You sure are glad to see Leyna!"
    Johan "Hahahaha"
    Leyna "WOW! what a big dick (!!!!!!) fu-fuck did I say that out loud? Sorry...."
    Leyna "When I drink too much I'm not myself"
    Johan "Hahaha...(Wow I didn't expect that comment from Leyna ... even though she told the truth I can't help but feel jealous... I have a weird feeling in my stomach"
    "looking at this situation... I don't know if it's because of the alcohol but... well, don't think about it too much Johan)"
    $ show_picture(5, "rioleyna4")
    $ resolve_scene()
    Villager2 "Well Leyna don't worry here we are all friends and there is trust, isn't it Johan?"
    Johan "Of course! You can admire my wife's beauty all you want! After all it's only for me hahahaha"
    Villager2 "But man, don't tell us that, we'll die of envy! hahahaha"
    Leyna "Well, I think I'm going to take a bath guys!"
    $ show_picture(6, "rioleyna5")
    $ resolve_scene()
    Villager "Wait, you're going to go like that? You should strip completely naked or you'll get your panties wet and get cold"
    Leyna "I'm just a little embarrassed, guys"
    Villager "Don't worry, we are all adults here!"
    Villager2 "Yes, we're not going to see anything we haven't seen before"
    Leyna "I guess you are right"
    $ show_picture(6, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    Johan "W-well, I don't know..."
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV148_1_PlaySound_1
    Johan "!!!!"
    Villager "Wow! Awesome! Leyna do you exercise or something?"
    Leyna "Well... I do go to the gym every week"
    Villager "Very well, let's see!"
    call PlaySound("sound", "audio/Fall.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV148_1_PlaySound_2
    Leyna "!!!"
    $ show_picture(7, "rioleyna6")
    $ resolve_scene()
    Villager "It really shows! You have a great ass! And what kind of exercises do you do at the gym?"
    Johan "Hey hey!"
    Villager "Some cycling perhaps?"
    $ show_picture(8, "rioleyna7")
    $ resolve_scene()
    Leyna "Y-yes some biking... and some rubber exercises"
    Johan "(They're ignoring me? It's like I'm not even here... and Leyna...)"
    Johan "(The penis of this man we met just is soo close to Leyna's pussy)"
    Villager2 "Wow! May I see it?"
    $ show_picture(9, "rioleyna8")
    $ resolve_scene()
    Villager "Of course, look at her thighs! She's a real sportswoman!"
    Leyna "hm!"
    Villager2 "YES... that ... firmer thighs!"
    $ show_picture(10, "rioleyna9")
    $ resolve_scene()
    Villager2 "You could teach us some exercise, the truth is that these last years I have neglected a lot my physique and I'm getting a lot of belly hahahaa"
    Villager "Yes! With this great body you have to know some really good exercises!"
    Leyna "W-well, you could..."
    Johan "(This situation is getting too long for my taste... but after the little speech about trust I said before, I don't want to yell at them now)"
    $ show_picture(11, "rioleyna10")
    $ resolve_scene()
    Villager2 "What? I'm sorry, but you speak very softly and I can't hear you"
    Leyna "!!! I.... I..."
    Johan "Ahem well Leyna... shall we take a bath?"
    $ show_picture(12, "rioleyna11")
    $ resolve_scene()
    Leyna "Y-yeah right (for a second I forgot Johan is here, thank good from where he is, he can't see that this man's penis is pressed on me)"
    Villager "Oh! yeah, we'd better go for a swim"
    Villager2 "Yes, you're right hahaha sorry Johan!"
    $ show_picture(13, "rioleyna12")
    $ resolve_scene()
    Leyna "!!!Oooh!"
    Villager2 "Oops! I slipped! We almost fell down Leyna! hahaha"
    Villager2 "Uf... my back is... my back is bad, hold me for a second"
    Johan "??? Are you okay?"
    Villager2 "Oh yes yes, just give me a second"
    $ show_picture(14, "rioleyna13")
    $ resolve_scene()
    Leyna "hmmmmm Ahhh... I... I..."
    Villager "What's wrong Leyna? Did you hurt yourself?"
    Leyna "(Johan is right there... and this man has stuck his dick all the way in... in front of my husband...)"
    Johan "Leyna?"
    $ show_picture(15, "rioleyna14")
    $ resolve_scene()
    "plop! "
    Villager2 "There you go... hahahah it's just that my back always gives me problems, everything ok Leyna? Sorry I fell on you"
    Leyna "(Heavy breathing) Ah ah ah ah.... yes ... all right... come on Johan... let's go for a swim"
    Johan "Sure! (for a second I thought that... anyway, it's just my imagination...)"
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
    call ChangePartyMember("Johan", True) from _call_TownFestivalNightEV148_1_ChangePartyMember
    call TransferPlayer("TownNight", "TownFestivalNightEV148_1", 47, 23, direction=4) from _call_TownFestivalNightEV148_1_TransferPlayer_2
    $ fade_in()
    call Movement("TownFestivalNightEV148_1", "player", ["L","L","L","TURN_R"]) from _call_TownFestivalNightEV148_1_Movement_2
    $ resolve_scene()
    Johan "It looks like everyone has already gone to sleep... We better go to sleep too"
    Leyna "Yes... you are right"
    $ fade_out()
    call TransferPlayer("Town2", "TownFestivalNightEV148_1", 28, 22, direction=0) from _call_TownFestivalNightEV148_1_TransferPlayer_3
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ fade_in()
    $ resolve_scene()
    "The next morning..."
    $ erase_picture(1)
    call Movement("TownFestivalNightEV148_1", "player", ["D","TURN_U"]) from _call_TownFestivalNightEV148_1_Movement_3
    $ resolve_scene()
    Johan "My God, I have a terrible hangover, I can hardly remember what happened yesterday"
    Johan "... We were on the river with some guys, right? I hope we didn't do anything crazy"
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Oh hahaha... Right... no, relax we didn't do anything crazy...I don't remember much either...I also have a good hangover hahaha"
    Johan "Yeah... Well, what do you feel like doing today?"
    Leyna "The truth is that I should stop by my work at the hotsprings... but I can come by later"
    Johan "Don't worry, I could use a hot bath, I could walk you over there and take a bath and then I'll do some time while you finish up"
    Leyna "You don't have to if you don't want to..."
    Johan "Don't worry! It's not a problem!"
    Leyna "W-well, let's go there"
    $ erase_picture(1)
    $ resolve_scene()
    return False

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v7(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v7"):
        return None
    elif trigger == "event" and hiding_place >= 4:
        call PlayEvent(play_event, "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v7_1", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v7") from _call_TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v7_1_PlayEvent
        return (0, "", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v7_1")
    elif trigger == "event" and hiding_place >= 3:
        call PlayEvent(play_event, "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v7_0", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v7") from _call_TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v7_0_PlayEvent
        return (0, "", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v7_0")
    return None

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v8_0:
    call PauseForBalloon("TownFestivalNightEV149_0") from _call_TownFestivalNightEV149_0_PauseForBalloon
    Leyna "I should look for Johan, this game has gone longer than I'd like"
    $ fade_out()
    $ set_switch("final_hideout", True)
    call GalleryViewed("rioleyna") from _call_TownFestivalNightEV149_0_GalleryViewed
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV149_0", 15, 10, direction=4) from _call_TownFestivalNightEV149_0_TransferPlayer
    $ fade_in()
    call Movement("TownFestivalNightEV149_0", "player", ["L","L","L","L","L","U","U","L","L","L"]) from _call_TownFestivalNightEV149_0_Movement
    call Movement("TownFestivalNightEV149_0", "TownFestivalNightjohan2", ["TURN_R"]) from _call_TownFestivalNightEV149_0_Movement_1
    $ resolve_scene()
    call PauseForBalloon("TownFestivalNightEV149_0") from _call_TownFestivalNightEV149_0_PauseForBalloon_1
    Johan "Leyna! I was starting to worry, I couldn't find you anywhere, everything all right?"
    Leyna "Hmm yes... everything... everything is fine! Well... Shall we go to sleep? I'm exhausted"
    Johan "Exhausted? But the night just started! We met some villagers and they invited us for a drink!"
    Alexa "Exactly Leyna! I'm sure you'll have a great time! Let's have a few beers and I'm sure you'll get over your tiredness!"
    Leyna "I don't feel like it guys..."
    Johan "Come on Leyna, it will be fun, we have worked hard these days, we deserve a night out!"
    Leyna "Okay guys... let's have a couple of beers"
    Alexa "Good!! We're meeting them for a drink nearby"
    $ fade_out()
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV149_0", 44, 39, direction=2) from _call_TownFestivalNightEV149_0_TransferPlayer_1
    call SetEventLocation("TownFestivalNightEV149_0", "TownFestivalNightalexa2", 43, 39) from _call_TownFestivalNightEV149_0_setloc
    call SetEventLocation("TownFestivalNightEV149_0", "TownFestivalNightmarido2", 43, 40) from _call_TownFestivalNightEV149_0_setloc_1
    call SetEventLocation("TownFestivalNightEV149_0", "TownFestivalNightjohan2", 45, 39) from _call_TownFestivalNightEV149_0_setloc_2
    $ fade_in()
    $ resolve_scene()
    Alexa "We are here! Did you get the beers?"
    Villager "Yes, we have plenty for the whole night"
    Johan "Great! It's been years since I've been out partying!"
    Villager2 "(Wow how lucky we are! We finally convinced the two tourist girls to come and drink! we have to make the most of it)"
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(SEVERAL BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "No, but seriously Johan, your wife is beautiful, I don't know how you can live in peace"
    Johan "Well (ugh I'm so drunk) let's see... I believe that the most important thing in a relationship is trust and I ... I trust Leyna completely"
    Villager "Very well said... but of course, all the festivals in this town revolve around showing off your body..."
    Villager "Aren't you worried that all the men in town will see your wife's body?"
    Leyna "W-well my body..."
    Johan "NO! I'm not worried, we were all born naked and it's completely natural!"
    Alexa "Very well said! You are absolutely right"
    AlexasHusband "..."
    Villager2 "Yeah! If you have a good body, what better than to show it off, right?"
    Johan "Well... also not..."
    Villager "Johan... you are a wise man!"
    Johan "O-okey Thank you hahaha..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(MANY MORE BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "BUah I'm pretty fucked up already... Do you know what I'm really interested in right now?"
    Leyna "Wh-hip-what do you feel like?"
    Villager "I feel like fucking"
    Leyna "!!!"
    Villager "HAHAHAHAAHA No... I really feel like going to the river to take a bath... are you in?"
    Alexa "Sure, why not? That way we can sober up a little bit"
    Johan "Yes, a cold bath would be great for me right now!"
    Leyna "But... in the river, we would all have to undress"
    Johan "Shit, true..."
    Villager "Well, as you said, it's completely natural right?"
    Johan "Well, yes..."
    Villager2 "And besides, there's trust, right Johan? It's just taking a bath and all..."
    Johan "Well, I guess you're right"
    Leyna "If JoHan AgRees, I hAve no probLem..."
    Villager "Great! (she seems to be quite drunk)"
    Johan "YES! I'm looking forward to going back to the river"
    Villager "Ehm... ahem yes, the river of course..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "LATER IN THE RIVER ..."
    Villager "Come on, everyone without clothes, otherwise the goddess will get angry"
    Johan "hahahahahaha okay let's go"
    Leyna "Okay, but give me one more shot of beer first hahaha"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV149_0_PlaySound
    $ show_picture(2, "rioleyna1")
    $ resolve_scene()
    Leyna "Ahhh how nice, how refreshing... it may be the alcohol but the truth is that being like this without worrying so much is very ... liberalizing"
    Johan "Right? Now I feel a little bad for being angry in the past"
    $ show_picture(3, "rioleyna2")
    $ resolve_scene()
    Villager "Yesssss this is all tradition here! We have no problem seeing each other naked!"
    Leyna "It's certainly very different from how we behave in the city, but I guess it's cool"
    Villager2 "Hahahahaha man, here we are all happy to see each other, especially you Leyna! What a great body!"
    Johan "hahhaha you bet! Eeven though she is my wife, I still can't get used to seeing her like this"
    $ show_picture(4, "rioleyna3")
    $ resolve_scene()
    Villager2 "Dude! You sure are glad to see Leyna!"
    Johan "Hahahaha"
    Leyna "WOW! what a big dick (!!!!!!) fu-fuck did I say that out loud? Sorry...."
    Leyna "When I drink too much I'm not myself"
    Johan "Hahaha...(Wow I didn't expect that comment from Leyna ... even though she told the truth I can't help but feel jealous... I have a weird feeling in my stomach"
    "looking at this situation... I don't know if it's because of the alcohol but... well, don't think about it too much Johan)"
    $ show_picture(5, "rioleyna4")
    $ resolve_scene()
    Villager2 "Well Leyna don't worry here we are all friends and there is trust, isn't it Johan?"
    Johan "Of course! You can admire my wife's beauty all you want! After all it's only for me hahahaha"
    Villager2 "But man, don't tell us that, we'll die of envy! hahahaha"
    Leyna "Well, I think I'm going to take a bath guys!"
    $ show_picture(6, "rioleyna5")
    $ resolve_scene()
    Villager "Wait, you're going to go like that? You should strip completely naked or you'll get your panties wet and get cold"
    Leyna "I'm just a little embarrassed, guys"
    Villager "Don't worry, we are all adults here!"
    Villager2 "Yes, we're not going to see anything we haven't seen before"
    Leyna "I guess you are right"
    $ show_picture(6, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    Johan "W-well, I don't know..."
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV149_0_PlaySound_1
    Johan "!!!!"
    Villager "Wow! Awesome! Leyna do you exercise or something?"
    Leyna "Well... I do go to the gym every week"
    Villager "Very well, let's see!"
    call PlaySound("sound", "audio/Fall.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV149_0_PlaySound_2
    Leyna "!!!"
    $ show_picture(7, "rioleyna6")
    $ resolve_scene()
    Villager "It really shows! You have a great ass! And what kind of exercises do you do at the gym?"
    Johan "Hey hey!"
    Villager "Some cycling perhaps?"
    $ show_picture(8, "rioleyna7")
    $ resolve_scene()
    Leyna "Y-yes some biking... and some rubber exercises"
    Johan "(They're ignoring me? It's like I'm not even here... and Leyna...)"
    Johan "(The penis of this man we met just is soo close to Leyna's pussy)"
    Villager2 "Wow! May I see it?"
    $ show_picture(9, "rioleyna8")
    $ resolve_scene()
    Villager "Of course, look at her thighs! She's a real sportswoman!"
    Leyna "hm!"
    Villager2 "YES... that ... firmer thighs!"
    $ show_picture(10, "rioleyna9")
    $ resolve_scene()
    Villager2 "You could teach us some exercise, the truth is that these last years I have neglected a lot my physique and I'm getting a lot of belly hahahaa"
    Villager "Yes! With this great body you have to know some really good exercises!"
    Leyna "W-well, you could..."
    Johan "(This situation is getting too long for my taste... but after the little speech about trust I said before, I don't want to yell at them now)"
    $ show_picture(11, "rioleyna10")
    $ resolve_scene()
    Villager2 "What? I'm sorry, but you speak very softly and I can't hear you"
    Leyna "!!! I.... I..."
    Johan "Ahem well Leyna... shall we take a bath?"
    $ show_picture(12, "rioleyna11")
    $ resolve_scene()
    Leyna "Y-yeah right (for a second I forgot Johan is here, thank good from where he is, he can't see that this man's penis is pressed on me)"
    Villager "Oh! yeah, we'd better go for a swim"
    Villager2 "Yes, you're right hahaha sorry Johan!"
    $ show_picture(13, "rioleyna12")
    $ resolve_scene()
    Leyna "!!!Oooh!"
    Villager2 "Oops! I slipped! We almost fell down Leyna! hahaha"
    Villager2 "Uf... my back is... my back is bad, hold me for a second"
    Johan "??? Are you okay?"
    Villager2 "Oh yes yes, just give me a second"
    $ show_picture(14, "rioleyna13")
    $ resolve_scene()
    Leyna "hmmmmm Ahhh... I... I..."
    Villager "What's wrong Leyna? Did you hurt yourself?"
    Leyna "(Johan is right there... and this man has stuck his dick all the way in... in front of my husband...)"
    Johan "Leyna?"
    $ show_picture(15, "rioleyna14")
    $ resolve_scene()
    "plop! "
    Villager2 "There you go... hahahah it's just that my back always gives me problems, everything ok Leyna? Sorry I fell on you"
    Leyna "(Heavy breathing) Ah ah ah ah.... yes ... all right... come on Johan... let's go for a swim"
    Johan "Sure! (for a second I thought that... anyway, it's just my imagination...)"
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
    call ChangePartyMember("Johan", True) from _call_TownFestivalNightEV149_0_ChangePartyMember
    call TransferPlayer("TownNight", "TownFestivalNightEV149_0", 47, 23, direction=4) from _call_TownFestivalNightEV149_0_TransferPlayer_2
    $ fade_in()
    call Movement("TownFestivalNightEV149_0", "player", ["L","L","L","TURN_R"]) from _call_TownFestivalNightEV149_0_Movement_2
    $ resolve_scene()
    Johan "It looks like everyone has already gone to sleep... We better go to sleep too"
    Leyna "Yes... you are right"
    $ fade_out()
    call TransferPlayer("Town2", "TownFestivalNightEV149_0", 28, 22, direction=0) from _call_TownFestivalNightEV149_0_TransferPlayer_3
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ fade_in()
    $ resolve_scene()
    "The next morning..."
    $ erase_picture(1)
    call Movement("TownFestivalNightEV149_0", "player", ["D","TURN_U"]) from _call_TownFestivalNightEV149_0_Movement_3
    $ resolve_scene()
    Johan "My God, I have a terrible hangover, I can hardly remember what happened yesterday"
    Johan "... We were on the river with some guys, right? I hope we didn't do anything crazy"
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Oh hahaha... Right... no, relax we didn't do anything crazy...I don't remember much either...I also have a good hangover hahaha"
    Johan "Yeah... Well, what do you feel like doing today?"
    Leyna "The truth is that I should stop by my work at the hotsprings... but I can come by later"
    Johan "Don't worry, I could use a hot bath, I could walk you over there and take a bath and then I'll do some time while you finish up"
    Leyna "You don't have to if you don't want to..."
    Johan "Don't worry! It's not a problem!"
    Leyna "W-well, let's go there"
    $ erase_picture(1)
    $ resolve_scene()
    return False

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v8_1:
    call PauseForBalloon("TownFestivalNightEV149_1") from _call_TownFestivalNightEV149_1_PauseForBalloon
    Leyna "I should look for Johan, this game has gone longer than I'd like"
    $ fade_out()
    $ set_switch("final_hideout", True)
    call GalleryViewed("rioleyna") from _call_TownFestivalNightEV149_1_GalleryViewed
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV149_1", 15, 10, direction=4) from _call_TownFestivalNightEV149_1_TransferPlayer
    $ fade_in()
    call Movement("TownFestivalNightEV149_1", "player", ["L","L","L","L","L","U","U","L","L","L"]) from _call_TownFestivalNightEV149_1_Movement
    call Movement("TownFestivalNightEV149_1", "TownFestivalNightjohan2", ["TURN_R"]) from _call_TownFestivalNightEV149_1_Movement_1
    $ resolve_scene()
    call PauseForBalloon("TownFestivalNightEV149_1") from _call_TownFestivalNightEV149_1_PauseForBalloon_1
    Johan "Leyna! I was starting to worry, I couldn't find you anywhere, everything all right?"
    Leyna "Hmm yes... everything... everything is fine! Well... Shall we go to sleep? I'm exhausted"
    Johan "Exhausted? But the night just started! We met some villagers and they invited us for a drink!"
    Alexa "Exactly Leyna! I'm sure you'll have a great time! Let's have a few beers and I'm sure you'll get over your tiredness!"
    Leyna "I don't feel like it guys..."
    Johan "Come on Leyna, it will be fun, we have worked hard these days, we deserve a night out!"
    Leyna "Okay guys... let's have a couple of beers"
    Alexa "Good!! We're meeting them for a drink nearby"
    $ fade_out()
    call TransferPlayer("TownFestivalNight", "TownFestivalNightEV149_1", 44, 39, direction=2) from _call_TownFestivalNightEV149_1_TransferPlayer_1
    call SetEventLocation("TownFestivalNightEV149_1", "TownFestivalNightalexa2", 43, 39) from _call_TownFestivalNightEV149_1_setloc
    call SetEventLocation("TownFestivalNightEV149_1", "TownFestivalNightmarido2", 43, 40) from _call_TownFestivalNightEV149_1_setloc_1
    call SetEventLocation("TownFestivalNightEV149_1", "TownFestivalNightjohan2", 45, 39) from _call_TownFestivalNightEV149_1_setloc_2
    $ fade_in()
    $ resolve_scene()
    Alexa "We are here! Did you get the beers?"
    Villager "Yes, we have plenty for the whole night"
    Johan "Great! It's been years since I've been out partying!"
    Villager2 "(Wow how lucky we are! We finally convinced the two tourist girls to come and drink! we have to make the most of it)"
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(SEVERAL BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "No, but seriously Johan, your wife is beautiful, I don't know how you can live in peace"
    Johan "Well (ugh I'm so drunk) let's see... I believe that the most important thing in a relationship is trust and I ... I trust Leyna completely"
    Villager "Very well said... but of course, all the festivals in this town revolve around showing off your body..."
    Villager "Aren't you worried that all the men in town will see your wife's body?"
    Leyna "W-well my body..."
    Johan "NO! I'm not worried, we were all born naked and it's completely natural!"
    Alexa "Very well said! You are absolutely right"
    AlexasHusband "..."
    Villager2 "Yeah! If you have a good body, what better than to show it off, right?"
    Johan "Well... also not..."
    Villager "Johan... you are a wise man!"
    Johan "O-okey Thank you hahaha..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "(MANY MORE BEERS LATER)"
    $ erase_picture(1)
    $ resolve_scene()
    Villager "BUah I'm pretty fucked up already... Do you know what I'm really interested in right now?"
    Leyna "Wh-hip-what do you feel like?"
    Villager "I feel like fucking"
    Leyna "!!!"
    Villager "HAHAHAHAAHA No... I really feel like going to the river to take a bath... are you in?"
    Alexa "Sure, why not? That way we can sober up a little bit"
    Johan "Yes, a cold bath would be great for me right now!"
    Leyna "But... in the river, we would all have to undress"
    Johan "Shit, true..."
    Villager "Well, as you said, it's completely natural right?"
    Johan "Well, yes..."
    Villager2 "And besides, there's trust, right Johan? It's just taking a bath and all..."
    Johan "Well, I guess you're right"
    Leyna "If JoHan AgRees, I hAve no probLem..."
    Villager "Great! (she seems to be quite drunk)"
    Johan "YES! I'm looking forward to going back to the river"
    Villager "Ehm... ahem yes, the river of course..."
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "LATER IN THE RIVER ..."
    Villager "Come on, everyone without clothes, otherwise the goddess will get angry"
    Johan "hahahahahaha okay let's go"
    Leyna "Okay, but give me one more shot of beer first hahaha"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV149_1_PlaySound
    $ show_picture(2, "rioleyna1")
    $ resolve_scene()
    Leyna "Ahhh how nice, how refreshing... it may be the alcohol but the truth is that being like this without worrying so much is very ... liberalizing"
    Johan "Right? Now I feel a little bad for being angry in the past"
    $ show_picture(3, "rioleyna2")
    $ resolve_scene()
    Villager "Yesssss this is all tradition here! We have no problem seeing each other naked!"
    Leyna "It's certainly very different from how we behave in the city, but I guess it's cool"
    Villager2 "Hahahahaha man, here we are all happy to see each other, especially you Leyna! What a great body!"
    Johan "hahhaha you bet! Eeven though she is my wife, I still can't get used to seeing her like this"
    $ show_picture(4, "rioleyna3")
    $ resolve_scene()
    Villager2 "Dude! You sure are glad to see Leyna!"
    Johan "Hahahaha"
    Leyna "WOW! what a big dick (!!!!!!) fu-fuck did I say that out loud? Sorry...."
    Leyna "When I drink too much I'm not myself"
    Johan "Hahaha...(Wow I didn't expect that comment from Leyna ... even though she told the truth I can't help but feel jealous... I have a weird feeling in my stomach"
    "looking at this situation... I don't know if it's because of the alcohol but... well, don't think about it too much Johan)"
    $ show_picture(5, "rioleyna4")
    $ resolve_scene()
    Villager2 "Well Leyna don't worry here we are all friends and there is trust, isn't it Johan?"
    Johan "Of course! You can admire my wife's beauty all you want! After all it's only for me hahahaha"
    Villager2 "But man, don't tell us that, we'll die of envy! hahahaha"
    Leyna "Well, I think I'm going to take a bath guys!"
    $ show_picture(6, "rioleyna5")
    $ resolve_scene()
    Villager "Wait, you're going to go like that? You should strip completely naked or you'll get your panties wet and get cold"
    Leyna "I'm just a little embarrassed, guys"
    Villager "Don't worry, we are all adults here!"
    Villager2 "Yes, we're not going to see anything we haven't seen before"
    Leyna "I guess you are right"
    $ show_picture(6, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    Johan "W-well, I don't know..."
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV149_1_PlaySound_1
    Johan "!!!!"
    Villager "Wow! Awesome! Leyna do you exercise or something?"
    Leyna "Well... I do go to the gym every week"
    Villager "Very well, let's see!"
    call PlaySound("sound", "audio/Fall.ogg", volume=0.9, no_loop=True) from _call_TownFestivalNightEV149_1_PlaySound_2
    Leyna "!!!"
    $ show_picture(7, "rioleyna6")
    $ resolve_scene()
    Villager "It really shows! You have a great ass! And what kind of exercises do you do at the gym?"
    Johan "Hey hey!"
    Villager "Some cycling perhaps?"
    $ show_picture(8, "rioleyna7")
    $ resolve_scene()
    Leyna "Y-yes some biking... and some rubber exercises"
    Johan "(They're ignoring me? It's like I'm not even here... and Leyna...)"
    Johan "(The penis of this man we met just is soo close to Leyna's pussy)"
    Villager2 "Wow! May I see it?"
    $ show_picture(9, "rioleyna8")
    $ resolve_scene()
    Villager "Of course, look at her thighs! She's a real sportswoman!"
    Leyna "hm!"
    Villager2 "YES... that ... firmer thighs!"
    $ show_picture(10, "rioleyna9")
    $ resolve_scene()
    Villager2 "You could teach us some exercise, the truth is that these last years I have neglected a lot my physique and I'm getting a lot of belly hahahaa"
    Villager "Yes! With this great body you have to know some really good exercises!"
    Leyna "W-well, you could..."
    Johan "(This situation is getting too long for my taste... but after the little speech about trust I said before, I don't want to yell at them now)"
    $ show_picture(11, "rioleyna10")
    $ resolve_scene()
    Villager2 "What? I'm sorry, but you speak very softly and I can't hear you"
    Leyna "!!! I.... I..."
    Johan "Ahem well Leyna... shall we take a bath?"
    $ show_picture(12, "rioleyna11")
    $ resolve_scene()
    Leyna "Y-yeah right (for a second I forgot Johan is here, thank good from where he is, he can't see that this man's penis is pressed on me)"
    Villager "Oh! yeah, we'd better go for a swim"
    Villager2 "Yes, you're right hahaha sorry Johan!"
    $ show_picture(13, "rioleyna12")
    $ resolve_scene()
    Leyna "!!!Oooh!"
    Villager2 "Oops! I slipped! We almost fell down Leyna! hahaha"
    Villager2 "Uf... my back is... my back is bad, hold me for a second"
    Johan "??? Are you okay?"
    Villager2 "Oh yes yes, just give me a second"
    $ show_picture(14, "rioleyna13")
    $ resolve_scene()
    Leyna "hmmmmm Ahhh... I... I..."
    Villager "What's wrong Leyna? Did you hurt yourself?"
    Leyna "(Johan is right there... and this man has stuck his dick all the way in... in front of my husband...)"
    Johan "Leyna?"
    $ show_picture(15, "rioleyna14")
    $ resolve_scene()
    "plop! "
    Villager2 "There you go... hahahah it's just that my back always gives me problems, everything ok Leyna? Sorry I fell on you"
    Leyna "(Heavy breathing) Ah ah ah ah.... yes ... all right... come on Johan... let's go for a swim"
    Johan "Sure! (for a second I thought that... anyway, it's just my imagination...)"
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
    call ChangePartyMember("Johan", True) from _call_TownFestivalNightEV149_1_ChangePartyMember
    call TransferPlayer("TownNight", "TownFestivalNightEV149_1", 47, 23, direction=4) from _call_TownFestivalNightEV149_1_TransferPlayer_2
    $ fade_in()
    call Movement("TownFestivalNightEV149_1", "player", ["L","L","L","TURN_R"]) from _call_TownFestivalNightEV149_1_Movement_2
    $ resolve_scene()
    Johan "It looks like everyone has already gone to sleep... We better go to sleep too"
    Leyna "Yes... you are right"
    $ fade_out()
    call TransferPlayer("Town2", "TownFestivalNightEV149_1", 28, 22, direction=0) from _call_TownFestivalNightEV149_1_TransferPlayer_3
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ fade_in()
    $ resolve_scene()
    "The next morning..."
    $ erase_picture(1)
    call Movement("TownFestivalNightEV149_1", "player", ["D","TURN_U"]) from _call_TownFestivalNightEV149_1_Movement_3
    $ resolve_scene()
    Johan "My God, I have a terrible hangover, I can hardly remember what happened yesterday"
    Johan "... We were on the river with some guys, right? I hope we didn't do anything crazy"
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Oh hahaha... Right... no, relax we didn't do anything crazy...I don't remember much either...I also have a good hangover hahaha"
    Johan "Yeah... Well, what do you feel like doing today?"
    Leyna "The truth is that I should stop by my work at the hotsprings... but I can come by later"
    Johan "Don't worry, I could use a hot bath, I could walk you over there and take a bath and then I'll do some time while you finish up"
    Leyna "You don't have to if you don't want to..."
    Johan "Don't worry! It's not a problem!"
    Leyna "W-well, let's go there"
    $ erase_picture(1)
    $ resolve_scene()
    return False

label TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v8(play_event = True, trigger = None): # event
    if is_erased("TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v8"):
        return None
    elif trigger == "event" and hiding_place >= 4:
        call PlayEvent(play_event, "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v8_1", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v8") from _call_TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v8_1_PlayEvent
        return (0, "", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v8_1")
    elif trigger == "event" and hiding_place >= 3:
        call PlayEvent(play_event, "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v8_0", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v8") from _call_TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v8_0_PlayEvent
        return (0, "", "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_v8_0")
    return None

