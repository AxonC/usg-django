from django.contrib import admin
from .models import SenateSeat, StateDemographics

def make_mw(modeladmin, request, queryset):
    queryset.update(region='MW')
make_mw.short_description = "Mark Selected Seats as Midwest"

def make_ne(modeladmin, request, queryset):
    queryset.update(region='NE')
make_ne.short_description = "Mark selected seats as Northeast"

def make_s(modeladmin, request, queryset):
    queryset.update(region='S')
make_s.short_description = "Mark selected seats as South"

def make_w(modeladmin, request, queryset):
    queryset.update(region='W')
make_w.short_description = "Mark selected seats as West"

def mark_election(modeladmin, request, queryset):
    queryset.update(swingseat=1)
mark_election.short_description = "Mark Seat as Up for Election"
    
class SenateSeatAdmin(admin.ModelAdmin):
    list_display = ('state', 'sclass', 'party', 'user', 'region', 'vacant', 'swingseat')
    ordering = ('state', 'sclass')
    actions = (make_mw, make_ne, make_s, make_w, mark_election)
    
class DemographicsAdmin(admin.ModelAdmin):
    list_display = ('state', 'demographic_p', 'demographic_m', 'demographic_c')
    ordering = ['state']

admin.site.register(SenateSeat, SenateSeatAdmin)
admin.site.register(StateDemographics, DemographicsAdmin)
# Register your models here.
