label Receptionrecepcion_2:
    Receptionist "Hi honey, how can I help you?"
    show plano_mujer_sorpresa_lado:
        xsize 1600
        ysize 900
    Leyna "Hi! See, the people in town told me that you need a receptionist for these days and I'm looking a part-time job.."
    Receptionist "Ahhh! Thank goodness you came. I'm very busy with the festival and I would not like to have to close these days, with so many customers"
    Receptionist "I'm looking for someone to cover for me while during the event. You would only have to attend to the people and have the place clean, prepare towels... well"
    "There are several things I would have to teach you first, if you are interested, of course"
    hide plano_mujer_sorpresa_lado
    show plano_mujer_sonrisa:
        xsize 1600
        ysize 900
    Leyna "Of course!"
    Receptionist "You see, people come here to relax. It always smells good and the atmosphere is warm, I put in the water some plants that grow near the festival"
    Receptionist "You know, the flowers of the fruit that is usually taken...  at the festival hehehe.."
    hide plano_mujer_sonrisa
    Leyna "I see..."
    if switch("ate_the_fruit"):
        show expresion_gota
        Leyna "(damn fruit)..."
        hide expresion_gota
    Receptionist "I've run out and would need you to get a few to show you how I prepare hotsprings for people"
    Receptionist "Come see me when you have the flowers, you can get them in a field that is close to the festival"
    Leyna "That's done, I'll be right back"
    $ leyna_work = 4
    return

label Receptionrecepcion_4:
    Receptionist "You already have the flowers?"
    Leyna "Yes, here they are!"
    play sound "audio/Recovery.ogg" volume 0.9 noloop
    $ item_flowers = False
    Receptionist "Well, then let's see what the work consists of"
    scene black with dissolve
    call SetPlayerLocation("HotSpringsBathroom") from _call_Receptionrecepcion_4_SetPlayerLocation
    # fade in
    return

label Receptioneventohotsprings_0:
    pause 0.22
    show plano_mujer_sonrisa:
        xsize 1600
        ysize 900
    Leyna "Hello,  I've been told that the hot springs are already open"
    Receptionist "Yes, we were closed for renovations"
    Leyna "Great! So can I come in?"
    Receptionist "Yes, on my left you have the women's wardrobe. There you have clean towels, when you finish you can leave it in the basket and we will take care of it"
    hide plano_mujer_sonrisa
    show expresion_ilusion_mujer:
        xsize 1600
        ysize 900
    Leyna "Cool, it's been years since I've come to a place like this"
    Receptionist "Enjoy!"
    hide expresion_ilusion_mujer
    pause 0.44
    scene black with dissolve
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    pause 0.6
    call SetPlayerLocation("HotSpringsBathroom") from _call_Receptioneventohotsprings_0_SetPlayerLocation
    # fade in
    pause 0.24
    Leyna "There's nobody, I have the place for myself!"
    scene black with dissolve
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    pause 0.6
    call SetPlayerLocation("HotSpringsBathroom") from _call_Receptioneventohotsprings_0_SetPlayerLocation_1
    # fade in
    pause 0.6
    Leyna "Aaah... good... and the water is perfect how relaxing!"
    scene black with dissolve
    play sound "audio/Liquid.ogg" volume 0.9 noloop
    pause 0.6
    show onsen1 with dissolve
    "(5 MINUTES LATER...)"
    Leyna "I'm soooo chill right now..."
    Leyna "I could fall asleep here, but I don't have to abuse either. I can get dizzy from the heat.."
    Leyna "Well... closing my eyes for a few minutes won't hurt"
    scene black with dissolve
    hide onsen1
    call SetPlayerLocation("HotSprings") from _call_Receptioneventohotsprings_0_SetPlayerLocation_2
    # fade in
    return

label ReceptionDamn_0:
    pause 0.2
    Leyna "Damn..."
    scene trabajo1
    Leyna "Is this serious? What a uniform... this is too provocative, she goes with normal clothes.. Why do I have to put on this kind of clothing?"
    Leyna "You can see everything ..."
    WomansVoice "Leyna? what are you doing here?"
    scene trabajo2
    Leyna "???"
    Leyna "(I can't believe she's here without her husband, well, it was to be expected)"
    scene trabajo3
    Leyna "Wow Alexa, I didn't expect to see you here... alone"
    Leyna "You know that the hotsprings are mixed, right?"
    Alexa "I know..."
    Alexa "My husband is with the friends who accompany us in the trip and I didn't want to be alone"
    scene trabajo4
    Leyna "I see... although you never stay alone for long..."
    Alexa "I like to be accompanied, what can I say... hehehe"
    scene trabajo5
    Alexa "Well... and you? What are you doing here alone?"
    Leyna "I've started working here today so I will prepare your bath, I hope you enjoy it"
    Alexa "I'm sure I will hehehe"
    scene black with dissolve
    show trabajo6 with dissolve
    "A FEW MOMENTS LATER"
    Leyna "Alexa? I leave you here a few dry towe..."
    scene trabajo7
    Leyna "(what's going on here? where did these people come from?... I can't believe it, doing this in public again)"
    scene trabajo8
    Alexa "Right there, you're going to break me in half"
    Villager "What a dirty bitch"
    scene trabajo9
    Leyna "(They don't worry that somebody can see them? somebody could enter at any moment)"
    scene trabajo10
    Alexa "Fuck me, come on!"
    Villager2 "This bitch is crazy"
    Villager "I know... It's great, we have to take advantage of this unique opportunity in life, dude"
    Alexa "we don't have much time, fuck me before someone comes"
    scene trabajo11
    Leyna "(I... am I getting turned on? by this? What kind of person I' m becoming?)"
    scene trabajo12
    play bgs "audio/audio follar.ogg" loop volume 0.9
    Villager "Do you like it bitch?"
    Alexa "I love it! FUCK ME PLEASE! HARDER!"
    Villager2 "I'm going to cum, your ass is incredible!"
    Alexa "DON'T CUM YET! KEEP FUCKING ME PLEASE!!"
    stop bgs fadeout 1
    play music "audio/Town1.ogg" loop volume 0.9
    scene trabajo13
    Leyna "(... I think anyone can't see me from here. They don't even know I'm here)"
    Leyna "(I have to get it off my chest, it will only take a second)"
    scene trabajo14
    Leyna "Ahhhh"
    Leyna "(Shit, I have to be quiet or they might discover me and that... would be a problem)"
    Leyna "(Yes, I would be in serious trouble, I could get caught and between them two...)"
    scene trabajo15
    Leyna "Hmmmmm"
    Leyna "(I would be caught between the two of them and... fuck me through every hole in my body, using me)"
    $ flash_screen(wait=True)
    Leyna "Aaah!"
    $ flash_screen(wait=True)
    Leyna "I'm... I'm ..."
    $ flash_screen(wait=True)
    Leyna "Hmmmmmaaa..."
    scene trabajo16
    Leyna "Shit, I hope the didn't notice"
    Leyna "That... was very good, but I shouldn't have done it... just thinking about it, again I'm ... I'm not being myself, I should go back"
    pause
    scene black with dissolve
    hide trabajo16
    call SetPlayerLocation("Reception") from _call_ReceptionEV005_0_SetPlayerLocation
    # fade in
    pause 0.26
    pause 0.2
    Leyna "(Alexa... how can you do this kind of thing?... I... shouldn't have done it...)"
    pause 0.36
    pause 0.2
    Leyna "Wow, you're back from the festival already?"
    Receptionist "Yes, today there wasn't much work,you can leave if you want, there is a lot to do?"
    Leyna "Well... right now there are three clients inside... I need to clean up a little bit"
    Receptionist "Don't worry, I'll take care of it, come tomorrow at the same time"
    Leyna "Great thank you very much"
    scene black with dissolve
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    call SetPlayerLocation("HotSpringsExterior") from _call_ReceptionEV005_0_SetPlayerLocation_1
    # fade in
    pause 0.22
    $ leyna_work = 10
    return

label Receptionhotspringsjuntos_0:
    pause 0.24
    pause 0.2
    Receptionist "Leyna! thank goodness you are here! our hotsprings are full, it seems that the whole town has agreed to come today!"
    Receptionist "Please change quickly and help, they need someone in there to take care of them"
    show plano_mujer_ojos_blanco_negro:
        xsize 1600
        ysize 900
    Leyna "RI-RIGHT! I'll be right there, I'm sorry Johan, it looks like I won't be able to keep an eye on you"
    Johan "It's normal don't worry! I'll be over here taking a bath, try not to get nervous and I'm sure everything will be fine!"
    hide plano_mujer_ojos_blanco_negro
    show plano_mujer_sonrisa:
        xsize 1600
        ysize 900
    Leyna "Yes, I will do my best!"
    Johan "Of course! You can do it!"
    scene black with dissolve
    hide plano_mujer_sonrisa
    call SetPlayerLocation("HotSpringsWithJohan") from _call_Receptionhotspringsjuntos_0_SetPlayerLocation
    # fade in
    return

