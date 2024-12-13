label FestivalBG:
    $ set_transparency_backgrounds(["bg_festival"])
    $ set_map_backgrounds(["map_festival"])
    return

label FestivalStart:
    call FestivalBG from _call_FestivalBG
    stop music
    stop bgs
    return

label FestivalEnd:
    return

label FestivalToPath_0:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_FestivalEV001_0_PlaySound
    call TransferPlayer("Path", "FestivalEV001_0", 0, 9, direction=0) from _call_FestivalEV001_0_TransferPlayer
    $ resolve_scene()
    return False

label FestivalToPath_1:
    "(We have to talk to the worker first)"
    return False

label FestivalToPath_2:
    Johan "(There's still much to do in the festival)"
    return False

label FestivalToPath_3:
    $ fade_out()
    call TransferPlayer("Path", "FestivalEV001_3", 1, 10, direction=6) from _call_FestivalEV001_3_TransferPlayer
    $ fade_in()
    $ resolve_scene()
    return False

label FestivalToPath_4:
    Leyna "I have to go to work at the food stand"
    return False

label FestivalToPath(play_event = True, trigger = None): # event
    if is_erased("FestivalToPath"):
        return None
    elif trigger == "event" and butt_plug >= 3:
        call PlayEvent(play_event, "FestivalToPath_4", "FestivalToPath") from _call_FestivalToPath_4_PlayEvent
        return (0, "", "FestivalToPath_4")
    elif trigger == "event" and leyna_work >= 11:
        call PlayEvent(play_event, "FestivalToPath_3", "FestivalToPath") from _call_FestivalToPath_3_PlayEvent
        return (0, "", "FestivalToPath_3")
    elif trigger == "event" and elder_festival >= 10:
        call PlayEvent(play_event, "FestivalToPath_2", "FestivalToPath") from _call_FestivalToPath_2_PlayEvent
        return (0, "", "FestivalToPath_2")
    elif trigger == "event" and elder_festival >= 7:
        call PlayEvent(play_event, "FestivalToPath_1", "FestivalToPath") from _call_FestivalToPath_1_PlayEvent
        return (0, "", "FestivalToPath_1")
    elif trigger == "event" and switch("third_day"):
        call PlayEvent(play_event, "FestivalToPath_0", "FestivalToPath") from _call_FestivalToPath_0_PlayEvent
        return (0, "", "FestivalToPath_0")
    return None

label FestivalToPath_v2_0:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_FestivalEV002_0_PlaySound
    call TransferPlayer("Path", "FestivalEV002_0", 0, 10, direction=0) from _call_FestivalEV002_0_TransferPlayer
    $ resolve_scene()
    return False

label FestivalToPath_v2_1:
    "(We have to talk to the worker first)"
    return False

label FestivalToPath_v2_2:
    Johan "(There's still much to do in the festival)"
    return False

label FestivalToPath_v2_3:
    $ fade_out()
    call TransferPlayer("Path", "FestivalEV002_3", 1, 10, direction=6) from _call_FestivalEV002_3_TransferPlayer
    $ fade_in()
    $ resolve_scene()
    return False

label FestivalToPath_v2_4:
    Leyna "I have to go to work at the food stand"
    return False

label FestivalToPath_v2(play_event = True, trigger = None): # event
    if is_erased("FestivalToPath_v2"):
        return None
    elif trigger == "event" and butt_plug >= 3:
        call PlayEvent(play_event, "FestivalToPath_v2_4", "FestivalToPath_v2") from _call_FestivalToPath_v2_4_PlayEvent
        return (0, "", "FestivalToPath_v2_4")
    elif trigger == "event" and leyna_work >= 11:
        call PlayEvent(play_event, "FestivalToPath_v2_3", "FestivalToPath_v2") from _call_FestivalToPath_v2_3_PlayEvent
        return (0, "", "FestivalToPath_v2_3")
    elif trigger == "event" and elder_festival >= 10:
        call PlayEvent(play_event, "FestivalToPath_v2_2", "FestivalToPath_v2") from _call_FestivalToPath_v2_2_PlayEvent
        return (0, "", "FestivalToPath_v2_2")
    elif trigger == "event" and elder_festival >= 7:
        call PlayEvent(play_event, "FestivalToPath_v2_1", "FestivalToPath_v2") from _call_FestivalToPath_v2_1_PlayEvent
        return (0, "", "FestivalToPath_v2_1")
    elif trigger == "event" and switch("third_day"):
        call PlayEvent(play_event, "FestivalToPath_v2_0", "FestivalToPath_v2") from _call_FestivalToPath_v2_0_PlayEvent
        return (0, "", "FestivalToPath_v2_0")
    return None

label FestivalToPath_v3_0:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_FestivalEV003_0_PlaySound
    call TransferPlayer("Path", "FestivalEV003_0", 0, 10, direction=0) from _call_FestivalEV003_0_TransferPlayer
    $ resolve_scene()
    return False

label FestivalToPath_v3_1:
    "(We have to talk to the worker first)"
    return False

label FestivalToPath_v3_2:
    Johan "(There's still much to do in the festival)"
    return False

label FestivalToPath_v3_3:
    $ fade_out()
    call TransferPlayer("Path", "FestivalEV003_3", 1, 10, direction=6) from _call_FestivalEV003_3_TransferPlayer
    $ fade_in()
    $ resolve_scene()
    return False

label FestivalToPath_v3_4:
    Leyna "I have to go to work at the food stand"
    return False

label FestivalToPath_v3(play_event = True, trigger = None): # event
    if is_erased("FestivalToPath_v3"):
        return None
    elif trigger == "event" and butt_plug >= 3:
        call PlayEvent(play_event, "FestivalToPath_v3_4", "FestivalToPath_v3") from _call_FestivalToPath_v3_4_PlayEvent
        return (0, "", "FestivalToPath_v3_4")
    elif trigger == "event" and leyna_work >= 11:
        call PlayEvent(play_event, "FestivalToPath_v3_3", "FestivalToPath_v3") from _call_FestivalToPath_v3_3_PlayEvent
        return (0, "", "FestivalToPath_v3_3")
    elif trigger == "event" and elder_festival >= 10:
        call PlayEvent(play_event, "FestivalToPath_v3_2", "FestivalToPath_v3") from _call_FestivalToPath_v3_2_PlayEvent
        return (0, "", "FestivalToPath_v3_2")
    elif trigger == "event" and elder_festival >= 7:
        call PlayEvent(play_event, "FestivalToPath_v3_1", "FestivalToPath_v3") from _call_FestivalToPath_v3_1_PlayEvent
        return (0, "", "FestivalToPath_v3_1")
    elif trigger == "event" and switch("third_day"):
        call PlayEvent(play_event, "FestivalToPath_v3_0", "FestivalToPath_v3") from _call_FestivalToPath_v3_0_PlayEvent
        return (0, "", "FestivalToPath_v3_0")
    return None

label Festivalworkerdentrofestival_0:
    Worker "Hey guys!"
    Johan "Hi! We already have the festival clothes"
    Worker "The opening will be tomorrow, at the moment there's nothing interesting here,but you can take a look"
    Leyna "Thank you! We won't bother you for long"
    Worker "Let me know when you're done, I have to close the access"
    $ elder_festival = 7
    return False

label Festivalworkerdentrofestival_1:
    Worker "It's getting late, we must go now"
    Worker "Go to rest, see you tomorrow at the inauguration"
    Leyna "Thanks for everything"
    call Movement("Festivalworkerdentrofestival_1", "player", ["U","U","U"]) from _call_Festivalworkerdentrofestival_1_Movement
    $ fade_out()
    call TransferPlayer("Path", "Festivalworkerdentrofestival_1", 1, 10, direction=6) from _call_Festivalworkerdentrofestival_1_TransferPlayer
    $ fade_in()
    $ elder_festival = 8
    $ resolve_scene()
    return False

label Festivalworkerdentrofestival_2:
    Worker "Enjoy the festival!"
    return False

label Festivalworkerdentrofestival(play_event = True, trigger = None): # event
    if is_erased("Festivalworkerdentrofestival"):
        return None
    elif switch("last_hotsprings"):
        return None
    elif trigger == "event" and switch("festival"):
        call PlayEvent(play_event, "Festivalworkerdentrofestival_2", "Festivalworkerdentrofestival") from _call_Festivalworkerdentrofestival_2_PlayEvent
        return (1, "", "Festivalworkerdentrofestival_2")
    elif trigger == "event" and elder_festival >= 7:
        call PlayEvent(play_event, "Festivalworkerdentrofestival_1", "Festivalworkerdentrofestival") from _call_Festivalworkerdentrofestival_1_PlayEvent
        return (1, "", "Festivalworkerdentrofestival_1")
    elif trigger == "event" and elder_festival >= 6:
        call PlayEvent(play_event, "Festivalworkerdentrofestival_0", "Festivalworkerdentrofestival") from _call_Festivalworkerdentrofestival_0_PlayEvent
        return (1, "", "Festivalworkerdentrofestival_0")
    return None

label FestivalNPCDrinkCrazy_1:
    Villager "Enjoy the festival! Drink like crazy ... but responsibly"
    return False

label FestivalNPCDrinkCrazy(play_event = True, trigger = None): # event
    if is_erased("FestivalNPCDrinkCrazy"):
        return None
    elif trigger == "event" and suitcases >= 3:
        call PlayEvent(play_event, "FestivalNPCDrinkCrazy_1", "FestivalNPCDrinkCrazy") from _call_FestivalNPCDrinkCrazy_1_PlayEvent
        return (1, "", "FestivalNPCDrinkCrazy_1")
    return None

label FestivalNPCShrooms_1:
    Villager "My friends have taken some mushrooms and they are lost in the mountains"
    Johan "Be careful guys"
    return False

label FestivalNPCShrooms_2:
    Villager "My friends have taken some mushrooms and they are lost in the mountains"
    Leyna "Aren't you worried?"
    Villager "I would be if I hadn't taken them myself... AAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAHH!"
    return False

label FestivalNPCShrooms(play_event = True, trigger = None): # event
    if is_erased("FestivalNPCShrooms"):
        return None
    elif trigger == "event" and butt_plug >= 3:
        call PlayEvent(play_event, "FestivalNPCShrooms_2", "FestivalNPCShrooms") from _call_FestivalNPCShrooms_2_PlayEvent
        return (1, "", "FestivalNPCShrooms_2")
    elif trigger == "event" and johan_dream >= 3:
        call PlayEvent(play_event, "FestivalNPCShrooms_1", "FestivalNPCShrooms") from _call_FestivalNPCShrooms_1_PlayEvent
        return (1, "", "FestivalNPCShrooms_1")
    return None

label FestivalNPCNiceTits_1:
    Villager "Nice tits"
    Johan "You are talking to my wife"
    Villager "Sorry?"
    return False

label FestivalNPCNiceTits_2:
    Villager "Nice tits"
    Leyna "Th-thanks?"
    Villager "You are welcome"
    return False

label FestivalNPCNiceTits(play_event = True, trigger = None): # event
    if is_erased("FestivalNPCNiceTits"):
        return None
    elif trigger == "event" and butt_plug >= 3:
        call PlayEvent(play_event, "FestivalNPCNiceTits_2", "FestivalNPCNiceTits") from _call_FestivalNPCNiceTits_2_PlayEvent
        return (1, "", "FestivalNPCNiceTits_2")
    elif trigger == "event" and johan_dream >= 3:
        call PlayEvent(play_event, "FestivalNPCNiceTits_1", "FestivalNPCNiceTits") from _call_FestivalNPCNiceTits_1_PlayEvent
        return (1, "", "FestivalNPCNiceTits_1")
    return None

label FestivalNPCFruit_1:
    Villager "Wow, the fruit that they gave me is really powerful, I can't lower my erection"
    if switch("ate_the_fruit"):
        $ resolve_scene()
        Johan "...( Yeah me too...)"
        Leyna "(I'm glad I'm not the only one excited...)"
    $ resolve_scene()
    return False

label FestivalNPCFruit_2:
    Villager "Wow, the fruit that they gave me is really powerful, I can't lower my erection"
    Leyna "I see I am not the only one"
    return False

label FestivalNPCFruit(play_event = True, trigger = None): # event
    if is_erased("FestivalNPCFruit"):
        return None
    elif trigger == "event" and johan_dream >= 3:
        call PlayEvent(play_event, "FestivalNPCFruit_2", "FestivalNPCFruit") from _call_FestivalNPCFruit_2_PlayEvent
        return (1, "", "FestivalNPCFruit_2")
    elif trigger == "event" and johan_dream >= 3:
        call PlayEvent(play_event, "FestivalNPCFruit_1", "FestivalNPCFruit") from _call_FestivalNPCFruit_1_PlayEvent
        return (1, "", "FestivalNPCFruit_1")
    return None

label FestivalNPCHeyCutie_1:
    Villager "Hey cutie..."
    return False

label FestivalNPCHeyCutie(play_event = True, trigger = None): # event
    if is_erased("FestivalNPCHeyCutie"):
        return None
    elif trigger == "event" and johan_dream >= 3:
        call PlayEvent(play_event, "FestivalNPCHeyCutie_1", "FestivalNPCHeyCutie") from _call_FestivalNPCHeyCutie_1_PlayEvent
        return (1, "", "FestivalNPCHeyCutie_1")
    return None

label FestivalNPCSkint_1:
    Villager "Shit, I left my wallet at home.."
    Villager "How am I supposed to keep my things with this kind of clothes anyway?"
    return False

label FestivalNPCSkint(play_event = True, trigger = None): # event
    if is_erased("FestivalNPCSkint"):
        return None
    elif trigger == "event" and johan_dream >= 3:
        call PlayEvent(play_event, "FestivalNPCSkint_1", "FestivalNPCSkint") from _call_FestivalNPCSkint_1_PlayEvent
        return (1, "", "FestivalNPCSkint_1")
    return None

label FestivalNPCCompliment_1:
    Villager "Is that your wife? She is beautiful"
    Johan "Thanks?"
    return False

label FestivalNPCCompliment_2:
    OldVillager "WOW! You look beautiful in those clothes!"
    return False

label FestivalNPCCompliment(play_event = True, trigger = None): # event
    if is_erased("FestivalNPCCompliment"):
        return None
    elif trigger == "event" and butt_plug >= 3:
        call PlayEvent(play_event, "FestivalNPCCompliment_2", "FestivalNPCCompliment") from _call_FestivalNPCCompliment_2_PlayEvent
        return (1, "", "FestivalNPCCompliment_2")
    elif trigger == "event" and johan_dream >= 3:
        call PlayEvent(play_event, "FestivalNPCCompliment_1", "FestivalNPCCompliment") from _call_FestivalNPCCompliment_1_PlayEvent
        return (1, "", "FestivalNPCCompliment_1")
    return None

label FestivalWorkerSon_1:
    Villager "Heeeey...."
    return False

label FestivalFestivalWorkerSon(play_event = True, trigger = None): # event
    if is_erased("FestivalFestivalWorkerSon"):
        return None
    elif trigger == "event" and johan_dream >= 3:
        call PlayEvent(play_event, "FestivalWorkerSon_1", "FestivalFestivalWorkerSon") from _call_FestivalWorkerSon_1_PlayEvent
        return (1, "", "FestivalWorkerSon_1")
    return None

label FestivalNPCLetch_1:
    Villager "Hey! If you want me to buy you a beer, tell me"
    Johan "We're fine for now thanks"
    return False

label FestivalNPCLetch_2:
    Villager "Hey! It's a good thing you're no longer with that jerk, why don't we go back there and have a good time?"
    Leyna "Hmmm thanks but no"
    Villager "If you change your mind, you know where to find me"
    return False

label FestivalNPCLetch(play_event = True, trigger = None): # event
    if is_erased("FestivalNPCLetch"):
        return None
    elif trigger == "event" and butt_plug >= 3:
        call PlayEvent(play_event, "FestivalNPCLetch_2", "FestivalNPCLetch") from _call_FestivalNPCLetch_2_PlayEvent
        return (1, "", "FestivalNPCLetch_2")
    elif trigger == "event" and johan_dream >= 3:
        call PlayEvent(play_event, "FestivalNPCLetch_1", "FestivalNPCLetch") from _call_FestivalNPCLetch_1_PlayEvent
        return (1, "", "FestivalNPCLetch_1")
    return None

label Festivalintrofestival_0:
    Leyna "Is he the worker we helped yesterday?"
    Johan "Yes! Let's talk with him and see if he can guide us a bit"
    call Movement("Festivalintrofestival_0", "player", ["L","D","D","D"]) from _call_Festivalintrofestival_0_Movement
    $ resolve_scene()
    Johan "Good morning!"
    Worker "Oh! Good morning couple, how can I help you?"
    Johan "We just arrived and it seems to be so many things to do that we don't know where to start"
    Worker "It's normal the first time, don't worry"
    Worker "Within an hour the inauguration rite will begin, where the \"lucky person\" will be chosen"
    Leyna "Lucky person?"
    Worker "Yes! It's said that everyone who touches it will have good luck for a whole year!"
    Johan "..."
    Worker "Anyway, there's still a while for that... I've to go for a fruit that grows in these mountains we usually eat it before the festival starts"
    Worker "Puts everyone ... let's say.. in a good mood Do you want to come with me?"
    Johan "Sure!"
    Worker "Perfect! Follow me then"
    call Movement("Festivalintrofestival_0", "Festivalworkerdentrofestival", ["L","L","L"]) from _call_Festivalintrofestival_0_Movement_1
    $ fade_out()
    call TransferPlayer("Mountains", "Festivalintrofestival_0", 19, 8, direction=4) from _call_Festivalintrofestival_0_TransferPlayer
    $ fade_in()
    $ elder_festival = 10
    $ resolve_scene()
    return False

label Festivalintrofestival(play_event = True, trigger = None): # autorun
    if is_erased("Festivalintrofestival"):
        return None
    elif switch("fruit_event"):
        return None
    elif trigger == "autorun" and switch("festival"):
        call PlayEvent(play_event, "Festivalintrofestival_0", "Festivalintrofestival") from _call_Festivalintrofestival_0_PlayEvent
        return (0, "", "Festivalintrofestival_0")
    return None

label Festivalintrosorteo_0:
    $ fade_out()
    call SetEventLocation("Festivalintrosorteo_0", "Festivalworkerdentrofestival", 3, 12) from _call_Festivalintrosorteo_0_setloc
    $ fade_in()
    if switch("ate_the_fruit"):
        $ resolve_scene()
        Leyna "(I feel... weird...are these the effects of the strange fruit?)"
    call Movement("Festivalintrosorteo_0", "player", ["R","R"]) from _call_Festivalintrosorteo_0_Movement
    $ resolve_scene()
    Worker "Okay guys, follow me. We're late for the opening"
    Leyna "Y..Yeah"
    call Movement("Festivalintrosorteo_0", "Festivalworkerdentrofestival", [["CHANGE_SPEED",4],"D","D","D","D","R","R","D","D","D","D","D","D","L","L","TURN_U"]) from _call_Festivalintrosorteo_0_Movement_1
    call Movement("Festivalintrosorteo_0", "player", ["R","D","D","D","D","R","R","D","D","D","D","D","D","L","TURN_U"]) from _call_Festivalintrosorteo_0_Movement_2
    $ fade_out()
    call TransferPlayer("Casino", "Festivalintrosorteo_0", 7, 12, direction=8) from _call_Festivalintrosorteo_0_TransferPlayer
    $ fade_in()
    $ resolve_scene()
    return False

label Festivalintrosorteo(play_event = True, trigger = None): # autorun
    if is_erased("Festivalintrosorteo"):
        return None
    elif switch("lucky_person"):
        return None
    elif trigger == "autorun" and switch("fruit_event"):
        call PlayEvent(play_event, "Festivalintrosorteo_0", "Festivalintrosorteo") from _call_Festivalintrosorteo_0_PlayEvent
        return (0, "", "Festivalintrosorteo_0")
    return None

label FestivalSpyOnAlexa_0:
    Alexa "AAAhhh!! OOOOooh!!! HARDER!"
    Villager "YES!"
    $ resolve_scene()
    Johan "Hahahaha oh shit! someone is having a good time back there"
    Johan "Better not disturb them"
    call Movement("FestivalEV019_0", "player", ["L"]) from _call_FestivalEV019_0_Movement
    $ resolve_scene()
    return False

label FestivalSpyOnAlexa(play_event = True, trigger = None): # event
    if is_erased("FestivalSpyOnAlexa"):
        return None
    elif butt_plug >= 3:
        return None
    elif trigger == "event" and johan_dream >= 3:
        call PlayEvent(play_event, "FestivalSpyOnAlexa_0", "FestivalSpyOnAlexa") from _call_FestivalSpyOnAlexa_0_PlayEvent
        return (1, "", "FestivalSpyOnAlexa_0")
    return None

label FestivalFoodStand_0:
    Johan "Are you hungry? I'm starving.. Let's eat something here, it smells delicious"
    Leyna "Please!"
    call Movement("FestivalEV020_0", "player", ["U","L","TURN_U"]) from _call_FestivalEV020_0_Movement
    $ show_picture(1, "puesto1")
    $ resolve_scene()
    Johan "This food is so good!"
    Leyna "I need the recipe to make it at home"
    $ fade_out()
    $ erase_picture(1)
    call SetEventLocation("FestivalEV020_0", "FestivalHIJOWORKER", 16, 5) from _call_FestivalEV020_0_setloc
    call SetEventLocation("FestivalEV020_0", "FestivalFestivalWorkerSon", 15, 5) from _call_FestivalEV020_0_setloc_1
    $ resolve_scene()
    $ fade_in()
    $ resolve_scene()
    WorkersSon "Hey dude, this is the woman I talked to you about"
    $ show_picture(2, "puesto2")
    $ resolve_scene()
    Friend "She's so hot. Look at that ass"
    $ show_picture(3, "puesto3")
    $ resolve_scene()
    WorkersSon "Right? Everyone here is trying to fuck her, it's like she is asking for it."
    $ show_picture(4, "puesto4")
    $ resolve_scene()
    WorkersSon "I have an idea, let's say hi, keep talking to the man and I will try something"
    Friend "Be careful man, I don't want any trouble"
    WorkersSon "Don't worry,I can be stealthy when I want"
    $ show_picture(5, "puesto5")
    $ resolve_scene()
    WorkersSon "Hey guys, what a surprise to see you here. Are you having a good time?"
    Johan "Hey kid! Yes, this is very fun"
    $ show_picture(6, "puesto6")
    $ resolve_scene()
    WorkersSon "\"Whispering \"Leyna, it's nice to see you in those clothes"
    $ show_picture(7, "puesto7")
    $ resolve_scene()
    Leyna "He..hello"
    $ show_picture(8, "puesto8")
    $ resolve_scene()
    WorkersSon "They say you are the lucky person this year, everyone has to touch you, right?"
    Leyna "I guess..."
    $ show_picture(9, "puesto6")
    $ resolve_scene()
    WorkersSon "Do you know what brings more lucky?"
    Leyna "W...what?"
    $ show_picture(10, "puesto10")
    $ resolve_scene()
    Johan "This place is beautiful, I love your festivities!"
    Friend "Everyone here is very kind, right? We want you to feel as well as possible"
    $ show_picture(11, "puesto9")
    $ resolve_scene()
    WorkersSon "Touching gently the lucky person. The happier she is, the more luck she will bring to others"
    if switch("ate_the_fruit"):
        $ resolve_scene()
        Leyna "(What is he doing? I don't want to say anything, I wouldn't want to get Johan in trouble)"
        Leyna "(Oh my god, this boy... what is he doing? I can't resist, this fruit has turned me on so much...)"
        $ show_picture(12, "puesto11")
        $ resolve_scene()
        WorkersSon "Do you like it?"
        $ show_picture(13, "puesto12")
        $ resolve_scene()
        Leyna "Y...yes... (If Johan see us.... but I don't really care right now..)"
        $ show_picture(14, "puesto13")
        $ resolve_scene()
        WorkersSon "I want to be lucky for many years, you know?"
        $ show_picture(15, "puesto14")
        $ resolve_scene()
        WorkersSon "And you are so hot, I can't resist my self. I don't usually do this but.."
        $ show_picture(16, "puesto15")
        $ resolve_scene()
        WorkersSon "You are so warm down there.. I want a little of what your husband has"
        $ show_picture(17, "puesto16")
        $ resolve_scene()
        WorkersSon "Oh yes!"
        $ show_picture(20, "puesto17")
        $ resolve_scene()
        Leyna "OHH!!!!!!!!"
        $ show_picture(18, "puesto16")
        $ resolve_scene()
        WorkersSon "SHH! Don't scream. We don't want your husband to see us, right? Just enjoy.."
        $ show_picture(19, "puesto12")
        $ resolve_scene()
        Leyna "Please,do..don't, I love Johan... and..."
        $ show_picture(20, "puesto15")
        $ resolve_scene()
        WorkersSon "I don't doubt it, we are just having a good time"
        $ show_picture(21, "puesto10")
        $ resolve_scene()
        Johan "Well guys, see you over there then.."
        $ show_picture(22, "puesto18")
        $ resolve_scene()
        WorkersSon "Fuck....."
        $ show_picture(23, "puesto19")
        $ resolve_scene()
        WorkersSon "Yeah! See you..."
        Leyna "(Why are they leaving? I was so...)"
        Leyna "Yeah, bye guys.."
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
        $ erase_picture(17)
        $ erase_picture(18)
        $ erase_picture(19)
        $ erase_picture(20)
        $ erase_picture(21)
        $ erase_picture(22)
        $ erase_picture(23)
    if not switch("ate_the_fruit"):
        $ resolve_scene()
        Leyna "(What is he doing? I don't want to say anything, I wouldn't want to get Johan in trouble)"
        $ show_picture(12, "puesto11")
        $ resolve_scene()
        WorkersSon "Do you like it?"
        Leyna "Mmmm... we should stop this.."
        $ show_picture(14, "puesto13")
        $ resolve_scene()
        WorkersSon "I want to be lucky for many years, you know?"
        $ show_picture(15, "puesto14")
        $ resolve_scene()
        WorkersSon "And you are so hot, I can't resist my self. I don't usually do this but.."
        Leyna "Stop now"
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
        call PlaySound("sound", "audio/Blow1.ogg", volume=0.9, no_loop=True) from _call_FestivalEV020_0_PlaySound
        $ resolve_scene()
        call ShowAnimation(1, "FestivalEV020", "FestivalEV020_0") from _call_FestivalEV020_0_ShowAnimation
        pause 0.6
        $ show_picture(21, "puesto10")
        $ resolve_scene()
        Johan "Well guys, see you over there then.."
        $ show_picture(23, "puesto19")
        $ resolve_scene()
        WorkersSon "Yeah! See you..."
        Leyna "Yeah, bye guys (that was close..)"
        $ erase_picture(21)
        $ erase_picture(23)
    $ fade_out()
    call SetEventLocation("FestivalEV020_0", "FestivalHIJOWORKER", 21, 19) from _call_FestivalEV020_0_setloc_2
    call SetEventLocation("FestivalEV020_0", "FestivalFestivalWorkerSon", 23, 15) from _call_FestivalEV020_0_setloc_3
    $ fade_in()
    call Movement("FestivalEV020_0", "player", ["TURN_R"]) from _call_FestivalEV020_0_Movement_1
    $ resolve_scene()
    Johan "Well, what can we do now?"
    Leyna "There is a massage stand near the casino, we should go there"
    $ food_stand = 1
    call GalleryViewed("puesto") from _call_FestivalEV020_0_GalleryViewed
    if switch("ate_the_fruit"):
        $ corruption = corruption + 5
    $ resolve_scene()
    return False

label FestivalFoodStand(play_event = True, trigger = None): # event
    if is_erased("FestivalFoodStand"):
        return None
    elif food_stand >= 1:
        return None
    elif trigger == "event" and switch("festival_photos"):
        call PlayEvent(play_event, "FestivalFoodStand_0", "FestivalFoodStand") from _call_FestivalFoodStand_0_PlayEvent
        return (0, "", "FestivalFoodStand_0")
    return None

label FestivalNPCTourist_1:
    Tourist "Have you seen my wife Alexa? A few minutes ago she separated from me to go eat something, but I can't see her anywhere"
    Leyna "..."
    Johan "No, I'm sorry"
    return False

label FestivalNPCTourist_2:
    Tourist "Have you seen my wife Alexa? A few minutes ago she separated from me to go eat something, but I can't see her anywhere"
    Leyna "No, I'm sorry (Alexa, what are you doing now? your poor boyfriend... I wish I was brave enough to say something to him...)"
    return False

label FestivalNPCTourist(play_event = True, trigger = None): # event
    if is_erased("FestivalNPCTourist"):
        return None
    elif trigger == "event" and switch("introduction") and johan_dream >= 3:
        call PlayEvent(play_event, "FestivalNPCTourist_2", "FestivalNPCTourist") from _call_FestivalNPCTourist_2_PlayEvent
        return (1, "", "FestivalNPCTourist_2")
    elif trigger == "event" and switch("introduction") and johan_dream >= 3:
        call PlayEvent(play_event, "FestivalNPCTourist_1", "FestivalNPCTourist") from _call_FestivalNPCTourist_1_PlayEvent
        return (1, "", "FestivalNPCTourist_1")
    return None

label FestivalPhotoSession_0:
    Johan "Hey.. Leyna, you were very sexy yesterday at the photoshoot.."
    Leyna "Oh... thanks (Why does he say that so suddenly?)"
    Johan "And I had thought ..."
    Leyna "Yes?"
    Johan "...why don't we do our own photo session? I would like to have pictures of you ... sexy pictures"
    Leyna "Oh! hahaha... Okay, why not? but.. not here,right? I-in front of everyone..."
    Johan "Oh! no! Not here... let's go to a secluded place"
    $ fade_out()
    $ show_picture(1, "festivalfotos1")
    $ fade_in()
    $ resolve_scene()
    Leyna "Here, what do you think?.. I don't see anyone around"
    Johan "Yeah... I think it's perfect"
    $ show_picture(2, "festivalfotos2")
    $ resolve_scene()
    Leyna "Okay.. let's start then!"
    Johan "Okay, stay like that for a second, I want a cute photo"
    Leyna "Hahaha"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_FestivalPhotoSession_0_PlaySound
    pause
    $ show_picture(3, "festivalfotos3")
    $ resolve_scene()
    Leyna "Like this?"
    Johan "Great... you're so beautiful"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_FestivalPhotoSession_0_PlaySound_1
    pause
    $ show_picture(4, "festivalfotos4")
    $ resolve_scene()
    Johan "Nice..."
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_FestivalPhotoSession_0_PlaySound_2
    pause
    $ show_picture(5, "festivalfotos5")
    $ resolve_scene()
    Leyna "Look... take a photo now"
    Johan "Wow... so sexy..."
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_FestivalPhotoSession_0_PlaySound_3
    pause
    $ show_picture(6, "festivalfotos6")
    $ resolve_scene()
    Leyna "Do you like it?"
    Johan "I love it..."
    Johan "I'm getting hard"
    $ flash_screen([255,255,255,170], 60, True)
    call PlaySound("sound", "audio/Key.ogg", volume=0.9, no_loop=True) from _call_FestivalPhotoSession_0_PlaySound_4
    pause
    $ show_picture(7, "festivalfotos7")
    $ resolve_scene()
    Leyna "Now is when the good part begins"
    Johan "I'm looking forward to it"
    $ show_picture(8, "festivalfotos8")
    $ resolve_scene()
    DrunkVillager "YyeaaH Me toO!"
    Johan "Hey! What are you doing? This is not a good time pal!"
    DrunkVillager "hEy! I'm Not tHe onEe dOinG tHis In puBlIc"
    Johan "No, but you are naked in public!"
    $ show_picture(9, "festivalfotos9")
    $ resolve_scene()
    DrunkVillager "HaVe yoOu ForGoTtenn WhEre You arRre?? ThiSs Is tHe FESTIVal PAL! anD I Ccan Do wHat I WanT"
    DrunkVillager "You, bEauTifUl, Are tHe LuCky pErSonN, rRiGht?"
    if switch("ate_the_fruit"):
        $ show_picture(10, "festivalfotos10")
        $ resolve_scene()
        Leyna "(His huge cock is so close to me... Why is it so hard for me to control myself?)"
        Leyna "Yes..."
        DrunkVillager "lEt Me ToUcH YOU tHEn, I waAnt GoOd LuCk LIke EveRyoNe eLsE"
        Leyna "Oke.."
        Johan "Hey! Stop this!"
        Johan "I told you it isn't a good time friend, you are very drunk, leave us alone!"
        Johan "Leyna, get up we're leaving"
        $ show_picture(11, "festivalfotos11")
        $ resolve_scene()
        Leyna "Ye-yeah"
        DrunkVillager "Oook sTaY WitH All ThE lUcK, GrEeDy BoY"
        Johan "Yeah yeah..."
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
        call TransferPlayer("Festival", "FestivalPhotoSession_0", 18, 18, direction=8) from _call_FestivalPhotoSession_0_TransferPlayer
        $ fade_in()
        call Movement("FestivalPhotoSession_0", "player", ["U","U","U","TURN_D"]) from _call_FestivalPhotoSession_0_Movement
        $ resolve_scene()
        Johan "Moron!"
        Leyna "Don't worry, we'll have more chances to do it"
        Johan "... Yeah... you're right"
        Leyna "(Why I'm so horny?, at another time this situation would have scared me, but now ...)"
        Leyna "Let's eat something? I've seen a very delicious food stand"
        Johan "Yeah! I'm starving"
        $ set_switch("festival_photos", True)
        call GalleryViewed("festivalfotos") from _call_FestivalPhotoSession_0_GalleryViewed
    if not switch("ate_the_fruit"):
        Leyna "What?"
        DrunkVillager "lEt Me ToUcH YOU tHEn, I waAnt GoOd LuCk LIke EveRyoNe eLsE"
        Johan "Hey! Stop this!"
        Johan "I told you it isn't a good time friend, you are very drunk, leave us alone!"
        Johan "Leyna, get up we're leaving"
        $ show_picture(11, "festivalfotos11")
        $ resolve_scene()
        Leyna "Ye-yeah"
        DrunkVillager "Oook sTaY WitH All ThE lUcK, GrEeDy BoY"
        Johan "Yeah yeah..."
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
        $ erase_picture(11)
        call TransferPlayer("Festival", "FestivalPhotoSession_0", 18, 18, direction=8) from _call_FestivalPhotoSession_0_TransferPlayer_1
        $ fade_in()
        call Movement("FestivalPhotoSession_0", "player", ["U","U","U","TURN_D"]) from _call_FestivalPhotoSession_0_Movement_1
        $ resolve_scene()
        Johan "Moron!"
        Leyna "Don't worry, we'll have more chances to do it"
        Johan "... Yeah... you're right"
        Leyna "Let's eat something? I've seen a very delicious food stand"
        Johan "Yeah! I'm starving"
        $ set_switch("festival_photos", True)
        call GalleryViewed("festivalfotos") from _call_FestivalPhotoSession_0_GalleryViewed_1
    if switch("ate_the_fruit"):
        $ corruption = corruption + 2
    $ resolve_scene()
    return False

label FestivalPhotoSession(play_event = True, trigger = None): # event
    if is_erased("FestivalPhotoSession"):
        return None
    elif switch("festival_photos"):
        return None
    elif trigger == "event" and switch("lucky_person"):
        call PlayEvent(play_event, "FestivalPhotoSession_0", "FestivalPhotoSession") from _call_FestivalPhotoSession_0_PlayEvent
        return (0, "", "FestivalPhotoSession_0")
    return None

label FestivalMassageParlor_0:
    Leyna "A massage? wait. I want to see the festival a little more before going, I'm sure that after the massage I'll want to go to rest a little"
    Johan "Yeah, you're right"
    return False

label FestivalMassageParlor_1:
    call PlaySound("sound", "audio/Open1.ogg", volume=0.9, no_loop=True) from _call_FestivalEV023_1_PlaySound
    call Movement("FestivalEV023_1", "FestivalEV023", ["TURN_L",["WAIT",3],"TURN_R",["WAIT",3],"TURN_U","THROUGH_ON"]) from _call_FestivalEV023_1_Movement
    call Movement("FestivalEV023_1", "player", ["FORWARD"]) from _call_FestivalEV023_1_Movement_1
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_FestivalEV023_1_PlaySound_1
    call TransferPlayer("MassageParlor", "FestivalEV023_1", 7, 12, direction=0) from _call_FestivalEV023_1_TransferPlayer
    $ resolve_scene()
    return False

label FestivalMassageParlor_2:
    Leyna "W-we don't need to go back in there"
    return False

label FestivalMassageParlor_3:
    "Closed"
    return False

label FestivalMassageParlor(play_event = True, trigger = None): # event
    if is_erased("FestivalMassageParlor"):
        return None
    elif trigger == "event" and switch("johan_and_leyna_sex"):
        call PlayEvent(play_event, "FestivalMassageParlor_3", "FestivalMassageParlor") from _call_FestivalMassageParlor_3_PlayEvent
        return (1, "", "FestivalMassageParlor_3")
    elif trigger == "event" and (switch("massage_masturbation") or switch("massage_sex")):
        call PlayEvent(play_event, "FestivalMassageParlor_2", "FestivalMassageParlor") from _call_FestivalMassageParlor_2_PlayEvent
        return (1, "", "FestivalMassageParlor_2")
    elif trigger == "event" and food_stand >= 1:
        call PlayEvent(play_event, "FestivalMassageParlor_1", "FestivalMassageParlor") from _call_FestivalMassageParlor_1_PlayEvent
        return (1, "", "FestivalMassageParlor_1")
    elif trigger == "event" and switch("festival"):
        call PlayEvent(play_event, "FestivalMassageParlor_0", "FestivalMassageParlor") from _call_FestivalMassageParlor_0_PlayEvent
        return (1, "", "FestivalMassageParlor_0")
    return None

label FestivalAaahhhOooooohHarder_v2_0:
    Alexa "AAAhhh!! OOOOooh!!! HARDER!"
    Villager "YES!"
    $ resolve_scene()
    Johan "Hahahaha oh shit! someone is having a good time back there"
    Johan "Better not disturb them"
    call Movement("FestivalEV026_0", "player", ["L"]) from _call_FestivalEV026_0_Movement
    $ resolve_scene()
    return False

label FestivalAaahhhOooooohHarder_v2(play_event = True, trigger = None): # event
    if is_erased("FestivalAaahhhOooooohHarder_v2"):
        return None
    elif butt_plug >= 3:
        return None
    elif trigger == "event" and johan_dream >= 3:
        call PlayEvent(play_event, "FestivalAaahhhOooooohHarder_v2_0", "FestivalAaahhhOooooohHarder_v2") from _call_FestivalAaahhhOooooohHarder_v2_0_PlayEvent
        return (1, "", "FestivalAaahhhOooooohHarder_v2_0")
    return None

label Festivaliniciacionadolescencia_0(menu_choice = None):
    call Movement("Festivaliniciacionadolescencia_0", "player", ["D","D","D"]) from _call_Festivaliniciacionadolescencia_0_Movement
    $ resolve_scene()
    call PauseForBalloon("Festivaliniciacionadolescencia_0") from _call_Festivaliniciacionadolescencia_0_PauseForBalloon
    Worker "Great to see you guys, you're just in time!"
    Johan "Just in time? for what?"
    Worker "Today a couple of the town's kids are coming of age and will be going through the rite of adulthood"
    Johan "Rite of adulthood? Sounds interesting, are we allowed to see it?"
    Worker "Of course! you are more than welcome! although you will probably have to participate in one way or another"
    Leyna "Participate?"
    Worker "Yes, relax! it will be any silly game, don't worry!"
    Johan "Exactly Leyna, don't worry, it's also a golden opportunity to see another tradition of the town"
    Leyna "Yeah..."
    $ fade_out()
    $ show_picture(1, "ritual1")
    $ fade_in()
    $ resolve_scene()
    OldMan "Good morning townspeople and guests!"
    OldMan "Today we are gathered here to welcome these three young men into adulthood!"
    $ show_picture(2, "ritual2")
    if bottle_event == 3:
        $ resolve_scene()
        Leyna "Oh! ( those are the guys we drank with the other day!)"
    $ resolve_scene()
    OldMan "As tradition dictates, the ritual will be divided into two parts, you know how it goes!"
    OldMan "We need three women to step forward!"
    $ show_picture(3, "ritual3")
    $ resolve_scene()
    "Woman: Well, I guess it's our turn this year...."
    OldMan "Hmmmm great but we are missing one! You Miss step forward without fear"
    $ show_picture(4, "ritual4")
    $ resolve_scene()
    Leyna "M-me? But... I don't know if..."
    OldMan "Relax, We know you're just visiting, but you don't have to worry, it's a ritual... you don't want to offend our traditions, do you?"
    Leyna "NO! no of course..."
    $ show_picture(5, "ritual5")
    $ resolve_scene()
    Johan "Leyna honey don't worry I'll be here at all times"
    Leyna "Yes, of course..."
    $ show_picture(6, "ritual6")
    $ resolve_scene()
    OldMan "Well, let the women get in front of the guys!"
    OldMan "Hand out the infusions to all participants"
    Leyna "Infusions?"
    OldMan "Oh yes! infusions made with the fruit that grows in these forests"
    if switch("ate_the_fruit"):
        $ resolve_scene()
        Leyna "(That damn fruit again... I shouldn't be drinking that I know what kind of effect it has on the body)"
        Leyna "(But I don't want to disrespect all these people either)"
    if not switch("ate_the_fruit"):
        Leyna "(That fruit they talk so much about... well, what could go wrong?)"
    $ show_picture(7, "ritual7")
    $ resolve_scene()
    call GetChoice([_("Drink the infusion"), _("Pretend to drink")], value=menu_choice, called_from="Festivaliniciacionadolescencia_0") from _call_Festivaliniciacionadolescencia_0_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Drink the infusion"):
        $ menu_choice = None
        $ set_switch("infusion", True)
    elif menu_choice == _("Pretend to drink"):
        $ menu_choice = None
    $ show_picture(8, "ritual8")
    $ resolve_scene()
    Leyna "...."
    $ show_picture(9, "ritual9")
    $ resolve_scene()
    OldMan "Very good! now comes the first test, this one is for the boys!"
    OldMan "Every man has to prove that he can protect his beloved so lift her up in the air and show your strength to the other guys!"
    $ show_picture(10, "ritual10")
    $ resolve_scene()
    "Joven: UUoo!! "
    Leyna "Oh!"
    $ show_picture(11, "ritual14")
    $ resolve_scene()
    Villager "How lucky are this year's boys! what beautiful women"
    Villager2 "Hey watch what you say, there's my wife!"
    Villager "I'm sorry, but with the lack of women in this town..."
    Johan "(...)"
    $ show_picture(12, "ritual11")
    $ resolve_scene()
    OldMan "Hang in there guys! hang in there!"
    OldMan "All right, girls, look your young men in the face, remember them, you will need that later on!"
    $ show_picture(13, "ritual12")
    $ resolve_scene()
    OldMan "You know what's coming next! the second test! the youngsters will have to hide in the town and their respective beloved will have to find them"
    OldMan "Once they have found them, they will have to give them the test of maturity and that's..."
    $ show_picture(14, "ritual13")
    $ resolve_scene()
    Leyna "(The test of maturity? I hope he's not just saying ...)"
    OldMan "A kiss!"
    $ show_picture(15, "ritual12")
    $ resolve_scene()
    Leyna "Oh... (a kiss? well... it's no big deal, just a kiss on the cheek)"
    OldMan "Well, let the kids run and hide in the village!"
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
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    $ fade_in()
    $ resolve_scene()
    OldMan "And now girls! look for them!"
    Leyna "(well let's get this over with, I'm hungry)"
    $ fade_out()
    $ erase_picture(1)
    call TransferPlayer("Town2", "Festivaliniciacionadolescencia_0", 1, 21, direction=6) from _call_Festivaliniciacionadolescencia_0_TransferPlayer
    call ChangePartyMember("Johan", False) from _call_Festivaliniciacionadolescencia_0_ChangePartyMember
    $ fade_in()
    $ set_switch("find_youth", True)
    call GalleryViewed("ritual") from _call_Festivaliniciacionadolescencia_0_GalleryViewed
    $ resolve_scene()
    Leyna "Well... let's find that young man and give him the damn kiss"
    return False

label Festivaliniciacionadolescencia_2:
    call PauseForBalloon("Festivaliniciacionadolescencia_2") from _call_Festivaliniciacionadolescencia_2_PauseForBalloon
    call Movement("Festivaliniciacionadolescencia_2", "Festivaljohan", ["L"]) from _call_Festivaliniciacionadolescencia_2_Movement
    call Movement("Festivaliniciacionadolescencia_2", "player", ["TURN_R"]) from _call_Festivaliniciacionadolescencia_2_Movement_1
    $ resolve_scene()
    Johan "Leyna! How did the ritual go?"
    Leyna "....Good...."
    Johan "??? Are you ok?"
    Leyna "Yes... let's take a walk"
    $ fade_out()
    call ChangePartyMember("Johan", True) from _call_Festivaliniciacionadolescencia_2_ChangePartyMember
    $ ritual = 2
    $ fade_in()
    $ resolve_scene()
    return False

label Festivaliniciacionadolescencia(play_event = True, trigger = None): # autorun
    if is_erased("Festivaliniciacionadolescencia"):
        return None
    elif ritual >= 2:
        return None
    elif trigger == "autorun" and ritual >= 1:
        call PlayEvent(play_event, "Festivaliniciacionadolescencia_2", "Festivaliniciacionadolescencia") from _call_Festivaliniciacionadolescencia_2_PlayEvent
        return (0, "", "Festivaliniciacionadolescencia_2")
    elif switch("find_youth"):
        return None
    elif trigger == "autorun" and leyna_work >= 11:
        call PlayEvent(play_event, "Festivaliniciacionadolescencia_0", "Festivaliniciacionadolescencia") from _call_Festivaliniciacionadolescencia_0_PlayEvent
        return (0, "", "Festivaliniciacionadolescencia_0")
    return None

label FestivalButtPlugEvent_1(menu_choice = None):
    $ show_picture(1, "analcomida1")
    $ resolve_scene()
    Leyna "Hello sir, what do you need?"
    "Fat Villager: (WOw who is this girl? I was expecting the same guy as always) Ehm yeah, a beer and some marinated meat thanks"
    Leyna "Coming!"
    $ show_picture(2, "analcomida2")
    $ resolve_scene()
    Villager "Isn't that your wife?"
    Johan "Yes, it looks like she has already started working, don't tell her that we have already had a beer at the other stall or she will get angry"
    Villager "Hahahahaha easy, I've got your back"
    Johan "Well, let's have a drink with her"
    $ show_picture(3, "analcomida3")
    $ resolve_scene()
    Leyna "Oh Hi honey, have you been here long?"
    Johan "Hahaha no no no, we just got here ten minutes ago, just walking around"
    Leyna "Great, shall I put something on?"
    $ show_picture(4, "analcomida4")
    $ resolve_scene()
    Villager2 "Wow isn't that Leyna? I didn't know she was working at the food stall"
    Villager2 "Mother of God, is that the uniform they make her wear? She's practically naked! From here I can see practically everything!"
    $ show_picture(5, "analcomida5")
    $ resolve_scene()
    Villager2 "Wait a second... she's wearing a butt plug? Fuck!"
    Villager2 "I knew she was a bit of a slut, but to be dressed like that with a butt plug up your ass in public?"
    Villager2 "Just looking at it is making my dick hard"
    Villager2 "Although I have an idea... I should take advantage of this, besides, she has done it for a reason, right? I'm sure she's hoping that someone notices it"
    Villager2 "Yes, I'm going to make my move"
    pause
    $ show_picture(6, "analcomida6")
    $ resolve_scene()
    Leyna "AH!"
    Villager2 "Hey! what's up leyna? the boss told me to come and help you"
    Leyna "The boss?"
    Villager2 "Exactly, he told me that you probably need some help since you are new to all this"
    Leyna "I-I see"
    pause
    $ show_picture(7, "analcomida7")
    $ resolve_scene()
    Villager2 "Yeah... let's see what we have here?"
    Leyna "I-is touching the .... the guy is playing with my ass while Johan is there in front)"
    Leyna "(Whispering) What the hell are you doing? My husband is right here"
    $ show_picture(8, "analcomida8")
    $ resolve_scene()
    Villager2 "(Whispering) Come on, you've come out in public like this in front of everyone, you're asking for someone to help you with this right?"
    Villager2 "(whispering) Well, I have the balls to do it, and I don't give a damn if your husband is in front of me"
    Leyna "You..."
    Villager2 "Well guys, what can I put here?"
    Johan "I see you have a craft beer, right?"
    Villager2 "That's right, you want a pair?"
    Johan "Yes, thank you very much"
    Villager2 "Okay, I'm going to look for them, they should be down here"
    "..."
    Leyna "!!! (The bastard pulled out my butt plug! What the hell is he doing?)"
    Leyna "!!!!"
    $ show_picture(9, "analcomida9")
    $ resolve_scene()
    Leyna "Hmm! ah (H-he's eating my ass! in front of Johan and these guys!)"
    Leyna "(Don't they see it?... no... they are not seeing it...)"
    Leyna "(My God, why does it feel so good?)"
    pause
    $ show_picture(10, "analcomida10")
    $ resolve_scene()
    Johan "???"
    Johan "What's wrong? Where are the beers?"
    Leyna "AH! n-nothing"
    Leyna "The boss must have moved them or something (how long is he going to keep this up?...my god)"
    $ show_picture(11, "analcomida11")
    call PlaySound("sound", "audio/Equip2.ogg", volume=0.9, no_loop=True) from _call_FestivalButtPlugEvent_1_PlaySound
    $ resolve_scene()
    Leyna "AH!!"
    Johan "!!!!"
    Villager "Wow, I certainly didn't expect that"
    Leyna "I-I'm mmm s-sorry guys it slipped and... ahh... I'll put it on right away"
    pause
    $ show_picture(12, "analcomida12")
    $ resolve_scene()
    Villager "No rush, take as much time as you need hahahahaha"
    Johan "Dude stop looking!"
    Villager "I'm sorry, I can't help it... my God, what a pair of tits your wife has!"
    Johan "For the love of God I'm right here"
    pause
    $ show_picture(13, "analcomida13")
    $ resolve_scene()
    Villager2 "Sorry guys, here are the beers"
    Leyna "(My God, thank goodness it's over, a little more and I wouldn't know how to hide anymore... wait)"
    Leyna "(When he took out his dick?... and he's pressing it  against my ass... he won't attempt to...)"
    Villager2 "Sorry Leyna I'm going to clean up the counter a little bit"
    Leyna "!!!"
    pause
    $ show_picture(14, "analcomida14")
    $ resolve_scene()
    Leyna "(I-I can't pull away he's holding me too tight and squeezing me against him)"
    Villager2 "The rag is over here, isn't it? It's just that everything is a bit dirty..."
    pause
    $ show_picture(15, "analcomida15")
    $ resolve_scene()
    Leyna "!!!! mmm"
    Villager2 "Where did he put the rag? your boss is a disaster hehehehehe"
    Leyna "(Whispering) Don't even think about it... hmmm ah... don't do that"
    Villager2 "(whispering) I'm sorry but I can't help it...I'll be discreet, don't worry"
    Johan "??? What's the matter?"
    Villager2 "Oh hahaha nothing relax, the owner is a disaster and keeps changing everything around"
    Johan "Hahahahaha I see, but the beer is very good"
    Villager2 "hahaha I see... it's our specialty"
    Leyna "(Is Johan blind? is he really not noticing anything?)"
    if switch("corruption_average"):
        $ resolve_scene()
        call GetChoice([_("resist"), _("it feels so good...")], value=menu_choice, called_from="FestivalButtPlugEvent_1") from _call_FestivalButtPlugEvent_1_GetChoice
        $ menu_choice = _return
        if menu_choice == _("resist"):
            $ menu_choice = None
            $ resolve_scene()
            Leyna "(No! I can't let him do this to me in front of Johan! ... no matter how much I want to.... I have to control myself)"
            Villager "(Ooooh the tip is already in... it's so hot) I'm going to fuck your tight asshole"
            $ show_picture(16, "analalter3", width=814, height=625)
            $ resolve_scene()
            Villager "AAH!"
            Johan "!!!!"
            Villager2 "!!!! Dude, are you okay?"
            $ show_picture(17, "analalter4", width=814, height=625)
            $ resolve_scene()
            Villager "Y-yeah, I'm fine, just a little cramp in my leg that's all"
            Johan "I see, working in the service sector is very hard..."
            $ show_picture(18, "analalter5", width=814, height=625)
            $ resolve_scene()
            Villager "You're telling me (this bitch...)"
        elif menu_choice == _("it feels so good..."):
            $ menu_choice = None
            $ show_picture(16, "analcomida16")
            $ resolve_scene()
            Leyna "!!!!! (He has put it in me! It's in!)"
            Villager2 "(Whispering) Wow you must have been dilated down there and it went in really well.... uff feels like paradise...."
            pause
            $ show_picture(17, "analcomida17")
            $ resolve_scene()
            Leyna "(He's sticking it all the way up my ass and they're all less than a meter away from me.... they're talking so quietly while this guy is fucking my ass)"
            Leyna "(Johan's right in front of me... right there... and I'm getting my asshole drilled by a guy with a huge dick... my god... my god...)"
            Leyna "(I can't take it anymore... I can't take it anymore... !!!!)"
            pause
            $ flash_screen([255,255,255,170], 60, True)
            $ flash_screen([255,255,255,170], 60, True)
            $ show_picture(18, "analcomida18")
            $ resolve_scene()
            $ flash_screen([255,255,255,170], 60, True)
            Leyna "AAAhh!!!"
            Johan "Leyna?! Are you ok?!"
            Villager "Wow something is going on with her for sure..."
            Johan "Leyna, what's wrong?"
            pause
            $ show_picture(19, "analcomida19")
            $ resolve_scene()
            Villager2 "Oh! it's a cramp, don't worry, I'm a physiotherapist, I'll fix it right away, it's just that she' been in the wrong posture for a long time"
            Villager2 "Look, I hold his arms like this and with a couple of movements she will feel much better"
            call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_FestivalButtPlugEvent_1_PlaySound_1
            $ show_picture(20, "analcomida20")
            $ resolve_scene()
            Leyna "Oh oh ooooh!!"
            Villager2 "Yes, that seems to be where it hurts! UFf is hard for me... what a tense back!"
            Johan "It does look like she' s feeling a bit of relief..."
            Villager "Hey, you could give me another one later, I am also very tense from work"
            pause
            $ flash_screen([255,255,255,170], 60, True)
            stop bgs fadeout 1
            $ show_picture(21, "analcomida21")
            $ resolve_scene()
            $ flash_screen([255,255,255,170], 60, True)
            Villager2 "AAAh! now... now you should be much better...Right Leyna? are you feeling better?"
            pause
            $ show_picture(22, "analcomida22")
            $ resolve_scene()
            Leyna "I-I... I... I... yes... I feel better..."
            Leyna "(the son of a bitch leaves me halfway through...)"
            Leyna "(First I let some teenagers blackmail me because I couldn't control myself, then I let them do all kinds of things to me in the bar and now this...)"
            Leyna "(I don't know what kind of person I'm becoming, but it's getting harder to control myself)"
            Leyna "You can let me go... thank you very much..."
            Villager2 "Great! Well, I should get going... I think the boss told me..."
            pause
            $ show_picture(23, "analcomida23")
            $ resolve_scene()
            Leyna "(whispering) after what you've done to me in front of everyone you might as well stay and help me the rest of the shift you son of a bitch"
            Leyna "(whispering) or would you rather I talk to the police right now?"
            Villager2 "!!! (Fuck that' s scary...) Of course... I'll stay as long as it takes..."
            $ set_switch("corruption_maximum", True)
    if switch("corruption_low"):
        $ resolve_scene()
        call GetChoice([_("resist"), _("it feels so good...")], value=menu_choice, called_from="FestivalButtPlugEvent_1") from _call_FestivalButtPlugEvent_1_GetChoice_1
        $ menu_choice = _return
        if menu_choice == _("resist"):
            $ menu_choice = None
            $ resolve_scene()
            Leyna "(No! I can't let him do this to me in front of Johan! ... no matter how much I want to.... I have to control myself)"
            Villager "(Ooooh the tip is already in... it's so hot) I'm going to fuck your tight asshole"
            $ show_picture(16, "analalter3", width=814, height=625)
            $ resolve_scene()
            Villager "AAH!"
            Johan "!!!!"
            Villager2 "!!!! Dude, are you okay?"
            $ show_picture(17, "analalter4", width=814, height=625)
            $ resolve_scene()
            Villager "Y-yeah, I'm fine, just a little cramp in my leg that's all"
            Johan "I see, working in the service sector is very hard..."
            $ show_picture(18, "analalter5", width=814, height=625)
            $ resolve_scene()
            Villager "You're telling me (this bitch...)"
        elif menu_choice == _("it feels so good..."):
            $ menu_choice = None
            $ show_picture(16, "analcomida16")
            $ resolve_scene()
            Leyna "!!!!! (He has put it in me! It's in!)"
            Villager2 "(Whispering) Wow you must have been dilated down there and it went in really well.... uff feels like paradise...."
            pause
            $ show_picture(17, "analcomida17")
            $ resolve_scene()
            Leyna "(He's sticking it all the way up my ass and they're all less than a meter away from me.... they're talking so quietly while this guy is fucking my ass)"
            Leyna "(Johan's right in front of me... right there... and I'm getting my asshole drilled by a guy with a huge dick... my god... my god...)"
            Leyna "(I can't take it anymore... I can't take it anymore... !!!!)"
            pause
            $ flash_screen([255,255,255,170], 60, True)
            $ flash_screen([255,255,255,170], 60, True)
            $ show_picture(18, "analcomida18")
            $ resolve_scene()
            $ flash_screen([255,255,255,170], 60, True)
            Leyna "AAAhh!!!"
            Johan "Leyna?! Are you ok?!"
            Villager "Wow something is going on with her for sure..."
            Johan "Leyna, what's wrong?"
            pause
            $ show_picture(19, "analcomida19")
            $ resolve_scene()
            Villager2 "Oh! it's a cramp, don't worry, I'm a physiotherapist, I'll fix it right away, it's just that she' been in the wrong posture for a long time"
            Villager2 "Look, I hold his arms like this and with a couple of movements she will feel much better"
            call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_FestivalButtPlugEvent_1_PlaySound_2
            $ show_picture(20, "analcomida20")
            $ resolve_scene()
            Leyna "Oh oh ooooh!!"
            Villager2 "Yes, that seems to be where it hurts! UFf is hard for me... what a tense back!"
            Johan "It does look like she' s feeling a bit of relief..."
            Villager "Hey, you could give me another one later, I am also very tense from work"
            pause
            $ flash_screen([255,255,255,170], 60, True)
            stop bgs fadeout 1
            $ show_picture(21, "analcomida21")
            $ resolve_scene()
            $ flash_screen([255,255,255,170], 60, True)
            Villager2 "AAAh! now... now you should be much better...Right Leyna? are you feeling better?"
            pause
            $ show_picture(22, "analcomida22")
            $ resolve_scene()
            Leyna "I-I... I... I... yes... I feel better..."
            Leyna "(the son of a bitch leaves me halfway through...)"
            Leyna "You can let me go... thank you very much..."
            Villager2 "Great! Well, I should get going... I think the boss told me..."
            pause
            $ show_picture(23, "analcomida23")
            $ resolve_scene()
            Leyna "(whispering) after what you've done to me in front of everyone you might as well stay and help me the rest of the shift you son of a bitch"
            Leyna "(whispering) or would you rather I talk to the police right now?"
            Villager2 "!!! (Fuck that' s scary...) Of course... I'll stay as long as it takes..."
            $ set_switch("corruption_maximum", True)
    $ show_picture(24, "analcomida24")
    $ resolve_scene()
    Leyna "Well guys... I see you've already finished your beers, would you like one more round?"
    Johan "Yes please! after this scary moment, I need to relax with another round"
    Leyna "Hahahahaha, coming right up"
    $ fade_out()
    $ butt_plug = 4
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
    $ erase_picture(17)
    $ erase_picture(18)
    $ erase_picture(19)
    $ erase_picture(20)
    $ erase_picture(21)
    $ erase_picture(22)
    $ erase_picture(23)
    $ erase_picture(24)
    call TransferPlayer("Festival", "FestivalButtPlugEvent_1", 16, 2, direction=2) from _call_FestivalButtPlugEvent_1_TransferPlayer
    $ resolve_scene()
    $ tint_screen((68, -34, -34, 0), 60, True)
    $ fade_in()
    call PlaySound("sound", "audio/Crow.ogg", volume=0.9, no_loop=True) from _call_FestivalButtPlugEvent_1_PlaySound_3
    $ resolve_scene()
    Leyna "Well, it's getting late, the other stalls are opening for the party tonight, we should be closing"
    Villager "Yes... (in the end she made me work for hours ... well I'm still in time to take revenge )"
    $ show_picture(1, "analalter1", width=814, height=625)
    $ resolve_scene()
    Villager "Here, I'll give you back what I took from you before"
    Leyna "!!!!!!!"
    $ show_picture(2, "analalter2", width=814, height=625)
    $ resolve_scene()
    Leyna "OOoh!!!"
    Leyna "You..."
    Villager "I see you're still pretty sensitive down there hahahahahaha"
    Villager "Well, I'm going now, if you need me to relieve yourself, look for me, I'll be around here"
    Leyna "Not in your wildest dreams..."
    Villager "Well... your words and your actions don't match, honey"
    Leyna "Shu-shut up"
    $ fade_out()
    $ erase_picture(1)
    $ erase_picture(2)
    $ fade_in()
    $ resolve_scene()
    Leyna "Well... I've finished what I had to do, time to look for Johan, he should be here at the festival"
    $ fade_out()
    call TransferPlayer("FestivalNight", "FestivalButtPlugEvent_1", 12, 5, direction=2) from _call_FestivalButtPlugEvent_1_TransferPlayer_1
    $ fade_in()
    $ resolve_scene()
    $ tint_screen((-68, -68, 0, 68), 60, True)
    Leyna "It seems that many of the food stall workers have not yet arrived"
    Leyna "I'm sure Johan is having a drink with his new friends, better go find him quickly before he drinks too much"
    Leyna "Shit, I can't go dressed like this, can I? and less so with this stuff stuffed in the back"
    Leyna "I should go back and change now that I have the opportunity"
    call GalleryViewed("analcomida") from _call_FestivalButtPlugEvent_1_GalleryViewed
    return False

label FestivalButtPlugEvent(play_event = True, trigger = None): # event
    if is_erased("FestivalButtPlugEvent"):
        return None
    elif butt_plug >= 4:
        return None
    elif trigger == "event" and butt_plug >= 3:
        call PlayEvent(play_event, "FestivalButtPlugEvent_1", "FestivalButtPlugEvent") from _call_FestivalButtPlugEvent_1_PlayEvent
        return (1, "", "FestivalButtPlugEvent_1")
    return None

