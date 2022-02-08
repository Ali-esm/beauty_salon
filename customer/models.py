from django.db import models
from core.models import BaseModel


# Create your models here.
class Customer(BaseModel):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)

    def __str__(self):
        return f'{self.username}'