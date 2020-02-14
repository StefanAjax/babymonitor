from django.urls import path
from babymon.views import MonitorView

urlpatterns = [
    path('', MonitorView.as_view()),
]