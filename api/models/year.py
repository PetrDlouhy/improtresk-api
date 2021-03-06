"""Year model."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .base import Base


class Year(Base):
    """Stores years."""

    year = models.SlugField(
        verbose_name=_("Year"),
        unique=True,
    )
    topic = models.TextField(
        verbose_name=_("Topic of this year"),
        null=False,
        blank=True,
    )
    start_date = models.DateField(
        verbose_name=_("Date of festival start"),
    )
    end_date = models.DateField(
        verbose_name=_("Date of festival end"),
    )
    start_date_of_signups = models.DateField(
        verbose_name=_("Date when signups are starting"),
    )
    current = models.BooleanField(
        verbose_name=_("Is this year current?"),
    )

