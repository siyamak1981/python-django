from django.template import loader
from django.conf import settings
import os

BASE_DIR = settings.BASE_DIR
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def get_html_message(type_mail):
    file_name = BASE_DIR + '/media/templates/mail/'
    if type_mail == 'welcome':
        file_name += 'welcome.html'
    elif type_mail == 'news':
        file_name += 'good-news.html'
    else:
        raise ValueError("type_mail is empty.")
    return loader.render_to_string(file_name)