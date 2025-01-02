label start:
    stop music fadeout 1.0
    scene black
    call PlayEntireGame from _call_PlayEntireGame 
    return

label PlayEntireGame:
    call PlayIntro from _call_PlayIntro
    call PlayDay1 from _call_PlayDay1
    call PlayDay2 from _call_PlayDay2
    call PlayDay3 from _call_PlayDay3
    call PlayDay4 from _call_PlayDay4
    call PlayDay5 from _call_PlayDay5
    call PlayDay6 from _call_PlayDay6
    call PlayDay7 from _call_PlayDay7
    call PlayFinalDay from _call_PlayFinalDay
    show text "end of content"
    pause
    hide text
    return

label PlayIntro:
    # apartment intro
    call SetPlayerLocation("Intro") from _call_SetPlayerLocation_Intro
    call IntroOhHelloThere from _call_IntroOhHelloThere
    call ApartmentNPCMUJER_0 from _call_ApartmentNPCMUJER_0
    call ApartmentORDENADOR from _call_ApartmentORDENADOR
    # town intro
    call SetPlayerLocation("Town") from _call_SetPlayerLocation_Town
    call TownEntranceparadabus_0 from _call_TownEntranceparadabus_0
    call TownNPCCop_0 from _call_TownNPCCop_0
    call Innposadero_0 from _call_Innposadero_0
    call InnRoomsDEJANDOlasmaletas_0 from _call_InnRoomsDEJANDOlasmaletas_0
    scene black
    call Innposadero_1 from _call_Innposadero_1
    return

label PlayDay1:
    # bar 1
    call SetPlayerLocation("Bar") from _call_SetPlayerLocation_BarDay1
    call BarWetTShirt_0 from _call_BarWetTShirt_0
    scene black
    # merchant
    call SetPlayerLocation("Town") from _call_SetPlayerLocation_TownDay1
    call TownMerchant_0 from _call_TownMerchant_0
    call TownSkirtLift_0 from _call_TownSkirtLift_0
    # villagers
    call Towneventolemetenmanobarrio_0 from _call_Towneventolemetenmanobarrio_0
    # river
    call SetPlayerLocation("River") from _call_SetPlayerLocation_RiverDay1
    label RiverDay1:
        call Riverentradario_0 from _call_Riverentradario_0
        if player_location != "River":
            jump RiverDay1
    call RiverNPCEventMan from _call_RiverNPCEventMan
    call Townfinaldelprimerdia_0 from _call_Townfinaldelprimerdia_0
    return

label PlayDay2:
    # photographer 1
    call SetPlayerLocation("Town") from _call_SetPlayerLocation_TownDay2
    label PhotographerDay2:
        call Towneventofotografiaintro_0 from _call_Towneventofotografiaintro_0
        if player_location != "PhotographersHouse":
            jump PhotographerDay2
    call PhotographersHousesesionfotografica1 from _call_PhotographersHousesesionfotografica1
    # hotsprings
    call SetPlayerLocation("Reception") from _call_SetPlayerLocation_ReceptionDay2
    call Receptioneventohotsprings_0 from _call_Receptioneventohotsprings_0
    call HotSpringshotspringseventopart2 from _call_HotSpringshotspringseventopart2
    # photographer 2
    call SetPlayerLocation("Town") from _call_SetPlayerLocation_TownDay2_2
    call Townfotografo_1 from _call_Townfotografo_1
    call SetPlayerLocation("ClothingStore") from _call_SetPlayerLocation_ClothingStoreDay2
    call ClothingStoreHeyThere_1 from _call_ClothingStoreHeyThere_1
    call SetPlayerLocation("Town") from _call_SetPlayerLocation_TownDay2_3
    call Townfotografo_3 from _call_Townfotografo_3
    call Photoshoot2Sesionfotografica2 from _call_Photoshoot2Sesionfotografica2
    # bar 2
    call SetPlayerLocation("Bar") from _call_SetPlayerLocation_BarDay2
    label BarDay2:
        call BarBJGame_0 from _call_BarBJGame_0
        if player_location != "Town":
            jump BarDay2
    # river 2
    call SetPlayerLocation("Town") from _call_SetPlayerLocation_TownDay2_4
    call TownMeetAlexa_0 from _call_TownMeetAlexa_0
    label ReturnToAlexa:
        if player_location != "River2":
            call TownNPCwoman_2 from _call_TownNPCwoman_2
            jump ReturnToAlexa
    call River2ThisPlaceIsBeautiful from _call_River2ThisPlaceIsBeautiful
    # inn night
    call SetPlayerLocation("InnNight") from _call_SetPlayerLocation_InnNightDay2
    call InnNightentradaalaposadanoche_0 from _call_InnNightentradaalaposadanoche_0
    return

label PlayDay3:
    # photographer 3
    call SetPlayerLocation("Town2") from _call_SetPlayerLocation_Town2Day3
    call Town2MeetPhotographer_0 from _call_Town2MeetPhotographer_0
    call Town2fotografo_1 from _call_Town2fotografo_1
    # worker's quest
    call SetPlayerLocation("Path") from _call_SetPlayerLocation_PathDay3
    call PathNPCFestivalWorker_0 from _call_PathNPCFestivalWorker_0
    call SetPlayerLocation("Town2") from _call_SetPlayerLocation_Town2Day3_2
    call Town2NPCWorkersSon_0 from _call_Town2NPCWorkersSon_0
    call SetPlayerLocation("FoodStore") from _call_SetPlayerLocation_FoodStoreDay3
    call FoodStoreYouWonANewObject_0 from _call_FoodStoreYouWonANewObject_0
    call SetPlayerLocation("Path") from _call_SetPlayerLocation_PathDay3_2
    call PathNPCFestivalWorker_2 from _call_PathNPCFestivalWorker_2
    # dresser
    call SetPlayerLocation("ClothingStore") from _call_SetPlayerLocation_ClothingStoreDay3
    call ClothingStoreHeyThere_2 from _call_ClothingStoreHeyThere_2
    call ClothingStoreIShouldComeBackLaterToTryTheFestivalClothes_1 from _call_ClothingStoreIShouldComeBackLaterToTryTheFestivalClothes_1
    call SetPlayerLocation("Festival") from _call_SetPlayerLocation_FestivalDay3
    call Festivalworkerdentrofestival_0 from _call_Festivalworkerdentrofestival_0
    call Festivalworkerdentrofestival_1 from _call_Festivalworkerdentrofestival_1
    # Day 3 night
    call SetPlayerLocation("InnRooms") from _call_SetPlayerLocation_InnRoomsDay3
    label Day3DayTime:
        call InnRoomsSleep_0 from _call_InnRoomsSleep_0
        if player_location != "InnRoomsNight":
            jump Day3DayTime
    call SetPlayerLocation("TownNight") from _call_SetPlayerLocation_TownNightDay3
    call TownNightEhhhYouuuuuuuuu_0 from _call_TownNightEhhhYouuuuuuuuu_0
    # The dream
    call SetPlayerLocation("InnRooms") from _call_SetPlayerLocation_InnRoomsDay3_2
    call InnRoomssueojohan_0 from _call_InnRoomssueojohan_0
    # Police station
    call SetPlayerLocation("PoliceStation") from _call_SetPlayerLocation_PoliceStationDay3
    call PoliceStationeventocomisaria_0 from _call_PoliceStationeventocomisaria_0
    # Night Party
    call SetPlayerLocation("FoodStore") from _call_SetPlayerLocation_FoodStoreDay3_2
    call FoodStoreMerchant_1 from _call_FoodStoreMerchant_1
    call SetPlayerLocation("InnRooms") from _call_SetPlayerLocation_InnRoomsDay3_3  
    label Day3DayTime2:
        call InnRoomsSleep_0 from _call_InnRoomsSleep_0_2
        if player_location != "InnRoomsNight":
            jump Day3DayTime2
    call SetPlayerLocation("TownNight") from _call_SetPlayerLocation_TownNightDay3_2
    call TownNightEhhhYouuuuuuuuu_2 from _call_TownNightEhhhYouuuuuuuuu_2
    return

label PlayDay4:
    call SetPlayerLocation("Path") from _call_SetPlayerLocation_PathDay4
    call Pathnpcentradafestivalcamino_4 from _call_Pathnpcentradafestivalcamino_4
    call SetPlayerLocation("Festival") from _call_SetPlayerLocation_FestivalDay4
    call Festivalintrofestival_0 from _call_Festivalintrofestival_0
    call SetPlayerLocation("Mountains") from _call_SetPlayerLocation_MountainsDay4
    call MountainsWowThisPlaceIsBeautiful_0 from _call_MountainsWowThisPlaceIsBeautiful_0
    call Festivalintrosorteo_0 from _call_Festivalintrosorteo_0
    call Casinohombredelasuerte from _call_Casinohombredelasuerte
    call FestivalPhotoSession_0 from _call_FestivalPhotoSession_0
    call FestivalFoodStand_0 from _call_FestivalFoodStand_0
    call SetPlayerLocation("MassageParlor") from _call_SetPlayerLocation_MassageParlorDay4
    call MassageParlorICantWaitToHaveARelaxingMassage_0 from _call_MassageParlorICantWaitToHaveARelaxingMassage_0
    call InnNightSleep from _call_InnNightSleep
    return

label PlayDay5:
    # groceries store
    call SetPlayerLocation("FoodStore") from _call_SetPlayerLocation_FoodStoreDay5
    call FoodStoreMerchant_3 from _call_FoodStoreMerchant_3
    # bar
    call SetPlayerLocation("Bar2") from _call_SetPlayerLocation_Bar2Day5
    call Bar2barman_1 from _call_Bar2barman_1
    # photographer
    call SetPlayerLocation("Town2") from _call_SetPlayerLocation_Town2Day5
    call Town2fotografo_4 from _call_Town2fotografo_4
    # hot springs
    call SetPlayerLocation("Reception") from _call_SetPlayerLocation_ReceptionDay5
    call Receptionrecepcion_2 from _call_Receptionrecepcion_2
    # flowers
    call SetPlayerLocation("Mountains") from _call_SetPlayerLocation_MountainsDay5
    call MountainsYouWonANewObject_0 from _call_MountainsYouWonANewObject_0
    call MountainsYouWonANewObject_v2_0 from _call_MountainsYouWonANewObject_v2_0
    call MountainsYouWonANewObject_v3_0 from _call_MountainsYouWonANewObject_v3_0
    call MountainsYouWonANewObject_v4_0 from _call_MountainsYouWonANewObject_v4_0
    # come back to hot springs
    call SetPlayerLocation("Reception") from _call_SetPlayerLocation_ReceptionDay5_2
    call Receptionrecepcion_4 from _call_Receptionrecepcion_4
    call HotSpringsBathroomeventoenseatrabajo from _call_HotSpringsBathroomeventoenseatrabajo
    call ReceptionDamn_0 from _call_ReceptionDamn_0
    # ritual
    call SetPlayerLocation("Path") from _call_SetPlayerLocation_PathDay5
    call PathJohan_0 from _call_PathJohan_0
    call SetPlayerLocation("Festival") from _call_SetPlayerLocation_FestivalDay5
    call Festivaliniciacionadolescencia_0 from _call_Festivaliniciacionadolescencia_0
    call SetPlayerLocation("Town2") from _call_SetPlayerLocation_Town2Day5_2
    call Town2chicofestival_0 from _call_Town2chicofestival_0
    call Town2NPCAnotherFestivalBoy_0 from _call_Town2NPCAnotherFestivalBoy_0
    call Town2chicoencontrado_0 from _call_Town2chicoencontrado_0
    call Festivaliniciacionadolescencia_2 from _call_Festivaliniciacionadolescencia_2
    call SetPlayerLocation("Inn") from _call_SetPlayerLocation_InnDay5
    call Inninicionochefiesta_0 from _call_Inninicionochefiesta_0
    # town night
    if bottle_event >= 4:
        call TownFestivalNighteventoblackmail_2 from _call_TownFestivalNighteventoblackmail_2
    elif bottle_event >= 3:
        call TownFestivalNighteventoblackmail_1 from _call_TownFestivalNighteventoblackmail_1
    else:
        call TownFestivalNighteventoblackmail_0 from _call_TownFestivalNighteventoblackmail_0
    call TownFestivalNighteventoescondite_0 from _call_TownFestivalNighteventoescondite_0
    call GladeImSureHeWontFindMeHereThisAreaIsALittleScaryAtNightThough_0 from _call_GladeImSureHeWontFindMeHereThisAreaIsALittleScaryAtNightThough_0
    if hiding_place >= 4:
        call TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_1 from _call_TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_1
    elif hiding_place >= 3:
        call TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_0 from _call_TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_0
    return

label PlayDay6:
    # hot springs
    call SetPlayerLocation("Reception") from _call_SetPlayerLocation_ReceptionDay6
    call Receptionhotspringsjuntos_0 from _call_Receptionhotspringsjuntos_0
    call HotSpringsWithJohanhotspringjuntoscont from _call_HotSpringsWithJohanhotspringjuntoscont
    # photographer
    call SetPlayerLocation("Town2") from _call_SetPlayerLocation_Town2Day6
    call Town2fotografo_10 from _call_Town2fotografo_10
    call Town2LeynaJohanSex_0 from _call_Town2LeynaJohanSex_0
    # bar
    call SetPlayerLocation("Bar2") from _call_SetPlayerLocation_Bar2Day6
    call Bar2WowGuysWhatACoincidence_0  from _call_Bar2WowGuysWhatACoincidence_0
    # hot springs
    if bet_together >= 2:
        call PathLeynaWorkTrigger_1 from _call_PathLeynaWorkTrigger_1
    elif bet_together >= 1:
        call PathLeynaWorkTrigger_0 from _call_PathLeynaWorkTrigger_0
    # back to bar
    call SetPlayerLocation("Bar2") from _call_SetPlayerLocation_Bar2Day6_2
    call Bar2barman_3 from _call_Bar2barman_3
    # johan & alexa
    call SetPlayerLocation("Inn") from _call_SetPlayerLocation_InnDay6
    call InneventoJohanyalexa_0 from _call_InneventoJohanyalexa_0
    return

label PlayDay7:
    call SetPlayerLocation("Bar2") from _call_SetPlayerLocation_Bar2Day7
    call Bar2barman_5 from _call_Bar2barman_5
    call SetPlayerLocation("Bar2") from _call_SetPlayerLocation_Bar2Day7_2
    call Bar2Eventoanal1_0 from _call_Bar2Eventoanal1_0
    call SetPlayerLocation("InnRooms") from _call_SetPlayerLocation_InnRoomsDay7
    call InnRoomsescenadildo_0 from _call_InnRoomsescenadildo_0
    call SetPlayerLocation("Inn") from _call_SetPlayerLocation_InnDay7
    call Innposadero_3 from _call_Innposadero_3
    call SetPlayerLocation("Town2") from _call_SetPlayerLocation_Town2Day7
    call Town2JohanIWasLookingForYou_1 from _call_Town2JohanIWasLookingForYou_1
    call FestivalButtPlugEvent_1 from _call_FestivalButtPlugEvent_1
    call FestivalNightLeynaropa from _call_FestivalNightLeynaropa
    call SetPlayerLocation("Town2") from _call_SetPlayerLocation_Town2Day7_2
    call Town2finalfiestafestival_0 from _call_Town2finalfiestafestival_0
    label Day7River:
        call Town2ToRiverEvent_1 from _call_Town2ToRiverEvent_1
        if not switch("river_3"):
            jump Day7River
    call Town2fotografo_13 from _call_Town2fotografo_13
    if switch("hotsprings_photo_session"):
        call Town2Flashback_0 from _call_Town2Flashback_0
        call SetPlayerLocation("Bar2") from _call_SetPlayerLocation_Bar2Day7_3
        call Bar2LeynaWeWereLookingForYou_0 from _call_Bar2LeynaWeWereLookingForYou_0
    if switch("bet_2"):
        call InnRoomsMyHeadIsKillingMeSeemsLikeYesterdayWeHadTooMuchToDrinkAgainICanBarelyRememberWhatHappened_0 from _call_InnRoomsMyHeadIsKilling
        call SetPlayerLocation("Inn") from _call_SetPlayerLocation_InnDay7_2
        call InnToInn_0 from _call_InnToInn_0
    if switch("breakfast"):
        call SetPlayerLocation("Bar2") from _call_SetPlayerLocation_Bar2Day7_4
        call Bar2ToBar2_0 from _call_Bar2ToBar2_0
    call SetPlayerLocation("Path") from _call_SetPlayerLocation_PathDay7
    if switch("last_bar"):
        call PathWowItLooksLikeTheHotspringsHaveReopened_0 from _call_PathWowItLooksLikeTheHotspringsHaveReopened_0
    call Pathespacioentradafestival_12 from _call_Pathespacioentradafestival_12
    call FestivalFinaleDoYouWantSomeMasksForTheFinalEvent from _call_FestivalFinaleDoYouWantSomeMasksForTheFinalEvent
    call FestivalFinaleHeyLeynaGoodToSeeYouHere from _call_FestivalFinaleHeyLeynaGoodToSeeYouHere
    call FestivalFinaleHeyGoodToSeeYouLeynaEspeciallyInThisSituationHehehehehe from _call_FestivalFinaleHeyGoodToSeeYouLeynaEspeciallyInThisSituationHehehehehe
    call FestivalFinaleYoSlap from _call_FestivalFinaleYoSlap
    call FestivalFinaleOhLeynaIWasHopingToMeetYouIHaveSomethingToGiveYou from _call_FestivalFinaleOhLeynaIWasHopingToMeetYouIHaveSomethingToGiveYou
    call FestivalFinaleHeyWhatsGoingOnHere_0 from _call_FestivalFinaleHeyWhatsGoingOnHere_0
    call FestivalFinaleEvent15_0 from _call_FestivalFinaleEvent15_0
    call SetPlayerLocation("CasinoFinale") from _call_SetPlayerLocation_CasinoFinaleDay7
    call CasinoFinaleLooksLikeTheLastEventIsGoingToBeHere from _call_CasinoFinaleLooksLikeTheLastEventIsGoingToBeHere
    return

label PlayFinalDay:
    call SetPlayerLocation("InnRooms") from _call_SetPlayerLocation_InnRoomsFinalDay
    if switch("corruption_high"):
        call InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_0 from _call_InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_0
    if switch("corruption_average"):
        call InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_1 from _call_InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_1
    call SetPlayerLocation("Town2") from _call_SetPlayerLocation_Town2FinalDay
    if switch("corruption_high"):
        call Town2HeySweetieDoYouWantToHaveAGoodTime_0 from _call_Town2HeySweetieDoYouWantToHaveAGoodTime_0
        call SetPlayerLocation("Bar2") from _call_SetPlayerLocation_Bar2FinalDay
        call Bar2LeynawhatAreYouDoingHereIThoughtYouWereLeavingTownThisMorning_0 from _call_Bar2LeynawhatAreYouDoingHereIThoughtYouWereLeavingTownThisMorning_0
    call SetPlayerLocation("TownEntrance") from _call_SetPlayerLocation_TownEntranceFinalDay
    if switch("corruption_high"):
        call TownEntranceJohanAlta_1 from _call_TownEntranceJohanAlta_1
        call ApartmentEndingCbajaending2 from _call_ApartmentEndingCbajaending2
    if switch("corruption_average"):
        call TownEntranceJohanmedia_1 from _call_TownEntranceJohanmedia_1
        call ApartmentEndingCbajaending2_v2 from _call_ApartmentEndingCbajaending2_v2
    if switch("corruption_low"):
        call TownEntranceCbajaending from _call_TownEntranceCbajaending
        call ApartmentGroundFloorCbajaending2 from _call_ApartmentGroundFloorCbajaending2
    return
