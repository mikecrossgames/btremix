label HotSpringsWithJohanhotspringjuntoscont:
    pause 0.22
    pause 0.2
    Johan "Wow! it is true that there are quite a lot of people, and as far as I can see, there are still more coming in... even though..."
    Johan "These hotsprings were supposed to be mixed, right? but there are only men here... for a change, well... I just love Leyna"
    Johan "But looking is not a crime, right? hahahaha... anyway, I guess I'll take a bath, I hope Leyna doesn't have a hard time with this amount of work"
    scene black with dissolve
    # TransferPlayer: "HotSpringsWithJohan"
    # fade in
    pause 0.2
    Johan "Aaaahhh, how nice! I don't know why I didn't come here before! The water is at the perfect temperature! and it feels... a bit weird to be honest..."
    Johan "Is it the spices they put in the water...? I don't know ...but I don't really care! it's really good!"
    scene hotspringsjuntos2
    Villager "Hey, is this your first time? I don't think I know you from the village!"
    Johan "Well, yes, I came with my wife to work and take a little vacation"
    Villager "Ohh great great! I hope you enjoy it, we have the best Hotsprings in the country that's for sure! we put some special herbs that only grow here"
    Johan "Wow! I had imagined it, they certainly have a revitalizing effect on the body!"
    Villager "You're telling me! hahahahahahaha!"
    Johan "(Did I say something funny?) Yeah hahaha... by the way this is pretty crowded isn't it? is it always like this?"
    Villager "Oh no no no, we only come on special occasions, winter festivals and such..."
    Villager "... But do you want to know the truth?"
    Johan "The truth? sure, tell me"
    Villager "Word has spread around town that a new girl has come to work here and she is nothing less than a beauty!"
    Johan "!!!..."
    Villager "A goddess by all accounts! And of course the guys can't help but come in droves to gossip and if they can show off a bit in front of the girl too hahaha"
    Johan "Of course hahahaha (Shit he's talking about Leyna right?, more attention to Leyna...)"
    scene hotspringsjuntos3
    Johan "(Leyna has arrived! She seems to be a little nervous but I'm sure she'll do fine)"
    Johan "(I hope no one goes overboard with her)"
    scene hotspringsjuntos4
    Johan "????"
    Johan "(What the hell, when I arrived everyone was dressed! and now they're all naked!)"
    scene hotspringsjuntos5
    Johan "(And that guy has a boner! They're all surrounding her, it's not necessary to get that close)"
    Johan "(What are they saying to him? damn it, from here I can't hear anything they are saying... but getting close would be a bit... embarrassing)"
    Johan "(I don't want to go and make Leyna even more nervous, she might lose her job...)"
    scene hotspringsjuntos6
    Johan "(It seems that he has been asked for something from the storage)"
    Johan "(Well, she seems to be calmer and in a good mood, I guess after these days in this town she is getting used to seeing naked men)"
    Johan "(I'm glad she's calmer.... but I don't like this situation)"
    scene hotspringsjuntos7
    Johan "(Well, he will be giving them the products whatever they have asked him for)"
    pause
    if switch("infusion"):
        scene hotspringsjuntos8
        Johan "(what's going on there? I hope they are not giving problems to Leyna...)"
        Johan "(she will be looking for something on the shelves... some cream or balm)"
        pause
        scene hotspringsjuntos9
        Johan "(They are taking a long time.... Why am I so worried? my stomach is upset... I don't know what's been happening to me for a couple of days now)"
        Johan "(Am I becoming a jealous husband?... I have to stop having such a hard time when Leyna is not with me for the sake of our relationship)"
        Johan "(And my mental health... shit... it's taking too long, isn't it... here we go again Johan try to relax)"
        pause
        scene black with dissolve
        hide hotspringsjuntos9
    if not switch("infusion"):
        Johan "(what's going on there? I hope they are not giving problems to Leyna...)"
        Johan "(she will be looking for something on the shelves... some cream or balm)"
        Johan "(Am I becoming a jealous husband?... I have to stop having such a hard time when Leyna is not with me for the sake of our relationship)"
        Johan "(And my mental health... shit... it's taking too long, isn't it... here we go again Johan try to relax)"
        pause
        scene black with dissolve
    scene hotspringsjuntos8
    show hotspringsjuntos10 with dissolve
    "A FEW MOMENTS LATER"
    Johan "!!! (It looks like Leyna has finished helping those guys and comes to greet me)"
    Johan "(At the end it does seem that she is a little uncomfortable with all these naked men around her... the truth is that I feel a little relieved hahaha)"
    scene hotspringsjuntos11
    Leyna "Hello Johan, is everything all right?"
    Johan "Yes! everything is perfect honey, you don't need to pay much attention to me, I don't want to cause you any problems"
    if switch("infusion"):
        scene hotspringsjuntos13
        Leyna "Ohh don't worry, I'm almost done... in half an hour everything will be ready and I'll be able to go out"
        Johan "Great! I'll wait for you to finish and we'll go out together Is that okay with you?"
        Leyna "Yes, of course!"
        scene black with dissolve
    if not switch("infusion"):
        Leyna "Ohh don't worry, I'm almost done... in half an hour everything will be ready and I'll be able to go out"
        Johan "Great! I'll wait for you to finish and we'll go out together Is that okay with you?"
        Leyna "Yes, of course!"
        scene black with dissolve
    hide hotspringsjuntos2
    hide hotspringsjuntos3
    hide hotspringsjuntos4
    hide hotspringsjuntos5
    hide hotspringsjuntos6
    hide hotspringsjuntos7
    hide hotspringsjuntos8
    hide hotspringsjuntos10
    hide hotspringsjuntos11
    hide hotspringsjuntos13
    # TransferPlayer: "Path"
    show hotspringsjuntos12 with dissolve
    pause 0.26
    Johan "Well, what should we do now?"
    show plano_mujer_sorpresa_lado:
        xsize 1600
        ysize 900
    Leyna "Well... do you remember the photographer?"
    Johan "Hmmm yes... yes I remember ,why?"
    Leyna "He said he had to talk to me about something..."
    Johan "I see, if I'm being honest, I'm not very excited about this whole photographer thing, Leyna"
    Leyna "I know... but he told me that this is a good way to get money, and since we need it so much...."
    Johan "Yeah... well if you want we can go to see it together"
    Leyna "Yeah... sure"
    hide plano_mujer_sorpresa_lado
    $ set_switch("hotsprings_together", True)
    return

