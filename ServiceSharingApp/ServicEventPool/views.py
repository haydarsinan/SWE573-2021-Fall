from django.shortcuts import render, redirect
from .models import Service
from .models import Event
from .forms import LocationForm
from .forms import EventForm
from .forms import ServiceForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Profile
from django.db.models import Q


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
    services = Service.objects.all()
    events = Event.objects.all()
    servicesCreated = services.filter(Q(service_provider=user))
    servicesApplied = services.filter(Q(applicants__username=user))
    servicesApproved = services.filter(Q(attendees__username=user))
    servicesDeclined = services.filter(Q(declinedList__username=user))
    eventsCreated = events.filter(Q(event_provider=user))
    eventsApplied = events.filter(Q(applicants__username=user))
    eventsApproved = events.filter(Q(attendees__username=user))
    eventsDeclined = events.filter(Q(declinedList__username=user))
    return render(request, 'ServicEventPool/profile_page.html',
                  {'user': user,
                   'servicesCreated': servicesCreated,
                   'servicesApplied': servicesApplied,
                   'servicesApproved': servicesApproved,
                   'servicesDeclined': servicesDeclined,
                   'eventsCreated': eventsCreated,
                   'eventsApplied': eventsApplied,
                   'eventsApproved': eventsApproved,
                   'eventsDeclined': eventsDeclined
                   })

def profile_page_others(request, id):
    profile = get_object_or_404(Profile, pk=id)
    return render(request, 'ServicEventPool/profile_page_others.html',
                  {'profile': profile})

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
    if request.method == "POST":
        event = get_object_or_404(Event, slug=slug)
        user = request.user
        event.applicants.add(user)
        context = {
            'event': event
        }
        return render(request, 'ServicEventPool/event_details.html', context)
    else:
        return render(request, 'ServicEventPool/event_details.html',
                      {'event': event})


def service_details(request, slug):
    service = get_object_or_404(Service, slug=slug)
    if request.method == "POST":
        service = get_object_or_404(Service, slug=slug)
        user = request.user
        service.applicants.add(user)
        context = {
            'service': service
        }
        return render(request, 'ServicEventPool/service_details.html', context)
    else:
        return render(request, 'ServicEventPool/service_details.html',
                      {'service': service})

def approve_service(request, slug):
    service = get_object_or_404(Service, slug=slug)
    applicants = service.applicants.all()
    # print(applicants.get(pk=5).profile.pk)
    attendee = request.GET.get('attendee')
    if request.method == "POST":
        user = attendee
        service.attendees.add(user)
        service.applicants.remove(user)
        context = {
            'service': service,
            'applicants': applicants
        }
        return render(request, 'ServicEventPool/service_applications.html', context)
    else:
        return render(request, 'ServicEventPool/service_applications.html',
                        {'service': service,
                         'applicants': applicants
                         })

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


def approve_applicant_service(request, slug, id):
    service = get_object_or_404(Service, slug=slug)
    applicant = service.applicants.get(id=id)
    service.attendees.add(applicant)
    service.applicants.remove(applicant)
    applicants = service.applicants.all()
    context = {
        'service': service,
        'applicants': applicants
    }
    return HttpResponseRedirect('/attendees/'+slug)

def unapprove_applicant_service(request, slug, id):
    service = get_object_or_404(Service, slug=slug)
    attendee = service.attendees.get(id=id)
    service.applicants.add(attendee)
    service.attendees.remove(attendee)
    applicants = service.applicants.all()
    attendees = service.attendees.all()
    context = {
        'service': service,
        'applicants': applicants,
        'attendees': attendees,
    }
    return HttpResponseRedirect('/attendees/'+slug)


def decline_applicant_service(request, slug, id):
    service = get_object_or_404(Service, slug=slug)
    applicant = service.applicant.get(id=id)
    service.applicants.add(attendee)
    service.attendees.remove(attendee)
    applicants = service.applicants.all()
    attendees = service.attendees.all()
    context = {
        'service': service,
        'applicants': applicants,
        'attendees': attendees,
    }
    return HttpResponseRedirect('/attendees/'+slug)