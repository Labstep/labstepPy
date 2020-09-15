#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep

user = labstep.login('myaccount@labstep.com', 'mypassword')

protocol = user.newProtocol('My Protocol with Table')

data = {
    "rowCount": 12,
    "columnCount": 12,
    "colHeaderData": {},
    "data": {
        "dataTable": {
            0: {
                0: {
                    "value": 'Cell A1'
                },
                1: {
                    "value": 'Cell B1'
                }
            }
        }
    }
}

table = protocol.addTable(name='Test Table', data=data)

table.attributes()
