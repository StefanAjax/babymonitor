# Generated by Django 3.0.3 on 2020-02-18 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('babymon', '0006_auto_20200218_1718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='led',
            old_name='noleds',
            new_name='all_leds',
        ),
    ]