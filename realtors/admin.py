from django.contrib import admin
from .models import Realtors

class RealtorsAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'seller_of_month', 'email', 'phone')
    list_display_links=('id', 'name')
    list_filter=('name',)
    list_editable=('seller_of_month',)
    search_fields=('name', 'email')
    list_per_page= 20


admin.site.register(Realtors, RealtorsAdmin)
