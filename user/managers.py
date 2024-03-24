from django.db import models


class PersonManager(models.Manager):
    def get_queryset(self):
        """
        Returns a queryset filtering out any entries marked as not deleted.
        """
        return super().get_queryset().filter(is_deleted=False)


class DeletedPersonManager(models.Manager):
    def get_queryset(self):
        """
        Returns a queryset filtering out any entries marked as deleted.
        """
        return super().get_queryset().filter(is_deleted=True)
