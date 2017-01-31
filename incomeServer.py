#! /usr/bin/env python3
import json
import os

from flask import Flask, request
from two1.wallet import Wallet
from two1.bitserv.flask import Payment

import fetch_data as get_object


# Configure the app and wallet
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

# Load the key
key = os.environ.get('KEY')


# Call the "FetchData" object and charge 1000 satoshi per request
@app.route('/get')
@payment.required(1000)
def get_endpoint():
    """
    Input: IP address
    Output: JSON with geo-location and average income
            details of the IP address.
    """
    ip = request.args.get('ip')
    response = get_object.FetchData().income_by_ip(key)
    return response


if __name__ == '__main__':
    app.run('::', port=9876)
