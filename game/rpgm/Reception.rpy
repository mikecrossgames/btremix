label ReceptionBG:
    $ set_transparency_backgrounds(["bg_reception"])
    $ set_map_backgrounds(["map_reception"])
    return

label ReceptionStart:
    call ReceptionBG from _call_ReceptionBG
    stop music
    stop bgs
    return

label ReceptionEnd:
    return

label Receptionrecepcion_1:
    Receptionist "Sorry, today we are cleaning the area. Come back tomorrow"
    return False

label Receptionrecepcion_2:
    Receptionist "Hi honey, how can I help you?"
    $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
    $ resolve_scene()
    Leyna "Hi! See, the people in town told me that you need a receptionist for these days and I'm looking a part-time job.."
    Receptionist "Ahhh! Thank goodness you came. I'm very busy with the festival and I would not like to have to close these days, with so many customers"
    Receptionist "I'm looking for someone to cover for me while during the event. You would only have to attend to the people and have the place clean, prepare towels... well"
    "There are several things I would have to teach you first, if you are interested, of course"
    $ erase_picture(1)
    $ show_transparent(2, "plano_mujer_sonrisa", width=1600, height=900)
    $ resolve_scene()
    Leyna "Of course!"
    Receptionist "You see, people come here to relax. It always smells good and the atmosphere is warm, I put in the water some plants that grow near the festival"
    Receptionist "You know, the flowers of the fruit that is usually taken...  at the festival hehehe.."
    $ erase_picture(2)
    $ resolve_scene()
    Leyna "I see..."
    if switch("ate_the_fruit"):
        $ show_transparent(3, "expresion_gota")
        $ resolve_scene()
        Leyna "(damn fruit)..."
        $ erase_picture(3)
    $ resolve_scene()
    Receptionist "I've run out and would need you to get a few to show you how I prepare hotsprings for people"
    Receptionist "Come see me when you have the flowers, you can get them in a field that is close to the festival"
    Leyna "That's done, I'll be right back"
    $ leyna_work = 4
    return False

label Receptionrecepcion_3:
    Receptionist "Do you have the flowers?"
    return False

label Receptionrecepcion_4:
    Receptionist "You already have the flowers?"
    Leyna "Yes, here they are!"
    call PlaySound("sound", "audio/Recovery.ogg", volume=0.9, no_loop=True) from _call_Receptionrecepcion_4_PlaySound
    $ set_item("flowers", False)
    Receptionist "Well, then let's see what the work consists of"
    $ fade_out()
    call TransferPlayer("HotSpringsBathroom", "Receptionrecepcion_4", 3, 3, direction=4) from _call_Receptionrecepcion_4_TransferPlayer
    $ fade_in()
    $ resolve_scene()
    return False

label Receptionrecepcion_5:
    Receptionist "See you tomorrow honey"
    return False

label Receptionrecepcion(play_event = True, trigger = None): # event
    if is_erased("Receptionrecepcion"):
        return None
    elif trigger == "event" and leyna_work >= 10:
        call PlayEvent(play_event, "Receptionrecepcion_5", "Receptionrecepcion") from _call_Receptionrecepcion_5_PlayEvent
        return (1, "", "Receptionrecepcion_5")
    elif trigger == "event" and leyna_work >= 8:
        call PlayEvent(play_event, "Receptionrecepcion_4", "Receptionrecepcion") from _call_Receptionrecepcion_4_PlayEvent
        return (1, "", "Receptionrecepcion_4")
    elif trigger == "event" and leyna_work >= 4:
        call PlayEvent(play_event, "Receptionrecepcion_3", "Receptionrecepcion") from _call_Receptionrecepcion_3_PlayEvent
        return (1, "", "Receptionrecepcion_3")
    elif trigger == "event" and leyna_work >= 3:
        call PlayEvent(play_event, "Receptionrecepcion_2", "Receptionrecepcion") from _call_Receptionrecepcion_2_PlayEvent
        return (1, "", "Receptionrecepcion_2")
    elif trigger == "event" and switch("third_day"):
        call PlayEvent(play_event, "Receptionrecepcion_1", "Receptionrecepcion") from _call_Receptionrecepcion_1_PlayEvent
        return (1, "", "Receptionrecepcion_1")
    return None

label ReceptionToHotSpringsExteriorBase:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_ReceptionEV002_PlaySound
    call TransferPlayer("HotSpringsExterior", "ReceptionEV002", 11, 8, direction=2) from _call_ReceptionEV002_TransferPlayer
    $ resolve_scene()
    return False

label ReceptionToHotSpringsExterior(play_event = True, trigger = None): # event
    if is_erased("ReceptionToHotSpringsExterior"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "ReceptionToHotSpringsExteriorBase", "ReceptionToHotSpringsExterior") from _call_ReceptionToHotSpringsExterior_PlayEvent
        return (0, "", "ReceptionToHotSpringsExterior")
    return None

label ReceptionToHotSpringsExterior_v2Base:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_ReceptionEV003_PlaySound
    call TransferPlayer("HotSpringsExterior", "ReceptionEV003", 12, 8, direction=2) from _call_ReceptionEV003_TransferPlayer
    $ resolve_scene()
    return False

label ReceptionToHotSpringsExterior_v2(play_event = True, trigger = None): # event
    if is_erased("ReceptionToHotSpringsExterior_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "ReceptionToHotSpringsExterior_v2Base", "ReceptionToHotSpringsExterior_v2") from _call_ReceptionToHotSpringsExterior_v2_PlayEvent
        return (0, "", "ReceptionToHotSpringsExterior_v2")
    return None

label Receptioneventohotsprings_0:
    call Movement("Receptioneventohotsprings_0", "player", ["U"]) from _call_Receptioneventohotsprings_0_Movement
    $ show_transparent(1, "plano_mujer_sonrisa", width=1600, height=900)
    $ resolve_scene()
    Leyna "Hello,  I've been told that the hot springs are already open"
    Receptionist "Yes, we were closed for renovations"
    Leyna "Great! So can I come in?"
    Receptionist "Yes, on my left you have the women's wardrobe. There you have clean towels, when you finish you can leave it in the basket and we will take care of it"
    $ erase_picture(1)
    $ show_transparent(1, "expresion_ilusion_mujer", width=1600, height=900)
    $ resolve_scene()
    Leyna "Cool, it's been years since I've come to a place like this"
    Receptionist "Enjoy!"
    $ erase_picture(1)
    call Movement("Receptioneventohotsprings_0", "player", ["R","R","R","R","R","U","U","U","U","U","U","U"]) from _call_Receptioneventohotsprings_0_Movement_1
    $ fade_out()
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_Receptioneventohotsprings_0_PlaySound
    $ resolve_scene()
    pause 0.6
    call TransferPlayer("HotSpringsBathroom", "Receptioneventohotsprings_0", 2, 3, direction=0) from _call_Receptioneventohotsprings_0_TransferPlayer
    $ fade_in()
    call Movement("Receptioneventohotsprings_0", "player", ["D","D"]) from _call_Receptioneventohotsprings_0_Movement_2
    $ resolve_scene()
    Leyna "There's nobody, I have the place for myself!"
    $ fade_out()
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_Receptioneventohotsprings_0_PlaySound_1
    pause 0.6
    call TransferPlayer("HotSpringsBathroom", "Receptioneventohotsprings_0", 12, 10, direction=8) from _call_Receptioneventohotsprings_0_TransferPlayer_1
    $ fade_in()
    $ resolve_scene()
    pause 0.6
    Leyna "Aaah... good... and the water is perfect how relaxing!"
    $ fade_out()
    call PlaySound("sound", "audio/Liquid.ogg", volume=0.9, no_loop=True) from _call_Receptioneventohotsprings_0_PlaySound_2
    pause 0.6
    $ show_picture(1, "onsen1")
    $ fade_in()
    $ resolve_scene()
    "(5 MINUTES LATER...)"
    Leyna "I'm soooo chill right now..."
    Leyna "I could fall asleep here, but I don't have to abuse either. I can get dizzy from the heat.."
    Leyna "Well... closing my eyes for a few minutes won't hurt"
    $ fade_out()
    $ erase_picture(1)
    call TransferPlayer("HotSprings", "Receptioneventohotsprings_0", 12, 10, direction=8) from _call_Receptioneventohotsprings_0_TransferPlayer_2
    $ fade_in()
    $ resolve_scene()
    return False

label Receptioneventohotsprings(play_event = True, trigger = None): # autorun
    if is_erased("Receptioneventohotsprings"):
        return None
    elif switch("hot_springs_first_visit"):
        return None
    elif trigger == "autorun" and switch("leyna_alone"):
        call PlayEvent(play_event, "Receptioneventohotsprings_0", "Receptioneventohotsprings") from _call_Receptioneventohotsprings_0_PlayEvent
        return (0, "", "Receptioneventohotsprings_0")
    return None

label ReceptionDamn_0:
    call PauseForBalloon("ReceptionEV005_0") from _call_ReceptionEV005_0_PauseForBalloon
    Leyna "Damn..."
    $ show_picture(1, "trabajo1")
    $ resolve_scene()
    Leyna "Is this serious? What a uniform... this is too provocative, she goes with normal clothes.. Why do I have to put on this kind of clothing?"
    Leyna "You can see everything ..."
    WomansVoice "Leyna? what are you doing here?"
    $ show_picture(2, "trabajo2")
    $ resolve_scene()
    Leyna "???"
    Leyna "(I can't believe she's here without her husband, well, it was to be expected)"
    $ show_picture(3, "trabajo3")
    $ resolve_scene()
    Leyna "Wow Alexa, I didn't expect to see you here... alone"
    Leyna "You know that the hotsprings are mixed, right?"
    Alexa "I know..."
    Alexa "My husband is with the friends who accompany us in the trip and I didn't want to be alone"
    $ show_picture(4, "trabajo4")
    $ resolve_scene()
    Leyna "I see... although you never stay alone for long..."
    Alexa "I like to be accompanied, what can I say... hehehe"
    $ show_picture(5, "trabajo5")
    $ resolve_scene()
    Alexa "Well... and you? What are you doing here alone?"
    Leyna "I've started working here today so I will prepare your bath, I hope you enjoy it"
    Alexa "I'm sure I will hehehe"
    $ fade_out()
    $ show_picture(6, "trabajo6")
    $ fade_in()
    $ resolve_scene()
    "A FEW MOMENTS LATER"
    Leyna "Alexa? I leave you here a few dry towe..."
    $ show_picture(7, "trabajo7")
    $ resolve_scene()
    Leyna "(what's going on here? where did these people come from?... I can't believe it, doing this in public again)"
    $ show_picture(8, "trabajo8")
    $ resolve_scene()
    Alexa "Right there, you're going to break me in half"
    Villager "What a dirty bitch"
    $ show_picture(9, "trabajo9")
    $ resolve_scene()
    Leyna "(They don't worry that somebody can see them? somebody could enter at any moment)"
    $ show_picture(10, "trabajo10")
    $ resolve_scene()
    Alexa "Fuck me, come on!"
    Villager2 "This bitch is crazy"
    Villager "I know... It's great, we have to take advantage of this unique opportunity in life, dude"
    Alexa "we don't have much time, fuck me before someone comes"
    $ show_picture(11, "trabajo11")
    $ resolve_scene()
    Leyna "(I... am I getting turned on? by this? What kind of person I' m becoming?)"
    $ show_picture(12, "trabajo12")
    call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_ReceptionEV005_0_PlaySound
    $ resolve_scene()
    Villager "Do you like it bitch?"
    Alexa "I love it! FUCK ME PLEASE! HARDER!"
    Villager2 "I'm going to cum, your ass is incredible!"
    Alexa "DON'T CUM YET! KEEP FUCKING ME PLEASE!!"
    stop bgs fadeout 1
    call PlaySound("music", "audio/Town1.ogg", volume=0.9, no_loop=False) from _call_ReceptionEV005_0_PlaySound_1
    $ show_picture(13, "trabajo13")
    $ resolve_scene()
    Leyna "(... I think anyone can't see me from here. They don't even know I'm here)"
    Leyna "(I have to get it off my chest, it will only take a second)"
    $ show_picture(14, "trabajo14")
    $ resolve_scene()
    Leyna "Ahhhh"
    Leyna "(Shit, I have to be quiet or they might discover me and that... would be a problem)"
    Leyna "(Yes, I would be in serious trouble, I could get caught and between them two...)"
    $ show_picture(15, "trabajo15")
    $ resolve_scene()
    Leyna "Hmmmmm"
    Leyna "(I would be caught between the two of them and... fuck me through every hole in my body, using me)"
    $ flash_screen([255,255,255,170], 60, True)
    Leyna "Aaah!"
    $ flash_screen([255,255,255,170], 60, True)
    Leyna "I'm... I'm ..."
    $ flash_screen([255,255,255,170], 60, True)
    Leyna "Hmmmmmaaa..."
    $ show_picture(16, "trabajo16")
    $ resolve_scene()
    Leyna "Shit, I hope the didn't notice"
    Leyna "That... was very good, but I shouldn't have done it... just thinking about it, again I'm ... I'm not being myself, I should go back"
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
    $ erase_picture(14)
    $ erase_picture(15)
    $ erase_picture(16)
    call TransferPlayer("Reception", "ReceptionEV005_0", 7, 3, direction=2) from _call_ReceptionEV005_0_TransferPlayer
    $ fade_in()
    call Movement("ReceptionEV005_0", "player", ["R","R","TURN_D"]) from _call_ReceptionEV005_0_Movement
    $ resolve_scene()
    call PauseForBalloon("ReceptionEV005_0") from _call_ReceptionEV005_0_PauseForBalloon_1
    Leyna "(Alexa... how can you do this kind of thing?... I... shouldn't have done it...)"
    call Movement("ReceptionEV005_0", "player", ["D","R","D","D","D","D","D","TURN_L"]) from _call_ReceptionEV005_0_Movement_1
    $ resolve_scene()
    call PauseForBalloon("ReceptionEV005_0") from _call_ReceptionEV005_0_PauseForBalloon_2
    Leyna "Wow, you're back from the festival already?"
    Receptionist "Yes, today there wasn't much work,you can leave if you want, there is a lot to do?"
    Leyna "Well... right now there are three clients inside... I need to clean up a little bit"
    Receptionist "Don't worry, I'll take care of it, come tomorrow at the same time"
    Leyna "Great thank you very much"
    $ fade_out()
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_ReceptionEV005_0_PlaySound_2
    call TransferPlayer("HotSpringsExterior", "ReceptionEV005_0", 11, 8, direction=2) from _call_ReceptionEV005_0_TransferPlayer_1
    $ fade_in()
    call Movement("ReceptionEV005_0", "player", ["D"]) from _call_ReceptionEV005_0_Movement_2
    $ leyna_work = 10
    call GalleryViewed("trabajo") from _call_ReceptionEV005_0_GalleryViewed
    $ resolve_scene()
    return False

label ReceptionDamn(play_event = True, trigger = None): # autorun
    if is_erased("ReceptionDamn"):
        return None
    elif leyna_work >= 10:
        return None
    elif trigger == "autorun" and leyna_work >= 9:
        call PlayEvent(play_event, "ReceptionDamn_0", "ReceptionDamn") from _call_ReceptionDamn_0_PlayEvent
        return (0, "", "ReceptionDamn_0")
    return None

label Receptionhotspringsjuntos_0:
    call Movement("Receptionhotspringsjuntos_0", "player", ["U","U"]) from _call_Receptionhotspringsjuntos_0_Movement
    $ resolve_scene()
    call PauseForBalloon("Receptionhotspringsjuntos_0") from _call_Receptionhotspringsjuntos_0_PauseForBalloon
    Receptionist "Leyna! thank goodness you are here! our hotsprings are full, it seems that the whole town has agreed to come today!"
    Receptionist "Please change quickly and help, they need someone in there to take care of them"
    $ show_transparent(1, "plano_mujer_ojos_blanco_negro", width=1600, height=900)
    $ resolve_scene()
    Leyna "RI-RIGHT! I'll be right there, I'm sorry Johan, it looks like I won't be able to keep an eye on you"
    Johan "It's normal don't worry! I'll be over here taking a bath, try not to get nervous and I'm sure everything will be fine!"
    $ erase_picture(1)
    $ show_transparent(2, "plano_mujer_sonrisa", width=1600, height=900)
    $ resolve_scene()
    Leyna "Yes, I will do my best!"
    Johan "Of course! You can do it!"
    $ fade_out()
    $ erase_picture(2)
    call ChangePartyMember("Leyna", False) from _call_Receptionhotspringsjuntos_0_ChangePartyMember
    call TransferPlayer("HotSpringsWithJohan", "Receptionhotspringsjuntos_0", 2, 3, direction=2) from _call_Receptionhotspringsjuntos_0_TransferPlayer
    $ fade_in()
    $ set_self_switch("Reception","Receptionhotspringsjuntos","A",True)
    $ resolve_scene()
    return False

label Receptionhotspringsjuntos(play_event = True, trigger = None): # autorun
    if is_erased("Receptionhotspringsjuntos"):
        return None
    elif self_switch("Reception","Receptionhotspringsjuntos","A"):
        return None
    elif trigger == "autorun" and switch("final_hideout"):
        call PlayEvent(play_event, "Receptionhotspringsjuntos_0", "Receptionhotspringsjuntos") from _call_Receptionhotspringsjuntos_0_PlayEvent
        return (0, "", "Receptionhotspringsjuntos_0")
    return None

