# -*- coding: utf-8 -*-
from .base import *  # NOQA

DEBUG = True

DATABASES = {
    'default':{
        'ENGLINE':'django.db.backends.sqlite3',
        'NAME':os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
