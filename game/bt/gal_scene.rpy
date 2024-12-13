default persistent.unlocked_scenes = []

init python:
    class GalScene:
        
        inside_gallery = False

        def __init__(self, characters, name, label, image, can_be_done = None):
            self.characters = characters
            self.name = name
            self.label = label
            self.image = image
            self.can_be_done = can_be_done if can_be_done != None else lambda: True

        @staticmethod
        def unlock_scene(label):
            global scene_unlocked
            if not GalScene.inside_gallery and not label in persistent.unlocked_scenes:
                persistent.unlocked_scenes.append(label)
                scene_unlocked = True

        @staticmethod
        def lock_all_scenes():
            persistent.unlocked_scenes = []

        @staticmethod
        def set_inside_gallery(is_inside):
            GalScene.inside_gallery = is_inside

        @staticmethod
        def is_inside_gallery():
            return GalScene.inside_gallery

        @staticmethod
        def is_gallery_scene(scene_name):
            for scene in gallery_scenes:
                if scene.label == scene_name:
                    return True
            return False

        def is_unlocked(self):
            return self.label in persistent.unlocked_scenes

