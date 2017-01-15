from __future__ import unicode_literals

from django.db import models
from localflavor.us.us_states import STATE_CHOICES

class Seat(models.Model):
    SEAT_CLASS = (
    (1, 'Class I'),
    (2, 'Class II'),
    (3, 'Class III'),
    )
    sclass = models.IntegerField(choices=SEAT_CLASS)
    state = models.CharField(choices=STATE_CHOICES, max_length=2)
    PARTIES = (
    ('R', 'Republican'),
    ('D', 'Democratic'),
    ('C-IND', 'Independent (CON)'),
    ('P-IND', 'Independent (PROG)'),
    )
    party = models.CharField(choices=PARTIES, max_length=25)
    holder = models.CharField("username of Present Holder", max_length=25)
    character = models.CharField("character Name of Present Holder", max_length=55)
    demographic_p = models.DecimalField("progressive Demographic", decimal_places=1, max_digits=3)
    demographic_m = models.DecimalField("moderate Demographic", decimal_places=1, max_digits=3)
    demographic_c = models.DecimalField("conservative Demographic", decimal_places=1, max_digits=3)
    seat_id = models.CharField("identificiation of Seat (format: STATECODE CLASS", max_length=6, unique=True, default="", null=True)
    def set_seat_id(self):
        self.seat_id = self.state + self.sclass
        return self.seat_id
    def __str__(self):
        return '%s %s' % (self.seat_id, self.party)

class PollingData(models.Model):
    seat = models.ForeignKey(Seat, to_field='seat_id')
    avg_dem = models.DecimalField("democrat Polling Average", max_digits=3, decimal_places=1)
    avg_gop = models.DecimalField("republican Polling Average", max_digits=3, decimal_places=1)
    avg_ind = models.DecimalField("independent Polling Average (Can be NULL)", max_digits=3, decimal_places=1, null=True)
    def margin(self):
        if self.avg_dem > self.avg_gop:
            return '%s,  %s' % ('D +', (self.avg_dem - self.avg_gop))
        elif self.avg_gop > self.avg_dem:
            return '%s,  %s' % ('R +', (self.avg_gop - self.avg_dem))
        else:
            return "TCTC"

