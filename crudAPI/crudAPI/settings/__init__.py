from . import *
import os

env_name = os.getenv('ENV_NAME', 'local')

print(env_name)

if env_name == 'prod':
  from .production import *
# elif env_name == 'test':
#   from .test import *
else:
  from .local import *
