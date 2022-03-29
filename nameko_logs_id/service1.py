import os
import sys

import loguru
from nameko.rpc import RpcProxy, rpc

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
 
 
class GreetingService:
    name = 'service_1'
    service2 = RpcProxy('service_2')
    # Dont use standalone rpc
    # with ClusterRpcProxy(CONFIG) as cluster_rpc:
    #     response = cluster_rpc.service2.hello(
    #         name
    #     )

    stack_id = GetStackID()

    @rpc
    def hello(self, name):

        with logger.contextualize(log_id=self.stack_id):
            response = self.service2.format_greeting(name)
            logger.info('Service 1 - log')
            utils.do_something_commom()

            return {'response': response}
