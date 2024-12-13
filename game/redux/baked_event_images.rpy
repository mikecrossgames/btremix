init python:
    use_baked_images = True

    def get_baked_event_images(map_name, pos=None):
        if not use_baked_images:
            return []
        try:
            map_name_to_use = get_baked_event_image_map(map_name)
        except NameError:
            map_name_to_use = map_name

        filtered_events = get_filtered_events_for_map(map_name_to_use, location=None if pos is None else get_xy_location(map_name, pos[0], pos[1]))
        filtered_events_with_zorder = list(map(lambda fe: { "event": fe[0][0], "zorder": get_event_zorder(fe[0][0]) }, filtered_events))
        sorted_filtered_events = sorted(filtered_events_with_zorder, key=lambda event_object: event_object["zorder"])
        baked_event_images = []
        for filtered_event in sorted_filtered_events:
            event = filtered_event["event"]
            has_fixed_pos = event in map_event_xy_fixed and event in face_images and (len(map_event_xy_fixed[event]) == 2 or not map_event_xy_fixed[event][2])
            if has_fixed_pos and event in map_event_xyposition and event in map_event_xyposition:
                pos = (map_event_xyposition[event][0] - adjust_x, map_event_xyposition[event][1] - adjust_y)
                if face_images[event] in large_face_images:
                    baked_event_images.append((pos, face_images[event], large_face_images[face_images[event]]))
                else:
                    baked_event_images.append((pos, face_images[event]))
            elif has_fixed_pos:
                pos = (map_event_xy_fixed[event][0] - adjust_x, map_event_xy_fixed[event][1] - adjust_y)
                if face_images[event] in large_face_images:
                    baked_event_images.append((pos, face_images[event], large_face_images[face_images[event]]))
                else:
                    baked_event_images.append((pos, face_images[event]))
        return baked_event_images
