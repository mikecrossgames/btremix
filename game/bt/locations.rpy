init python:
    def show_event_screen(map, choices):
        definitely = [
            "Glade",
            "HotSpringsExterior",
            "PoliceStation",
            "Mountains",
            "HouseInterior",
            "Bar",
            "Bar2",
            "FoodStore",
            "ClothingStore",
            "River",
            "Reception",
        ]
        if map in definitely:
            return True
        definitely_not = ["MassageParlor", "TownEntrance"]
        if map in definitely_not:
            return False
        yes_group = ["Apartment", "Inn", "Town", "Path", "Festival"]
        for starts_with in yes_group:
            if map.startswith(starts_with):
                return True
        not_group = []
        for starts_with in not_group:
            if map.startswith(starts_with):
                return False
        return len(choices) > 1

    def get_festival_location(map_name):
        return {
            "North": {
                "bounds": [[0,0],[26,13]],
                "fit_to_map_bounds": True, # @TODO respect this
                "start_event": "FestivalNorthStart",
                "extra_events": [
                    {
                        "event": map_name + "NorthToSouth",
                        "title": "Continue",
                        "pos": [13, 12]
                    },
                ],
            },
            "South": {
                "bounds": [[0,13],[26,26]],
                "fit_to_map_bounds": True,
                "start_event": "FestivalSouthStart",
                "extra_events": [
                    {
                        "event": map_name + "SouthToNorth",
                        "title": "Back",
                        "pos": [13, 14]
                    },
                ]
            },
        }

    def get_town_location(map_name):
        return {
            "North": {
                "bounds": [[0,0],[50,12]],
                "fit_to_map_bounds": True, # @TODO respect this
                "start_event": "TownNorthStart",
                "extra_events": [
                    {
                        "event": map_name + "NorthToCenter",
                        "title": "Back to town",
                        "pos": [25, 12]
                    },
                ],
            },
            "East": {
                "bounds": [[32,13],[50,32]],
                "fit_to_map_bounds": True, # @TODO respect this
                "start_event": "TownEastStart",
                "extra_events": [
                    {
                        "event": map_name + "EastToCenter",
                        "title": "Back to town square",
                        "pos": [33, 22]
                    },
                    {
                        "event": map_name + "EastToSouthEast",
                        "title": "To village green",
                        "pos": [49, 22]
                    },
                ]
            },
            "West": {
                "bounds": [[0,13],[8,32]],
                "fit_to_map_bounds": True, # @TODO respect this
                "start_event": "TownWestStart",
                "extra_events": [
                    {
                        "event": map_name + "WestToCenter",
                        "title": "Back to market",
                        "pos": [6, 22]
                    },
                ]
            },
            "CenterWest": {
                "bounds": [[8,13],[17,32]],
                "fit_to_map_bounds": True,
                "start_event": "TownCenterWestStart",
                "extra_events": [
                    {
                        "event": map_name + "CenterWestToCenter",
                        "title": "Back to town square",
                        "pos": [16, 22]
                    },
                    {
                        "event": map_name + "CenterWestToWest",
                        "title": "To village edge",
                        "pos": [9, 22]
                    },
                ],
            },
            "Center": {
                "bounds": [[18,13],[31,32]],
                "fit_to_map_bounds": True,
                "start_event": "TownCenterStart",
                "extra_events": [
                    {
                        "event": map_name + "CenterToNorth",
                        "title": "To upper town",
                        "pos": [25, 18]
                    },
                    {
                        "event": map_name + "CenterToSouth",
                        "title": "To bar",
                        "pos": [25, 28]
                    },
                    {
                        "event": map_name + "CenterToEast",
                        "title": "To stores",
                        "pos": [30, 22]
                    },
                    {
                        "event": map_name + "CenterToCenterWest",
                        "title": "To market",
                        "pos": [19, 22]
                    },
                ]
            },
            "South": {
                "bounds": [[0,33],[37,50]],
                "fit_to_map_bounds": True,
                "start_event": "TownSouthStart",
                "extra_events": [
                    {
                        "event": map_name + "SouthToCenter",
                        "title": "Back to town square",
                        "pos": [25, 33]
                    },
                    {
                        "event": map_name + "SouthToSouthEast",
                        "title": "To village green",
                        "pos": [36, 41]
                    },
                ]
            },
            "SouthEast": {
                "bounds": [[38,33],[50,50]],
                "fit_to_map_bounds": True,
                "start_event": "TownSouthEastStart",
                "extra_events": [
                    {
                        "event": map_name + "SouthEastToSouth",
                        "title": "Back to bar",
                        "pos": [39, 41]
                    },
                    {
                        "event": map_name + "SouthEastToEast",
                        "title": "To stores",
                        "pos": [44, 34]
                    },
                ]
            }
        }

    def get_locations():
        return {
            "Town": get_town_location("Town"),
            "Town2": get_town_location("Town2"),
            "TownNight": get_town_location("TownNight"),
            "TownFestivalNight": get_town_location("TownFestivalNight"),
            "Festival": get_festival_location("Festival"),
            "FestivalFinale": get_festival_location("FestivalFinale"),
            "FestivalNight": get_festival_location("FestivalNight"),
        }

    def get_movement_direction():
        return {
        }

    def get_preceding_events():
        return {
            "InnCantLeave": ["InnToTown"],
            "Townfinaldelprimerdia": "*",
            "TownToRiverEvent": ["TownToRiver"],
            "TownNPCEntryFestival": ["TownToPath"],
            "Townespacioentradafestival": ["TownToPath"],
            "Towneventofotografiaintro": ["Townfotografo"],
            "Town2ToRiverEvent": ["Town2ToRiver"],
            "Town2finaldelprimerdia": "*",
            "TownCorruptionFairy": ["TownCorruptionCounter"],
            "Town2CorruptionFairy": ["Town2CorruptionCounter"],
            "Town2MeetPhotographer": ["Town2fotografo"],
            "Town2IHaveToFindThatGuy": ["Town2ToInn"],
            "TownFestivalNightimpedimento": ["TownFestivalNightToInnNight"],
            "TownFestivalNightIShouldLookForJohanThisGameHasGoneLongerThanIdLike": ["TownFestivalNightEastToCenter"],
            "PathLeynaWorkTrigger": ["PathToHotSpringsExterior", "Pathespacioentradafestival"],
            "Towneventolemetenmanobarrio": ["TownNPCDrunkEvent1"],
            "TownIShouldGoToTheInnJohannIsWaitingForMe": ["TownEastToSouthEast"],
            "TownIShouldGoToTheInnJohannIsWaitingForMe_v10": ["TownCenterToNorth"],
            "TownIShouldGoToTheInnJohannIsWaitingForMe_v11": ["TownCenterToCenterWest"],
            "TownIShouldGoToTheInnJohannIsWaitingForMe_v12": ["TownCenterToSouth"],
            "PathNPCFestivalWorker": ["PathNPCFestivalWorker2"],
            "PathWowItLooksLikeTheHotspringsHaveReopened": ["PathToHotSpringsExterior"],
            "FestivalNightLeynaropa": ["FestivalNightnosalida"],
            "FestivalNightICantGoDressedLikeThisWhatWouldJohanThink": ["FestivalNightNorthToSouth"],
        }

    def connected_maps(from_map, to_map):
        starts_withs = ["Inn"]
        for starts_with in starts_withs:
            if from_map.startswith(starts_with) and to_map.startswith(starts_with):
                return_obj = {}
                return_obj[from_map] = [to_map]
                return_obj[to_map] = [from_map]
                return return_obj
        return {}

define min_square_sizes = {
}