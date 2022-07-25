import datetime
from django.db import models


# Create your models here.


class Events(models.Model):
    class Meta:
        ordering = ('event_date',)

    event_name = models.CharField(max_length=255)
    event_description = models.TextField()
    event_date = models.DateField(("Date"), default=datetime.date.today)
    event_start_time = models.TimeField()
    event_end_time = models.TimeField()
    event_location = models.CharField(max_length=255)
    event_ticket_link = models.URLField(max_length=200)
    event_ticket_host = models.CharField(max_length=255)
