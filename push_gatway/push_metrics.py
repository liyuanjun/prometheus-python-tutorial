#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-11-23 下午2:31
# @Author         : Tom.Lee
# @File           : push_metrics.py
# @Product        : PyCharm
# @Docs           : 推送数据到pushgatway
# @Source         : 


import requests

if __name__ == '__main__':
    # job = push_job
    # instance = 192.168.12.16:9100
    # label >> cpu = ? , mode = ?

    push_url = 'http://172.16.4.31:9091/metrics/job/push_job/instance/192.168.12.16:9100'
    headers = {
        'Content-Type': 'multipart/form-data'
    }
    push_data = """
    # HELP node_cpu Seconds the cpus spent in each mode.
    # TYPE node_cpu counter
    node_cpu{cpu="cpu0",mode="guest"} 0
    node_cpu{cpu="cpu0",mode="guest_nice"} 0
    node_cpu{cpu="cpu0",mode="idle"} 249452.96
    node_cpu{cpu="cpu0",mode="iowait"} 1252.02
    node_cpu{cpu="cpu0",mode="irq"} 0.08
    node_cpu{cpu="cpu0",mode="nice"} 11.26
    node_cpu{cpu="cpu0",mode="softirq"} 16.24
    node_cpu{cpu="cpu0",mode="steal"} 0
    node_cpu{cpu="cpu0",mode="system"} 7079.8
    node_cpu{cpu="cpu0",mode="user"} 16345.95
    node_cpu{cpu="cpu1",mode="guest"} 0
    node_cpu{cpu="cpu1",mode="guest_nice"} 0
    node_cpu{cpu="cpu1",mode="idle"} 251042.11
    node_cpu{cpu="cpu1",mode="iowait"} 2073.73
    node_cpu{cpu="cpu1",mode="irq"} 0
    node_cpu{cpu="cpu1",mode="nice"} 38.42
    node_cpu{cpu="cpu1",mode="softirq"} 6.38
    node_cpu{cpu="cpu1",mode="steal"} 0
    node_cpu{cpu="cpu1",mode="system"} 6781.58
    node_cpu{cpu="cpu1",mode="user"} 14713.58
    node_cpu{cpu="cpu2",mode="guest"} 0
    node_cpu{cpu="cpu2",mode="guest_nice"} 0
    node_cpu{cpu="cpu2",mode="idle"} 249300.31
    node_cpu{cpu="cpu2",mode="iowait"} 984.1
    node_cpu{cpu="cpu2",mode="irq"} 0.1
    node_cpu{cpu="cpu2",mode="nice"} 21.83
    node_cpu{cpu="cpu2",mode="softirq"} 45.57
    node_cpu{cpu="cpu2",mode="steal"} 0
    node_cpu{cpu="cpu2",mode="system"} 7149.66
    node_cpu{cpu="cpu2",mode="user"} 16554.14
    node_cpu{cpu="cpu3",mode="guest"} 0
    node_cpu{cpu="cpu3",mode="guest_nice"} 0
    node_cpu{cpu="cpu3",mode="idle"} 252398.21
    node_cpu{cpu="cpu3",mode="iowait"} 1107.12
    node_cpu{cpu="cpu3",mode="irq"} 0
    node_cpu{cpu="cpu3",mode="nice"} 28.55
    node_cpu{cpu="cpu3",mode="softirq"} 4.63
    node_cpu{cpu="cpu3",mode="steal"} 0
    node_cpu{cpu="cpu3",mode="system"} 6548.69
    node_cpu{cpu="cpu3",mode="user"} 14585.93
    """
    response = requests.post(push_url, data=push_data, headers=headers)
    result = 'push success!!!' if response.status_code == 202 else 'push error: ' + response.content
    print result
