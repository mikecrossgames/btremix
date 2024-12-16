label TownNightEhhhYouuuuuuuuu_0:
    pause 0.22
    "ehhh youuuuuuuuu"
    pause 0.22
    Johan "Hm? are you talking to us?"
    YoungVillager "You are new around here right? if you have nothing to do you can have a drink with us"
    Johan "(They seem quite nice ...) Okey, why not?"
    YoungVillager "Great! but we have a problem, the shop owner is my Grandma and she doesn't want to sell us any alcohol..."
    "... But since he doesn't know you, you could stop by and grab a couple of bottles for us..."
    "... As it just closed, you will have to go in the morning ... We better meet you here tomorrow night"
    Johan "Ok, if we have some free time we'll stop by the store"
    YoungVillager "Great! Thanks!!!"
    $ bottle_event = 1
    return

label TownNightEhhhYouuuuuuuuu_2(menu_choice = None):
    YoungVillager "Good night guys"
    Johan "We got the bottles! Your grandmother almost catches us"
    play sound "audio/Recovery.ogg" volume 0.9 noloop
    $ item_liqueur = False
    YoungVillager "Thanks a lot guys!!! You saved the night"
    YoungVillager "Why don't you do the honours and start the bottle?"
    pause 0.2
    Johan "Hahahaha thank you, let's get started"
    scene adolescentes1
    Johan "Wow this liquor is quite strong"
    YoungVillager "Hahahaha I know, in this town we make liquors quite strong"
    Leyna "So you have already tried it, huh?"
    YoungVillager "Mmm yes.. from time to time I take a little from my father, but it's not enough for all of us"
    YoungVillager "Hey, I don't know your names yet"
    Johan "Oh sure, I'm Johan and this is my wife Leyna"
    YoungVillager "A pleasure guys! Hey Leyna, don't you want to drink a couple of shots?"
    Leyna "Oh ... I don't know if I should ..."
    Johan "(Leyna feels bad about alcohol ... but a little shouldn't hurt)"
    YoungVillager "Came on! It's not a proper party if we don't all drink"
    Johan "He's right, come on Leyna, a little doesn't hurt"
    Leyna "If that's okay with you then ... why not?"
    YoungVillager "Great!"
    scene adolescentes2
    Johan "(Wow that's a pretty big drink)"
    YoungVillager "(Cool she's not playing, she almost drinks half a bottle in one go)"
    scene adolescentes3
    Leyna "Wow! It's strong but it's very good"
    YoungVillager2 "So tell me, are you here on vacation?"
    Leyna "Yes, we've come to do a report of the festival for a tourism magazine, we are from the capital"
    YoungVillager2 "Great, the capital! I've always wanted to go but my father makes me work every day in the fields and I don't have time for anything"
    YoungVillager "Yes, it must be great to live in the capital, surely there are many beautiful girls like you there"
    scene adolescentes4
    Leyna "Pretty girls? Hahaha thanks"
    YoungVillager "Here there are almost none and those who live here are already married or their parents have them out of our reach"
    Johan "Hahahahha a classic, Leyna's father was also very protective of her"
    YoungVillager2 "Ahh so in the capital they are also like that.. there is no hope guys! let's drink more"
    Johan "Hahahah perfect, but I have to control myself, that liquor is very strong and it is already going to my head!"
    YoungVillager "Well ... that's the idea isn't it? hahaha"
    Johan "You're right (although Leyna worries me, you can see in her face that she's quite drunk)"
    YoungVillager2 "Ahh !! Man, we're going to die without seeing a naked woman"
    Johan "Come on come on, it's not so bad, you will surely find your ideal woman and meanwhile you have internet to entertain you"
    YoungVillager "Internet? There is no connection here except in the town hall and there it's impossible to see anything"
    Johan "(Wow, teenagers without internet or girls ... poor guys I can't imagine how bad it would have been for me)"
    Johan "Come on guys don't get depressed, for sure it will be solved!"
    YoungVillager2 "It's easy for you to say, you are with a beautiful woman. Sure you do it every day!"
    Johan "(I wish I were...) Hahaha well it's not that simple.."
    YoungVillager "Right, if I had a wife like Leyna I would be fucking everyday day without stopping"
    scene adolescentes5
    Leyna "Hahaha what an impressive youth"
    YoungVillager2 "And.. this.. since you see them every day.. How are they?"
    Johan "... the boobs?"
    YoungVillager "Yes yes!"
    Johan "Well they are ... very pretty?"
    YoungVillager2 "Ahh very pretty and we will die without seeing some"
    YoungVillager "Hey ... couldn't you show us something Leyna? Just a a little to know how they are"
    Leyna "Ah?!"
    YoungVillager "Come on it will be only a second! You're beautiful! Just a little bit and we won't talk about it again"
    Johan "Wow, slow down!"
    YoungVillager "Oh! Of course if you give us permission Johan, let's go, we don't have internet and we are crazy to know a little"
    YoungVillager2 "Yes! And what if one day I do it with a woman and I haven't seen anything before? I will stay like a stone. How embarrassing.."
    Johan "Guys..."
    YoungVillager "Please it will only be a second"
    Johan "eh..."
    Leyna "If it's only for a second ..."
    Johan "Leyna?"
    Leyna "They're just kids, they're harmless! They give me a little pity"
    Johan "...(Leyna is clearly drunk ... well and I am too ... just a second? The truth is they also give me some pity ..)"
    Johan "(If she shows them something they will leave us alone with the subject ...)"
    menu:
        "Yes":
            Johan "Okay guys, but just a second and that's it!"
            YoungVillager "REALLY?! Great, thank you very much!"
            YoungVillager2 "Incredible I can't believe it, thank you very much!"
            Leyna "Okay, just a little look and that's it"
            scene adolescentes6
            Leyna "Here they are!"
            YoungVillager "Wow!! Amazing!"
            YoungVillager2 "Great, I'm going to jerk off tonight, thank you very much!"
            Johan "Hey you don't have to tell us that"
            YoungVillager "Hey can I ... can I touch them?"
            Leyna "Ehm..."
            Johan "No way! Without touching, this has been enough!"
            YoungVillager "Sorry..."
            pause
            scene black with dissolve
            hide adolescentes6
            # fade in
            "...A FEW DRINKS OF LIQUOR LATER..."
            Leyna "Well ... I think it's about time we go"
            YoungVillager2 "Oooh! Now that we were having a good time?"
            Johan "Relax, we'll see you around here"
            YoungVillager "I take your word, if you want to have a good time one day you know where we are"
            $ bottle_event = 3
        "No":
            Johan "You're drunk, you don't know what you're saying"
            Johan "You're definitely not going to show your tits to these kids, sorry guys."
            Johan "We were having a good time but we should go"
            $ bottle_event = 4
    return

