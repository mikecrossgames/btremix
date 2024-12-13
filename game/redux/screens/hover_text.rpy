default hover_text = None

screen hover_text():
    if hover_text != "" and hover_text is not None:
        python:
            hover_text_to_display = hover_text[1:] if hover_text.startswith("!") else hover_text
            color = "#FFFFFF" if not hover_text.startswith("!") else "#FFFFFF20"
            outlines = hover_text_outlines if not hover_text.startswith("!") else  [ (absolute(1), "#FFFFFF10", absolute(0), absolute(0)) ]

        fixed:
            vbox:
                ypos hover_text_ypos
                xpos 0
                xsize config.screen_width
                text hover_text_to_display:
                    xmaximum config.screen_width / 2
                    xalign 0.5
                    font hover_text_font
                    size hover_text_size
                    outlines outlines
                    color color
                    line_spacing hover_text_line_spacing
