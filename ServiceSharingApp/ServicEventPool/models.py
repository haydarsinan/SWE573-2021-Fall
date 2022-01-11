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
    geoLocation = models.CharField(max_length=300, blank=True, null=True, default='41.083556 29.050598')

    def __str__(self):
        return self.name

class Media(models.Model):
        name = models.CharField(max_length=300, blank=True, null=True)
        media_pic = models.ImageField(null=True, blank=True, upload_to="ServicEventPool/images/systemPictures/")

        def __str__(self):
            return self.name


class Event(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True)
    event_date = models.DateField()
    event_time = models.TimeField(default='00:00')
    duration = models.PositiveIntegerField();
    location = models.CharField(max_length=300, blank=True, null=True)
    event_pic = models.ImageField(null=True, blank=True, upload_to="ServicEventPool/images/eventPictures/")
    event_publish_date = models.CharField(max_length=300, blank=True, null=True)
    slug = AutoSlugField(populate_from='name', unique=True, default="")
    event_provider = models.ForeignKey(User, default="", on_delete=models.CASCADE, related_name='user_event_provider')
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
    description = models.TextField(blank=True)
    service_date = models.DateField()
    service_time = models.TimeField(default='00:00')
    duration_credit = models.PositiveIntegerField();
    location = models.CharField(max_length=300, blank=True, null=True)
    service_pic = models.ImageField(null=True, blank=True, upload_to="ServicEventPool/images/servicePictures/")
    service_publish_date = models.CharField(max_length=300, blank=True, null=True)
    slug = AutoSlugField(populate_from='name', unique=True, default="")
    service_provider = models.ForeignKey(User, default="", on_delete=models.CASCADE, related_name='user_service_provider')
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
    commenter = models.ForeignKey(User, default="", null=True, blank=True, related_name='user_commenter', on_delete=models.CASCADE)
    commentTaker = models.ForeignKey(User, default="", null=True, blank=True, related_name='user_commentTaker',
                                  on_delete=models.CASCADE)
    service = models.ForeignKey(Service, default="", null=True, blank=True, related_name='service_comment',
                                on_delete=models.CASCADE)
    comment = models.TextField(max_length=300, blank=True, null=True)
    RATING_CHOICES = (
        (1, '1- Poor'),
        (2, '2- Fair'),
        (3, '3- Good'),
        (4, '4- Very Good'),
        (5, '5- Excellent')
                      )
    rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=3)


class Notification(models.Model):
    user = models.ForeignKey(User, default="", null=True, blank=True, related_name='user_notification', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, default="", null=True, blank=True, related_name='service_notification', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, default="", null=True, blank=True, related_name='event_notification', on_delete=models.CASCADE)
    other_user = models.ForeignKey(User, default="", null=True, blank=True, related_name='other_user_notification', on_delete=models.CASCADE)
    notification_datetime = models.DateTimeField()
    NOTIFICATION_CHOICES = (
        (1, 'Applied to Your Service'),
        (2, 'Applied to Your Event'),
        (3, 'Your application approved to Service'),
        (4, 'Your application approved to Event'),
        (5, 'Transaction is completed'),
        (6, 'Your application declined to Service'),
        (7, 'Your application declined to Event')
                      )
    types_notifications = models.PositiveIntegerField(choices=NOTIFICATION_CHOICES)

class Activity(models.Model):
    user = models.ForeignKey(User, default="", null=True, blank=True, related_name='user_activities', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, default="", null=True, blank=True, related_name='service_activities', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, default="", null=True, blank=True, related_name='event_activities', on_delete=models.CASCADE)
    other_user = models.ForeignKey(User, default="", null=True, blank=True, related_name='other_user_activities', on_delete=models.CASCADE)
    activity_datetime = models.DateTimeField()
    ACTIVITIES_CHOICES = (
        (1, 'Created a Service'),
        (2, 'Created an Event'),
        (3, 'Attended to Service'),
        (4, 'Attended to Event'),
                      )
    types_activities = models.PositiveIntegerField(choices=ACTIVITIES_CHOICES)

class User_Service_Status(models.Model):
    user_serviceStatus = models.ForeignKey(User, default="", null=True, blank=True, related_name='user_service_status_user', on_delete=models.CASCADE)
    service_serviceStatus = models.ForeignKey(Service, default="", null=True, blank=True, related_name='user_service_status_service', on_delete=models.CASCADE)
    USER_SERVICE_STATUS_CHOICES = (
        (1, 'Applied'),
        (2, 'Accepted'),
        (3, 'Finished'),
        (4, 'Not Finished'),
        (5, 'Declined')
                      )
    user_service_status = models.PositiveIntegerField(choices=USER_SERVICE_STATUS_CHOICES)

class User_Event_Status(models.Model):
    user_eventStatus = models.ForeignKey(User, default="", null=True, blank=True, related_name='user_event_status_user', on_delete=models.CASCADE)
    event_eventStatus = models.ForeignKey(Event, default="", null=True, blank=True, related_name='user_event_status_event', on_delete=models.CASCADE)
    USER_EVENT_STATUS_CHOICES = (
        (1, 'Applied'),
        (2, 'Accepted'),
        (3, 'Finished'),
        (4, 'Not Finished'),
        (5, 'Declined')
                      )
    user_event_status = models.PositiveIntegerField(choices=USER_EVENT_STATUS_CHOICES)
