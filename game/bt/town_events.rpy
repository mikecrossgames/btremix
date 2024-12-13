label TownDirection(map_name, event_name, x, y, play_event = True, trigger = None):
    if trigger == "event":
        if play_event:
            call TransferPlayer(map_name, event_name, x, y) from _TransferPlayer_TownDirection
        return (0, "", event_name)
    return None

# Town 
label TownCenterStart():
    if current_map == "TownFestivalNight":
        $ set_transparency_backgrounds(["bg_town_center_night"])
        $ set_map_backgrounds(["map_town_center_festival_night"])
    elif "Night" in current_map or (current_map == "Town" and switch("second_river")):
        $ set_transparency_backgrounds(["bg_town_center_night"])
        $ set_map_backgrounds(["map_town_center_night"])
    else:
        $ set_transparency_backgrounds(["bg_town_center"])
        $ set_map_backgrounds(["map_town_center"])
    return

label TownNorthStart():
    if "Night" in current_map or (current_map == "Town" and switch("second_river")):
        $ set_transparency_backgrounds(["bg_town_north", "midbg_night"])
        $ set_map_backgrounds(["map_town_north_night"])
    else:
        $ set_transparency_backgrounds(["bg_town_north", "midbg"])
        $ set_map_backgrounds(["map_town_north"])
    return

label TownSouthStart():
    if "Night" in current_map or (current_map == "Town" and switch("second_river")):
        $ set_transparency_backgrounds(["bg_town_south_night"])
        $ set_map_backgrounds(["map_town_south_night"])
    else:
        $ set_transparency_backgrounds(["bg_town_south"])
        $ set_map_backgrounds(["map_town_south"])
    return

label TownSouthEastStart():
    if "Night" in current_map or (current_map == "Town" and switch("second_river")):
        $ set_transparency_backgrounds(["bg_town_south_east_night"])
        $ set_map_backgrounds(["map_town_south_east_night"])
    else:
        $ set_transparency_backgrounds(["bg_town_south_east"])
        $ set_map_backgrounds(["map_town_south_east"])
    return

label TownEastStart():
    if "Night" in current_map or (current_map == "Town" and switch("second_river")):
        $ set_transparency_backgrounds(["bg_town_east_night"])
        $ set_map_backgrounds(["map_town_east_night"])
    else:
        $ set_transparency_backgrounds(["bg_town_east"])
        $ set_map_backgrounds(["map_town_east"])
    return

label TownWestStart():
    if "Night" in current_map or (current_map == "Town" and switch("second_river")):
        $ set_transparency_backgrounds(["bg_town_west_night"])
        $ set_map_backgrounds(["map_town_west_night"])
    else:
        $ set_transparency_backgrounds(["bg_town_west"])
        $ set_map_backgrounds(["map_town_west"])
    return

label TownCenterWestStart():
    if "Night" in current_map or (current_map == "Town" and switch("second_river")):
        $ set_transparency_backgrounds(["bg_town_center_west_night"])
        $ set_map_backgrounds(["map_town_center_west_night"])
    else:
        $ set_transparency_backgrounds(["bg_town_center_west"])
        $ set_map_backgrounds(["map_town_center_west"])
    return

label TownNorthToCenter(play_event = True, trigger = None): # event
    call TownDirection("Town", "TownNorthToCenter", 20, 14, play_event, trigger) from _TransferPlayer_TownNorthToCenter
    return _return

label TownCenterToNorth(play_event = True, trigger = None): # event
    call TownDirection("Town", "TownCenterToNorth", 20, 11, play_event, trigger) from _TransferPlayer_TownCenterToNorth
    return _return

label TownCenterToCenterWest(play_event = True, trigger = None): # event
    call TownDirection("Town", "TownCenterToCenterWest", 16, 22, play_event, trigger) from _TransferPlayer_TownCenterToCenterWest
    return _return

label TownCenterWestToWest(play_event = True, trigger = None): # event
    call TownDirection("Town", "TownCenterWestToWest", 7, 22, play_event, trigger) from _TransferPlayer_TownCenterWestToWest
    return _return

label TownCenterWestToCenter(play_event = True, trigger = None): # event
    call TownDirection("Town", "TownCenterWestToCenter", 20, 22, play_event, trigger) from _TransferPlayer_TownCenterWestToCenter
    return _return

label TownWestToCenter(play_event = True, trigger = None): # event
    call TownDirection("Town", "TownWestToCenter", 10, 22, play_event, trigger) from _TransferPlayer_TownWestToCenter
    return _return

label TownCenterToEast(play_event = True, trigger = None): # event
    call TownDirection("Town", "TownCenterToEast", 34, 22, play_event, trigger) from _TransferPlayer_TownCenterToEast
    return _return

label TownEastToCenter(play_event = True, trigger = None): # event
    call TownDirection("Town", "TownEastToCenter", 30, 22, play_event, trigger) from _TransferPlayer_TownEastToCenter
    return _return

label TownCenterToSouth(play_event = True, trigger = None): # event
    call TownDirection("Town", "TownCenterToSouth", 20, 34, play_event, trigger) from _TransferPlayer_TownCenterToSouth
    return _return

label TownSouthToCenter(play_event = True, trigger = None): # event
    call TownDirection("Town", "TownSouthToCenter", 20, 29, play_event, trigger) from _TransferPlayer_TownSouthToCenter
    return _return

label TownSouthToSouthEast(play_event = True, trigger = None): # event
    call TownDirection("Town", "TownSouthToSouthEast", 39, 42, play_event, trigger) from _TransferPlayer_TownSouthToSouthEast
    return _return

label TownSouthEastToSouth(play_event = True, trigger = None): # event
    call TownDirection("Town", "TownSouthEastToSouth", 36, 42, play_event, trigger) from _TransferPlayer_TownSouthEastToSouth
    return _return

label TownEastToSouthEast(play_event = True, trigger = None): # event
    call TownDirection("Town", "TownEastToSouthEast", 39, 42, play_event, trigger) from _TransferPlayer_TownEastToSouthEast
    return _return

label TownSouthEastToEast(play_event = True, trigger = None): # event
    call TownDirection("Town", "TownSouthEastToEast", 34, 22, play_event, trigger) from _TransferPlayer_TownSouthEastToEast
    return _return

# Town2
label Town2NorthToCenter(play_event = True, trigger = None): # event
    call TownDirection("Town2", "Town2NorthToCenter", 20, 14, play_event, trigger) from _TransferPlayer_Town2NorthToCenter
    return _return

label Town2CenterToNorth(play_event = True, trigger = None): # event
    call TownDirection("Town2", "Town2CenterToNorth", 20, 11, play_event, trigger) from _TransferPlayer_Town2CenterToNorth
    return _return

label Town2CenterToCenterWest(play_event = True, trigger = None): # event
    call TownDirection("Town2", "Town2CenterToCenterWest", 16, 22, play_event, trigger) from _TransferPlayer_Town2CenterToCenterWest
    return _return

label Town2CenterWestToWest(play_event = True, trigger = None): # event
    call TownDirection("Town2", "Town2CenterWestToWest", 7, 22, play_event, trigger) from _TransferPlayer_Town2CenterWestToWest
    return _return

label Town2CenterWestToCenter(play_event = True, trigger = None): # event
    call TownDirection("Town2", "Town2CenterWestToCenter", 20, 22, play_event, trigger) from _TransferPlayer_Town2CenterWestToCenter
    return _return

label Town2WestToCenter(play_event = True, trigger = None): # event
    call TownDirection("Town2", "Town2WestToCenter", 10, 22, play_event, trigger) from _TransferPlayer_Town2WestToCenter
    return _return

label Town2CenterToEast(play_event = True, trigger = None): # event
    call TownDirection("Town2", "Town2CenterToEast", 34, 22, play_event, trigger) from _TransferPlayer_Town2CenterToEast
    return _return

label Town2EastToCenter(play_event = True, trigger = None): # event
    call TownDirection("Town2", "Town2EastToCenter", 30, 22, play_event, trigger) from _TransferPlayer_Town2EastToCenter
    return _return

label Town2CenterToSouth(play_event = True, trigger = None): # event
    call TownDirection("Town2", "Town2CenterToSouth", 20, 34, play_event, trigger) from _TransferPlayer_Town2CenterToSouth
    return _return

label Town2SouthToCenter(play_event = True, trigger = None): # event
    call TownDirection("Town2", "Town2SouthToCenter", 20, 29, play_event, trigger) from _TransferPlayer_Town2SouthToCenter
    return _return

label Town2SouthToSouthEast(play_event = True, trigger = None): # event
    call TownDirection("Town2", "Town2SouthToSouthEast", 39, 42, play_event, trigger) from _TransferPlayer_Town2SouthToSouthEast
    return _return

label Town2SouthEastToSouth(play_event = True, trigger = None): # event
    call TownDirection("Town2", "Town2SouthEastToSouth", 36, 42, play_event, trigger) from _TransferPlayer_Town2SouthEastToSouth
    return _return

label Town2EastToSouthEast(play_event = True, trigger = None): # event
    call TownDirection("Town2", "Town2EastToSouthEast", 39, 42, play_event, trigger) from _TransferPlayer_Town2EastToSouthEast
    return _return

label Town2SouthEastToEast(play_event = True, trigger = None): # event
    call TownDirection("Town2", "Town2SouthEastToEast", 34, 22, play_event, trigger) from _TransferPlayer_Town2SouthEastToEast
    return _return

# TownNight
label TownNightNorthToCenter(play_event = True, trigger = None): # event
    call TownDirection("TownNight", "TownNightNorthToCenter", 20, 14, play_event, trigger) from _TransferPlayer_TownNightNorthToCenter
    return _return

label TownNightCenterToNorth(play_event = True, trigger = None): # event
    call TownDirection("TownNight", "TownNightCenterToNorth", 20, 11, play_event, trigger) from _TransferPlayer_TownNightCenterToNorth
    return _return

label TownNightCenterToCenterWest(play_event = True, trigger = None): # event
    call TownDirection("TownNight", "TownNightCenterToCenterWest", 16, 22, play_event, trigger) from _TransferPlayer_TownNightCenterToCenterWest
    return _return

label TownNightCenterWestToWest(play_event = True, trigger = None): # event
    call TownDirection("TownNight", "TownNightCenterWestToWest", 7, 22, play_event, trigger) from _TransferPlayer_TownNightCenterWestToWest
    return _return

label TownNightCenterWestToCenter(play_event = True, trigger = None): # event
    call TownDirection("TownNight", "TownNightCenterWestToCenter", 20, 22, play_event, trigger) from _TransferPlayer_TownNightCenterWestToCenter
    return _return

label TownNightWestToCenter(play_event = True, trigger = None): # event
    call TownDirection("TownNight", "TownNightWestToCenter", 10, 22, play_event, trigger) from _TransferPlayer_TownNightWestToCenter
    return _return

label TownNightCenterToEast(play_event = True, trigger = None): # event
    call TownDirection("TownNight", "TownNightCenterToEast", 34, 22, play_event, trigger) from _TransferPlayer_TownNightCenterToEast
    return _return

label TownNightEastToCenter(play_event = True, trigger = None): # event
    call TownDirection("TownNight", "TownNightEastToCenter", 30, 22, play_event, trigger) from _TransferPlayer_TownNightEastToCenter
    return _return

label TownNightCenterToSouth(play_event = True, trigger = None): # event
    call TownDirection("TownNight", "TownNightCenterToSouth", 20, 34, play_event, trigger) from _TransferPlayer_TownNightCenterToSouth
    return _return

label TownNightSouthToCenter(play_event = True, trigger = None): # event
    call TownDirection("TownNight", "TownNightSouthToCenter", 20, 29, play_event, trigger) from _TransferPlayer_TownNightSouthToCenter
    return _return

label TownNightSouthToSouthEast(play_event = True, trigger = None): # event
    call TownDirection("TownNight", "TownNightSouthToSouthEast", 39, 42, play_event, trigger) from _TransferPlayer_TownNightSouthToSouthEast
    return _return

label TownNightSouthEastToSouth(play_event = True, trigger = None): # event
    call TownDirection("TownNight", "TownNightSouthEastToSouth", 36, 42, play_event, trigger) from _TransferPlayer_TownNightSouthEastToSouth
    return _return

label TownNightEastToSouthEast(play_event = True, trigger = None): # event
    call TownDirection("TownNight", "TownNightEastToSouthEast", 39, 42, play_event, trigger) from _TransferPlayer_TownNightEastToSouthEast
    return _return

label TownNightSouthEastToEast(play_event = True, trigger = None): # event
    call TownDirection("TownNight", "TownNightSouthEastToEast", 34, 22, play_event, trigger) from _TransferPlayer_TownNightSouthEastToEast
    return _return

# TownFestivalNight
label TownFestivalNightNorthToCenter(play_event = True, trigger = None): # event
    call TownDirection("TownFestivalNight", "TownFestivalNightNorthToCenter", 20, 14, play_event, trigger) from _TransferPlayer_TownFestivalNightNorthToCenter
    return _return

label TownFestivalNightCenterToNorth(play_event = True, trigger = None): # event
    call TownDirection("TownFestivalNight", "TownFestivalNightCenterToNorth", 20, 11, play_event, trigger) from _TransferPlayer_TownFestivalNightCenterToNorth
    return _return

label TownFestivalNightCenterToCenterWest(play_event = True, trigger = None): # event
    call TownDirection("TownFestivalNight", "TownFestivalNightCenterToCenterWest", 16, 22, play_event, trigger) from _TransferPlayer_TownFestivalNightCenterToCenterWest
    return _return

label TownFestivalNightCenterWestToWest(play_event = True, trigger = None): # event
    call TownDirection("TownFestivalNight", "TownFestivalNightCenterWestToWest", 7, 22, play_event, trigger) from _TransferPlayer_TownFestivalNightCenterWestToWest
    return _return

label TownFestivalNightCenterWestToCenter(play_event = True, trigger = None): # event
    call TownDirection("TownFestivalNight", "TownFestivalNightCenterWestToCenter", 20, 22, play_event, trigger) from _TransferPlayer_TownFestivalNightCenterWestToCenter
    return _return

label TownFestivalNightWestToCenter(play_event = True, trigger = None): # event
    call TownDirection("TownFestivalNight", "TownFestivalNightWestToCenter", 10, 22, play_event, trigger) from _TransferPlayer_TownFestivalNightWestToCenter
    return _return

label TownFestivalNightCenterToEast(play_event = True, trigger = None): # event
    call TownDirection("TownFestivalNight", "TownFestivalNightCenterToEast", 34, 22, play_event, trigger) from _TransferPlayer_TownFestivalNightCenterToEast
    return _return

label TownFestivalNightEastToCenter(play_event = True, trigger = None): # event
    call TownDirection("TownFestivalNight", "TownFestivalNightEastToCenter", 30, 22, play_event, trigger) from _TransferPlayer_TownFestivalNightEastToCenter
    return _return

label TownFestivalNightCenterToSouth(play_event = True, trigger = None): # event
    call TownDirection("TownFestivalNight", "TownFestivalNightCenterToSouth", 20, 34, play_event, trigger) from _TransferPlayer_TownFestivalNightCenterToSouth
    return _return

label TownFestivalNightSouthToCenter(play_event = True, trigger = None): # event
    call TownDirection("TownFestivalNight", "TownFestivalNightSouthToCenter", 20, 29, play_event, trigger) from _TransferPlayer_TownFestivalNightSouthToCenter
    return _return

label TownFestivalNightSouthToSouthEast(play_event = True, trigger = None): # event
    call TownDirection("TownFestivalNight", "TownFestivalNightSouthToSouthEast", 39, 42, play_event, trigger) from _TransferPlayer_TownFestivalNightSouthToSouthEast
    return _return

label TownFestivalNightSouthEastToSouth(play_event = True, trigger = None): # event
    call TownDirection("TownFestivalNight", "TownFestivalNightSouthEastToSouth", 36, 42, play_event, trigger) from _TransferPlayer_TownFestivalNightSouthEastToSouth
    return _return

label TownFestivalNightEastToSouthEast(play_event = True, trigger = None): # event
    call TownDirection("TownFestivalNight", "TownFestivalNightEastToSouthEast", 39, 42, play_event, trigger) from _TransferPlayer_TownFestivalNightEastToSouthEast
    return _return

label TownFestivalNightSouthEastToEast(play_event = True, trigger = None): # event
    call TownDirection("TownFestivalNight", "TownFestivalNightSouthEastToEast", 34, 22, play_event, trigger) from _TransferPlayer_TownFestivalNightSouthEastToEast
    return _return

