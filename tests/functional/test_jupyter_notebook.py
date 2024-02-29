#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
from .fixtures import fixtures
from .shared import sharedTests


class TestJupyterNotebook:
    @pytest.fixture
    def loggedUser(self):
        return fixtures.defaultUser()

    @pytest.fixture
    def entity(self):
        return fixtures.jupyterNotebook()

    def setup_method(self):
        fixtures.loadFixtures('Python\\\\JupyterNotebook')

    def test_get(self, loggedUser, entity):
        guid = entity.guid
        jupyterNotebook = loggedUser.getJupyterNotebook(guid)
        assert guid == jupyterNotebook.guid

    def test_edit_name(self, entity):
        assert sharedTests.edit(entity)

    def test_edit_data(self, entity):
        newData = {"test": 43}
        result = entity.edit(data=newData)
        assert result.data == newData
