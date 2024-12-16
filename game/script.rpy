label start:
    stop music fadeout 1.0
    scene black
    call PlayEntireGame from _call_PlayEntireGame 
    return

label PlayEntireGame:

label intro:
    call PlayIntro from _call_PlayIntro
label day1:
    call PlayDay1 from _call_PlayDay1
label day2:
    call PlayDay2 from _call_PlayDay2

    show text "end of content"
    pause
    hide text
    "play again?"
    menu:
        "Intro":
            jump intro
        "Day 1":
            jump day1
        "Day 2":
            jump day2
        "Exit":
            pass
    return

label PlayIntro:
    # apartment intro
    $ player_location = "Intro"
    call IntroOhHelloThere from _call_IntroOhHelloThere
    call ApartmentNPCMUJER_0 from _call_ApartmentNPCMUJER_0
    call ApartmentORDENADOR from _call_ApartmentORDENADOR
    # town intro
    $ player_location = "Town"
    call TownEntranceparadabus_0 from _call_TownEntranceparadabus_0
    call TownNPCCop_0 from _call_TownNPCCop_0
    call Innposadero_0 from _call_Innposadero_0
    call InnRoomsDEJANDOlasmaletas_0 from _call_InnRoomsDEJANDOlasmaletas_0
    scene black
    call Innposadero_1 from _call_Innposadero_1
    return

label PlayDay1:
    # bar 1
    $ player_location = "Bar"
    call BarWetTShirt_0 from _call_BarWetTShirt_0
    scene black
    # merchant
    $ player_location = "Town"
    call TownMerchant_0 from _call_TownMerchant_0
    call TownSkirtLift_0 from _call_TownSkirtLift_0
    # villagers
    call Towneventolemetenmanobarrio_0 from _call_Towneventolemetenmanobarrio_0
    # river
    $ player_location = "River"
    label RiverDay1:
        call Riverentradario_0 from _call_Riverentradario_0
        if player_location != "River":
            jump RiverDay1
    call RiverNPCEventMan from _call_RiverNPCEventMan
    call Townfinaldelprimerdia_0 from _call_Townfinaldelprimerdia_0
    return

label PlayDay2:
    # photographer 1
    $ player_location = "Town"
    label PhotographerDay2:
        call Towneventofotografiaintro_0 from _call_Towneventofotografiaintro_0
        if player_location != "PhotographersHouse":
            jump PhotographerDay2
    call PhotographersHousesesionfotografica1 from _call_PhotographersHousesesionfotografica1
    # hotsprings
    $ player_location = "Reception"
    call Receptioneventohotsprings_0 from _call_Receptioneventohotsprings_0
    call HotSpringshotspringseventopart2 from _call_HotSpringshotspringseventopart2
    # photographer 2
    $ player_location = "Town"
    call Townfotografo_1 from _call_Townfotografo_1
    call ClothingStoreHeyThere_1 from _call_ClothingStoreHeyThere_1
    call Townfotografo_3 from _call_Townfotografo_3
    call Photoshoot2Sesionfotografica2 from _call_Photoshoot2Sesionfotografica2
    # bar 2
    $ player_location = "Bar"
    label BarDay2:
        call BarBJGame_0 from _call_BarBJGame_0
        if player_location != "Town":
            jump BarDay2
    # river 2
    return
