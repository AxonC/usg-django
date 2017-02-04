from django.contrib import admin
from .models import PollingData, WinningChanges, OverallChances, ContentNews

class PollingDataAdmin(admin.ModelAdmin):
    list_display = ('seat', 'series', 'avg_dem', 'avg_gop', 'avg_ind', 'pmargin')
    ordering = ('seat',)
    
admin.site.register(PollingData, PollingDataAdmin)

class WinningChangesAdmin(admin.ModelAdmin):
    list_display = ('data', 'chance_dnc', 'chance_gop', 'chance_ind')
    
admin.site.register(WinningChanges, WinningChangesAdmin)

class OverallChancesAdmin(admin.ModelAdmin):
    list_display = ('chance_dnc', 'chance_gop')
admin.site.register(OverallChances, OverallChancesAdmin)
admin.site.register(ContentNews)
    
