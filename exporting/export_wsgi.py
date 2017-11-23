#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-11-22 下午4:39
# @Author         : Tom.Lee
# @File           : export_wsgi.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : https://github.com/prometheus/client_python#wsgi


from wsgiref.simple_server import make_server

from prometheus_client import make_wsgi_app

if '__main__' == __name__:
    """
    >>> $ curl localhost:8000

    # HELP process_virtual_memory_bytes Virtual memory size in bytes.
    # TYPE process_virtual_memory_bytes gauge
    process_virtual_memory_bytes 203407360.0
    # HELP process_resident_memory_bytes Resident memory size in bytes.
    # TYPE process_resident_memory_bytes gauge
    process_resident_memory_bytes 15912960.0
    # HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
    # TYPE process_start_time_seconds gauge
    process_start_time_seconds 1511339718.13
    # HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
    # TYPE process_cpu_seconds_total counter
    process_cpu_seconds_total 3.37
    # HELP process_open_fds Number of open file descriptors.
    # TYPE process_open_fds gauge
    process_open_fds 6.0
    # HELP process_max_fds Maximum number of open file descriptors.
    # TYPE process_max_fds gauge
    process_max_fds 4096.0
    # HELP python_info Python platform information
    # TYPE python_info gauge
    python_info{implementation="CPython",major="2",minor="7",patchlevel="6",version="2.7.6"} 1.0
    """

    app = make_wsgi_app()
    httpd = make_server('', 8000, app)
    print 'Started HTTP server on [::]:8000'

    httpd.serve_forever()
