default events_seen_date = 0
default scenes_seen = []
default events_seen_today = []
default inventory = []

init python:
    gallery_viewed_scenes = []

    def reset_gallery_viewed_scenes():
        gallery_viewed_scenes = []

    def has_switch(s):
        return s in switches

    def switch(s):
        global switches
        if s not in switches:
            defaults = get_default_switches()
            if s not in defaults:
                renpy.say(None, "Switch " + s + " does not exist.")
                return False
            switches[s] = defaults[s]
        return switches[s]

    def set_switch(s, state):
        global switches, no_advancement_events
        switches[s] = state
        if s == "suitcases" and state:
            set_transparency_backgrounds(["map_inn_room_suitcase"])
            set_map_backgrounds(["map_inn_room_suitcase"])
            switch_to_next_backgrounds()
            scene_state = "dirty"
        no_advancement_events = 0

    def get_item_values():
        item_values = {}
        for item in item_qtys:
            item_values[item] = str(item_qtys[item])
        return item_values

    def game_variable_values():
        return {
            "suitcases": str(suitcases),
            "corruption": str(corruption),
            "fairy": str(fairy),
            "elder_festival": str(elder_festival),
            "event_clothing": str(event_clothing),
            "photograph_3": str(photograph_3),
            "johan_dream": str(johan_dream),
            "jail": str(jail),
            "bottle_event": str(bottle_event),
            "food_stand": str(food_stand),
            "leyna_work": str(leyna_work),
            "masks": str(masks),
            "ritual": str(ritual),
            "hiding_place": str(hiding_place),
            "blackmail": str(blackmail),
            "erotic_photos": str(erotic_photos),
            "bet_together": str(bet_together),
            "leyna_hot": str(leyna_hot),
            "bar_work": str(bar_work),
            "johan_leyna_sex": str(johan_leyna_sex),
            "butt_plug": str(butt_plug),
            "festival_clothes": str(festival_clothes),
            "v0_7_3": str(v0_7_3),
            "leyna_poker": str(leyna_poker),
            "final_festival": str(final_festival),
            "final_day": str(final_day),
        }

    def progression_name(scene_name, var_value, name = "Progression"):
        return scene_name + name + str(var_value)

    def get_gallery_scene_name(scene_name):
        scene_names = get_gallery_scene_name_base(scene_name)
        scene_switches = {            
            # "enchantment___jessie_andy_bathroom": "OShannonsAndy_3",
        }
        for switch_name, event in scene_switches.iteritems():
            if scene_name == event and switch(switch_name):
                scene_names.append(event + switch_name)
        return scene_names

    def get_gallery_scene_name_base(scene_name):
#         if scene_name.startswith("AbandonedSubwayDog"):
#             return [progression_name(scene_name, dog_in_subway)]
        return []

    def game_people_values():
        return {
        }

    def game_message_values():
        return {
        }

    def get_default_switches():
        return {
            "introduction": False,
            "innkeeper": False,
            "suitcases": False,
            "inn_departure": False,
            "wet_shirt": False,
            "dry_shirt": False,
            "separated_in_the_river": False,
            "finished_river_scene": False,
            "neighborhood_grope": False,
            "lifted_skirt": False,
            "leyna_alone": False,
            "gave_bj": False,
            "no_bj": False,
            "first_photo_session": False,
            "no_return_to_the_river": False,
            "hot_springs_first_visit": False,
            "pick_up_package": False,
            "collected_package": False,
            "second_photo_session": False,
            "photo_not_taken": False,
            "second_river": False,
            "third_day": False,
            "johan_photo": False,
            "johan_silent": False,
            "johan_intervened": False,
            "festival": False,
            "ate_the_fruit": False,
            "fruit_event": False,
            "lucky_person": False,
            "festival_photos": False,
            "massage_sex": False,
            "massage_masturbation": False,
            "johan_mira_massage": False,
            "leyna_dream_end": False,
            "infusion": False,
            "find_youth": False,
            "corruption_average": False,
            "corruption_low": False,
            "final_blackmail": False,
            "final_hideout": False,
            "hotsprings_together": False,
            "erotic_photos_together": False,
            "johan_and_leyna_sex": False,
            "flashback": False,
            "corruption_maximum": False,
            "corruption_high": False,
            "party_at_festival": False,
            "johan_rejects": False,
            "johan_does_nothing": False,
            "river_3": False,
            "hotsprings_photo_session": False,
            "bet_2": False,
            "breakfast": False,
            "last_hotsprings": False,
            "last_bar": False,
            "festival_final": False,
            "seen_tablon": False,
            "fairy_on": False,
        }

    def reset_state():
        global inventory
        global followers
        global current_map
        global previous_map_background_map
        global game_over
        global switches
        global suitcases
        global corruption
        global fairy
        global elder_festival
        global event_clothing
        global photograph_3
        global johan_dream
        global jail
        global bottle_event
        global food_stand
        global leyna_work
        global masks
        global ritual
        global hiding_place
        global blackmail
        global erotic_photos
        global bet_together
        global leyna_hot
        global bar_work
        global johan_leyna_sex
        global butt_plug
        global festival_clothes
        global v0_7_3
        global leyna_poker
        global final_festival
        global final_day

        inventory = []
        followers = []
        current_map = ""
        previous_map_background_map = None
        game_over = False
        switches = get_default_switches()
        suitcases = 0
        corruption = 0
        fairy = 0
        elder_festival = 0
        event_clothing = 0
        photograph_3 = 0
        johan_dream = 0
        jail = 0
        bottle_event = 0
        food_stand = 0
        leyna_work = 0
        masks = 0
        ritual = 0
        hiding_place = 0
        blackmail = 0
        erotic_photos = 0
        bet_together = 0
        leyna_hot = 0
        bar_work = 0
        johan_leyna_sex = 0
        butt_plug = 0
        festival_clothes = 0
        v0_7_3 = 0
        leyna_poker = 0
        final_festival = 0
        final_day = 0

    def new_day():
        global events_seen_today, events_seen_date
        events_seen_today = []
        events_seen_date = events_seen_date + 1

    def add_seen_today(event):
        global events_seen_date, events_seen_today
        if date != events_seen_date:
            events_seen_date = date
            events_seen_today = []
        if event not in events_seen_today:
            events_seen_today.append(event)

    def reset_seen_today(event):
        global events_seen_today
        events_seen_today = list(filter(lambda x: x != event, events_seen_today))

    def seen_today(event):
        if events_seen_date is None or date != events_seen_date:
            return False
        return event in events_seen_today

    def mark_as_seen(scene_name):
        if GalScene.is_gallery_scene(scene_name):
            if not GalScene.is_inside_gallery():
                if not scene_name in scenes_seen:
                    scenes_seen.append(scene_name)
                GalScene.unlock_scene(scene_name)
            elif not scene_name in gallery_viewed_scenes:
                gallery_viewed_scenes.append(scene_name)

default scenes_seen_length = 0

label GalleryViewed(scene_name):
    $ mark_as_seen(scene_name)
    if len(scenes_seen) > scenes_seen_length:
        $ scenes_seen_length = len(scenes_seen)
        $ renpy.force_autosave(take_screenshot = True)
    return

default followers = []
default current_map = ""
default previous_map_background_map = None
default map_x = 0
default map_y = 0
default map_direction = 0
default money = 0
default game_over = False
default switches = get_default_switches()
default _saved_bgm = None
default item_qtys = {}
default date = 1

default suitcases = 0
default corruption = 0
default fairy = 0
default elder_festival = 0
default event_clothing = 0
default photograph_3 = 0
default johan_dream = 0
default jail = 0
default bottle_event = 0
default food_stand = 0
default leyna_work = 0
default masks = 0
default ritual = 0
default hiding_place = 0
default blackmail = 0
default erotic_photos = 0
default bet_together = 0
default leyna_hot = 0
default bar_work = 0
default johan_leyna_sex = 0
default butt_plug = 0
default festival_clothes = 0
default v0_7_3 = 0
default leyna_poker = 0
default final_festival = 0
default final_day = 0