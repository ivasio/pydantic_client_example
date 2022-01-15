from typing import List

from ..entities.order_info import OrderInfo


class OrderInfoRepository:
    def __init__(self):
        self._store = []

    def get_all(self) -> List[OrderInfo]:
        return self._store

    def add(self, item: OrderInfo) -> None:
        self._store.append(item)
