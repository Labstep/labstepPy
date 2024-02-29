#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
# pylama:ignore=E501
import pytest
from .fixtures import fixtures
from .shared import sharedTests


class TestDeviceBooking:

    @pytest.fixture
    def entity(self):
        return fixtures.device_booking()

    def test_edit(self, entity):
        from labstep.service.helpers import handleDate
        test_date_string = handleDate('2026-12-01 00:00')
        entity.edit(ended_at='2026-12-01 00:00')
        assert entity['ended_at'] == test_date_string

    def test_delete(self, entity):
        assert sharedTests.delete(entity)
