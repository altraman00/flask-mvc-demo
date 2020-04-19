#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/8/11 18:41
#@Author: xk
#@File  : views.py


from . import home


@home.route("/home")
def index():
    return "this is home"