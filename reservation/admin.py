from django.contrib import admin
from .forms import BookingForm
from .models import Booking, Holiday


class BookingAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'agent', 'service', 'reserve_time', 'reserve_date']
    form = BookingForm


admin.site.register(Booking, BookingAdmin)
admin.site.register(Holiday)
