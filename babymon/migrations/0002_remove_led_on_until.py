# Generated by Django 3.0.3 on 2020-02-15 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('babymon', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='led',
            name='on_until',
        ),
    ]
