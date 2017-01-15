from django.contrib import admin
from .models import PollingData, Seat

class SeatAdmin(admin.ModelAdmin):
    list_display = ('state', 'sclass', 'party', 'seat_id')
    ordering = ('state',)
    
class PollingDataAdmin(admin.ModelAdmin):
    list_display = ('seat', 'avg_dem', 'avg_gop', 'avg_ind')
    ordering = ('seat',)
    
admin.site.register(PollingData, PollingDataAdmin)
admin.site.register(Seat, SeatAdmin)
    
