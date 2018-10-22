import random
from PIL import Image, ImageFont, ImageDraw

# create one random number
nums = random.randint(1,100)

# Read image
im = Image.open('ascii_dora.png')


w,h = im.size
wDraw = 0.8 * w
hDraw = 0.08 * w

# Draw image
font = ImageFont.truetype("DroidSans.ttf", 30) # use absolute font path to fix 'IOError: cannot open resource'
draw = ImageDraw.Draw(im)
draw.text((wDraw,hDraw), str(nums), font=font, fill=(255,33,33))

# Save image
im.save('kxrr_msg.png', 'png')