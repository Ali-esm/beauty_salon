from django.db import models
from core.models import BaseModel
from customer.models import Customer
from salon.models import Agent, Service


class Booking(BaseModel):
    agent = models.ForeignKey(Agent, on_delete=models.RESTRICT)
    service = models.ForeignKey(Service, on_delete=models.RESTRICT)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    total_price = models.PositiveIntegerField(null=True, blank=True)
    reserve_time = models.TimeField()
    reserve_date = models.DateField()

    def __str__(self):
        return f"{self.customer.username} reservation"


class Holiday(BaseModel):
    WEEK_DAYS = (
        (0, 'Saturday'),
        (1, 'Sunday'),
        (2, 'Monday'),
        (3, 'Tuesday'),
        (4, 'Wednesday'),
        (5, 'Thursday'),
        (6, 'Friday')
    )

    holiday = models.IntegerField(unique=True, choices=WEEK_DAYS)

    def __str__(self):
        return f"{self.WEEK_DAYS[self.holiday][1]}"