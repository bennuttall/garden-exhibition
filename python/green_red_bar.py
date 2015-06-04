from dotstar import Adafruit_DotStar
from time import sleep
from random import randint

def green_red_bar_graph(num_green):
    pause = 0.1
    for led in range(num_green):
        set_pixel(led, GREEN, pause)

def set_pixel(led, colour, pause=0):
    sleep(pause)
    r, g, b = colour
    strip.setPixelColor(led, r, g, b)
    strip.show()

def clear(colour):
    for led in range(NUM_LEDS):
        set_pixel(led, colour)


NUM_LEDS = 100

DATAPIN = 15
CLOCKPIN = 14
strip = Adafruit_DotStar(NUM_LEDS, DATAPIN, CLOCKPIN)

# colours
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def main():
    strip.begin()
    brightness = 255
    strip.setBrightness(brightness)
    clear(RED)

    num_green = randint(0, NUM_LEDS)
    print(num_green)
    green_red_bar_graph(num_green)

if __name__ == '__main__':
    main()
