""" #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
from .fixtures import fixtures


class TestJupyterSchedule:

    @pytest.fixture
    def user(self):
        return fixtures.defaultUser()

    @pytest.fixture
    def jupyter_notebook(self):
        return fixtures.jupyterNotebook()

    @pytest.fixture
    def entity(self):
        return fixtures.jupyterSchedule()

    def setup_method(self):
        fixtures.loadFixtures('Python')

    def test_delete(self, jupyter_notebook):
        jupyterSchedule = jupyter_notebook.newJupyterSchedule('weekly')
        jupyterSchedule.delete()
        get_jupyterSchedules = jupyter_notebook.getJupyterSchedules()
        assert get_jupyterSchedules == []

    def test_get(self, jupyter_notebook):
        jupyterSchedule = jupyter_notebook.newJupyterSchedule('weekly')
        get_jupyterSchedule = jupyter_notebook.getJupyterSchedule(
            jupyterSchedule.guid)
        try:
            assert jupyterSchedule.guid == get_jupyterSchedule.guid
        finally:
            get_jupyterSchedule.delete()

    def test_edit(self, jupyter_notebook):
        jupyterSchedule_hourly_edit = jupyter_notebook.newJupyterSchedule(
            'weekly')
        jupyterSchedule_daily_edit = jupyter_notebook.newJupyterSchedule(
            'weekly')
        jupyterSchedule_hourly_edit.edit(frequency='hourly')
        jupyterSchedule_daily_edit.edit(frequency='daily')
        try:
            assert (jupyterSchedule_hourly_edit['cron_expression'], jupyterSchedule_daily_edit['cron_expression']) == (
                '0 * * * ? *', '0 0 * * ? *')
        finally:
            jupyterSchedule_hourly_edit.delete()
            jupyterSchedule_daily_edit.delete()
 """
