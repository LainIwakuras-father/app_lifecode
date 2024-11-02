from app_lifecode.api.db_work import db_router
from app_lifecode.api.order import order_router
from app_lifecode.api.product import product_router
from app_lifecode.api.user import user_router

all_routers = [
    user_router,
    order_router,
    product_router,
    db_router
]