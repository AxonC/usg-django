from django.contrib import admin
from .models import Donation, Organisation


class DonationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'organisation', 'amount', 'deposited_status', 'username')
    
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('organisation', 'classification')
    
admin.site.register(Donation, DonationAdmin)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.site_header = "BETA - USG Additional Admin Tools Control Panel"