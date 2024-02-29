#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
from .fixtures import fixtures
from labstep.entities.entityImport.repository import newEntityImport, getEntityImport
from labstep.entities.device.model import Device


class TestEntityImport:
    def setup_method(self):
        fixtures.loadFixtures('Python\\\\EntityImport')

    def test_get_entity_import(self):
        user = fixtures.defaultUser()
        entityImportGuid = 'entity-import-guid'
        entityImport = getEntityImport(user, guid=entityImportGuid)
        assert entityImport['guid'] == entityImportGuid

    def test_new(self):
        user = fixtures.defaultUser()
        data = {
            "settings": {
                "modes": {
                    "device": "create_always",
                    "resource": "create_skip_existing",
                    "resource_item": "create_skip_existing",
                    "resource_location": "create_skip_existing"
                }
            },
            "items": {
                "device": [
                    {
                        "fields": {
                            "name": "Test",
                            "75fc86f7-d64f-47f4-b262-3667a4c9c964": "1 ml"
                        },
                        "metadatas": [
                            {
                                "template_guid": "ca3504d6-4a0e-422a-8bb3-176717c18a88",
                                "fields": {
                                    "type": "default",
                                    "value": "1 ml"
                                }
                            }
                        ]
                    },
                ]
            }
        }
        templateGuid = 'device-template-guid'
        name = 'custom import name'
        entityImport = newEntityImport(user, Device, data, templateGuid, name)
        assert entityImport['author']['id'] == user.id
        assert entityImport['target_entity_name'] == Device.__entityName__
        assert entityImport['data'] == data
        assert entityImport['name'] == name
        assert entityImport['device_template']['guid'] == templateGuid

    def test_edit_name(self):
        user = fixtures.defaultUser()
        entityImportGuid = 'entity-import-guid'
        entityImport = getEntityImport(user, guid=entityImportGuid)
        assert entityImport['guid'] == entityImportGuid
        newName = 'new name'
        entityImport.edit(name=newName)
        assert entityImport['name'] == newName
