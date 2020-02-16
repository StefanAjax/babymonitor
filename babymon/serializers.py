from rest_framework import serializers
from .models import LED


class LEDSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LED
        fields = ('url', 'id', 'on_until', 'duty_cycle_percent')
