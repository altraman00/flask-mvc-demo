#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/8/11 18:41
# @Author: xk
# @File  : forms.py

# coding:utf8
from contextlib import ContextDecorator

from flask import session
from flask_restful.representations import json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

from app import db
from app.modules import Admin


class AdminService(object):
    """查询admin用户"""

    def queryAdmin(self, id):
        # 数据库链接方式一，使用db.session
        admin = db.session.query(Admin).filter_by(id=id).first()

        # 数据库连接方式二，使用model对象Admin直接进行查询操作
        # adminCount = Admin.query.filter_by(id=id).all()
        if admin is None:
            resStr = "暂时没有admin用户"
            # return resStr
            print(resStr)

        # 创建新的admin对象
        try:
            admin = self.create_admin()

            print(type(admin))
            print("创建新用户", admin.name)
            # # 先插入数据，然后等所有逻辑操作做完之后，再db.session.commit()，事务才会起效
            # a = 1 / 0

            # 提交事务
            db.session.commit()

        except BaseException:
            print("创建异常，事务回滚")
            db.session.rollback()
            return '创建异常，事务已经回滚'
        return admin.name

    # 插入数据
    def create_admin(self):
        from werkzeug.security import generate_password_hash
        admin = Admin(
            name="mtianyan14",
            pwd=generate_password_hash("123456"),
            is_super=0,
            role_id=2
        )
        db.session.add(admin)
        return admin
