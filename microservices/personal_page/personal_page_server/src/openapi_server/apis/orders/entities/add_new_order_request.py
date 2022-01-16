from common_models.models import Order
from pydantic import BaseModel


class AddNewOrderRequest(BaseModel):
    price: float
    pet_category: str
    order: Order
