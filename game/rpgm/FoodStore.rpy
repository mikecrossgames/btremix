label FoodStoreBG:
    $ set_transparency_backgrounds(["bg_food_store","darkbg"])
    $ set_map_backgrounds(["map_food_store"])
    return

label FoodStoreStart:
    call FoodStoreBG from _call_FoodStoreBG
    stop music
    stop bgs
    return

label FoodStoreEnd:
    return

label FoodStoreToTown_0:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_FoodStoreEV001_0_PlaySound
    call TransferPlayer("Town", "FoodStoreEV001_0", 44, 21, direction=2) from _call_FoodStoreEV001_0_TransferPlayer
    $ resolve_scene()
    return False

label FoodStoreToTown_1:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_FoodStoreEV001_1_PlaySound
    call TransferPlayer("Town2", "FoodStoreEV001_1", 44, 21, direction=2) from _call_FoodStoreEV001_1_TransferPlayer
    $ resolve_scene()
    return False

label FoodStoreToTown(play_event = True, trigger = None): # event
    if is_erased("FoodStoreToTown"):
        return None
    elif trigger == "event" and switch("third_day"):
        call PlayEvent(play_event, "FoodStoreToTown_1", "FoodStoreToTown") from _call_FoodStoreToTown_1_PlayEvent
        return (0, "", "FoodStoreToTown_1")
    elif trigger == "event":
        call PlayEvent(play_event, "FoodStoreToTown_0", "FoodStoreToTown") from _call_FoodStoreToTown_0_PlayEvent
        return (0, "", "FoodStoreToTown_0")
    return None

label FoodStoreToTown_v2_0:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_FoodStoreEV002_0_PlaySound
    call TransferPlayer("Town", "FoodStoreEV002_0", 43, 21, direction=6) from _call_FoodStoreEV002_0_TransferPlayer
    $ resolve_scene()
    return False

label FoodStoreToTown_v2_1:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_FoodStoreEV002_1_PlaySound
    call TransferPlayer("Town2", "FoodStoreEV002_1", 43, 21, direction=6) from _call_FoodStoreEV002_1_TransferPlayer
    $ resolve_scene()
    return False

label FoodStoreToTown_v2(play_event = True, trigger = None): # event
    if is_erased("FoodStoreToTown_v2"):
        return None
    elif trigger == "event" and switch("third_day"):
        call PlayEvent(play_event, "FoodStoreToTown_v2_1", "FoodStoreToTown_v2") from _call_FoodStoreToTown_v2_1_PlayEvent
        return (0, "", "FoodStoreToTown_v2_1")
    elif trigger == "event":
        call PlayEvent(play_event, "FoodStoreToTown_v2_0", "FoodStoreToTown_v2") from _call_FoodStoreToTown_v2_0_PlayEvent
        return (0, "", "FoodStoreToTown_v2_0")
    return None

label FoodStoreTheyHaveSoftDrinksOfAllFlavorsBase:
    "(They have soft drinks of all flavors..)"
    return False

label FoodStoreTheyHaveSoftDrinksOfAllFlavors(play_event = True, trigger = None): # event
    if is_erased("FoodStoreTheyHaveSoftDrinksOfAllFlavors"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "FoodStoreTheyHaveSoftDrinksOfAllFlavorsBase", "FoodStoreTheyHaveSoftDrinksOfAllFlavors") from _call_FoodStoreTheyHaveSoftDrinksOfAllFlavors_PlayEvent
        return (1, "", "FoodStoreTheyHaveSoftDrinksOfAllFlavors")
    return None

label FoodStoreMmmSpicyNoodlesBase:
    "(Mmm spicy noodles..)"
    return False

label FoodStoreMmmSpicyNoodles(play_event = True, trigger = None): # event
    if is_erased("FoodStoreMmmSpicyNoodles"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "FoodStoreMmmSpicyNoodlesBase", "FoodStoreMmmSpicyNoodles") from _call_FoodStoreMmmSpicyNoodles_PlayEvent
        return (1, "", "FoodStoreMmmSpicyNoodles")
    return None

label FoodStoreMerchant_0:
    if not switch("leyna_alone"):
        $ resolve_scene()
        Merchant "Welcome to my store, we have all kinds of products at a very affordable price"
    if switch("leyna_alone"):
        Merchant "Oh darling.. you remind me of me when I was younger, same body.. and now look at me"
        "Enjoy yourself while you're young. In this town, there are many men.. hehehehe... "
    $ resolve_scene()
    return False

label FoodStoreMerchant_1:
    Merchant "Hello couple, how can I help you?"
    Johan "We would like to buy a couple of bottles of liquor"
    Merchant "Ah of course .. are you going to have a party? It's a lot of alcohol for you two"
    $ show_transparent(1, "expresion_gota")
    $ resolve_scene()
    Johan "Yes of course, we have made a couple of friends in town and we would like to join the celebrations by carrying something"
    Merchant "Good idea .. as long as it's an adult party .. my grandson just turned 18 and he's out of control"
    Merchant "He always tries to convince someone to buy him alcohol, but in this town we all know each other"
    $ erase_picture(1)
    $ show_transparent(1, "plano_mujer_cartoon", width=1600, height=900)
    $ resolve_scene()
    Leyna "Yeah ... hehehe young people want to live as adults earlier and earlier"
    Merchant "Well, I am not entertaining you anymore .. here you have, have fun!"
    $ erase_picture(1)
    call PlaySound("sound", "audio/Recovery.ogg", volume=0.9, no_loop=True) from _call_FoodStoreMerchant_1_PlaySound
    $ resolve_scene()
    $ set_item("liqueur", True)
    "(YOU WON A NEW OBJECT)"
    Johan "Thank you!"
    $ bottle_event = 2
    return False

label FoodStoreMerchant_2:
    Merchant "Welcome to my store, we have all kinds of products at a very affordable price"
    return False

label FoodStoreMerchant_3:
    Merchant "Hello dear, can I help you with something?"
    $ show_transparent(1, "plano_mujer_sonrisa", width=1600, height=900)
    $ resolve_scene()
    Leyna "Yes, you see... I'm looking for a little job to these festival days and I thought you might need someone to help you"
    Merchant "You are very kind to offer but this store is very small and the income is not very high"
    "Even if I wanted to, I couldn't afford to hire someone. I'm so sorry, honey"
    $ erase_picture(1)
    $ show_transparent(2, "plano_mujer_timida", width=1600, height=900)
    $ resolve_scene()
    Leyna "Oh... don't worry I'll keep looking"
    Merchant "you could go to the village bar, there is always many people and they might be interested in having a girl so beautiful"
    $ erase_picture(2)
    $ show_transparent(3, "expresion_gota")
    $ resolve_scene()
    "you know... to attract the customers hehehe"
    Leyna "(I don't think it's a good idea but...) Maybe I stop by, thank you very much!"
    $ erase_picture(3)
    $ leyna_work = 2
    $ resolve_scene()
    return False

label FoodStoreMerchant_4:
    Merchant "Welcome to my store, we have all kinds of products at a very affordable price"
    return False

label FoodStoreMerchant(play_event = True, trigger = None): # event
    if is_erased("FoodStoreMerchant"):
        return None
    elif trigger == "event" and leyna_work >= 2:
        call PlayEvent(play_event, "FoodStoreMerchant_4", "FoodStoreMerchant") from _call_FoodStoreMerchant_4_PlayEvent
        return (1, "", "FoodStoreMerchant_4")
    elif trigger == "event" and leyna_work >= 1:
        call PlayEvent(play_event, "FoodStoreMerchant_3", "FoodStoreMerchant") from _call_FoodStoreMerchant_3_PlayEvent
        return (1, "", "FoodStoreMerchant_3")
    elif trigger == "event" and bottle_event >= 2:
        call PlayEvent(play_event, "FoodStoreMerchant_2", "FoodStoreMerchant") from _call_FoodStoreMerchant_2_PlayEvent
        return (1, "", "FoodStoreMerchant_2")
    elif trigger == "event" and bottle_event >= 1:
        call PlayEvent(play_event, "FoodStoreMerchant_1", "FoodStoreMerchant") from _call_FoodStoreMerchant_1_PlayEvent
        return (1, "", "FoodStoreMerchant_1")
    elif trigger == "event":
        call PlayEvent(play_event, "FoodStoreMerchant_0", "FoodStoreMerchant") from _call_FoodStoreMerchant_0_PlayEvent
        return (1, "", "FoodStoreMerchant_0")
    return None

label FoodStoreYouWonANewObject_0:
    call PlaySound("sound", "audio/Recovery.ogg", volume=0.9, no_loop=True) from _call_FoodStoreEV008_0_PlaySound
    $ resolve_scene()
    $ set_item("tools_bag", True)
    "(YOU WON A NEW OBJECT)"
    $ elder_festival = 5
    return False

label FoodStoreYouWonANewObject(play_event = True, trigger = None): # event
    if is_erased("FoodStoreYouWonANewObject"):
        return None
    elif elder_festival >= 5:
        return None
    elif trigger == "event" and elder_festival >= 4:
        call PlayEvent(play_event, "FoodStoreYouWonANewObject_0", "FoodStoreYouWonANewObject") from _call_FoodStoreYouWonANewObject_0_PlayEvent
        return (1, "", "FoodStoreYouWonANewObject_0")
    return None

