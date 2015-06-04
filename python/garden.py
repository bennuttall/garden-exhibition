from __future__ import print_function, division
from RPi import GPIO
from dotstar import Adafruit_DotStar
from time import sleep
from random import randint

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PULL = GPIO.PUD_UP
EDGE = GPIO.FALLING
BOUNCE = 1000

BUTTON = 18

NUM_LEDS = 100
DATAPIN = 15
CLOCKPIN = 14

# colours
GREEN = (0, 255, 0)
RED = (255, 0, 0)

strip = Adafruit_DotStar(NUM_LEDS, DATAPIN, CLOCKPIN)

def setup_button():
    """
    Setup main GPIO button with callback
    """

    GPIO.setup(BUTTON, GPIO.IN, PULL)

def set_pixel(led, colour):
    """
    Set a given pixel on the LED matrix
    """

    r, g, b = colour
    strip.setPixelColor(led, r, g, b)
    strip.show()

def clear_strip(colour):
    """
    Clear LED matrix by setting all pixels to a single colour
    """

    for led in range(NUM_LEDS):
        set_pixel(led, colour)

def calculate_score():
    """
    Calculate score based on scoring algorithm
    """

    return randint(1, NUM_LEDS)

def show_score(score):
    """
    Display score on LED matrix
    """

    pause = 0.1

    for led in range(score):
        set_pixel(led, GREEN)
        sleep(pause)

    for led in range(score + 1, NUM_LEDS + 1):
        set_pixel(led, RED)
        sleep(pause)

def callback(pin):
    print("Run", pin)
    """
    Button press callback - calculate score and show on LED matrix
    """


def main():
    setup_button()
    strip.begin()

    strip.setBrightness(255)
    strip.clear()
    sleep(2)

    print("Ready...")

    while True:
        #GPIO.wait_for_edge(BUTTON, EDGE)
        strip.clear()
        score = calculate_score()
        print("Score is %s" % score)
        show_score(score)
        sleep(60)

if __name__ == '__main__':
    main()
