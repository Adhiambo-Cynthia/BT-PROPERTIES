from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'address', 'price', 'realtor', 'is_published', 'list_date' )
    list_display_links=('id', 'title' )
    list_filter=('realtor', 'city' )
    list_editable=('is_published',)
    search_fields=('title', 'description', 'city', 'address')
    list_per_page= 20


admin.site.register(Listing, ListingAdmin)
