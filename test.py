#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-11-23 下午1:25
# @Author         : Tom.Lee
# @File           : test.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 


from prometheus_client import Counter

c = Counter('my_requests_total', 'HTTP Failures', ['method', 'endpoint'])
c.labels('get', '/').inc()
c.labels('post', '/submit').inc()
