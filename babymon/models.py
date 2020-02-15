from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class LED(models.Model):
    on_until = models.BigIntegerField()
    duty_cycle_percent = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
