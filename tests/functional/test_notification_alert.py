#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
from .fixtures import fixtures
from .fixtures import fixtures


class TestNotificationAlert:
    @pytest.fixture
    def metadata(self):
        return fixtures.metadataDate()

    def setup_method(self):
        fixtures.loadFixtures('Python\\\\Metadata')

    def test_edit(self, metadata):

        alert = metadata.setNotificationAlert(
            message='Wrong', minutes_before=1)

        alert.edit(message='Test', minutes_before=10)

        metadata.update()

        alert = metadata.getNotificationAlert()

        assert alert.message == 'Test'
        assert alert.minutes_before == 10

    def test_set_from_none(self, metadata):

        alert = metadata.setNotificationAlert(
            message='Test', minutes_before=10)

        assert alert.message == 'Test'
        assert alert.minutes_before == 10

    def test_set_from_existing(self, metadata):

        metadata.setNotificationAlert(
            message='Wrong', minutes_before=20)

        metadata.update()

        alert = metadata.setNotificationAlert(
            message='Test', minutes_before=10)

        assert alert.message == 'Test'
        assert alert.minutes_before == 10

    def test_enable_disable(self, metadata):

        alert = metadata.setNotificationAlert(
            message='Wrong', minutes_before=20)

        alert = alert.disable()

        assert alert.deleted_at is not None

        alert = alert.enable()

        assert alert.deleted_at is None
