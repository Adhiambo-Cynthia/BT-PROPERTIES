from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'email', 'phone', 'listing', 'contact_date')
    list_display_links=('id', 'name')
    list_filter=('contact_date',)
    search_fields=('listing','email', 'name')
    list_per_page= 20


admin.site.register(Contact, ContactAdmin)


