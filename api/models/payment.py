"""Payment model."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .order import Order
from .base import Base


class Payment(Base):
    """Stores payments."""

    ident = models.CharField(
        max_length=255,
        blank=True,
        unique=True,
        verbose_name=_("Identificator"),
        help_text=_("Payment identificator, usually generated by the bank"),
    )
    symvar = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Variable symbol"),
        help_text=_("Variable symbol of the transaction"),
    )
    symcon = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Constant symbol"),
        help_text=_("Constant symbol of the transaction"),
    )
    symspc = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Specific symbol"),
        help_text=_("Specific symbol of the transaction"),
    )
    amount = models.CharField(
        max_length=255,
        verbose_name=_("Amount received"),
        help_text=_("Amount of money received in this payment in CZK"),
    )
    sender = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Sender"),
        help_text=_("Account number of person sending this payment"),
    )
    bank = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Bank"),
        help_text=_("Bank sending this payment"),
    )
    currency = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Currency"),
        help_text=_("Currency of the payment"),
    )
    received = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_("Date Time received"),
        help_text=_("When was the payment received by our bank"),
    )
    message = models.TextField(
        max_length=255,
        blank=True,
        verbose_name=_("Message"),
    )
    order = models.ForeignKey(
        Order,
        blank=True,
        null=True,
        verbose_name=_("Order"),
        help_text=_("Which order is this payment related to?")
    )
