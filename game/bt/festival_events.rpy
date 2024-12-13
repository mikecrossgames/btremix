label FestivalDirection(map_name, event_name, x, y, play_event = True, trigger = None):
    if trigger == "event":
        if play_event:
            call TransferPlayer(map_name, event_name, x, y) from _TransferPlayer_FestivalDirection
        return (0, "", event_name)
    return None

label FestivalNorthStart():
    if "Night" in current_map:
        $ set_transparency_backgrounds(["bg_festival_night"])
        $ set_map_backgrounds(["map_festival_night"])
    else:
        $ set_transparency_backgrounds(["bg_festival"])
        $ set_map_backgrounds(["map_festival"])
    return

label FestivalSouthStart():
    if "Night" in current_map:
        $ set_transparency_backgrounds(["bg_festival_south_night"])
        $ set_map_backgrounds(["map_festival_south_night"])
    else:
        $ set_transparency_backgrounds(["bg_festival_south"])
        $ set_map_backgrounds(["map_festival_south"])
    return

# Festival

label FestivalNorthToSouth(play_event = True, trigger = None): # event
    call FestivalDirection("Festival", "FestivalNorthToSouth", 13, 15, play_event, trigger) from _TransferPlayer_FestivalNorthToSouth
    return _return

label FestivalSouthToNorth(play_event = True, trigger = None): # event
    call FestivalDirection("Festival", "FestivalSouthToNorth", 13, 12, play_event, trigger) from _TransferPlayer_FestivalSouthToNorth
    return _return

# FestivalNight

label FestivalNightNorthToSouth(play_event = True, trigger = None): # event
    call FestivalDirection("FestivalNight", "FestivalNightNorthToSouth", 13, 15, play_event, trigger) from _TransferPlayer_FestivalNightNorthToSouth
    return _return

label FestivalNightSouthToNorth(play_event = True, trigger = None): # event
    call FestivalDirection("FestivalNight", "FestivalNightSouthToNorth", 13, 12, play_event, trigger) from _TransferPlayer_FestivalNightSouthToNorth
    return _return

# FestivalFinale

label FestivalFinaleNorthToSouth(play_event = True, trigger = None): # event
    call FestivalDirection("FestivalFinale", "FestivalFinaleNorthToSouth", 13, 15, play_event, trigger) from _TransferPlayer_FestivalFinaleNorthToSouth
    return _return

label FestivalFinaleSouthToNorth(play_event = True, trigger = None): # event
    call FestivalDirection("FestivalFinale", "FestivalFinaleSouthToNorth", 13, 12, play_event, trigger) from _TransferPlayer_FestivalFinaleSouthToNorth
    return _return

