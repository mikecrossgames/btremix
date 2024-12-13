label InnBG:
    $ set_transparency_backgrounds(["bg_inn"])
    $ set_map_backgrounds(["map_inn"])
    return

label InnStart:
    call InnBG from _call_InnBG
    stop music
    stop bgs
    return

label InnEnd:
    return

label InnToTown_0:
    call TransferPlayer("Town", "InnEV001_0", 28, 21, direction=2) from _call_InnEV001_0_TransferPlayer
    $ resolve_scene()
    return False

label InnToTown_1:
    call TransferPlayer("Town2", "InnEV001_1", 28, 21, direction=2) from _call_InnEV001_1_TransferPlayer
    $ resolve_scene()
    return False

label InnToTown(play_event = True, trigger = None): # event
    if is_erased("InnToTown"):
        return None
    elif trigger == "event" and switch("second_river"):
        call PlayEvent(play_event, "InnToTown_1", "InnToTown") from _call_InnToTown_1_PlayEvent
        return (0, "", "InnToTown_1")
    elif trigger == "event":
        call PlayEvent(play_event, "InnToTown_0", "InnToTown") from _call_InnToTown_0_PlayEvent
        return (0, "", "InnToTown_0")
    return None

label InnToInnRoomsBase:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_InnEV002_PlaySound
    call TransferPlayer("InnRooms", "InnEV002", 6, 18, direction=8) from _call_InnEV002_TransferPlayer
    $ resolve_scene()
    return False

label InnToInnRooms(play_event = True, trigger = None): # event
    if is_erased("InnToInnRooms"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnToInnRoomsBase", "InnToInnRooms") from _call_InnToInnRooms_PlayEvent
        return (0, "", "InnToInnRooms")
    return None

label InnToInnRooms_v2Base:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_InnEV003_PlaySound
    call TransferPlayer("InnRooms", "InnEV003", 7, 18, direction=8) from _call_InnEV003_TransferPlayer
    $ resolve_scene()
    return False

label InnToInnRooms_v2(play_event = True, trigger = None): # event
    if is_erased("InnToInnRooms_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnToInnRooms_v2Base", "InnToInnRooms_v2") from _call_InnToInnRooms_v2_PlayEvent
        return (0, "", "InnToInnRooms_v2")
    return None

label Innposadero_0:
    call Movement("Innposadero_0", "player", ["U","U","U","U","U","U","U","R","R"]) from _call_Innposadero_0_Movement
    $ resolve_scene()
    Johan "Hi, I have a room booked in the name of Johan"
    $ show_transparent(1, "plano_mujer_general", width=1600, height=900)
    $ resolve_scene()
    Innkeeper "(..what the fuck?)"
    "(who's that goddess? All women who were worth it in this damn town, have long since left..) "
    $ erase_picture(1)
    $ show_transparent(2, "plano_de_frente", width=1600, height=900)
    $ resolve_scene()
    "(look at the size of those tits!)"
    pause
    $ erase_picture(2)
    $ resolve_scene()
    Johan "emm... hello?"
    Innkeeper "ah, yes! Good morning, room in the name of Johan? Yes, we have it ready."
    "Have you come for the summer festival?"
    Johan "Yes, I work for a magazine and I'm going to write an article about the traditions of this town and its festivities."
    Innkeeper "oh! Great, that will help us get more people to come. If you want, later I can tell you some emblematic places to visit"
    Leyna "Great, thank you very much sir"
    Innkeeper "No worries, you can talk to me when you finish unpacking your things"
    call Movement("Innposadero_0", "player", ["TURN_L","L","L"]) from _call_Innposadero_0_Movement_1
    $ show_transparent(3, "plano_de_espaldas", width=1600, height=900)
    $ resolve_scene()
    "(damn!)"
    $ erase_picture(3)
    $ set_switch("innkeeper", True)
    $ resolve_scene()
    return False

label Innposadero_1:
    if suitcases == 0:
        $ resolve_scene()
        Innkeeper "Please leave your bags in your room and we will talk.."
    if suitcases == 1:
        Johan "We are ready."
        Innkeeper "Perfect. This town isn't very big, but it has quite interesting places."
        "First, you have the upper area, which is located to the north. There you will find the old castle, the town hall and some mansions where the wealthy live"
        "To the west, you have the police station and west exit of the village. There you can access the festival, the hot springs, and the coal mine, where most of the men work.."
        "... although I don't know why you would want to go there..."
        "To the south, you have the residential neighbourhoods and the town bar. Go carefully in that area, in this time of year people drink a lot and there are usually some problems."
        "And finally here in the east, you have most of the shops in town and, if you follow the path, you will reach the river.."
        "where some ancient rites are done, all naked bathing and that sort of things..."
        $ show_transparent(1, "plano_mujer_sorpresa_lado", width=1600, height=900)
        $ resolve_scene()
        Leyna "Naked?!"
        Innkeeper "Yes ... although.. being an outsider and a woman like you, I think they will allow an exception, but with these religious things you never know"
        $ show_transparent(2, "plano_mujer_timida", width=1600, height=900)
        $ resolve_scene()
        Leyna "Right..."
        $ erase_picture(1)
        $ erase_picture(2)
        $ resolve_scene()
        Innkeeper "Well, if you want to find out a bit about the festival and traditions of the town, ask around before getting into any misunderstanding."
        Johan "Great, thanks for your help."
        $ set_switch("suitcases", False)
        $ set_switch("inn_departure", True)
    $ resolve_scene()
    return False

label Innposadero_2:
    Innkeeper "Need anything?"
    return False

label Innposadero_3:
    Johan "Hello! I think a package has arrived for me?"
    Innkeeper "Right... Johan right? here you go"
    Johan "Thank you very much! have a nice evening"
    Innkeeper "Yeah, same here... (Not as good as yours buying that kind of stuff... with the wife he's got, lucky motherfucker)"
    call Movement("Innposadero_3", "player", ["L","L","L"]) from _call_Innposadero_3_Movement
    call TransferPlayer("InnRooms", "Innposadero_3", 11, 12, direction=8) from _call_Innposadero_3_TransferPlayer
    call Movement("Innposadero_3", "player", ["U","U"]) from _call_Innposadero_3_Movement_1
    $ resolve_scene()
    Johan "Well... I'm going to open it, I can't help it anymore"
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_Innposadero_3_PlaySound
    $ resolve_scene()
    call PauseForBalloon("Innposadero_3") from _call_Innposadero_3_PauseForBalloon
    Johan "So this is it... a butt plug... according to what I have read Leyna should wear it for a while before... well... that so that she would be prepared..."
    Johan "Hehehehehe great! I can't wait! I've been wanting to do something like this with Leyna for a long time...."
    Johan "Wait a minute... it comes with an instruction manual? How complicated does it have to be?"
    Johan "\"with this toy your wife will be looking forward to it when you get home from work\" hahahaha Great"
    Johan "\"Using our traditional techniques in...\" What the hell? I was right, they make it in this town...."
    Johan "\"We use a traditional blend of aphrodisiac herbs that will greatly intensify your partner's desire and arousal...\""
    Johan "they sure are fans here of the damn herbs... but hey... if it works I have nothing to complain about... now I just have to find Leyna"
    Johan "And see how she likes the idea... now that I think about it she should be here, where has she gone this time?"
    $ butt_plug = 2
    return False

label Innposadero_4:
    Innkeeper "Need anything?"
    return False

label Innposadero(play_event = True, trigger = None): # event, autorun
    if is_erased("Innposadero"):
        return None
    elif (trigger == "any" or trigger == "event") and butt_plug >= 2:
        call PlayEvent(play_event, "Innposadero_4", "Innposadero") from _call_Innposadero_4_PlayEvent
        return (1, "", "Innposadero_4")
    elif (trigger == "any" or trigger == "event") and butt_plug >= 1:
        call PlayEvent(play_event, "Innposadero_3", "Innposadero") from _call_Innposadero_3_PlayEvent
        return (1, "", "Innposadero_3")
    elif (trigger == "any" or trigger == "event") and switch("inn_departure"):
        call PlayEvent(play_event, "Innposadero_2", "Innposadero") from _call_Innposadero_2_PlayEvent
        return (1, "", "Innposadero_2")
    elif (trigger == "any" or trigger == "event") and switch("innkeeper"):
        call PlayEvent(play_event, "Innposadero_1", "Innposadero") from _call_Innposadero_1_PlayEvent
        return (1, "", "Innposadero_1")
    elif (trigger == "any" or trigger == "autorun"):
        call PlayEvent(play_event, "Innposadero_0", "Innposadero") from _call_Innposadero_0_PlayEvent
        return (1, "", "Innposadero_0")
    return None

label InnCantLeave_0:
    Johan "We have to leave the suitcases."
    call Movement("InnCantLeave_0", "player", ["TURN_U","U"]) from _call_InnCantLeave_0_Movement
    $ resolve_scene()
    return False

label InnCantLeave_1:
    Johan "We have to talk to the innkeeper."
    call Movement("InnCantLeave_1", "player", ["TURN_U","U"]) from _call_InnCantLeave_1_Movement
    $ resolve_scene()
    return False

label InnCantLeave(play_event = True, trigger = None): # event
    if is_erased("InnCantLeave"):
        return None
    elif switch("inn_departure"):
        return None
    elif trigger == "event" and switch("suitcases"):
        call PlayEvent(play_event, "InnCantLeave_1", "InnCantLeave") from _call_InnCantLeave_1_PlayEvent
        return (0, "", "InnCantLeave_1")
    elif trigger == "event" and switch("innkeeper"):
        call PlayEvent(play_event, "InnCantLeave_0", "InnCantLeave") from _call_InnCantLeave_0_PlayEvent
        return (0, "", "InnCantLeave_0")
    return None

label InnNPCEaterBase:
    Tourist "Wow the food is spectacular."
    return False

label InnNPCEater(play_event = True, trigger = None): # event
    if is_erased("InnNPCEater"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnNPCEaterBase", "InnNPCEater") from _call_InnNPCEater_PlayEvent
        return (1, "", "InnNPCEater")
    return None

label InnNPCDrinkerBase:
    DrunkTourist "we are preparing for the after party! the villagers don't stop talking about it."
    return False

label InnNPCDrinker(play_event = True, trigger = None): # event
    if is_erased("InnNPCDrinker"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnNPCDrinkerBase", "InnNPCDrinker") from _call_InnNPCDrinker_PlayEvent
        return (1, "", "InnNPCDrinker")
    return None

label InnNPCDinerBase:
    DrunkTourist "Ugh... drank too much...and i just want to sleep.... but my friend is too excited about the festival."
    return False

label InnNPCDiner(play_event = True, trigger = None): # event
    if is_erased("InnNPCDiner"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnNPCDinerBase", "InnNPCDiner") from _call_InnNPCDiner_PlayEvent
        return (1, "", "InnNPCDiner")
    return None

label InnmusicaposadaBase:
    call PlaySound("music", "audio/Town2.ogg", volume=0.9, no_loop=False) from _call_Innmusicaposada_PlaySound
    $ resolve_scene()
    return False

label Innmusicaposada(play_event = True, trigger = None): # parallel
    if is_erased("Innmusicaposada"):
        return None
    elif trigger == "parallel":
        call PlayEvent(play_event, "InnmusicaposadaBase", "Innmusicaposada") from _call_Innmusicaposada_PlayEvent
        return (0, "", "Innmusicaposada")
    return None

label InnpapelesposadaBase:
    "( Someone has left is rent papers)"
    return False

label Innpapelesposada(play_event = True, trigger = None): # event
    if is_erased("Innpapelesposada"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnpapelesposadaBase", "Innpapelesposada") from _call_Innpapelesposada_PlayEvent
        return (1, "", "Innpapelesposada")
    return None

label InnpanBase:
    "(hmmm it smells really good)"
    return False

label Innpan(play_event = True, trigger = None): # event
    if is_erased("Innpan"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnpanBase", "Innpan") from _call_Innpan_PlayEvent
        return (0, "", "Innpan")
    return None

label InnSueojohanpart2_0:
    call Movement("InnSueojohanpart2_0", "player", ["D","R","R","R"]) from _call_InnSueojohanpart2_0_Movement
    $ resolve_scene()
    Johan "Leyna?"
    $ resolve_scene()
    call PauseForBalloon("InnSueojohanpart2_0") from _call_InnSueojohanpart2_0_PauseForBalloon
    call Movement("InnSueojohanpart2_0", "InnLeyna", ["TURN_L"]) from _call_InnSueojohanpart2_0_Movement_1
    $ resolve_scene()
    Leyna "Good morning ... are you okay?"
    Johan "Yeah... I'm okey"
    Leyna "Great! Are we going to the festival? It should be open already"
    Johan "Hmm? The festival? Yeah yeah right... Let's go"
    $ fade_out()
    $ johan_dream = 2
    call ChangePartyMember("Leyna", True) from _call_InnSueojohanpart2_0_ChangePartyMember
    call TransferPlayer("Town2", "InnSueojohanpart2_0", 28, 21, direction=0) from _call_InnSueojohanpart2_0_TransferPlayer
    $ fade_in()
    $ resolve_scene()
    return False

label InnSueojohanpart2(play_event = True, trigger = None): # autorun
    if is_erased("InnSueojohanpart2"):
        return None
    elif johan_dream >= 2:
        return None
    elif trigger == "autorun" and johan_dream >= 1:
        call PlayEvent(play_event, "InnSueojohanpart2_0", "InnSueojohanpart2") from _call_InnSueojohanpart2_0_PlayEvent
        return (0, "", "InnSueojohanpart2_0")
    return None

label Inninicionochefiesta_0:
    call Movement("Inninicionochefiesta_0", "player", ["U","U","U","TURN_D"]) from _call_Inninicionochefiesta_0_Movement
    $ resolve_scene()
    Johan "Oh I almost forgot, several of the guys in town have told me that there're parties all over town tonight"
    Johan "And I was thinking if you feel like it, we could go out tonight,you know, have some dinner and a drink together"
    Johan "It's been a while since we've partied together like we used to"
    $ show_transparent(1, "expresion_gui_o_lengua")
    $ resolve_scene()
    Leyna "Sure, I'd love to! Now that you mention it, that's a good excuse to get dressed up. I have a little surprise for you that I brought from the apartment.."
    Johan "Oh! Now you've got me intrigued! I'm looking forward to seeing it"
    Leyna "Wait for me down here and I'll get ready"
    Johan "Sure, I'll be right here"
    $ fade_out()
    $ erase_picture(1)
    call ChangePartyMember("Leyna", False) from _call_Inninicionochefiesta_0_ChangePartyMember
    call TransferPlayer("InnNight", "Inninicionochefiesta_0", 3, 2, direction=2) from _call_Inninicionochefiesta_0_TransferPlayer
    $ fade_in()
    $ resolve_scene()
    call PauseForBalloon("Inninicionochefiesta_0") from _call_Inninicionochefiesta_0_PauseForBalloon
    Johan "Fuck, it's taking forever! What's she doing?"
    Leyna "Hi handsome... What do you think?"
    $ show_picture(2, "cambioropa")
    $ resolve_scene()
    Johan "WOW! You look gorgeous... wait, those clothes...."
    Leyna "Do you remember? I used to go out dressed like this when we were younger and partying around"
    Johan "Yes! Yes I remember... wow, you look beautiful... Now I feel bad to be dressed like this"
    Johan "Anyway, wow, I didn't remember it so revealing.."
    Leyna "Yeah... but I know you like to show off your wife, so it's okay, right?"
    Johan "Of course, I can't wait to show off my woman. Let's go for a walk around town and grab some dinner!"
    $ fade_out()
    $ erase_picture(2)
    call ChangePartyMember("Leyna", True) from _call_Inninicionochefiesta_0_ChangePartyMember_1
    call TransferPlayer("TownFestivalNight", "Inninicionochefiesta_0", 28, 21, direction=2) from _call_Inninicionochefiesta_0_TransferPlayer_1
    $ fade_in()
    call Movement("Inninicionochefiesta_0", "player", ["D","D"]) from _call_Inninicionochefiesta_0_Movement_1
    $ ritual = 3
    $ resolve_scene()
    return False

label Inninicionochefiesta(play_event = True, trigger = None): # autorun
    if is_erased("Inninicionochefiesta"):
        return None
    elif ritual >= 3:
        return None
    elif trigger == "autorun" and ritual >= 2:
        call PlayEvent(play_event, "Inninicionochefiesta_0", "Inninicionochefiesta") from _call_Inninicionochefiesta_0_PlayEvent
        return (0, "", "Inninicionochefiesta_0")
    return None

label InneventoJohanyalexa_0(menu_choice = None):
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ resolve_scene()
    "Meanwhile Johan was on his way to continue his work"
    call ChangePartyMember("Johan", True) from _call_InneventoJohanyalexa_0_ChangePartyMember
    call ChangePartyMember("Leyna", False) from _call_InneventoJohanyalexa_0_ChangePartyMember_1
    call TransferPlayer("Path", "InneventoJohanyalexa_0", 22, 10, direction=4) from _call_InneventoJohanyalexa_0_TransferPlayer
    $ erase_picture(1)
    $ resolve_scene()
    call PauseForBalloon("InneventoJohanyalexa_0") from _call_InneventoJohanyalexa_0_PauseForBalloon
    Johan "At the end I got nervous at the bar watching Leyna surrounded by men and being semi naked...."
    Johan "I've also drank more beer than I should..."
    Johan "... Anyway, let's finish with this interview and I'll be back with Leyna..."
    Johan "And tonight we could..."
    if johan_leyna_sex == 1:
        $ resolve_scene()
        $ flash_screen([255,255,255,170], 60, True)
        $ show_picture(1, "fotoerotica8")
        $ resolve_scene()
        Johan "Shit, again...I can't help it...every time I think about fucking with Leyna these images come to my mind"
        $ erase_picture(1)
    if johan_leyna_sex == 2:
        $ show_picture(1, "johanfollar9")
        $ resolve_scene()
        Johan "Hehehehehe that was good.... well tonight we'll see"
        $ erase_picture(1)
    $ resolve_scene()
    Johan "Anyway, enough of this nonsense... I should go to the festival. I'm meeting the mayor for the interview"
    $ fade_out()
    call TransferPlayer("Festival", "InneventoJohanyalexa_0", 8, 17, direction=0) from _call_InneventoJohanyalexa_0_TransferPlayer_1
    $ fade_in()
    call Movement("InneventoJohanyalexa_0", "player", ["TURN_L","TURN_R","TURN_U","TURN_D"]) from _call_InneventoJohanyalexa_0_Movement
    $ resolve_scene()
    call PauseForBalloon("InneventoJohanyalexa_0") from _call_InneventoJohanyalexa_0_PauseForBalloon_1
    $ show_picture(1, "johanxalexa1")
    $ resolve_scene()
    Johan "Damn it... I've been waiting for half an hour already ..."
    Johan "And while I was waiting, I couldn't help but drink one of those infusions they make in this town"
    Johan "The guy who offered it to me has been very annoying"
    Johan "Now, in addition to being drunk, I feel very strange"
    $ show_picture(2, "johanxalexa2")
    $ resolve_scene()
    Alexa "Helloooo Johan..."
    Johan "!!!"
    $ show_picture(3, "johanxalexa3")
    $ resolve_scene()
    Alexa "What are you doing here alone Johaaaan?"
    Johan "(Wow, she's so close! she's touching me with her breasts)"
    Johan "(she looks like she's drunk or something... this girl never acts normal but today she's even weirder than ever...)"
    $ show_picture(4, "johanxalexa4")
    $ resolve_scene()
    Alexa "I don't know if it's the infusion or what... but today you're very attractive Johan..."
    Johan "O-oh? really? i uhmm.... thank you"
    Alexa "Why don't you come a little closer to me and give me a kiss?"
    Johan "I-I don't... (How good Alexa smells... I hadn't noticed but she is very pretty)"
    Alexa "Come on, come here, what's the problem?"
    Johan "I-I can't do that... you know I'm married"
    Alexa "Well..."
    $ show_picture(5, "johanxalexa5")
    $ resolve_scene()
    Johan "!!!!"
    Alexa "You're telling me no, but this one here is telling me yes..."
    Johan "Sto-stop..."
    Alexa "Oooh? how shy Johan"
    $ show_picture(6, "johanxalexa6")
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_InneventoJohanyalexa_0_PlaySound
    $ resolve_scene()
    Alexa "Look how hard it is... that's for me?... you like me that much?"
    Johan "We shouldn't... anyone can see us... (I'm having trouble thinking clearly... what's happening to me? I want to fuck her with all my will)"
    Johan "But I can't do it, Leyna is my wife and she's perfect! besides... anyone could see us!)"
    Alexa "Come with me... let's go to a more private place..."
    Johan "I..."
    call GetChoice([_("Go with Alexa"), _("No")], value=menu_choice, called_from="InneventoJohanyalexa_0") from _call_InneventoJohanyalexa_0_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Go with Alexa"):
        $ menu_choice = None
        $ resolve_scene()
        Johan "C-Come on..."
        $ fade_out()
        $ show_picture(7, "johanxalexa7")
        $ fade_in()
        $ resolve_scene()
        Alexa "Here no one will see us, come on man, we are going to have a good time"
        Johan "(God... am I really doing this?...I can't believe it... this all seems like a hallucination)"
        $ show_picture(8, "johanxalexa8")
        $ resolve_scene()
        Alexa "That's it, it's almost in... fuck me"
        Johan "Ohhh you are so warm...."
        Johan "I'm going to fuck you like you've never been fucked before..."
        Alexa "Well, don't make me wait any longer"
        $ show_picture(9, "johanxalexa9")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_InneventoJohanyalexa_0_PlaySound_1
        $ resolve_scene()
        Alexa "Yes! like this! go on, don't stop"
        Johan "Ah ah ah!!!"
        Alexa "Keep fucking me like that!"
        pause
        $ show_picture(10, "johanxalexa10")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_InneventoJohanyalexa_0_PlaySound_2
        $ resolve_scene()
        Alexa "That's it, break me in half..."
        Alexa "Fuck me hard... anyone could see us at any time Johan ... do you like that?"
        Johan "Ah ah ah ah, yes, I love it, let them see us while I fuck you, I don't care!"
        Alexa "Aaaah I love it!"
        pause
        $ show_picture(11, "johanxalexa11")
        call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_InneventoJohanyalexa_0_PlaySound_3
        $ resolve_scene()
        Johan "AH! I am about to..."
        Alexa "Keep fucking me hard Johan!"
        Alexa "Fuck me like the whore I am!!!"
        Johan "AH AH AH I'm going to cum!"
        Alexa "Cum inside my Johan, use me like a tissue"
        Johan "ah ahaaah!!"
        $ flash_screen([255,255,255,170], 60, True)
        $ show_picture(12, "johanxalexa12")
        $ resolve_scene()
        $ flash_screen([255,255,255,170], 60, True)
        stop bgs fadeout 1
        Johan "Aaaaaahhh...."
        Alexa "Very good Johan... that's the way I like it..."
        Johan "ah ah ah (WHAT THE HELL HAVE I DONE?)"
        Johan "(I have to get out of here right now... I'm getting dizzy)"
        Alexa "Shall we have a drink? I'm thirsty"
        Johan "I-I can't, I have to go to work"
        Alexa "Work?...I see"
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
        call ChangePartyMember("Leyna", True) from _call_InneventoJohanyalexa_0_ChangePartyMember_2
        call ChangePartyMember("Johan", False) from _call_InneventoJohanyalexa_0_ChangePartyMember_3
        $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
        $ erase_picture(1)
        call TransferPlayer("Town2", "InneventoJohanyalexa_0", 28, 22, direction=2) from _call_InneventoJohanyalexa_0_TransferPlayer_2
        $ fade_in()
        $ resolve_scene()
        "The next day..."
        Leyna "Where did Johan go? he didn't wake me up when he left this morning"
        $ bar_work = 2
        call GalleryViewed("johanxalexa") from _call_InneventoJohanyalexa_0_GalleryViewed
        Leyna "I don't have time to worry about that I should go to work at the bar"
    elif menu_choice == _("No"):
        $ menu_choice = None
        Johan "N-no, I can't do it, I'm married, s-sorry"
        Alexa "Oh come on, wait don't leave"
        Johan "I'm sorry..."
        $ fade_out()
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(4)
        $ erase_picture(5)
        $ erase_picture(6)
        call TransferPlayer("Path", "InneventoJohanyalexa_0", 7, 10, direction=6) from _call_InneventoJohanyalexa_0_TransferPlayer_3
        $ fade_in()
        call Movement("InneventoJohanyalexa_0", "player", ["R","R","R","R"]) from _call_InneventoJohanyalexa_0_Movement_1
        $ resolve_scene()
        call PauseForBalloon("InneventoJohanyalexa_0") from _call_InneventoJohanyalexa_0_PauseForBalloon_2
        Johan "that was a close call..."
        Johan "I should go back to the inn..."
        $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
        call ChangePartyMember("Leyna", True) from _call_InneventoJohanyalexa_0_ChangePartyMember_4
        call ChangePartyMember("Johan", False) from _call_InneventoJohanyalexa_0_ChangePartyMember_5
        call TransferPlayer("Town2", "InneventoJohanyalexa_0", 28, 22, direction=2) from _call_InneventoJohanyalexa_0_TransferPlayer_4
        $ resolve_scene()
        "The next day..."
        $ erase_picture(1)
        $ resolve_scene()
        Leyna "Well... one more day! Johan has already left to continue with his interviews... I should go to work at the bar now"
        $ bar_work = 2
        call GalleryViewed("johanxalexa") from _call_InneventoJohanyalexa_0_GalleryViewed_1
    $ resolve_scene()
    return False

label InneventoJohanyalexa(play_event = True, trigger = None): # autorun
    if is_erased("InneventoJohanyalexa"):
        return None
    elif bar_work >= 2:
        return None
    elif trigger == "autorun" and bar_work >= 1:
        call PlayEvent(play_event, "InneventoJohanyalexa_0", "InneventoJohanyalexa") from _call_InneventoJohanyalexa_0_PlayEvent
        return (0, "", "InneventoJohanyalexa_0")
    return None

label InnToInn_0:
    $ fade_out()
    call TransferPlayer("Inn", "InnEV016_0", 3, 3, direction=6) from _call_InnEV016_0_TransferPlayer
    $ fade_in()
    $ resolve_scene()
    call PauseForBalloon("InnEV016_0") from _call_InnEV016_0_PauseForBalloon
    Johan "Hey Leyna, good morning..."
    $ resolve_scene()
    call PauseForBalloon("InnEV016_0") from _call_InnEV016_0_PauseForBalloon_1
    call Movement("InnEV016_0", "InnLeyna", [["WAIT",60],"TURN_L"]) from _call_InnEV016_0_Movement
    $ resolve_scene()
    Leyna "J-Johan... you're awake... how are you?"
    Johan "Well, with a big hangover... but I guess I'm okay hahahaha"
    Leyna "Don't you remember what happened yesterday?"
    Johan "???"
    Johan "...Well, not much, something about playing cards and that we were with Alexa, but not much else really"
    Leyna "( Jesus Christ, he doesn't remember... thank goodness...)"
    Johan "I-I done something wrong? I didn't fight with anyone, did I?"
    Leyna "OH... well there was a little argument... but it was silly hahaha nothing important happened...."
    Johan "I see... well, it's the last day of the festival"
    Leyna "Yes..."
    Johan "The celebrations will not start until the afternoon-evening so why don't we take advantage of it and spend the morning together relaxed?"
    Leyna "!!! Nice!"
    Johan "Great lately we haven't been able to spend much time together without any stress...."
    Leyna "Yes, hahaha we have been very... busy"
    Johan "Yes... let's start with a good breakfast, what do you think?"
    Leyna "I think it's a great idea"
    Johan "Perfect then... let's go to the bar"
    $ fade_out()
    call ChangePartyMember("Leyna", True) from _call_InnEV016_0_ChangePartyMember
    $ set_self_switch("Inn","InnToInn","A",True)
    $ set_switch("breakfast", True)
    call Movement("InnEV016_0", "player", ["D","D","TURN_U"]) from _call_InnEV016_0_Movement_1
    call TransferPlayer("Town2", "InnEV016_0", 28, 22, direction=0) from _call_InnEV016_0_TransferPlayer_1
    $ fade_in()
    $ resolve_scene()
    return False

label InnToInn(play_event = True, trigger = None): # autorun
    if is_erased("InnToInn"):
        return None
    elif self_switch("Inn","InnToInn","A"):
        return None
    elif trigger == "autorun" and switch("bet_2"):
        call PlayEvent(play_event, "InnToInn_0", "InnToInn") from _call_InnToInn_0_PlayEvent
        return (0, "", "InnToInn_0")
    return None

