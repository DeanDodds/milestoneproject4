# Generated by Django 3.2.13 on 2022-07-22 21:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
