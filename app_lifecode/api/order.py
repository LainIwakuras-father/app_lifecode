from typing import Annotated

from fastapi import APIRouter, Depends

from app_lifecode.api.dependencies import order_service
from app_lifecode.schema.schema import OrderCreate
from app_lifecode.service.order import OrderService

order_router =APIRouter(prefix='/order',tags=['orders'])

@order_router.post("")
async def users_read(order:OrderCreate,service: Annotated[OrderService,Depends(order_service)]):
    order_id = await service.add_order(order)
    return {'order_id':order_id}

@order_router.put("/{id}")
async def users_read(id:int,new_data:dict,service: Annotated[OrderService,Depends(order_service)]):
    res = await service.update_order(id,new_data)
    return res


@order_router.delete("/{id}")
async def users_read(id:int,service: Annotated[OrderService,Depends(order_service)]):
    res = await service.delete_order(id)
    return res