

from app_lifecode.schema.schema import ProductCreate
from app_lifecode.utils.repository import AbstractRepository


class ProductService:
    def __init__(self, product_repo: AbstractRepository):
        self.product_repo = product_repo()


    async def add_product(self, product: ProductCreate):
        user_dict = product.model_dump()
        product_id = await self.product_repo.add_one(user_dict)
        return product_id


    async def update_product(self, id: int, new_data: dict):
        result = await self.product_repo.update_info(id, new_data)
        return result

    async def get_product_info(self, id: int):
        product_info = await self.product_repo.find_by_id(id)
        return product_info


    async def delete_product(self, id):
        result = await self.product_repo.delete_item(id)
        return result