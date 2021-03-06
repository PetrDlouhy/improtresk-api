"""Site administration module."""
from django.contrib import admin

from . import models


DEFAULT_READONLY = ['createdAt', 'updatedAt']


class BaseAdminModel(admin.ModelAdmin):
    """Base for all admin models."""

    def get_readonly_fields(self, request, obj=None):
        """Define default readonly fields."""
        return DEFAULT_READONLY


class BaseInlineAdminModel(admin.TabularInline):
    """Base for all inline admin models."""

    def get_readonly_fields(self, request, obj=None):
        """Define default readonly fields."""
        return DEFAULT_READONLY


class LectorPhotoAdmin(BaseInlineAdminModel):
    """Admin model for Lector photos."""

    model = models.LectorPhoto


@admin.register(models.Lector)
class LectorAdmin(BaseAdminModel):
    """Admin model for Lectors and their photos."""

    inlines = [
        LectorPhotoAdmin,
    ]


@admin.register(models.LectorRole)
class LectorRoleAdmin(BaseAdminModel):
    """Admin model for Lector roles."""

    prepopulated_fields = {'slug': ('name',)}


class WorkshopPhotoAdmin(BaseInlineAdminModel):
    """Admin model for Workshop photos."""

    model = models.WorkshopPhoto


@admin.register(models.WorkshopDifficulty)
class WorkshopDifficultyAdmin(BaseAdminModel):
    """Admin model for Workshop difficulties."""

    prepopulated_fields = {'slug': ('name',)}

class WorkshopLectorInlineAdmin(BaseInlineAdminModel):
    """Inline admin model for Workshop lectors."""

    model = models.WorkshopLector


class WorkshopPriceInlineAdmin(BaseInlineAdminModel):
    """Inline admin for Workshop prices."""

    model = models.WorkshopPrice


@admin.register(models.Workshop)
class WorkshopAdmin(BaseAdminModel):
    """Admin model for Workshops and their photos."""

    inlines = [
        WorkshopPhotoAdmin,
        WorkshopLectorInlineAdmin,
        WorkshopPriceInlineAdmin,
    ]


class AccomodationPhotoAdmin(BaseInlineAdminModel):
    """Admin model for Accomodation photos."""

    model = models.AccomodationPhoto


@admin.register(models.Accomodation)
class AccomodationAdmin(BaseAdminModel):
    """Admin model for Accomodation and its photos."""

    inlines = [
        AccomodationPhotoAdmin,
    ]


class FoodPhotoAdmin(BaseInlineAdminModel):
    """Admin model for Food photos."""

    model = models.FoodPhoto


@admin.register(models.Food)
class FoodAdmin(BaseAdminModel):
    """Admin model for Food and its photos."""

    inlines = [
        FoodPhotoAdmin,
    ]


@admin.register(models.Meal)
class MealAdmin(BaseAdminModel):
    """Admin model for Meal."""

    pass


@admin.register(models.MealReservation)
class MealReservationAdmin(BaseAdminModel):
    """Admin model for MealReservation."""

    pass


@admin.register(models.Payment)
class PaymentAdmin(BaseAdminModel):
    """Admin model for Food and its photos."""

    def get_readonly_fields(self, request, obj=None):
        """Define all read only fields."""
        if obj:
            return DEFAULT_READONLY + [
                'ident',
                'symvar',
                'symcon',
                'symspc',
                'amount',
                'sender',
                'bank',
                'message',
                'currency',
                'received',
                'message',
            ]
        return super(PaymentAdmin, self).get_readonly_fields(
            request,
            obj
        )


@admin.register(models.Participant)
class ParticipantAdmin(BaseAdminModel):
    """Admin model for Participants."""

    pass


@admin.register(models.Reservation)
class ReservationAdmin(BaseAdminModel):
    """Admin model for Reservations."""

    pass


@admin.register(models.Order)
class OrderAdmin(BaseAdminModel):
    """Admin model for Orders."""

    pass


class PriceLevelInlineAdmin(BaseInlineAdminModel):
    """Inline admin for Workshop prices."""

    model = models.PriceLevel


@admin.register(models.Year)
class YearAdmin(BaseAdminModel):
    """Admin model for Years."""

    inlines = [
        PriceLevelInlineAdmin,
    ]


@admin.register(models.Team)
class TeamAdmin(BaseAdminModel):
    """Admin model for Teams."""

    pass
