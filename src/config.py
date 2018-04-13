from collections import namedtuple
from os import environ

Config = namedtuple('Config', 'proxy root port')

config = Config(
    root=environ.get('ARTIFACTS_PATH'),
    port=int(environ.get('PORT', 5000)),
    proxy=environ.get('PROXY_PATH', '')
)
