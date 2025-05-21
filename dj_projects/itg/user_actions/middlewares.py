from threading import local

thread_locals = local()

def get_current_user():
    return getattr(thread_locals, 'user', None)

class ThreadLocals( object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.


        thread_locals.user = getattr(request, 'user', None)
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response