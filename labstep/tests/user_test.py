#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS


testUser = LS.login('demo@labstep.com', 'demopassword')


# Create a new experiment
new_exp = testUser.newExperiment(name='api pytest newexp',
                                 description='api pytest description')

# Create a new protocol
new_pro = testUser.newProtocol(name='api pytest newprotocol')

# Create a new resource
new_res = testUser.newResource(name='api pytest newresource',
                               status='Available')

# Create a new workspace
new_wksp = testUser.newWorkspace(name='api pytest newworkspace')

# Create a new file
# new_file = testUser.newFile(filepath='./api_pytest_newfile.py')


class TestUser:
    # getSingle()
    def test_getExperiment(self):
        get_exp = testUser.getExperiment(new_exp['id'])

        assert get_exp['name'] == 'api pytest newexp', \
            'INCORRECT EXPERIMENT NAME!'
        assert get_exp['description'] == 'api pytest description', \
            'INCORRECT EXPERIMENT DESCRIPTION!'

    def test_getProtocol(self):
        get_pro = testUser.getProtocol(new_pro['id'])

        assert get_pro['name'] == 'api pytest newprotocol', \
            'INCORRECT PROTOCOL NAME!'

    def test_getResource(self):
        get_res = testUser.getResource(new_res['id'])

        assert get_res['name'] == 'api pytest newresource', \
            'INCORRECT RESOURCE NAME!'
        assert get_res['status'] == 'available', \
            'INCORRECT RESOURCE STATUS!'

    def test_getWorkspace(self):
        get_wksp = testUser.getWorkspace(new_wksp['id'])

        assert get_wksp['name'] == 'api pytest newworkspace', \
            'INCORRECT WORKSPACE NAME!'

    # newEntity()
    def test_newExperiment(self):
        assert new_exp['name'] == 'api pytest newexp', \
            'INCORRECT NEW EXPERIMENT NAME!'
        assert new_exp['description'] == 'api pytest description', \
            'INCORRECT NEW EXPERIMENT DESCRIPTION!'

    def test_newProtocol(self):
        assert new_pro['name'] == 'api pytest newprotocol', \
            'INCORRECT NEW PROTOCOL NAME!'

    def test_newResource(self):
        assert new_res['name'] == 'api pytest newresource', \
            'INCORRECT NEW RESOURCE NAME!'
        assert new_res['status'] == 'available', \
            'INCORRECT NEW RESOURCE STATUS!'

    def test_newWorkspace(self):
        assert new_wksp['name'] == 'api pytest newworkspace', \
            'INCORRECT NEW WORKSPACE NAME!'

    # def test_newFile(self):
    #     assert new_file['name'] == 'api_pytest_newfile.py', \
    #         'INCORRECT NEW FILE NAME!'
