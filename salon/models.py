import datetime
from datetime import timedelta

from django.db import models
from core.models import BaseModel


class Service(BaseModel):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    duration = models.DurationField(default=timedelta(minutes=60))
    start_time = models.TimeField()
    end_time = models.TimeField()

    @property
    def times_list(self):
        times = [str(self.start_time)]
        new_time = self.start_time
        while new_time < self.end_time:
            new_time = timedelta(hours=new_time.hour, minutes=new_time.minute)
            new_time += self.duration
            times.append(str(new_time))
            new_time = datetime.datetime.strptime(str(new_time), '%H:%M:%S').time()
        return times

    @property
    def child_price(self):
        return self.price * 0.5

    def __str__(self):
        return f'{self.name}'


class Agent(BaseModel):
    name = models.CharField(max_length=60)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    experience_year = models.PositiveSmallIntegerField(null=True, blank=True)
    services_count = models.PositiveIntegerField(default=0)
    biography = models.TextField(null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name}'
