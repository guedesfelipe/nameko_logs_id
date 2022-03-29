from nameko.extensions import DependencyProvider
 
 
def _format_worker_ctx(worker_ctx):
    return '->'.join(worker_ctx.call_id_stack[1:])
 
 
class GetStackID(DependencyProvider):
    def get_dependency(self, worker_ctx):
        return _format_worker_ctx(worker_ctx) 
