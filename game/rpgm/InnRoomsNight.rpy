label InnRoomsNightBG:
    $ set_transparency_backgrounds(["bg_inn_rooms"])
    $ set_map_backgrounds(["map_inn_rooms"])
    return

label InnRoomsNightStart:
    call InnRoomsNightBG from _call_InnRoomsNightBG
    stop music
    stop bgs
    return

label InnRoomsNightEnd:
    return

label InnRoomsNightToInnNightBase:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_InnRoomsNightEV001_PlaySound
    call TransferPlayer("InnNight", "InnRoomsNightEV001", 1, 0, direction=2) from _call_InnRoomsNightEV001_TransferPlayer
    $ resolve_scene()
    return False

label InnRoomsNightToInnNight(play_event = True, trigger = None): # event
    if is_erased("InnRoomsNightToInnNight"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnRoomsNightToInnNightBase", "InnRoomsNightToInnNight") from _call_InnRoomsNightToInnNight_PlayEvent
        return (0, "", "InnRoomsNightToInnNight")
    return None

label InnRoomsNightToInnNight_v2Base:
    call PlaySound("sound", "audio/Move1.ogg", volume=0.9, no_loop=True) from _call_InnRoomsNightEV002_PlaySound
    call TransferPlayer("InnNight", "InnRoomsNightEV002", 2, 0, direction=2) from _call_InnRoomsNightEV002_TransferPlayer
    $ resolve_scene()
    return False

label InnRoomsNightToInnNight_v2(play_event = True, trigger = None): # event
    if is_erased("InnRoomsNightToInnNight_v2"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnRoomsNightToInnNight_v2Base", "InnRoomsNightToInnNight_v2") from _call_InnRoomsNightToInnNight_v2_PlayEvent
        return (0, "", "InnRoomsNightToInnNight_v2")
    return None

label InnRoomsNightSleepBase(menu_choice = None):
    "Do you want to go to sleep?"
    call GetChoice([_("Yes"), _("No")], value=menu_choice, called_from="InnRoomsNightSleep") from _call_InnRoomsNightSleep_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Yes"):
        $ menu_choice = None
        $ fade_out()
        if not renpy.in_rollback():
            $ _saved_bgm = renpy.music.get_playing()
        play music "audio/Inn.ogg" volume 0.9 noloop
        if _saved_bgm is not None and not renpy.in_rollback():
            queue music _saved_bgm
            $ _saved_bgm = None
        call TransferPlayer("InnRooms", "InnRoomsNightSleep", 11, 11, direction=2) from _call_InnRoomsNightSleep_TransferPlayer
        $ resolve_scene()
        $ tint_screen((0, 0, 0, 0), 60, True)
        $ fade_in()
    elif menu_choice == _("No"):
        $ menu_choice = None
    $ resolve_scene()
    return False

label InnRoomsNightSleep(play_event = True, trigger = None): # event
    if is_erased("InnRoomsNightSleep"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnRoomsNightSleepBase", "InnRoomsNightSleep") from _call_InnRoomsNightSleep_PlayEvent
        return (1, "", "InnRoomsNightSleep")
    return None

label InnRoomsNightIchaIchaParadiseAuthorJiraiyaBase(menu_choice = None):
    "ICHA ICHA PARADISE - AUTHOR: JIRAIYA"
    "Do you want to read it?"
    call GetChoice([_("Yes"), _("No")], value=menu_choice, called_from="InnRoomsNightEV007") from _call_InnRoomsNightEV007_GetChoice
    $ menu_choice = _return
    if menu_choice == _("Yes"):
        $ menu_choice = None
        $ show_picture(1, "menofculture")
        $ resolve_scene()
        pause
    elif menu_choice == _("No"):
        $ menu_choice = None
        $ show_picture(2, "jiraiya")
        $ resolve_scene()
        pause
    $ erase_picture(1)
    $ erase_picture(2)
    $ resolve_scene()
    return False

label InnRoomsNightIchaIchaParadiseAuthorJiraiya(play_event = True, trigger = None): # event
    if is_erased("InnRoomsNightIchaIchaParadiseAuthorJiraiya"):
        return None
    elif trigger == "event":
        call PlayEvent(play_event, "InnRoomsNightIchaIchaParadiseAuthorJiraiyaBase", "InnRoomsNightIchaIchaParadiseAuthorJiraiya") from _call_InnRoomsNightIchaIchaParadiseAuthorJiraiya_PlayEvent
        return (1, "", "InnRoomsNightIchaIchaParadiseAuthorJiraiya")
    return None

