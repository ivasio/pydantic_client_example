from common_models.models import Order
from pydantic import BaseModel


class OrderInfo(BaseModel):
    order: Order
    pet_category: str
    price: float
