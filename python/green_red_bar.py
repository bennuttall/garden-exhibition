from dotstar import Adafruit_DotStar
from time import sleep
from random import randint

def green_red_bar_graph(num_green):
    for led in range(num_green):
        r, g, b = GREEN
        strip.setPixelColor(led, r, g, b)

    for led in range(num_green, NUM_LEDS):
        r, g, b = RED
        strip.setPixelColor(led, r, g, b)

    brightness = 255
    strip.setBrightness(brightness)
    strip.show()

NUM_LEDS = 10

DATAPIN = 15
CLOCKPIN = 14
strip = Adafruit_DotStar(NUM_LEDS, DATAPIN, CLOCKPIN)

strip.begin()

# colours
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def main():
    num_green = randint(0, NUM_LEDS)
    print(num_green)
    green_red_bar_graph(num_green)

if __name__ == '__main__':
    main()
