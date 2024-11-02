"""СХЕМЫ ДЛЯ PYDANTIC VALIDATION"""
from pydantic import BaseModel
"""
схема юзера
"""
class UserCreate(BaseModel):
    name: str
    age:int

class UserRead(UserCreate):
    id:int

'''
Orders schema
'''
class OrderCreate(BaseModel):
    status:str
    user_id:int
    product_id:int

class OrderRead(OrderCreate):
    id:int

'''Product Schema'''
class ProductCreate(BaseModel):
    name: str
    price:int



class ProductRead(ProductCreate):
    id:int


'''
Relationships
'''

class UserRel(UserRead):
    orders:list['OrderRead']

class OrderRel(OrderRead):
    user:'UserRead'
    product:list['ProductRead']

class ProductRel(ProductRead):
    order:'OrderRead'

