# Generated by Django 3.0.7 on 2021-03-17 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0007_auto_20210316_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_user_log',
            name='timedetails',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 17, 7, 52, 19, 681807)),
        ),
    ]
