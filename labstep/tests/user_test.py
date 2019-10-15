#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS


testUser = LS.login('demo@labstep.com', 'demopassword')


class TestUser:
    def test_newExperiment(self):
        new_exp = testUser.newExperiment(name='api test newexp',
                                         description='api test description')

        assert new_exp['name'] == 'api test newexp', \
            'INCORRECT NEW EXPERIMENT NAME!'
        assert new_exp['description'] == 'api test description', \
            'INCORRECT NEW EXPERIMENT NAME!'

    def test_getExperiment(self):
        get_exp = testUser.getExperiment(23451)

        assert get_exp['name'] == 'api test newexp', \
            'INCORRECT EXPERIMENT NAME!'
        assert get_exp['description'] == 'api test description', \
            'INCORRECT EXPERIMENT DESCRIPTION!'
