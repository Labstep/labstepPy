#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv

API = os.getenv('LABSTEP_API')

if API is None:
    load_dotenv()
    API = os.getenv('LABSTEP_API')

if API == 'testing':
    API_ROOT = 'https://api-testing.labstep.com/'
    print('WARNING: You are using the testing api')
elif API == 'staging':
    API_ROOT = 'https://api-staging.labstep.com/'
    print('WARNING: You are using the staging api')
else:
    API_ROOT = 'https://api.labstep.com/'
