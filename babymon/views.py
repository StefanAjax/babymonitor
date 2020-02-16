from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import LED
from .serializers import LEDSerializer
from django.views.generic import TemplateView


class MonitorView(TemplateView):
    template_name = "babymon/monitor.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offtime'] = get_object_or_404(LED, pk=1).on_until
        return context


class LEDView(viewsets.ModelViewSet):
    queryset = LED.objects.all()
    serializer_class = LEDSerializer
