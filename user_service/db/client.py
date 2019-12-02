from asyncpg import DataError


class DBClient(object):
    def __init__(self, pool, logger):
        self._pool = pool
        self._logger = logger

    @property
    def pool(self):
        return self._pool

    async def subtract_balance(self):
        """
        Выполняет расчет баланса.
        """
        async with self._pool.acquire() as connection:
            async with connection.transaction():
                return await connection.fetchrow(f'UPDATE users'
                                                 f' SET current_balans = current_balans - hold, hold = 0'
                                                 f' WHERE hold > 0')


class User(object):
    def __init__(self, connection):
        self._connection = connection

    async def create_user(self, fio, hold, current_balans, status=True, **kwargs):
        return await self._connection.fetchrow(f'INSERT INTO users (fio, hold, current_balans, status)'
                                               f' VALUES($1,$2,$3,$4) RETURNING *', fio, hold, current_balans, status)

    async def get_user(self, uuid, **kwargs):
        try:
            return await self._connection.fetchrow('SELECT * FROM users WHERE uuid = $1', uuid)
        except DataError:
            return None

    async def balance_replenishment(self, uuid, added):
        try:
            return await self._connection.fetchrow('UPDATE users SET current_balans = current_balans + $1 '
                                                   'WHERE uuid = $2 RETURNING *', added, uuid)
        except DataError:
            return None

    async def balance_substraction(self, uuid, subtract):
        try:
            return await self._connection.fetchrow('UPDATE users SET hold = hold + $1 '
                                                   'WHERE uuid = $2 '
                                                   'AND current_balans - hold - $1 > 0 RETURNING *', subtract, uuid)
        except DataError:
            return None
