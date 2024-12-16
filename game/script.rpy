label start:
    stop music fadeout 1.0
    scene black
    call PlayEntireGame from _call_PlayEntireGame 
    return

label PlayEntireGame:
    ## Intro
    
    # apartment intro
    call IntroHelloMyNameIsJohan from _call_IntroHelloMyNameIsJohan
    call ApartmentNPCMUJER_0 from _call_ApartmentNPCMUJER_0
    call ApartmentORDENADOR from _call_ApartmentORDENADOR
    # town intro
    call TownEntranceparadabus_0 from _call_TownEntranceparadabus_0
    call TownNPCCop_0 from _call_TownNPCCop_0
    call Innposadero_0 from _call_Innposadero_0
    call InnRoomsDEJANDOlasmaletas_0 from _call_InnRoomsDEJANDOlasmaletas_0
    scene black
    call Innposadero_1 from _call_Innposadero_1
    
    ## Day 1
    call BarWetTShirt_0 from _call_BarWetTShirt_0
    scene black
    call TownMerchant_0 from _call_TownMerchant_0
    call TownSkirtLift_0 from _call_TownSkirtLift_0
    call Towneventolemetenmanobarrio_0 from _call_Towneventolemetenmanobarrio_0
label RiverDay1:
    call Riverentradario_0 from _call_Riverentradario_0
    if not switch("separated_in_the_river"):
        jump RiverDay1
    call RiverNPCEventMan from _call_RiverNPCEventMan
    return