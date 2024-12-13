init python:
    def replay_scene(galscene):
        GalScene.set_inside_gallery(True)
        reset_gallery_viewed_scenes()
        show_dialog_background()
        renpy.call_in_new_context("PlayGallery", galscene.label)
        GalScene.set_inside_gallery(False)

    def gallery_ysize():
        return 418 if persistent.gallery_unlocked and main_menu else 450

    def get_default_character():
        return characters[0][0]

default selected_character = get_default_character()
default show_all = False
default view_all = False

screen character_list():
    python:
        available_scenes = gallery_scenes if show_all and main_menu else list(filter(lambda galscene: ((main_menu and galscene.is_unlocked()) or (not main_menu and galscene.label in scenes_seen)), gallery_scenes))
        characters_with_scenes = list(filter(lambda character, available_scenes=available_scenes: any((character[0] in s.characters) for s in available_scenes), characters))
        nav_items = list(map(lambda character: {"id": character[0], "label": character[1], "action": SetVariable("selected_character", character[0])}, characters_with_scenes))
        if len(nav_items) == 0:
            nav_items.append({"id": characters[0][0], "label": characters[0][1], "action": SetVariable("selected_character", characters[0][0])})
        if persistent.gallery_unlocked and main_menu:
            if not show_all and len(characters_with_scenes) < len(characters):
                nav_items.append({"id": "show_all", "label": _("(show all)"), "action": SetVariable("show_all", True)})
            elif len(characters_with_scenes) < len(characters):
                nav_items.append({"id": "hide_all", "label": _("(hide unseen)"), "action": [SetVariable("show_all", False), SetVariable("selected_character", get_default_character())]})

        items_in_rows = [[]]
        row_length = 0
        for nav_item in nav_items:
            row_length += len(nav_item["label"]) + 1.5
            if row_length >= 58:
                # items_in_rows[-1].append({"id": "len", "label": str(row_length), "action": None})
                items_in_rows.append([])
                row_length = 0
            items_in_rows[-1].append(nav_item)            

    vbox:
        ysize 32
        for row in items_in_rows:            
            hbox:
                spacing 10
                for item in row:
                    textbutton item["label"] action item["action"]:
                        ysize 20
                        text_size 16
                        background None                        
                        if selected_character == item["id"]:
                            text_color "#FFF"
                        else:
                            text_color gui.idle_color
                            text_hover_color gui.accent_color

screen gallery_screen():
    tag menu
    use game_menu(_("Replay scenes") if main_menu else _("Scenes"), show_scene_text="gallery" if not main_menu else "galleryalt"):

        style_prefix "gallery"

        vbox:
            use character_list
            # Scene grid
            null height 18
            vbox:
                ysize gallery_ysize()
                vpgrid:
                    python:
                        filtered_scenes = list(filter(lambda x: selected_character in x.characters, gallery_scenes))

                    cols 3
                    xspacing 30

                    draggable True
                    mousewheel True

                    for galscene in filtered_scenes:
                        vbox:
                            python:
                                view_this = (galscene.is_unlocked() or view_all if main_menu else galscene.label in scenes_seen)
                                text_color = gui.insensitive_color if not view_this else gui.idle_small_color
                                gal_name = "?" if not view_this else galscene.name
                                im_tint = 0.25 if main_menu and not view_this else 0.25 if not view_this else 1.0
                                im_blur = 1.5 if not view_this else 1.0
                                unblurred_image = im.MatrixColor(im.Scale(Image(get_filename(galscene.image)), 160, 122), im.matrix.tint(im_tint, im_tint, im_tint))
                                blurred_image = im.Blur(unblurred_image, 0.05)
                                click_action = None if not view_this else Function(replay_scene, galscene)
                            xsize 160
                            ysize 160
                            if main_menu:
                                fixed:
                                    imagebutton:
                                        idle im.Alpha(blurred_image, 1.0)
                                        hover im.Alpha(unblurred_image, 1.0)
                                        action click_action
                                    text gal_name:
                                        xalign 0.5
                                        ypos 124
                                        size 14
                                        color text_color
                            else:
                                fixed:
                                    image unblurred_image
                                    text gal_name:
                                        xalign 0.5
                                        ypos 124
                                        size 14
                                        color text_color

                    if len(filtered_scenes) % 3 != 0:
                        for x in range(0, 3 - len(filtered_scenes) % 3):
                            null width 160 height 122

            if persistent.gallery_unlocked and main_menu:
                # Toggle to view unlocked scenes
                python:
                    textbutton_text = _("Play locked scenes: No") if not view_all else _("Play locked scenes: Yes")
                hbox:
                    xalign 1.0
                    textbutton textbutton_text action SetVariable("view_all", not view_all) text_color gui.idle_color text_size 14 background None text_hover_color gui.hover_color

style gallery_label is gui_label
style gallery_label_text is gui_label_text
style gallery_text is gui_text

style gallery_label_text:
    size gui.label_text_size

screen gallery_scene_textbox():
    frame:
        background None
        ysize 80
        ypos 16
        xpos 12
        vbox:
            yalign 0
            use gallery_scene_text(_("These are the scenes completed in the current playthrough."))
            use gallery_scene_text(_("To replay scenes, select {i}Main Menu{/i} - {i}Replay Scenes{/i}."))
            if not persistent.gallery_been_unlocked:
                use gallery_scene_text(_("Enable {i}Scene unlocker{/i} in {i}Preferences{/i} to play locked scenes."))

screen gallery_scene_textbox_alt():
    frame:
        background None
        ysize 80
        ypos 26
        vbox:
            yalign 0.5
            if not persistent.gallery_been_unlocked:
                use gallery_scene_text(_("Enable {i}Scene unlocker{/i} in {i}Preferences{/i} to play locked scenes."))

screen gallery_scene_text(text):
    vbox:
        text text color gui.idle_color size 16 xalign 1.0 textalign 1.0