from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./imgs"
pathOut = "/editedImgs"

for filename in os.listdir(path):
    im = Image.open(f"{path}/{filename}")
    
    edit = im.filter(ImageFilter.SHARPEN).convert("L").rotate(-10)
    
    ImageEnhance.Contrast(edit).enhance(1.5)
    
    clean_name = os.path.splitext(filename)[0]
    ext = os.path.splitext(filename)[1]
    
    edit.save(f".{pathOut}/{clean_name}{ext}")
    
