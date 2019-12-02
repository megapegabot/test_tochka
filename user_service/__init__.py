import os
import logging.config
import yaml


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

with open(f'{BASE_DIR}/configs/logging.yml', 'r') as __file:
    logging.config.dictConfig(yaml.load(__file.read(), Loader=yaml.FullLoader))

logger = logging.getLogger(__name__)
