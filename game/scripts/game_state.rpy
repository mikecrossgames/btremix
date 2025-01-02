init python:
    def switch(s):
        if s not in switches:
            defaults = get_default_switches()
            switches[s] = False if s not in defaults else defaults[s]
        return switches[s]

    def set_switch(s, state):
        switches[s] = state

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
            "netorase": False,
            "netorare": False,
        }

    def set_self_switch(called_from, event_id, switch_id, value):
        if not called_from in self_switches:
            self_switches[called_from] = {}
        if not event_id in self_switches[called_from]:
            self_switches[called_from][event_id] = {}
        self_switches[called_from][event_id][switch_id] = value

    def self_switch(called_from, event_id, switch_id):
        if not called_from in self_switches:
            return False
        if not event_id in self_switches[called_from]:
            return False
        if not switch_id in self_switches[called_from][event_id]:
            return False
        if self_switches[called_from][event_id][switch_id] == None:
            return False
        return self_switches[called_from][event_id][switch_id]

default _saved_bgm = None
default switches = get_default_switches()
default self_switches = {}
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

default item_clothes = False
default item_liqueur = False
default item_tools_bag = False
default item_flowers = False