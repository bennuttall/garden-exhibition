from RPi import GPIO
from dotstar import Adafruit_DotStar
from random import randint
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PULL = GPIO.PUD_UP
EDGE = GPIO.FALLING
BOUNCE = 3000

LED = 7
BUTTON = 24

def setup_button():
    GPIO.setup(BUTTON, GPIO.IN, PULL)
    GPIO.add_event_detect(BUTTON, EDGE, button_callback, BOUNCE)

def setup_led():
    GPIO.setup(LED, GPIO.OUT, False)

def flash_led():
    GPIO.output(LED, True)
    sleep(2)
    GPIO.output(LED, False)

def button_callback(pin):
    num_green = randint(0, NUM_LEDS)
    print(num_green)
    green_red_bar_graph(num_green)
    flash_led()

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
setup_button()
setup_led()

# colours
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def main():
    sleep(1000)

if __name__ == '__main__':
    main()
