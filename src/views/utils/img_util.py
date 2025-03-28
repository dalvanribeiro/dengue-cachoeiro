from PIL import Image
import os

def open_img(path_rel):
    path = os.path.abspath(path_rel)
    pil_img = Image.open(path)
    return pil_img