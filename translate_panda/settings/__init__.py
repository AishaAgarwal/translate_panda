import os

ENVIRONMENT = os.environ.get("SERVICE_ENV", 'production')
cmd = f'from .settings_{ENVIRONMENT} import *'
exec(cmd)