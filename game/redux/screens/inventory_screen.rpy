init python:
    def get_item_image(item):
        if inventory_height > inventory_width:
            scale = inventory_height / 256
        else:
            scale = inventory_width / 256
        return im.FactorScale(Image(get_filename("item_" + item["key"])), scale)
    
    def get_item_description(item):
        return item["description"]

default inventory_item_hovered = None
default inventory_page = 0

screen inventory_screen(items, get_action, get_details=get_item_details):
    python:
        keys = get_ui_key_actions()
        actions = {}
        for key, action in keys:
            if not isinstance(action, list):
                actions[key] = action # for NullAction()
            elif key != "4":
                actions[key] = [Function(ui_return_action("inventory")), *action]
            else:
                actions[key] = Function(ui_return_action("inventory"))

        i = inventory_page * (inventory_cols * inventory_rows)
        displayed_items = []
        while i < len(items) and len(displayed_items) < (inventory_cols * inventory_rows):
            displayed_items.append(items[i])
            i = i + 1
        while len(displayed_items) < (inventory_cols * inventory_rows):
            displayed_items.append(None)
        prev_action = SetVariable("inventory_page", max(0, inventory_page - 1)) if inventory_page > 0 else NullAction()
        next_action = SetVariable("inventory_page", inventory_page + 1) if len(items) > ((inventory_page + 1) * (inventory_cols * inventory_rows)) else NullAction()
        prev_i = im.FactorScale(Image("arrowleft.webp"), 0.5)
        next_i = im.FactorScale(Image("arrowright.webp"), 0.5)
        prev_icon = prev_i if inventory_page > 0 else im.Alpha(prev_i, 0.25)
        next_icon = next_i if len(items) > ((inventory_page + 1) * (inventory_cols * inventory_rows)) else im.Alpha(next_i, 0.25)

    for key, action in keys:
        key [key] action actions[key]

    fixed:
        xpos inventory_xpos
        ypos 0
        vbox:
            yalign inventory_hover_yalign
            xsize config.screen_width - inventory_xpos
            if inventory_item_hovered is not None:
                text inventory_item_hovered["name"]:
                    xmaximum 440
                    xalign 0.5
                    size inventory_text_size_large
                    font hover_text_font
                    outlines hover_text_outlines
                text get_item_description(inventory_item_hovered):
                    xmaximum 440
                    xalign 0.5
                    size inventory_text_size
                    font hover_text_font
                    outlines hover_text_outlines
        vbox:
            yalign 0.5
            xalign 0.5
            null height 20
            grid inventory_cols inventory_rows:
                xspacing inventory_xspacing
                yspacing inventory_yspacing
                for item in displayed_items:
                    use inventory_screen_item(item, None if item is None else get_action(item), get_details)
            null height 24
        hbox:
            yalign 0.9166666667
            xalign 0.5
            imagebutton action prev_action: 
                xalign 0.0
                idle prev_icon
                hover prev_icon
                xsize 72
                ysize 48
            null width 256
            imagebutton action next_action: 
                xalign 1.0
                idle next_icon
                hover next_icon
                xsize 72
                ysize 48

screen wallet_amount(money, money_type):
    if money is not None:
        fixed:
            xpos 34
            ypos 128
            xmaximum 120
            vbox:
                text "You have":
                    size inventory_text_size_large
                    font inventory_font
                    outlines hover_text_outlines
                hbox:
                    text str(money) + " ":
                        size inventory_text_size_large
                        font inventory_font
                        outlines hover_text_outlines
                    text "🪙":
                        size inventory_text_size_large
                        font "emoji.ttf"
                        color "#FFD700"
                    text money_type:
                        size inventory_text_size_large
                        font inventory_font
                        outlines hover_text_outlines

screen inventory_screen_item(item, item_action, get_details):
    python:
        details = get_details(item)
        item_image = None if item is None else get_item_image(item)
        not_actionble = details is not None and details["price"] is None
        if not_actionble:
            item_image = im.Alpha(item_image, 0.5)
            action = NullAction()
        else:
            action = item_action
        item_background = "#5f5f5fA0" if item is None else "#1a1a1a80" if inventory_item_hovered is None or inventory_item_hovered != item else "#1a1a1aA0"
        qty = 0 if details is None else details["qty"]
        price = None if details is None else details["price"]
        bag_image = im.FactorScale(get_filename("inventory"), 0.25)
    frame:
        xsize inventory_width
        ysize inventory_height
        xalign 0.5
        yalign 0.5
        background Solid(item_background)
        if item is not None:
            imagebutton:
                xalign 0.5
                yalign 0.5
                idle item_image
                xsize inventory_width
                ysize inventory_height
                action action
                hovered SetVariable("inventory_item_hovered", item)
                unhovered SetVariable("inventory_item_hovered", None)
            if qty > 0 and not not_actionble:
                fixed:
                    xsize inventory_width
                    frame:
                        xalign 1.0
                        background Solid("#00000080")
                        hbox:
                            text str(qty):
                                size inventory_text_size
                            image bag_image
            if price is not None and price > 0 and not not_actionble:
                fixed:
                    xsize inventory_width - inventory_xspacing - 1
                    ysize inventory_height - inventory_yspacing - 1
                    frame:
                        xalign 1.0
                        yalign 1.0
                        background Solid("#00000080")
                        hbox:
                            text str(price):
                                size inventory_text_size
                            null width 2
                            text "🪙":
                                size inventory_text_size - 1
                                font "emoji.ttf"
                                color "#FFD700"
