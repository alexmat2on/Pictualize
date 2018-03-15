from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from math import ceil
import os
import random

# Read all possible top and bottom texts ---------------------------------------
with open('top.txt') as t:
    top_options = t.readlines()
top_options = [x.strip() for x in top_options]

with open('bot.txt') as b:
    bot_options = b.readlines()
bot_options = [x.strip() for x in bot_options]

# Function to superimpose text on an image -------------------------------------
def drawText(img, textstr, position):
    # Make font size 7% of the image width
    font = ImageFont.truetype("impact.ttf", ceil(img.size[0] * 0.07))

    text_x = font.getsize(textstr)[0]
    text_y = font.getsize(textstr)[1]
    x = (img.size[0] - text_x) / 2

    if position == "TOP":
        y = 5
    elif position == "BOT":
        y = img.size[1] - text_y - 10

    if text_x >= img.size[0]:
        sp = textstr.split()
        words = len(sp)
        topline = ""
        nextline = ""
        for i in range(0, words // 2):
            topline += sp[i] + " "

        for i in range(words // 2, words):
            nextline += sp[i] + " "

        nextx = (img.size[0] - font.getsize(nextline)[0]) / 2
        draw.text((nextx + 2, y + text_y + 8), nextline, (0, 0, 0), font=font)
        draw.text((nextx, y + text_y + 5), nextline, (255, 255, 255), font=font)

        textstr = topline
        x = (img.size[0] - font.getsize(textstr)[0]) / 2

    draw.text((x + 2, y + 2), textstr, (0, 0, 0), font=font)
    draw.text((x, y), textstr, (255, 255, 255), font=font)

# Create the memes! ---------------------------------------------------------------
# make sure output directory exists: 
if not os.path.exists('random_memes'):
    os.makedirs('random_memes')

# loop through templates & randomly assign text
count = 0
for filename in os.listdir("base_imgs"):
    img = Image.open("base_imgs/" + filename)
    draw = ImageDraw.Draw(img)

    text_top = random.choice(top_options)
    text_bot = random.choice(bot_options)

    drawText(img, text_top, "TOP")
    drawText(img, text_bot, "BOT")

    img.save('random_memes/wow' + str(count) + '.jpg')
    count += 1
