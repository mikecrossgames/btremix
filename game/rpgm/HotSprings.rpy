label HotSpringsBG:
    $ set_transparency_backgrounds(["bg_hot_springs"])
    $ set_map_backgrounds(["bg_hot_springs"])
    return

label HotSpringsStart:
    call HotSpringsBG from _call_HotSpringsBG
    stop music
    stop bgs
    return

label HotSpringsEnd:
    return

label HotSpringshotspringseventopart2Base:
    call Movement("HotSpringshotspringseventopart2", "HotSpringshombreonsen2", ["D","R","D","D","D","D","TURN_L"]) from _call_HotSpringshotspringseventopart2_Movement
    call Movement("HotSpringshotspringseventopart2", "HotSpringshombreonsen1", ["D","D","R","D","D","D","TURN_L"]) from _call_HotSpringshotspringseventopart2_Movement_1
    $ resolve_scene()
    Villager "Wow, I see we are not alone"
    call Movement("HotSpringshotspringseventopart2", "player", ["TURN_R"]) from _call_HotSpringshotspringseventopart2_Movement_2
    $ resolve_scene()
    Leyna "Aaah!? (What the hell are those guys doing here)..."
    Leyna "What?! I ... I didn't know the hot springs are mixed"
    Villager "You are not from here, of course. Yeah, they are mixed but don't worry about us, relax.. We'll keep you company!"
    $ resolve_scene()
    Leyna "Oh... I see"
    $ fade_out()
    call SetEventLocation("HotSpringshotspringseventopart2", "HotSpringshombreonsen1", 11, 10) from _call_HotSpringshotspringseventopart2_setloc
    call SetEventLocation("HotSpringshotspringseventopart2", "HotSpringshombreonsen2", 13, 10) from _call_HotSpringshotspringseventopart2_setloc_1
    $ show_picture(1, "onsen2")
    $ fade_in()
    call PlaySound("sound", "audio/Dive.ogg", volume=0.9, no_loop=True) from _call_HotSpringshotspringseventopart2_PlaySound
    $ resolve_scene()
    Villager "So, are you travelling?"
    Leyna "( He is too close ) Yes.. I've come with my husband.."
    Villager "Oh?... And where is your husband, if I may ask?"
    Leyna "In the town hall talking to some workers and the mayor"
    Villager "Hmm, I see.. better for haha, only us enjoying your company.."
    Leyna "What?"
    Villager "Hahaha is a joke, relax woman, this place is to enjoy and have a good time"
    Leyna "Hahaha of course..."
    $ fade_out()
    call PlaySound("sound", "audio/Liquid.ogg", volume=0.9, no_loop=True) from _call_HotSpringshotspringseventopart2_PlaySound_1
    $ show_picture(2, "onsen3")
    $ fade_in()
    $ resolve_scene()
    "(A FEW MINUTES LATER...)"
    Leyna "(I'm starting to get dizzy ... but I don't want to be seen naked and I've left the towel on the bench over there)"
    Villager "Are you okay lady?"
    pause
    $ show_picture(3, "onsen5")
    $ resolve_scene()
    Leyna "The heat is affecting me, I guess"
    Villager "Yeah, you are in a very tense position. Relax or you'll pass out"
    Leyna "Do you think so? ... I suppose you are right"
    pause
    $ show_picture(4, "onsen6")
    call PlaySound("sound", "audio/Jump1.ogg", volume=0.9, no_loop=True) from _call_HotSpringshotspringseventopart2_PlaySound_2
    $ resolve_scene()
    Villager "This is better, right?"
    Leyna "I guess so... thank you very much, I need to relax more, after all I'm on a kind of vacation"
    Villager "Hahaha... Well I must admit you have a great body, and breasts as I've never seen in my life"
    Leyna "Tha..thanks"
    Villager "Plus, you're nice! The usual is a woman being angry when someone says this kind of thing to her"
    Leyna "Don't worry, it's a compliment, right?"
    Villager "(She's clearly not thinking straight.. probably because of the vapours and heat)"
    Villager "( What if I..? )"
    Villager "Yes... Hey, can I touch one? As I said, I've never seen such beautiful ones"
    Leyna "... ah?"
    Villager "Yeah, I'm older and at this rate, I don't think I'll ever get married. Let me touch you a tit, I have to do it before I die"
    Villager2 "Come on dude, don't be a dirty old man.."
    Leyna "...Well... if it's such an important thing to you... it's just touching a tit"
    $ show_picture(5, "onsen7")
    call PlaySound("sound", "audio/Jump1.ogg", volume=0.9, no_loop=True) from _call_HotSpringshotspringseventopart2_PlaySound_3
    call PlaySound("music", "audio/Dungeon3.ogg", volume=0.9, no_loop=False) from _call_HotSpringshotspringseventopart2_PlaySound_4
    $ resolve_scene()
    Leyna "(!!!)"
    Villager "Wow! Thanks.. as I said, perfect. They are soft and smooth, you have an incredible body"
    Leyna "... Thanks (I'm too dizzy for this)"
    Villager2 "... Hey! If he can, me too, right? It wouldn't be fair if only one of us could"
    Leyna "Well I don't..."
    $ show_picture(6, "onsen8")
    call PlaySound("sound", "audio/Jump1.ogg", volume=0.9, no_loop=True) from _call_HotSpringshotspringseventopart2_PlaySound_5
    $ resolve_scene()
    Villager2 "You're right!! They are perfect, what a feeling !!! I wish I had known you years ago to ask you to marry me Your husband is very lucky"
    Leyna "Hahaha..."
    $ show_picture(7, "onsen9")
    $ resolve_scene()
    Leyna "I think I've been here too long ... I feel dizzy.. I better get out"
    Villager "Already?! What a shame.. we are having so  much fun.."
    Leyna "Excuse me..."
    $ show_picture(8, "onsen10")
    call PlaySound("sound", "audio/Jump2.ogg", volume=0.9, no_loop=True) from _call_HotSpringshotspringseventopart2_PlaySound_6
    $ resolve_scene()
    Leyna "Oh?!!"
    Villager "Seems like you're very stunned, let me help you..."
    pause
    $ show_picture(9, "onsen11")
    call PlaySound("sound", "audio/Jump2.ogg", volume=0.9, no_loop=True) from _call_HotSpringshotspringseventopart2_PlaySound_7
    $ resolve_scene()
    Leyna "Oooh ... don't..."
    Villager "Relax... I will take you to the locker room and give you something cold to drink"
    Leyna "..."
    Villager "Shit, the ground is wet… uoh shit!"
    call PlaySound("sound", "audio/Fall.ogg", volume=0.9, no_loop=True) from _call_HotSpringshotspringseventopart2_PlaySound_8
    $ show_picture(10, "onsen12")
    call PlaySound("sound", "audio/Blow1.ogg", volume=0.9, no_loop=True) from _call_HotSpringshotspringseventopart2_PlaySound_9
    $ resolve_scene()
    $ shake_screen(5, 5, 60)
    Leyna "What... Have we fallen?"
    pause
    $ show_picture(11, "onsen13")
    call PlaySound("sound", "audio/Jump2.ogg", volume=0.9, no_loop=True) from _call_HotSpringshotspringseventopart2_PlaySound_10
    $ resolve_scene()
    Leyna "(!!!)"
    Villager "Shit my back... Wait a second miss, don't move. We have hit the ground.."
    Villager "(Oooh, I have to take advantage of this situation. I'm touching her with my... damn I have to tell this to the boys)"
    Leyna "I think ... I think we can get up now, right?"
    Villager "Yes, sure.. I'm better now.. (Fuck..)"
    $ fade_out()
    $ show_picture(12, "onsen14")
    $ fade_in()
    $ resolve_scene()
    Leyna "Sorry for the inconvenience, because of me you hit you back... I owe you a favour, if you ever need anything tell me"
    Villager "Of course, don't worry, you're going to the festival right? we'll see you there ..."
    Leyna "Yeah right..."
    $ fade_out()
    $ erase_picture(1)
    $ erase_picture(2)
    $ erase_picture(3)
    $ erase_picture(4)
    $ erase_picture(5)
    $ erase_picture(6)
    $ erase_picture(7)
    $ erase_picture(9)
    $ erase_picture(8)
    $ erase_picture(10)
    $ erase_picture(11)
    $ erase_picture(12)
    stop music fadeout 1
    $ fade_in()
    call TransferPlayer("HotSpringsExterior", "HotSpringshotspringseventopart2", 11, 8, direction=2) from _call_HotSpringshotspringseventopart2_TransferPlayer
    call Movement("HotSpringshotspringseventopart2", "player", ["D","D"]) from _call_HotSpringshotspringseventopart2_Movement_3
    $ resolve_scene()
    Leyna "That has been dangerous, I can't fall asleep in that place again ... I'm still a little giddy"
    "(+2 CORRUPTION)"
    $ set_switch("hot_springs_first_visit", True)
    call GalleryViewed("onsen") from _call_HotSpringshotspringseventopart2_GalleryViewed
    $ corruption = corruption + 2
    return False

label HotSpringshotspringseventopart2(play_event = True, trigger = None): # autorun
    if is_erased("HotSpringshotspringseventopart2"):
        return None
    elif trigger == "autorun":
        call PlayEvent(play_event, "HotSpringshotspringseventopart2Base", "HotSpringshotspringseventopart2") from _call_HotSpringshotspringseventopart2_PlayEvent
        return (0, "", "HotSpringshotspringseventopart2")
    return None

