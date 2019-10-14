#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
from config import API_ROOT
from helpers import url_join


class TestHelpers:
    def test_url_join(self):
        assert url_join(API_ROOT,
                        "/public-api/user/login") == "https://api-staging.labstep.com/public-api/user/login"
