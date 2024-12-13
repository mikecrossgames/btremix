default party = {"Johan", "Leyna2", "Johan2"}

label ChangePartyMember(actor_name, present):
    if present:
        $ party.add(actor_name)
    else:
        if actor_name in party:
            $ party.remove(actor_name)
    return

screen party_followers:
    if "Johan" in party or "Johan2" in party:
        if "Leyna" in party or "Leyna2" in party:
            add "images/party/johan_and_leyna.webp" xpos 10 ypos 10 xsize 96 ysize 48
        else:
            add "images/party/johan.webp" xpos 10 ypos 10 xsize 48 ysize 48
    else:
        add "images/party/leyna.webp" xpos 10 ypos 10 xsize 48 ysize 48
