import requests
import json
import time
from gpiozero import PWMLED

leds = [PWMLED(14, frequency=400), PWMLED(15, frequency=713)]

url = "http://192.168.1.188/babymon/apileds/1/"

payload = {}
headers = {
    'Content-Type': 'application/json'
}

while True:
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text.encode('utf8'))
    on_until = data['on_until']
    duty_cycle_percent = data['duty_cycle_percent']
    time_now = int(round(time.time() * 1000))
    time_left = on_until - time_now
    print("On Until: {}\tTime Now: {}\tTime Left: {}".format(on_until, time_now, time_left))
    for led in leds:
        # led.frequency = freq
        if time_left > 0 and abs(time_left) < 25000:
            led.value = duty_cycle_percent * 0.01
        else:
            led.value = 0.0
    time.sleep(0.2)
