import random
import json
from aiohttp import web
from user_service import logger
from user_service.db.client import User
from user_service.api.utils import ResponseTemplate, UUIDEncoder
from user_service.api.utils import to_dict


async def create_user(request: web.Request):
    db = request.app['db']
    payload = await request.json()
    payload['hold'] = random.randint(100, 1000)
    async with db.pool.acquire() as connection:
        user_conn = User(connection)
        user = await user_conn.create_user(**payload)
    logger.debug(f'payload : {payload} \n user_data : {user}')
    return web.json_response(ResponseTemplate(request=request, result='OK', addition={**user}).to_dict())


async def add(request: web.Request):
    db = request.app['db']
    payload = await request.json()
    async with db.pool.acquire() as connection:
        user_conn = User(connection)
        user = await user_conn.get_user(**payload)
        if user is None:
            return web.json_response(ResponseTemplate(request=request,
                                                      result='Fail',
                                                      description='uuid not found or incorrect').to_dict(), status=404)
        user = await user_conn.balance_replenishment(**payload)
    logger.debug(f'payload : {payload} \n user_data : {user}')
    return web.json_response(ResponseTemplate(request=request,
                                              result='OK',
                                              addition=user).to_dict())


async def subtract(request: web.Request):
    db = request.app['db']
    payload = await request.json()
    async with db.pool.acquire() as connection:
        user_conn = User(connection)
        user = await user_conn.get_user(**payload)
        if user is None:
            return web.json_response(ResponseTemplate(request=request,
                                                      result='Fail',
                                                      description='uuid not found or incorrect').to_dict(), status=404)
        result = await user_conn.balance_substraction(**payload)
        if result is None:
            return web.json_response(ResponseTemplate(request=request,
                                                      result='Fail',
                                                      description='insufficient funds').to_dict(), status=400)
    logger.debug(f'payload : {payload} \n user_data : {result}')
    return web.json_response(ResponseTemplate(request=request, result='OK', addition=result).to_dict())


async def get_user(request: web.Request):
    db = request.app['db']
    payload = await request.json()
    async with db.pool.acquire() as connection:
        user_conn = User(connection)
        user = to_dict(await user_conn.get_user(**payload))
        if user is None:
            return web.json_response(ResponseTemplate(request=request,
                                                      result='Fail',
                                                      description='uuid not found or incorrect').to_dict(), status=404)
    logger.debug(f'payload : {payload} \n user_data : {user}')
    return web.json_response(json.dumps(user, cls=UUIDEncoder))
