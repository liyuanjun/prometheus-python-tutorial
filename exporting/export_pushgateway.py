#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-11-22 下午4:44
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017 OpenBridge by yihecloud
# @File           : export_pushgateway.py
# @Product        : PyCharm
# @Docs           : push_to_gateway 把批量任务的指标接口暴露给prometheus抓取
# @Source         : https://github.com/prometheus/client_python#exporting-to-a-pushgateway


import random
import time

from prometheus_client import (
    CollectorRegistry,
    Gauge,
    push_to_gateway)


# from prometheus_client.exposition import instance_ip_grouping_key


def push_default_data():
    """
    推送一个默认没有labels的数据,接口会返回以下增加的信息

    >$ curl http://172.16.4.31:9091/metrics　
    #　
    ...
    # HELP push_time_seconds Last Unix time when this group was changed in the Pushgateway.
    # TYPE push_time_seconds gauge
    push_time_seconds{instance="",job="tom_job"} 1.5114080519317884e+09
    ...
    # HELP tom_random_metric loop push a random number to pushgatway
    # TYPE tom_random_metric gauge
    tom_random_metric{instance="",job="tom_job"} 0.8609551526448003
    """
    cr = CollectorRegistry()

    # 创建Gauge对象时，必须传入registry，否则数据不会写入
    g = Gauge(
        'tom_random_metric',
        'loop push a random number to pushgatway',
        registry=cr,
    )

    @g.time()
    def process_request_gauge(t):
        """创建一个虚拟延迟函数."""
        time.sleep(t)

    def push():
        print '....push_default_data time:', time.time()
        # 设置时间戳
        g.set_to_current_time()
        # 设置value值
        g.set(random.random())
        # 推送数据
        push_to_gateway(
            gateway='http://172.16.4.31:9091',
            job='tom_job',
            registry=cr
        )

    while True:
        process_request_gauge(random.randint(1, 5))
        push()


def push_labels_data():
    """
    推送一个自定义labels的数据,接口会返回以下增加的信息

    >$ curl http://172.16.4.31:9091/metrics　
    #　
    ...
    # HELP push_time_seconds Last Unix time when this group was changed in the Pushgateway.
    # TYPE push_time_seconds gauge
    push_time_seconds{instance="",job="label_job"} 1.5114179956714425e+09
    ...
    # HELP tom_custom_label_metric test push label metric
    # TYPE tom_custom_label_metric gauge
    tom_custom_label_metric{endpoint="/",instance="172.16.4.31:9100",job="label_job"} 8
    :return:
    """
    c = Gauge(
        'tom_custom_label_metric',
        'test push label metric',
        ['instance', 'endpoint']
    )
    registry = CollectorRegistry()
    registry.register(c)

    while True:
        time.sleep(2)
        c.labels('172.16.4.31:9100', '/').set_to_current_time()
        c.labels('172.16.4.31:9100', '/').set(random.randint(1, 99))
        push_to_gateway(gateway='http://172.16.4.31:9091',
                        job='label_job',
                        registry=registry)


if __name__ == '__main__':
    """TEST"""

    # push_labels_data()
    # push_default_data()
