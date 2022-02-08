from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone']
    list_display_links = ['username', 'email']

    def logical_delete(self, request, queryset):
        queryset.update(is_deleted=True)

    actions = ['logical_delete']


admin.site.register(Customer, CustomerAdmin)