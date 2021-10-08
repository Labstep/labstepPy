#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Thomas Bullier <thomas@labstep.com>

import json
from labstep.service.request import requestService
from labstep.service.config import configService
from labstep.service.helpers import (
    url_join,
    getHeaders,
)


def ping():
    """
    Ping the API.

    """
    headers = getHeaders()

    url = url_join(configService.getHost(), 'ping')
    response = requestService.get(url, headers=headers)

    return json.loads(response.content)

