from django.urls import path, include
from babymon.views import MonitorView
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('leds', views.LEDView)


urlpatterns = [
    path('', MonitorView.as_view()),
    path('api', include(router.urls))
]
