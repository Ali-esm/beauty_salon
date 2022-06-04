from django.db import models
from core.models import BaseModel


class Customer(BaseModel):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=14)

    def __str__(self):
        return f"{self.name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.name} {self.last_name}"
