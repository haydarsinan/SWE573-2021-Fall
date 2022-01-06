from django.db import models
from django.contrib.auth.models import User
from django.db.models import PositiveIntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator
from autoslug import AutoSlugField


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='pk', unique=True)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="ServicEventPool/images/profilePictures/")
    linkedinURL = models.CharField(max_length=255, null=True, blank=True)
    instagramURL = models.CharField(max_length=255, null=True, blank=True)
    twitterURL = models.CharField(max_length=255, null=True, blank=True)
    timeCredit = models.PositiveIntegerField(default=5, validators=[
        MaxValueValidator(15),
        MinValueValidator(0)
    ])
    blockedCredit = models.PositiveIntegerField(default=0, validators=[
        MaxValueValidator(15),
        MinValueValidator(0)
    ])

    def __str__(self):
        return str(self.user)


class Location(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    geoLocation = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    event_pic = models.ImageField(null=True, blank=True, upload_to="ServicEventPool/images/eventPictures/")
    event_date = models.DateTimeField()
    event_publish_date = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, default="")
    event_provider = models.ForeignKey(User, default="", on_delete=models.CASCADE, related_name='user_event_provider')
    location = models.ForeignKey(Location, default="", on_delete=models.CASCADE)
    applicants = models.ManyToManyField(User, default="", null=True, blank=True, related_name='user_event_applicants')
    attendees = models.ManyToManyField(User, default="", null=True, blank=True, related_name='user_event_attendees')
    declinedList = models.ManyToManyField(User, default="", null=True, blank=True,
                                          related_name='user_event_declinedlist')
    EVENT_STATUS = (
        (1, 'Open to Application'),
        (2, 'Closed to Application'),
        (3, 'Completed')
    )
    event_status = models.PositiveIntegerField(choices=EVENT_STATUS, default=1)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    service_pic = models.ImageField(null=True, blank=True, upload_to="ServicEventPool/images/servicePictures/")
    service_date = models.DateTimeField()
    service_publish_date = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, default="")
    duration_credit = models.PositiveIntegerField();
    service_provider = models.ForeignKey(User, default="", on_delete=models.CASCADE, related_name='user_service_provider')
    location = models.ForeignKey(Location, default="", on_delete=models.CASCADE)
    applicants = models.ManyToManyField(User, default="", null=True, blank=True, related_name='user_service_applicants')
    attendees = models.ManyToManyField(User, default="", null=True, blank=True, related_name='user_service_attendees')
    declinedList = models.ManyToManyField(User, default="", null=True, blank=True, related_name='user_service_declinedlist')

    SERVICE_STATUS = (
        (1, 'Open to Application'),
        (2, 'Closed to Application'),
        (3, 'Completed')
    )
    service_status = models.PositiveIntegerField(choices=SERVICE_STATUS, default=1)


    def __str__(self):
        return self.name

class Comment(models.Model):
    comment = models.TextField(max_length=300, blank=True, null=True)
    RATING_CHOICES = (
        (1, '1- Poor'),
        (2, '2- Fair'),
        (3, '3- Good'),
        (4, '4- Very Good'),
        (5, '5- Excellent')
                      )
    rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=3)


# class Notification(models.Model):
#     comment = models.TextField(max_length=300, blank=True, null=True)
#     RATING_CHOICES = (
#         (1, '1- Poor'),
#         (2, '2- Fair'),
#         (3, '3- Good'),
#         (4, '4- Very Good'),
#         (5, '5- Excellent')
#                       )
#     rating = models.PositiveIntegerField(choices=RATING_CHOICES)
#
# class Activities(models.Model):
#     comment = models.TextField(max_length=300, blank=True, null=True)
#     RATING_CHOICES = (
#         (1, '1- Poor'),
#         (2, '2- Fair'),
#         (3, '3- Good'),
#         (4, '4- Very Good'),
#         (5, '5- Excellent')
#                       )
#     rating = models.PositiveIntegerField(choices=RATING_CHOICES)
#
class User_Service_Status(models.Model):
    user_serviceStatus = models.ManyToManyField(User, default="", null=True, blank=True, related_name='user_service_status_user')
    service_serviceStatus = models.ManyToManyField(Service, default="", null=True, blank=True, related_name='user_service_status_service')
    USER_SERVICE_STATUS_CHOICES = (
        (1, 'Applied'),
        (2, 'Accepted'),
        (3, 'Finished'),
        (4, 'Not Finished'),
        (5, 'Declined')
                      )
    user_service_status = models.PositiveIntegerField(choices=USER_SERVICE_STATUS_CHOICES)

class User_Event_Status(models.Model):
    user_eventStatus = models.ManyToManyField(User, default="", null=True, blank=True, related_name='user_event_status_user')
    event_eventStatus = models.ManyToManyField(Event, default="", null=True, blank=True, related_name='user_event_status_event')
    USER_EVENT_STATUS_CHOICES = (
        (1, 'Applied'),
        (2, 'Accepted'),
        (3, 'Finished'),
        (4, 'Not Finished'),
        (5, 'Declined')
                      )
    user_event_status = models.PositiveIntegerField(choices=USER_EVENT_STATUS_CHOICES)
