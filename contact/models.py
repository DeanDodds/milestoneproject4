from django.db import models


# Create your models here.

class Message(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    subject = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    message = models.TextField(max_length=500, null=False, blank=False)
    received = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
