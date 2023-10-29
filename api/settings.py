import os

BERRIES_PER_PAGE_LIMIT = os.environ.get('BERRIES_PER_PAGE_LIMIT', 20)
REQUEST_TIMEOUT = os.environ.get('REQUEST_TIMEOUT', 10)

REDIS_CACHE_ENABLED = os.environ.get('REDIS_CACHE_ENABLED', 'False') == 'True'
REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
