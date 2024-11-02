from typing import Annotated

from fastapi import APIRouter, Depends

from app_lifecode.api.dependencies import user_service
from app_lifecode.schema.schema import UserCreate
from app_lifecode.service.user import UserService

user_router =APIRouter(prefix='/users',tags=['users'])

@user_router.get("")
async def users_read(service: Annotated[UserService,Depends(user_service)]):
    users = await service.get_users()
    return {'users':users}


@user_router.get("/{id}")
async def users_read_one(id:int,service: Annotated[UserService,Depends(user_service)]):
    user = await service.get_user_info(id)
    return {'user':user}


@user_router.post("")
async def users_create(
        user_data:UserCreate,
        service: Annotated[UserService,Depends(user_service)]):
    user_id = await service.add_user(user_data)
    return {'user_id':user_id}

@user_router.put("/{id}")
async def users_update(service: Annotated[UserService,Depends(user_service)]):
    users = await service.get_users()
    return {'users':users}


@user_router.delete("/{id}")
async def users_delete(id:int,service: Annotated[UserService,Depends(user_service)]):
    res = await service.delete_user(id)
    return res
