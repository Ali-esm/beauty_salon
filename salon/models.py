from django.db import models
from core.models import BaseModel


class Service(BaseModel):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    duration = models.DurationField()


# todo: create Agent model here
