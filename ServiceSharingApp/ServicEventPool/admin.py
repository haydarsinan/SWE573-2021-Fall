from django.contrib import admin

from .models import Location, Profile, Event, Service

admin.site.register(Service)
admin.site.register(Event)
admin.site.register(Location)
admin.site.register(Profile)


