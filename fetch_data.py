"""
Copyright (c) 2016-2017 Blockshare Technologies, LLC.
  ____  _            _     ____  _                      ___ ___
 | __ )| | ___   ___| | __/ ___|| |__   __ _ _ __ ___  |_ _/ _ \
 |  _ \| |/ _ \ / __| |/ /\___ \| '_ \ / _` | '__/ _ \  | | | | |
 | |_) | | (_) | (__|   <  ___) | | | | (_| | | |  __/_ | | |_| |
 |____/|_|\___/ \___|_|\_\|____/|_| |_|\__,_|_|  \___(_)___\___/
"""

__author__ = "cponeill"
__version__ = "0.01"
__maintainer__ = "cponeill"
__email__ = "cponeill@blockshare.io"


#!/usr/bin/env python3
import requests
import json

from flask import request

class FetchData(object):

    def __init__(self):
        return None

    def income_by_ip(self, api_key):
        ip = request.args.get('ip')
        headers = {"X-Mashape-Key": api_key, "Accept": "application/json"}
        response = requests.get("https://income.p.mashape.com/api/income/" + ip, headers=headers)
        params = {
            'ip_address': response.json()
        }
        return json.dumps(params, indent=2)
