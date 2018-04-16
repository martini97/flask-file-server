from collections import namedtuple
from json import loads
from os import environ, path

def jsonDeserializer(path):
    with open(path) as f:
        json = loads(f.read())
    return namedtuple('JSON', json.keys())(**json)

Config = namedtuple('Config', 'proxy root port files')

dir_path = path.dirname(path.realpath(__file__))
path = path.join(dir_path, 'files_config.json')
files = jsonDeserializer(path)

config = Config(
    root=environ.get('ARTIFACTS_PATH'),
    port=int(environ.get('PORT', 5000)),
    proxy=environ.get('PROXY_PATH', ''),
    files=files,
)
