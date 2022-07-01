from django.db import models
from core.models import BaseModel
from customer.models import Customer
from salon.models import Agent, Service
import uuid


class Booking(BaseModel):
    agent = models.ForeignKey(Agent, on_delete=models.RESTRICT)
    service = models.ForeignKey(Service, on_delete=models.RESTRICT)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    total_price = models.PositiveIntegerField(null=True, blank=True)
    reserve_time = models.TextField()
    reserve_date = models.DateField()
    reservation_uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    def __str__(self):
        return f"{self.customer.full_name} reservation"


class Holiday(BaseModel):
    holiday = models.DateField()

    def __str__(self):
        return f"{self.holiday}"
