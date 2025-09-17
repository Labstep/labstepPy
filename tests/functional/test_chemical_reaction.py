#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pytest
from .fixtures import fixtures

from .shared import sharedTests

# __tracebackhide__ = True


class TestChemicalReaction:
    @pytest.fixture
    def entity(self):
        return fixtures.chemicalReaction()

    def setup_method(self):
        fixtures.loadFixtures('Python\\\\Molecule')

    def test_delete(self, entity):
        assert sharedTests.delete(entity)

    def test_addChemical(self, entity):
        chemical = entity.addChemical(
            'product', molar_amount='10', density='2', molecular_weight='50')
        assert chemical['type'] == 'product'

    def test_setLimitingChemical(self, entity):
        import labstep.entities.chemicalReaction.repository as chemicalReactionRepository
        user = fixtures.defaultUser()
        chemicalReaction = chemicalReactionRepository.getChemicalReaction(
            user, '1234ae5d-4502-4f10-a7c9-822b082b5678')
        assert chemicalReaction['limiting_chemical']['guid'] == '8439ae3d-4502-4f10-a7c9-822b082b2259'
        chemicalReaction.setLimitingChemical(
            '1e493da7-01db-4795-a5c4-e68d824dfcf3')
        assert chemicalReaction['limiting_chemical']['guid'] == '1e493da7-01db-4795-a5c4-e68d824dfcf3'

    def test_demoForDavid(self, entity):
        import labstep.entities.resourceItem.repository as resourceItemRepository

        user = fixtures.defaultUser()

        experiment = user.newExperiment('Chemistry Experiment')

        resource = user.newResource('Benzyene')

        resourceItem1 = resourceItemRepository.newResourceItem(
            user, resource.id, name='Item 1')
        resourceItem2 = resourceItemRepository.newResourceItem(
            user, resource.id, name='Item 2')

        reaction = experiment.addChemicalReaction(data='RXN 233')

        reaction.addChemical(type='reactant', properties={'Safety': [], 'name': 'benzene', 'density': 1, 'formula': 'C4H6', 'MolecularWeight': '54.6'},
                             equivalents=1, purity='0.78', molar_amount='400', amount='45', units='g', resource_id=resource.id, resource_item_id=resourceItem1.id)

        reaction.addChemical(type='product', properties={'Safety': [], 'name': 'benzene', 'density': 1, 'formula': 'C4H6', 'MolecularWeight': '54.6'},
                             equivalents=1, purity='0.78', amount='45', units='g', resource_id=resource.id, resource_item_id=resourceItem2.id)

        entry = {
            "type": "doc",
            "content": [
                {
                    "type": "paragraph",
                    "attrs": {"align": None},
                    "content": [
                        {
                            "type": "text",
                                    "text": "My chemistry experiment"
                        }
                    ]
                },
                {
                    "type": "paragraph",
                    "attrs": {"align": None}
                },
                {
                    "type": "molecule",
                    "attrs": {"guid": reaction.guid},
                }
            ]
        }

        experiment.edit(entry=entry)

        reactions = experiment.getChemicalReactions()

        chemicals = reactions[0].getChemicals()

        linkedInventoryField = chemicals[0].getLinkedInventoryField()

        assert chemicals[0].is_limiting == True
        assert chemicals[0].molar_amount == '400'
        assert linkedInventoryField.resource['id'] == 1
        assert linkedInventoryField.amount == '45'
