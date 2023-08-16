import logging

import asyncio
from tornado.web import Application

from rinha_api.urls import APIS_URL

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


async def main():
    app = Application([APIS_URL])
    app.listen(8888)
    logger.info('Listen on 8888 port')
    await asyncio.Event().wait()


if __name__ == '__main__':
    asyncio.run(main())