#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/8/11 18:46
# @Author: xk
# @File  : modules.py


# 数据处理的模型文件
import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@127.0.0.1:3305/python_flask"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)


# 会员
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    passwd = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(120), unique=True)
    info = db.Column(db.String(120), unique=True)
    face = db.Column(db.String(120), unique=True) #头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow) #注册时间
    userlogs = db.relationship('Userlog', backref='user')  # 会员日志外间关系字段

    def __repr__(self):
        return "<User %r>" % self.name


# 会员登陆日志
class Userlog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True) #编号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #所属会员
    ip = db.Column(db.String(120))
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow) #登陆时间

    def __repr__(self):
        return "<>userlog %r" % self.id

#标签
class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(120))
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  #添加时间
    movie = db.relationship('Movie',backref='tag')


    def __repr__(self):
        return "<tag %r>" % self.name


class Movie(db.Movie):
    __tanlename__ = "movie"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255),unique = True)
    url = db.Column(db.String(255),unique = True)
    info = db.Column(db.Text,unique = True)
    logo = db.Column(db.String(255),unique = True)
    star = db.Column(db.SmallInteger,unique = True)
    playnum = db.Column(db.BigInteger,unique = True)
    commentnum = db.Column(db.BigInteger,unique = True)
    tag_id = db.Column(db.Integer,db.ForeignKey('tag.id'))

    area = db.Column(db.String(255))
    release_time = db.Column(db.Date)
    length = db.Column(db.String(255))
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间