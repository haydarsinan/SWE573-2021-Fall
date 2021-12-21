from django.db import models
from django.contrib.auth.models import User
from django.db.models import PositiveIntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator
from autoslug import AutoSlugField


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='pk', unique=True)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="ServicEventPool/profilePictures/")
    linkedinURL = models.CharField(max_length=255, null=True, blank=True)
    instagramURL = models.CharField(max_length=255, null=True, blank=True)
    twitterURL = models.CharField(max_length=255, null=True, blank=True)
    timeCredit = models.PositiveIntegerField(default=5, validators=[
        MaxValueValidator(100),
        MinValueValidator(1)
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
    event_date = models.DateTimeField()
    event_publish_date = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, default="")
    event_provider = models.ForeignKey(User, default="", on_delete=models.CASCADE, related_name='user_event_provider')
    location = models.ForeignKey(Location, default="", on_delete=models.CASCADE)
    applicants = models.ManyToManyField(User, default="", blank=True, related_name='user_event_applicants')
    attendees = models.ManyToManyField(User, default="", blank=True, related_name='user_event_attendees')

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    service_date = models.DateTimeField()
    service_publish_date = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, default="")
    duration_credit = models.PositiveIntegerField();
    service_provider = models.ForeignKey(User, default="", on_delete=models.CASCADE, related_name='user_service_provider')
    location = models.ForeignKey(Location, default="", on_delete=models.CASCADE)
    applicants = models.ManyToManyField(User, default="", blank=True, related_name='user_service_applicants')
    attendees = models.ManyToManyField(User, default="", blank=True, related_name='user_service_attendees')
    def __str__(self):
        return self.name
