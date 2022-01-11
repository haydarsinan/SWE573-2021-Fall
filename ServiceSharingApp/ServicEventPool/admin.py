from django.contrib import admin

from .models import Location, Profile, Event, Service, Notification, Activity, Media, Comment, User_Event_Status, User_Service_Status

admin.site.register(Service)
admin.site.register(Event)
admin.site.register(Location)
admin.site.register(Profile)
admin.site.register(Notification)
admin.site.register(Activity)
admin.site.register(Media)
admin.site.register(Comment)
admin.site.register(User_Event_Status)
admin.site.register(User_Service_Status)


