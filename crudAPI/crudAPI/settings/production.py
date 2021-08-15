from crudAPI.settings.common import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
var_secret = os.getenv('SECRET_KEY')

if var_secret is not None:
  SECRET_KEY = var_secret
else:
  SECRET_KEY = 'cvboa##uy87rrd#v9-dntvy&_wyul7f!k%c#(k^82!09$-24up'

ALLOWED_HOSTS = ['0.0.0.0', 'localhost']
