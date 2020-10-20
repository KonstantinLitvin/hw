import json
import logging
import logging.config
import os
import pathlib
from pathlib import Path

# Write path to the project root instead of None if you don't want to set env variable.
project_root = Path(os.getenv('epam_hw', None))


def load_config():
    with open(pathlib.Path(project_root, 'logging.json'), 'rt') as file:
        return json.load(file)


logging.config.dictConfig(load_config())


def get_logger(name):
    return logging.getLogger(name)
