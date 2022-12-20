from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Event(models.Model):
    """Event model.

    Attributes:
        >title (str): Event title.
        >place (str): Location of the event.
        >description (set): Event description.

    """
    objects = ['title', 'point', 'place', 'description']

    title = models.CharField(
        max_length=100,
        verbose_name=_('Title')
    )

    point = models.CharField(
        max_length=250,
        verbose_name=_('Point'),
    )

    place = models.CharField(
        max_length=250,
        verbose_name=_('Place'),
    )

    description = models.TextField(
        verbose_name=_('Description'),
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.id}'
