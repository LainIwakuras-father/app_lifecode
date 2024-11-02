from app_lifecode.models.Models import UserOrm
from app_lifecode.utils.user_repository import UserSQLAlchemyRepository


class UserRepository(UserSQLAlchemyRepository):
    model = UserOrm