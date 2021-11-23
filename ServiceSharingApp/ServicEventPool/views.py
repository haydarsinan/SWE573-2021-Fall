from django.shortcuts import render
from .models import Service
from .models import Event


# Create your views here.

def home(request):
    serviceName = "Baklava with Olive Oil"
    return render(request, 'ServicEventPool/home.html', {
        "serviceName_Here": serviceName
    })


def calendar(request, year, month):
    year = year
    month = month
    return render(request, 'ServicEventPool/calendar.html', {
        "year_Here": year,
        "month_Here": month
    })


def all_services(request):
    service_list = Service.objects.all()
    return render(request, 'ServicEventPool/service_list.html',
                  {'service_list': service_list})


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'ServicEventPool/event_list.html',
                  {'event_list': event_list})
