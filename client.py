#!/usr/bin/env python3
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

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
