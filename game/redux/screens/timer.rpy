default game_timer_expired = 0
default show_timer = None

label StartGameTimer(time, called_from):
    $ game_timer_expired = 0
    $ show_timer = time
    return

label StopGameTimer(called_from):
    $ show_timer = None
    $ game_timer_expired = 0
    return

default timer_frame_timer = 0

screen timer_frame(timeout, timeout_actions = [], on_screen = True):
    timer 0.1:
        repeat True
        action If(
            timer_frame_timer > timeout, 
            false = SetVariable("timer_frame_timer", timer_frame_timer + 0.1), 
            true = [Hide("timer_frame"), SetVariable("timer_frame_timer", 0), SetVariable("game_timer_expired", 1), *timeout_actions]
        )
    if on_screen:
        fixed:
            vbox:
                xpos config.screen_width - 216
                ypos 86
                bar:
                    value AnimatedValue(value=timer_frame_timer if game_timer_expired == 0 else timeout, range=timeout, delay=0.5)
                    xmaximum 200