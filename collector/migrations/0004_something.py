# Generated by Django 3.0.7 on 2021-02-09 04:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0005_auto_20210129_1024'),
        ('collector', '0003_auto_20210207_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='something',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewDetails', models.IntegerField(default=0)),
                ('viewDate', models.IntegerField(default=0)),
                ('viewLocation', models.IntegerField(default=0)),
                ('viewRegistration', models.IntegerField(default=0)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Events_model')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
