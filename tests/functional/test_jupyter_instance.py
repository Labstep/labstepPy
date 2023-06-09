#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
from .fixtures import loadFixtures, authUser, jupyterInstance


class TestJupyterInstance:
    @pytest.fixture
    def loggedUser(self):
        return authUser()

    @pytest.fixture
    def entity(self):
        return jupyterInstance()

    def setup_method(self):
        loadFixtures('Python\\\\JupyterInstance')

    def test_get(self, loggedUser):
        guid = 'guid-test'
        jupyterInstance = loggedUser.getJupyterInstance(guid)
        assert guid == jupyterInstance.guid
        assert jupyterInstance.started_at is None
        assert jupyterInstance.ended_at is None

    def test_start(self, loggedUser):
        guid = 'guid-test'
        jupyterInstance = loggedUser.getJupyterInstance(guid)
        assert jupyterInstance.started_at is None
        jupyterInstance.start()
        assert jupyterInstance.started_at is not None

    def test_end(self, loggedUser):
        guid = 'guid-test'
        jupyterInstance = loggedUser.getJupyterInstance(guid)
        assert jupyterInstance.ended_at is None
        jupyterInstance.end()
        assert jupyterInstance.ended_at is not None

    def test_edit_data(self, entity):
        newData = {"test": 43}
        result = entity.edit(data=newData)
        return result.data == newData
