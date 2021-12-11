from django.contrib import admin


from .models import Service
from .models import Event
from .models import Location

admin.site.register(Service)
admin.site.register(Event)
admin.site.register(Location)


