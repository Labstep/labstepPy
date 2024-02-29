#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
from .fixtures import fixtures
from .fixtures import fixtures


class TestNotificationAlert:
    @pytest.fixture
    def user(self):
        return fixtures.defaultUser()

    def setup_method(self):
        fixtures.loadFixtures('Python')

    def test_get_notifications(self, user):
        import labstep.generic.entity.repository as entityRepository
        from labstep.constants import UNSPECIFIED
        from labstep.service.helpers import handleString
        from labstep.entities.comment.model import Comment
        import time

        user.update()
        workspace = user.getWorkspace(user.activeWorkspace)

        threadId = workspace.thread["id"]

        user_name = user['name']
        user_id = user.id

        params = {
            "body": handleString(f'@[{user_name}]({user_id})'),
            "parent_thread_id": threadId,
        }

        comment = entityRepository.newEntity(user, Comment, params)
        time.sleep(10)
        get_notifications = user.getNotifications()
        get_notification = user.getNotification(
            guid=get_notifications[0]['guid'])
        assert get_notifications[0]['guid'] == get_notification.guid
