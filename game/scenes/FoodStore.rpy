label FoodStoreMerchant_1:
    Merchant "Hello couple, how can I help you?"
    Johan "We would like to buy a couple of bottles of liquor"
    Merchant "Ah of course .. are you going to have a party? It's a lot of alcohol for you two"
    show expresion_gota
    Johan "Yes of course, we have made a couple of friends in town and we would like to join the celebrations by carrying something"
    Merchant "Good idea .. as long as it's an adult party .. my grandson just turned 18 and he's out of control"
    Merchant "He always tries to convince someone to buy him alcohol, but in this town we all know each other"
    hide expresion_gota
    show plano_mujer_cartoon:
        xsize 1600
        ysize 900
    Leyna "Yeah ... hehehe young people want to live as adults earlier and earlier"
    Merchant "Well, I am not entertaining you anymore .. here you have, have fun!"
    hide plano_mujer_cartoon
    play sound "audio/Recovery.ogg" volume 0.9 noloop
    $ item_liqueur = True
    "(YOU WON A NEW OBJECT)"
    Johan "Thank you!"
    $ bottle_event = 2
    return

label FoodStoreMerchant_3:
    Merchant "Hello dear, can I help you with something?"
    show plano_mujer_sonrisa:
        xsize 1600
        ysize 900
    Leyna "Yes, you see... I'm looking for a little job to these festival days and I thought you might need someone to help you"
    Merchant "You are very kind to offer but this store is very small and the income is not very high"
    "Even if I wanted to, I couldn't afford to hire someone. I'm so sorry, honey"
    hide plano_mujer_sonrisa
    show plano_mujer_timida:
        xsize 1600
        ysize 900
    Leyna "Oh... don't worry I'll keep looking"
    Merchant "you could go to the village bar, there is always many people and they might be interested in having a girl so beautiful"
    hide plano_mujer_timida
    show expresion_gota
    "you know... to attract the customers hehehe"
    Leyna "(I don't think it's a good idea but...) Maybe I stop by, thank you very much!"
    hide expresion_gota
    $ leyna_work = 2
    return

