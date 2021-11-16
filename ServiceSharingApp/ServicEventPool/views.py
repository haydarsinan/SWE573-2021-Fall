from django.shortcuts import render

# Create your views here.

def home(request):
    serviceName="Baklava with Olive Oil"
    return render(request, 'ServicEventPool/home.html', {
        "serviceName_Here": serviceName
    })

def calendar(request, year, month):
    year=year
    month=month
    return render(request, 'ServicEventPool/calendar.html', {
        "year_Here": year,
        "month_Here": month
    })