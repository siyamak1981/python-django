from .base import *
from .secure import *

DEBUG = False
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v:[s.strip() for s in v.split(',')])