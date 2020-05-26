"""Small implementation of popular python framework flask"""
import os
import importlib
import types
from werkzeug import Request, Response
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.routing import Map, Rule

__version__ = '0.0.2'

class Flasky:
    """The flasky object implements a WSGI application and acts as the
    central object. It is passed the name of the module or package of
    the application. One it is created it will act as the central
    registry for the view classes.
    """
    def __init__(self, urls):
        self.debug = False
        self.url_map = Map()
        self.bind_urls(urls)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        response = self.make_response(response, request.environ)
        return response(environ, start_response)

    def make_response(self, rv, environ):
        if isinstance(rv, Response):
            return rv
        if isinstance(rv, str):
            return Response(rv)
        if isinstance(rv, tuple):
            return Response(*rv)
        return Response.force_type(rv, environ)

    def dispatch_request(self, request):
        """Dispatches the request to the view classes loaded with
        package_name.
        """
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            if not hasattr(endpoint, request.method) or not callable(getattr(endpoint, request.method)):
                raise HTTPException('{} method is not supported on this url'.format(request.method))
            else:
                obj = endpoint()
                return getattr(obj, request.method)(**values)
        except HTTPException as e:
            return e

    def add_route(self, rule, endpoint):
        self.url_map.add(Rule(rule, endpoint=endpoint))

    def bind_urls(self, urls):
        for rule, endpoint in urls:
            self.add_route(rule, endpoint)

    def run(self, host='127.0.0.1', port=5000):
        from werkzeug.serving import run_simple
        run_simple(
            host,
            port,
            self,
            use_debugger=self.debug,
            use_reloader=self.debug
        )
