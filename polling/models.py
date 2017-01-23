from __future__ import unicode_literals

from django.db import models
from localflavor.us.us_states import STATE_CHOICES
from seatportal.models import SenateSeat

class PollingData(models.Model):
    seat = models.ForeignKey(SenateSeat)
    avg_dem = models.DecimalField("democrat Polling Average", max_digits=3, decimal_places=1)
    avg_gop = models.DecimalField("republican Polling Average", max_digits=3, decimal_places=1)
    avg_ind = models.DecimalField("independent Polling Average (Can be NULL)", max_digits=3, decimal_places=1, null=True)
    series = models.IntegerField("polling Series Number (Round of polling e.g. First series is 1)", default=0)
    def _get_margin(self):
        if self.avg_dem > self.avg_gop:
            return '%s,  %s' % ('D +', (self.avg_dem - self.avg_gop))
        elif self.avg_gop > self.avg_dem:
            return '%s,  %s' % ('R +', (self.avg_gop - self.avg_dem))
        else:
            return "TCTC"
    pmargin = property(_get_margin)
    class Meta:
        verbose_name_plural = "Polling Data"