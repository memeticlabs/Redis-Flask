# -*- coding: utf-8 -*-
from redis import Redis as Redis_, ConnectionPool
from redis.connection import UnixDomainSocketConnection


class Redis(Redis_):
    """This class is used for the intergration of Redis to a Flask
    application.

    There are two usage modes which work very similar. One if binding
    the instance to a specific flask application.

        app = Flask(__name__)
        redis = Redis(app)

    The second possibility is to create the object once and configure the
    application later to support it.

        db = Redis()

        def create_app():
            app = Flask(__name__)
            redis.init_app(app)
            return app

    The second case requires a request context to be present.
    """

    def __init__(self, app=None):
        """Initializer.

        Keyword Arguments:
        app -- flask application instance.
        """

        if app is not None:
            config = self._get_config(app)
            super(Redis_, self).__init__(**config)

    def init_app(self, app):
        """This is used to initialize the application to be used with Redis.

        Keyword Arguments:
        app -- flask application instance.
        """
        
        config = self._get_config(app)
        super(Redis_, self).__init__(**config)

    def _get_config(self, app):

        # Redis related configuration from flask application config
        config = {
            'host': app.config.setdefault('REDIS_HOST', 'localhost'),
            'port': app.config.setdefault('REDIS_PORT', 6379),
            'db': app.config.setdefault('REDIS_DB', 0),
            'password': app.config.setdefault('REDIS_PASSWORD', None),
            'socket_timeout': app.config.setdefault('REDIS_SOCKET_TIMEOUT', None),
            'charset': app.config.setdefault('REDIS_CHARSET', 'utf-8'),
            'errors': app.config.setdefault('REDIS_ERRORS', 'strict'),
            'unix_socket_path': app.config.setdefault('REDIS_UNIX_SOCKET_PATH', None),
            'connection_pool': None
        }

        max_connections = app.config.setdefault('REDIS_MAX_CONNECTIONS', None)
        if max_connections:
            print 'Yeah! I am making a new connection pool.'
            kwargs = {
                'db': config['db'],
                'password': config['password'],
                'socket_timeout': config['socket_timeout'],
                'encoding': config['charset'],
                'encoding_errors': config['errors'],
            }
            # based on input, setup appropriate connection args
            if config['unix_socket_path']:
                kwargs.update({
                    'path': config['unix_socket_path'],
                    'connection_class': UnixDomainSocketConnection
                })
            else:
                kwargs.update({
                    'host': config['host'],
                    'port': config['port'],
                })
            config['connection_pool'] = ConnectionPool(**kwargs)

        return config
