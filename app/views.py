# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 23:24
# @Author  : WUsuowei
# @File    : views.py
# @Software: PyCharm
from flask import render_template
from app import app
from .forms import LoginFrom
from flask import flash,redirect

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template('admin.html')

