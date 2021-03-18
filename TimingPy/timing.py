#!/usr/bin/env python

"""A base module for calling timing api"""

from builtins import range
import requests #pylint: disable=import-error

class Connection: #pylint: disable=too-few-public-methods)
    """Create connection with api key"""
    proxyDict = dict()

    def __init__(self, api_key):
        self.api_key = "Bearer " + api_key
        self.headers = { 'Authorization' : self.api_key }

    def _url(self, path): #pylint: disable=no-self-use
        """base api url"""
        return 'https://web.timingapp.com/api/v1' + path

    def _get_data(self, url, data=None):
        """GET call to Timing API"""
        has_more = True
        resp_data = []
        while has_more:
            resp = requests.get(url, params=data, headers=self.headers, proxies=self.proxyDict)
            resp_json = resp.json()
            if not resp.status_code in range(200, 207):
                break
            if 'links' in resp_json:
                has_more = resp_json['links'].get('next', None)
            else:
                has_more = None
            if has_more is None or resp_json['data'] == []:
                resp_data = resp_json['data']
                break
            resp_data = resp_data + resp_json['data']
        return resp_data

    def _patch_data(self, url, data):
        """PATCH call to Timing API"""
        resp = requests.patch(url, data, headers=self.headers, \
            proxies=self.proxyDict)
        return resp

    def _post_data(self, url, data):
        """POST call to Timing API"""
        resp = requests.post(url, data, headers=self.headers, \
            proxies=self.proxyDict)
        return resp

    def _put_data(self, url, data):
        """PUT call to Timing API"""
        resp = requests.put(url, data, headers=self.headers, \
            proxies=self.proxyDict)
        return resp

    def _delete_data(self, url):
        """DELETE call to Timing API"""
        return requests.delete(url, headers=self.headers, proxies=self.proxyDict)
