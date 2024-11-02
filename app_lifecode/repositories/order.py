from app_lifecode.models.Models import OrderOrm
from app_lifecode.utils.order_repository import OrderSQLAlchemyRepository


class OrderRepository(OrderSQLAlchemyRepository):
    model = OrderOrm