from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('profile/<int:id>', views.profile_page_others, name="profile_page_others"),
    path('update_profile_personal', views.update_user_profile_personal, name="update_user_profile_personal"),

    path('mediaUpload', views.mediaUpload, name="mediaUpload"),

    path('eventSearch', views.eventSearch, name="eventSearch"),
    path('serviceSearch', views.serviceSearch, name="serviceSearch"),
    path('profileSearch', views.profileSearch, name="profileSearch"),

    path('notifications', views.notifications, name="notifications"),
    path('newsFeed', views.newsFeed, name="newsFeed"),

    path('add_location', views.add_location, name="add_location"),
    path('add_event', views.add_event, name="add_event"),
    path('add_service', views.add_service, name="add_service"),

    path('delete_service/<slug:slug>', views.delete_service, name="delete_service"),
    path('delete_event/<slug:slug>', views.delete_event, name="delete_event"),

    path('update_service/<slug:slug>', views.update_service, name="update_service"),
    path('update_event/<slug:slug>', views.update_event, name="update_event"),

    path('event_details/<slug:slug>', views.event_details, name="event_details"),
    path('service_details/<slug:slug>', views.service_details, name="service_details"),

    path('request_service/<slug:slug>', views.request_service, name="request_service"),
    path('request_back_service/<slug:slug>', views.request_back_service, name="request_back_service"),

    path('attend_event/<slug:slug>', views.attend_event, name="attend_event"),
    path('attend_back_event/<slug:slug>', views.attend_back_event, name="attend_back_event"),

    path('attendees/<slug:slug>', views.approve_service, name="approve_service"),
    path('attendees_event/<slug:slug>', views.approve_event, name="approve_event"),

    path('approve/<slug:slug>/<int:id>', views.approve_applicant_service, name="approve_applicant_service"),
    path('unapprove/<slug:slug>/<int:id>', views.unapprove_applicant_service, name="unapprove_applicant_service"),
    path('decline/<slug:slug>/<int:id>', views.decline_applicant_service, name="decline_applicant_service"),
    path('decline_back_service/<slug:slug>/<int:id>', views.decline_back_applicant_service, name="decline_back_applicant_service"),

    path('approve_event/<slug:slug>/<int:id>', views.approve_applicant_event,name="approve_applicant_event"),
    path('unapprove_event/<slug:slug>/<int:id>', views.unapprove_applicant_event,name="unapprove_applicant_event"),
    path('decline_event/<slug:slug>/<int:id>', views.decline_applicant_event,name="decline_applicant_event"),
    path('decline_back_event/<slug:slug>/<int:id>', views.decline_back_applicant_event, name="decline_back_applicant_event"),

    path('approve_service_transaction/<slug:slug>', views.approve_service_transaction, name="approve_service_transaction"),
    path('complete_event/<slug:slug>', views.complete_event, name="complete_event"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
