# Generated by Django 3.0.5 on 2020-06-16 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0017_orte_zoom_width_height_startpoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='orte',
            name='hide_on_entrance',
            field=models.BooleanField(default=False),
        ),
    ]
