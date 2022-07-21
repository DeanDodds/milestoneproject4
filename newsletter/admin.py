from django.contrib import admin
from .models import NewletterSubscribers


# Register your models here.
class NewletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added',)

admin.site.register(NewletterSubscribers, NewletterAdmin)
