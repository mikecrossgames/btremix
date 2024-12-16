init python:
    def shake_screen():
        power = 5
        speed = 5
        duration = 60
        size = power * speed
        delay = duration / 120
        renpy.with_statement(Move((size, 0), (-size, 0), 0.5 / power, repeat = True, bounce = True, delay=delay))
