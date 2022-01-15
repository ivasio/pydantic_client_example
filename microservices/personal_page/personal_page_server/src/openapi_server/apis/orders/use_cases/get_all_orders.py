from collections import Counter

from ..entities.orders_history import OrdersHistory
from ..repositories.order_info import OrderInfoRepository


class GetAllOrdersUseCase:
    def __init__(self, order_infos: OrderInfoRepository):
        self.order_infos = order_infos

    def __call__(self) -> OrdersHistory:
        order_infos = self.order_infos.get_all()
        order_infos_sorted = sorted(order_infos, key=lambda order_info: order_info.order.ship_date)

        categories_counter = Counter()
        for order_info in order_infos:
            categories_counter.update(order_info.pet_category for _ in range(order_info.order.quantity))
        favourite_pet_category = categories_counter.most_common(1)[0][0]

        total_spent = sum(order_info.price * order_info.order.quantity for order_info in order_infos)

        return OrdersHistory(
            orders=order_infos_sorted,
            favourite_pet_category=favourite_pet_category,
            total_spent=total_spent
        )
