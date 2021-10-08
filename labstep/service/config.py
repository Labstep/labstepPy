#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

import os
from dotenv import load_dotenv

load_dotenv()


class ConfigService:
    host = 'https://api.labstep.com'

    def __init__(self):
        envApiUrl = os.getenv("LABSTEP_API_URL")

        if envApiUrl is not None:
            self.host = envApiUrl
            print('Connecting to Labstep API at: ', envApiUrl)

    def setHost(self, host):
        self.host = host
        print('Connecting to Labstep API at: ', host)

    def getHost(self):
        return self.host


configService = ConfigService()
