# parse
import json

# log
import logging

# api
import urllib.request

# utils
from utils import constant as cons

def get(url):
    logging.debug(f"request url : {url}")
    logging.debug("request method : get")

    req = urllib.request.Request(url)
    req.add_header("Authorization", cons.ELASTIC_AUTH_HEADER)
    res = urllib.request.urlopen(req)
    return res

def post(url, data):
    logging.debug(f"request url : {url}")
    logging.debug("request method : post")
    data_bytes = json.dumps(data).encode()

    req = urllib.request.Request(url, data=data_bytes)
    req.add_header("Authorization", cons.ELASTIC_AUTH_HEADER)
    req.add_header("Content-Type", "application/json")
    req.add_header("kbn-xsrf", "true")

    res = urllib.request.urlopen(req)
    if res.getcode() >= 400:
        raise Exception(f"status >= 400 : {res}")
    return res