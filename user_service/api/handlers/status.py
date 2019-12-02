from aiohttp import web
from user_service.api.utils import ResponseTemplate


async def ping(request: web.Request):
    return web.json_response(ResponseTemplate(request=request, result="OK", description='Ping-Pong').to_dict())
