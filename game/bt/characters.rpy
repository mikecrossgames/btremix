init python:
    def get_event_title(e, location, locations):
        if current_map not in e["title"] and e["event"] != (current_map + e["title"]):
            title = e["title"]
        elif "NPC" in e["title"]:
            if len(e["title"]) > 5:
                title = e["title"][3:]
            else:
                title = "NPC " + e["title"][3:]
        else:
            title = e["title"] # + " @ " + str(e["xy"][0]) + "," + str(e["xy"][1])
        if current_map in locations:
            if location in locations[current_map]:
                if "events" in locations[current_map][location] and e["event"] in locations[current_map][location]["events"]:
                    title = locations[current_map][location]["events"][e["event"]]
        return title

    def get_choice_from_event(location):
        locations = get_locations()
        def get_choice_from_event_at_location(e):
            title = get_event_title(e, location, locations)
            if not title.endswith("."):
                title = title + "."
            return (e["event"], title)
        return get_choice_from_event_at_location

    def choice_sort_key(choice):
        xy = get_event_xy(choice[0])
        return xy[1] + (xy[0] / 128)

    def sorted_choices(choices):
        return sorted(choices, key=choice_sort_key)

define Leyna = Character("Leyna", color="#fa7a4b")
define Johan = Character("Johan", color="#65cc41")
define Prisoner = Character("Prisoner", color="#65cc41")
define Alexa = Character("Alexa", color="#ffffa3")
define Innkeeper = Character("Innkeeper", color="#bbbbbb")
define Grandson = Character("Grandson", color="#bbbbbb")
define Thug = Character("Thug", color="#bbbbbb")
define Kid = Character("Kid", color="#bbbbbb")
define Husband = Character("Husband", color="#bbbbbb")
define Wife = Character("Wife", color="#bbbbbb")
define OldMan = Character("Old man", color="#bbbbbb")
define DrunkOldMan = Character("Drunk old man", color="#bbbbbb")
define OldVillager = Character("Old villager", color="#bbbbbb")
define NakedVillager = Character("Naked villager", color="#bbbbbb")
define YoungVillager = Character("Young villager", color="#bbbbbb")
define YoungVillager2 = Character("Young villager 2", color="#bbbbbb")
define YoungVillager3 = Character("Young villager 3", color="#bbbbbb")
define Villager = Character("Villager", color="#bbbbbb")
define Villager1 = Character("Villager 1", color="#bbbbbb")
define Villager2 = Character("Villager 2", color="#bbbbbb")
define Villager3 = Character("Villager 3", color="#bbbbbb")
define MaleVoice = Character("Male voice", color="#bbbbbb")
define FemaleVoice = Character("Female voice", color="#bbbbbb")
define Unknown = Character("???", color="#bbbbbb")
define VillagerWoman = Character("Villager woman", color="#bbbbbb")
define VillagerMan = Character("Villager man", color="#bbbbbb")
define DrunkVillager = Character("Drunk villager", color="#bbbbbb")
define DrunkVillager2 = Character("Drunk villager 2", color="#bbbbbb")
define VillagerGirl = Character("Villager girl", color="#bbbbbb")
define Barman = Character("Barman", color="#bbbbbb")
define Receptionist = Character("Receptionist", color="#bbbbbb")
define DrunkTourist = Character("Drunk tourist", color="#bbbbbb")
define OldWoman = Character("Old woman", color="#bbbbbb")
define Tourist = Character("Tourist", color="#bbbbbb")
define Policeman = Character("Policeman", color="#bbbbbb")
define John = Character("John", color="#bbbbbb")
define Boy = Character("Boy", color="#bbbbbb")
define Officer = Character("Officer", color="#bbbbbb")
define PoliceCaptain = Character("Police captain", color="#bbbbbb")
define WomansVoice = Character("(Woman's voice)", color="#bbbbbb")
define Laura = Character("Laura", color="#bbbbbb")
define TV = Character("TV", color="#bbbbbb")
define Merchant = Character("Merchant", color="#bbbbbb")
define AlexasHusband = Character("Alexa's husband", color="#65cc41")
define WorkersSon = Character("Worker's son", color="#bbbbbb")
define Worker = Character("Worker", color="#bbbbbb")
define Villagers = Character("Villagers", color="#bbbbbb")
define Friend = Character("Friend", color="#bbbbbb")
define TouristWoman = Character("Tourist woman", color="#bbbbbb")
define Kevin = Character("Kevin", color="#bbbbbb")
define Daniela = Character("Daniela", color="#bbbbbb")
define CutMeOwnThroatDibbler = Character("Cut-Me-Own-Throat Dibbler", color="#bbbbbb")


