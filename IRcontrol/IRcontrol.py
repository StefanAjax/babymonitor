import requests
import json
import time
from gpiozero import PWMLED

led1 = PWMLED(14, frequency=200)
led2 = PWMLED(15, frequency=500)

url = "http://192.168.0.18/babymon/apileds/1/"

payload = {}
headers = {
        'Content-Type': 'application/json'
}

while True:
    response = requests.request("GET", url, headers=headers, data= payload)
    data = json.loads(response.text.encode('utf8'))
    on_until = data['on_until']
    duty_cycle_percent = data['duty_cycle_percent']
    all_leds = data['all_leds']

    time_now = int(round(time.time() * 1000))
    time_left = on_until - time_now
    print("On Until: {}\tTime Now: {}\tTime Left: {}".format(on_until, time_now, time_left))
    if time_left > 0 and abs(time_left) < 25000:
        led1.value = duty_cycle_percent * 0.01
    else:
        led1.value = 0.0
    if time_left > 0 and abs(time_left) < 25000 and all_leds == 1:
        led2.value = duty_cycle_percent * 0.01
    else:
        led2.value = 0.0
    time.sleep(0.2)
