#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
from .fixtures import workspace, resource, resourceCategory, authUser, testString, loadFixtures
from .shared import sharedTests


class TestResource:
    @pytest.fixture
    def entity(self):
        return resource()

    @pytest.fixture
    def category(self):
        return resourceCategory()

    @pytest.fixture
    def workspaceToShare(self):
        return workspace()

    def setup_method(self):
        loadFixtures('Python\\\\Resource')

    def test_edit(self, entity):
        assert sharedTests.edit(entity)

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test_commenting(self, entity):
        assert sharedTests.commenting(entity)

    def test_metadata(self, entity):
        assert sharedTests.metadata(entity)

    def test_tagging(self, entity):
        assert sharedTests.tagging(entity)

    def test_sharelink(self, entity):
        assert sharedTests.sharelink(entity)

    def test_sharing(self, entity, workspaceToShare):
        assert sharedTests.sharing(entity, workspaceToShare)

    def test_setResourceCategory(self, entity, category):
        entity.setResourceCategory(category.id)
        resourceCategoryFromGet = entity.getResourceCategory()
        assert resourceCategoryFromGet.id == category.id

    def test_newOrderRequest(self, entity):
        result = entity.newOrderRequest()
        assert result.status

    def test_getData(self, entity):
        user = authUser()
        exp = user.newExperiment('Test')
        item = entity.newItem()
        data = exp.addDataField('Test', value='test',
                                extraParams={'is_output': True})
        exp.addInventoryField(resource_item_id=item.id)

        result = entity.getData()
        assert result[0].id == data.id

    def test_newItem(self, entity):
        result = entity.newItem(name=testString)
        assert result.id

    def test_getItems(self, entity):
        item = entity.newItem()
        result = entity.getItems()
        assert result[0].id == item.id

    def test_enableItemTemplate(self, entity):
        entity.enableCustomItemTemplate()
        itemTemplate = entity.getItemTemplate()
        assert itemTemplate.deleted_at is None

    def test_disableItemTemplate(self, entity):
        entity.enableCustomItemTemplate()
        entity.disableCustomItemTemplate()
        itemTemplate = entity.getItemTemplate()
        assert itemTemplate.deleted_at is not None

    def test_chemicalMetadata(self, entity):
        entity.addChemicalMetadata(
            structure='C1=CC=CC=C1',
            iupac_name="benzene",
            cas="71-43-2",
            density="0.879 at 68 °F (USCG, 1999)",
            inchi="InChI=1S/C6H6/c1-2-4-6-5-3-1/h1-6H",
            molecular_formula="C6H6",
            molecular_weight="78.11",
            smiles='C1=CC=CC=C1',
            safety={
                "precautionary": {
                    "General": [],
                    "Prevention": [
                        "P281"
                    ],
                    "Response": [

                        "P370+P378"
                    ],
                    "Storage": [

                        "P405"
                    ],
                    "Disposal": [
                        "P501"
                    ]
                },
                "ghs_hazard_statements": [
                    "H372"
                ],
                "pictograms": [
                    "GHS02",
                    "GHS07",
                    "GHS08"
                ]
            })
        chemicalMetadata = entity.getChemicalMetadata()
        assert chemicalMetadata['Structure'] == 'C1=CC=CC=C1'
        assert chemicalMetadata['IUPACName'] == 'benzene'
        assert chemicalMetadata['CAS'] == "71-43-2"
        assert chemicalMetadata['InChI'] == "InChI=1S/C6H6/c1-2-4-6-5-3-1/h1-6H"
        assert chemicalMetadata['MolecularFormula'] == "C6H6"
        assert chemicalMetadata['MolecularWeight'] == "78.11"
        assert chemicalMetadata['SMILES'] == 'C1=CC=CC=C1'
        assert chemicalMetadata['Safety'] == {
            "precautionary": {
                "General": [],
                "Prevention": [
                    "P281"
                ],
                "Response": [

                    "P370+P378"
                ],
                "Storage": [

                    "P405"
                ],
                "Disposal": [
                    "P501"
                ]
            },
            "ghs_hazard_statements": [
                "H372"
            ],
            "pictograms": [
                "GHS02",
                "GHS07",
                "GHS08"
            ]
        }
