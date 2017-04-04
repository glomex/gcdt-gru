# -*- coding: utf-8 -*-
"""Simple example to demonstrate how to configure routes for AWS Lambda
"""
from gcdt_gru import Gru

app = Gru(app_name='math')


@app.route('/add/{x}/{y}')
def add(x, y):
    x = int(x)
    y = int(y)
    if x == 4 and y == 4:
        # easter egg
        return {'result': 'happy easter to all of you!'}
    return {'result': str(x + y)}
