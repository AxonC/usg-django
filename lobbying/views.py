from django.shortcuts import render
from django.db.models import Sum

from lobbying.models import Donation, Organisation

def Index(request):
    donations = Donation.objects.all()
    title = 'Master List'
    amount = Donation.objects.all().aggregate(Sum('amount')).values()[0]
    return render(request, 'lobbying/index.html', {
        'donations': donations,
        'title': title,
        'amount': amount,
    })

def search(request, id):
    donations_filtered = Donation.objects.filter(organisation=id)
    title = Organisation.objects.filter(id=id).only("organisation").get()
    amount = Donation.objects.filter(organisation=id).aggregate(Sum('amount')).values()[0]
    return render(request, 'lobbying/index.html', {
        'donations': donations_filtered,
        'title': title,
        'amount': amount,
    })