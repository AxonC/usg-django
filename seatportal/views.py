from django.shortcuts import render
from django.db.models import Count

from seatportal.models import SenateSeat, StateDemographics

def index(request):
    seats = SenateSeat.objects.all
    demographics = StateDemographics.objects.all()
    count = True
    count_gop = SenateSeat.objects.filter(party="R").count()
    count_dem = SenateSeat.objects.filter(party="D").count()
    count_ind = SenateSeat.objects.filter(party="C-IND").count() + SenateSeat.objects.filter(party="P-IND").count()
    return render(request, 'seatportal/index.html', {
        's': seats,
        'demos': demographics,
        'cgop': count_gop,
        'cdem': count_dem,
        'cind': count_ind,
        'count': count,
    })
def vacant(request):
    seats = SenateSeat.objects.filter(vacant=1)
    demographics = StateDemographics.objects.all()
    count = False
    return render(request, 'seatportal/index.html', {
        's': seats,
        'demos': demographics,
        'count': count,
    })
def republican(request):
    seats = SenateSeat.objects.filter(party="R")
    demographics = StateDemographics.objects.all()
    count = False
    return render(request, 'seatportal/index.html', {
        's': seats,
        'demos': demographics,
        'count': count,
    })
def democrat(request):
    seats = SenateSeat.objects.filter(party="D")
    demographics = StateDemographics.objects.all()
    count = False
    return render(request, 'seatportal/index.html', {
        's': seats,
        'demos': demographics,
        'count': count,
    })

# Create your views here.
