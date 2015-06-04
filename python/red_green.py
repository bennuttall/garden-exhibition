from dotstar import Adafruit_DotStar
from time import sleep

def go(colour, pause=0):
    for led in range(NUM_LEDS):
        print(led)
        r, g, b = colour
        strip.setPixelColor(led, r, g, b)
        strip.show()
        sleep(pause)

NUM_LEDS = 100

DATAPIN = 15
CLOCKPIN = 14
strip = Adafruit_DotStar(NUM_LEDS, DATAPIN, CLOCKPIN)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
OFF = (0, 0, 0)

strip.begin()

brightness = 255
strip.setBrightness(brightness)
go(OFF)
print("done")


def main():
    while True:
        print("green")
        go(GREEN, 0.1)
        print("red")
        go(RED, 0.1)

if __name__ == '__main__':
    main()
