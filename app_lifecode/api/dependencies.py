from app_lifecode.repositories.order import OrderRepository
from app_lifecode.repositories.product import ProductRepository
from app_lifecode.repositories.user import UserRepository
from app_lifecode.service.order import OrderService
from app_lifecode.service.product import ProductService
from app_lifecode.service.user import UserService


def user_service():
    return UserService(UserRepository)


def order_service():
    return OrderService(OrderRepository)

def product_service():
    return ProductService(ProductRepository)

