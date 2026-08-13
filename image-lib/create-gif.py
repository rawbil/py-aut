from PIL import Image
import os

images = [Image.open(f"./imgs/{image}") for image in os.listdir("./imgs")]

images[0].save("./editedImgs/animated-gif1.gif", append_images=images[1:], loop=0, duration=500)