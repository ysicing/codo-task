#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contact : 191715030@qq.com
Author  : shenshuo
Date    : 2018/12/24
Desc    : 生产表结构
"""

from models.scheduler import Base as Abase
from models.task_other import Base as TBase
from models.git_model import Base as GBase
from models.publish_model import Base as PBase
from websdk.consts import const
from settings import settings as app_settings
# ORM创建表结构
from sqlalchemy import create_engine

default_configs = app_settings[const.DB_CONFIG_ITEM][const.DEFAULT_DB_KEY]
engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (
    default_configs.get(const.DBUSER_KEY),
    default_configs.get(const.DBPWD_KEY),
    default_configs.get(const.DBHOST_KEY),
    default_configs.get(const.DBPORT_KEY),
    default_configs.get(const.DBNAME_KEY),
), encoding='utf-8', echo=True)


def create():
    Abase.metadata.create_all(engine)
    TBase.metadata.create_all(engine)
    GBase.metadata.create_all(engine)
    PBase.metadata.create_all(engine)
    print('[Success] Table structure created!')


def drop():
    Abase.metadata.drop_all(engine)
    TBase.metadata.drop_all(engine)
    GBase.metadata.drop_all(engine)
    PBase.metadata.drop_all(engine)


if __name__ == '__main__':
    create()
