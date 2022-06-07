import os.path

import yaml


def get_pro_path():
    cp = os.path.relpath(__file__)
    cd = os.path.dirname(cp)
    cd = os.path.dirname(cd)
    return cd


def read_yaml(file_name):
    path = os.path.join(get_pro_path(), "data_case", file_name)
    with open(path, encoding="UTF-8") as f:
        return yaml.load(f.read(), yaml.FullLoader)
