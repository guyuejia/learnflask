# -*- coding: utf-8 -*-
'''
@File    :   errors.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/5/26 13:24   gujiayue      1.0         错误处理
'''

from flask import render_template
from app import app,db

@app.errorhandler(404)
def not_find_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500