import os
from utils.config import UPLOAD_FOLDER

def save_image(image_file, filename):
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    image_file.save(os.path.join(UPLOAD_FOLDER, filename))
    return os.path.join(UPLOAD_FOLDER, filename)

def validate_input(text, image):
    if not text and not image:
        return False, 'Either text or image is required'
    return True, ''