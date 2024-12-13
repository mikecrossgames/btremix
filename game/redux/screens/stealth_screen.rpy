init python:
    import math

    def get_rotation(time, duration, middle_pause, end_pause, easing):
        halfway = duration / 2
        if time < halfway:
            amount = time / halfway
        elif time < halfway + middle_pause:
            amount = 1
        elif time < duration + middle_pause:
            amount = 1 - ((time - halfway - middle_pause) / halfway)
        else:
            amount = 0
        if easing == "easein":
            return math.sin(amount * math.pi / 2)
        elif easing == "easeout":
            return 1 - math.sin((1 - amount) * math.pi / 2)
        elif easing == "easeinout" or easing == "ease":
            return (math.sin((amount - 0.5) * math.pi) + 1) / 2
        else:
            return amount

    def calculate_isosceles_triangle_vertices(vertex, rotation, length, vertex_angle):
        rotation_rad = math.radians(rotation - 90) # sub 90 to assume 0 degrees is -ve y axis
        vertex_angle_rad = math.radians(vertex_angle)
        base_midpoint_distance = length * math.cos(vertex_angle_rad / 2)
        base_midpoint = (
            vertex[0] + base_midpoint_distance * math.cos(rotation_rad),
            vertex[1] + base_midpoint_distance * math.sin(rotation_rad),
        )
        half_base_length = length * math.sin(vertex_angle_rad / 2)
        vertex2 = (
            base_midpoint[0] + half_base_length * math.cos(rotation_rad + math.pi/2),
            base_midpoint[1] + half_base_length * math.sin(rotation_rad + math.pi/2),
        )
        vertex3 = (
            base_midpoint[0] + half_base_length * math.cos(rotation_rad - math.pi/2),
            base_midpoint[1] + half_base_length * math.sin(rotation_rad - math.pi/2),
        )
        return [vertex, vertex2, vertex3]

    def calculate_new_coordinates(original_x, original_y, image_width, image_height, rotate_degrees, anchor_x, anchor_y):
        angle_rad = math.radians(rotate_degrees)
        anchor_absolute_x = original_x + anchor_x * image_width
        anchor_absolute_y = original_y + anchor_y * image_height

        new_coords = []
        for corner_x, corner_y in [(0, 0), (image_width, 0), (0, image_height), (image_width, image_height)]:
            relative_x = corner_x - anchor_x * image_width
            relative_y = corner_y - anchor_y * image_height

            rotated_x = math.cos(angle_rad) * relative_x - math.sin(angle_rad) * relative_y
            rotated_y = math.sin(angle_rad) * relative_x + math.cos(angle_rad) * relative_y

            new_x = rotated_x + anchor_absolute_x
            new_y = rotated_y + anchor_absolute_y
            new_coords.append((new_x, new_y))

        blit_x = min(x for x, y in new_coords)
        blit_y = min(y for x, y in new_coords)

        return blit_x, blit_y

    class StealthDisplayable(renpy.Displayable):
        def __init__(self, spotlights, options1, options2):
            renpy.Displayable.__init__(self)
            self.oldst = None
            self.dot = Image("images/bg/dot.webp")
            self.text_bg = Transform(Image("gui/button/choice_idle_background.png"), ysize=STEALTH_TEXT_HEIGHT)
            self.text_bg_red = Transform(Image("gui/button/choice_idle_background_red.png"), ysize=STEALTH_TEXT_HEIGHT)
            self.text_bg_hover = Transform(Image("gui/button/choice_hover_background.png"), ysize=STEALTH_TEXT_HEIGHT)
            self.spotlights = spotlights
            self.spotlight_images = list(map(lambda x: Image(get_filename(x["image"])), spotlights))
            self.spotlight_times = list(map(lambda x: x["offset"], spotlights))
            self.options1 = options1
            self.options2 = options2
            self.mouse_pos = get_mouse_position()
            self.hovered_event = None
            self.focused_event = None

        def visit(self):
            return [self.text_bg, self.text_bg_red, self.text_bg_hover, *self.spotlight_images]

        def plot(self, render, dot_render, x, y):
            if developer_mode():
                render.blit(dot_render, (x - 12, y - 12))

        def render(self, width, height, st, at):
            if self.oldst is None:
                self.oldst = st
            dtime = st - self.oldst
            self.oldst = st

            render = renpy.Render(width, height)
            height = len(self.options1) * (STEALTH_TEXT_HEIGHT) + (len(self.options1) -1) * STEALTH_PADDING
            xpos = 480 - round(STEALTH_WIDTH / 2)
            ypos = 360 - round(height / 2)
            rectangle = ((xpos, ypos), (xpos + STEALTH_WIDTH, ypos + height))

            dot_render = renpy.render(self.dot, width, height, st, at)
            self.plot(render, dot_render, xpos, ypos)
            self.plot(render, dot_render, xpos + STEALTH_WIDTH, ypos)
            self.plot(render, dot_render, xpos, ypos + height)
            self.plot(render, dot_render, xpos + STEALTH_WIDTH, ypos + height)
            self.plot(render, dot_render, self.mouse_pos[0], self.mouse_pos[1])

            intersected = False
            for i in range(len(self.spotlights)):
                self.spotlight_times[i] += dtime
                while self.spotlight_times[i] > self.spotlights[i]["duration"] + self.spotlights[i]["middle_pause"] + self.spotlights[i]["end_pause"]:
                    self.spotlight_times[i] -= self.spotlights[i]["duration"] + self.spotlights[i]["middle_pause"] + self.spotlights[i]["end_pause"]

                spotlight = self.spotlights[i]
                rotation_position = get_rotation(self.spotlight_times[i], spotlight["duration"], self.spotlights[i]["middle_pause"], self.spotlights[i]["end_pause"], spotlight["easing"])
                rotation = spotlight["anglefromto"][0] + rotation_position * (spotlight["anglefromto"][1] - spotlight["anglefromto"][0])
                spot_displayable = Transform(self.spotlight_images[i], rotate_pad=False, rotate=rotation)
                spot_render = renpy.render(spot_displayable, width, height, st, at)
                xy = calculate_new_coordinates(
                    spotlight["pos"][0] - (spotlight["size"] * spotlight["anchor"][0]),
                    spotlight["pos"][1] - (spotlight["size"] * spotlight["anchor"][1]),
                    spotlight["size"], 
                    spotlight["size"], 
                    rotation, 
                    spotlight["anchor"][0], 
                    spotlight["anchor"][1]
                )
                render.blit(spot_render, xy)

                triangle = calculate_isosceles_triangle_vertices(spotlight["pos"], rotation, spotlight["size"], spotlight["spread"])

                intersected = intersected or triangle_intersects_rectangle(triangle, rectangle)

                if developer_mode():
                    triangle2 = calculate_isosceles_triangle_vertices(spotlight["pos"], rotation, 400, spotlight["spread"])
                    self.plot(render, dot_render, triangle2[0][0], triangle2[0][1])
                    self.plot(render, dot_render, triangle2[1][0], triangle2[1][1])
                    self.plot(render, dot_render, triangle2[2][0], triangle2[2][1])

            choices = self.options2 if intersected else self.options1

            text_bg_render = renpy.render(self.text_bg, width, height, st, at)
            text_bg_red_render = renpy.render(self.text_bg_red, width, height, st, at)
            text_bg_hover_render = renpy.render(self.text_bg_hover, width, height, st, at)

            self.hovered_event = None
            for i, choice in enumerate(choices):
                y = ypos + (i * (STEALTH_TEXT_HEIGHT + STEALTH_PADDING))
                is_hovered = self.mouse_pos[0] >= xpos and self.mouse_pos[0] <= xpos + STEALTH_WIDTH and self.mouse_pos[1] >= y + STEALTH_PADDING and self.mouse_pos[1] <= y + STEALTH_PADDING + STEALTH_TEXT_HEIGHT
                if is_hovered:
                    self.hovered_event = choice
                if intersected and self.options1[i][0] != self.options2[i][0]:
                    render.blit(text_bg_red_render, (xpos, y))
                elif is_hovered:
                    render.blit(text_bg_hover_render, (xpos, y))
                else:
                    render.blit(text_bg_render, (xpos, y))

            for i, choice in enumerate(choices):
                color = gui.selected_color if intersected and self.options1[i][0] != self.options2[i][0] else gui.selected_color if self.hovered_event == choice else gui.idle_color
                text_displayable = Text(choice[1], size=STEALTH_TEXT_SIZE, min_width=STEALTH_WIDTH, textalign=0.5, yalign=0.5, outlines=[], color=color)
                text_render = renpy.render(text_displayable, width, height, st, at)
                render.blit(text_render, (xpos, ypos - 2 + ((STEALTH_TEXT_HEIGHT - STEALTH_TEXT_SIZE) / 2) + (i * (STEALTH_TEXT_HEIGHT + STEALTH_PADDING))))

            renpy.redraw(self, 0)

            return render

        # Handles events.
        def event(self, ev, x, y, st):
            self.mouse_pos = get_mouse_position()
            if ev.type == pygame.MOUSEBUTTONDOWN and self.hovered_event is not None:
                renpy.restart_interaction()
                return self.hovered_event[0]
            elif ev.type == pygame.KEYDOWN:
                pressed = pygame.key.get_pressed()
                if self.focused_event is not None:
                    if pressed[pygame.K_SPACE] or pressed[pygame.K_RETURN]:
                        renpy.restart_interaction()
                        return self.focused_event[0]
                if pressed[pygame.K_ESCAPE]:
                    return None
            raise renpy.IgnoreEvent()

screen stealth_screen(spotlights, options1, options2):
    default stealth = StealthDisplayable(spotlights, options1, options2)
    add stealth