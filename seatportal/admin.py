from django.contrib import admin
from .models import SenateSeat, StateDemographics

class SenateSeatAdmin(admin.ModelAdmin):
    list_display = ('state', 'sclass', 'party', 'user', 'vacant')
    ordering = ('state', 'sclass')
    
class DemographicsAdmin(admin.ModelAdmin):
    list_display = ('state', 'demographic_p', 'demographic_m', 'demographic_c')
    ordering = ['state']

admin.site.register(SenateSeat, SenateSeatAdmin)
admin.site.register(StateDemographics, DemographicsAdmin)
# Register your models here.
