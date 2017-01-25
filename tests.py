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
# Adding in unittests to test Pinpoint microservice.
import os
import unittest
import incomeServer
import json

from unittest import mock

class PinpointTestCase(unittest.TestCase):

    # Getting app to test url
    def get(self, url):
        self.app = incomeServer.app.test_client()
        return self.app.get(url)

    # Testing whether 402 endpoint is called by the client
    def test_success(self):
        response = self.get('/get?ip=' + 'localhost')
        return self.assertEqual(response.status_code, 402)

    # Testing whether 200 endpoint is returned after payment received by 402
    @mock.patch('two1.bitserv.flask.decorator.Payment.contains_payment',
                return_value=True)
    def test_buy_success(self, *args):
         response = self.get('/get?ip=' + 'localhost')
         return self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
