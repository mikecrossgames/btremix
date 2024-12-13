init python:
    def is_choice_disabled(choice_text):
        return "(disabled)" in choice_text.lower()
        
    def set_gallery_locked():
        persistent.gallery_unlocked = False

    def set_gallery_unlocked():
        persistent.gallery_unlocked = True

    def use_square_hotspots(event):
        return get_person_image(event["event"], event["title"]) is not None

    def get_redux_config():
        return {
            "show_black_below_videos": True,
            "play_faded_out_videos": True,
            "scene_animation_speed": 1.0,
            "remove_faded_out_pictures": False,
            "resolve_after_fade_out": True,
            "move_player_to_edge_of_location": False,
            "always_show_video_obscured_pictures": False,
            "map_backgrounds_have_priority": True,
            "sfw": persistent.sfw_mode,
        }

    config.default_transform = topleft
    renpy.music.register_channel("bgs", mixer="sfx")
    config.return_not_found_label = 'return_not_found'
    config.gestures = { "n" : "game_menu", "s" : "hide_windows", "w" : "rollback" }
    config.keymap['dismiss'].append('mousedown_5')
    config.keymap['rollforward'].remove('mousedown_5')
    config.menu_include_disabled = True

define config.mouse = { }
define config.mouse['action'] = [ ( "gui/action.png", 0, 0) ]    
default persistent.gallery_unlocked = False
default persistent.gallery_been_unlocked = False
default persistent.hints_onscreen = False
default persistent.tooltip1 = False
default persistent.tooltip2 = False
# define gui.text_font = "regular.ttf"
# define gui.interface_text_font = "regular.ttf"

define location_text_size = 36
define location_small_size = 21

define help_text_outline_color = "#FFFFFF20" # "#000"
define help_button_text_color = '#FFF' # '#888888'

define default_min_square_size = 48
define default_max_square_size = 48
define default_max_face_size = 48

define default_screen_padh = 45
define default_screen_padtop = 165
define default_screen_padbottom = 30
define event_hotspot_padding = 0
define hover_title_unknown = "(unknown location)"
define hover_title_ypos = 15

define BLEND_MODE_NAMES = {
    1: "add",
    2: "multiply",
    3: "max",
    4: "sub",
    # 1: "normal",
    # 2: "normal",
    # 3: "normal",
}

define image_choice_screen_font = "light.ttf"
define image_choice_font_size = location_text_size

define hover_text_ypos = 12
define hover_text_font = "light.ttf"
define hover_text_size = 22
define hover_text_outlines = [ (absolute(1), help_text_outline_color, absolute(0), absolute(0)) ]
define hover_text_line_spacing = -6

define inventory_cols = 4
define inventory_rows = 3
define inventory_width = 144
define inventory_height = 144
define inventory_xspacing = 3
define inventory_yspacing = 3
define inventory_text_size_large = 28
define inventory_text_size = 20
define inventory_font = "light.ttf"
define inventory_xpos = 60
define inventory_hover_yalign = 0.02777777778

label return_not_found:
    "{font=monospace.ttf}{size=16}updating save game from previous version - apologies for any errors or inconsistencies"
    call GameLoop from _call_ReturnNotFound_GameLoop
    return