#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Thomas Bullier <thomas@labstep.com>
import pytest
from fixtures import loadFixtures, authUser
from shared import sharedTests


class TestJupyterNotebook:
    @pytest.fixture
    def loggedUser(self):
        return authUser()

    def setup_method(self):
        loadFixtures('Python\\\\JupyterNotebook')

    def test_get(self, loggedUser):
        guid = 'guid-test'
        jupyterNotebook = loggedUser.getJupyterNotebook(guid)
        assert guid == jupyterNotebook.guid
        assert 'Capsule' == jupyterNotebook.name
        assert {'test': 42} == jupyterNotebook.data

    def test_edit_name(self, loggedUser):
        guid = 'guid-test'
        jupyterNotebook = loggedUser.getJupyterNotebook(guid)
        assert sharedTests.edit(jupyterNotebook)

    def test_edit_data(self, loggedUser):
        guid = 'guid-test'
        jupyterNotebook = loggedUser.getJupyterNotebook(guid)
        newData = {"test":43}
        result = jupyterNotebook.edit(data=newData)
        return result.data == newData
