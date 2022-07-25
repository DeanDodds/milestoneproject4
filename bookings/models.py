from django.db import models
import datetime


# Create your models here.
class BreweryTourBooking(models.Model):
    class Meta:
        ordering = ('date',)

    NUMBER_OF_PEOPLE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
    )

    TOUR_TIMES = (
        ('13:00', '13:00'),
        ('14:30', '14:30'),
    )

    name = models.CharField(max_length=22)
    email = email = models.EmailField()
    phone = models.CharField(max_length=20, null=False, blank=False)
    number_of_people = models.IntegerField('Number of people',
                                           choices=NUMBER_OF_PEOPLE)
    date = models.DateField()
    time = models.CharField(max_length=15, choices=TOUR_TIMES)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date_booked = models.DateTimeField(auto_now_add=True)


class TaproomBooking(models.Model):
    class Meta:
        ordering = ('date',)
        
    NUMBER_OF_PEOPLE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
    )

    TAPRROOM_TIMES = (
        ('12:00', '12:00'),
        ('12:30', '12,30'),
        ('13:00', '13:00'),
        ('13:30', '13,30'),
        ('14:00', '14:00'),
        ('14:30', '14:30'),
        ('15:00', '15:00'),
        ('15:30', '15,30'),
        ('16:00', '16:00'),
        ('16:30', '16,30'),
        ('17:00', '17:00'),
        ('17:30', '17:30'),
        ('18:00', '18:00'),
        ('18:30', '18,30'),
        ('19:00', '19:00'),
        ('19:30', '19:30'),
        ('20:00', '20:00'),
        ('20:30', '20:30'),
        ('21:00', '21:00'),
        ('21:30', '21:30'),
        ('22:00', '22:00'),
    )

    name = models.CharField(max_length=22)
    email = email = models.EmailField()
    phone = models.CharField(max_length=20, null=False, blank=False)
    number_of_people = models.IntegerField('Number of people',
                                           choices=NUMBER_OF_PEOPLE)
    date = models.DateField()
    time = models.CharField(max_length=15, choices=TAPRROOM_TIMES)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date_booked = models.DateTimeField(auto_now_add=True)
