init python:
    def get_alternative_stealth_options(choices, stealth_events):
        stealth_index = 0
        new_options = []
        for choice in choices:
            if is_non_stealth_event(choice[0]):
                new_options.append(choice)
            else:
                new_options.append(stealth_events[stealth_index])
                stealth_index += 1
                if stealth_index >= len(stealth_events):
                    stealth_index = 0
        return new_options

    def get_stealth_events(choices):
        return list(filter(lambda choice: is_stealth_event(choice[0]), choices))

    def is_stealth_event(event):
        stealth_events = [
        ]
        return event in stealth_events

    def is_non_stealth_event(event):
        non_stealth_events = [
        ]
        return event in non_stealth_events

    def get_spotlights():
        return [{
            "image": "spot1200",
            "size": 1200,
            "pos": (960, 0),
            "anchor": (0.5, 1),
            "duration": 4,
            "middle_pause": 0,
            "end_pause": 0,
            "spread": 25,
            "offset": 0,
            "easing": "ease",
            "anglefromto": (180, 270),
        }]

define STEALTH_TEXT_SIZE = 28
define STEALTH_TEXT_HEIGHT = 48
define STEALTH_PADDING = 7
define STEALTH_WIDTH = 592

label StealthEvent(choices, stealth_events):
    $ choices_without_stealth_events = [choice for choice in choices if choice not in stealth_events]
    call screen stealth_screen(get_spotlights(), choices_without_stealth_events, get_alternative_stealth_options(choices_without_stealth_events, stealth_events))
    pause 0.5
    return _return