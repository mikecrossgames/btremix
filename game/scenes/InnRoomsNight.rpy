label InnRoomsNightSleep:
    "Do you want to go to sleep?"
    menu:
        "Yes":
            scene black with dissolve
            if not renpy.in_rollback():
                $ _saved_bgm = renpy.music.get_playing()
            play music "audio/Inn.ogg" volume 0.9 noloop
            if _saved_bgm is not None and not renpy.in_rollback():
                queue music _saved_bgm
                $ _saved_bgm = None
            call SetPlayerLocation("InnRooms") from _call_InnRoomsNightSleep_SetPlayerLocation
            # fade in
        "No":
            pass
    return

