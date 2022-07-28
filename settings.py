# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import os
import sys
from random import choice

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

zf = r"qwertyuiopasdfghjklzxcvbnm1234567890~!@#$%^&*()_+`{}|[]\:;<>?,./"
zf = list(zf)
sk = ""
for i in range(25):
    sk = sk + choice(zf)

class BaseConfig:
    CATCHAT_MESSAGE_PER_PAGE = 30
    CATCHAT_ADMIN_EMAIL = "wry_beiyong06@outlook.com"

    SECRET_KEY = os.getenv('SECRET_KEY', sk)

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
