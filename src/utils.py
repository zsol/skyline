from redis import StrictRedis

import settings

def redis_conn():
    if settings.REDIS_HOST_PORT is not None:
        (host, port) = settings.REDIS_HOST_PORT
        return StrictRedis(host=host, port=port)
    else:
        return StrictRedis(unix_socket_path=settings.REDIS_SOCKET_PATH)
