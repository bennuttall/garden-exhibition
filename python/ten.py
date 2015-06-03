from dotstar import Adafruit_DotStar
from time import sleep

def go(colour):
    for led in range(NUM_LEDS):
        r, g, b = colour
        strip.setPixelColor(led, r, g, b)

    brightness = 255
    strip.setBrightness(brightness)
    strip.show()



NUM_LEDS = 10

DATAPIN = 15
CLOCKPIN = 14
strip = Adafruit_DotStar(NUM_LEDS, DATAPIN, CLOCKPIN)

strip.begin()

RED = (255, 0, 0)
GREEN = (0, 255, 0)

def main():
    while True:
        go(RED)
        print("red")
        sleep(2)

if __name__ == '__main__':
    main()
