# etc
import os

# utils
from utils import constant as cons

def create_dir(path):
    create_path = f"{cons.BASE_PATH}/{path}"
    os.mkdir(create_path)

def create_dirs(path):
    create_path = f"{cons.BASE_PATH}/{path}"
    if not os.path.exists(create_path):
        os.makedirs(create_path)

def create_file(path, name, extension, data):
    create_path = f"{cons.BASE_PATH}/{path}/{name}.{extension}"
    with open(create_path, "w") as f:
        f.write(data)