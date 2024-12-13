screen follower_list(followers_to_show):
    python:
        follower_list_ypos = 10
        follower_list_xpos = 10
        follower_text_size = 24
        follower_text_color = gui.selected_color
        follower_text_font =  "regular.ttf"
        hint_text = hint
    vbox:
        xpos follower_list_xpos
        ypos follower_list_ypos

        hbox:
            spacing 20
            for shown_follower in followers_to_show:
                use follower_image(shown_follower)
            text hint_text:
                yalign 0.5
                font follower_text_font
                size follower_text_size
                color follower_text_color

screen follower_list(followers_to_show):
    python:
        follower_list_ypos = 10
        follower_list_xpos = 10
        follower_text_size = 21
        follower_text_color = gui.selected_color
        follower_text_font =  "regular.ttf"
        hint_text = hint
    variant "small"
    vbox:
        xpos follower_list_xpos
        ypos follower_list_ypos

        hbox:
            spacing 20
            for shown_follower in followers_to_show:
                use follower_image(shown_follower)
        null height 8
        text hint_text:
            xsize 236
            yalign 0.5
            font follower_text_font
            size follower_text_size
            color follower_text_color

screen follower_image(image_name):
    python:
        displayed_image = im.FactorScale(get_filename(image_name), 108 / 144)
    image displayed_image

