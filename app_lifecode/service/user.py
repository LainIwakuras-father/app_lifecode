from app_lifecode.schema.schema import UserCreate
from app_lifecode.utils.repository import AbstractRepository


class UserService:
    def __init__(self, user_repo: AbstractRepository):
        self.user_repo = user_repo()

    async def add_user(self, user: UserCreate):
        user_dict = user.model_dump()
        user_id = await self.user_repo.add_one(user_dict)
        return user_id


    async def get_users(self):
        users = await self.user_repo.find_all()
        return users

    async def update_info(self, id: int, new_data: dict):
        result = await self.user_repo.update_info(id, new_data)
        return result

    async def get_user_info(self, id: int):
        order_info = await self.user_repo.find_by_id(id)
        return order_info


    async def delete_user(self, id):
        result = await self.user_repo.delete_item(id)
        return result