import asyncio
import asyncpg
import connexion
from connexion.resolver import RestyResolver
from user_service import logger, BASE_DIR
from user_service.configs import configurations
from user_service.db.client import DBClient
from user_service.task import subtract_balance


def main():
    logger.info('Starting')
    loop = asyncio.get_event_loop()
    db = DBClient(loop.run_until_complete(asyncpg.create_pool(**configurations['db'])), logger)
    logger.info('Инициализация API')
    app = connexion.AioHttpApp(__name__, specification_dir=f'{BASE_DIR}/spec/',)
    api = app.add_api('openapi.yaml',
                      validate_responses=True,
                      strict_validation=True,
                      resolver=RestyResolver('user_service.api.handlers'),
                      pass_context_arg_name='request')

    api.subapp['db'] = db
    # Раз в 10 минут считаем балансы
    loop.create_task(subtract_balance(db, 600))

    app.run(port=80)
    logger.info('Stopped')


if __name__ == '__main__':
    main()
