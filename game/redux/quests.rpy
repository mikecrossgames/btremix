default quest_ids = []
default completed_quest_ids = []
default failed_quest_ids = []
default previous_quest_ids = []

init python:
    def has_new_quests(active_quests):
        if previous_quest_ids == None:
            return False
        return len(active_quests) != len(previous_quest_ids) or not all(map(lambda x: x[0]["id"] == x[1], zip(active_quests, previous_quest_ids)))

    def get_new_quests():
        global previous_quest_ids, shown_quest
        active_quests = get_active_quests()
        new_quests = has_new_quests(active_quests)
        if new_quests:
            shown_quest = None
        previous_quest_ids = list(map(lambda x: x["id"], active_quests))
        return new_quests

    def add_quest(quest):
        if quest not in quest_ids:
            quest_ids.append(quest)

    def quest_is_active(quest):
        return quest in quest_ids

    def quest_revealed(quest):
        return quest_is_active(quest) or quest_complete(quest) or quest_failed(quest)

    def quest_complete(quest):
        return quest in completed_quest_ids

    def quest_failed(quest):
        return quest in failed_quest_ids

    def remove_quest(quest):
        global quest_ids
        quest_ids = list(filter(lambda x: x != quest, quest_ids))

    def add_completed_quest(quest):
        global completed_quest_ids
        if quest not in completed_quest_ids:
            completed_quest_ids.append(quest)

    def add_failed_quest(quest):
        global failed_quest_ids
        if quest not in failed_quest_ids:
            failed_quest_ids.append(quest)

    def get_active_quests():
        return list(map(get_quest_by_id, quest_ids))

    def get_completed_quests():
        return list(reversed(list(map(get_quest_by_id, completed_quest_ids))))

    def get_failed_quests():
        return list(reversed(list(map(get_quest_by_id, failed_quest_ids))))

    def get_quest_by_id(quest_id):
        return next((x for x in get_rpgm_quests() if x["id"] == quest_id), None)

label QuestAdd(quest):
    $ add_quest(quest)
    # $ renpy.notify("New quest: " + get_quest_by_id(quest)["title"])
    return

label QuestUpdated(quest):
    # $ renpy.notify("Quest updated: " + get_quest_by_id(quest)["title"])
    return

label QuestComplete(quest):
    if quest_is_active(quest):
        $ add_completed_quest(quest)
        $ remove_quest(quest)
        # $ renpy.notify("Quest complete: " + get_quest_by_id(quest)["title"])
    return

label QuestFailed(quest):
    if quest_is_active(quest):
        $ add_failed_quest(quest)
        $ remove_quest(quest)
        # $ renpy.notify("Quest complete: " + get_quest_by_id(quest)["title"])
    return

label DeleteQuest(quest):
    $ remove_quest(quest)
    return
