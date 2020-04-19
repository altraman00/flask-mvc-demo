#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/8/11 18:39
# @Author: xk
# @File  : __init__.py.py

# coding:utf8

from flask import Flask

app = Flask(__name__)

app.debug = True

# 引入home和admin的蓝图模块
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

# 注册蓝图
app.register_blueprint(home_blueprint)

# 访问地址需要加上/admin_pre前缀
# 如：http://127.0.0.1:5000/admin_pre/admin
app.register_blueprint(admin_blueprint, url_prefix="/admin_pre")
