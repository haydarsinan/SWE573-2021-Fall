from django import forms
from django.forms import ModelForm
from .models import Location
from .models import Event
from .models import Service
from .models import Comment
from .models import Media
from .models import Profile


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
        exclude = ('applicants', 'attendees', 'event_provider', 'event_publish_date',
                   'event_status', 'declinedList')

        labels = {
            'name': 'Enter the Name of the Event',
            'event_date': 'Date',
            'event_time': 'Time',
            'event_publish_date': 'Publish Date',
            'description': 'Description',
            'slug': 'Slug',
            'location': 'Location',
            'attendees': 'Attendees',
        }
        widgets = {
            'name': forms.widgets.TextInput(attrs={'placeholder': 'Name of the Event',}),
            'event_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'event_time': forms.widgets.TimeInput(attrs={'type': 'time'}),
            'event_publish_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Publish Date'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'slug'}),
            'location': forms.widgets.Select(attrs={'placeholder': 'Location'}),
            'attendees': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
        }


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = "__all__"
        # fields = ('name', 'description', 'location', 'duration_credit', 'service_date', 'service_pic')
        exclude = ('applicants', 'attendees', 'service_provider', 'service_publish_date',
                   'service_status', 'declinedList')

        labels = {
            'name': 'Enter the Name of the Service',
            'service_date': 'Date',
            'service_time': 'Time',
            'service_publish_date': 'Publish Date',
            'description': 'Description',
            'slug': 'Slug',
            'location': 'Location',
            'service_provider': 'Service Provider',
            'duration_credit': 'Time Credit Requested',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name of the Service'}),
            # 'service_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
            'service_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'service_time': forms.widgets.TimeInput(attrs={'type': 'time'}),
            'service_publish_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Publish Date'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description', 'style': 'width:500px'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'slug'}),
            'location': forms.widgets.Select(attrs={'placeholder': 'Location'}),
            'service_provider': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Service Provider'}),
            'duration_credit': forms.TextInput(attrs={'placeholder': 'Time Credit Requested'}),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ('commenter', 'commentTaker', 'service', 'event')

class MediaForm(ModelForm):
    class Meta:
        model = Media
        fields = "__all__"

class UpdateProfilePersonalForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ('user', 'twitterURL', 'linkedinURL', 'instagramURL', 'timeCredit', 'blockedCredit')

        labels = {
            'bio': 'Short Biography',
        }

        widgets = {
            'bio': forms.TextInput(attrs={'style': 'width:500px; height:100px'}),
        }
