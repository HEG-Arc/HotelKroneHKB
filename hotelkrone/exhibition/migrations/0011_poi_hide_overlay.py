# Generated by Django 3.0.5 on 2020-06-07 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0010_poi_this_is_a_sound'),
    ]

    operations = [
        migrations.AddField(
            model_name='poi',
            name='hide_overlay',
            field=models.BooleanField(default=False),
        ),
    ]
