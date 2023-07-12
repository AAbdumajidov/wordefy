from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'number', 'email', 'message']
    date_hierarchy = 'created_date'
    search_fields = ['name', 'email', 'number']


admin.site.register(Contact, ContactAdmin)
