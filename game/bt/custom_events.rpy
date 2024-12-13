init python:
    def get_new_quests_or_objectives():
        return False

label LogicCallback(called_from, script):
    return

label MovementHacks(called_from, character, moves):
    return

label ShowAnimation(id, character, called_from):
    $ x = map_click_xy[0]
    $ y = map_click_xy[1]
    if called_from.startswith("BarWetTShirt"):    
        $ x = 540
        $ y = 480
    if called_from.startswith("PoliceStation"):    
        $ x = 303
        $ y = 380
    $ frame_time = 0.05
    $ end_pause = 0.24
    $ show_animation(id, x, y, frame_time, end_pause)
    return

label InnRoomBG:
    if suitcases >= 1:
        $ bg = "map_inn_room_suitcase"
    else:
        $ bg = "map_inn_room"
    $ set_transparency_backgrounds([bg])
    $ set_map_backgrounds([bg])
    $ resolve_scene("dirty")
    return

label InnRoomsDEJANDOlasmaletas_0Custom:
    call InnRoomBG from _call_InnRoomBG_InnRoomsDEJANDOlasmaletas
    call InnRoomsDEJANDOlasmaletas_0 from _call_InnRoomsDEJANDOlasmaletas_0
    return _return

label InnRoomssueojohan_0Custom:
    call InnRoomBG from _call_InnRoomBG_InnRoomssueojohan_0
    call InnRoomssueojohan_0 from _call_InnRoomssueojohan_0
    return _return

label InnRoomsescenadildo_0Custom:
    call InnRoomBG from _call_InnRoomBG_InnRoomsescenadildo_0
    call InnRoomsescenadildo_0 from _call_InnRoomsescenadildo_0
    return _return

label InnRoomsMyHeadIsKillingMeSeemsLikeYesterdayWeHadTooMuchToDrinkAgainICanBarelyRememberWhatHappened_0Custom:
    call InnRoomBG from _call_InnRoomBG_InnRoomsMyHeadIsKillingMeSeemsLikeYesterdayWeHadTooMuchToDrinkAgainICanBarelyRememberWhatHappened_0
    call InnRoomsMyHeadIsKillingMeSeemsLikeYesterdayWeHadTooMuchToDrinkAgainICanBarelyRememberWhatHappened_0 from _call_InnRoomsMyHeadIsKillingMeSeemsLikeYesterdayWeHadTooMuchToDrinkAgainICanBarelyRememberWhatHappened_0
    return _return

label InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_0Custom:
    call InnRoomBG from _call_InnRoomBG_InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_0
    call InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_0 from _call_InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_0
    return _return

label InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_1Custom:
    call InnRoomBG from _call_InnRoomBG_InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_1
    call InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_1 from _call_InnRoomsJohanHasntSleptHereTonightWhereIsHeIShouldLookForHimOrNotMaybeHesAtTheBusStop_1
    return _return

label InnRoomsRoomToHallwayBase:
    call InnRoomsBG from _call_InnRoomBG_InnRoomsRoomToHallwayBase
    $ resolve_scene()
    return False

label InnRoomsRoomToHallway(play_event = True, trigger = None): # event
    if trigger == "event":
        call PlayEvent(play_event, "InnRoomsRoomToHallwayBase", "InnRoomsRoomToHallway") from _call_InnRoomsRoomToHallway_PlayEvent
        return (0, "", "InnRoomsRoomToHallway")
    return None

label InnRoomsToInnRoomBase:
    call InnRoomBG from _call_InnRoomBG_InnRoomsToInnRoomBase
    return False

label InnRoomsToInnRoom(play_event = True, trigger = None): # event
    if is_erased("InnRoomsToInnRoom"):
        return None
    elif switch("leyna_dream_end"):
        return None
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "InnRoomsToInnRoomBase", "InnRoomsToInnRoom") from _call_InnRoomsToInnRoomBase_PlayEvent
        return (1, "", "InnRoomsToInnRoomBase")
    return None

label PathJohanDreamBase:
    call PathEV014Base from _call_PathEV014_PathJohanDreamBase
    $ erase_event_from_map("PathEV014")
    return True

label PathJohanDream(play_event = True, trigger = None): # autorun
    if trigger == "autorun" and johan_dream == 2:
        call PlayEvent(play_event, "PathJohanDreamBase", "PathJohanDream") from _call_PathJohanDreamBase_PlayEvent
        return (1, "", "PathJohanDreamBase")
    return None

label Town2LeynaJohanSexAutorun(play_event = True, trigger = None): # turned from event into autorun
    if is_erased("Town2LeynaJohanSex"):
        return None
    elif switch("johan_and_leyna_sex"):
        return None
    elif trigger == "autorun" and switch("erotic_photos_together"):
        call PlayEvent(play_event, "Town2LeynaJohanSex_0", "Town2LeynaJohanSex") from _call_Town2LeynaJohanSex_0_PlayEventAutorun
        return (0, "", "Town2LeynaJohanSex_0")
    return None

label MountainsYouWonANewObject_0Custom:
    $ use_baked_images = False
    $ set_transparency_backgrounds(["map_mountain3"])
    $ set_map_backgrounds(["map_mountain3"])
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    $ use_baked_images = True
    call MountainsYouWonANewObject_0 from _call_MountainsYouWonANewObject_0
    $ set_transparency_backgrounds(["map_mountain2"])
    $ set_map_backgrounds(["map_mountain2"])
    $ switch_to_next_backgrounds(no_fades=True)
    return _return

label MountainsYouWonANewObject_v2_0Custom:
    $ use_baked_images = False
    $ set_transparency_backgrounds(["map_mountain2"])
    $ set_map_backgrounds(["map_mountain2"])
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    $ use_baked_images = True
    call MountainsYouWonANewObject_v2_0 from _call_MountainsYouWonANewObject_v2_0
    $ set_transparency_backgrounds(["map_mountain1"])
    $ set_map_backgrounds(["map_mountain1"])
    $ switch_to_next_backgrounds(no_fades=True)
    return _return

label MountainsYouWonANewObject_v3_0Custom:
    $ use_baked_images = False
    $ set_transparency_backgrounds(["map_mountain1"])
    $ set_map_backgrounds(["map_mountain1"])
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    $ use_baked_images = True
    call MountainsYouWonANewObject_v3_0 from _call_MountainsYouWonANewObject_v3_0
    $ set_transparency_backgrounds(["map_mountain"])
    $ set_map_backgrounds(["map_mountain"])
    $ switch_to_next_backgrounds(no_fades=True)
    return _return

label MountainsYouWonANewObject_v4_0Custom:
    $ use_baked_images = False
    $ set_transparency_backgrounds(["map_mountain"])
    $ set_map_backgrounds(["map_mountain"])
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    $ use_baked_images = True
    call MountainsYouWonANewObject_v4_0 from _call_MountainsYouWonANewObject_v4_0
    return _return

label Townfinaldelprimerdia_0Custom:
    call Townfinaldelprimerdia_0 from _call_Townfinaldelprimerdia_0
    # $ fade_out()
    # "End of Ren'Py version 0.1"
    # $ game_over = True
    return _return

label InnNightentradaalaposadanoche_0Custom:
    call InnNightentradaalaposadanoche_0 from _call_InnNightentradaalaposadanoche_0
    # $ fade_out()
    # "End of Ren'Py version 0.2"
    # $ game_over = True
    return _return

label FestivalButtPlugEvent_1Custom:
    call FestivalButtPlugEvent_1 from _call_FestivalButtPlugEvent_1
    # $ fade_out()
    # "End of Ren'Py version 0.3"
    # $ game_over = True
    return _return

label InnJohanEndOfDay2Base:
    return False

label InnJohanEndOfDay2(play_event = True, trigger = None): # event
    if trigger == "event" and switch("second_river") and not switch("third_day"):
        call PlayEvent(play_event, "InnJohanEndOfDay2Base", "InnJohanEndOfDay2") from _call_InnJohanEndOfDay2Base_PlayEvent
        return (1, "", "InnJohanEndOfDay2Base")
    return None

label PathNPCFestivalWorker2Base:
    return False

label PathNPCFestivalWorker2(play_event = True, trigger = None): # event
    if is_erased("Pathespacioentradafestival"):
        return None
    elif switch("festival_final"):
        return None
    elif trigger == "event" and switch("last_hotsprings"):
        return None
    elif trigger == "event" and switch("party_at_festival"):
        return None
    elif trigger == "event" and leyna_work >= 4:
        return None
    elif trigger == "event" and switch("leyna_dream_end"):
        return None
    elif trigger == "event" and switch("festival"):
        return None
    elif trigger == "event" and johan_dream >= 3:
        return None
    elif trigger == "event" and event_clothing >= 2:
        return None
    elif trigger == "event" and elder_festival >= 6:
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "PathNPCFestivalWorker2Base", "PathNPCFestivalWorker") from _call_PathNPCFestivalWorker2Base_PlayEvent
        return (0, "", "PathNPCFestivalWorker2Base")
    return None

label FoodStoreToolbag_0:
    return False

label FoodStoreToolbag(play_event = True, trigger = None): # event
    if is_erased("FoodStoreToolbag"):
        return None
    elif elder_festival >= 4:
        return None
    elif trigger == "event" and elder_festival >= 1:
        call PlayEvent(play_event, "FoodStoreToolbag_0", "FoodStoreToolbag") from _call_FoodStoreToolbag_0_PlayEvent
        return (1, "", "FoodStoreToolbag_0")
    return None

label FestivalFinaleChef_0:
    return False

label FestivalFinaleChef(play_event = True, trigger = None): # event
    if is_erased("FestivalFinaleChef"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "FestivalFinaleChef_0", "FestivalFinaleChef") from _call_FestivalFinaleChef_0_PlayEvent
        return (1, "", "FestivalFinaleChef_0")
    return None

label TownNightBottleBoys_0:
    "have you bought the alocohol?"
    return False

label TownNightBottleBoys_1:
    "if you want a good time, you know where we are"
    return False

label TownNightBottleBoys(play_event = True, trigger = None): # event
    if is_erased("TownNightBottleBoys"):
        return None
    elif trigger == "event" and bottle_event >= 3:
        call PlayEvent(play_event, "TownNightBottleBoys_1", "TownNightBottleBoys") from _call_TownNightBottleBoys_1_PlayEvent
        return (1, "", "TownNightBottleBoys_1")
    elif bottle_event >= 2:
        return None
    elif trigger == "event" and bottle_event >= 1:
        call PlayEvent(play_event, "TownNightBottleBoys_0", "TownNightBottleBoys") from _call_TownNightBottleBoys_0_PlayEvent
        return (1, "", "TownNightBottleBoys_0")
    return None

label PoliceStationPrisoner_0:
    return False

label PoliceStationPrisoner(play_event = True, trigger = None): # event
    if is_erased("PoliceStationPrisoner"):
        return None
    elif switch("leyna_dream_end"):
        return None
    elif trigger == "event" and (switch("third_day") or jail >= 1):
        call PlayEvent(play_event, "PoliceStationPrisoner_1", "PoliceStationPrisoner") from _call_PoliceStationPrisoner_1_PlayEvent
        return (0, "", "PoliceStationPrisoner_1")
    return None

label BarAlexa_0:
    return False

label BarAlexa(play_event = True, trigger = None): # event
    if is_erased("BarAlexa"):
        return None
    elif self_switch("Bar2","Bar2LeynaWeWereLookingForYou","A"):
        return None
    elif trigger == "event" and switch("hotsprings_photo_session"):
        call PlayEvent(play_event, "BarAlexa_0", "BarAlexa") from _call_BarAlexa_0_PlayEvent
        return (0, "", "BarAlexa_0")
    elif self_switch("Bar2","Bar2WowGuysWhatACoincidence","A"):
        return None
    elif trigger == "event" and switch("erotic_photos_together"):
        call PlayEvent(play_event, "BarAlexa_0", "BarAlexa") from _call_BarAlexa_0_PlayEvent2
        return (0, "", "BarAlexa_0")
    return None

label PoliceStationBars_0:
    return False

label PoliceStationBars(play_event = True, trigger = None): # event
    if is_erased("PoliceStationBars"):
        return None
    elif switch("leyna_dream_end"):
        return None
    elif trigger == "event" and (switch("third_day") or jail >= 1):
        call PlayEvent(play_event, "PoliceStationBars_0", "PoliceStationBars") from _call_PoliceStationBars_0_PlayEvent
        return (0, "", "PoliceStationBars_0")
    return None

label TownTABLON_0Custom:
    call TownTABLON_0 from _call_TownTABLON_0Custom
    $ set_switch("seen_tablon", True)
    $ no_advancement_events = 0
    return _return

label TownNightTABLON_0Custom:
    call TownNightTABLON_0 from _call_TownNightTABLON_0Custom
    $ set_switch("seen_tablon", True)
    $ no_advancement_events = 0
    return _return

label Town2TABLON_0Custom:
    call Town2TABLON_0 from _call_Town2TABLON_0Custom
    $ set_switch("seen_tablon", True)
    $ no_advancement_events = 0
    return _return

label ClothingStoreIShouldComeBackLaterToTryTheFestivalClothes_0Custom:
    if elder_festival == 6 and event_clothing == 0:
        "I should talk to the merchant"
    else:
        call ClothingStoreIShouldComeBackLaterToTryTheFestivalClothes_0 from _call_ClothingStoreIShouldComeBackLaterToTryTheFestivalClothes_0
    return

label Town2fotografo_1Custom(menu_choice = None):
    call Town2fotografo_1(menu_choice) from _call_Town2fotografo_1Custom
    call SetEventLocation("Town2fotografo_1Custom", "Town2fotografo", 18, 5) from _call_Town2fotografo_1Custom_setloc
    return

label Town2finalfiestafestivalAsAutorun(play_event = True, trigger = None): # event
    if is_erased("Town2finalfiestafestival"):
        return None
    elif self_switch("Town2","Town2finalfiestafestival","A"):
        return None
    elif switch("river_3"):
        return None
    elif trigger == "autorun" and switch("party_at_festival"):
        call PlayEvent(play_event, "Town2finalfiestafestival_0", "Town2finalfiestafestivalAsAutorun") from _call_Town2finalfiestafestivalAsAutorun_0_PlayEvent
        return (0, "", "Town2finalfiestafestival_0")
    return None

label FestivalFinaleToCasinoFinale_1Custom:
    "have you finished exploring the festival?"
    menu:
        "yes":
            call FestivalFinaleToCasinoFinale_1 from _call_FestivalFinaleToCasinoFinale_1Custom
        "no":
            pass
    return False

label Town2ToTownEntranceBaseCustom:
    "are you ready to leave town?"
    menu:
        "yes":
            call Town2ToTownEntranceBase from _call_Town2ToTownEntranceBaseCustom
        "no":
            pass
    return False

label FestivalFinaleHeyWhatsGoingOnHereDone_0:
    return False

label FestivalFinaleHeyWhatsGoingOnHereDone(play_event = True, trigger = None): # event
    if is_erased("FestivalFinaleHeyWhatsGoingOnHereDone"):
        return None
    elif self_switch("FestivalFinale","FestivalFinaleHeyWhatsGoingOnHere","A"):
        call PlayEvent(play_event, "FestivalFinaleHeyWhatsGoingOnHereDone_0", "FestivalFinaleHeyWhatsGoingOnHereDone") from _call_FestivalFinaleHeyWhatsGoingOnHereDone_0_PlayEvent
        return (1, "", "FestivalFinaleHeyWhatsGoingOnHereDone_0")
    elif trigger == "event":
        return None
    return None

label TownEntranceStartCustom:
    call TownEntranceStart from _call_TownEntranceStartCustom
    if switch("festival_final"):
        $ set_transparency_backgrounds(["bg_townentrance_johan","darkbg"])
        $ set_map_backgrounds(["bg_townentrance_johan","darkbg"])
    return

label Town2TABLON_6Custom:
    "explore the town before leaving"
    return