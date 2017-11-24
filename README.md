# Prometheus tutorials for Python

* dependency package

        pip install prometheus_client
        pip install requests

---
## export metrics
> 暴露监控指标的多种方式

* [prometheus client http_server](./exporting/export_http.py)
* [flask](test.py)
* [wsgi](./exporting/export_wsgi.py)

## push data to pushgateway
> 推送你的监控指标到网关

* [use requests](./pushgateway/push_metrics.py)
