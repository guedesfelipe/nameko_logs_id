import os
import sys

import loguru
from nameko.rpc import rpc

from get_stack_id import GetStackID
from utils import utils

logger = loguru.logger
logger.remove()
logger.add(
    sys.stdout,
    format=(
        '{time} | {level: <8} | {name}:{function}:{line:>4} | '
        '({extra[log_id]}) {message} '
    ),
    level=os.getenv('LOGGING_LEVEL', 'DEBUG'),
)


class FormatGreetingService:
    name = 'service_2'

    stack_id = GetStackID()

    @rpc
    def format_greeting(self, name):
        with logger.contextualize(log_id=self.stack_id):
            logger.info('Service 2 - log')
            utils.do_something_commom()
            return f'Hello, {name}!'
