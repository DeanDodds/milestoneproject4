# Generated by Django 3.2.13 on 2022-07-24 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_alter_brewerytourbooking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewerytourbooking',
            name='time',
            field=models.CharField(choices=[('14:00', '14:00'), ('15:30', '15:30')], max_length=15),
        ),
        migrations.AlterField(
            model_name='taproombooking',
            name='time',
            field=models.CharField(choices=[('12:00', '12:00'), ('12:30', '12,30'), ('13:00', '13:00'), ('13:30', '13,30'), ('14:00', '14:00'), ('14:30', '14:30'), ('15:00', '15:00'), ('15:30', '15,30'), ('16:00', '16:00'), ('16:30', '16,30'), ('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18,30'), ('19:00', '19:00'), ('19:30', '19:30'), ('20:00', '20:00'), ('20:30', '20:30'), ('21:00', '21:00'), ('21:30', '21:30'), ('22:00', '22:00')], max_length=15),
        ),
    ]
