"""
@file: RIPdaemon.py
@author: Logan Beard, Matt Bellworthy
@description: The main script for the RIP daemon
"""

from configParser import *


def get_config_values():
    """Use the modules in configParser to retrieve initialisation values from .cfg file,
    returns value dict if it is read OK"""
    cfg_name = get_config_name()
    cfg_values = parse_config_file(cfg_name)
    missing_params = check_missing_parameters(cfg_values)
    if missing_params:
        print_missing_parameters(missing_params)
    else:
        if check_config_values(cfg_values):
            return cfg_values


def main():
    init_values = get_config_values()



main()
