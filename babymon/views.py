from django.shortcuts import render
from django.http import HttpResponse
from babymon.models import LED
from django.shortcuts import get_object_or_404

# led = gpiozero.PWMLED(14)

# Create your views here.

# def index(request):
#    led.value=0.5
#
#    return HttpResponse("LEDS TOGGLED!")

from django.views.generic import TemplateView


class MonitorView(TemplateView):
    template_name = "babymon/monitor.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offtime'] = 1581812941559
        return context
