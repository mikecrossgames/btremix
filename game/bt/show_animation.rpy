label ShowAnimation(id, character, called_from):
    $ x = round(config.screen_width / 2)
    $ y = round(config.screen_height / 2)
    if called_from.startswith("BarWetTShirt"):    
        $ x = 540
        $ y = 480
    if called_from.startswith("PoliceStation"):    
        $ x = 303
        $ y = 380
    $ frame_time = 0.05
    $ end_pause = 0.24
    $ show_animation(id, x, y, frame_time, end_pause)
    return

transform fadetoeasein(old_alpha, new_alpha, duration=1.0):
    alpha old_alpha
    easein duration alpha new_alpha
