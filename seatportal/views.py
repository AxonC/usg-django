from django.shortcuts import render

from seatportal.models import SenateSeat, StateDemographics

def index(request):
    seats = SenateSeat.objects.all()
    demographics = StateDemographics.objects.all()
    return render(request, 'seatportal/index.html', {
        's': seats,
        'demos': demographics,
    })

# Create your views here.
