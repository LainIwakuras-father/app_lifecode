from typing import Annotated

from fastapi import APIRouter, Depends

from app_lifecode.api.dependencies import product_service
from app_lifecode.schema.schema import ProductCreate
from app_lifecode.service.product import ProductService

product_router =APIRouter(prefix='/product',tags=['products'])



@product_router.get("/{id}")
async def users_read(id:int,service: Annotated[ProductService,Depends(product_service)]):
    product = await service.get_product_info(id)
    return {'product buy':product}


@product_router.post("")
async def product_create(product_data:ProductCreate,service: Annotated[ProductService,Depends(product_service)]):
    product_id = await service.add_product(product_data)
    return {'product_id':product_id}

@product_router.put("/{id}")
async def product_update(id:int,new_data:dict,service: Annotated[ProductService,Depends(product_service)]):
    product_change = await service.update_product(id,new_data)
    return product_change

@product_router.delete("/{id}")
async def product_read(id:int,service: Annotated[ProductService,Depends(product_service)]):
    res = await service.delete_product(id)
    return res