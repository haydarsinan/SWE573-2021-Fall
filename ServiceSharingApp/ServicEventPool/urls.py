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
    path('profile', views.profile_page, name="profile_page"),

    path('add_location', views.add_location, name="add_location"),
    path('add_event', views.add_event, name="add_event"),
    path('add_service', views.add_service, name="add_service"),

    path('event_details/<slug:slug>', views.event_details, name="event_details"),
    path('service_details/<slug:slug>', views.service_details, name="service_details"),

    path('apply_service/<slug:slug>', views.apply_service, name="apply_service"),

]
