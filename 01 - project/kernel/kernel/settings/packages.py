# ############## #
# custom project #
# ############## #
from .base import INSTALLED_APPS

INSTALLED_APPS.append('blog')
INSTALLED_APPS.append('panel')
INSTALLED_APPS.append('mysite')
INSTALLED_APPS.append('jinjafilters')
INSTALLED_APPS.append('accounts')
INSTALLED_APPS.append('shop')
INSTALLED_APPS.append('cart')
INSTALLED_APPS.append('sportboard')
AUTH_USER_MODEL = 'accounts.User'

# INSTALLED_APPS.append('widget_tweaks')


# ############## #
#    extensions  #
# ############## #

# Django-Widget-Tweaks
# INSTALLED_APPS.append('widget_tweaks')


#######
# install virtualenv
# activate virtualenv
# requirements
# decouple settings
# modular settings
#######