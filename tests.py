
#! /usr/bin/env python3
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

    def test_buy_no_success(self, *args):
        # Ensuring 402 endpoint hits a 404.
        response = self.get('/')
        return self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
