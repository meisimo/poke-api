import redis

from .settings import REDIS_HOST, REDIS_PORT, REDIS_CACHE_ENABLED

class Cache(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Cache, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self._redis = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)

    def set(self, key: str, value: str, timeout: int = None):
        self._redis.set(key, value, timeout)

    def get(self, key: str):
        return self._redis.get(key)

def cache_static_endpoint(
    endpoint_key: str,
    serialize_cb: callable,
    deserialize_cb: callable,
    timeout: int = None,
):
    def _cache_endpoint(fn):
        if not REDIS_CACHE_ENABLED:
            return fn

        def _wrapper(*args, **kwargs):
            cache = Cache()

            if cached_result := cache.get(endpoint_key):
                return deserialize_cb(cached_result)

            result = fn(*args, **kwargs)
            cache.set(endpoint_key, serialize_cb(result), timeout)

            return result
        return _wrapper
    return _cache_endpoint
