from django.db import models
import datetime

# Create your models here.
class Events(models.Model):
    event_name = models.CharField(max_length=255)
    event_description = models.TextField()
    event_date = models.DateField(("Date"), default=datetime.date.today)
    event_start_time = models.TimeField()
    event_end_time = models.TimeField()
    event_location = models.CharField(max_length=255)
    event_ticket_link = models.URLField(max_length=200)
    event_ticket_host = models.CharField(max_length=255)
    


    def __str__(self):
        return self.event_name
