from django import forms
from django.forms import ModelForm
from .models import Location
from .models import Event
from .models import Service
from .models import Comment


class LocationForm(ModelForm):
    class Meta:
        model = Location
        # fields = "__all__"
        fields = ('name', 'geoLocation')

        labels = {
            'name': 'Enter the Name of the Location',
            'geoLocation': 'Detect GeoLocation',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of the Location'}),
            'geoLocation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'GeoLocation'}),
        }


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        # fields = ('name', '')

        # labels = {
        #     'name': 'Enter the Name of the Event',
        #     'event_date': 'Date',
        #     'event_publish_date': 'Publish Date',
        #     'description': 'Description',
        #     'slug': 'Slug',
        #     'location': 'Location',
        #     'attendees': 'Attendees',
        # }
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of the Event'}),
        #     'event_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
        #     'event_publish_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Publish Date'}),
        #     'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        #     'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'slug'}),
        #     'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
        #     'attendees': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
        # }


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = "__all__"
        # fields = ('name', '')

        # labels = {
        #     'name': 'Enter the Name of the Service',
        #     'service_date': 'Date',
        #     'service_publish_date': 'Publish Date',
        #     'description': 'Description',
        #     'slug': 'Slug',
        #     'location': 'Location',
        #     'service_provider': 'Service Provider',
        #     'duration_credit': 'Time Credit Requested',
        # }
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of the Service'}),
        #     'service_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
        #     'service_publish_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Publish Date'}),
        #     'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        #     'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'slug'}),
        #     'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
        #     'service_provider': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Service Provider'}),
        #     'duration_credit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Time Credit Requested'}),
        # }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"