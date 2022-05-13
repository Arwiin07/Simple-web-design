from django.contrib import admin
from .models import Meetup,Locations,participant


class MeetupAdmin(admin.ModelAdmin):
    list_display=("title","date","location")
    list_filter=("location","date")
    prepopulated_fields={"slug":('title',)}

admin.site.register(Meetup,MeetupAdmin)
admin.site.register(Locations)
admin.site.register(participant)
# Register your models here.
