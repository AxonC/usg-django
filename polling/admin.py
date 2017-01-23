from django.contrib import admin
from .models import PollingData

class PollingDataAdmin(admin.ModelAdmin):
    list_display = ('seat', 'avg_dem', 'avg_gop', 'avg_ind')
    ordering = ('seat',)
    
admin.site.register(PollingData, PollingDataAdmin)
    
