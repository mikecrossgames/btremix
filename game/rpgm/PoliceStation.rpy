label PoliceStationeventocomisaria_0:
    call ShowAnimation(1, "player", "PoliceStationeventocomisaria_0") from _call_PoliceStationeventocomisaria_0_ShowAnimation
    Leyna "Hey!!"
    play music "audio/Dungeon1.ogg" loop volume 0.9
    $ show_picture(1, "carcel1")
    Johan "Leyna!"
    Johan "Somebody help us!!"
    $ show_picture(2, "carcel2")
    Policeman "Shit... I told you not to go near the cell"
    Prisoner "What a fine woman you've brought me"
    Johan "Get away from my wife right now"
    Prisoner "I don't think so ... I haven't fucked a woman as pretty as you in years, darling"
    Prisoner "Let me see those tits"
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    $ show_picture(3, "carcel3")
    Johan "YOU SON OF A BITCH LET HER GO!"
    Johan "Are you not going to do anything?"
    Policeman "Wait, as soon as we get the chance we'll release your wife"
    Prisoner "Are you getting horny with this, bitch?"
    Leyna "Please let me go!"
    Prisoner "Nah, let me touch your pussy and see if you're wet"
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    $ show_picture(4, "carcel4")
    Leyna "NO! PLEASE!"
    Johan "STOP!"
    Policeman "(I have to stop it but ... what a good view!)"
    Prisoner "God damn! You're sexy as fuck, girl"
    Prisoner "Since you are showing me everything, let me show you mine"
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    $ show_picture(5, "carcel5")
    Prisoner "You're very hot down there, can you really be getting horny with this? You are a whore!"
    Leyna "Shu-shut up!"
    Johan "!!!"
    Prisoner "I can't wait any longer, I have to fuck this pussy right now"
    Leyna "What?!"
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    $ show_picture(6, "carcel6")
    Leyna "NO! STOP!"
    Prisoner "Almost there!"
    Policeman "NOW! Stop him!"
    Prisoner "Hm?"
    scene black with dissolve
    stop music fadeout 1
    $ erase_picture(1)
    $ erase_picture(2)
    $ erase_picture(3)
    $ erase_picture(4)
    $ erase_picture(5)
    $ erase_picture(6)
    # TransferPlayer: "PoliceStation"
    hide black with dissolve
    call ShowAnimation(1, "PoliceStationprisionero", "PoliceStationeventocomisaria_0") from _call_PoliceStationeventocomisaria_0_ShowAnimation_1
    PoliceCaptain "My sincere apologies for this, but in this way you will learn that you should not get back to approach a prisoner"
    Johan "Are you talking seriously? something very serious could have happened, they should put better bars in the cell"
    Leyna "Johan... let's go"
    Johan "Yeah..."
    PoliceCaptain "(Douchebag...)"
    Johan "(Dickhead...)"
    scene black with dissolve
    # TransferPlayer: "Town2"
    hide black with dissolve
    pause 0.26
    Johan "Are you okay Leyna?"
    Leyna "I'm ... fine, still shaking a bit from what happened, but fine"
    $ corruption = corruption + 2
    $ jail = 1
    return

