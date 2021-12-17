from django.shortcuts import render, redirect
from .models import Service
from .models import Event
from .forms import LocationForm
from .forms import EventForm
from .forms import ServiceForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages


def home(request):
    serviceName = "I like Baklava with Olive Oil :)"
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

def profile_page(request):
    user = request.user
    return render(request, 'ServicEventPool/profile_page.html',
                  {'user': user})

def all_services(request):
    service_list = Service.objects.all()
    return render(request, 'ServicEventPool/service_list.html',
                  {'service_list': service_list})


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'ServicEventPool/event_list.html',
                  {'event_list': event_list})


def add_location(request):
    submitted = False
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_location?submitted=True')
    else:
        form = LocationForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'ServicEventPool/add_location.html', {
        'form': form,
        'submitted': submitted,
    })


def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'ServicEventPool/add_event.html', {
        'form': form,
        'submitted': submitted,
    })

def add_service(request):
    submitted = False
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_service?submitted=True')
    else:
        form = ServiceForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'ServicEventPool/add_service.html', {
        'form': form,
        'submitted': submitted,
    })

def event_details(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'ServicEventPool/event_details.html',
                  {'event': event})

def service_details(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'ServicEventPool/service_details.html',
                  {'service': service})

def apply_service(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'ServicEventPool/service_details.html',
                  {'service': service})
    # user = request.user
    # service = get_object_or_404(Service, slug=slug)
    # print(service.name)
    # if service.objects.filter(applicants=user.id):
    #     messages.success(request, "You have already requested this service!")
    #     return redirect('service_details')
    # else:
    #     service.applicants.add(user)
    #     messages.success(request, "You successfully requested for the service!")
    #     return render(request, 'ServicEventPool/apply_service.html',
    #                   {'service': service})
