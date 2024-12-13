init python:
    def get_steps(quest):
        new_steps = []
        for step in range(len(quest["steps"])):
            new_steps.append((quest["steps"][step], objective_complete(quest["id"], step), objective_revealed(quest["id"], step)))
        return new_steps

    def set_focused_quest(quest):
        global focused_quest
        focused_quest = quest

    def all_quests_of_type(type_of_interest):
        return get_active_quests() if type_of_interest == "active" else get_completed_quests() if type_of_interest == "completed" else get_failed_quests()

    def get_focused_quest(type_of_interest):
        quest_of_interest = None
        all_quests = all_quests_of_type(type_of_interest)
        for quest in all_quests:
            if quest["id"] == focused_quest:
                quest_of_interest = quest
        if quest_of_interest is None and len(all_quests) > 0:
            quest_of_interest = all_quests[0]
        return quest_of_interest

default focused_quest = None

screen quests():
    python:
        keys = get_ui_key_actions()
        actions = {}
        for key, action in keys:
            if not isinstance(action, list):
                actions[key] = action # for NullAction()
            elif key != "1":
                actions[key] = [Function(ui_return_action("quests")), *action]
            else:
                actions[key] = Function(ui_return_action("quests"))
        default_quest_type = "failed" if last_updated_quest is not None and last_updated_quest[1] == "failed" else "completed" if last_updated_quest is not None and last_updated_quest[1] == "completed" else "active"

    for key, action in keys:
        key [key] action actions[key]

    default quest_type = default_quest_type
    zorder 200
    modal True
    tag gameui
    use gameui(
            "Quests", 
            Function(ui_return_action("quests")), 
            background=Image(get_filename("menubg")),
            subs=[
                ("Active (" + str(len(all_quests_of_type("active"))) + ")", SetScreenVariable("quest_type", "active"), quest_type == "active"), 
                ("Completed (" + str(len(all_quests_of_type("completed"))) + ")", SetScreenVariable("quest_type", "completed"), quest_type == "completed"),
                ("Failed (" + str(len(all_quests_of_type("failed"))) + ")", SetScreenVariable("quest_type", "failed"), quest_type == "failed"),
            ],
        ):
        vbox:
            xpos 180
            frame:
                ypos 24
                ysize 474
                xsize 720
                background None
                use quest_details(get_focused_quest(quest_type))
            if len(all_quests_of_type(quest_type)) > 1:
                side "c r":
                    area (100, 24, 520, 210)
                    viewport id "quest_list":
                        draggable True 
                        mousewheel True
                        frame:
                            xsize 420 - gui.bar_size
                            background None
                            vbox:
                                for quest in all_quests_of_type(quest_type):
                                    use quest_select(quest, quest_type)
                    if len(all_quests_of_type(quest_type)) > 6:
                        vbar value YScrollValue("quest_list")
                    else:
                        null width gui.bar_size

screen quest_select(quest, quest_type):
    python:
        col = "#FFFFFF" if quest["id"] != get_focused_quest(quest_type)["id"] else gui.hover_color

    hbox:
        if quest["category"] == "main":
            text "⭐" font "emoji.ttf" color "#fefd3e" size 24
        else:
            text "⭐" font "emoji.ttf" color "#bbbbbb" size 24

        textbutton quest["title"]:
            action Function(set_focused_quest, quest["id"])
            text_size 24
            text_color col
            text_hover_color gui.hover_color

screen quest_details(quest):
    vbox:
        if quest is not None:
            text quest["title"]:
                xalign 0.5
                color gui.hover_color
                size 32
            null height 16
            hbox:
                xsize 720
                hbox:
                    xalign 0
                    text "Client: "
                    text quest["client"] color gui.hover_color
                hbox:
                    xalign 1.0
                    text "Location: "
                    text quest["location"] color gui.hover_color
            null height 16
            text "Description":
                xalign 0.5
                color gui.hover_color
            text quest["description"]:
                xalign 0.5
            null height 16
            text "Objectives":
                xalign 0.5
                color gui.hover_color
            vbox:
                xalign 0.5
                for step in get_steps(quest):
                    hbox:
                        if not step[2]:
                            text "▫️" font "emoji.ttf" color "#bbbbbb80"
                            text " " + step[0] color "#bbbbbb80"
                        else:
                            if step[1]:
                                text "✅" font "emoji.ttf" color "#00e000"
                            else:
                                text "▫️" font "emoji.ttf"
                            text " " + step[0]
            null height 16
            text "Rewards":
                xalign 0.5
                color gui.hover_color
            vbox:
                xalign 0.5
                hbox:
                    if quest["rewards"][0] == "gold":
                        text "🪙" font "emoji.ttf" color "#FFD700"
                    elif quest["rewards"][1] == 122:
                        text "♥️" font "emoji.ttf" color "#ff0000"
                    else:
                        text "⭐" font "emoji.ttf" color "#fefd3e"
                    if len(quest["rewards"]) >= 4:
                        text " " + quest["rewards"][3] + " "
                    else:
                        text " " + str(quest["rewards"][1]) + " "
                    if quest["rewards"][0] == "gold":
                        text get_money_name()