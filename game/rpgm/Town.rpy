label TownBG:
    $ set_transparency_backgrounds(["bg_town_south"])
    $ set_map_backgrounds(["map_town_south"])
    return

label TownStart:
    call TownBG from _call_TownBG
    stop music
    stop bgs
    return

label TownEnd:
    return

label TownBoarInnBase:
    "Boar Inn"
    return False

label TownBoarInn(play_event = True, trigger = None): # event
    if is_erased("TownBoarInn"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownBoarInnBase", "TownBoarInn") from _call_TownBoarInn_PlayEvent
        return (1, "", "TownBoarInn")
    return None

label TownToInn_0:
    call PlaySound("sound", "audio/Open1.ogg", volume=0.9, no_loop=True) from _call_TownEV003_0_PlaySound
    call Movement("TownEV003_0", "TownEV003", ["TURN_L",["WAIT",3],"TURN_R",["WAIT",3],"TURN_U","THROUGH_ON"]) from _call_TownEV003_0_Movement
    call Movement("TownEV003_0", "player", ["FORWARD"]) from _call_TownEV003_0_Movement_1
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_TownEV003_0_PlaySound_1
    call TransferPlayer("Inn", "TownEV003_0", 8, 12, direction=0) from _call_TownEV003_0_TransferPlayer
    $ resolve_scene()
    return False

label TownToInn_1:
    call PlaySound("sound", "audio/Open1.ogg", volume=0.9, no_loop=True) from _call_TownEV003_1_PlaySound
    call Movement("TownEV003_1", "TownEV003", ["TURN_L",["WAIT",3],"TURN_R",["WAIT",3],"TURN_U","THROUGH_ON"]) from _call_TownEV003_1_Movement
    call Movement("TownEV003_1", "player", ["FORWARD"]) from _call_TownEV003_1_Movement_1
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_TownEV003_1_PlaySound_1
    call TransferPlayer("InnNight", "TownEV003_1", 8, 12, direction=8) from _call_TownEV003_1_TransferPlayer
    $ resolve_scene()
    return False

label TownToInn(play_event = True, trigger = None): # event
    if is_erased("TownToInn"):
        return None
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "TownToInn_1", "TownToInn") from _call_TownToInn_1_PlayEvent
        return (1, "", "TownToInn_1")
    elif trigger == "event":
        call PlayEvent(play_event, "TownToInn_0", "TownToInn") from _call_TownToInn_0_PlayEvent
        return (1, "", "TownToInn_0")
    return None

label TownToRiverBase:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_TownEV004_PlaySound
    call TransferPlayer("River", "TownEV004", 0, 8, direction=6) from _call_TownEV004_TransferPlayer
    $ resolve_scene()
    return False

label TownToRiver(play_event = True, trigger = None): # event
    if is_erased("TownToRiver"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownToRiverBase", "TownToRiver") from _call_TownToRiver_PlayEvent
        return (0, "", "TownToRiver")
    return None

label TownToRiver_v2Base:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_TownEV005_PlaySound
    call TransferPlayer("River", "TownEV005", 0, 9, direction=6) from _call_TownEV005_TransferPlayer
    $ resolve_scene()
    return False

label TownToRiver_v2(play_event = True, trigger = None): # event
    if is_erased("TownToRiver_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownToRiver_v2Base", "TownToRiver_v2") from _call_TownToRiver_v2_PlayEvent
        return (0, "", "TownToRiver_v2")
    return None

label TownMapBase:
    "River -> Festival <- Hot springs <- Coal mine <-"
    return False

label TownMap(play_event = True, trigger = None): # event
    if is_erased("TownMap"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownMapBase", "TownMap") from _call_TownMap_PlayEvent
        return (1, "", "TownMap")
    return None

label TownToBarBase:
    call PlaySound("sound", "audio/Open1.ogg", volume=0.9, no_loop=True) from _call_TownEV008_PlaySound
    call Movement("TownEV008", "TownEV008", ["TURN_L",["WAIT",3],"TURN_R",["WAIT",3],"TURN_U","THROUGH_ON"]) from _call_TownEV008_Movement
    call Movement("TownEV008", "player", ["FORWARD"]) from _call_TownEV008_Movement_1
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_TownEV008_PlaySound_1
    call TransferPlayer("Bar", "TownEV008", 8, 12, direction=0) from _call_TownEV008_TransferPlayer
    $ resolve_scene()
    return False

label TownToBar(play_event = True, trigger = None): # event
    if is_erased("TownToBar"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownToBarBase", "TownToBar") from _call_TownToBar_PlayEvent
        return (1, "", "TownToBar")
    return None

label TownToFoodStoreBase:
    call PlaySound("sound", "audio/Open1.ogg", volume=0.9, no_loop=True) from _call_TownEV009_PlaySound
    call Movement("TownEV009", "TownEV009", ["TURN_L",["WAIT",3],"TURN_R",["WAIT",3],"TURN_U","THROUGH_ON"]) from _call_TownEV009_Movement
    call Movement("TownEV009", "player", ["FORWARD"]) from _call_TownEV009_Movement_1
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_TownEV009_PlaySound_1
    call TransferPlayer("FoodStore", "TownEV009", 10, 8, direction=4) from _call_TownEV009_TransferPlayer
    $ resolve_scene()
    return False

label TownToFoodStore(play_event = True, trigger = None): # event
    if is_erased("TownToFoodStore"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownToFoodStoreBase", "TownToFoodStore") from _call_TownToFoodStore_PlayEvent
        return (1, "", "TownToFoodStore")
    return None

label TownToFoodStore_v2Base:
    call PlaySound("sound", "audio/Open1.ogg", volume=0.9, no_loop=True) from _call_TownEV010_PlaySound
    call Movement("TownEV010", "TownEV010", ["TURN_L",["WAIT",3],"TURN_R",["WAIT",3],"TURN_U","THROUGH_ON"]) from _call_TownEV010_Movement
    call Movement("TownEV010", "player", ["FORWARD"]) from _call_TownEV010_Movement_1
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_TownEV010_PlaySound_1
    call TransferPlayer("FoodStore", "TownEV010", 10, 7, direction=4) from _call_TownEV010_TransferPlayer
    $ resolve_scene()
    return False

label TownToFoodStore_v2(play_event = True, trigger = None): # event
    if is_erased("TownToFoodStore_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownToFoodStore_v2Base", "TownToFoodStore_v2") from _call_TownToFoodStore_v2_PlayEvent
        return (1, "", "TownToFoodStore_v2")
    return None

label TownToClothingStoreBase:
    call PlaySound("sound", "audio/Open1.ogg", volume=0.9, no_loop=True) from _call_TownEV011_PlaySound
    call Movement("TownEV011", "TownEV011", ["TURN_L",["WAIT",3],"TURN_R",["WAIT",3],"TURN_U","THROUGH_ON"]) from _call_TownEV011_Movement
    call Movement("TownEV011", "player", ["FORWARD"]) from _call_TownEV011_Movement_1
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_TownEV011_PlaySound_1
    call TransferPlayer("ClothingStore", "TownEV011", 9, 7, direction=4) from _call_TownEV011_TransferPlayer
    $ resolve_scene()
    return False

label TownToClothingStore(play_event = True, trigger = None): # event
    if is_erased("TownToClothingStore"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownToClothingStoreBase", "TownToClothingStore") from _call_TownToClothingStore_PlayEvent
        return (1, "", "TownToClothingStore")
    return None

label TownToHouseInteriorBase:
    call PlaySound("sound", "audio/Open1.ogg", volume=0.9, no_loop=True) from _call_TownEV012_PlaySound
    call Movement("TownEV012", "TownEV012", ["TURN_L",["WAIT",3],"TURN_R",["WAIT",3],"TURN_U","THROUGH_ON"]) from _call_TownEV012_Movement
    call Movement("TownEV012", "player", ["FORWARD"]) from _call_TownEV012_Movement_1
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_TownEV012_PlaySound_1
    call TransferPlayer("HouseInterior", "TownEV012", 4, 12, direction=0) from _call_TownEV012_TransferPlayer
    $ resolve_scene()
    return False

label TownToHouseInterior(play_event = True, trigger = None): # event
    if is_erased("TownToHouseInterior"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownToHouseInteriorBase", "TownToHouseInterior") from _call_TownToHouseInterior_PlayEvent
        return (1, "", "TownToHouseInterior")
    return None

label TownSeemsItsClosedBase:
    "Seems it's closed"
    return False

label TownSeemsItsClosed(play_event = True, trigger = None): # event
    if is_erased("TownSeemsItsClosed"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownSeemsItsClosedBase", "TownSeemsItsClosed") from _call_TownSeemsItsClosed_PlayEvent
        return (1, "", "TownSeemsItsClosed")
    return None

label TownNPCOldManBase:
    OldMan "I hope you enjoy the festivities"
    $ show_transparent(1, "plano_de_frente", width=1600, height=900)
    $ resolve_scene()
    "(damn, those tits are something ..)"
    pause
    $ erase_picture(1)
    $ resolve_scene()
    return False

label TownNPCOldMan(play_event = True, trigger = None): # event
    if is_erased("TownNPCOldMan"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNPCOldManBase", "TownNPCOldMan") from _call_TownNPCOldMan_PlayEvent
        return (1, "", "TownNPCOldMan")
    return None

label TownCastlePosterBase:
    "Closed for restoration."
    return False

label TownCastlePoster(play_event = True, trigger = None): # event
    if is_erased("TownCastlePoster"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownCastlePosterBase", "TownCastlePoster") from _call_TownCastlePoster_PlayEvent
        return (1, "", "TownCastlePoster")
    return None

label TownCastlePoster_v2Base:
    "Closed for restoration."
    return False

label TownCastlePoster_v2(play_event = True, trigger = None): # event
    if is_erased("TownCastlePoster_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownCastlePoster_v2Base", "TownCastlePoster_v2") from _call_TownCastlePoster_v2_PlayEvent
        return (1, "", "TownCastlePoster_v2")
    return None

label TownNPCEntryFestival_0:
    Villager "You can't pass yet, we are building the tents"
    return False

label TownNPCEntryFestival(play_event = True, trigger = None): # event
    if is_erased("TownNPCEntryFestival"):
        return None
    elif switch("leyna_alone"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNPCEntryFestival_0", "TownNPCEntryFestival") from _call_TownNPCEntryFestival_0_PlayEvent
        return (1, "", "TownNPCEntryFestival_0")
    return None

label Townespacioentradafestival_0:
    call Movement("Townespacioentradafestival_0", "TownNPCEntryFestival", ["TURN_D"]) from _call_Townespacioentradafestival_0_Movement
    $ resolve_scene()
    Villager "Hey! you can't pass yet, we are building the tents"
    Johan "Oh, sorry"
    call Movement("Townespacioentradafestival_0", "TownNPCEntryFestival", ["TURN_R"]) from _call_Townespacioentradafestival_0_Movement_1
    call Movement("Townespacioentradafestival_0", "player", ["TURN_R","R"]) from _call_Townespacioentradafestival_0_Movement_2
    $ resolve_scene()
    return False

label Townespacioentradafestival(play_event = True, trigger = None): # event
    if is_erased("Townespacioentradafestival"):
        return None
    elif switch("leyna_alone"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Townespacioentradafestival_0", "Townespacioentradafestival") from _call_Townespacioentradafestival_0_PlayEvent
        return (0, "", "Townespacioentradafestival_0")
    return None

label TownToRiverEvent_0:
    if corruption == 3:
        pass
    if corruption < 3:
        $ resolve_scene()
        Leyna "I don't want to go to the river yet.."
        ".. we can continue interviewing people in the town"
        call Movement("TownToRiverEvent_0", "player", ["TURN_L","L"]) from _call_TownToRiverEvent_0_Movement
        $ resolve_scene()
        "YOU NEED 3 POINTS OF CORRUPTION TO ENTER THE RIVER"
    $ resolve_scene()
    return False

label TownToRiverEvent_1:
    Johan "We don't need to go back there for now."
    call Movement("TownToRiverEvent_1", "player", ["TURN_L","L"]) from _call_TownToRiverEvent_1_Movement
    $ resolve_scene()
    return False

label TownToRiverEvent_2:
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "I don't want to go to the river without Johan..."
    $ erase_picture(1)
    call Movement("TownToRiverEvent_2", "player", ["TURN_L","L"]) from _call_TownToRiverEvent_2_Movement
    $ resolve_scene()
    return False

label TownToRiverEvent(play_event = True, trigger = None): # event
    if is_erased("TownToRiverEvent"):
        return None
    elif trigger == "event" and switch("leyna_alone"):
        call PlayEvent(play_event, "TownToRiverEvent_2", "TownToRiverEvent") from _call_TownToRiverEvent_2_PlayEvent
        return (0, "", "TownToRiverEvent_2")
    elif trigger == "event" and switch("finished_river_scene"):
        call PlayEvent(play_event, "TownToRiverEvent_1", "TownToRiverEvent") from _call_TownToRiverEvent_1_PlayEvent
        return (0, "", "TownToRiverEvent_1")
    elif trigger == "event":
        call PlayEvent(play_event, "TownToRiverEvent_0", "TownToRiverEvent") from _call_TownToRiverEvent_0_PlayEvent
        return (0, "", "TownToRiverEvent_0")
    return None

label TownToRiverEvent_v2_0:
    if corruption == 3:
        pass
    if corruption < 3:
        $ resolve_scene()
        Leyna "I don't want to go to the river yet.."
        ".. we can continue interviewing people in the town"
        call Movement("TownToRiverEvent_v2_0", "player", ["TURN_L","L"]) from _call_TownToRiverEvent_v2_0_Movement
        $ resolve_scene()
        "YOU NEED 3 POINTS OF CORRUPTION TO ENTER THE RIVER"
    $ resolve_scene()
    return False

label TownToRiverEvent_v2_1:
    Johan "We don't need to go back there for now."
    call Movement("TownToRiverEvent_v2_1", "player", ["TURN_L","L"]) from _call_TownToRiverEvent_v2_1_Movement
    $ resolve_scene()
    return False

label TownToRiverEvent_v2_2:
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "I don't want to go to the river without Johan..."
    $ erase_picture(1)
    call Movement("TownToRiverEvent_v2_2", "player", ["TURN_L","L"]) from _call_TownToRiverEvent_v2_2_Movement
    $ resolve_scene()
    return False

label TownToRiverEvent_v2(play_event = True, trigger = None): # event
    if is_erased("TownToRiverEvent_v2"):
        return None
    elif trigger == "event" and switch("leyna_alone"):
        call PlayEvent(play_event, "TownToRiverEvent_v2_2", "TownToRiverEvent_v2") from _call_TownToRiverEvent_v2_2_PlayEvent
        return (0, "", "TownToRiverEvent_v2_2")
    elif trigger == "event" and switch("finished_river_scene"):
        call PlayEvent(play_event, "TownToRiverEvent_v2_1", "TownToRiverEvent_v2") from _call_TownToRiverEvent_v2_1_PlayEvent
        return (0, "", "TownToRiverEvent_v2_1")
    elif trigger == "event":
        call PlayEvent(play_event, "TownToRiverEvent_v2_0", "TownToRiverEvent_v2") from _call_TownToRiverEvent_v2_0_PlayEvent
        return (0, "", "TownToRiverEvent_v2_0")
    return None

label TownNPCCop_0:
    call Movement("TownNPCCop_0", "player", ["U","R","TURN_U"]) from _call_TownNPCCop_0_Movement
    $ resolve_scene()
    $ show_transparent(1, "expresion_ilusion_mujer", width=1600, height=900)
    $ resolve_scene()
    "OHHH!!"
    Leyna "How beautiful, it looks so medieval"
    $ erase_picture(1)
    $ resolve_scene()
    Johan "We should look for the inn and leave the luggage"
    call Movement("TownNPCCop_0", "player", ["U","U","U","L","L","L","L"]) from _call_TownNPCCop_0_Movement_1
    $ resolve_scene()
    Policeman "Good morning couple. I see that you are new in town"
    Johan "Yes, we came to the festival"
    Policeman "On these dates, we receive many tourists, although it's worth visiting the town at any time of the year"
    "Anyway, if you need anything, you can find me here"
    Johan "Since you mention it, can you tell us how to get to the inn?"
    Policeman "Sure, you have to go straight to the end of the town and turn right, there it is!"
    Johan "Okey, thanks"
    call TransferPlayer("Town", "TownNPCCop_0", 26, 23, direction=6) from _call_TownNPCCop_0_TransferPlayer
    call Movement("TownNPCCop_0", "player", ["R","R","U","U"]) from _call_TownNPCCop_0_Movement_2
    call TransferPlayer("Inn", "TownNPCCop_0", 8, 11, direction=0) from _call_TownNPCCop_0_TransferPlayer_1
    $ resolve_scene()
    return False

label TownNPCCop_1:
    if not switch("leyna_alone"):
        $ resolve_scene()
        Policeman "Everything alright?"
    if switch("leyna_alone"):
        Policeman "This is a safe town. But just in case, the police station is on the top of this path"
    $ resolve_scene()
    return False

label TownNPCCop(play_event = True, trigger = None): # event, autorun
    if is_erased("TownNPCCop"):
        return None
    elif (trigger == "any" or trigger == "event") and switch("inn_departure"):
        call PlayEvent(play_event, "TownNPCCop_1", "TownNPCCop") from _call_TownNPCCop_1_PlayEvent
        return (1, "", "TownNPCCop_1")
    elif (trigger == "any" or trigger == "autorun") and switch("introduction"):
        call PlayEvent(play_event, "TownNPCCop_0", "TownNPCCop") from _call_TownNPCCop_0_PlayEvent
        return (1, "", "TownNPCCop_0")
    return None

label Townturista1Base:
    if not switch("leyna_alone"):
        $ resolve_scene()
        Tourist "This town is great. although there are very few women ..."
    if switch("leyna_alone"):
        Tourist "Can't wait to see you on the fest.. Maybe we can take some beers"
    $ resolve_scene()
    return False

label Townturista1(play_event = True, trigger = None): # event
    if is_erased("Townturista1"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Townturista1Base", "Townturista1") from _call_Townturista1_PlayEvent
        return (1, "", "Townturista1")
    return None

label TownborrachoinconscienteBase:
    DrunkVillager "Uhhg... tits... come closer... (pass out)"
    return False

label Townborrachoinconsciente(play_event = True, trigger = None): # event
    if is_erased("Townborrachoinconsciente"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownborrachoinconscienteBase", "Townborrachoinconsciente") from _call_Townborrachoinconsciente_PlayEvent
        return (1, "", "Townborrachoinconsciente")
    return None

label TownStallBase:
    VillagerWoman "PANTIES!. UNDERPANTS!. LOW PRICES, WE PRACTICALLY GIVE IT AWAY. LADIES AND GENTLEMEN BUY NOW"
    return False

label TownStall(play_event = True, trigger = None): # event
    if is_erased("TownStall"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownStallBase", "TownStall") from _call_TownStall_PlayEvent
        return (1, "", "TownStall")
    return None

label TownMerchant_0:
    VillagerMan "COATS! PANTS!. VERY LOW PRICES! WE ARE ALMOST GIVING IT AWAY. SIR, BUY NOW OR REGRET IT LATER"
    VillagerWoman "You wish ... that clothing is rubbish and very expensive..."
    VillagerMan "shut up old witch..."
    VillagerWoman "you shut up, helpless old man"
    $ set_self_switch("Town","TownMerchant","A",True)
    return False

label TownMerchant_1:
    VillagerMan "COATS! PANTS!. VERY LOW PRICES! WE ARE ALMOST GIVING IT AWAY. SIR, BUY NOW OR REGRET IT LATER"
    return False

label TownMerchant(play_event = True, trigger = None): # event
    if is_erased("TownMerchant"):
        return None
    elif trigger == "event" and self_switch("Town","TownMerchant","A"):
        call PlayEvent(play_event, "TownMerchant_1", "TownMerchant") from _call_TownMerchant_1_PlayEvent
        return (1, "", "TownMerchant_1")
    elif trigger == "event":
        call PlayEvent(play_event, "TownMerchant_0", "TownMerchant") from _call_TownMerchant_0_PlayEvent
        return (1, "", "TownMerchant_0")
    return None

label TownFleaMarketBase:
    VillagerGirl "FRUITS! VEGETABLES! ALL FRESH! RECENTLY BROUGHT FROM THE GARDEN!"
    return False

label TownFleaMarket(play_event = True, trigger = None): # event
    if is_erased("TownFleaMarket"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownFleaMarketBase", "TownFleaMarket") from _call_TownFleaMarket_PlayEvent
        return (1, "", "TownFleaMarket")
    return None

label TownNPCVillageWomanBase:
    if not switch("leyna_alone"):
        $ resolve_scene()
        VillagerWoman "Men in this village are wild. I should have moved to the city, like my sister..."
    if switch("leyna_alone"):
        VillagerWoman "Between you and me.. men are rough here but, hehehe.. they know how to provoke a woman to do bad things..."
    $ resolve_scene()
    return False

label TownNPCVillageWoman(play_event = True, trigger = None): # event
    if is_erased("TownNPCVillageWoman"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNPCVillageWomanBase", "TownNPCVillageWoman") from _call_TownNPCVillageWoman_PlayEvent
        return (1, "", "TownNPCVillageWoman")
    return None

label TownToRiverEvent_v3_0:
    if corruption == 3:
        pass
    if corruption < 3:
        $ resolve_scene()
        Leyna "I don't want to go to the river yet.."
        ".. we can continue interviewing people in the town"
        call Movement("TownToRiverEvent_v3_0", "player", ["TURN_L","L"]) from _call_TownToRiverEvent_v3_0_Movement
        $ resolve_scene()
        "YOU NEED 3 POINTS OF CORRUPTION TO ENTER THE RIVER"
    $ resolve_scene()
    return False

label TownToRiverEvent_v3_1:
    Johan "We don't need to go back there for now."
    call Movement("TownToRiverEvent_v3_1", "player", ["TURN_L","L"]) from _call_TownToRiverEvent_v3_1_Movement
    $ resolve_scene()
    return False

label TownToRiverEvent_v3_2:
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "I don't want to go to the river without johan..."
    $ erase_picture(1)
    call Movement("TownToRiverEvent_v3_2", "player", ["TURN_L","L"]) from _call_TownToRiverEvent_v3_2_Movement
    $ resolve_scene()
    return False

label TownToRiverEvent_v3(play_event = True, trigger = None): # event
    if is_erased("TownToRiverEvent_v3"):
        return None
    elif trigger == "event" and switch("leyna_alone"):
        call PlayEvent(play_event, "TownToRiverEvent_v3_2", "TownToRiverEvent_v3") from _call_TownToRiverEvent_v3_2_PlayEvent
        return (0, "", "TownToRiverEvent_v3_2")
    elif trigger == "event" and switch("finished_river_scene"):
        call PlayEvent(play_event, "TownToRiverEvent_v3_1", "TownToRiverEvent_v3") from _call_TownToRiverEvent_v3_1_PlayEvent
        return (0, "", "TownToRiverEvent_v3_1")
    elif trigger == "event":
        call PlayEvent(play_event, "TownToRiverEvent_v3_0", "TownToRiverEvent_v3") from _call_TownToRiverEvent_v3_0_PlayEvent
        return (0, "", "TownToRiverEvent_v3_0")
    return None

label TownNPCwoman_0:
    Tourist "This town is beautiful,but there's almost no women here Thanks god I came with my friends. Men here are very thirsty"
    return False

label TownNPCwoman_2(menu_choice = None):
    Alexa "Do you want to go to the river now?"
    call GetChoice([_("Yes"), _("No")], value=menu_choice, called_from="TownNPCwoman_2") from _call_TownNPCwoman_2_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Yes"):
        $ menu_choice = None
        if corruption <= 9:
            $ resolve_scene()
            Leyna "N.. now? I wanted to take a walk around here before going there again"
            "(YOU NEED 9 POINTS OF CORRUPTION OR MORE TO ENTER THIS EVENT)"
            call Movement("TownNPCwoman_2", "TownNPCwoman", ["TURN_D"]) from _call_TownNPCwoman_2_Movement
        if corruption >= 9:
            $ resolve_scene()
            Leyna "Now? Okay, why not .."
            Alexa "Great! Let's do this"
            $ fade_out()
            call TransferPlayer("River2", "TownNPCwoman_2", 4, 10, direction=6) from _call_TownNPCwoman_2_TransferPlayer
            $ fade_in()
    elif menu_choice == _("No"):
        $ menu_choice = None
        $ show_transparent(1, "plano_mujer_timida", width=1600, height=900)
        $ resolve_scene()
        Leyna "N.. now? I wanted to take a walk around here before going there again"
        $ erase_picture(1)
        $ show_transparent(2, "alexa_gui_o")
        $ resolve_scene()
        Alexa "It's okay. If you change your mind come find me, I'll be here"
        $ erase_picture(2)
        call Movement("TownNPCwoman_2", "TownNPCwoman", ["TURN_D"]) from _call_TownNPCwoman_2_Movement_1
        $ set_switch("no_return_to_the_river", True)
    $ resolve_scene()
    return False

label TownNPCwoman(play_event = True, trigger = None): # event
    if is_erased("TownNPCwoman"):
        return None
    elif switch("second_river"):
        return None
    elif trigger == "event" and switch("no_return_to_the_river"):
        call PlayEvent(play_event, "TownNPCwoman_2", "TownNPCwoman") from _call_TownNPCwoman_2_PlayEvent
        return (1, "", "TownNPCwoman_2")
    elif switch("leyna_alone"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNPCwoman_0", "TownNPCwoman") from _call_TownNPCwoman_0_PlayEvent
        return (1, "", "TownNPCwoman_0")
    return None

label Townturista1_v2_0:
    Tourist "I wonder why nobody wants to come to this town. This place is pretty cool... and cheap"
    return False

label Townturista1_v2(play_event = True, trigger = None): # event
    if is_erased("Townturista1_v2"):
        return None
    elif switch("leyna_alone"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Townturista1_v2_0", "Townturista1_v2") from _call_Townturista1_v2_0_PlayEvent
        return (1, "", "Townturista1_v2_0")
    return None

label TownNPCtourist2_0:
    Tourist "Shit, there's almost no women here  and they are married. What, I'm the third wheel? ... I need a girlfriend..."
    return False

label TownNPCtourist2_1:
    Tourist "I should never have traveled with these two.."
    return False

label TownNPCtourist2(play_event = True, trigger = None): # event
    if is_erased("TownNPCtourist2"):
        return None
    elif trigger == "event" and switch("leyna_alone"):
        call PlayEvent(play_event, "TownNPCtourist2_1", "TownNPCtourist2") from _call_TownNPCtourist2_1_PlayEvent
        return (1, "", "TownNPCtourist2_1")
    elif trigger == "event":
        call PlayEvent(play_event, "TownNPCtourist2_0", "TownNPCtourist2") from _call_TownNPCtourist2_0_PlayEvent
        return (1, "", "TownNPCtourist2_0")
    return None

label TownNPCtourist3Base:
    Tourist "What a disappointment, the castle is closed."
    return False

label TownNPCtourist3(play_event = True, trigger = None): # event
    if is_erased("TownNPCtourist3"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNPCtourist3Base", "TownNPCtourist3") from _call_TownNPCtourist3_PlayEvent
        return (1, "", "TownNPCtourist3")
    return None

label TownNPCCantWaitBase:
    if not switch("leyna_alone"):
        $ resolve_scene()
        Villager "I can't wait for the festival to start"
        "( it's my chance to take off my office suit and walk around naked, 0 regrets hehehe.. )"
    if switch("leyna_alone"):
        Villager "I don't go very often to the river cause it's a \"just dick area\""
    $ resolve_scene()
    return False

label TownNPCCantWait(play_event = True, trigger = None): # event
    if is_erased("TownNPCCantWait"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNPCCantWaitBase", "TownNPCCantWait") from _call_TownNPCCantWait_PlayEvent
        return (1, "", "TownNPCCantWait")
    return None

label TownNPCmafiosoBase:
    if not switch("leyna_alone"):
        $ resolve_scene()
        Thug "Don't bother me, I'm waiting for a clien... mmm ... a friend"
    if switch("leyna_alone"):
        Thug "A pretty girl like you shouldn't be alone in this part of town"
        "All I'm saying is that shit happens, you know.."
    $ resolve_scene()
    return False

label TownNPCmafioso(play_event = True, trigger = None): # event
    if is_erased("TownNPCmafioso"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNPCmafiosoBase", "TownNPCmafioso") from _call_TownNPCmafioso_PlayEvent
        return (1, "", "TownNPCmafioso")
    return None

label TownborrachoBase:
    DrunkOldMan "p\@rT!y! ..hehehe..."
    return False

label Townborracho(play_event = True, trigger = None): # event
    if is_erased("Townborracho"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownborrachoBase", "Townborracho") from _call_Townborracho_PlayEvent
        return (1, "", "Townborracho")
    return None

label TownNPCVillagerBase:
    Villager "There's a lot to see in the town, I recommend you visit the river"
    return False

label TownNPCVillager(play_event = True, trigger = None): # event
    if is_erased("TownNPCVillager"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNPCVillagerBase", "TownNPCVillager") from _call_TownNPCVillager_PlayEvent
        return (1, "", "TownNPCVillager")
    return None

label TownmusicapuebloBase:
    call PlaySound("music", "audio/Town1.ogg", volume=0.9, no_loop=False) from _call_Townmusicapueblo_PlaySound
    $ resolve_scene()
    $ tint_screen((0, 0, 0, 0), 60, True)
    return False

label Townmusicapueblo(play_event = True, trigger = None): # parallel
    if is_erased("Townmusicapueblo"):
        return None
    elif trigger == "parallel":
        call PlayEvent(play_event, "TownmusicapuebloBase", "Townmusicapueblo") from _call_Townmusicapueblo_PlayEvent
        return (0, "", "Townmusicapueblo")
    return None

label TownToPoliceStationBase:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_TownToPoliceStation_PlaySound
    call TransferPlayer("PoliceStation", "TownToPoliceStation", 14, 12, direction=8) from _call_TownToPoliceStation_TransferPlayer
    $ resolve_scene()
    return False

label TownToPoliceStation(play_event = True, trigger = None): # event
    if is_erased("TownToPoliceStation"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownToPoliceStationBase", "TownToPoliceStation") from _call_TownToPoliceStation_PlayEvent
        return (0, "", "TownToPoliceStation")
    return None

label TownToPoliceStation_v2Base:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_TownToPoliceStation_v2_PlaySound
    call TransferPlayer("PoliceStation", "TownToPoliceStation_v2", 14, 12, direction=8) from _call_TownToPoliceStation_v2_TransferPlayer
    $ resolve_scene()
    return False

label TownToPoliceStation_v2(play_event = True, trigger = None): # event
    if is_erased("TownToPoliceStation_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownToPoliceStation_v2Base", "TownToPoliceStation_v2") from _call_TownToPoliceStation_v2_PlayEvent
        return (0, "", "TownToPoliceStation_v2")
    return None

label TownToPoliceStation_v3Base:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_TownToPoliceStation_v3_PlaySound
    call TransferPlayer("PoliceStation", "TownToPoliceStation_v3", 15, 12, direction=8) from _call_TownToPoliceStation_v3_TransferPlayer
    $ resolve_scene()
    return False

label TownToPoliceStation_v3(play_event = True, trigger = None): # event
    if is_erased("TownToPoliceStation_v3"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownToPoliceStation_v3Base", "TownToPoliceStation_v3") from _call_TownToPoliceStation_v3_PlayEvent
        return (0, "", "TownToPoliceStation_v3")
    return None

label TownPolicePosterBase:
    "Police station of Goddess cliff. to serve and protect."
    return False

label TownPolicePoster(play_event = True, trigger = None): # event
    if is_erased("TownPolicePoster"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownPolicePosterBase", "TownPolicePoster") from _call_TownPolicePoster_PlayEvent
        return (1, "", "TownPolicePoster")
    return None

label TownDataCityPosterBase:
    "Upper town"
    return False

label TownDataCityPoster(play_event = True, trigger = None): # event
    if is_erased("TownDataCityPoster"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownDataCityPosterBase", "TownDataCityPoster") from _call_TownDataCityPoster_PlayEvent
        return (1, "", "TownDataCityPoster")
    return None

label TownPillarBase:
    "Goddess Cliff: where dreams are lived day by day."
    return False

label TownPillar(play_event = True, trigger = None): # event
    if is_erased("TownPillar"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownPillarBase", "TownPillar") from _call_TownPillar_PlayEvent
        return (1, "", "TownPillar")
    return None

label TownNPCDrunkEvent1_0:
    DrunkVillager "what"
    return False

label TownNPCDrunkEvent1_1:
    DrunkVillager "You came for more?"
    return False

label TownNPCDrunkEvent1_2:
    Villager "The other day was good, you can find me here if you want to have a good time"
    return False

label TownNPCDrunkEvent1(play_event = True, trigger = None): # event
    if is_erased("TownNPCDrunkEvent1"):
        return None
    elif trigger == "event" and switch("leyna_alone"):
        call PlayEvent(play_event, "TownNPCDrunkEvent1_2", "TownNPCDrunkEvent1") from _call_TownNPCDrunkEvent1_2_PlayEvent
        return (1, "", "TownNPCDrunkEvent1_2")
    elif trigger == "event" and switch("neighborhood_grope"):
        call PlayEvent(play_event, "TownNPCDrunkEvent1_1", "TownNPCDrunkEvent1") from _call_TownNPCDrunkEvent1_1_PlayEvent
        return (1, "", "TownNPCDrunkEvent1_1")
    elif trigger == "event":
        call PlayEvent(play_event, "TownNPCDrunkEvent1_0", "TownNPCDrunkEvent1") from _call_TownNPCDrunkEvent1_0_PlayEvent
        return (1, "", "TownNPCDrunkEvent1_0")
    return None

label TownNPCDrunkEvent2_0:
    DrunkVillager "Hey..."
    return False

label TownNPCDrunkEvent2_1:
    DrunkVillager "... (glance)"
    return False

label TownNPCDrunkEvent2_2:
    Villager "Yeah, we will treat you well... hehehe"
    return False

label TownNPCDrunkEvent2(play_event = True, trigger = None): # event
    if is_erased("TownNPCDrunkEvent2"):
        return None
    elif trigger == "event" and switch("leyna_alone"):
        call PlayEvent(play_event, "TownNPCDrunkEvent2_2", "TownNPCDrunkEvent2") from _call_TownNPCDrunkEvent2_2_PlayEvent
        return (1, "", "TownNPCDrunkEvent2_2")
    elif trigger == "event" and switch("neighborhood_grope"):
        call PlayEvent(play_event, "TownNPCDrunkEvent2_1", "TownNPCDrunkEvent2") from _call_TownNPCDrunkEvent2_1_PlayEvent
        return (1, "", "TownNPCDrunkEvent2_1")
    elif trigger == "event":
        call PlayEvent(play_event, "TownNPCDrunkEvent2_0", "TownNPCDrunkEvent2") from _call_TownNPCDrunkEvent2_0_PlayEvent
        return (1, "", "TownNPCDrunkEvent2_0")
    return None

label Towneventolemetenmanobarrio_0:
    DrunkVillager "Oi! We're told you're doing an article about our traditions!"
    $ resolve_scene()
    call Movement("Towneventolemetenmanobarrio_0", "player", ["TURN_U"]) from _call_Towneventolemetenmanobarrio_0_Movement
    $ resolve_scene()
    Johan "(Wow... I see that in a small town  gossips spread quickly)"
    Johan "That's right, do you want to tell us something?"
    DrunkVillager "Nah, I'm too drunk to have a normal conversation, but I feel extremely handsome today"
    DrunkVillager "Why don't you take some pictures of me and my friend?"
    Johan "Oh, sure!"
    DrunkVillager "What a beautiful woman you have hidden there friend!"
    $ show_transparent(1, "expresion_gota")
    $ resolve_scene()
    Johan "What? My wife?"
    DrunkVillager "Is that your wife?.. Really? Wow some are lucky while we.. we are dying of the desire"
    Johan "(Dying of desire? Now he's getting poetic)"
    $ erase_picture(1)
    $ resolve_scene()
    Johan "You could say that I'm a very lucky man to have such a beautiful woman as a wife"
    $ show_transparent(1, "plano_mujer_sonrisa", width=1600, height=900)
    $ resolve_scene()
    Leyna "Hahahahaha how romantic!"
    DrunkVillager "Okey come here"
    $ show_picture(1, "manoseo2")
    $ resolve_scene()
    Johan "HEY!!"
    DrunkVillager "Come on! Don't worry, take a couple of pictures!"
    DrunkVillager "So there will be two beautiful people in the photo, not like my friend here"
    DrunkVillager2 "Fuck you..."
    Johan "I..."
    DrunkVillager "Come on! Look ...."
    $ fade_out()
    $ erase_picture(1)
    $ show_picture(2, "manoseo_3")
    $ fade_in()
    call PlaySound("sound", "audio/Jump1.ogg", volume=0.9, no_loop=True) from _call_Towneventolemetenmanobarrio_0_PlaySound
    $ resolve_scene()
    DrunkVillager "Take a picture now hahahahaha!"
    Johan "KNOCK IT OFF!!!"
    $ erase_picture(2)
    $ resolve_scene()
    DrunkVillager "Hahaha okay okay don't be mad it was a joke. We are all partying, relax a little!"
    Johan "Whatever, we are leaving!"
    call Movement("Towneventolemetenmanobarrio_0", "player", ["L","L"]) from _call_Towneventolemetenmanobarrio_0_Movement_1
    $ set_switch("neighborhood_grope", True)
    call GalleryViewed("manoseo") from _call_Towneventolemetenmanobarrio_0_GalleryViewed
    $ corruption = corruption + 1
    $ resolve_scene()
    "CORRUPTION +1"
    return False

label Towneventolemetenmanobarrio(play_event = True, trigger = None): # event
    if is_erased("Towneventolemetenmanobarrio"):
        return None
    elif switch("neighborhood_grope"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Towneventolemetenmanobarrio_0", "Towneventolemetenmanobarrio") from _call_Towneventolemetenmanobarrio_0_PlayEvent
        return (0, "", "Towneventolemetenmanobarrio_0")
    return None

label TownNPCPADRE_0:
    Villager "Come on kid let's go."
    $ resolve_scene()
    Kid "oookey"
    return False

label TownNPCPADRE_1:
    Villager "Sorry my son is a bit of a joker."
    return False

label TownNPCPADRE(play_event = True, trigger = None): # event
    if is_erased("TownNPCPADRE"):
        return None
    elif trigger == "event" and switch("lifted_skirt"):
        call PlayEvent(play_event, "TownNPCPADRE_1", "TownNPCPADRE") from _call_TownNPCPADRE_1_PlayEvent
        return (1, "", "TownNPCPADRE_1")
    elif trigger == "event":
        call PlayEvent(play_event, "TownNPCPADRE_0", "TownNPCPADRE") from _call_TownNPCPADRE_0_PlayEvent
        return (1, "", "TownNPCPADRE_0")
    return None

label TownNPCkid_0:
    Villager "Come on kid let's go."
    $ resolve_scene()
    Kid "oookey"
    return False

label TownNPCkid_1:
    Kid "Red panties! red panties!"
    if switch("leyna_alone"):
        pass
    if not switch("leyna_alone"):
        $ resolve_scene()
        Johan "(...)"
    $ resolve_scene()
    return False

label TownNPCkid(play_event = True, trigger = None): # event
    if is_erased("TownNPCkid"):
        return None
    elif trigger == "event" and switch("lifted_skirt"):
        call PlayEvent(play_event, "TownNPCkid_1", "TownNPCkid") from _call_TownNPCkid_1_PlayEvent
        return (1, "", "TownNPCkid_1")
    elif trigger == "event":
        call PlayEvent(play_event, "TownNPCkid_0", "TownNPCkid") from _call_TownNPCkid_0_PlayEvent
        return (1, "", "TownNPCkid_0")
    return None

label TownSkirtLift_0:
    call Movement("TownSkirtLift_0", "player", ["TURN_U"]) from _call_TownSkirtLift_0_Movement
    $ resolve_scene()
    Johan "A street market in the center of town, beautiful"
    Leyna "Yes, very joyful. I'm falling in love with this town"
    call Movement("TownSkirtLift_0", "TownNPCkid", ["L","U","U","L","L","L","L","TURN_U"]) from _call_TownSkirtLift_0_Movement_1
    $ resolve_scene()
    call Movement("TownSkirtLift_0", "TownNPCPADRE", ["L","U","L","L","L","TURN_U"]) from _call_TownSkirtLift_0_Movement_2
    $ resolve_scene()
    Villager "What's up son?"
    $ show_transparent(1, "plano_de_espaldas", width=1600, height=900)
    $ resolve_scene()
    Kid "Look dad, what a beautiful girl!"
    Villager "Yeah. A tourist that probably has come for the festival..."
    $ erase_picture(1)
    $ resolve_scene()
    Villager "...but I don't think she will go in as soon as she sees the requirements. After all, most of the women in this town have left for a reason..."
    $ resolve_scene()
    Kid "And what if i prank her, dad?"
    Villager "A prank?"
    Kid "Yeah, I can lift her skirt and run away hahaha"
    Villager "(Oh! ... No, I shouldn't ... but ... sorry son. I'm turning you into a savage, but that woman has a gorgeous body!)"
    $ resolve_scene()
    Villager "Hahahaha I see... yes!, it's a good idea son, very ... funny!"
    Kid "Alright then...!"
    $ fade_out()
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownSkirtLift_0_PlaySound
    $ set_switch("lifted_skirt", True)
    call GalleryViewed("levantamiento_de_falda") from _call_TownSkirtLift_0_GalleryViewed
    $ show_transparent(2, "levantamiento_de_falda_1", scale=(69, 69), width=1600, height=900)
    $ fade_in()
    $ resolve_scene()
    Villager "(!!!!)"
    pause
    $ erase_picture(2)
    $ show_transparent(3, "levantamiento_falda_2", scale=(69, 69), width=1600, height=900)
    $ resolve_scene()
    Leyna "Oh?"
    Villager "(DAMN, HE DID IT!)"
    pause
    $ fade_out()
    $ erase_picture(3)
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_TownSkirtLift_0_PlaySound_1
    call SetEventLocation("TownSkirtLift_0", "TownNPCPADRE", 17, 24) from _call_TownSkirtLift_0_setloc
    call SetEventLocation("TownSkirtLift_0", "TownNPCkid", 17, 25) from _call_TownSkirtLift_0_setloc_1
    $ fade_in()
    $ resolve_scene()
    Johan "Damn kids ..."
    Leyna "Well, don't be angry Johan, it's a silly joke"
    $ corruption = corruption + 1
    "CORRUPTION +1"
    return False

label TownSkirtLift(play_event = True, trigger = None): # event
    if is_erased("TownSkirtLift"):
        return None
    elif switch("lifted_skirt"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownSkirtLift_0", "TownSkirtLift") from _call_TownSkirtLift_0_PlayEvent
        return (0, "", "TownSkirtLift_0")
    return None

label TownNPCRelaxBase:
    OldVillager "I always come here to relax, it's a nice place..."
    return False

label TownNPCRelax(play_event = True, trigger = None): # event
    if is_erased("TownNPCRelax"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNPCRelaxBase", "TownNPCRelax") from _call_TownNPCRelax_PlayEvent
        return (1, "", "TownNPCRelax")
    return None

label Townhombrepaseando3Base:
    Villager "All work and no play makes jack a dull boy..."
    return False

label Townhombrepaseando3(play_event = True, trigger = None): # event
    if is_erased("Townhombrepaseando3"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "Townhombrepaseando3Base", "Townhombrepaseando3") from _call_Townhombrepaseando3_PlayEvent
        return (1, "", "Townhombrepaseando3")
    return None

label TownNPCBrowserBase:
    Villager "This is trash..."
    return False

label TownNPCBrowser(play_event = True, trigger = None): # event
    if is_erased("TownNPCBrowser"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownNPCBrowserBase", "TownNPCBrowser") from _call_TownNPCBrowser_PlayEvent
        return (1, "", "TownNPCBrowser")
    return None

label TownClothingSignBase:
    "Happy pig Clothes and accessories"
    return False

label TownClothingSign(play_event = True, trigger = None): # event
    if is_erased("TownClothingSign"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownClothingSignBase", "TownClothingSign") from _call_TownClothingSign_PlayEvent
        return (1, "", "TownClothingSign")
    return None

label TownStoreSignBase:
    "General goods."
    return False

label TownStoreSign(play_event = True, trigger = None): # event
    if is_erased("TownStoreSign"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownStoreSignBase", "TownStoreSign") from _call_TownStoreSign_PlayEvent
        return (1, "", "TownStoreSign")
    return None

label Townfinaldelprimerdia_0:
    Leyna "Johan wait..."
    call Movement("Townfinaldelprimerdia_0", "player", ["TURN_R"]) from _call_Townfinaldelprimerdia_0_Movement
    $ resolve_scene()
    Johan "Is something wrong ?"
    Leyna "No no, nothing's wrong but... It has been a very long day and with the trip and the interviews I'm tired..."
    "Can we go back to the hotel and go to sleep?"
    Johan "Oh of course"
    call TransferPlayer("InnRooms", "Townfinaldelprimerdia_0", 7, 17, direction=6) from _call_Townfinaldelprimerdia_0_TransferPlayer
    call Movement("Townfinaldelprimerdia_0", "player", ["R","R","R","R","U","U","U"]) from _call_Townfinaldelprimerdia_0_Movement_1
    $ fade_out()
    if not renpy.in_rollback():
        $ _saved_bgm = renpy.music.get_playing()
    play music "audio/Inn.ogg" volume 0.9 noloop
    if _saved_bgm is not None and not renpy.in_rollback():
        queue music _saved_bgm
        $ _saved_bgm = None
    call TransferPlayer("Inn", "Townfinaldelprimerdia_0", 2, 3, direction=6) from _call_Townfinaldelprimerdia_0_TransferPlayer_1
    $ fade_in()
    call Movement("Townfinaldelprimerdia_0", "player", ["R","R","R","TURN_L"]) from _call_Townfinaldelprimerdia_0_Movement_2
    $ resolve_scene()
    Johan "Leyna, today I'm going to the town hall to interview the mayor and talk to some public employees..."
    "..if you want, take advantage of the day and take a walk around the town, you know ... relax and meet some friendly villagers"
    "I've been told the hot springs are already open, in case you wanna take a relaxing bath"
    Leyna "Well... yes, you're right. I think I need a day to relax a little. See you here in the afternoon?"
    Johan "Yeah perfect! See you later"
    $ fade_out()
    call ChangePartyMember("Johan", False) from _call_Townfinaldelprimerdia_0_ChangePartyMember
    call TransferPlayer("Town", "Townfinaldelprimerdia_0", 28, 21, direction=2) from _call_Townfinaldelprimerdia_0_TransferPlayer_2
    $ fade_in()
    call Movement("Townfinaldelprimerdia_0", "player", ["D","D"]) from _call_Townfinaldelprimerdia_0_Movement_3
    $ show_transparent(1, "plano_mujer_sonrisa", width=1600, height=900)
    $ resolve_scene()
    Leyna "A day for myself ..."
    $ erase_picture(1)
    $ set_switch("leyna_alone", True)
    $ resolve_scene()
    return False

label Townfinaldelprimerdia(play_event = True, trigger = None): # event
    if is_erased("Townfinaldelprimerdia"):
        return None
    elif switch("leyna_alone"):
        return None
    elif trigger == "event" and switch("finished_river_scene"):
        call PlayEvent(play_event, "Townfinaldelprimerdia_0", "Townfinaldelprimerdia") from _call_Townfinaldelprimerdia_0_PlayEvent
        return (0, "", "Townfinaldelprimerdia_0")
    return None

label Townfinaldelprimerdia_v2_0:
    Leyna "Johan wait..."
    call Movement("Townfinaldelprimerdia_v2_0", "player", ["TURN_R"]) from _call_Townfinaldelprimerdia_v2_0_Movement
    $ resolve_scene()
    Johan "Is something wrong ?"
    Leyna "No no, nothing's wrong but... It has been a very long day and with the trip and the interviews I'm tired..."
    "Can we go back to the hotel and go to sleep?"
    Johan "Oh of course"
    call TransferPlayer("InnRooms", "Townfinaldelprimerdia_v2_0", 7, 17, direction=6) from _call_Townfinaldelprimerdia_v2_0_TransferPlayer
    call Movement("Townfinaldelprimerdia_v2_0", "player", ["R","R","R","R","U","U","U"]) from _call_Townfinaldelprimerdia_v2_0_Movement_1
    $ fade_out()
    if not renpy.in_rollback():
        $ _saved_bgm = renpy.music.get_playing()
    play music "audio/Inn.ogg" volume 0.9 noloop
    if _saved_bgm is not None and not renpy.in_rollback():
        queue music _saved_bgm
        $ _saved_bgm = None
    call TransferPlayer("Inn", "Townfinaldelprimerdia_v2_0", 2, 3, direction=6) from _call_Townfinaldelprimerdia_v2_0_TransferPlayer_1
    $ fade_in()
    call Movement("Townfinaldelprimerdia_v2_0", "player", ["R","R","R","TURN_L"]) from _call_Townfinaldelprimerdia_v2_0_Movement_2
    $ resolve_scene()
    Johan "Leyna, today I'm going to the town hall to interview the mayor and talk to some public employees..."
    "..if you want, take advantage of the day and take a walk around the town, you know ... relax and meet some friendly villagers"
    "I've been told the hot springs are already open, in case you wanna take a relaxing bath"
    Leyna "Well... yes, you're right. I think I need a day to relax a little. See you here in the afternoon?"
    Johan "Yeah perfect! See you later"
    $ fade_out()
    call ChangePartyMember("Johan", False) from _call_Townfinaldelprimerdia_v2_0_ChangePartyMember
    call TransferPlayer("Town", "Townfinaldelprimerdia_v2_0", 28, 21, direction=2) from _call_Townfinaldelprimerdia_v2_0_TransferPlayer_2
    $ fade_in()
    call Movement("Townfinaldelprimerdia_v2_0", "player", ["D","D"]) from _call_Townfinaldelprimerdia_v2_0_Movement_3
    $ show_transparent(1, "plano_mujer_sonrisa", width=1600, height=900)
    $ resolve_scene()
    Leyna "A day for myself ..."
    $ erase_picture(1)
    $ set_switch("leyna_alone", True)
    $ resolve_scene()
    return False

label Townfinaldelprimerdia_v2(play_event = True, trigger = None): # event
    if is_erased("Townfinaldelprimerdia_v2"):
        return None
    elif switch("leyna_alone"):
        return None
    elif trigger == "event" and switch("finished_river_scene"):
        call PlayEvent(play_event, "Townfinaldelprimerdia_v2_0", "Townfinaldelprimerdia_v2") from _call_Townfinaldelprimerdia_v2_0_PlayEvent
        return (0, "", "Townfinaldelprimerdia_v2_0")
    return None

label Townfinaldelprimerdia_v3_0:
    Leyna "Johan wait..."
    call Movement("Townfinaldelprimerdia_v3_0", "player", ["TURN_R"]) from _call_Townfinaldelprimerdia_v3_0_Movement
    $ resolve_scene()
    Johan "Is something wrong ?"
    Leyna "No no, nothing's wrong but... It has been a very long day and with the trip and the interviews I'm tired..."
    "Can we go back to the hotel and go to sleep?"
    Johan "Oh of course"
    call TransferPlayer("InnRooms", "Townfinaldelprimerdia_v3_0", 7, 17, direction=6) from _call_Townfinaldelprimerdia_v3_0_TransferPlayer
    call Movement("Townfinaldelprimerdia_v3_0", "player", ["R","R","R","R","U","U","U"]) from _call_Townfinaldelprimerdia_v3_0_Movement_1
    $ fade_out()
    if not renpy.in_rollback():
        $ _saved_bgm = renpy.music.get_playing()
    play music "audio/Inn.ogg" volume 0.9 noloop
    if _saved_bgm is not None and not renpy.in_rollback():
        queue music _saved_bgm
        $ _saved_bgm = None
    call TransferPlayer("Inn", "Townfinaldelprimerdia_v3_0", 2, 3, direction=6) from _call_Townfinaldelprimerdia_v3_0_TransferPlayer_1
    $ fade_in()
    call Movement("Townfinaldelprimerdia_v3_0", "player", ["R","R","R","TURN_L"]) from _call_Townfinaldelprimerdia_v3_0_Movement_2
    $ resolve_scene()
    Johan "Leyna, today I'm going to the town hall to interview the mayor and talk to some public employees..."
    "..if you want, take advantage of the day and take a walk around the town, you know ... relax and meet some friendly villagers"
    "I've been told the hot springs are already open, in case you wanna take a relaxing bath"
    Leyna "Well... yes, you're right. I think I need a day to relax a little. See you here in the afternoon?"
    Johan "Yeah perfect! See you later"
    $ fade_out()
    call ChangePartyMember("Johan", False) from _call_Townfinaldelprimerdia_v3_0_ChangePartyMember
    call TransferPlayer("Town", "Townfinaldelprimerdia_v3_0", 28, 21, direction=2) from _call_Townfinaldelprimerdia_v3_0_TransferPlayer_2
    $ fade_in()
    call Movement("Townfinaldelprimerdia_v3_0", "player", ["D","D"]) from _call_Townfinaldelprimerdia_v3_0_Movement_3
    $ show_transparent(1, "plano_mujer_sonrisa", width=1600, height=900)
    $ resolve_scene()
    Leyna "A day for myself ..."
    $ erase_picture(1)
    $ set_switch("leyna_alone", True)
    $ resolve_scene()
    return False

label Townfinaldelprimerdia_v3(play_event = True, trigger = None): # event
    if is_erased("Townfinaldelprimerdia_v3"):
        return None
    elif switch("leyna_alone"):
        return None
    elif trigger == "event" and switch("finished_river_scene"):
        call PlayEvent(play_event, "Townfinaldelprimerdia_v3_0", "Townfinaldelprimerdia_v3") from _call_Townfinaldelprimerdia_v3_0_PlayEvent
        return (0, "", "Townfinaldelprimerdia_v3_0")
    return None

label Townfinaldelprimerdia_v4_0:
    Leyna "Johan wait..."
    call Movement("Townfinaldelprimerdia_v4_0", "player", ["TURN_U"]) from _call_Townfinaldelprimerdia_v4_0_Movement
    $ resolve_scene()
    Johan "Is something wrong ?"
    Leyna "No no, nothing wrong but... It has been a very long day and between the trip and the interviews i'm tired.."
    "Can we go back to the hotel and go to sleep?"
    Johan "Oh of course"
    call TransferPlayer("InnRooms", "Townfinaldelprimerdia_v4_0", 7, 17, direction=6) from _call_Townfinaldelprimerdia_v4_0_TransferPlayer
    call Movement("Townfinaldelprimerdia_v4_0", "player", ["R","R","R","R","U","U","U"]) from _call_Townfinaldelprimerdia_v4_0_Movement_1
    $ fade_out()
    if not renpy.in_rollback():
        $ _saved_bgm = renpy.music.get_playing()
    play music "audio/Inn.ogg" volume 0.9 noloop
    if _saved_bgm is not None and not renpy.in_rollback():
        queue music _saved_bgm
        $ _saved_bgm = None
    call TransferPlayer("Inn", "Townfinaldelprimerdia_v4_0", 2, 3, direction=6) from _call_Townfinaldelprimerdia_v4_0_TransferPlayer_1
    $ fade_in()
    call Movement("Townfinaldelprimerdia_v4_0", "player", ["R","R","R","TURN_L"]) from _call_Townfinaldelprimerdia_v4_0_Movement_2
    $ resolve_scene()
    Johan "Leyna, Today I'm going to the town hall to interview the mayor and talk to some public employees..."
    "...If you want to take advantage of the day and take a walk around the town, You know ... relax and meet some friendly villagers."
    "I've been told that the hot springs are already open in case you want to take a relaxing bath."
    Leyna "Well... yes, you're right, i think i need a day to relax a little. See you here in the afternoon?"
    Johan "Yeah perfect! see you later."
    $ fade_out()
    call ChangePartyMember("Johan", False) from _call_Townfinaldelprimerdia_v4_0_ChangePartyMember
    call TransferPlayer("Town", "Townfinaldelprimerdia_v4_0", 28, 21, direction=2) from _call_Townfinaldelprimerdia_v4_0_TransferPlayer_2
    $ fade_in()
    call Movement("Townfinaldelprimerdia_v4_0", "player", ["D","D"]) from _call_Townfinaldelprimerdia_v4_0_Movement_3
    $ show_transparent(1, "plano_mujer_sonrisa", width=1600, height=900)
    $ resolve_scene()
    Leyna "A day for myself ..."
    $ erase_picture(1)
    $ set_switch("leyna_alone", True)
    $ resolve_scene()
    return False

label Townfinaldelprimerdia_v4(play_event = True, trigger = None): # event
    if is_erased("Townfinaldelprimerdia_v4"):
        return None
    elif switch("leyna_alone"):
        return None
    elif trigger == "event" and switch("finished_river_scene"):
        call PlayEvent(play_event, "Townfinaldelprimerdia_v4_0", "Townfinaldelprimerdia_v4") from _call_Townfinaldelprimerdia_v4_0_PlayEvent
        return (0, "", "Townfinaldelprimerdia_v4_0")
    return None

label TownToPathBase:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_TownEV079_PlaySound
    call TransferPlayer("Path", "TownEV079", 36, 9, direction=4) from _call_TownEV079_TransferPlayer
    $ resolve_scene()
    return False

label TownToPath(play_event = True, trigger = None): # event
    if is_erased("TownToPath"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownToPathBase", "TownToPath") from _call_TownToPath_PlayEvent
        return (0, "", "TownToPath")
    return None

label TownToPath_v2Base:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_TownEV080_PlaySound
    call TransferPlayer("Path", "TownEV080", 36, 10, direction=4) from _call_TownEV080_TransferPlayer
    $ resolve_scene()
    return False

label TownToPath_v2(play_event = True, trigger = None): # event
    if is_erased("TownToPath_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownToPath_v2Base", "TownToPath_v2") from _call_TownToPath_v2_PlayEvent
        return (0, "", "TownToPath_v2")
    return None

label Townfotografo_0:
    OldMan "... need anything?"
    return False

label Townfotografo_1:
    if not switch("hot_springs_first_visit"):
        $ resolve_scene()
        OldMan "The magazine loved the pictures, give me time to prepare things so we can do the second session"
        "On the meantime maybe you could visit the hot springs, which are on the west of the town"
    if switch("hot_springs_first_visit"):
        OldMan "I have almost everything ready, can you go to the clothing store and pick up the package of lingerie that the fashion magazine sent me?"
        Leyna "Okey!"
        $ set_switch("pick_up_package", True)
    $ resolve_scene()
    return False

label Townfotografo_2:
    OldMan "Do you have the package?"
    return False

label Townfotografo_3:
    Leyna "Sir, I have the package"
    call PlaySound("sound", "audio/Recovery.ogg", volume=0.9, no_loop=True) from _call_Townfotografo_3_PlaySound
    $ set_item("clothes", False)
    OldMan "Perfect, the second session is going to be a little different from the first"
    OldMan "My grandson is a young man with an impressive physique and I don't want him to stay the rest of his days in this town."
    OldMan "So I'm helping him and I'd like to introduce him to the world of modelling"
    $ show_transparent(1, "plano_mujer_cartoon", width=1600, height=900)
    $ resolve_scene()
    Leyna "That's... sweet i suppose"
    OldMan "Hahaha, well that's why I asked him to pose with you this time"
    Leyna "With me?..."
    OldMan "Yeah, I was thinking of doing something a little more artistic, the boy will go with the traditional clothes and you with lingerie from the magazine"
    OldMan "If that's okay with you, of course"
    $ erase_picture(1)
    $ resolve_scene()
    Leyna "Well yes, why not?"
    OldMan "Great! Let's go there"
    call TransferPlayer("Photoshoot2", "Townfotografo_3", 2, 12, direction=8) from _call_Townfotografo_3_TransferPlayer
    $ resolve_scene()
    return False

label Townfotografo_4:
    OldMan "It's been a pleasure working with you"
    OldMan "If I get a new offer from the magazine I will let you know"
    $ show_transparent(1, "plano_mujer_cartoon", width=1600, height=900)
    $ resolve_scene()
    Leyna "Okay, thank you"
    $ erase_picture(1)
    $ resolve_scene()
    return False

label Townfotografo(play_event = True, trigger = None): # event
    if is_erased("Townfotografo"):
        return None
    elif trigger == "event" and switch("second_photo_session"):
        call PlayEvent(play_event, "Townfotografo_4", "Townfotografo") from _call_Townfotografo_4_PlayEvent
        return (1, "", "Townfotografo_4")
    elif trigger == "event" and switch("collected_package"):
        call PlayEvent(play_event, "Townfotografo_3", "Townfotografo") from _call_Townfotografo_3_PlayEvent
        return (1, "", "Townfotografo_3")
    elif trigger == "event" and switch("pick_up_package"):
        call PlayEvent(play_event, "Townfotografo_2", "Townfotografo") from _call_Townfotografo_2_PlayEvent
        return (1, "", "Townfotografo_2")
    elif trigger == "event" and switch("first_photo_session"):
        call PlayEvent(play_event, "Townfotografo_1", "Townfotografo") from _call_Townfotografo_1_PlayEvent
        return (1, "", "Townfotografo_1")
    elif trigger == "event":
        call PlayEvent(play_event, "Townfotografo_0", "Townfotografo") from _call_Townfotografo_0_PlayEvent
        return (1, "", "Townfotografo_0")
    return None

label Towneventofotografiaintro_0(menu_choice = None):
    $ event_erased = False
    if switch("photo_not_taken"):
        $ resolve_scene()
        OldMan "Have you changed your mind?"
        call GetChoice([_("Yes"), _("No")], value=menu_choice, called_from="Towneventofotografiaintro_0") from _call_Towneventofotografiaintro_0_GetChoice
        $ menu_choice = _return
        if menu_choice == _("Yes"):
            $ menu_choice = None
            $ resolve_scene()
            Leyna "Well.. I've some free time and a little extra money won't hurt me.. Sure, I'm interested"
            OldMan "Perfect, come with me to my house, that's where I have the photo studio.."
            $ fade_out()
            $ event_erased = True
            call TransferPlayer("PhotographersHouse", "Towneventofotografiaintro_0", 2, 12, direction=8) from _call_Towneventofotografiaintro_0_TransferPlayer
            $ fade_in()
        elif menu_choice == _("No"):
            $ menu_choice = None
            $ resolve_scene()
            Leyna "I'm sorry, I'm not interested right now..."
            OldMan "Oh it's fine, if you change your mind I'll be here"
            call Movement("Towneventofotografiaintro_0", "player", ["TURN_D","D","D"]) from _call_Towneventofotografiaintro_0_Movement
    if not switch("photo_not_taken"):
        $ resolve_scene()
        OldMan "Excuse me miss, you aren't from this town, right?"
        $ show_transparent(1, "expresion_neutral_mujer", width=1600, height=900)
        $ resolve_scene()
        Leyna "No, I'm writing an article with my husband."
        OldMan "I see... You've come to see the festival, I'm the town's photographer"
        "You know.. basically passport photo, ID photos and a few weddings around here..."
        "... it's strange to see such a beautiful woman in this town"
        $ show_transparent(2, "plano_mujer_sonrisa", width=1600, height=900)
        $ erase_picture(1)
        $ resolve_scene()
        Leyna "Hahaha, thank you very much"
        OldMan "Would you mind if I ask you something? Would you be interested in doing a job?"
        $ show_transparent(3, "plano_mujer_sorpresa_lado", width=1600, height=900)
        $ erase_picture(2)
        $ resolve_scene()
        Leyna "A job?... What is it about?"
        OldMan "You see.. with passport photos I cannot earn a living.."
        ".. I recently got a job online for a lingerie magazine, I've already been paid and they sent me the clothes to do a photoshoot .."
        "... the problem is my wife doesn't want to pose for me (and she is not as attractive as you)"
        "Would you be interested in doing a session with me? I would pay you for this job, of course"
        call GetChoice([_("Yes"), _("No")], value=menu_choice, called_from="Towneventofotografiaintro_0") from _call_Towneventofotografiaintro_0_GetChoice_1
        $ menu_choice = _return
        if menu_choice == _("Yes"):
            $ menu_choice = None
            $ resolve_scene()
            Leyna "Well.. I've some free time and a little extra money won't hurt me.. Sure, I'm interested"
            OldMan "Perfect, come with me to my house, that's where I have the photo studio.."
            $ fade_out()
            $ erase_picture(3)
            $ event_erased = True
            call TransferPlayer("PhotographersHouse", "Towneventofotografiaintro_0", 2, 12, direction=8) from _call_Towneventofotografiaintro_0_TransferPlayer_1
            $ fade_in()
        elif menu_choice == _("No"):
            $ menu_choice = None
            $ resolve_scene()
            Leyna "I'm sorry, I'm not interested right now..."
            OldMan "Oh it's fine, if you change your mind I'll be here"
            $ erase_picture(3)
            call Movement("Towneventofotografiaintro_0", "player", ["TURN_D","D","D"]) from _call_Towneventofotografiaintro_0_Movement_1
        $ set_switch("photo_not_taken", True)
    $ resolve_scene()
    return event_erased

label Towneventofotografiaintro(play_event = True, trigger = None): # event
    if is_erased("Towneventofotografiaintro"):
        return None
    elif switch("first_photo_session"):
        return None
    elif trigger == "event" and switch("leyna_alone"):
        call PlayEvent(play_event, "Towneventofotografiaintro_0", "Towneventofotografiaintro") from _call_Towneventofotografiaintro_0_PlayEvent
        return (0, "", "Towneventofotografiaintro_0")
    return None

label TownToGladeBase:
    call TransferPlayer("Glade", "TownEV083", 0, 5, direction=6) from _call_TownEV083_TransferPlayer
    $ resolve_scene()
    return False

label TownToGlade(play_event = True, trigger = None): # event
    if is_erased("TownToGlade"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownToGladeBase", "TownToGlade") from _call_TownToGlade_PlayEvent
        return (0, "", "TownToGlade")
    return None

label TownToGlade_v2Base:
    call TransferPlayer("Glade", "TownEV084", 0, 6, direction=6) from _call_TownEV084_TransferPlayer
    $ resolve_scene()
    return False

label TownToGlade_v2(play_event = True, trigger = None): # event
    if is_erased("TownToGlade_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownToGlade_v2Base", "TownToGlade_v2") from _call_TownToGlade_v2_PlayEvent
        return (0, "", "TownToGlade_v2")
    return None

label TownMeetAlexa_0(menu_choice = None):
    call Movement("TownEV085_0", "player", ["TURN_L"]) from _call_TownEV085_0_Movement
    $ resolve_scene()
    TouristWoman "Don't be mad, it was silly"
    $ resolve_scene()
    Tourist "I thought it would be good for us to come on this trip, but I start to think that it wasn't a good idea"
    $ resolve_scene()
    TouristWoman "You don't have to worry, we've come to enjoy with our friends. You don't need to watch over me all the time"
    Tourist "But .. there are many men here and I .."
    TouristWoman "We have already talked about that, you know it was a mistake and it won't happen again. Try to enjoy this vacation"
    Tourist "I know, but I don't trust those villagers."
    $ resolve_scene()
    "Sorry I distrusted you honey. I'm going back to the inn to apologize for my earlier behaviour"
    call Movement("TownEV085_0", "Townturista1_v2", ["D","D","D","D"]) from _call_TownEV085_0_Movement_1
    $ fade_out()
    call SetEventLocation("TownEV085_0", "Townturista1_v2", 1, 36) from _call_TownEV085_0_setloc
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_TownEV085_0_PlaySound
    $ fade_in()
    call Movement("TownEV085_0", "player", ["L","L","L","L","L"]) from _call_TownEV085_0_Movement_2
    call Movement("TownEV085_0", "TownNPCwoman", ["TURN_R"]) from _call_TownEV085_0_Movement_3
    $ show_transparent(1, "plano_mujer_cerca", width=1600, height=900)
    $ resolve_scene()
    Leyna "Hello, are you okay? I thought you were arguing .."
    $ erase_picture(1)
    $ show_transparent(9, "alexa_timida")
    $ resolve_scene()
    TouristWoman "It's all good, thanks. He's my husband, sometimes he gets a little jealous, and there are many men here..."
    $ erase_picture(9)
    $ show_transparent(2, "plano_mujer_sonrisa", width=1600, height=900)
    $ resolve_scene()
    Leyna "Yeah.. (You're telling me!) By the way, I haven't introduced myself, my name is Leyna"
    "I came with my husband to photograph the festival"
    $ erase_picture(2)
    $ show_transparent(10, "alexa_neutral")
    $ resolve_scene()
    TouristWoman "Nice to meet you, my name is Alexa and I've come to save my marriage .."
    $ erase_picture(10)
    $ show_transparent(3, "plano_mujer_ojos_blanco_negro", width=1600, height=900)
    $ resolve_scene()
    "hahahaha.. Just kidding, we're sightseeing"
    $ erase_picture(3)
    $ show_transparent(4, "plano_mujer_sonrisa", width=1600, height=900)
    $ resolve_scene()
    Leyna "Hahaha.. Okey"
    "I'm alone today and I was taking a walk around the area. I was told that there are hot springs around here"
    $ erase_picture(4)
    $ show_transparent(11, "alexa_gui_o")
    $ resolve_scene()
    Alexa "Yes, we've already gone. They are a great place to relax ... but I prefer the river"
    $ erase_picture(11)
    $ show_transparent(5, "plano_mujer_timida", width=1600, height=900)
    $ resolve_scene()
    Leyna "The river? But .. everyone goes naked there, don't you feel ashamed?"
    $ erase_picture(5)
    $ show_transparent(12, "alexa_gui_o")
    $ resolve_scene()
    Alexa "No way! We are all born naked, there is nothing to be ashamed of"
    $ erase_picture(12)
    $ show_transparent(6, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Yeah well .."
    Alexa "Don't be ashamed, you have a beautiful body, surely the men around here have their eyes on you hahaha"
    $ erase_picture(6)
    $ show_transparent(7, "plano_mujer_timida", width=1600, height=900)
    $ resolve_scene()
    Leyna "The thing is that I travel with my husband and it's a bit violent to go somewhere like that with him ..."
    $ erase_picture(7)
    $ resolve_scene()
    $ show_transparent(13, "alexa_timida")
    $ resolve_scene()
    Alexa "Look, if you want we can go together and so we protect each other"
    $ erase_picture(13)
    $ show_transparent(8, "expresion_ilusion_mujer", width=1600, height=900)
    $ resolve_scene()
    Leyna "Sure, it would be great to go together!"
    $ erase_picture(8)
    $ resolve_scene()
    "Do you want to go to the river with Alexa now?"
    call GetChoice([_("Yes"), _("No")], value=menu_choice, called_from="TownEV085_0") from _call_TownEV085_0_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Yes"):
        $ menu_choice = None
        if corruption <= 9:
            $ resolve_scene()
            Leyna "N.. now? I wanted to take a walk around here before going there again"
            "(YOU NEED 9 POINTS OF CORRUPTION OR MORE TO ENTER THIS EVENT)"
            call Movement("TownEV085_0", "TownNPCwoman", ["TURN_D"]) from _call_TownEV085_0_Movement_4
            call Movement("TownEV085_0", "player", ["TURN_R","R"]) from _call_TownEV085_0_Movement_5
            $ set_switch("no_return_to_the_river", True)
        if corruption >= 9:
            $ resolve_scene()
            Leyna "Now? Okay, why not .."
            Alexa "Great! Let's do this"
            $ fade_out()
            call TransferPlayer("River2", "TownEV085_0", 4, 10, direction=6) from _call_TownEV085_0_TransferPlayer
            $ fade_in()
    elif menu_choice == _("No"):
        $ menu_choice = None
        $ show_transparent(1, "plano_mujer_timida", width=1600, height=900)
        $ resolve_scene()
        Leyna "N.. now? I wanted to take a walk around here before going there again"
        $ erase_picture(1)
        $ show_transparent(2, "alexa_gui_o")
        $ resolve_scene()
        Alexa "It's okay. If you change your mind come find me, I'll be here"
        $ erase_picture(2)
        call Movement("TownEV085_0", "TownNPCwoman", ["TURN_D"]) from _call_TownEV085_0_Movement_6
        call Movement("TownEV085_0", "player", ["TURN_R","R"]) from _call_TownEV085_0_Movement_7
        $ set_switch("no_return_to_the_river", True)
    $ resolve_scene()
    return False

label TownMeetAlexa(play_event = True, trigger = None): # event
    if is_erased("TownMeetAlexa"):
        return None
    elif switch("no_return_to_the_river"):
        return None
    elif trigger == "event" and switch("leyna_alone"):
        call PlayEvent(play_event, "TownMeetAlexa_0", "TownMeetAlexa") from _call_TownMeetAlexa_0_PlayEvent
        return (0, "", "TownMeetAlexa_0")
    return None

label TownGraveBase:
    "Here lies Geralt of Rivia, the mercenary knight"
    return False

label TownGrave(play_event = True, trigger = None): # event
    if is_erased("TownGrave"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownGraveBase", "TownGrave") from _call_TownGrave_PlayEvent
        return (1, "", "TownGrave")
    return None

label TownCorruptionCounterBase:
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

label TownCorruptionCounter(play_event = True, trigger = None): # event
    if is_erased("TownCorruptionCounter"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownCorruptionCounterBase", "TownCorruptionCounter") from _call_TownCorruptionCounter_PlayEvent
        return (1, "", "TownCorruptionCounter")
    return None

label TownCorruptionFairy_0:
    $ event_erased = False
    $ fairy = 1
    $ resolve_scene()
    "Hello player! I want to introduce you to the corruption counter, this sculpture on my right"
    "Each time you win a corruption point, you will be able to see it here"
    "Some scenes require a minimum level of corruption"
    "so if you think you don't have it, come here and check it out"
    $ resolve_scene()
    call Movement("TownCorruptionFairy_0", "TownCorruptionFairy", [["JUMP",0,0]]) from _call_TownCorruptionFairy_0_Movement
    $ resolve_scene()
    "Oh! One more thing.."
    "On a poster South of here you can see clues of what to do every time you feel lost"
    "I do not recommend it if you prefer to travel freely on the map"
    "Have fun!!!!!!!!!!!!!! Bye"
    call ShowAnimation(117, "TownCorruptionFairy", "TownCorruptionFairy_0") from _call_TownCorruptionFairy_0_ShowAnimation
    $ fairy = 2
    $ event_erased = True
    return event_erased

label TownCorruptionFairy(play_event = True, trigger = None): # event
    if is_erased("TownCorruptionFairy"):
        return None
    elif fairy >= 2:
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "TownCorruptionFairy_0", "TownCorruptionFairy") from _call_TownCorruptionFairy_0_PlayEvent
        return (1, "", "TownCorruptionFairy_0")
    return None

label TownEV090_0:
    label TownEV090_0_loop_1:
        $ resolve_scene()
        call PauseForBalloon("TownEV090_0") from _call_TownEV090_0_PauseForBalloon
        # jump TownEV090_0_loop_1
    label TownEV090_0_loop_1_end:
        pass
    $ fairy = 1
    $ resolve_scene()
    return False

label TownEV090(play_event = True, trigger = None): # None-only parallel
    if is_erased("TownEV090"):
        return None
    elif fairy >= 1:
        return None
    elif trigger == "parallel":
        return None # TownEV090_0 potentially infinite looping parallel
    return None

label unparalleledTownEV091Base:
    $ tint_screen((68, -34, -34, 0), 60, True)
    return False

label TownEV091Base:
    call ParallelAnimTintScreen(0, rgba=[68,-34,-34,0], interval=0) from _call_townev091base_ParallelTintScreen
    $ resolve_scene()
    return False

label TownEV091(play_event = True, trigger = None): # parallel
    if is_erased("TownEV091"):
        return None
    elif trigger == "parallel" and switch("second_river"):
        call PlayEvent(play_event, "TownEV091Base", "TownEV091") from _call_TownEV091_PlayEvent
        return (0, "", "TownEV091")
    return None

label TownIShouldGoToTheInnJohannIsWaitingForMeBase:
    "I should go to the inn, johan is waiting for me"
    call Movement("TownEV092", "player", ["TURN_U","U"]) from _call_TownEV092_Movement
    $ resolve_scene()
    return False

label TownIShouldGoToTheInnJohannIsWaitingForMe(play_event = True, trigger = None): # event
    if is_erased("TownIShouldGoToTheInnJohannIsWaitingForMe"):
        return None
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "TownIShouldGoToTheInnJohannIsWaitingForMeBase", "TownIShouldGoToTheInnJohannIsWaitingForMe") from _call_TownIShouldGoToTheInnJohannIsWaitingForMe_PlayEvent
        return (0, "", "TownIShouldGoToTheInnJohannIsWaitingForMe")
    return None

label TownIShouldGoToTheInnJohannIsWaitingForMe_v2Base:
    "I should go to the inn, johan is waiting for me"
    call Movement("TownEV093", "player", ["TURN_U","U"]) from _call_TownEV093_Movement
    $ resolve_scene()
    return False

label TownIShouldGoToTheInnJohannIsWaitingForMe_v2(play_event = True, trigger = None): # event
    if is_erased("TownIShouldGoToTheInnJohannIsWaitingForMe_v2"):
        return None
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "TownIShouldGoToTheInnJohannIsWaitingForMe_v2Base", "TownIShouldGoToTheInnJohannIsWaitingForMe_v2") from _call_TownIShouldGoToTheInnJohannIsWaitingForMe_v2_PlayEvent
        return (0, "", "TownIShouldGoToTheInnJohannIsWaitingForMe_v2")
    return None

label TownIShouldGoToTheInnJohannIsWaitingForMe_v3Base:
    "I should go to the inn, johan is waiting for me"
    call Movement("TownEV094", "player", ["TURN_U","U"]) from _call_TownEV094_Movement
    $ resolve_scene()
    return False

label TownIShouldGoToTheInnJohannIsWaitingForMe_v3(play_event = True, trigger = None): # event
    if is_erased("TownIShouldGoToTheInnJohannIsWaitingForMe_v3"):
        return None
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "TownIShouldGoToTheInnJohannIsWaitingForMe_v3Base", "TownIShouldGoToTheInnJohannIsWaitingForMe_v3") from _call_TownIShouldGoToTheInnJohannIsWaitingForMe_v3_PlayEvent
        return (0, "", "TownIShouldGoToTheInnJohannIsWaitingForMe_v3")
    return None

label TownIShouldGoToTheInnJohannIsWaitingForMe_v4Base:
    "I should go to the inn, johan is waiting for me"
    call Movement("TownEV095", "player", ["TURN_U","U"]) from _call_TownEV095_Movement
    $ resolve_scene()
    return False

label TownIShouldGoToTheInnJohannIsWaitingForMe_v4(play_event = True, trigger = None): # event
    if is_erased("TownIShouldGoToTheInnJohannIsWaitingForMe_v4"):
        return None
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "TownIShouldGoToTheInnJohannIsWaitingForMe_v4Base", "TownIShouldGoToTheInnJohannIsWaitingForMe_v4") from _call_TownIShouldGoToTheInnJohannIsWaitingForMe_v4_PlayEvent
        return (0, "", "TownIShouldGoToTheInnJohannIsWaitingForMe_v4")
    return None

label TownIShouldGoToTheInnJohannIsWaitingForMe_v5Base:
    "I should go to the inn, johan is waiting for me"
    call Movement("TownEV096", "player", ["TURN_U","U"]) from _call_TownEV096_Movement
    $ resolve_scene()
    return False

label TownIShouldGoToTheInnJohannIsWaitingForMe_v5(play_event = True, trigger = None): # event
    if is_erased("TownIShouldGoToTheInnJohannIsWaitingForMe_v5"):
        return None
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "TownIShouldGoToTheInnJohannIsWaitingForMe_v5Base", "TownIShouldGoToTheInnJohannIsWaitingForMe_v5") from _call_TownIShouldGoToTheInnJohannIsWaitingForMe_v5_PlayEvent
        return (0, "", "TownIShouldGoToTheInnJohannIsWaitingForMe_v5")
    return None

label TownIShouldGoToTheInnJohannIsWaitingForMe_v6Base:
    "I should go to the inn, johan is waiting for me"
    call Movement("TownEV097", "player", ["TURN_U","U"]) from _call_TownEV097_Movement
    $ resolve_scene()
    return False

label TownIShouldGoToTheInnJohannIsWaitingForMe_v6(play_event = True, trigger = None): # event
    if is_erased("TownIShouldGoToTheInnJohannIsWaitingForMe_v6"):
        return None
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "TownIShouldGoToTheInnJohannIsWaitingForMe_v6Base", "TownIShouldGoToTheInnJohannIsWaitingForMe_v6") from _call_TownIShouldGoToTheInnJohannIsWaitingForMe_v6_PlayEvent
        return (0, "", "TownIShouldGoToTheInnJohannIsWaitingForMe_v6")
    return None

label TownIShouldGoToTheInnJohannIsWaitingForMe_v7Base:
    "I should go to the inn, johan is waiting for me"
    call Movement("TownEV098", "player", ["TURN_U","U"]) from _call_TownEV098_Movement
    $ resolve_scene()
    return False

label TownIShouldGoToTheInnJohannIsWaitingForMe_v7(play_event = True, trigger = None): # event
    if is_erased("TownIShouldGoToTheInnJohannIsWaitingForMe_v7"):
        return None
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "TownIShouldGoToTheInnJohannIsWaitingForMe_v7Base", "TownIShouldGoToTheInnJohannIsWaitingForMe_v7") from _call_TownIShouldGoToTheInnJohannIsWaitingForMe_v7_PlayEvent
        return (0, "", "TownIShouldGoToTheInnJohannIsWaitingForMe_v7")
    return None

label TownIShouldGoToTheInnJohannIsWaitingForMe_v8Base:
    "I should go to the inn, johan is waiting for me"
    call Movement("TownEV099", "player", ["TURN_U","U"]) from _call_TownEV099_Movement
    $ resolve_scene()
    return False

label TownIShouldGoToTheInnJohannIsWaitingForMe_v8(play_event = True, trigger = None): # event
    if is_erased("TownIShouldGoToTheInnJohannIsWaitingForMe_v8"):
        return None
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "TownIShouldGoToTheInnJohannIsWaitingForMe_v8Base", "TownIShouldGoToTheInnJohannIsWaitingForMe_v8") from _call_TownIShouldGoToTheInnJohannIsWaitingForMe_v8_PlayEvent
        return (0, "", "TownIShouldGoToTheInnJohannIsWaitingForMe_v8")
    return None

label TownIShouldGoToTheInnJohannIsWaitingForMe_v9Base:
    "I should go to the inn, johan is waiting for me"
    call Movement("TownEV100", "player", ["TURN_U","U"]) from _call_TownEV100_Movement
    $ resolve_scene()
    return False

label TownIShouldGoToTheInnJohannIsWaitingForMe_v9(play_event = True, trigger = None): # event
    if is_erased("TownIShouldGoToTheInnJohannIsWaitingForMe_v9"):
        return None
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "TownIShouldGoToTheInnJohannIsWaitingForMe_v9Base", "TownIShouldGoToTheInnJohannIsWaitingForMe_v9") from _call_TownIShouldGoToTheInnJohannIsWaitingForMe_v9_PlayEvent
        return (0, "", "TownIShouldGoToTheInnJohannIsWaitingForMe_v9")
    return None

label TownIShouldGoToTheInnJohannIsWaitingForMe_v10Base:
    "I should go to the inn, johan is waiting for me"
    call Movement("TownEV101", "player", ["TURN_R","R"]) from _call_TownEV101_Movement
    $ resolve_scene()
    return False

label TownIShouldGoToTheInnJohannIsWaitingForMe_v10(play_event = True, trigger = None): # event
    if is_erased("TownIShouldGoToTheInnJohannIsWaitingForMe_v10"):
        return None
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "TownIShouldGoToTheInnJohannIsWaitingForMe_v10Base", "TownIShouldGoToTheInnJohannIsWaitingForMe_v10") from _call_TownIShouldGoToTheInnJohannIsWaitingForMe_v10_PlayEvent
        return (0, "", "TownIShouldGoToTheInnJohannIsWaitingForMe_v10")
    return None

label TownIShouldGoToTheInnJohannIsWaitingForMe_v11Base:
    "I should go to the inn, johan is waiting for me"
    call Movement("TownEV102", "player", ["TURN_R","R"]) from _call_TownEV102_Movement
    $ resolve_scene()
    return False

label TownIShouldGoToTheInnJohannIsWaitingForMe_v11(play_event = True, trigger = None): # event
    if is_erased("TownIShouldGoToTheInnJohannIsWaitingForMe_v11"):
        return None
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "TownIShouldGoToTheInnJohannIsWaitingForMe_v11Base", "TownIShouldGoToTheInnJohannIsWaitingForMe_v11") from _call_TownIShouldGoToTheInnJohannIsWaitingForMe_v11_PlayEvent
        return (0, "", "TownIShouldGoToTheInnJohannIsWaitingForMe_v11")
    return None

label TownIShouldGoToTheInnJohannIsWaitingForMe_v12Base:
    "I should go to the inn, johan is waiting for me"
    call Movement("TownEV103", "player", ["TURN_R","R"]) from _call_TownEV103_Movement
    $ resolve_scene()
    return False

label TownIShouldGoToTheInnJohannIsWaitingForMe_v12(play_event = True, trigger = None): # event
    if is_erased("TownIShouldGoToTheInnJohannIsWaitingForMe_v12"):
        return None
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "TownIShouldGoToTheInnJohannIsWaitingForMe_v12Base", "TownIShouldGoToTheInnJohannIsWaitingForMe_v12") from _call_TownIShouldGoToTheInnJohannIsWaitingForMe_v12_PlayEvent
        return (0, "", "TownIShouldGoToTheInnJohannIsWaitingForMe_v12")
    return None

label TownIShouldGoToTheInnJohannIsWaitingForMe_v13Base:
    "I should go to the inn, johan is waiting for me"
    call Movement("TownEV104", "player", ["TURN_U","U"]) from _call_TownEV104_Movement
    $ resolve_scene()
    return False

label TownIShouldGoToTheInnJohannIsWaitingForMe_v13(play_event = True, trigger = None): # event
    if is_erased("TownIShouldGoToTheInnJohannIsWaitingForMe_v13"):
        return None
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "TownIShouldGoToTheInnJohannIsWaitingForMe_v13Base", "TownIShouldGoToTheInnJohannIsWaitingForMe_v13") from _call_TownIShouldGoToTheInnJohannIsWaitingForMe_v13_PlayEvent
        return (0, "", "TownIShouldGoToTheInnJohannIsWaitingForMe_v13")
    return None

label TownIShouldGoToTheInnJohannIsWaitingForMe_v14Base:
    "I should go to the inn, johan is waiting for me"
    call Movement("TownEV105", "player", ["TURN_U","U"]) from _call_TownEV105_Movement
    $ resolve_scene()
    return False

label TownIShouldGoToTheInnJohannIsWaitingForMe_v14(play_event = True, trigger = None): # event
    if is_erased("TownIShouldGoToTheInnJohannIsWaitingForMe_v14"):
        return None
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "TownIShouldGoToTheInnJohannIsWaitingForMe_v14Base", "TownIShouldGoToTheInnJohannIsWaitingForMe_v14") from _call_TownIShouldGoToTheInnJohannIsWaitingForMe_v14_PlayEvent
        return (0, "", "TownIShouldGoToTheInnJohannIsWaitingForMe_v14")
    return None

label TownIShouldGoToTheInnJohannIsWaitingForMe_v15Base:
    "I should go to the inn, johan is waiting for me"
    call Movement("TownEV106", "player", ["TURN_R","R"]) from _call_TownEV106_Movement
    $ resolve_scene()
    return False

label TownIShouldGoToTheInnJohannIsWaitingForMe_v15(play_event = True, trigger = None): # event
    if is_erased("TownIShouldGoToTheInnJohannIsWaitingForMe_v15"):
        return None
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "TownIShouldGoToTheInnJohannIsWaitingForMe_v15Base", "TownIShouldGoToTheInnJohannIsWaitingForMe_v15") from _call_TownIShouldGoToTheInnJohannIsWaitingForMe_v15_PlayEvent
        return (0, "", "TownIShouldGoToTheInnJohannIsWaitingForMe_v15")
    return None

label TownTABLON_0(menu_choice = None):
    "What to do today:"
    call GetChoice([_("Bar 1"), _("Market"), _("Villagers"), _("River 1")], value=menu_choice, called_from="TownTABLON_0") from _call_TownTABLON_0_GetChoice
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

label TownTABLON_1(menu_choice = None):
    "What to do today:"
    call GetChoice([_("Photographer 1"), _("Hotsprings"), _("Photographer 2"), _("Bar 2"), _("River 2")], value=menu_choice, called_from="TownTABLON_1") from _call_TownTABLON_1_GetChoice
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

label TownTABLON_2(menu_choice = None):
    "What to do today:"
    call GetChoice([_("Photographer 3"), _("Worker's quest"), _("Dresser"), _("The dream"), _("Police station"), _("Night Party")], value=menu_choice, called_from="TownTABLON_2") from _call_TownTABLON_2_GetChoice
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

label TownTABLON(play_event = True, trigger = None): # event
    if is_erased("TownTABLON"):
        return None
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "TownTABLON_2", "TownTABLON") from _call_TownTABLON_2_PlayEvent
        return (1, "", "TownTABLON_2")
    elif trigger == "event" and switch("finished_river_scene"):
        call PlayEvent(play_event, "TownTABLON_1", "TownTABLON") from _call_TownTABLON_1_PlayEvent
        return (1, "", "TownTABLON_1")
    elif trigger == "event":
        call PlayEvent(play_event, "TownTABLON_0", "TownTABLON") from _call_TownTABLON_0_PlayEvent
        return (1, "", "TownTABLON_0")
    return None

