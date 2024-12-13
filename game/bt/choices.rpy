init python:
    def choice_is_disabled(choice, called_from):
        if not called_from.startswith("Town"):
            return False
        if choice == _("Bar 1") and switch("wet_shirt"):
            return True
        if choice == _("Market") and switch("lifted_skirt"):
            return True
        if choice == _("Villagers") and switch("neighborhood_grope"):
            return True
        if choice == _("River 1") and switch("finished_river_scene"):
            return True
        if choice == _("Photographer 1") and switch("first_photo_session"):
            return True
        if choice == _("Hotsprings") and switch("hot_springs_first_visit"):
            return True
        if choice == _("Photographer 2") and switch("second_photo_session"):
            return True
        if choice == _("Bar 2") and (switch("no_bj") or switch("gave_bj")):
            return True
        if choice == _("River 2") and switch("second_river"):
            return True
        if choice == _("Photographer 3") and photograph_3 > 0:
            return True
        if choice == _("Worker's quest") and elder_festival >= 6:
            return True
        if choice == _("Dresser") and event_clothing > 1:
            return True
        if choice == _("The dream") and johan_dream > 0:
            return True
        if choice == _("Police station") and jail > 0:
            return True
        if choice == _("Night Party") and bottle_event > 2:
            return True
        if choice == _("Go to the festival") and switch("lucky_person"):
            return True
        if choice == _("Groceries store") and leyna_work >= 2:
            return True
        if choice == _("Bar") and leyna_work >= 3:
            return True
        if choice == _("Hot springs") and leyna_work >= 4:
            return True
        if choice == _("Flowers") and leyna_work >= 8:
            return True
        if choice == _("Come back to hotsprings") and leyna_work >= 9:
            return True
        if choice == _("Photographer") and masks > 0 and leyna_work < 11:
            return True
        if choice == _("Photographer") and leyna_work >= 11:
            return True
        return False

    def set_disabled_choices(choices, called_from):
        for index, choice in enumerate(choices):
            if choice_is_disabled(choice, called_from):
                disable_choice(index + 1, visible=True)

    def get_done_count():
        all_choices = [
            "Bar 1",
            "Market",
            "Villagers",
            "River 1",
            "Photographer 1",
            "Hotsprings",
            "Photographer 2",
            "Bar 2",
            "River 2",
            "Photographer 3",
            "Worker's quest",
            "Dresser",
            "The dream",
            "Police station",
            "Night Party",
            "Police station",
            "Night Party",
            "Go to the festival",
            "Groceries store",
            "Bar",
            "Hot springs",
            "Flowers",
            "Come back to hotsprings",
            "Photographer",
        ]
        return len(list(filter(lambda choice: choice_is_disabled(choice, "Town"), all_choices)))

label GetChoice(choices, value = None, called_from = "", cancel = None, cancel_default = None):
    $ set_disabled_choices(choices, called_from)
    $ choice_result = get_choice(choices, value, called_from, cancel, cancel_default)
    $ reset_choices()
    if not called_from.startswith("InnRooms") and "TABLON" not in called_from:
        $ no_advancement_events = 0
    return choice_result