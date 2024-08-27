#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest

from .fixtures import fixtures
from .shared import sharedTests


class TestDevice:
    @pytest.fixture
    def entity(self):
        return fixtures.device()

    @pytest.fixture
    def category(self):
        return fixtures.deviceCategory()

    def setup_method(self):
        fixtures.loadFixtures('Python')

    def test_edit(self, entity):
        assert sharedTests.edit(entity)

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test_addDataNumber(self, entity):
        data = entity.addData('Test', 'numeric', number=13, unit='oC')
        assert data.name == 'Test' \
            and data.type == 'numeric' \
            and data.number == 13, \
            'FAILED TO CREATE DATA'

    def test_addDataFile(self, entity):
        data = entity.addData(
            'Test', 'file', filepath=__file__)
        assert data.name == 'Test' \
            and data.files is not None, \
            'FAILED TO CREATE DATA'

    def test_addDataText(self, entity):
        data = entity.addData('Test', 'text', text='Testings')
        assert data.name == 'Test' \
            and data.type == 'default' \
            and data.value == 'Testings', \
            'FAILED TO CREATE DATA'

    def test_getData(self, entity):
        first_data = entity.addData('Test', text='Words')
        data = entity.getData(search_query='Test')
        assert data[0].id == first_data.id

    def test_setDeviceCategory(self, entity, category):
        entity.setDeviceCategory(category.id)
        deviceCategoryFromGet = entity.getDeviceCategory()
        assert deviceCategoryFromGet.id == category.id

    def test_assign(self, entity):
        assert sharedTests.assign(entity)

    def test_getDeviceBooking(self, entity):
        device_booking = entity.addDeviceBooking(
            started_at='2022-12-01 00:00', ended_at='2022-12-01 10:00')
        get_device_booking = entity.getDeviceBooking(device_booking.id)
        get_device_bookings = entity.getDeviceBookings()

        assert device_booking.id == get_device_booking.id and get_device_bookings[
            0].id == device_booking.id
