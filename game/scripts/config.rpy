init python:
    config.default_transform = topleft
    renpy.music.register_channel("bgs", mixer="sfx")
    config.gestures = { "n" : "game_menu", "s" : "hide_windows", "w" : "rollback" }
    config.keymap['dismiss'].append('mousedown_5')
    config.keymap['rollforward'].remove('mousedown_5')
    config.menu_include_disabled = True

    from renpy.uguu import GL_FUNC_ADD, GL_ONE_MINUS_DST_COLOR, GL_ZERO, GL_ONE, GL_FUNC_REVERSE_SUBTRACT  # type: ignore
    config.gl_blend_func["screen"] = (GL_FUNC_ADD, GL_ONE_MINUS_DST_COLOR, GL_ONE, GL_FUNC_ADD, GL_ONE, GL_ONE)
    config.gl_blend_func["sub"] = (GL_FUNC_REVERSE_SUBTRACT, GL_ONE, GL_ONE, GL_FUNC_REVERSE_SUBTRACT, GL_ZERO, GL_ONE)

define BLEND_MODE_NAMES = {
    1: "add",
    2: "multiply",
    3: "screen",
    4: "sub",
}
