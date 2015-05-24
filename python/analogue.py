from __future__ import division
from MCP3008 import MCP3008
from dotstar import Adafruit_DotStar
from time import sleep

def get_analogue_value(device, channel):
    with MCP3008(device=device, channel=channel) as ch:
        return ch.read()

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
    while True:
        channels = [0]
        devices = [0, 1]
        values = [get_analogue_value(device=d, channel=c) for c in channels for d in devices]
        max_value = 1023
        average = sum(values) / (max_value * len(values))
        num_green = int(average * NUM_LEDS)
        print(average, num_green)
        green_red_bar_graph(num_green)

if __name__ == '__main__':
    main()
