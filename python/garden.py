from __future__ import print_function, division
from RPi import GPIO
from dotstar import Adafruit_DotStar
from random import randint
from fractions import Fraction
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PULL = GPIO.PUD_UP
EDGE = GPIO.FALLING
BOUNCE = 3000

BUTTON_LED = 7
BUTTON = 24
SWITCH = 23

POINTS = 10

NUM_LEDS = 10
DATAPIN = 15
CLOCKPIN = 14

strip = Adafruit_DotStar(NUM_LEDS, DATAPIN, CLOCKPIN)

# colours
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def setup_button():
    GPIO.setup(BUTTON, GPIO.IN, PULL)
    GPIO.add_event_detect(BUTTON, EDGE, display_score_on_led_strip, BOUNCE)

def setup_led():
    GPIO.setup(BUTTON_LED, GPIO.OUT, False)

def setup_switch():
    GPIO.setup(SWITCH, GPIO.IN)

def control_led(on):
    GPIO.output(BUTTON_LED, on)

def calculate_score():
    random = randint(0, POINTS)
    print("random", random)
    switch = POINTS if GPIO.input(SWITCH) else POINTS / 2
    print("switch", switch)

    scores = [random, switch]

    total = sum(scores)
    print("total", total)
    potential = len(scores) * POINTS
    print("potential", potential)
    score = float(total / potential)
    print("score", score, int(score * NUM_LEDS))
    return int(score * NUM_LEDS)

def display_score_on_led_strip(pin):
    control_led(False)
    num_green = calculate_score()

    for led in range(num_green):
        r, g, b = GREEN
        strip.setPixelColor(led, r, g, b)

    for led in range(num_green, NUM_LEDS):
        r, g, b = RED
        strip.setPixelColor(led, r, g, b)

    brightness = 255
    strip.setBrightness(brightness)
    strip.show()
    control_led(True)

strip.begin()
setup_button()
setup_led()
setup_switch()

def main():
    while True:
        sleep(1000)

if __name__ == '__main__':
    main()
