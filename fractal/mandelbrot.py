from PIL import Image
from numpy import complex, array
import colorsys
import keyboard

WIDTH = 256

def rgb_conv(i):
    color = 255 * array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
    return tuple(color.astype(int))

def mandelbrot(x, y):
    c0 = complex(x, y)
    c = 0
    for i in range(1, 1000):
        if abs(c) > 2:
            return rgb_conv(i)
        c = c * c + c0

    return (0, 0, 0)

img = Image.new('RGB', (WIDTH, WIDTH//2))
pixels = img.load()

image_width = WIDTH
image_height = image_width // 2

def map_mdt_coord(x, y):
    xf = x * 1.0 / image_width
    xf = xf * 4.0 - 3.0         # map to [-3, 1]

    yf = y * 1.0 / image_height
    yf = yf * 2.0 - 1.0         # map to [-1, 1]

    return (xf, yf)

def show_mandelbrot(xlhs, xrhs, ylhs, yrhs):
    for x in range(xlhs, xrhs):
        print("%.2f %%" % ((x - xlhs) / (xrhs - xlhs) * 100.0))
        for y in range(ylhs, yrhs):
            coord = map_mdt_coord(x, y)
            pixels[x-xlhs, y-ylhs] = mandelbrot(coord[0], coord[1])

    img.show()

# show_mandelbrot(0, image_width, 0, image_height)

zoom_scale = 1.0
def zoom_in():
    global image_width, image_height, zoom_scale

    zoom_scale = zoom_scale * 2.0

    image_width = int(WIDTH * zoom_scale)
    image_height = image_width // 2

    xlhs = (image_width - WIDTH) // 2
    xrhs = xlhs + WIDTH

    ylhs = xlhs // 2
    yrhs = xrhs // 2

    print("{} {} {} {}".format(xlhs, xrhs, ylhs, yrhs))
    show_mandelbrot(xlhs, xrhs, ylhs, yrhs)

def move_left():
    pass

keyboard.add_hotkey('s', zoom_in)
keyboard.wait()