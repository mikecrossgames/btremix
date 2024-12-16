label TownNPCCop_0:
    pause 0.26
    show expresion_ilusion_mujer:
        xsize 1600
        ysize 900
    "OHHH!!"
    Leyna "How beautiful, it looks so medieval"
    hide expresion_ilusion_mujer
    Johan "We should look for the inn and leave the luggage"
    pause 0.34
    Policeman "Good morning couple. I see that you are new in town"
    Johan "Yes, we came to the festival"
    Policeman "On these dates, we receive many tourists, although it's worth visiting the town at any time of the year"
    "Anyway, if you need anything, you can find me here"
    Johan "Since you mention it, can you tell us how to get to the inn?"
    Policeman "Sure, you have to go straight to the end of the town and turn right, there it is!"
    Johan "Okey, thanks"
    $ player_location = "Town"
    pause 0.28
    $ player_location = "Inn"
    return

label TownMerchant_0:
    VillagerMan "COATS! PANTS!. VERY LOW PRICES! WE ARE ALMOST GIVING IT AWAY. SIR, BUY NOW OR REGRET IT LATER"
    VillagerWoman "You wish ... that clothing is rubbish and very expensive..."
    VillagerMan "shut up old witch..."
    VillagerWoman "you shut up, helpless old man"
    return

label TownNPCwoman_2(menu_choice = None):
    Alexa "Do you want to go to the river now?"
    menu:
        "Yes":
            if corruption <= 9:
                Leyna "N.. now? I wanted to take a walk around here before going there again"
                "(YOU NEED 9 POINTS OF CORRUPTION OR MORE TO ENTER THIS EVENT)"
                pause 0.22
            if corruption >= 9:
                Leyna "Now? Okay, why not .."
                Alexa "Great! Let's do this"
                scene black with dissolve
                $ player_location = "River2"
                # fade in
        "No":
            show plano_mujer_timida:
                xsize 1600
                ysize 900
            Leyna "N.. now? I wanted to take a walk around here before going there again"
            hide plano_mujer_timida
            show alexa_gui_o
            Alexa "It's okay. If you change your mind come find me, I'll be here"
            hide alexa_gui_o
            pause 0.22
            $ set_switch("no_return_to_the_river", True)
    return

label Towneventolemetenmanobarrio_0:
    DrunkVillager "Oi! We're told you're doing an article about our traditions!"
    pause 0.22
    Johan "(Wow... I see that in a small town  gossips spread quickly)"
    Johan "That's right, do you want to tell us something?"
    DrunkVillager "Nah, I'm too drunk to have a normal conversation, but I feel extremely handsome today"
    DrunkVillager "Why don't you take some pictures of me and my friend?"
    Johan "Oh, sure!"
    DrunkVillager "What a beautiful woman you have hidden there friend!"
    show expresion_gota
    Johan "What? My wife?"
    DrunkVillager "Is that your wife?.. Really? Wow some are lucky while we.. we are dying of the desire"
    Johan "(Dying of desire? Now he's getting poetic)"
    hide expresion_gota
    Johan "You could say that I'm a very lucky man to have such a beautiful woman as a wife"
    show plano_mujer_sonrisa:
        xsize 1600
        ysize 900
    Leyna "Hahahahaha how romantic!"
    DrunkVillager "Okey come here"
    scene manoseo2
    Johan "HEY!!"
    DrunkVillager "Come on! Don't worry, take a couple of pictures!"
    DrunkVillager "So there will be two beautiful people in the photo, not like my friend here"
    DrunkVillager2 "Fuck you..."
    Johan "I..."
    DrunkVillager "Come on! Look ...."
    scene black with dissolve
    hide manoseo2
    show manoseo_3 with dissolve
    play sound "audio/Jump1.ogg" volume 0.9 noloop
    DrunkVillager "Take a picture now hahahahaha!"
    Johan "KNOCK IT OFF!!!"
    hide manoseo_3
    DrunkVillager "Hahaha okay okay don't be mad it was a joke. We are all partying, relax a little!"
    Johan "Whatever, we are leaving!"
    pause 0.24
    $ set_switch("neighborhood_grope", True)
    $ corruption = corruption + 1
    "CORRUPTION +1"
    return

label TownSkirtLift_0:
    pause 0.22
    Johan "A street market in the center of town, beautiful"
    Leyna "Yes, very joyful. I'm falling in love with this town"
    pause 0.36
    pause 0.32
    Villager "What's up son?"
    show plano_de_espaldas:
        xsize 1600
        ysize 900
    Kid "Look dad, what a beautiful girl!"
    Villager "Yeah. A tourist that probably has come for the festival..."
    hide plano_de_espaldas
    Villager "...but I don't think she will go in as soon as she sees the requirements. After all, most of the women in this town have left for a reason..."
    Kid "And what if i prank her, dad?"
    Villager "A prank?"
    Kid "Yeah, I can lift her skirt and run away hahaha"
    Villager "(Oh! ... No, I shouldn't ... but ... sorry son. I'm turning you into a savage, but that woman has a gorgeous body!)"
    Villager "Hahahaha I see... yes!, it's a good idea son, very ... funny!"
    Kid "Alright then...!"
    scene black with dissolve
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    $ set_switch("lifted_skirt", True)
    show levantamiento_de_falda_1 with dissolve:
        xsize 1104
        ysize 621
    Villager "(!!!!)"
    pause
    hide levantamiento_de_falda_1
    show levantamiento_falda_2:
        xsize 1104
        ysize 621
    Leyna "Oh?"
    Villager "(DAMN, HE DID IT!)"
    pause
    scene black with dissolve
    hide levantamiento_falda_2
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    # fade in
    Johan "Damn kids ..."
    Leyna "Well, don't be angry Johan, it's a silly joke"
    $ corruption = corruption + 1
    "CORRUPTION +1"
    return

label Townfinaldelprimerdia_0:
    Leyna "Johan wait..."
    pause 0.22
    Johan "Is something wrong ?"
    Leyna "No no, nothing's wrong but... It has been a very long day and with the trip and the interviews I'm tired..."
    "Can we go back to the hotel and go to sleep?"
    Johan "Oh of course"
    $ player_location = "InnRooms"
    pause 0.34
    scene black with dissolve
    if not renpy.in_rollback():
        $ _saved_bgm = renpy.music.get_playing()
    play music "audio/Inn.ogg" volume 0.9 noloop
    if _saved_bgm is not None and not renpy.in_rollback():
        queue music _saved_bgm
        $ _saved_bgm = None
    $ player_location = "Inn"
    # fade in
    pause 0.28
    Johan "Leyna, today I'm going to the town hall to interview the mayor and talk to some public employees..."
    "..if you want, take advantage of the day and take a walk around the town, you know ... relax and meet some friendly villagers"
    "I've been told the hot springs are already open, in case you wanna take a relaxing bath"
    Leyna "Well... yes, you're right. I think I need a day to relax a little. See you here in the afternoon?"
    Johan "Yeah perfect! See you later"
    scene black with dissolve
    $ player_location = "Town"
    # fade in
    pause 0.24
    show plano_mujer_sonrisa:
        xsize 1600
        ysize 900
    Leyna "A day for myself ..."
    hide plano_mujer_sonrisa
    $ set_switch("leyna_alone", True)
    return

label Townfotografo_1:
    if not switch("hot_springs_first_visit"):
        OldMan "The magazine loved the pictures, give me time to prepare things so we can do the second session"
        "On the meantime maybe you could visit the hot springs, which are on the west of the town"
    if switch("hot_springs_first_visit"):
        OldMan "I have almost everything ready, can you go to the clothing store and pick up the package of lingerie that the fashion magazine sent me?"
        Leyna "Okey!"
        $ set_switch("pick_up_package", True)
    return

label Townfotografo_3:
    Leyna "Sir, I have the package"
    play sound "audio/Recovery.ogg" volume 0.9 noloop
    $ item_clothes = False
    OldMan "Perfect, the second session is going to be a little different from the first"
    OldMan "My grandson is a young man with an impressive physique and I don't want him to stay the rest of his days in this town."
    OldMan "So I'm helping him and I'd like to introduce him to the world of modelling"
    show plano_mujer_cartoon:
        xsize 1600
        ysize 900
    Leyna "That's... sweet i suppose"
    OldMan "Hahaha, well that's why I asked him to pose with you this time"
    Leyna "With me?..."
    OldMan "Yeah, I was thinking of doing something a little more artistic, the boy will go with the traditional clothes and you with lingerie from the magazine"
    OldMan "If that's okay with you, of course"
    hide plano_mujer_cartoon
    Leyna "Well yes, why not?"
    OldMan "Great! Let's go there"
    $ player_location = "Photoshoot2"
    return

label Towneventofotografiaintro_0(menu_choice = None):
    if switch("photo_not_taken"):
        OldMan "Have you changed your mind?"
        menu:
            "Yes":
                Leyna "Well.. I've some free time and a little extra money won't hurt me.. Sure, I'm interested"
                OldMan "Perfect, come with me to my house, that's where I have the photo studio.."
                scene black with dissolve
                $ player_location = "PhotographersHouse"
                # fade in
            "No":
                Leyna "I'm sorry, I'm not interested right now..."
                OldMan "Oh it's fine, if you change your mind I'll be here"
                pause 0.26
    if not switch("photo_not_taken"):
        OldMan "Excuse me miss, you aren't from this town, right?"
        show expresion_neutral_mujer:
            xsize 1600
            ysize 900
        Leyna "No, I'm writing an article with my husband."
        OldMan "I see... You've come to see the festival, I'm the town's photographer"
        "You know.. basically passport photo, ID photos and a few weddings around here..."
        "... it's strange to see such a beautiful woman in this town"
        show plano_mujer_sonrisa:
            xsize 1600
            ysize 900
        hide expresion_neutral_mujer
        Leyna "Hahaha, thank you very much"
        OldMan "Would you mind if I ask you something? Would you be interested in doing a job?"
        show plano_mujer_sorpresa_lado:
            xsize 1600
            ysize 900
        hide plano_mujer_sonrisa
        Leyna "A job?... What is it about?"
        OldMan "You see.. with passport photos I cannot earn a living.."
        ".. I recently got a job online for a lingerie magazine, I've already been paid and they sent me the clothes to do a photoshoot .."
        "... the problem is my wife doesn't want to pose for me (and she is not as attractive as you)"
        "Would you be interested in doing a session with me? I would pay you for this job, of course"
        menu:
            "Yes":
                Leyna "Well.. I've some free time and a little extra money won't hurt me.. Sure, I'm interested"
                OldMan "Perfect, come with me to my house, that's where I have the photo studio.."
                scene black with dissolve
                hide plano_mujer_sorpresa_lado
                $ player_location = "PhotographersHouse"
                # fade in
            "No":
                Leyna "I'm sorry, I'm not interested right now..."
                OldMan "Oh it's fine, if you change your mind I'll be here"
                pause 0.26
        $ set_switch("photo_not_taken", True)
    return

label TownMeetAlexa_0(menu_choice = None):
    pause 0.22
    TouristWoman "Don't be mad, it was silly"
    Tourist "I thought it would be good for us to come on this trip, but I start to think that it wasn't a good idea"
    TouristWoman "You don't have to worry, we've come to enjoy with our friends. You don't need to watch over me all the time"
    Tourist "But .. there are many men here and I .."
    TouristWoman "We have already talked about that, you know it was a mistake and it won't happen again. Try to enjoy this vacation"
    Tourist "I know, but I don't trust those villagers."
    "Sorry I distrusted you honey. I'm going back to the inn to apologize for my earlier behaviour"
    pause 0.28
    scene black with dissolve
    play sound "audio/Move1.ogg" volume 0.9 noloop
    # fade in
    pause 0.30
    pause 0.22
    show plano_mujer_cerca:
        xsize 1600
        ysize 900
    Leyna "Hello, are you okay? I thought you were arguing .."
    hide plano_mujer_cerca
    show alexa_timida
    TouristWoman "It's all good, thanks. He's my husband, sometimes he gets a little jealous, and there are many men here..."
    hide alexa_timida
    show plano_mujer_sonrisa:
        xsize 1600
        ysize 900
    Leyna "Yeah.. (You're telling me!) By the way, I haven't introduced myself, my name is Leyna"
    "I came with my husband to photograph the festival"
    hide plano_mujer_sonrisa
    show alexa_neutral
    TouristWoman "Nice to meet you, my name is Alexa and I've come to save my marriage .."
    hide alexa_neutral
    show plano_mujer_ojos_blanco_negro:
        xsize 1600
        ysize 900
    "hahahaha.. Just kidding, we're sightseeing"
    hide plano_mujer_ojos_blanco_negro
    show plano_mujer_sonrisa:
        xsize 1600
        ysize 900
    Leyna "Hahaha.. Okey"
    "I'm alone today and I was taking a walk around the area. I was told that there are hot springs around here"
    hide plano_mujer_sonrisa
    show alexa_gui_o
    Alexa "Yes, we've already gone. They are a great place to relax ... but I prefer the river"
    hide alexa_gui_o
    show plano_mujer_timida:
        xsize 1600
        ysize 900
    Leyna "The river? But .. everyone goes naked there, don't you feel ashamed?"
    hide plano_mujer_timida
    show alexa_gui_o
    Alexa "No way! We are all born naked, there is nothing to be ashamed of"
    hide alexa_gui_o
    show plano_mujer_sorpresa_lado:
        xsize 1600
        ysize 900
    Leyna "Yeah well .."
    Alexa "Don't be ashamed, you have a beautiful body, surely the men around here have their eyes on you hahaha"
    hide plano_mujer_sorpresa_lado
    show plano_mujer_timida:
        xsize 1600
        ysize 900
    Leyna "The thing is that I travel with my husband and it's a bit violent to go somewhere like that with him ..."
    hide plano_mujer_timida
    show alexa_timida
    Alexa "Look, if you want we can go together and so we protect each other"
    hide alexa_timida
    show expresion_ilusion_mujer:
        xsize 1600
        ysize 900
    Leyna "Sure, it would be great to go together!"
    hide expresion_ilusion_mujer
    "Do you want to go to the river with Alexa now?"
    menu:
        "Yes":
            if corruption <= 9:
                Leyna "N.. now? I wanted to take a walk around here before going there again"
                "(YOU NEED 9 POINTS OF CORRUPTION OR MORE TO ENTER THIS EVENT)"
                pause 0.22
                pause 0.24
                $ set_switch("no_return_to_the_river", True)
            if corruption >= 9:
                Leyna "Now? Okay, why not .."
                Alexa "Great! Let's do this"
                scene black with dissolve
                $ player_location = "River2"
                # fade in
        "No":
            show plano_mujer_timida:
                xsize 1600
                ysize 900
            Leyna "N.. now? I wanted to take a walk around here before going there again"
            hide plano_mujer_timida
            show alexa_gui_o
            Alexa "It's okay. If you change your mind come find me, I'll be here"
            hide alexa_gui_o
            pause 0.22
            pause 0.24
            $ set_switch("no_return_to_the_river", True)
    return

