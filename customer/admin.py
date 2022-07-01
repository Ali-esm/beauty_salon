from django.contrib import admin

from .forms import CustomerForm
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "last_name", "phone", "is_deleted", "is_active"]
    list_display_links = ["name", "phone"]
    form = CustomerForm

    def logical_delete(self, request, queryset):
        queryset.update(is_deleted=True)

    actions = ["logical_delete"]


admin.site.register(Customer, CustomerAdmin)
