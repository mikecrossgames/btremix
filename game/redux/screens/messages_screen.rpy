init python:
    def set_focused_message(message):
        global focused_message
        focused_message = message

    def all_messages_of_type(type_of_interest):
        return get_unread_messages() if type_of_interest == "unread" else get_read_messages() if type_of_interest == "read" else get_all_messages()

    def get_focused_message(type_of_interest):
        message_of_interest = None
        all_messages = all_messages_of_type(type_of_interest)
        for message in all_messages:
            if message["id"] == focused_message:
                message_of_interest = message
        if message_of_interest is None and len(all_messages) > 0:
            message_of_interest = all_messages[0]
        return message_of_interest

    def mark_items_as_read(ids):
        def perform_function():
            unread_ids = filter(lambda id: not read_message(id), ids)
            for id in unread_ids:
                mark_message_as_read(id)
        return perform_function

default focused_message = None

screen messages():
    python:
        keys = get_ui_key_actions()
        actions = {}
        for key, action in keys:
            if not isinstance(action, list):
                actions[key] = action # for NullAction()
            elif key != "2":
                actions[key] = [Function(ui_return_action("messages")), *action]
            else:
                actions[key] = Function(ui_return_action("messages"))

    for key, action in keys:
        key [key] action actions[key]
    default message_type = "all"
    default clicked_message_ids = set()
    zorder 200
    modal True
    tag gameui
    use gameui(
        "Messages",
        [
            Function(mark_items_as_read(clicked_message_ids)),
            Function(ui_return_action("messages")), 
        ],
        background=Image(get_filename("menubg")),
        subs=[
            ("All (" + str(len(all_messages_of_type("all"))) + ")", SetScreenVariable("message_type", "all"), message_type == "all"), 
            ("Unread (" + str(len(all_messages_of_type("unread"))) + ")", SetScreenVariable("message_type", "unread"), message_type == "unread"),
            ("Read (" + str(len(all_messages_of_type("read"))) + ")", SetScreenVariable("message_type", "read"), message_type == "read"),
        ],
    ):
        vbox:
            xpos 180
            frame:
                ypos 24
                ysize 474
                xsize 720
                background None
                use message_details(get_focused_message(message_type))
            if len(all_messages_of_type(message_type)) > 1:
                side "c r":
                    area (0, 24, 720, 210)
                    viewport id "message_list":
                        draggable True 
                        mousewheel True
                        frame:
                            xsize 720 - gui.bar_size
                            background None
                            vbox:
                                for message in all_messages_of_type(message_type):
                                    use message_select(message, message_type, clicked_message_ids)
                    if len(all_messages_of_type(message_type)) > 6:
                        vbar value YScrollValue("message_list")
                    else:
                        null width gui.bar_size

screen message_select(message, message_type, clicked_message_ids):
    python:
        col = "#FFFFFF" if message["id"] != get_focused_message(message_type)["id"] else gui.hover_color
    hbox:
        textbutton get_sender(message) + ": " + get_topic(message):
            action [
                Function(set_focused_message, message["id"]), 
                SetScreenVariable("clicked_message_ids", clicked_message_ids | {message["id"]}),
            ]
            text_size 24
            text_color col
            text_hover_color gui.hover_color

screen message_details(message):
    vbox:
        if message is not None:
            hbox:
                text "From: " size 32
                text get_sender(message) color gui.hover_color size 32
            hbox:
                text "Subject: " size 32
                text get_topic(message) color gui.hover_color size 32
            null height 32
            text message["message"] size 32