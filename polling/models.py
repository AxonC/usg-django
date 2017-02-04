from __future__ import unicode_literals
import datetime
from django.db import models
from localflavor.us.us_states import STATE_CHOICES
from seatportal.models import SenateSeat
from djrichtextfield.models import RichTextField

class PollingData(models.Model):
    seat = models.ForeignKey(SenateSeat)
    avg_dem = models.DecimalField("democrat Polling Average", max_digits=3, decimal_places=1)
    avg_gop = models.DecimalField("republican Polling Average", max_digits=3, decimal_places=1)
    avg_ind = models.DecimalField("independent Polling Average (Can be NULL)", max_digits=3, decimal_places=1, null=True)
    series = models.IntegerField("polling Series Number (Round of polling e.g. First series is 1)", default=0)
    def _get_margin(self):
        if self.avg_dem > self.avg_gop:
            return '%s %s' % ('D +', (self.avg_dem - self.avg_gop))
        elif self.avg_gop > self.avg_dem:
            return '%s %s' % ('R +', (self.avg_gop - self.avg_dem))
        else:
            return "TCTC"
    pmargin = property(_get_margin)
    class Meta:
        verbose_name_plural = "Polling Data"
        get_latest_by = "series"
    def __str__(self):
        return "%s" % (self.seat)
    def _get_state(self):
        return "%s %s" % (self.seat.state, self.seat.sclass)
    state_pol = property(_get_state)
    def _get_seat_id(self):
        return "%d" % (self.seat.id)
    state_id = property(_get_seat_id)
    date = models.DateField("Date of Polling", default=datetime.datetime.today)
    incumbent = models.CharField("Surname of Incumbent", max_length=40, null=True)


class ContentNews(models.Model):
    content = models.TextField("news for Front Page Display")
    topbar = RichTextField()
    date = models.DateField("date of Publication", auto_now=True)
    
class WinningChanges(models.Model):
    data = models.ForeignKey(PollingData)
    chance_gop = models.DecimalField("GOP Chance of Winning", max_digits=3, decimal_places=1)
    chance_dnc = models.DecimalField("DNC Chance of Winning", max_digits=3, decimal_places=1)
    chance_ind = models.DecimalField("IND Chance of Winning", max_digits=3, decimal_places=1, null=True)
    class Meta:
        verbose_name_plural = "Chances of Winning"
    def _get_dem_chances(self):
        return "%d" % (self.chance_dnc)
    dem = property(_get_dem_chances)
    def _get_gop_chances(self):
        return "%d" % (self.chance_gop)
    gop = property(_get_gop_chances)
    
class OverallChances(models.Model):
    chance_gop = models.DecimalField("Overall GOP Chance of Winning", max_digits=3, decimal_places=1)
    chance_dnc = models.DecimalField("Overall DNC Chance of Winning", max_digits=3, decimal_places=1)
    class Meta:
        verbose_name_plural = "Chances of Winning Senate Majority"
        