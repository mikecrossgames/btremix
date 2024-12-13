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
    # TransferPlayer: "Town2"
    hide black with dissolve
    return

label Inninicionochefiesta_0:
    pause 0.28
    Johan "Oh I almost forgot, several of the guys in town have told me that there're parties all over town tonight"
    Johan "And I was thinking if you feel like it, we could go out tonight,you know, have some dinner and a drink together"
    Johan "It's been a while since we've partied together like we used to"
    $ show_transparent(1, "expresion_gui_o_lengua")
    Leyna "Sure, I'd love to! Now that you mention it, that's a good excuse to get dressed up. I have a little surprise for you that I brought from the apartment.."
    Johan "Oh! Now you've got me intrigued! I'm looking forward to seeing it"
    Leyna "Wait for me down here and I'll get ready"
    Johan "Sure, I'll be right here"
    scene black with dissolve
    $ erase_picture(1)
    # TransferPlayer: "InnNight"
    hide black with dissolve
    pause 0.2
    Johan "Fuck, it's taking forever! What's she doing?"
    Leyna "Hi handsome... What do you think?"
    $ show_picture(2, "cambioropa")
    Johan "WOW! You look gorgeous... wait, those clothes...."
    Leyna "Do you remember? I used to go out dressed like this when we were younger and partying around"
    Johan "Yes! Yes I remember... wow, you look beautiful... Now I feel bad to be dressed like this"
    Johan "Anyway, wow, I didn't remember it so revealing.."
    Leyna "Yeah... but I know you like to show off your wife, so it's okay, right?"
    Johan "Of course, I can't wait to show off my woman. Let's go for a walk around town and grab some dinner!"
    scene black with dissolve
    $ erase_picture(2)
    # TransferPlayer: "TownFestivalNight"
    hide black with dissolve
    pause 0.24
    $ ritual = 3
    return

label InneventoJohanyalexa_0(menu_choice = None):
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    "Meanwhile Johan was on his way to continue his work"
    # TransferPlayer: "Path"
    $ erase_picture(1)
    pause 0.2
    Johan "At the end I got nervous at the bar watching Leyna surrounded by men and being semi naked...."
    Johan "I've also drank more beer than I should..."
    Johan "... Anyway, let's finish with this interview and I'll be back with Leyna..."
    Johan "And tonight we could..."
    if johan_leyna_sex == 1:
        $ flash_screen([255,255,255,170], 60, True)
        $ show_picture(1, "fotoerotica8")
        Johan "Shit, again...I can't help it...every time I think about fucking with Leyna these images come to my mind"
        $ erase_picture(1)
    if johan_leyna_sex == 2:
        $ show_picture(1, "johanfollar9")
        Johan "Hehehehehe that was good.... well tonight we'll see"
        $ erase_picture(1)
    Johan "Anyway, enough of this nonsense... I should go to the festival. I'm meeting the mayor for the interview"
    scene black with dissolve
    # TransferPlayer: "Festival"
    hide black with dissolve
    pause 0.28
    pause 0.2
    $ show_picture(1, "johanxalexa1")
    Johan "Damn it... I've been waiting for half an hour already ..."
    Johan "And while I was waiting, I couldn't help but drink one of those infusions they make in this town"
    Johan "The guy who offered it to me has been very annoying"
    Johan "Now, in addition to being drunk, I feel very strange"
    $ show_picture(2, "johanxalexa2")
    Alexa "Helloooo Johan..."
    Johan "!!!"
    $ show_picture(3, "johanxalexa3")
    Alexa "What are you doing here alone Johaaaan?"
    Johan "(Wow, she's so close! she's touching me with her breasts)"
    Johan "(she looks like she's drunk or something... this girl never acts normal but today she's even weirder than ever...)"
    $ show_picture(4, "johanxalexa4")
    Alexa "I don't know if it's the infusion or what... but today you're very attractive Johan..."
    Johan "O-oh? really? i uhmm.... thank you"
    Alexa "Why don't you come a little closer to me and give me a kiss?"
    Johan "I-I don't... (How good Alexa smells... I hadn't noticed but she is very pretty)"
    Alexa "Come on, come here, what's the problem?"
    Johan "I-I can't do that... you know I'm married"
    Alexa "Well..."
    $ show_picture(5, "johanxalexa5")
    Johan "!!!!"
    Alexa "You're telling me no, but this one here is telling me yes..."
    Johan "Sto-stop..."
    Alexa "Oooh? how shy Johan"
    $ show_picture(6, "johanxalexa6")
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    Alexa "Look how hard it is... that's for me?... you like me that much?"
    Johan "We shouldn't... anyone can see us... (I'm having trouble thinking clearly... what's happening to me? I want to fuck her with all my will)"
    Johan "But I can't do it, Leyna is my wife and she's perfect! besides... anyone could see us!)"
    Alexa "Come with me... let's go to a more private place..."
    Johan "I..."
    call GetChoice([_("Go with Alexa"), _("No")], value=menu_choice, called_from="InneventoJohanyalexa_0") from _call_InneventoJohanyalexa_0_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Go with Alexa"):
        $ menu_choice = None
        Johan "C-Come on..."
        scene black with dissolve
        $ show_picture(7, "johanxalexa7")
        hide black with dissolve
        Alexa "Here no one will see us, come on man, we are going to have a good time"
        Johan "(God... am I really doing this?...I can't believe it... this all seems like a hallucination)"
        $ show_picture(8, "johanxalexa8")
        Alexa "That's it, it's almost in... fuck me"
        Johan "Ohhh you are so warm...."
        Johan "I'm going to fuck you like you've never been fucked before..."
        Alexa "Well, don't make me wait any longer"
        $ show_picture(9, "johanxalexa9")
        play bgs "audio/audio follar.ogg" loop volume 0.9
        Alexa "Yes! like this! go on, don't stop"
        Johan "Ah ah ah!!!"
        Alexa "Keep fucking me like that!"
        pause
        $ show_picture(10, "johanxalexa10")
        play bgs "audio/audio follar.ogg" loop volume 0.9
        Alexa "That's it, break me in half..."
        Alexa "Fuck me hard... anyone could see us at any time Johan ... do you like that?"
        Johan "Ah ah ah ah, yes, I love it, let them see us while I fuck you, I don't care!"
        Alexa "Aaaah I love it!"
        pause
        $ show_picture(11, "johanxalexa11")
        play bgs "audio/audio follar.ogg" loop volume 0.9
        Johan "AH! I am about to..."
        Alexa "Keep fucking me hard Johan!"
        Alexa "Fuck me like the whore I am!!!"
        Johan "AH AH AH I'm going to cum!"
        Alexa "Cum inside my Johan, use me like a tissue"
        Johan "ah ahaaah!!"
        $ flash_screen([255,255,255,170], 60, True)
        $ show_picture(12, "johanxalexa12")
        $ flash_screen([255,255,255,170], 60, True)
        stop bgs fadeout 1
        Johan "Aaaaaahhh...."
        Alexa "Very good Johan... that's the way I like it..."
        Johan "ah ah ah (WHAT THE HELL HAVE I DONE?)"
        Johan "(I have to get out of here right now... I'm getting dizzy)"
        Alexa "Shall we have a drink? I'm thirsty"
        Johan "I-I can't, I have to go to work"
        Alexa "Work?...I see"
        scene black with dissolve
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
        $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
        $ erase_picture(1)
        # TransferPlayer: "Town2"
        hide black with dissolve
        "The next day..."
        Leyna "Where did Johan go? he didn't wake me up when he left this morning"
        $ bar_work = 2
        Leyna "I don't have time to worry about that I should go to work at the bar"
    elif menu_choice == _("No"):
        $ menu_choice = None
        Johan "N-no, I can't do it, I'm married, s-sorry"
        Alexa "Oh come on, wait don't leave"
        Johan "I'm sorry..."
        scene black with dissolve
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(4)
        $ erase_picture(5)
        $ erase_picture(6)
        # TransferPlayer: "Path"
        hide black with dissolve
        pause 0.28
        pause 0.2
        Johan "that was a close call..."
        Johan "I should go back to the inn..."
        $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
        # TransferPlayer: "Town2"
        "The next day..."
        $ erase_picture(1)
        Leyna "Well... one more day! Johan has already left to continue with his interviews... I should go to work at the bar now"
        $ bar_work = 2
    return

label InnToInn_0:
    scene black with dissolve
    # TransferPlayer: "Inn"
    hide black with dissolve
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
    # TransferPlayer: "Town2"
    hide black with dissolve
    return

