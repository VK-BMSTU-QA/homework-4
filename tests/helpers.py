import os
import random
import string
import png

cyrillic = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def string_generator(size=6, chars=string.ascii_uppercase + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_pic(name='test.png', width=255, height=255):
    img = []
    for y in range(height):
        row = ()
        for x in range(width):
            row = row + (x%255, max(0, abs(255 + random.randint(0,255)
                                       - random.randint(0,x) - random.randint(0,y)) %255), 255)
        img.append(row)
    with open(name, 'wb') as f:
        w = png.Writer(width, height, greyscale=False)
        w.write(f, img)


def delete_pic(name='test.png'):
    os.remove(name)
