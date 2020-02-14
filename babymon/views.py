from django.shortcuts import render
from django.http import HttpResponse
import gpiozero
from time import sleep

#led = gpiozero.PWMLED(14)

# Create your views here.

#def index(request):
#    led.value=0.5
#
#    return HttpResponse("LEDS TOGGLED!")

from django.views.generic import TemplateView

class MonitorView(TemplateView):
    template_name = "babymon/monitor.html"