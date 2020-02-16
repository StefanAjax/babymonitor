from gpiozero import PWMLED
from time import sleep
#
#percent = int(sys.argv[1])
#freq = int(sys.argv[2])
#PWM_value = percent * 0.01
#
leds = [PWMLED(14), PWMLED(15)]
#
#for led in leds:
#    led.frequency = freq
#    led.value = PWM_value


import requests
import json

url = "http://192.168.1.188/babymon/apileds/1/"

payload = {}
headers = {
    'Content-Type': 'application/json'
}


while True:
    response = requests.request("GET", url, headers=headers, data = payload)
    data = json.loads(response.text.encode('utf8'))
    on_until = data['on_until']
    duty_cycle_percent = data['duty_cycle_percent']
    for led in leds:
        # led.frequency = freq
        led.value = duty_cycle_percent*0.01
    sleep(1)
