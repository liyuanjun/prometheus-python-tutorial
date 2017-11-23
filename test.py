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

"""
tom@ThinkPad:~$ curl localhost:5000/metrics

# HELP go_gc_duration_seconds A summary of the GC invocation durations.
# TYPE go_gc_duration_seconds summary
go_gc_duration_seconds{quantile="0"} 2.5483e-05
go_gc_duration_seconds{quantile="0.25"} 3.4437e-05
go_gc_duration_seconds{quantile="0.5"} 4.0085e-05
go_gc_duration_seconds{quantile="0.75"} 5.2158e-05
go_gc_duration_seconds{quantile="1"} 0.012065288
go_gc_duration_seconds_sum 0.022820333
go_gc_duration_seconds_count 171
"""


@app.route('/metrics', methods=['GET', 'POST'])
def metrics():
    return u"""
# HELP go_gc_duration_seconds A summary of the GC invocation durations.
# TYPE go_gc_duration_seconds summary
go_gc_duration_seconds{quantile="0"} 2.5483e-05
go_gc_duration_seconds{quantile="0.25"} 3.4437e-05
go_gc_duration_seconds{quantile="0.5"} 4.0085e-05
go_gc_duration_seconds{quantile="0.75"} 5.2158e-05
go_gc_duration_seconds{quantile="1"} 0.012065288
go_gc_duration_seconds_sum 0.022820333
go_gc_duration_seconds_count 171
"""


if __name__ == '__main__':
    app.run()
