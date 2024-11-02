from app_lifecode.schema.schema import  OrderCreate
from app_lifecode.utils.repository import AbstractRepository


class OrderService:
    def __init__(self, order_repo: AbstractRepository):
        self.order_repo = order_repo()


    async def add_order(self, order: OrderCreate):
        user_dict = order.model_dump()
        product_id = await self.order_repo.add_one(user_dict)
        return product_id


    async def update_order(self, id: int, new_data: dict):
        result = await self.order_repo.update_info(id, new_data)
        return result


    async def delete_order(self, id):
        result = await self.order_repo.delete_item(id)
        return result