#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
from .fixtures import fixtures



class TestNotificationAlert:
    @pytest.fixture
    def user(self):
        return fixtures.defaultUser()

    def setup_method(self):
        fixtures.loadFixtures('Python\\\\Notification')

    def test_get_notifications(self, user):
        get_notifications = user.getNotifications()
        get_notification = user.getNotification(id=get_notifications[0]['guid'])
        
        assert get_notifications[0]['guid'] == get_notification.guid
