#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/8/11 18:39
# @Author: xk
# @File  : manage.py
from flask_script import Manager, Server

from app import app

from flask_bootstrap import Bootstrap
Bootstrap(app)

manage = Manager(app)
manage.add_command("runserver", Server(use_debugger=True))

if __name__ == "__main__":
    app.run()
