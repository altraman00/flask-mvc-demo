#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/8/11 18:41
# @Author: xk
# @File  : views.py

# 从当前模块导入home
from flask import render_template

from . import home


@home.route("/home")
def index():
    # return "<h1 stype='color:red'> this is home</h1>"
    return render_template("/home/login.html")
