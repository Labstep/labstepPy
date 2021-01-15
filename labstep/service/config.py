#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

import os
from dotenv import load_dotenv

load_dotenv()
API_ROOT = os.getenv("LABSTEP_API_URL")

if API_ROOT is None:

    API_ROOT = 'https://api.labstep.com'


if API_ROOT != 'https://api.labstep.com':

    print('Connecting to Labstep API at: ',API_ROOT)