from common_models.models import Order

from ..controllers import AddNewOrderRequest
from ..entities.order_info import OrderInfo
from ..repositories.order_info import OrderInfoRepository
from ..repositories.order import OrderRepository


class AddNewOrderUseCase:
    def __init__(self, order_infos: OrderInfoRepository, orders: OrderRepository):
        self.order_infos = order_infos
        self.orders = orders

    async def __call__(self, request: AddNewOrderRequest) -> Order:
        filled_order = await self.orders.add(request.order)
        self.order_infos.add(OrderInfo(
            order=filled_order,
            pet_category=request.pet_category,
            price=request.price,
        ))
        return filled_order
