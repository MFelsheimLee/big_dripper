from PIL import Image
import math

image = Image.open('formlabs_logo_with_words.png')
print(f"Original size : {image.size}") # 5464x3640
ratio = image.size[0] / image.size[1]

width = 50
height = math.floor(ratio * width)

resized_image = image.resize((width, height))
resized_image.save('formlabs_image_50px.png')