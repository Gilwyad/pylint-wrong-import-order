from django.db import models
from django.db.models import Manager

# Create your models here.

class Area(models.Model):
    """
    Database model of an Area.
    """
    objects = Manager()

    class Meta:
        """
        Settings of this model
        """
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

    name = models.CharField(
        max_length=200,
        verbose_name="Human friendly unique name of this area.",
        unique=True,
    )

    def __str__(self) -> str:
        """
        The textual representation of this model.
        """
        return f'{self.name}'
