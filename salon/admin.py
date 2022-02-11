from django.contrib import admin
from .models import Service, Agent


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_deleted', 'is_active']
    list_editable = ['price']
    list_filter = ['price']


class AgentAdmin(admin.ModelAdmin):
    list_display = ['name', 'experience_year', 'age', 'services_count']


admin.site.register(Service, ServiceAdmin)
admin.site.register(Agent, AgentAdmin)