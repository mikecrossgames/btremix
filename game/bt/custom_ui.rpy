init python:
    def has_custom_ui():
        return True

    def display_normal_ui():
        return True

    def is_custom_ui_event(event):
        return event[0] in ["TownGoNorth", "TownGoEast", "TownGoSouth", "TownGoWest"]

screen custom_ui(events_with_priorities):
    python:
        direction_events = []
        for event, priority in events_with_priorities:
            if is_custom_ui_event(event):
                direction_events.append((event, priority[0], priority[1]))

    use direction_list(direction_events)

screen help_icon():
    tag helpicon