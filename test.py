#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-11-23 下午1:25
# @Author         : Tom.Lee
# @File           : test.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello World!flask'


if __name__ == '__main__':
    app.run(debug=True)
