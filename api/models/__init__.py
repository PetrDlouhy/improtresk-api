"""Import all models."""

from .accomodation import Accomodation
from .accomodationPhoto import AccomodationPhoto
from .food import Food
from .foodPhoto import FoodPhoto
from .lector import Lector
from .lectorPhoto import LectorPhoto
from .order import Order
from .orderToWorkshop import OrderToWorkshop
from .payment import Payment
from .signup import Signup
from .workshop import Workshop
from .workshopPhoto import WorkshopPhoto

__all__ = (
    Accomodation,
    AccomodationPhoto,
    Food,
    FoodPhoto,
    Lector,
    LectorPhoto,
    Order,
    OrderToWorkshop,
    Payment,
    Signup,
    Workshop,
    WorkshopPhoto,
)
