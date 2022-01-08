from django.contrib import admin

from .models import Location, Profile, Event, Service, Notification, Activity, Media

admin.site.register(Service)
admin.site.register(Event)
admin.site.register(Location)
admin.site.register(Profile)
admin.site.register(Notification)
admin.site.register(Activity)
admin.site.register(Media)


