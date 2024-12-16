label ClothingStoreHeyThere_1:
    Leyna "I come for the photographer's package"
    Merchant "The photographer's package? I see.."
    "So you are the new victim.. sometimes I think he just pretends he has this magazine jobs to take lewd photos"
    show plano_mujer_ojos_blanco_negro:
        xsize 1600
        ysize 900
    Leyna "What? He seems such a nice old man"
    Merchant "Yes, he is... just be careful"
    hide plano_mujer_ojos_blanco_negro
    show plano_mujer_sonrisa:
        xsize 1600
        ysize 900
    Leyna "Okay, thanks for the advice"
    Merchant "Here you have the package"
    hide plano_mujer_sonrisa
    play sound "audio/Recovery.ogg" volume 0.9 noloop
    $ set_item("clothes", True)
    "(YOU WON A NEW OBJECT)"
    Leyna "Thank you!"
    $ set_switch("pick_up_package", False)
    $ set_switch("collected_package", True)
    return

label ClothingStoreHeyThere_2:
    Merchant "Welcome again to my store! As I told you, I already have the festival clothes"
    "Do you want to try them on?"
    Leyna "Sure, I'm so excited!"
    Merchant "The fitting room is over there and the clothes are inside, just choose your size"
    Leyna "Thank you"
    $ event_clothing = 1
    return

label ClothingStoreIShouldComeBackLaterToTryTheFestivalClothes_1:
    show expresion_gui_o_lengua
    Leyna "I'm going to try it on, wait here and I'll let you know when I'm ready"
    Johan "O..okay"
    scene black with dissolve
    play sound "audio/Equip2.ogg" volume 0.9 noloop
    Leyna "Johan? Come in"
    play sound "audio/Move1.ogg" volume 0.9 noloop
    hide expresion_gui_o_lengua
    show probador1 with dissolve
    Leyna "So ... what do you think?"
    Johan "Wow, that's so sexy!"
    scene probador2
    Leyna "Do I look good?"
    Johan "You are beautiful (I would say too beautiful. Now that I think about it, is she supposed to go through the festival like this in front of everyone?)"
    Johan "(Now that I remember, these last days Leyna has had several \"accidents\" around the men of this village)"
    $ flash_screen([255,255,255,170], 60, True)
    play sound "audio/Poison.ogg" volume 0.9 noloop
    scene rio_7:
        pos (-125, 0)
        xsize 1104
        ysize 621
    Johan "Why am I thinking about this right now?"
    Johan "(I feel something in my stomach ... Am I getting turned on thinking about this?... No, I'm just...)"
    hide rio_7
    $ flash_screen([255,255,255,170], 60, True)
    scene probador3
    Leyna "Why are you staring at me so hard, Johan?"
    Johan "I'm just... You're so sexy in that outfit... I can't control myself"
    Johan "Let's make love, here and now"
    Leyna "Johan... we shouldn't..."
    Johan "Come here"
    scene black with dissolve
    hide probador1
    hide probador2
    hide probador3
    # fade in
    pause 0.2
    Merchant "They are taking a long time ..."
    play music "audio/Dungeon3.ogg" loop volume 0.9
    scene probador4
    Johan "Oh God,  I can't take it anymore, it's been weeks since last time..."
    Leyna "Ssshhh..."
    scene probador5
    hide probador4
    Johan "Ooh! Yes..."
    Leyna "Hm hm hm...."
    pause
    scene probador6
    Leyna "You like it?"
    Johan "I love it"
    pause
    $ flash_screen([255,255,255,170], 60, True)
    scene escena_camisa_mojada_1:
        pos (-125, 0)
        xsize 1104
        ysize 621
    Johan "Shit, this again? What the hell is wrong with me?"
    hide escena_camisa_mojada_1
    Johan "Get up Leyna"
    Leyna "!!!"
    scene probador7
    Johan "Right there"
    Leyna "hmmmmmmm...."
    scene probador8
    play bgs "audio/audio follar.ogg" loop volume 0.9
    Johan "Yes... damn...."
    Leyna "Oooh... (I have never seen Johan so excited... Does he like to do it in public?)"
    Johan "(Shit ... I can't get those pictures out of my head ... I'm...)"
    Johan "I'm coming!"
    Leyna "Wa...Wait! Take it out"
    scene probador9
    stop bgs fadeout 1
    $ flash_screen([255,255,255,170], 60, True)
    Johan "OOOHHH"
    Leyna "!!!"
    Johan "SHIT! I'm sorry, let me find something to clean you with"
    scene black with dissolve
    hide probador5
    hide probador6
    hide probador7
    hide probador8
    hide probador9
    stop bgs fadeout 1
    # TransferPlayer: "ClothingStore"
    # fade in
    pause 0.40
    show plano_mujer_sorpresa_lado:
        xsize 1600
        ysize 900
    Leyna "The clothes are perfect for me"
    Merchant "Glad to hear that, have fun at the festival!"
    Johan "... We will"
    scene black with dissolve
    hide plano_mujer_sorpresa_lado
    # TransferPlayer: "Town2"
    # fade in
    pause 0.24
    Johan "(What is happening to me? ... I've never had these kinds of thoughts)"
    $ corruption = corruption + 3
    $ event_clothing = 2
    return

