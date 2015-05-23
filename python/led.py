from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PULL = GPIO.PUD_UP
EDGE = GPIO.FALLING
BOUNCE = 1000

LED = 7
BUTTON = 24

def setup_button():
    GPIO.setup(BUTTON, GPIO.IN, PULL)
    GPIO.add_event_detect(BUTTON, EDGE, flash_led, BOUNCE)

def setup_led():
    GPIO.setup(LED, GPIO.OUT, False)

def flash_led(pin):
    GPIO.output(LED, True)
    sleep(2)
    GPIO.output(LED, False)

setup_button()
setup_led()

def main():
    sleep(1000)

if __name__ == '__main__':
    main()
