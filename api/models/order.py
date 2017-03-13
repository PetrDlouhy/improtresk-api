"""Order model."""
from datetime import datetime

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

import gopay

from .base import Base
from .participant import Participant


def generate_symvar():
    """Generate variable symbol for a new order."""
    today = datetime.now().strftime('%y%m%d%H%M')
    total = Order.objects.count()
    return "%s%s" % (today, total)


class Order(Base):
    """Stores orders types."""

    participant = models.ForeignKey(Participant, related_name="orders")
    symvar = models.CharField(
        verbose_name=_("Variable symbol"),
        max_length=63,
        blank=True,
    )
    price = models.PositiveIntegerField(
        verbose_name=_("Definitive price"),
        null=True,
    )
    paid = models.BooleanField(
        default=False,
        verbose_name=_("Is paid?"),
    )
    over_paid = models.BooleanField(default=False)
    canceled = models.BooleanField(
        verbose_name=_("Is canceled?"),
        default=False,
    )

    def save(self, *args, **kwargs):
        """Generate variable symbol if not available yet."""
        super().save(*args, **kwargs)

        if not self.symvar:
            self.symvar = generate_symvar()
            self.save()

    def __str__(self):
        """Return name as string representation."""
        return "%s at %s" % (self.participant.name, self.created_at)

    def confirm(self, payment_id):
        self.reservation.extend_reservation()
        self.reservation.save()
        payments = gopay.payments({
            'goid': settings.GOPAY_ID,
            'clientId': settings.GOPAY_CLIENT_ID,
            'clientSecret': settings.GOPAY_CLIENT_SECRET,
            'isProductionMode': settings.GOPAY_PRODUCTION_MODE,
        })
        payment_status = payments.get_status(payment_id)
        from .payment import Payment
        payment, _ = Payment.objects.get_or_create(
            ident=payment_status.id,
            defaults={
                'amount': payment_status.amount,
                'symvar': payment_status.order_number,
                'currency': payment_status.currency,
                'bank': payment_status.payment_instrument,
            },
        )
