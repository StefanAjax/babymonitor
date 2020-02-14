from gpiozero import PWMLED
import sys
from time import sleep

percent = int(sys.argv[1])
freq = int(sys.argv[2])
PWM_value = percent * 0.01

leds = [PWMLED(14), PWMLED(15)]

for led in leds:
    led.frequency = freq
    led.value = PWM_value

sleep(10)
