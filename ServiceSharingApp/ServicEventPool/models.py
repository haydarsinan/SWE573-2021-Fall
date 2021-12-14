from django.db import models
from django.contrib.auth.models import User
from django.db.models import PositiveIntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator
from autoslug import AutoSlugField


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
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

    # Change models of location and attendees!!
    event_provider = models.ForeignKey(User, default="", on_delete=models.CASCADE)
    location = models.ForeignKey(Location, default="", on_delete=models.CASCADE)

    # attendees = models.ManyToManyField(Profile, blank=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    service_date = models.DateTimeField()
    service_publish_date = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, default="")
    duration_credit = models.PositiveIntegerField();

    # Change models of location, provider, and lists!!
    service_provider = models.ForeignKey(User, default="", on_delete=models.CASCADE)
    location = models.ForeignKey(Location, default="", on_delete=models.CASCADE)

    # request_list = models.ManyToManyField(Profile, blank=True)
    # approved_list = models.ManyToManyField(Profile, blank=True)

    def __str__(self):
        return self.name
