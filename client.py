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
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

# Configure wallet and requests library
wallet = Wallet()
requests = BitTransferRequests(wallet)

server_url = 'http://[::]:9876/'

def get_data():

    ip_addr = input()
    sel_url = server_url+'get?ip={0}'
    response = requests.get(url=sel_url.format(ip_addr))
    print(response)

if __name__ == '__main__':
    get_data()
