from __future__ import unicode_literals
import moneyed, datetime
from django.db import models
from djmoney.models.fields import MoneyField

class Organisation(models.Model):
    organisation = models.CharField("name of Organisation", max_length=55)
    CLASSIFICATION = (
        ('CON', 'Conservative'),
        ('PRO', 'Progressive'),
        ('NON', 'Non-Partisan'),)
    classification = models.CharField("type of Organisation", max_length=25, choices=CLASSIFICATION)
    
    def __str__(self):
        return self.organisation;
    
class Donation(models.Model):
    PARTIES = (
    ('R', 'Republican'),
    ('D', 'Democratic'),
    ('C-IND', 'Independent (CON)'),
    ('P-IND', 'Independent (PROG)'),
    )
    recipient = models.CharField("donation recipient", max_length=75)
    party = models.CharField("party of Recipiant", choices=PARTIES, max_length=20)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    amount = MoneyField("amount Donated", max_digits=7, decimal_places=0, default_currency='USD')
    notes = models.TextField("donation notes")
    deposited_status = models.BooleanField("has the donation been deposited?",default=False)
    donation_date = models.DateField(default=datetime.datetime.today)
    username = models.CharField(max_length=50, default='User')
    
    def __str__(self):
        return '%s %s' % (self.organisation, self.recipient)
    def __int__(self):
        return '%s' % (self.amount)
