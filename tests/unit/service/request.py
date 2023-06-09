#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from unittest import mock

class TestRequestService:
    def testGet(self):
        m = mock.Mock()
        assert isinstance(m.foo, mock.Mock)
        assert isinstance(m.bar, mock.Mock)
        assert isinstance(m(), mock.Mock)
        assert m.foo is not m.bar is not m()
