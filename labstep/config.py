#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv
load_dotenv()

API = os.getenv('LABSTEP_API')

if API == 'testing':
    API_ROOT = 'https://api-testing.labstep.com/'
elif API == 'staging':
    API_ROOT = 'https://api-staging.labstep.com/'
else:
    API_ROOT = 'https://api.labstep.com/'
