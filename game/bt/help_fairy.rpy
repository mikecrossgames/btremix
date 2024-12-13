init python:
    def get_automated_hint():
        if event_clothing > 0 and elder_festival < 8:
            return _("go to the festival and talk to the worker")
        if switch("finished_river_scene") and not switch("leyna_alone") and not switch("third_day"):
            return _("talk to Johan")
        if switch("second_river") and not switch("third_day"):
            return _("go to the inn to meet Johan")
        if switch("lucky_person"):
            if not switch("festival_photos"):
                return _("talk to Johan")
            if food_stand == 0:
                return _("go to the food stand")
            if food_stand == 1 and not switch("massage_masturbation") and not switch("massage_sex"):
                return _("go for a massage")
        if ritual == 2:
            return _("go to the inn")
        if ritual == 3 and blackmail == 0:
            return _("talk to the boys in the village park")
        if ritual == 3 and blackmail > 0 and hiding_place == 0 and not switch("final_hideout"):
            return _("go and talk to Alexa")
        if ritual == 3 and blackmail > 0 and not switch("final_hideout"):
            return _("go and find Johan")
        if switch("final_hideout") and not self_switch("Reception","Receptionhotspringsjuntos","A"):
            return _("go to the hot springs")
        if switch("erotic_photos_together") and not self_switch("Bar2","Bar2WowGuysWhatACoincidence","A"):
            return _("go to the bar")
        if not self_switch("Path","PathLeynaWorkTrigger","A") and bet_together >= 1:
            return _("go to the hot springs")
        if switch("flashback") and bar_work == 0:
            return _("go and talk to the barman at the bar")
        if bar_work == 1:
            return _("go back to the inn")
        if bar_work == 2:
            return _("go work at the bar")
        if bar_work == 3:
            return _("meet Leyna at the bar")
        if bar_work >= 4 and butt_plug == 0: 
            return _("go to your room at the inn")
        if butt_plug == 1:
            return _("talk to the innkeeper about your delivery")
        if butt_plug == 2:
            return _("go and find Leyna")
        if butt_plug == 3:
            return _("work at the food stand")
        if switch("hotsprings_together") and not self_switch("Town2","Town2fotografo","A") and not self_switch("Town2","Town2fotografo","B"):
            return _("talk to the photographer")
        if switch("johan_and_leyna_sex") and not self_switch("Bar2","Bar2WowGuysWhatACoincidence","A"):
            return _("go to the bar")
        if current_map == "FestivalNight":
            return _("go and find Johan")
        if switch("pick_up_package"):
            return _("talk to the clothing store merchant")
        if elder_festival >= 2 and elder_festival < 5:
            return _("look for the tools in the general store")
        if elder_festival == 5:
            return _("take the tools back to the father")
        if leyna_work == 11 and not switch("find_youth") and ritual == 0:
            return _("go to the festival")
        if switch("find_youth"):
            return _("find the boy")
        if switch("party_at_festival") and not switch("river_3"):
            return _("go to the river")
        if switch("river_3") and not switch("hotsprings_photo_session"):
            return _("talk to the photographer")
        if switch("hotsprings_photo_session") and not self_switch("Bar2","Bar2LeynaWeWereLookingForYou","A"):
            return _("go to the bar")
        if self_switch("Bar2","Bar2LeynaWeWereLookingForYou","A") and not switch("bet_2"):
            return _("go to the bar")
        if switch("bet_2") and not switch("last_bar"):
            return _("go to the bar")
        if switch("last_bar") and not switch("last_hotsprings"):
            return _("go to the hot springs")
        if switch("last_hotsprings") and not switch("festival_final"):
            return _("enjoy the festival")
        if switch("festival_final") and switch("corruption_high") and not self_switch("Bar2","Bar2LeynawhatAreYouDoingHereIThoughtYouWereLeavingTownThisMorning","A"):
            return _("say goodbye to the guys in the bar")
        if switch("festival_final"):
            return _("time to return home")
        return None

    def get_town_map():
        if "Night" in current_map:
            return "TownNight"
        if switch("third_day"):
            return "Town2"
        return "Town"

default fairy_first_time = True

label FairyHelp:
    $ automated_hint = get_automated_hint()
    if fairy_first_time:
        "I'm here to help you, I can give you some advice on what to do"
    if automated_hint is not None:
        "[automated_hint]"
    else:
        if not switch("seen_tablon"):
            "there is a poster near the inn that shows some ideas on what to do today"
        "would you like to view the poster?"
        menu:
            "Yes":
                $ from_x = map_x
                $ from_y = map_y
                $ from_map = current_map
                $ from_map_backgrounds = map_backgrounds
                $ from_transparency_backgrounds = transparency_backgrounds
                $ town_map = get_town_map()
                call TransferPlayer(town_map, "FairyHelp", 18, 34) from _TransferPlayer_FairyHelp
                $ resolve_scene("dirty")
                $ renpy.call(town_map + "TABLON", play_event = True, trigger = "event")
                call TransferPlayer(from_map, "FairyHelp", from_x, from_y) from _TransferPlayer_FairyHelp_Back
                $ set_map_backgrounds(from_map_backgrounds)
                $ set_transparency_backgrounds(from_transparency_backgrounds)
                $ resolve_scene("dirty")
            "No":
                pass
    if fairy_first_time:
        "would you like me to stay on the screen to help you?"
        menu:
            "Yes":
                "okay"
                pass
            "No":
                "okay, you can change your mind in {i}Preferences{/i}"
                $ persistent.fairy_help = False
                pass
        $ fairy_first_time = False
    return

screen help_fairy():
    if switch("fairy_on") and fairy > 0 and persistent.fairy_help:
        imagebutton at fade_in_event:
            action Call("FairyHelp")
            xalign 0.980392156862745
            yalign 0.025641025641026
            idle Transform("faces/fairy1.webp", xsize=66, ysize=72)
            hover Transform("faces/fairy2.webp", xsize=66, ysize=72)
            mouse "action"
