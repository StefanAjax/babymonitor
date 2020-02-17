from gpiozero import PWMLED
import time

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
    time_now = int(round(time.time() * 1000))
    time_left = on_until - time_now
    # print("On Until: {}\tTime Now: {}\tTime Left: {}".format(on_until, time_now, time_left))
    for led in leds:
        # led.frequency = freq
        if time_left > 1200 and abs(time_left) < 25000:
            led.value = duty_cycle_percent * 0.01
        else:
            led.value = 0.0
    time.sleep(0.2)
