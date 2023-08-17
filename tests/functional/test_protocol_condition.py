# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # Author: Labstep <dev@labstep.com>
# import pytest
# from .fixtures import protocolDataField, experimentInventoryField, loadFixtures, authUser
# from .shared import sharedTests


# class TestProtocolCondition:

#     @pytest.fixture
#     def entity(self):
#         return protocolDataField()

#     @pytest.fixture
#     def inventoryField(self):
#         return experimentInventoryField()

#     def setup_method(self):
#         loadFixtures('Python\\\\Metadata')

#     def test_edit(self, entity):
#         result = entity.edit(fieldName='Pytest Edited')
#         assert result.label == 'Pytest Edited'

#     def test_delete(self, entity):
#         assert sharedTests.delete(entity)

#     def test_link_to_inventory_field(self):
#         user = authUser()
#         exp = user.newProtocol('Test')
#         data = exp.addDataField('Test')
#         inventoryField = exp.addInventoryField('Test')
#         data.linkToInventoryField(inventoryField)
#         linkedInventoryFields = data.getLinkedInventoryFields()
#         assert linkedInventoryFields[0].id == inventoryField.id
