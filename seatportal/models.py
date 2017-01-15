from __future__ import unicode_literals

from django.db import models
from localflavor.us.us_states import STATE_CHOICES

class SenateSeat(models.Model):
    state = models.CharField("state of Seat", choices=STATE_CHOICES, max_length=2)
    PARTIES = (
    ('R', 'Republican'),
    ('D', 'Democratic'),
    ('C-IND', 'Independent (CON)'),
    ('P-IND', 'Independent (PROG)'),
    )
    party = models.CharField("seat Affiliation", max_length=20, choices=PARTIES)
    SEAT_CLASS = (
    (1, 'Class I'),
    (2, 'Class II'),
    (3, 'Class III'),
    )
    sclass = models.IntegerField("class of Seat", choices=SEAT_CLASS)
    user = models.CharField("username of Player", max_length=30, null=True)
    vacant = models.BooleanField("Is the Seat Vacant?", default=0)
    class Meta:
        verbose_name_plural = "Seats"
    
class StateDemographics(models.Model):
    state = models.CharField("state", choices=STATE_CHOICES, max_length=2)
    demographic_p = models.DecimalField("progressive Demographic", decimal_places=1, max_digits=3)
    demographic_m = models.DecimalField("moderate Demographic", decimal_places=1, max_digits=3)
    demographic_c = models.DecimalField("conservative Demographic", decimal_places=1, max_digits=3)
    class Meta:
        verbose_name_plural = "State Demographics"
    def __str__(self):
        return self.state
    
