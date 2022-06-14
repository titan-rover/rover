import RPi.GPIO as GPIO
import sys
from modules import config
from modules.relay import Relay


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    for pin in config.mode_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)
    GPIO.setup(config.aux_pin, GPIO.IN)

    relay = Relay()

    GPIO.output(config.mode_pins[0], 0)
    GPIO.output(config.mode_pins[1], 0)

    while True:
        buf = relay.GetSock()
        if buf:
            relay.PutRF(0b00, buf)