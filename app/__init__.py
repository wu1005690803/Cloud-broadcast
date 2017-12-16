# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 23:20
# @Author  : WUsuowei
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Flask
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
from app import views