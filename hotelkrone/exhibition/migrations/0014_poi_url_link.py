# Generated by Django 3.0.5 on 2020-06-11 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0013_trackedfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='poi',
            name='url_link',
            field=models.CharField(default='', max_length=100),
        ),
    ]
