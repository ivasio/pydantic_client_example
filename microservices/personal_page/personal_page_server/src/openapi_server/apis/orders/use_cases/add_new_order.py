from ..entities.orders_history import OrdersHistory
from ..repositories.order_info import OrderInfoRepository


class GetAllOrdersUseCase:
    def __init__(self, order_infos: OrderInfoRepository):
        self.order_infos = order_infos

