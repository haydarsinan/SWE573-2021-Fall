from django.urls import path
from . import views

"""
Notes:
int: numbers
str: String
path: whole urls /
slug: hypen-and-underscores-stuff
UUID: universal unique ID
"""
urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/<str:month>', views.calendar, name="calendar"),
    path('services', views.all_services, name="service_list"),
    path('events', views.all_events, name="event_list"),
]
