label CommonEventsBG:
    $ set_transparency_backgrounds(None)
    $ set_map_backgrounds(None)
    return

label CommonEventsStart:
    call CommonEventsBG from _call_CommonEventsBG
    stop music
    stop bgs
    return

label CommonEventsEnd:
    return

