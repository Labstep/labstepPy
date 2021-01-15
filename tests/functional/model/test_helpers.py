#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>
# pylama:ignore=E402

# from labstep.helpers import (
#     url_join,
#     getTime,
#     createdAtFrom,
#     createdAtTo,
#     handleDate,
#     handleString
# )


# class TestHelpers:
#     def test_url_join(self):
#         assert url_join('https://api-staging.labstep.com/',
#                         '/public-api/user/login') == \
#             'https://api-staging.labstep.com/public-api/user/login', \
#             'FAILED TO JOIN URL'

#     def test_getTime(self):
#         assert len(getTime()) != 0, \
#             'FAILED TO GET TIME'

#     def test_createdAtFrom(self):
#         timezone = getTime()[-6:]
#         assert createdAtFrom('2020-01-01') == \
#             '2020-01-01' + 'T00:00:00' + timezone, \
#             'FAILED TO CREATE TIME FROM'

#     def test_createdAtTo(self):
#         timezone = getTime()[-6:]
#         assert createdAtTo('2020-01-01') == \
#             '2020-01-01' + 'T23:59:59' + timezone, \
#             'FAILED TO CREATE TIME TO'

#     def test_handleDate(self):
#         timezone = getTime()[-6:]
#         assert handleDate('2020-01-01 09:30') == \
#             '2020-01-01T09:30:00' + timezone, \
#             'FAILED TO HANDLE DATE'

#     def test_handleString(self):
#         assert handleString('orDEr RequeST') == 'order_request', \
#             'FAILED TO HANDLE STATUS'
