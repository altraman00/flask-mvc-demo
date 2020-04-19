#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/8/11 18:40
#@Author: xk
#@File  : views.py



from . import admin


@admin.route("/admin")
def index():
    return "this is admin"