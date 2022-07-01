from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def get_all(self):
        return super().get_queryset()

    def get_delete_list(self):
        return super().get_queryset().filter(is_deleted=True)

    def get_active_list(self):
        return super().get_queryset().filter(is_deleted=False, is_active=True)

    def get_deactivate_list(self):
        return super().get_queryset().filter(is_active=False)


class BaseModel(models.Model):
    create_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = BaseManager()

    class Meta:
        abstract = True

    def activate(self):
        self.is_active = True
        self.save()

    def deactivate(self):
        self.is_active = False
        self.save()

    def logical_delete(self):
        self.is_deleted = True
        self.save()
