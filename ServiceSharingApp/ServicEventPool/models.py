from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    geoLocation = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=300, blank=True, null=True)
    email = models.EmailField()
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)

    # telephone =
    # location =
    # time_credit =
    # password =
    # event_created =
    # event_attended =
    # service_given =
    # service_taken =

    def __str__(self):
        return self.username


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
