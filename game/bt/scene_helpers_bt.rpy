init python:
    def day_to_night(image):
        return image

    def get_at_list(transforms):
        return transforms
        
    def get_video_background(bg):
        return bg

    def is_message_picture(picture):
        return False

    def is_message_background(picture):
        return False

    def should_flip():
        return False

    def get_image_list_size(len_events):
        return 160 if len_events < 5 else 128 if len_events < 11 else 108 if len_events < 20 else 80 if len_events < 25 else 64

    def allow_choice_cancel(called_from):
        return False