#! /usr/bin/env python3
# Loading developer libraries
import requests
import json

from flask import request


class FetchData(object):

    def __init__(self):
        return None

    def income_by_ip(self, api_key):
        """
        Input: API Key and IP address request.
        Output: JSOP-encoded output of geo-location and
                average income of IP address.
        """
        ip = request.args.get('ip')
        url = "https://income.p.mashape.com/api/income/"
        headers = {"X-Mashape-Key": api_key,
                   "Accept": "application/json"}
        response = requests.get(url + ip, headers=headers)
        params = {
            'ip_address': response.json()
        }
        return json.dumps(params, indent=2)
