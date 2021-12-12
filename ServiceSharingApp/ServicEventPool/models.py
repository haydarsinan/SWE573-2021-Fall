from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="ServicEventPool/profilePictures/")
    linkedinURL = models.CharField(max_length=255, null=True, blank=True)
    instagramURL = models.CharField(max_length=255, null=True, blank=True)
    twitterURL = models.CharField(max_length=255, null=True, blank=True)


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
    slug = models.URLField(blank=True, null=True)
    # location = models.CharField(max_length=300, blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    attendees = models.TextField(blank=True, null=True)

    # Change models of location and attendees!!
    # location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.CASCADE)
    # attendees = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    service_date = models.DateTimeField()
    service_publish_date = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True)
    slug = models.URLField(blank=True, null=True)
    # location = models.CharField(max_length=300, blank=True, null=True)
    duration_credit = models.PositiveIntegerField();
    service_provider = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)

    # Change models of location, provider, and lists!!
    # service_provider = models.ForeignKey(User, on_delete=models.CASCADE)
    # location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.CASCADE)
    # request_list = models.ManyToManyField(User, blank=True)
    # approved_list = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name
