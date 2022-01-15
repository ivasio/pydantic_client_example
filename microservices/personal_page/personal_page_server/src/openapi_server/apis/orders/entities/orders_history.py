from typing import List

from pydantic import BaseModel

from .order_info import OrderInfo


class OrdersHistory(BaseModel):
    orders: List[OrderInfo]
    favourite_pet_category: str
    total_spent: float
