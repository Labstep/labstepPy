#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
from random import randrange

testUser = LS.login('apitest@labstep.com', 'apitestpass')

# Create a new entity
tag = testUser.getTags()[0]

# Set variables for editting
randomNum = randrange(1, 9)
editName = 'Api Pytest Name Edit {n}'.format(n=randomNum)


class TestTag:
    def test_edit(self):
        result = tag.edit(editName)
        assert result.name == editName, \
            'INCORRECT EDITTED TAG NAME!'

    def test_delete(self):
        result = tag.delete()
        assert result is None, \
            'FAILED TO DELETE TAG'
