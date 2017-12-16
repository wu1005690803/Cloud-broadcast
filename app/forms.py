# -*- coding: utf-8 -*-
# @Time    : 2017/12/16 16:27
# @Author  : WUsuowei
# @File    : forms.py
# @Software: PyCharm
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators  import DataRequired

class LoginFrom(Form):
	openid = StringField('Openid',validators=[DataRequired()])
	remember_me = BooleanField('remember_me',default=False)
