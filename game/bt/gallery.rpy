label ClothesChoice:
    menu:
        "Leyna wore festival clothes":
            $ festival_clothes = 1
            pass
        "Leyna wore her normal clothes":
            $ festival_clothes = 2
            pass
    return

label InfusionChoice:
    menu:
        "Leyna drank the infusion":
            $ set_switch("infusion", True)
            pass
        "Leyna did not drink the infusion":
            $ set_switch("infusion", False)
            pass
    return

label FruitChoice:
    menu:
        "Leyna ate the fruit":
            $ set_switch("ate_the_fruit", True)
            pass
        "Leyna did not eat the fruit":
            $ set_switch("ate_the_fruit", False)
            pass
    return

label CorruptionChoice(include_high = True):
    menu:
        "Leyna has high corruption" if include_high:
            $ set_switch("corruption_high", True)
            pass
        "Leyna has average corruption":
            $ set_switch("corruption_average", True)
            pass
        "Leyna has low corruption":
            $ set_switch("corruption_low", True)
            pass
    return

label JohanLeynaSexChoice:
    menu:
        "Johan felt the pressure having sex with Leyna":
            $ johan_leyna_sex = 1
            pass
        "Johan felt comfortable having sex with Leyna":
            $ johan_leyna_sex = 2
            pass
    return

label PlayGallery(label_name):
    $ reset_state()
    if renpy.has_label(label_name + "Gallery"):
        $ renpy.call(label_name + "Gallery")
    else:
        $ renpy.call(label_name)
    return

label adolescentesGallery:
    call TownNightStart from _call_gallery_adolescentes_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call TownNightEhhhYouuuuuuuuu_2(_("Yes")) from _call_gallery_adolescentes
    return

label analcomidaGallery:
    call FestivalStart from _call_gallery_analcomida_start
    call CorruptionChoice(include_high=False) from _call_gallery_analcomida_CorruptionChoice
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call FestivalButtPlugEvent_1 from _call_gallery_analcomida
    return

label apuestaGallery:
    call Bar2Start from _call_gallery_apuesta_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call Bar2WowGuysWhatACoincidence_0 from _call_gallery_apuesta
    return

label barGallery:
    call BarStart from _call_gallery_bar_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call BarBJGame_0(_("Yes")) from _call_gallery_bar
    return

label barfinalGallery:
    call Bar2Start from _call_gallery_barfinal_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call Bar2LeynawhatAreYouDoingHereIThoughtYouWereLeavingTownThisMorning_0 from _call_gallery_barfinal
    return

label blackmailGallery:
    call TownFestivalNightStart from _call_gallery_blackmail_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    $ set_switch("corruption_average", True)
    call TownFestivalNighteventoblackmail_0 from _call_gallery_blackmail
    return

label callefinalGallery:
    call TownCenterStart from _call_gallery_callefinal_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call Town2HeySweetieDoYouWantToHaveAGoodTime_0 from _call_gallery_callefinal
    return

label calta1Gallery:
    call ApartmentEndingStart from _call_gallery_calta1_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    $ johan_leyna_sex = 2
    call ApartmentEndingCbajaending2Base from _call_gallery_calta1
    return

label calta2Gallery:
    call ApartmentEndingStart from _call_gallery_calta2_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    $ johan_leyna_sex = 1
    call ApartmentEndingCbajaending2Base from _call_gallery_calta2
    return

label cambiandoseGallery:
    call Town2Start from _call_gallery_cambiandose_start
    call CorruptionChoice(include_high=False) from _call_gallery_cambiandose_CorruptionChoice
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call Town2JohanIWasLookingForYou_1 from _call_gallery_cambiandose
    return

label carcelGallery:
    call PoliceStationStart from _call_gallery_carcel_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call PoliceStationeventocomisaria_0 from _call_gallery_carcel
    return

label cbajacontGallery:
    call ApartmentGroundFloorStart from _call_gallery_cbajacont_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call ApartmentGroundFloorCbajaending2Base from _call_gallery_cbajacont
    return

label cmedia2Gallery:
    call TownEntranceStart from _call_gallery_cmedia2_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    $ johan_leyna_sex = 1
    call TownEntranceJohanmedia_1(_("I will think about it")) from _call_gallery_cmedia2
    return

label cmedia3Gallery:
    call TownEntranceStart from _call_gallery_cmedia3_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    $ johan_leyna_sex = 2
    call TownEntranceJohanmedia_1(_("I will think about it")) from _call_gallery_cmedia3
    return

label desayunoGallery:
    call Bar2Start from _call_gallery_desayuno_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call CorruptionChoice from _call_gallery_desayuno_CorruptionChoice
    call Bar2ToBar2_0 from _call_gallery_desayuno
    return

label dildoGallery:
    call InnRoomBG from _call_gallery_dildo_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call InnRoomsescenadildo_0 from _call_gallery_dildo
    return

label drunkGallery:
    call PathStart from _call_gallery_drunk_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    $ set_switch("corruption_high", True)
    call PathWowItLooksLikeTheHotspringsHaveReopened_0 from _call_gallery_drunk
    return

label dueloGallery:
    call FestivalFinaleStart from _call_gallery_duelo_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call CorruptionChoice from _call_gallery_duelo_CorruptionChoice
    call FestivalFinaleHeyWhatsGoingOnHere_0 from _call_gallery_duelo
    return

label escena_camisa_mojadaGallery:
    call BarStart from _call_gallery_escena_camisa_mojada_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call BarWetTShirt_0 from _call_gallery_escena_camisa_mojada
    return

label festivalfotosGallery:
    call FestivalStart from _call_gallery_festivalfotos_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call FestivalPhotoSession_0 from _call_gallery_festivalfotos
    return

label festivalnocheGallery:
    call FestivalNightStart from _call_gallery_festivalnoche_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call FestivalNightLeynaropaBase from _call_gallery_festivalnoche
    return

label flashGallery:
    call Town2Start from _call_gallery_flash_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call CorruptionChoice from _call_gallery_flash_CorruptionChoice    
    call ClothesChoice from _call_gallery_flash_ClothesChoice    
    call Town2Flashback_0 from _call_gallery_flash
    return

label flashbackGallery:
    call FestivalStart from _call_gallery_flashback_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call InfusionChoice from _call_gallery_flash_InfusionChoice
    call PathLeynaWorkTrigger_0 from _call_gallery_flashback
    return

label fotoeroticaGallery:
    call Town2Start from _call_gallery_fotoerotica_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call Town2fotografo_10(_("Do it")) from _call_gallery_fotoerotica
    return

label fotofestivalGallery:
    call FestivalFinaleStart from _call_gallery_fotofestival_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call CorruptionChoice from _call_gallery_fotofestival_CorruptionChoice
    call FestivalFinaleevent_15_0 from _call_gallery_fotofestival
    return

label fotografo1Gallery:
    call PhotographersHouseStart from _call_gallery_fotografo1_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call PhotographersHousesesionfotografica1Base from _call_gallery_fotografo1
    return

label fotografo2Gallery:
    call Photoshoot2Start from _call_gallery_fotografo2_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call Photoshoot2Sesionfotografica2Base from _call_gallery_fotografo2
    return

label hotspringsjuntosGallery:
    call HotSpringsWithJohanStart from _call_gallery_hotspringsjuntos_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call InfusionChoice from _call_gallery_hotspringsjuntos_InfusionChoice
    call HotSpringsWithJohanhotspringjuntoscontBase from _call_gallery_hotspringsjuntos
    return

label johanfollarGallery:
    call Town2Start from _call_gallery_johanfollar_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call Town2LeynaJohanSex_0 from _call_gallery_johanfollar
    return

label johanxalexaGallery:
    call InnStart from _call_gallery_johanxalexa_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call JohanLeynaSexChoice from _call_gallery_johanxalexa_JohanLeynaSexChoice
    call InneventoJohanyalexa_0 from _call_gallery_johanxalexa
    return

label levantamiento_de_faldaGallery:
    call TownCenterWestStart from _call_gallery_levantamiento_de_falda_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call TownSkirtLift_0 from _call_gallery_levantamiento_de_falda
    return

label mamadaGallery:
    call TownSouthEastStart from _call_gallery_mamada_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call InfusionChoice from _call_gallery_mamada_InfusionChoice
    call Town2chicoencontrado_0(_("Help him")) from _call_gallery_mamada
    return

label manoseoGallery:
    call TownSouthEastStart from _call_gallery_manoseo_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call Towneventolemetenmanobarrio_0 from _call_gallery_manoseo
    return

label masageGallery:
    call MassageParlorStart from _call_gallery_masage_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call FruitChoice from _call_gallery_masage_FruitChoice
    call MassageParlorICantWaitToHaveARelaxingMassage_0 from _call_gallery_masage
    return

label mascaraGallery:
    call Town2Start from _call_gallery_mascara_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call Town2fotografo_4(_("Do the session")) from _call_gallery_mascara
    return

label mini1Gallery:
    call FestivalFinaleStart from _call_gallery_mini1_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call FestivalFinaleHeyLeynaGoodToSeeYouHereBase from _call_gallery_mini1
    return

label mini2Gallery:
    call FestivalFinaleStart from _call_gallery_mini2_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call FestivalFinaleHeyGoodToSeeYouLeynaEspeciallyInThisSituationHeheheheheBase from _call_gallery_mini2
    return

label mini4Gallery:
    call FestivalFinaleStart from _call_gallery_mini4_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call FestivalFinaleYoSlapBase from _call_gallery_mini4
    return

label mini5Gallery:
    call FestivalFinaleStart from _call_gallery_mini5_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call FestivalFinaleOhLeynaIWasHopingToMeetYouIHaveSomethingToGiveYouBase from _call_gallery_mini5
    return

label noblackmailGallery:
    call TownFestivalNightStart from _call_gallery_noblackmail_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    $ set_switch("corruption_low", True)
    call TownFestivalNighteventoblackmail_0 from _call_gallery_noblackmail
    return

label onsenGallery:
    call HotSpringsStart from _call_gallery_onsen_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call HotSpringshotspringseventopart2Base from _call_gallery_onsen
    return

label orgiaGallery:
    call CasinoFinaleStart from _call_gallery_orgia_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call CorruptionChoice from _call_gallery_orgia_CorruptionChoice
    call CasinoFinaleLooksLikeTheLastEventIsGoingToBeHereBase from _call_gallery_orgia
    return

label photohotGallery:
    call Town2Start from _call_gallery_photohot_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call Town2fotografo_13(_("Okay, let's do it")) from _call_gallery_photohot
    return

label pokerGallery:
    call Bar2Start from _call_gallery_poker_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call Bar2LeynaWeWereLookingForYou_0 from _call_gallery_poker
    return

label probadorGallery:
    call ClothingStoreStart from _call_gallery_probador_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call ClothingStoreIShouldComeBackLaterToTryTheFestivalClothes_1 from _call_gallery_probador
    return

label publicoGallery:
    call Town2Start from _call_gallery_publico_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call Town2fotografo_1 from _call_gallery_publico
    return

label puestoGallery:
    call FestivalStart from _call_gallery_puesto_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call FruitChoice from _call_gallery_puesto_FruitChoice
    call FestivalFoodStand_0 from _call_gallery_puesto
    return

label revengeGallery:
    call GladeStart from _call_gallery_revenge_start
    $ set_transparency_backgrounds(["bg_glade_night"])
    $ set_map_backgrounds(["map_glade_night"])
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call GladeImSureHeWontFindMeHereThisAreaIsALittleScaryAtNightThough_0 from _call_gallery_revenge
    return

label rioGallery:
    call RiverStart from _call_gallery_rio_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call RiverNPCEventManBase from _call_gallery_rio
    return

label rio2Gallery:
    call River2Start from _call_gallery_rio2_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call River2ThisPlaceIsBeautifulBase from _call_gallery_rio2
    return

label rioleynaGallery:
    call TownFestivalNightStart from _call_gallery_rioleyna_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike_0 from _call_gallery_rioleyna
    return

label riosexoGallery:
    call Town2Start from _call_gallery_riosexo_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call JohanLeynaSexChoice from _call_gallery_riosexo_JohanLeynaSexChoice
    call Town2ToRiverEvent_v2_1(_("Enter the river")) from _call_gallery_riosexo
    return

label ritualGallery:
    call FestivalStart from _call_gallery_ritual_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call Festivaliniciacionadolescencia_0 from _call_gallery_ritual
    return

label sue_oGallery:
    call InnRoomsStart from _call_gallery_sue_o_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    $ set_switch("johan_silent", True)
    call InnRoomssueojohan_0 from _call_gallery_sue_o
    return

label sue_oleynaGallery:
    call InnNightStart from _call_gallery_sue_oleyna_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call FruitChoice from _call_gallery_sue_oleyna_FruitChoice
    $ set_switch("massage_sex", switch("ate_the_fruit"))
    $ set_switch("massage_masturbation", not switch("ate_the_fruit"))
    call InnNightSleepBase from _call_gallery_sue_oleyna
    return

label suerteGallery:
    call CasinoStart from _call_gallery_suerte_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call FruitChoice from _call_gallery_suerte_FruitChoice
    call CasinohombredelasuerteBase from _call_gallery_suerte
    return

label trabajoGallery:
    call ReceptionStart from _call_gallery_trabajo_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call ReceptionDamn_0 from _call_gallery_trabajo
    return

label trabajobar2Gallery:
    call Bar2Start from _call_gallery_trabajobar2_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call Bar2barman_5(_("I will work like this ")) from _call_gallery_trabajobar2
    return

label trabajobarGallery:
    call Bar2Start from _call_gallery_trabajobar_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    $ bet_together = 2
    $ set_switch("corruption_average", True)
    call Bar2barman_3 from _call_gallery_trabajobar
    return

label vestuarioGallery:
    call PathStart from _call_gallery_vestuario_start
    $ switch_to_next_backgrounds(no_fades=True)
    $ resolve_scene("dirty")
    call Pathnpcentradafestivalcamino_4 from _call_gallery_vestuario
    return
