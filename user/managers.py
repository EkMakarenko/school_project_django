from django.db import models


class PersonManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class DeletedPersonManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=True)
