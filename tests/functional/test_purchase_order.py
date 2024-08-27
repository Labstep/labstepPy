#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
# pylama:ignore=E501
import pytest

from .fixtures import fixtures
from .shared import sharedTests


class TestPurchaseOrder:
    def setup_method(self):
        fixtures.loadFixtures('Python')

    @pytest.fixture
    def entity(self):
        return fixtures.purchaseOrder()

    def test_edit(self, entity):
        entity.edit(name='Edited name', status='pending', currency='GBP')
        assert entity['name'] == 'Edited name' \
            and entity['status'] == 'pending' \
            and entity['currency'] == 'GBP'

    def test_get_order_requests(self, entity):
        order_request = fixtures.orderRequest()
        entity.addOrderRequest(order_request.id)
        get_order_requests = entity.getOrderRequests()

        assert order_request.id == get_order_requests[0]['id']

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test_commenting(self, entity):
        assert sharedTests.commenting(entity)
