from app_lifecode.models.Models import  ProductOrm
from app_lifecode.utils.repository import SQLAlchemyRepository


class ProductRepository(SQLAlchemyRepository):
    model = ProductOrm