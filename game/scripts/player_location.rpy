default player_location = "Intro"

define location_names = {
    "Town": "Town",
    "Inn": "Inn",
    "River": "River",
    "InnRooms": "Inn Rooms",
    "Festival": "Festival",
    "Bar": "Bar",
    "FoodStore": "Food Store",
    "ClothingStore": "Clothing Store",
    "TownEntrance": "Entrance to Town",
    "Apartment": "Apartment",
    "Intro": "Intro",
    "HouseInterior": "House Interior",
    "HotSpringsExterior": "Hot Springs Exterior",
    "HotSpringsBathroom": "Hot Springs Bathroom",
    "Reception": "Hot Springs Reception",
    "Path": "Path",
    "PhotographersHouse": "Photographer's House",
    "PoliceStation": "Police Station",
    "Glade": "Glade",
    "River2": "River",
    "HotSprings": "Hot Springs",
    "Photoshoot2": "Photographer's House",
    "TownNight": "Town at night",
    "InnNight": "Inn at night",
    "InnRoomsNight": "Inn Rooms at night",
    "Town2": "Town",
    "Bar2": "Bar",
    "Mountains": "Mountains",
    "Casino": "Casino",
    "MassageParlor": "Massage Parlor",
    "TownFestivalNight": "Town at Night",
    "HotSpringsWithJohan": "Hot Springs",
    "FestivalNight": "Festival at night",
    "Gallery": "Gallery",
    "FestivalFinale": "Festival",
    "CasinoFinale": "Casino",
    "ApartmentEnding": "Apartment",
    "ApartmentGroundFloor": "Apartment",
}

label SetPlayerLocation(location):
    if location in location_names and player_location != location:
        $ location_name = location_names[location]
        show text "Go to [location_name]" at truecenter
        pause
        hide text
    $ player_location = location
    return