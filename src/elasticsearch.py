# log
import logging

# utils
from utils import constant as cons
from utils import utils


def get_dataview():
    logging.debug("elasticsearch : data-views")
    url = f"{cons.ELASTIC_DOMAIN}/api/data_views"
    try:
        res = utils.get(url)
    except Exception as e:
        logging.error(str(e))
        return 0
    return res

def get_dataview_detail(uid: str):
    logging.debug("elasticsearch : data-views-detail")
    url = f"{cons.ELASTIC_DOMAIN}/api/data_views/data_view/{uid}"
    try:
        res = utils.get(url)
    except Exception as e:
        logging.error(str(e))
        return 0
    return res

def get_dashboard():
    logging.debug("elasticsearch : dashboard")
    url = f"{cons.ELASTIC_DOMAIN}/api/saved_objects/_export"
    data = {
        "type": "dashboard",
        "includeReferencesDeep": True
    }
    try:
        res = utils.post(url, data)
    except Exception as e:
        logging.error(str(e))
        return 0
    return res

# {DOMAIN}/api/saved_objects/_import?overwrite=true
def put_dashboard(): ...