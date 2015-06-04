from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PULL = GPIO.PUD_UP
EDGE = GPIO.FALLING
BOUNCE = 1000

BUTTON = 18

def setup_button():
    GPIO.setup(BUTTON, GPIO.IN, PULL)
    GPIO.add_event_detect(BUTTON, EDGE, callback, BOUNCE)

def callback(pin):
    print("pressed")

setup_button()

def main():
    sleep(1000)

if __name__ == '__main__':
    main()
