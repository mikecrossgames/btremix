label TownEntranceBG:
    $ set_transparency_backgrounds(["bg_townentrance","darkbg"])
    $ set_map_backgrounds(["bg_townentrance","darkbg"])
    return

label TownEntranceStart:
    call TownEntranceBG from _call_TownEntranceBG
    stop music
    stop bgs
    return

label TownEntranceEnd:
    return

label TownEntranceparadabus_0:
    call ChangePartyMember("Leyna", True) from _call_TownEntranceparadabus_0_ChangePartyMember
    call Movement("TownEntranceparadabus_0", "player", ["R","R","R","R","U","U","TURN_D"]) from _call_TownEntranceparadabus_0_Movement
    $ resolve_scene()
    Johan "Well, we're already here. The place is beautiful, we just have to follow this path and.."
    ".. we'll be in town in a few minutes"
    $ set_switch("introduction", True)
    call Movement("TownEntranceparadabus_0", "player", ["TURN_U","U","U","U"]) from _call_TownEntranceparadabus_0_Movement_1
    call TransferPlayer("Town", "TownEntranceparadabus_0", 21, 49, direction=8) from _call_TownEntranceparadabus_0_TransferPlayer
    $ resolve_scene()
    return False

label TownEntranceparadabus(play_event = True, trigger = None): # autorun
    if is_erased("TownEntranceparadabus"):
        return None
    elif switch("festival_final"):
        return None
    elif trigger == "autorun":
        call PlayEvent(play_event, "TownEntranceparadabus_0", "TownEntranceparadabus") from _call_TownEntranceparadabus_0_PlayEvent
        return (0, "", "TownEntranceparadabus_0")
    return None

label TownEntranceJohanmedia_1(menu_choice = None):
    $ show_picture(1, "ending4")
    $ resolve_scene()
    Leyna "Johan..."
    Johan "Johan?! How could you do this to me!"
    $ show_picture(2, "ending5")
    $ resolve_scene()
    Leyna "I..."
    $ show_picture(3, "ending6")
    $ resolve_scene()
    Johan "You don't need to say anything! This is over Leyna, how am I supposed to live after this?!"
    Johan "How am I supposed to ever trust anyone again after this shit?"
    $ show_picture(4, "ending7")
    $ resolve_scene()
    Leyna "Johan, I really understand you... I don't know how this could have happened... since we arrived to this town..."
    Leyna "Everything has been very strange, things have happened too fast, everything has gotten out of control..."
    $ show_picture(5, "ending8")
    $ resolve_scene()
    Leyna "I'm sure you've felt it too, haven't you? the atmosphere of this town... doesn't let you think clearly..."
    Johan "... And? does it matter? what's done is done! there's no turning back now... after this we can't go on as before"
    $ show_picture(6, "ending9")
    $ resolve_scene()
    Leyna "... Can't we? I still love you Johan... like the first day! and I'm sure you do too... we can..."
    Leyna "We can simply wipe the slate clean... as if this never happened... go home together and move on with our lives"
    Johan "... I... I"
    call GetChoice([_("I will think about it"), _("Don't forgive her")], value=menu_choice, called_from="TownEntranceJohanmedia_1") from _call_TownEntranceJohanmedia_1_GetChoice
    $ menu_choice = _return
    if menu_choice == _("I will think about it"):
        $ menu_choice = None
        $ show_picture(7, "ending10")
        $ resolve_scene()
        Johan "Of course I still love you, Leyna..."
        Leyna "!!!! Then let's go home together"
        Johan "... Yes, but I'll need some time to think about our future... and if I can really forgive you for this"
        Leyna "I... I understand... I will give you as much time as you need"
        Johan "Very well... let's go"
        Leyna "Wait..."
        $ show_picture(8, "ending11")
        $ resolve_scene()
        Johan "!!!"
        $ show_picture(9, "ending12")
        $ resolve_scene()
        pause
        $ show_picture(10, "ending13")
        $ resolve_scene()
        Leyna "Just... don't forget about me... I'll be waiting for you"
        Johan "... Ok"
        $ show_picture(11, "pantallanegro", scale=(120, 120), width=816, height=600)
        $ resolve_scene()
        Johan "(I couldn't help it... I still love her too much to let her go..... Leyna and I got back together after a couple of months)"
        Johan "(Things have improved a lot between us... I guess this crisis helped us to get closer)"
        Johan "(And the truth is that our sex life has improved considerably...)"
        Johan "(The magazine paid me for the article, a large sum of money for helping tourism in the area, now we could live without worries)"
        Johan "(Although Leyna decided to look for a job to entertain herself and help with the domestic economy)"
        Johan "(Everything was going well and we were both able to move forward with the relationship)"
        if johan_leyna_sex == 1:
            $ resolve_scene()
            "Some time later"
            $ show_picture(12, "ending14")
            $ resolve_scene()
            Leyna "Johan!"
            Johan "Yes?"
            $ show_picture(13, "ending15")
            $ resolve_scene()
            Leyna "I'm off to work, see you this afternoon"
            Johan "Okay honey! see you this afternoon!"
            call PlaySound("sound", "audio/Door1.ogg", volume=0.9, no_loop=True) from _call_TownEntranceJohanmedia_1_PlaySound
            $ fade_out()
            $ show_picture(14, "ending16")
            $ fade_in()
            $ resolve_scene()
            Johan "Well... alone at last... I'm going to jerk off"
            Johan "let's see... ooh amateur girl fucked in the subway let's see"
            $ show_picture(15, "cmedia2cont1")
            $ resolve_scene()
            Johan "Wow! great, this is in good quality, finally a good video in the amateur section, most of them are shit"
            Johan "Well let's start!"
            MaleVoice "Wow he's groping her right here in front of everyone!"
            FemaleVoice "What a shame... isn't there any other place where they can do this?"
            pause
            $ show_picture(16, "cmedia2cont2")
            $ resolve_scene()
            MaleVoice "Oh wow, looks like she wanted some action too huh? she's eating his cock in front of everyone"
            FemaleVoice "What are you doing? Are you recording this?"
            MaleVoice "Of course! Do you have a problem?"
            FemaleVoice "...."
            pause
            $ show_picture(17, "cmedia2cont3")
            $ resolve_scene()
            Unknown "Come here bitch, I'm going to fuck you in front of all these people! so they can see what a slut you are!"
            Unknown "Ah... N-no... let's go somewhere else..."
            Unknown "No fucking way"
            FemaleVoice "W-wait... are they really going to do it right here?"
            pause
            $ show_picture(18, "cmedia2cont4")
            $ resolve_scene()
            Unknown "AAhhh god... what a tight pussy you have... your husband doesn't fuck you like he should eh?"
            Unknown "S-shut up.... ah ah ah"
            MaleVoice "He's fucking impaling her! He's got a giant cock!"
            FemaleVoice "M-my god..."
            MaleVoice "Hey... Are you getting horny watching this? If you want we can..."
            FemaleVoice "N-not even in your best dreams pervert... besides I have a boyfriend"
            MaleVoice "Well, I had to try"
            Unknown "Ah ah! G-G-God!!! I-I'm going to cum"
            pause
            $ flash_screen([255,255,255,170], 60, True)
            $ show_picture(19, "cmedia2cont5")
            $ resolve_scene()
            $ flash_screen([255,255,255,170], 60, True)
            Unknown "AAaaahhh! Fuck! I haven't fucked like this for years!"
            Unknown "ah ah ah ah god... look how you have left me.... and ...in front of all these people...."
            call PlaySound("music", "audio/Stay with me .ogg", volume=0.9, no_loop=False) from _call_TownEntranceJohanmedia_1_PlaySound_1
            "it seems that this is not the end of the problems in Johan's life.... "
            call GalleryViewed("cmedia2") from _call_TownEntranceJohanmedia_1_GalleryViewed
            "Leyna seems to be dissatisfied with the current sexual situation between the two of them and has decided to seek satisfaction outside the relationship"
            "And unfortunately Johan doesn't seem to have the slightest idea of what's going on... this is pretty bad, don't you think? "
            "Although looking at it in a different way... "
            "From Johan's point of view he is having a happy life with the woman he loves, I guess he is better off than most people"
            "And Leyna for her part has found what she was missing in this relationship in another place, but she is still with the man she loves... I guess the situation could be much worse"
            "I guess time will tell if this relationship is destined to fail or if they can both make it work"
            "Anyway, this is the end of Bawdy Traditions, I hope you liked this little story, see you soon"
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
            $ erase_picture(17)
            $ erase_picture(18)
            $ erase_picture(19)
            stop music fadeout 1
            stop bgs fadeout 1
            label TownEntranceJohanmedia_1_loop_1:
                if True:
                    jump TownEntranceJohanmedia_1_loop_1_end
                jump TownEntranceJohanmedia_1_loop_1
            label TownEntranceJohanmedia_1_loop_1_end:
                pass
            $ play_video_looped(1, "creditosdavid_webm", "CREDITOSDAVID.webm")
            $ fade_in()
            $ resolve_scene()
            pause
            pause
            $ stop_video(1)
            call ReturnToTitleScreen("TownEntranceJohanmedia_1") from _call_TownEntranceJohanmedia_1_ReturnToTitleScreen
        if johan_leyna_sex == 2:
            $ resolve_scene()
            "Some time later"
            $ show_picture(12, "ending14")
            $ resolve_scene()
            Leyna "Johan!"
            Johan "Yes?"
            $ show_picture(13, "ending15")
            $ resolve_scene()
            Leyna "I'm off to work, see you this afternoon"
            Johan "To work already?"
            Leyna "Yes, today I want to go with some extra time, you never know when public transportation might leave you stranded"
            Johan "... Hmmm"
            $ show_picture(14, "cmedia3cont1")
            $ resolve_scene()
            Johan "Leyna! Wait a second"
            Leyna "Ah? W-what is it?"
            Johan "Oh.. no big deal... why don't you stay a few more minutes?"
            Leyna "Johan... no, I don't want to be late for work, it's my first month and I don't want to start off on the wrong foot"
            Johan "Leyna, come on... it will only take a moment, come on, I know you are also looking forward to it"
            Leyna "Johan..."
            Leyna "Come on... but just a little bit"
            $ fade_out()
            $ show_picture(15, "cmedia3cont2")
            $ fade_in()
            $ resolve_scene()
            Johan "God... as sexy as ever"
            Leyna "S-shut up..."
            Johan "Oooh... I see you're still blushing like a teenage girl hehehe"
            Leyna "Come on... what are you waiting for?"
            pause
            $ show_picture(16, "cmedia3cont3")
            $ resolve_scene()
            Johan "Come on, spread those legs"
            Leyna "Ah..."
            Leyna "W-what are you going to do?"
            Johan "Ssshhh be quiet and enjoy"
            pause
            $ show_picture(17, "cmedia3cont4")
            $ resolve_scene()
            Leyna "Aaaahhh..."
            Johan "(Hehehehe now she will be happy for work)"
            Leyna "M-my god..."
            pause
            $ show_picture(18, "cmedia3cont5")
            $ resolve_scene()
            Leyna "Oh! Fuck! (When did he get so good at... doing this?)"
            Johan "!!!"
            Leyna "Ah ah ah ah..."
            Leyna "F-fuck I'm goin' to c-cum"
            Leyna "Stop... stop!"
            pause
            $ show_picture(19, "cmedia3cont6")
            $ resolve_scene()
            Leyna "Let's go... come here, I don't want to cum yet..."
            Johan "Hehehehe you were not in such a hurry?"
            Leyna "SSshhh... Shut up and come"
            pause
            $ show_picture(20, "cmedia3cont7")
            $ resolve_scene()
            Johan "As you wish, my dear..."
            Leyna "Don't make me wait any longer..."
            pause
            $ show_picture(21, "cmedia3cont8")
            $ resolve_scene()
            Johan "Ufff"
            Leyna "Aahhh..."
            Leyna "Like this... like this, little by little"
            pause
            $ show_picture(22, "cmedia3cont9")
            call PlaySound("bgs", "audio/audio follar.ogg", volume=0.9, no_loop=False) from _call_TownEntranceJohanmedia_1_PlaySound_2
            $ resolve_scene()
            Leyna "Ah ah ah ah"
            Johan "Fuck! you're dripping"
            Leyna "Keep going... my god!"
            Johan "Ah ah ah!!"
            Johan "Shit I-I'm not going to last long"
            Leyna "I'm almost there!!! almost there!!!"
            pause
            $ fade_out()
            $ show_picture(23, "cmedia3cont10")
            stop bgs fadeout 1
            $ fade_in()
            $ resolve_scene()
            "Several minutes later... "
            Leyna "God... you were... really good today"
            Johan "Hahahaha Yeah?..."
            pause
            $ show_picture(24, "cmedia3cont11")
            $ resolve_scene()
            Johan "Well, doing it in the morning gives me more energy. hahaahah"
            Leyna "Don't say it too much or I might start asking you for this every day before I go to work heheheeh"
            Johan "Well, I'll do my best"
            Leyna "hmmm then I'll think about it, see if you can keep up with the pace"
            Johan "Hahahaha I will start training to be able to do it"
            $ fade_out()
            $ show_picture(25, "ending17")
            $ fade_in()
            $ resolve_scene()
            "Moments later... "
            Johan "Aaahhh... what a nice day... now that I have already cashed the article of the magazine at last we can have a break in the economical aspect"
            Johan "What could I do today... hmmm I could go for a walk later and buy something to make dinner for Leyna when she comes back"
            call PlaySound("music", "audio/Stay with me .ogg", volume=0.9, no_loop=False) from _call_TownEntranceJohanmedia_1_PlaySound_3
            "It seems that Johan is having a happy life together with Leyna... Life has given him a wake-up call and he has learned from his previous mistakes"
            call GalleryViewed("cmedia3") from _call_TownEntranceJohanmedia_1_GalleryViewed_1
            "Now he pays more attention to his wife's needs and they both have a full life.... good job Johan"
            "But Johan can't rest on his laurels, he needs to keep working on his relationship and keep treating Leyna as he did in the beginning"
            "Keeping the flame of love intact, they are now a happy couple and have been able to overcome this crisis, further strengthening their love"
            "this is the end of Bawdy Traditions, I hope you liked this little story... see you soon"
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
            $ erase_picture(17)
            $ erase_picture(18)
            $ erase_picture(19)
            $ erase_picture(20)
            $ erase_picture(25)
            stop music fadeout 1
            stop bgs fadeout 1
            label TownEntranceJohanmedia_1_loop_2:
                if True:
                    jump TownEntranceJohanmedia_1_loop_2_end
                jump TownEntranceJohanmedia_1_loop_2
            label TownEntranceJohanmedia_1_loop_2_end:
                pass
            $ play_video_looped(1, "creditosdavid_webm", "CREDITOSDAVID.webm")
            $ fade_in()
            $ resolve_scene()
            pause
            pause
            $ stop_video(1)
            call ReturnToTitleScreen("TownEntranceJohanmedia_1") from _call_TownEntranceJohanmedia_1_ReturnToTitleScreen_1
    elif menu_choice == _("Don't forgive her"):
        $ menu_choice = None
        $ resolve_scene()
        Johan "I... I'm sorry, but right now I can't forgive you for what you've done to me"
        Johan "After this I don't even know how I can trust anyone else...."
        Leyna "B-but Johan after everything we've been through"
        Johan "That's what I say, after everything we've been through! and you do something like that to me! it's over... Leyna it's over!"
        Leyna "... J-johan"
        Johan "Don't talk to me, I don't want to listen to you anymore... see you never again Leyna..."
        Leyna "Johan!"
        $ show_picture(8, "pantallanegro", scale=(120, 120), width=816, height=600)
        call ChangePartyMember("Johan", True) from _call_TownEntranceJohanmedia_1_ChangePartyMember
        call ChangePartyMember("Leyna", False) from _call_TownEntranceJohanmedia_1_ChangePartyMember_1
        call TransferPlayer("ApartmentEnding", "TownEntranceJohanmedia_1", 5, 10, direction=8) from _call_TownEntranceJohanmedia_1_TransferPlayer
        $ resolve_scene()
        "Some time later..."
        $ fade_out()
        $ erase_picture(1)
        $ erase_picture(2)
        $ erase_picture(3)
        $ erase_picture(4)
        $ erase_picture(5)
        $ erase_picture(6)
        $ erase_picture(7)
        $ erase_picture(8)
        $ fade_in()
    $ resolve_scene()
    return False

label TownEntranceJohanmedia(play_event = True, trigger = None): # event
    if is_erased("TownEntranceJohanmedia"):
        return None
    elif trigger == "event" and switch("festival_final") and switch("corruption_average"):
        call PlayEvent(play_event, "TownEntranceJohanmedia_1", "TownEntranceJohanmedia") from _call_TownEntranceJohanmedia_1_PlayEvent
        return (1, "", "TownEntranceJohanmedia_1")
    return None

label TownEntranceJohanAlta_1:
    $ show_picture(1, "ending4")
    $ resolve_scene()
    Leyna "Johan..."
    Johan "Johan?! How could you do this to me!"
    $ show_picture(2, "ending5")
    $ resolve_scene()
    Leyna "I..."
    $ show_picture(3, "ending6")
    $ resolve_scene()
    Johan "You don't need to say anything! This is over Leyna, how am I supposed to live after this?!"
    Johan "How am I supposed to ever trust anyone again after this shit?"
    $ show_picture(4, "ending7")
    $ resolve_scene()
    Leyna "Johan, I really understand you... I don't know how this could have happened... since we arrived to this town..."
    Leyna "Everything has been very strange, things have happened too fast, everything has gotten out of control..."
    $ show_picture(5, "ending8")
    $ resolve_scene()
    Leyna "I'm sure you've felt it too, haven't you? the atmosphere of this town... doesn't let you think clearly..."
    Johan "... And? does it matter? what's done is done! there's no turning back now... after this we can't go on as before"
    $ show_picture(6, "ending9")
    $ resolve_scene()
    Leyna "... Can't we? I still love you Johan... like the first day! and I'm sure you do too... we can..."
    Leyna "We can simply wipe the slate clean... as if this never happened... go home together and move on with our lives"
    Johan "... I... I"
    Johan "I... I'm sorry, but right now I can't forgive you for what you've done to me"
    Johan "After this I don't even know how I can trust anyone else...."
    Leyna "B-but Johan after everything we've been through"
    Johan "That's what I say, after everything we've been through! and you do something like that to me! it's over... Leyna it's over!"
    Leyna "... J-johan"
    Johan "Don't talk to me, I don't want to listen to you anymore... see you never again Leyna..."
    Leyna "Johan!"
    $ show_picture(7, "pantallanegro", scale=(120, 120), width=816, height=600)
    call ChangePartyMember("Johan", True) from _call_TownEntranceJohanAlta_1_ChangePartyMember
    call ChangePartyMember("Leyna", False) from _call_TownEntranceJohanAlta_1_ChangePartyMember_1
    call TransferPlayer("ApartmentEnding", "TownEntranceJohanAlta_1", 5, 10, direction=8) from _call_TownEntranceJohanAlta_1_TransferPlayer
    $ resolve_scene()
    "Some time later..."
    $ fade_out()
    $ erase_picture(1)
    $ erase_picture(2)
    $ erase_picture(3)
    $ erase_picture(4)
    $ erase_picture(5)
    $ erase_picture(6)
    $ erase_picture(7)
    $ fade_in()
    $ resolve_scene()
    return False

label TownEntranceJohanAlta(play_event = True, trigger = None): # event
    if is_erased("TownEntranceJohanAlta"):
        return None
    elif trigger == "event" and switch("festival_final") and switch("corruption_high"):
        call PlayEvent(play_event, "TownEntranceJohanAlta_1", "TownEntranceJohanAlta") from _call_TownEntranceJohanAlta_1_PlayEvent
        return (1, "", "TownEntranceJohanAlta_1")
    return None

label TownEntranceCbajaendingBase:
    call Movement("TownEntranceCbajaending", "player", ["D","D","D"]) from _call_TownEntranceCbajaending_Movement
    call Movement("TownEntranceCbajaending", "player", ["TURN_U"]) from _call_TownEntranceCbajaending_Movement_1
    $ resolve_scene()
    Johan "... Well, that's it, I've finished the article, the only thing left to do is to go back home"
    Leyna "Yeah..."
    Johan "In a way I will miss this town..."
    Leyna "Yes, although not everything in this town has been to my liking, I will miss it too"
    Johan "Yes, it has been an experience that I will never forget, we have gone out of our comfort zone and done things we never thought we would do...."
    Leyna "Especially on the subject of going naked...."
    Johan "Yes..."
    Johan "And the food was good... hehehe"
    Leyna "Yeah, well... let's go back home, I think I need to rest for a couple of days, this experience has been too intense for me hahaha"
    Johan "Yes... Let's go back home"
    $ show_picture(1, "pantallanegro", scale=(120, 120), width=816, height=600)
    call ChangePartyMember("Leyna", False) from _call_TownEntranceCbajaending_ChangePartyMember
    call TransferPlayer("ApartmentGroundFloor", "TownEntranceCbajaending", 6, 4, direction=8) from _call_TownEntranceCbajaending_TransferPlayer
    $ resolve_scene()
    "Several weeks later..."
    $ erase_picture(1)
    $ resolve_scene()
    return False

label TownEntranceCbajaending(play_event = True, trigger = None): # autorun
    if is_erased("TownEntranceCbajaending"):
        return None
    elif trigger == "autorun" and switch("festival_final") and switch("corruption_low"):
        call PlayEvent(play_event, "TownEntranceCbajaendingBase", "TownEntranceCbajaending") from _call_TownEntranceCbajaending_PlayEvent
        return (0, "", "TownEntranceCbajaending")
    return None
