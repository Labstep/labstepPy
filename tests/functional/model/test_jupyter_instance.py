#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Thomas Bullier <thomas@labstep.com>
import pytest
from fixtures import loadFixtures, authUser


class TestJupyterInstance:
    @pytest.fixture
    def loggedUser(self):
        return authUser()

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
