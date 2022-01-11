from django.shortcuts import render, redirect
from .models import Service, Event, Notification, Activity, Media, User_Service_Status, User_Event_Status,Comment
from .forms import LocationForm, EventForm, ServiceForm, CommentForm, MediaForm,UpdateProfilePersonalForm
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
        if form.is_valid():
            form.save()
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
    comments = Comment.objects.filter(Q(commentTaker=user))
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
                   'numberOfEventsApproved': numberOfEventsApproved,
                   'comments': comments
                   })

def profile_page_others(request, id):
    profile = get_object_or_404(Profile, pk=id)
    user = profile.user
    services = Service.objects.all()
    events = Event.objects.all()
    comments = Comment.objects.filter(Q(commentTaker=user))

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
                   'numberOfEventsApproved': numberOfEventsApproved,
                   'comments': comments
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
    event_list = Event.objects.order_by('-id')
    if searchText:
        event_list =  event_list.filter(Q(name__icontains=searchText) |
                                            Q(description__icontains=searchText))
    return render(request, 'ServicEventPool/event_list.html',
                  {'event_list': event_list})

def profileSearch(request):
    profile_list = Profile.objects.all()
    searchText = request.GET.get('profileSearch')
    if searchText:
        profile_list = profile_list.filter(Q(user__first_name__icontains=searchText) |
                                           Q(user__username__icontains=searchText) |
                                           Q(user__last_name__icontains=searchText))
    return render(request, 'ServicEventPool/profile_search_result.html',
                  {'profile_list': profile_list})

def notifications(request):
    notificationList = Notification.objects.order_by('-id')
    notificationList = notificationList.filter(user=request.user)
    user = request.user
    return render(request, 'ServicEventPool/notifications.html',
                  {'notificationList': notificationList,
                   'user': user
                   })

def newsFeed(request):
    activityList = Activity.objects.order_by('-id')
    activityList = activityList.filter(user=request.user)
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
            newActivity = Activity.objects.create(user=user, event=obj, types_activities=2, activity_datetime=time)
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
            newActivity = Activity.objects.create(user=user, service=obj, types_activities=1, activity_datetime=time)
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
        status = User_Event_Status.objects.create(user_eventStatus=user, event_eventStatus=event, user_event_status=4)
        context = {
            'event': event,
            'user': user,
            'status': status
        }
        return render(request, 'ServicEventPool/event_details.html', context)
    else:
        return render(request, 'ServicEventPool/event_details.html',
                      {'event': event})


def service_details(request, slug):
    service = get_object_or_404(Service, slug=slug)
    user = request.user
    status = User_Service_Status.objects.create(user_serviceStatus=user, service_serviceStatus=service, user_service_status=4)
    return render(request, 'ServicEventPool/service_details.html',
                  {'service': service,
                   'user': user,
                   'status': status
                   })

def request_service(request, slug):
    service = get_object_or_404(Service, slug=slug)
    user = request.user
    time = datetime.datetime.now()
    if (user.profile.timeCredit-user.profile.blockedCredit)>=service.duration_credit:
        service.applicants.add(user)
        currentBlockedCredit = user.profile.blockedCredit
        user.profile.blockedCredit = currentBlockedCredit + service.duration_credit
        user.profile.save()
        newUserStatus = User_Service_Status.objects.get(user_serviceStatus=user, service_serviceStatus=service)
        newUserStatus.user_service_status = 1
        newUserStatus.save()
        newNotification = Notification.objects.create(user=user, service=service, types_notifications= 1,
                                                      notification_datetime=time, other_user=service.service_provider)
        newNotification.save()
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
    newUserStatus = User_Service_Status.objects.get(user_serviceStatus=user, service_serviceStatus=service)
    newUserStatus.user_service_status = 4
    newUserStatus.save()
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
    time = datetime.datetime.now()
    newActivity = Activity.objects.create(user=applicant, other_user=request.user, service=service, types_activities=3,
                                          activity_datetime=time)
    newActivity.save()
    status = User_Service_Status.objects.get(user_serviceStatus=applicant, service_serviceStatus=service)
    status.user_service_status = 2
    status.save()
    newNotification = Notification.objects.create(user=applicant, service=service,
                                                  notification_datetime=time, types_notifications=3)
    newNotification.save()
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
    status = User_Service_Status.objects.get(user_serviceStatus=attendee, service_serviceStatus=service)
    status.user_service_status = 1
    status.save()
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
    status = User_Service_Status.objects.get(user_serviceStatus=applicant, service_serviceStatus=service)
    status.user_service_status = 5
    status.save()
    time = datetime.datetime.now()
    newNotification = Notification.objects.create(user=applicant, service=service, notification_datetime=time,
                                                  types_notifications=6)
    newNotification.save()
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
    status = User_Service_Status.objects.get(user_serviceStatus=applicant, service_serviceStatus=service)
    status.user_service_status = 1
    status.save()
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
                obj = form.save(commit=False)
                obj.commenter = user
                obj.commentTaker = service.service_provider
                obj.service = service
                obj.save()
                user.profile.timeCredit = currentServiceTakerCredit - service.duration_credit
                service.service_provider.profile.timeCredit = currentServiceProviderCredit + service.duration_credit
                user.profile.blockedCredit = currentServiceTakerBlockedCredit - service.duration_credit
                user.profile.save()
                service.service_provider.profile.save()
                status = User_Service_Status.objects.get(user_serviceStatus=user, service_serviceStatus=service)
                status.user_service_status = 3
                status.save()
                time = datetime.datetime.now()
                newNotification = Notification.objects.create(user=user, service=service, notification_datetime=time,
                                                              types_notifications=5, other_user=service.service_provider)
                newNotification.save()
                # messages.success("Transaction is completed!")
                return HttpResponseRedirect('/service_details/' + slug)
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
    newUserStatus = User_Event_Status.objects.get(user_eventStatus=user, event_eventStatus=event)
    newUserStatus.user_event_status = 1
    newUserStatus.save()
    time = datetime.datetime.now()
    newNotification = Notification.objects.create(user=user, event=event, notification_datetime=time,
                                                  types_notifications=2, other_user=event.event_provider)
    newNotification.save()
    context = {
        'event': event
    }
    messages.success(request, "You send your application successfully!")
    return render(request, 'ServicEventPool/event_details.html', context)


def attend_back_event(request, slug):
    event = get_object_or_404(Event, slug=slug)
    user = request.user
    event.applicants.remove(user)
    newUserStatus = User_Event_Status.objects.get(user_eventStatus=user, event_eventStatus=event)
    newUserStatus.user_event_status = 4
    newUserStatus.save()
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
    time = datetime.datetime.now()
    newActivity = Activity.objects.create(user=applicant, other_user=request.user, event=event, types_activities=4,
                                          activity_datetime=time)
    newActivity.save()
    status = User_Event_Status.objects.get(user_eventStatus=applicant, event_eventStatus=event)
    status.user_event_status = 2
    status.save()
    newNotification = Notification.objects.create(user=applicant, event=event, notification_datetime=time,
                                                  types_notifications=4)
    newNotification.save()
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
    status = User_Event_Status.objects.get(user_eventStatus=attendee, event_eventStatus=event)
    status.user_event_status = 1
    status.save()
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
    status = User_Event_Status.objects.get(user_eventStatus=applicant, event_eventStatus=event)
    status.user_event_status = 5
    status.save()
    time = datetime.datetime.now()
    newNotification = Notification.objects.create(user=applicant, event=event, notification_datetime=time,
                                                  types_notifications=7)
    newNotification.save()
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
    status = User_Event_Status.objects.get(user_eventStatus=applicant, event_eventStatus=event)
    status.user_event_status = 1
    status.save()
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
