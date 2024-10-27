# log
import logging

# utils
from utils import constant as cons
from utils import utils

def get_datasources():
    logging.debug("grafana : datasources")
    url = f"{cons.GRAFANA_DOMAIN}/api/datasources"
    try:
        res = utils.get(url)
    except Exception as e:
        logging.error(str(e))
        return 0
    return res
    
def get_dashboards():
    logging.debug("grafana : dashboards")
    url = f"{cons.GRAFANA_DOMAIN}/api/search"
    try:
        res = utils.get(url)
    except Exception as e:
        logging.error(str(e))
        return 0
    return res

def get_dashboard_detail(uid: str):
    logging.debug("grafana : dashboard_detail")
    url = f"{cons.GRAFANA_DOMAIN}/api/dashboards/uid/{uid}"
    try:
        res = utils.get(url)
    except Exception as e:
        logging.error(str(e))
        return 0
    return res    
