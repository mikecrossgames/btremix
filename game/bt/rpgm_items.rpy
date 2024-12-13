init python:
    def has_item(id, qty = 1):
        if id not in item_qtys:
            return False
        return item_qtys[id] >= qty

    def item_qty(id):
        if id not in item_qtys:
            return 0
        return item_qtys[id]

    has_new_items = False

    def get_rpgm_item(id):
        return list(filter(lambda x: x["key"] == id, get_rpgm_items()))[0]

    def set_item(id, obtained):
        global has_new_items, no_advancement_events
        if obtained and id not in item_qtys:
            has_new_items = get_rpgm_item(id)["itype_id"]
        if obtained:
            if id not in item_qtys:
                item_qtys[id] = 1
            else:
                item_qtys[id] += 1
        else:
            if id in item_qtys:
                item_qtys[id] -= 1
                if item_qtys[id] <= 0:
                    del item_qtys[id]
        no_advancement_events = 0