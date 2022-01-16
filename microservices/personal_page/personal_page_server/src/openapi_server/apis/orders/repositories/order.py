from common_models.models import Order

from petstore_httpx_client.api_client import AsyncApis


class OrderRepository:
    def __init__(self, petstore_client: AsyncApis):
        self.petstore_client = petstore_client

    async def add(self, order: Order) -> Order:
        return await self.petstore_client.store_api.place_order(order)
