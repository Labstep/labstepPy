#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import os
from dotenv import load_dotenv
from labstep.constants import VERSION

load_dotenv()


class ConfigService:
    host = 'https://api.labstep.com'

    def __init__(self):

        self.userAgent = f"Python SDK {VERSION}"
        envApiUrl = os.getenv("LABSTEP_API_URL")

        if envApiUrl is not None:
            self.host = envApiUrl
            print('Connecting to Labstep API at: ', envApiUrl)

    def setHost(self, host):
        self.host = host
        print('Connecting to Labstep API at: ', host)

    def getHost(self):
        return self.host

    def setUserAgent(self, userAgent):
        self.userAgent = userAgent

    def getUserAgent(self):
        return self.userAgent


configService = ConfigService()
