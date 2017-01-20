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
