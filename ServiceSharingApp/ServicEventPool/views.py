from django.shortcuts import render, redirect
from .models import Service
from .models import Event
from .models import Notification
from .models import Activity
from .models import Media
from .forms import LocationForm
from .forms import EventForm
from .forms import ServiceForm
from .forms import CommentForm
from .forms import MediaForm
from .forms import UpdateProfilePersonalForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Profile
from django.db.models import Q
import datetime


def home(request):
    serviceName = "I like Baklava with Olive Oil :)"
    medias = Media.objects.all()
    if medias.get(name='homePage1'):
        media1 = medias.get(name='homePage1')
    if medias.get(name='homePage2'):
        media2 = medias.get(name='homePage2')
    return render(request, 'ServicEventPool/home.html', {
        "serviceName_Here": serviceName,
        "medias": medias,
        "media1": media1,
        "media2": media2
    })

def mediaUpload(request):
    submitted = False
    if request.method == "POST":
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return HttpResponseRedirect('/mediaUpload?submitted=True')
    else:
        form = MediaForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'ServicEventPool/media.html', {
        'form': form,
        'submitted': submitted,
    })

def calendar(request, year, month):
    year = year
    month = month
    return render(request, 'ServicEventPool/calendar.html', {
        "year_Here": year,
        "month_Here": month
    })

def update_user_profile_personal(request):
    if request.method == "POST":
        form = UpdateProfilePersonalForm(request.POST, request.FILES, instance=request.user.profile)
        print("DENEME")
        if form.is_valid():
            form.save()
            print("deneme")
            messages.success(request, "You successfully updated!")
            return redirect('home')
    else:
        form = UpdateProfilePersonalForm(instance=request.user.profile)
    return render(request, 'ServicEventPool/update_profile_personal.html', {
        'form': form,
    })




def profile_page(request):
    user = request.user
    services = Service.objects.all()
    events = Event.objects.all()
    servicesCreated = services.filter(Q(service_provider=user))
    numberOfServicesCreated = servicesCreated.__len__()
    servicesApplied = services.filter(Q(applicants__username=user))
    servicesApproved = services.filter(Q(attendees__username=user))
    numberOfServicesApproved = servicesApproved.__len__()
    servicesDeclined = services.filter(Q(declinedList__username=user))
    eventsCreated = events.filter(Q(event_provider=user))
    numberOfEventsCreated = eventsCreated.__len__()
    eventsApplied = events.filter(Q(applicants__username=user))
    eventsApproved = events.filter(Q(attendees__username=user))
    numberOfEventsApproved = eventsApproved.__len__()
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
                   'eventsDeclined': eventsDeclined,
                   'numberOfServicesCreated': numberOfServicesCreated,
                   'numberOfServicesApproved': numberOfServicesApproved,
                   'numberOfEventsCreated': numberOfEventsCreated,
                   'numberOfEventsApproved': numberOfEventsApproved
                   })

def profile_page_others(request, id):
    profile = get_object_or_404(Profile, pk=id)
    user = profile.user
    services = Service.objects.all()
    events = Event.objects.all()

    servicesCreated = services.filter(Q(service_provider=user))
    numberOfServicesCreated = servicesCreated.__len__()
    servicesApplied = services.filter(Q(applicants__username=user))
    servicesApproved = services.filter(Q(attendees__username=user))
    numberOfServicesApproved = servicesApproved.__len__()
    servicesDeclined = services.filter(Q(declinedList__username=user))
    eventsCreated = events.filter(Q(event_provider=user))
    numberOfEventsCreated = eventsCreated.__len__()
    eventsApplied = events.filter(Q(applicants__username=user))
    eventsApproved = events.filter(Q(attendees__username=user))
    numberOfEventsApproved = eventsApproved.__len__()
    eventsDeclined = events.filter(Q(declinedList__username=user))

    return render(request, 'ServicEventPool/profile_page_others.html',
                  {'profile': profile,
                   'user': user,
                   'servicesCreated': servicesCreated,
                   'servicesApplied': servicesApplied,
                   'servicesApproved': servicesApproved,
                   'servicesDeclined': servicesDeclined,
                   'eventsCreated': eventsCreated,
                   'eventsApplied': eventsApplied,
                   'eventsApproved': eventsApproved,
                   'eventsDeclined': eventsDeclined,
                   'numberOfServicesCreated': numberOfServicesCreated,
                   'numberOfServicesApproved': numberOfServicesApproved,
                   'numberOfEventsCreated': numberOfEventsCreated,
                   'numberOfEventsApproved': numberOfEventsApproved
                   })

def all_services(request):
    service_list = Service.objects.all()
    service_list = Service.objects.order_by('-id')
    return render(request, 'ServicEventPool/service_list.html',
                  {'service_list': service_list})


def all_events(request):
    event_list = Event.objects.all()
    event_list = Event.objects.order_by('-id')
    return render(request, 'ServicEventPool/event_list.html',
                  {'event_list': event_list})

def serviceSearch(request):
    service_list = Service.objects.all()
    searchText = request.GET.get('serviceSearch')
    service_list = Service.objects.order_by('-id')
    if searchText:
        service_list =  service_list.filter(Q(name__icontains=searchText) |
                                            Q(description__icontains=searchText))

    return render(request, 'ServicEventPool/service_list.html',
                  {'service_list': service_list})

def eventSearch(request):
    event_list = Event.objects.all()
    searchText = request.GET.get('eventSearch')
    print(searchText)
    event_list = Event.objects.order_by('-id')
    if searchText:
        event_list =  event_list.filter(Q(name__icontains=searchText) |
                                            Q(description__icontains=searchText))
    return render(request, 'ServicEventPool/event_list.html',
                  {'event_list': event_list})

def notifications(request):
    notificationList = Notification.objects.filter(user=request.user)
    return render(request, 'ServicEventPool/notifications.html',
                  {'notificationList': notificationList})

def newsFeed(request):
    activityList = Activity.objects.filter(user=request.user)
    return render(request, 'ServicEventPool/news_feed.html',
                  {'activityList': activityList})

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
    user = request.user
    time = datetime.datetime.now()
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.event_provider = user
            obj.event_publish_date = time
            obj.save()
            newActivity = Activity.objects.create(user=user, event=obj, types_activities=2)
            newActivity.save()
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
    user = request.user
    time = datetime.datetime.now()
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.service_provider = user
            obj.service_publish_date = time
            obj.save()
            newActivity = Activity.objects.create(user=user, service=obj, types_activities=1)
            newActivity.save()
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
            'event': event,
            'user': user
        }
        return render(request, 'ServicEventPool/event_details.html', context)
    else:
        return render(request, 'ServicEventPool/event_details.html',
                      {'event': event})


def service_details(request, slug):
    service = get_object_or_404(Service, slug=slug)
    user = request.user
    return render(request, 'ServicEventPool/service_details.html',
                  {'service': service,
                   'user': user})

def request_service(request, slug):
    service = get_object_or_404(Service, slug=slug)
    user = request.user
    if (user.profile.timeCredit-user.profile.blockedCredit)>=service.duration_credit:
        service.applicants.add(user)
        currentBlockedCredit = user.profile.blockedCredit
        user.profile.blockedCredit = currentBlockedCredit + service.duration_credit
        user.profile.save()
        context = {
            'service': service
        }
        messages.success(request, "You send request successfully!")
        return render(request, 'ServicEventPool/service_details.html', context)
    else:
        messages.success(request, "You do not have enough credits!")
        return HttpResponseRedirect('/service_details/'+slug)

def request_back_service(request, slug):
    service = get_object_or_404(Service, slug=slug)
    user = request.user
    service.applicants.remove(user)
    currentBlockedCredit = user.profile.blockedCredit
    user.profile.blockedCredit = currentBlockedCredit - service.duration_credit
    user.profile.save()
    messages.success(request, "You withdraw your request!")
    return HttpResponseRedirect('/service_details/' + slug)

def approve_service(request, slug):
    service = get_object_or_404(Service, slug=slug)
    applicants = service.applicants.all()
    # print(applicants.get(pk=5).profile.pk)
    return render(request, 'ServicEventPool/service_applications.html',
                  {'service': service,
                   'applicants': applicants
                   })



def approve_applicant_service(request, slug, id):
    service = get_object_or_404(Service, slug=slug)
    applicant = service.applicants.get(id=id)
    service.attendees.add(applicant)
    service.applicants.remove(applicant)
    applicants = service.applicants.all()
    newActivity = Activity.objects.create(user=applicant, other_user=request.user, service=service, types_activities=3)
    newActivity.save()
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
    applicant = service.applicants.get(id=id)
    service.declinedList.add(applicant)
    service.applicants.remove(applicant)
    applicants = service.applicants.all()
    attendees = service.attendees.all()
    currentBlockedCredit = applicant.profile.blockedCredit
    applicant.profile.blockedCredit = currentBlockedCredit - service.duration_credit
    applicant.profile.save()
    context = {
        'service': service,
        'applicants': applicants,
        'attendees': attendees,
    }
    return HttpResponseRedirect('/attendees/'+slug)

def decline_back_applicant_service(request, slug, id):
    service = get_object_or_404(Service, slug=slug)
    applicant = service.declinedList.get(id=id)
    service.applicants.add(applicant)
    service.declinedList.remove(applicant)
    applicants = service.applicants.all()
    attendees = service.attendees.all()
    currentBlockedCredit = applicant.profile.blockedCredit
    applicant.profile.blockedCredit = currentBlockedCredit + service.duration_credit
    applicant.profile.save()
    context = {
        'service': service,
        'applicants': applicants,
        'attendees': attendees,
    }
    return HttpResponseRedirect('/attendees/'+slug)

def approve_service_transaction(request, slug):
    service = get_object_or_404(Service, slug=slug)
    user = request.user

    currentServiceProviderCredit = service.service_provider.profile.timeCredit
    currentServiceTakerCredit = user.profile.timeCredit
    currentServiceTakerBlockedCredit = user.profile.blockedCredit
    if user in service.attendees.all():

        submitted = False
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save()
                user.profile.timeCredit = currentServiceTakerCredit - service.duration_credit
                service.service_provider.profile.timeCredit = currentServiceProviderCredit + service.duration_credit
                user.profile.blockedCredit = currentServiceTakerBlockedCredit - service.duration_credit
                user.profile.save()
                service.service_provider.profile.save()
                # messages.success("Transaction is completed!")
                return HttpResponseRedirect('/approve_service_transaction/' + slug +'?submitted=True')
        else:
            form = CommentForm
        return render(request, 'ServicEventPool/approve_service_transaction.html', {
            'form': form,
            'submitted': submitted,
        })



def attend_event(request, slug):
    event = get_object_or_404(Event, slug=slug)
    user = request.user
    event.applicants.add(user)

    context = {
        'event': event
    }
    messages.success(request, "You send your application successfully!")
    return render(request, 'ServicEventPool/event_details.html', context)


def attend_back_event(request, slug):
    event = get_object_or_404(Event, slug=slug)
    user = request.user
    event.applicants.remove(user)
    messages.success(request, "You withdraw your application!")
    return HttpResponseRedirect('/event_details/' + slug)

def approve_event(request, slug):
    event = get_object_or_404(Event, slug=slug)
    applicants = event.applicants.all()
    return render(request, 'ServicEventPool/event_applications.html',
                  {'event': event,
                   'applicants': applicants
                   })



def approve_applicant_event(request, slug, id):
    event = get_object_or_404(Event, slug=slug)
    applicant = event.applicants.get(id=id)
    event.attendees.add(applicant)
    event.applicants.remove(applicant)
    applicants = event.applicants.all()
    newActivity = Activity.objects.create(user=applicant, other_user=request.user, event=event, types_activities=4)
    newActivity.save()
    context = {
        'event': event,
        'applicants': applicants
    }
    return HttpResponseRedirect('/attendees_event/'+slug)

def unapprove_applicant_event(request, slug, id):
    event = get_object_or_404(Event, slug=slug)
    attendee = event.attendees.get(id=id)
    event.applicants.add(attendee)
    event.attendees.remove(attendee)
    applicants = event.applicants.all()
    attendees = event.attendees.all()
    context = {
        'event': event,
        'applicants': applicants,
        'attendees': attendees,
    }
    return HttpResponseRedirect('/attendees_event/'+slug)


def decline_applicant_event(request, slug, id):
    event = get_object_or_404(Event, slug=slug)
    applicant = event.applicants.get(id=id)
    event.declinedList.add(applicant)
    event.applicants.remove(applicant)
    applicants = event.applicants.all()
    attendees = event.attendees.all()
    context = {
        'event': event,
        'applicants': applicants,
        'attendees': attendees,
    }
    return HttpResponseRedirect('/attendees_event/'+slug)

def decline_back_applicant_event(request, slug, id):
    event = get_object_or_404(Event, slug=slug)
    applicant = event.declinedList.get(id=id)
    event.applicants.add(applicant)
    event.declinedList.remove(applicant)
    applicants = event.applicants.all()
    attendees = event.attendees.all()
    context = {
        'event': event,
        'applicants': applicants,
        'attendees': attendees,
    }
    return HttpResponseRedirect('/attendees_event/'+slug)

def complete_event(request, slug):
    event = get_object_or_404(Event, slug=slug)
    user = request.user
    event.event_status = 3
    event.save()
    return HttpResponseRedirect('/attendees_event/'+slug)

def delete_service(request, slug):
    service = get_object_or_404(Service, slug=slug)
    service.delete()
    return HttpResponseRedirect('/services')

def delete_event(request, slug):
    event = get_object_or_404(Event, slug=slug)
    event.delete()
    return HttpResponseRedirect('/events')
