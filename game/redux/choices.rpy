default disabled_choices = []

init python:
    def reset_choices():
        global disabled_choices
        disabled_choices = []

    def disable_choice(choice, visible=False):
        global disabled_choices
        disabled_choices.append((choice, visible))

    def enable_choice(choice):
        global disabled_choices
        new_disabled_choices = []
        for disabled_choice in disabled_choices:
            if disabled_choice[0] != choice:
                new_disabled_choices.append(disabled_choice)
        disabled_choices = new_disabled_choices

    def choice_disabled(choice):
        for disabled, visible in disabled_choices:
            if choice == disabled:
                return True
        return False

    def choice_hidden(choice):
        for disabled, visible in disabled_choices:
            if choice == disabled:
                return not visible
        return False

    last_selected_choice = None

    def get_choice(choices, value = None, called_from = "", cancel = None, cancel_default = None):
        global last_selected_choice
        if value != None:
            return value
        filtered_choices = []
        if last_displayed_map != current_map:
            show_map_background()

        has_no = False
        all_disabled = True
        for index, choice in enumerate(choices):
            choice_value = type(choice) == tuple and choice[0] or choice
            choice_text = type(choice) == tuple and choice[1] or choice
            if (choice_disabled(index + 1) or (called_from != "" and seen_today(called_from + choice))) and not choice_hidden(index + 1):
                filtered_choices.append((choice_text, renpy.ui.ChoiceReturn(choice_text, choice_value, location=renpy.game.context().current, sensitive=False)))
            elif not choice_disabled(index + 1):
                filtered_choices.append((choice_text, choice_value))
                has_no = has_no or choice_text.lower() == "no"
                all_disabled = False
        if not has_no:
            if cancel == "last" and (allow_choice_cancel(called_from) or len(filtered_choices) == 1):
                filtered_choices.append(("Cancel", "_cancel_"))
                all_disabled = False
            if cancel == "default":
                filtered_choices.append(("Cancel", "_cancel_" if cancel_default == None or choices[cancel_default] == None else type(choices[cancel_default]) == tuple and choices[cancel_default][0] or choices[cancel_default]))
                all_disabled = False
        if len(filtered_choices) == 0:
            renpy.say(None, "get_choice() with 0 choices in " + current_map)
        if all_disabled:
            filtered_choices.append(("Cancel", "_cancel_"))
        selected_choice = renpy.display_menu(filtered_choices)
        last_selected_choice = selected_choice
        return selected_choice
