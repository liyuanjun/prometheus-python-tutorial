#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-11-22 下午4:22
# @Author         : Tom.Lee
# @File           : export_http.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : https://github.com/prometheus/client_python#http

import random
import time

from prometheus_client import start_http_server, Summary

# Create a metric to track time spent and requests made.
# >>>
# # HELP request_processing_seconds Time spent processing request
# # TYPE request_processing_seconds summary
# request_processing_seconds_count 22.0
# request_processing_seconds_sum 10.612673997879028
REQUEST_TIME = Summary('request_processing_seconds',
                       'Time spent processing request')


# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)


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
    # Start up the server to expose the metrics.
    start_http_server(8000)
    print 'Started HTTP server on [::]:8000'
    # Generate some requests.
    while True:
        process_request(random.random())
