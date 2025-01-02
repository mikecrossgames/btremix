label Innposadero_0:
    pause 0.38
    Johan "Hi, I have a room booked in the name of Johan"
    show plano_mujer_general:
        xsize 1600
        ysize 900
    Innkeeper "(..what the fuck?)"
    "(who's that goddess? All women who were worth it in this damn town, have long since left..)"
    hide plano_mujer_general
    show plano_de_frente:
        xsize 1600
        ysize 900
    "(look at the size of those tits!)"
    pause
    hide plano_de_frente
    Johan "emm... hello?"
    Innkeeper "ah, yes! Good morning, room in the name of Johan? Yes, we have it ready."
    "Have you come for the summer festival?"
    Johan "Yes, I work for a magazine and I'm going to write an article about the traditions of this town and its festivities."
    Innkeeper "oh! Great, that will help us get more people to come. If you want, later I can tell you some emblematic places to visit"
    Leyna "Great, thank you very much sir"
    Innkeeper "No worries, you can talk to me when you finish unpacking your things"
    pause 0.26
    show plano_de_espaldas:
        xsize 1600
        ysize 900
    "(damn!)"
    hide plano_de_espaldas
    $ set_switch("innkeeper", True)
    return

label Innposadero_1:
    if suitcases == 0:
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
        show plano_mujer_sorpresa_lado:
            xsize 1600
            ysize 900
        Leyna "Naked?!"
        Innkeeper "Yes ... although.. being an outsider and a woman like you, I think they will allow an exception, but with these religious things you never know"
        show plano_mujer_timida:
            xsize 1600
            ysize 900
        Leyna "Right..."
        hide plano_mujer_sorpresa_lado
        hide plano_mujer_timida
        Innkeeper "Well, if you want to find out a bit about the festival and traditions of the town, ask around before getting into any misunderstanding."
        Johan "Great, thanks for your help."
        $ set_switch("suitcases", False)
        $ set_switch("inn_departure", True)
    return

label Innposadero_3:
    Johan "Hello! I think a package has arrived for me?"
    Innkeeper "Right... Johan right? here you go"
    Johan "Thank you very much! have a nice evening"
    Innkeeper "Yeah, same here... (Not as good as yours buying that kind of stuff... with the wife he's got, lucky motherfucker)"
    pause 0.26
    call SetPlayerLocation("InnRooms") from _call_Innposadero_3_SetPlayerLocation
    pause 0.24
    Johan "Well... I'm going to open it, I can't help it anymore"
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    pause 0.2
    Johan "So this is it... a butt plug... according to what I have read Leyna should wear it for a while before... well... that so that she would be prepared..."
    Johan "Hehehehehe great! I can't wait! I've been wanting to do something like this with Leyna for a long time...."
    Johan "Wait a minute... it comes with an instruction manual? How complicated does it have to be?"
    Johan "\"with this toy your wife will be looking forward to it when you get home from work\" hahahaha Great"
    Johan "\"Using our traditional techniques in...\" What the hell? I was right, they make it in this town...."
    Johan "\"We use a traditional blend of aphrodisiac herbs that will greatly intensify your partner's desire and arousal...\""
    Johan "they sure are fans here of the damn herbs... but hey... if it works I have nothing to complain about... now I just have to find Leyna"
    Johan "And see how she likes the idea... now that I think about it she should be here, where has she gone this time?"
    $ butt_plug = 2
    return

label InnSueojohanpart2_0:
    pause 0.28
    Johan "Leyna?"
    pause 0.2
    pause 0.22
    Leyna "Good morning ... are you okay?"
    Johan "Yeah... I'm okey"
    Leyna "Great! Are we going to the festival? It should be open already"
    Johan "Hmm? The festival? Yeah yeah right... Let's go"
    scene black with dissolve
    $ johan_dream = 2
    call SetPlayerLocation("Town2") from _call_InnSueojohanpart2_0_SetPlayerLocation
    # fade in
    return

label Inninicionochefiesta_0:
    pause 0.28
    Johan "Oh I almost forgot, several of the guys in town have told me that there're parties all over town tonight"
    Johan "And I was thinking if you feel like it, we could go out tonight,you know, have some dinner and a drink together"
    Johan "It's been a while since we've partied together like we used to"
    show expresion_gui_o_lengua
    Leyna "Sure, I'd love to! Now that you mention it, that's a good excuse to get dressed up. I have a little surprise for you that I brought from the apartment.."
    Johan "Oh! Now you've got me intrigued! I'm looking forward to seeing it"
    Leyna "Wait for me down here and I'll get ready"
    Johan "Sure, I'll be right here"
    scene black with dissolve
    hide expresion_gui_o_lengua
    call SetPlayerLocation("InnNight") from _call_Inninicionochefiesta_0_SetPlayerLocation
    # fade in
    pause 0.2
    Johan "Fuck, it's taking forever! What's she doing?"
    Leyna "Hi handsome... What do you think?"
    scene cambioropa
    Johan "WOW! You look gorgeous... wait, those clothes...."
    Leyna "Do you remember? I used to go out dressed like this when we were younger and partying around"
    Johan "Yes! Yes I remember... wow, you look beautiful... Now I feel bad to be dressed like this"
    Johan "Anyway, wow, I didn't remember it so revealing.."
    Leyna "Yeah... but I know you like to show off your wife, so it's okay, right?"
    Johan "Of course, I can't wait to show off my woman. Let's go for a walk around town and grab some dinner!"
    scene black with dissolve
    hide cambioropa
    call SetPlayerLocation("TownFestivalNight") from _call_Inninicionochefiesta_0_SetPlayerLocation_1
    # fade in
    pause 0.24
    $ ritual = 3
    return

label InneventoJohanyalexa_0:
    scene pantallanegro:
        xsize 979
        ysize 720
    "Meanwhile Johan was on his way to continue his work"
    call SetPlayerLocation("Path") from _call_InneventoJohanyalexa_0_SetPlayerLocation
    hide pantallanegro
    pause 0.2
    Johan "At the end I got nervous at the bar watching Leyna surrounded by men and being semi naked...."
    Johan "I've also drank more beer than I should..."
    Johan "... Anyway, let's finish with this interview and I'll be back with Leyna..."
    Johan "And tonight we could..."
    if johan_leyna_sex == 1:
        $ flash_screen(wait=True)
        scene fotoerotica8
        Johan "Shit, again...I can't help it...every time I think about fucking with Leyna these images come to my mind"
        hide fotoerotica8
    if johan_leyna_sex == 2:
        scene johanfollar9
        Johan "Hehehehehe that was good.... well tonight we'll see"
        hide johanfollar9
    Johan "Anyway, enough of this nonsense... I should go to the festival. I'm meeting the mayor for the interview"
    scene black with dissolve
    call SetPlayerLocation("Festival") from _call_InneventoJohanyalexa_0_SetPlayerLocation_1
    # fade in
    pause 0.28
    pause 0.2
    scene johanxalexa1
    Johan "Damn it... I've been waiting for half an hour already ..."
    Johan "And while I was waiting, I couldn't help but drink one of those infusions they make in this town"
    Johan "The guy who offered it to me has been very annoying"
    Johan "Now, in addition to being drunk, I feel very strange"
    scene johanxalexa2
    Alexa "Helloooo Johan..."
    Johan "!!!"
    scene johanxalexa3
    Alexa "What are you doing here alone Johaaaan?"
    Johan "(Wow, she's so close! she's touching me with her breasts)"
    Johan "(she looks like she's drunk or something... this girl never acts normal but today she's even weirder than ever...)"
    scene johanxalexa4
    Alexa "I don't know if it's the infusion or what... but today you're very attractive Johan..."
    Johan "O-oh? really? i uhmm.... thank you"
    Alexa "Why don't you come a little closer to me and give me a kiss?"
    Johan "I-I don't... (How good Alexa smells... I hadn't noticed but she is very pretty)"
    Alexa "Come on, come here, what's the problem?"
    Johan "I-I can't do that... you know I'm married"
    Alexa "Well..."
    scene johanxalexa5
    Johan "!!!!"
    Alexa "You're telling me no, but this one here is telling me yes..."
    Johan "Sto-stop..."
    Alexa "Oooh? how shy Johan"
    scene johanxalexa6
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    Alexa "Look how hard it is... that's for me?... you like me that much?"
    Johan "We shouldn't... anyone can see us... (I'm having trouble thinking clearly... what's happening to me? I want to fuck her with all my will)"
    Johan "But I can't do it, Leyna is my wife and she's perfect! besides... anyone could see us!)"
    Alexa "Come with me... let's go to a more private place..."
    Johan "I..."
    menu:
        "Go with Alexa":
            Johan "C-Come on..."
            scene black with dissolve
            show johanxalexa7 with dissolve
            Alexa "Here no one will see us, come on man, we are going to have a good time"
            Johan "(God... am I really doing this?...I can't believe it... this all seems like a hallucination)"
            scene johanxalexa8
            Alexa "That's it, it's almost in... fuck me"
            Johan "Ohhh you are so warm...."
            Johan "I'm going to fuck you like you've never been fucked before..."
            Alexa "Well, don't make me wait any longer"
            scene johanxalexa9
            play bgs "audio/audio follar.ogg" loop volume 0.9
            Alexa "Yes! like this! go on, don't stop"
            Johan "Ah ah ah!!!"
            Alexa "Keep fucking me like that!"
            pause
            scene johanxalexa10
            play bgs "audio/audio follar.ogg" loop volume 0.9
            Alexa "That's it, break me in half..."
            Alexa "Fuck me hard... anyone could see us at any time Johan ... do you like that?"
            Johan "Ah ah ah ah, yes, I love it, let them see us while I fuck you, I don't care!"
            Alexa "Aaaah I love it!"
            pause
            scene johanxalexa11
            play bgs "audio/audio follar.ogg" loop volume 0.9
            Johan "AH! I am about to..."
            Alexa "Keep fucking me hard Johan!"
            Alexa "Fuck me like the whore I am!!!"
            Johan "AH AH AH I'm going to cum!"
            Alexa "Cum inside my Johan, use me like a tissue"
            Johan "ah ahaaah!!"
            $ flash_screen(wait=True)
            scene johanxalexa12
            $ flash_screen(wait=True)
            stop bgs fadeout 1
            Johan "Aaaaaahhh...."
            Alexa "Very good Johan... that's the way I like it..."
            Johan "ah ah ah (WHAT THE HELL HAVE I DONE?)"
            Johan "(I have to get out of here right now... I'm getting dizzy)"
            Alexa "Shall we have a drink? I'm thirsty"
            Johan "I-I can't, I have to go to work"
            Alexa "Work?...I see"
            scene black with dissolve
            hide johanxalexa12
            call SetPlayerLocation("Town2") from _call_InneventoJohanyalexa_0_SetPlayerLocation_2
            show pantallanegro with dissolve:
                xsize 979
                ysize 720
            "The next day..."
            Leyna "Where did Johan go? he didn't wake me up when he left this morning"
            $ bar_work = 2
            Leyna "I don't have time to worry about that I should go to work at the bar"
        "No":
            Johan "N-no, I can't do it, I'm married, s-sorry"
            Alexa "Oh come on, wait don't leave"
            Johan "I'm sorry..."
            scene black with dissolve
            hide pantallanegro
            call SetPlayerLocation("Path") from _call_InneventoJohanyalexa_0_SetPlayerLocation_3
            # fade in
            pause 0.28
            pause 0.2
            Johan "that was a close call..."
            Johan "I should go back to the inn..."
            scene pantallanegro:
                xsize 979
                ysize 720
            call SetPlayerLocation("Town2") from _call_InneventoJohanyalexa_0_SetPlayerLocation_4
            "The next day..."
            hide pantallanegro
            Leyna "Well... one more day! Johan has already left to continue with his interviews... I should go to work at the bar now"
            $ bar_work = 2
    return

label InnToInn_0:
    scene black with dissolve
    call SetPlayerLocation("Inn") from _call_InnEV016_0_SetPlayerLocation
    # fade in
    pause 0.2
    Johan "Hey Leyna, good morning..."
    pause 0.2
    pause 0.24
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
    scene black with dissolve
    $ set_switch("breakfast", True)
    pause 0.26
    call SetPlayerLocation("Town2") from _call_InnEV016_0_SetPlayerLocation_1
    # fade in
    return

