# -*- coding: utf-8 -*-
"""Simple example to demonstrate how to configure a schedule_event for AWS Lambda
"""
from __future__ import unicode_literals, print_function
from gcdt_gru import Gru

app = Gru(app_name='ticktack')


@app.schedule('cron(0/5 9-17 ? * * *)', description='run every 5 min from 9-17')
def tick_tack():
    print('tick')
