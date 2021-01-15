#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Thomas Bullier <thomas@labstep.com>
# TODO Implement routing name
# Example: url = url_join(API_ROOT, "api/generic/share-link/email")

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from labstep.service.helpers import handleError

DEFAULT_TIMEOUT = 60  # seconds


class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)


http = requests.Session()

retry_strategy = Retry(
    total=3,
    status_forcelist=[501, 502, 503, 504],
    raise_on_status=False
)
# Mount it for both http and https usage
adapter = TimeoutHTTPAdapter(timeout=60, max_retries=retry_strategy)
http.hooks["response"] = [handleError]
http.mount("https://", adapter)
http.mount("http://", adapter)


class RequestService:
    def get(self, url, headers, params=None):
        response = http.get(url, headers=headers, params=params)
        return response

    def post(self, url, headers, json=None, files=None, data=None):
        response = http.post(
            url, headers=headers, json=json, files=files, data=data
        )
        return response

    def put(self, url, headers, json=None):
        response = http.put(url, headers=headers, json=json)
        return response

    def delete(self, url, headers, json=None):
        response = http.delete(url, headers=headers, json=json)
        return response


requestService = RequestService()
