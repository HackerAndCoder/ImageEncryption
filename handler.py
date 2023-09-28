from PIL import Image
import string, math, random

sizes = {}

num = 16

while num < 100000:
    sizes[num*num] = (num, num)
    num *= 2

def find_optimal_image_size(length : int):
    img_size = 0
    index = 0
    while length > img_size and index < len(sizes):
        img_size = tuple(sizes.keys())[index]
        index += 1
    return sizes[img_size]

def to_2d(one_d, two_d_width, two_d_height):
    y = math.floor(one_d / two_d_height)
    x = one_d % two_d_width
    return (x, y)

def text_to_image(text):
    text_list = list(text)
    img_size = find_optimal_image_size(len(text))
    img = Image.new(mode = "RGB", size = img_size, color = (0, 0, 0))

    for i in range(len(text_list)):
        char = text_list[i]
        if not char in string.printable:
            print(f'Can\'t process char {char}')
            continue

        color = string.printable.find(char) + 1 * 2
        img.putpixel(to_2d(i, img_size[0], img_size[1]), (random.randint(0, 255), color, random.randint(0, 255)))
    
    return img

def image_to_text(img):
    text = ''
    data = list(img.getdata())
    for pixel in data:
        if pixel[0] == 0:
            continue # this must be the background, not data, so ignore it
        text += string.printable[pixel[0]-2]
    return text