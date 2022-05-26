#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Onoufrios Malikkides <onoufrios@labstep.com>

from labstep.service.helpers import getTime
from labstep.constants import UNSPECIFIED
from labstep.generic.entity.model import Entity
from labstep.entities.experimentInventoryField.model import ExperimentInventoryField


TYPE_REACTANT = "reactant"
TYPE_PRODUCT = "product"
TYPE_SOLVENT = "solvent"


class Chemical(Entity):
    """
    Holds stoichiometry information and properties about a particular chemical in a chemical reaction.

    """
    __entityName__ = "chemical"
    __hasGuid__ = True

    def edit(self, equivalents=UNSPECIFIED, purity=UNSPECIFIED, molar_amount=UNSPECIFIED, density=UNSPECIFIED, molecular_weight=UNSPECIFIED, extraParams={}):
        """
        Edit an existing Chemical.

        Parameters
        ----------
        equivalents (int)
            Equivalents as an integer
        purity (float)
            Purity (Value between 0 and 1)
        density (str)
            The density of the chemical
        molecular_weight (str)
            The molecular weight of the chemical
        molar_amount (str)
            Molar Amount

        Returns
        -------
        :class:`~labstep.entities.chemical.model.Chemical`
            An object representing the edited chemical.
        """
        import labstep.generic.entity.repository as entityRepository

        properties = self.properties
        if (density):
            properties.Density = density
        if (molecular_weight):
            properties.MolecularWeight = molecular_weight

        params = {
            "equivalence": equivalents,
            "purity": purity,
            "molar_amount": molar_amount,
            "properties": properties,
            **extraParams
        }
        return entityRepository.editEntity(self, params)

    def delete(self):
        """
        Delete an existing Chemical.

        Example
        -------
        ::

            my_chemical = user.getChemical('guid')
            my_chemical.delete()
        """
        import labstep.entities.chemical.repository as chemicalRepository

        return chemicalRepository.editChemical(self, deleted_at=getTime())

    def getLinkedInventoryField(self):
        """
        Returns the inventory field linked to the chemical in the reaction

        Returns
        -------
        :class:`~labstep.entities.experimentInventoryField.model.ExperimentInventoryField`
            The Linked inventory field
        """
        return ExperimentInventoryField(self.protocol_value, self.__user__)
