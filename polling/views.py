from django.shortcuts import render
from django.db.models import Max
from polling.models import PollingData, WinningChanges, OverallChances
from seatportal.models import SenateSeat

def index(request):
    test = PollingData.objects.all()
    navigation = SenateSeat.objects.filter(swingseat=1).order_by("state")
    polling = PollingData.objects.filter(seat__swingseat=1).order_by("seat__state", "series")[:12]
    chances = OverallChances.objects.all()
    return render (request, 'polling/index.html', {
        't': test,
        'navigation': navigation,
        'polling': polling,
        'chances': chances,
    })
def seatview(request, state):
    title = PollingData.objects.filter(seat__state=state).first()
    ##seat_id = PollingData.objects.get('seat')
    polling = PollingData.objects.filter(seat__state=state)
    chances = OverallChances.objects.all()
    return render(request, 'polling/seatview.html', {
        'title': title,
        'polling': polling,
        'chances': chances,
    })
