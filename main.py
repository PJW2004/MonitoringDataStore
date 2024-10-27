# date
import time
date = time.strftime('%Y%m%d%H%M%S')

# parse
import json

# src
from src import filesystem
from src import elasticsearch
from src import grafana

# 모든 값은 .read().decode() 후 파일 작성을 진행해야 한다.
filesystem.create_dirs(f"{date}/elasticsearch/dataview")
filesystem.create_dirs(f"{date}/grafana/dashboard")

# elasticsearch
dataviews = elasticsearch.get_dataview().read().decode()
dict_dataviews = json.loads(dataviews)
for idx, dataview in enumerate(dict_dataviews.get("data_view", [])):
    uid = dataview.get("id")
    if not uid:
        raise Exception("not found dataview uid")
    dataview_detail = elasticsearch.get_dataview_detail(uid).read().decode()
    filesystem.create_file(f"{date}/elasticsearch/dataview", str(idx), "json", dataview_detail)

dashboard = elasticsearch.get_dashboard().read().decode()
filesystem.create_file(f"{date}/elasticsearch", "dashboard", "ndjson", dashboard)

# grafana
datasources = grafana.get_datasources().read().decode()
filesystem.create_file(f"{date}/grafana", "datasources", "json", datasources)

dashboards = grafana.get_dashboards().read().decode()
dict_dashboards = json.loads(dashboards)
for idx, dashboard in enumerate(dict_dashboards):
    uid = dashboard.get("uid")
    if not uid:
        raise Exception("not found dashboard uid")
    dashboard_detail = grafana.get_dashboard_detail(uid).read().decode()
    filesystem.create_file(f"{date}/grafana/dashboard", str(idx), "json", dashboard_detail)
