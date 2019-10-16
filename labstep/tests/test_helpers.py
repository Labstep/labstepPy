#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylama:ignore=E402

import sys
sys.path.append('./labstep/')
from config import API_ROOT
from helpers import (url_join, handleError, getTime, 
                     createdAtFrom, createdAtTo, handleStatus)

testDate = '2020-01-01'


class TestHelpers:
    def test_url_join(self):
        assert url_join(API_ROOT, '/public-api/user/login') == \
            'https://api.labstep.com/public-api/user/login', \
            'FAILED TO JOIN URL'

    def test_getTime(self):
        assert len(getTime()) != 0, \
            'FAILED TO GET TIME'

    def test_createdAtFrom(self):
        timezone = getTime()[-6:]
        assert createdAtFrom(testDate) == \
            testDate + 'T00:00:00{tz}'.format(tz=timezone), \
            'FAILED TO CREATE TIME FROM'

    def test_createdAtTo(self):
        timezone = getTime()[-6:]
        assert createdAtTo(testDate) == \
            testDate + 'T00:00:00{tz}'.format(tz=timezone), \
            'FAILED TO CREATE TIME TO'

    def test_handleStatus(self):
        assert handleStatus('AVaiLaBle') == 'available', \
            'FAILED TO HANDLE STATUS'
