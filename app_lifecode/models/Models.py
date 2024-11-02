from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, MetaData

from app_lifecode.db.db import Base

metadata=MetaData()


class UserOrm(Base):
    __tablename__='user'
    metadata=metadata

    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    age: Mapped[int]

    order: Mapped[list['OrderOrm']] = relationship("OrderOrm", back_populates='user')

    def to_read_model(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "order": self.order
        }

class OrderOrm(Base):
    __tablename__='order'
    metadata = metadata

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]=mapped_column(ForeignKey("user.id",ondelete='CASCADE'))
    product_id:Mapped[int]=mapped_column(ForeignKey("product.id",ondelete='CASCADE'))
    status: Mapped[str]

    user: Mapped['UserOrm']= relationship("UserOrm",back_populates='order')
    product: Mapped[list['ProductOrm']] = relationship("ProductOrm", back_populates='order')


class ProductOrm(Base):
    __tablename__='product'
    metadata = metadata

    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    price:Mapped[int]

    order:Mapped['OrderOrm']=relationship("OrderOrm", back_populates='product')











# class Product_OrderOrm(Base):
#     __tablename__='product_order'
#     id: Mapped[int] = mapped_column(primary_key=True)
#     order_id:  Mapped[int]=mapped_column(ForeignKey("orders.id",ondelete='CASCADE'))
#     Product_id: Mapped[int]=mapped_column(ForeignKey("product.id",ondelete='CASCADE'))
#     count:Mapped[int]
#
#     order: Mapped["OrderOrm"] = relationship("OrderOrm", back_populates="product_order")
#     product: Mapped["ProductOrm"] = relationship("ProductOrm", back_populates="product_order")