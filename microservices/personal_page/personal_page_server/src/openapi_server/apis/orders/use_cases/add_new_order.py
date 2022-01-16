import logging
from random import randint

from common_models.models import Order

from ..entities.add_new_order_request import AddNewOrderRequest
from ..entities.order_info import OrderInfo
from ..repositories.order_info import OrderInfoRepository
from ..repositories.order import OrderRepository


class AddNewOrderUseCase:
    def __init__(self, order_infos: OrderInfoRepository, orders: OrderRepository):
        self.order_infos = order_infos
        self.orders = orders
        self.logger = logging.getLogger(__name__)

    async def __call__(self, request: AddNewOrderRequest) -> Order:
        prepared_order = self.prepare_order(request.order)
        self.logger.info(f'Adding order {prepared_order}')

        filled_order = await self.orders.add(prepared_order)
        self.order_infos.add(OrderInfo(
            order=filled_order,
            pet_category=request.pet_category,
            price=request.price,
        ))
        self.logger.info(f'Added order info {filled_order}')

        return filled_order

    def prepare_order(self, order: Order) -> Order:
        result_dict = order.dict()
        result_dict.update(
            id=randint(0, 1_000_000),
            pet_id=randint(0, 1_000_000),
            quantity=1
        )
        return Order.parse_obj(result_dict)
