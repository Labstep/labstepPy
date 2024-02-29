#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
import labstep
from .fixtures import fixtures


class TestAccessAPIKey:

    @pytest.fixture
    def new_api_key(self):
        return fixtures.api_key()

    def setup_method(self):
        fixtures.loadFixtures('Python')

    def test_edit_access_api_key(self, new_api_key):
        new_name = 'New_name'
        new_api_key.edit(name=new_name)
        assert new_api_key.name == new_name

    def test_get_api_key(self, new_api_key):
        user = new_api_key.__user__
        get_entity = user.getAPIKey(APIKey_id=new_api_key.id)
        assert get_entity.id == new_api_key.id

    def test_get_api_keys(self, new_api_key):
        user = new_api_key.__user__
        get_entities = user.getAPIKeys()
        assert get_entities[0].id == new_api_key.id

    def test_get_api_keys_by_uuid(self, new_api_key):
        user = new_api_key.__user__
        get_entities = user.getAPIKeys(api_key=new_api_key.uuid)
        assert get_entities[0].id == new_api_key.id
