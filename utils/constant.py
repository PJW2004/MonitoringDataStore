# etc
import os
ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
BASE_PATH = f"{ROOT_PATH}/{os.getenv('BASE_PATH', 'Temp')}"

# log
import logging

# domain
GRAFANA_DOMAIN = os.getenv("GRAFANA_DOMAIN", "")
GRAFANA_DOMAIN = f"http://{GRAFANA_DOMAIN}" if "http" not in GRAFANA_DOMAIN else GRAFANA_DOMAIN
ELASTIC_DOMAIN = os.getenv("ELASTIC_DOMAIN", "")
ELASTIC_DOMAIN = f"http://{ELASTIC_DOMAIN}" if "http" not in ELASTIC_DOMAIN else ELASTIC_DOMAIN

# api key
GRAFANA_API_KEY = os.getenv("GRAFANA_API_KEY", "")
ELASTIC_API_KEY = os.getenv("ELASTIC_API_KEY", "")

# authorization header key
GRAFANA_AUTH_HEADER_KEY = "Bearer"
ELASTIC_AUTH_HEADER_KEY = "ApiKey"

# authorization header
GRAFANA_AUTH_HEADER = f"{GRAFANA_AUTH_HEADER_KEY} {GRAFANA_API_KEY}"
ELASTIC_AUTH_HEADER = f"{ELASTIC_AUTH_HEADER_KEY} {ELASTIC_API_KEY}"

logging.debug("your secret data")
logging.debug("----------------")
logging.debug("grafana")
logging.debug(f" - domain : {GRAFANA_DOMAIN}")
logging.debug(f" - api-key : {GRAFANA_AUTH_HEADER}")
logging.debug("----------------")
logging.debug("elastic")
logging.debug(f" - domain : {ELASTIC_DOMAIN}")
logging.debug(f" - api-key : {ELASTIC_AUTH_HEADER}")
logging.debug("----------------")