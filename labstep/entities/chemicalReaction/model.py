#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.constants import UNSPECIFIED
from labstep.service.helpers import getTime
import labstep.entities.chemical.repository as chemicalRepository


class ChemicalReaction(Entity):
    """
    Represents a chemical reaction in an Experiment

    """
    __entityName__ = "molecule"
    __hasGuid__ = True

    def edit(self, name=UNSPECIFIED, data=UNSPECIFIED, extraParams={}):
        """
        Edit an existing Chemical Reaction.

        Parameters
        ----------
        name (str)
            Reaction name
        data (str)
            The SMILES / RXN / JSON data for the reaction

        Returns
        -------
        :class:`~labstep.entities.chemicalReaction.model.ChemicalReaction`
            An object representing the edited Chemical Reaction.


        Example
        -------
        ::

            my_reaction = experiment.getChemicalReactions()[0]
            my_reaction.edit(data='C1=CC=CC=C1>>C1=CC=CC=C1')
        """
        import labstep.generic.entity.repository as entityRepository

        params = {
            "name": name,
            "data": data,
            **extraParams
        }
        return entityRepository.editEntity(self, params)

    def delete(self):
        """
        Delete the chemical reaction.

        Example
        -------
        ::

            my_reaction = experiment.getChemicalReactions()[0]
            my_reaction.delete()
        """
        import labstep.entities.molecule.repository as moleculeRepository

        return moleculeRepository.editMolecule(self, deleted_at=getTime())

    def addChemical(self, type="reactant", equivalents=UNSPECIFIED, purity=UNSPECIFIED, amount=UNSPECIFIED, molar_amount=UNSPECIFIED, density=UNSPECIFIED, molecular_weight=UNSPECIFIED, properties=UNSPECIFIED, units='g', resource_id=UNSPECIFIED, resource_item_id=UNSPECIFIED):
        """
        Add a new Chemical to the reaction.

        Parameters
        ----------
        type (string)
            "reactant"|"product"|"solvent". Defaults to "reactant".
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
        units (str)
            Defaults to "g"
        Returns
        -------
        :class:`~labstep.entities.chemical.model.Chemical`
            An object representing the Chemical added.
        """
        import labstep.entities.chemical.repository as chemicalRepository
        import labstep.entities.experimentInventoryField.repository as experimentInventoryFieldRepository

        if properties is UNSPECIFIED and resource_id is not UNSPECIFIED:

            properties = self.__user__.getResource(
                resource_id).getChemicalMetadata()

        finalProperties = properties if properties is not UNSPECIFIED else {}

        if (density != UNSPECIFIED):
            finalProperties['Density'] = density
        if (molecular_weight != UNSPECIFIED):
            finalProperties['MolecularWeight'] = molecular_weight

        if 'Safety' not in finalProperties:
            finalProperties['Safety'] = {}

        if (equivalents):
            equivalents = str(equivalents)

        params = {
            "type": type,
            "equivalence": equivalents,
            "purity": purity,
            "molar_amount": molar_amount,
            "properties": finalProperties
        }

        value = experimentInventoryFieldRepository.newExperimentInventoryField(
            self.__user__, self.experiment_id, None, units=units, amount=amount, resource_id=resource_id, resource_item_id=resource_item_id)
        return chemicalRepository.newChemical(
            self.__user__, value.id, self.guid, extraParams=params)

    def setLimitingChemical(self, guid):
        """
        Set the limiting Chemical.

        Parameters
        ----------
        guid (string)
            chemical guid

        Returns
        -------
        :class:`~labstep.entities.chemicalReaction.model.ChemicalReaction`
            An object representing the Chemical Reaction.
        """
        extraParams = {"limiting_chemical_guid": guid}
        return self.edit(extraParams=extraParams)

    def getChemicals(self):
        """
        Returns a list of the chemicals inside the chemical reaction

        Returns
        -------
        List[:class:`~labstep.entities.chemical.model.Chemical`]
            List of the chemicals inside the chemical reaction

        Example
        -------
        ::

            chemical_reaction_chemicals = reaction.getChemicals()
        """
        return chemicalRepository.getChemicals(self.__user__, self.guid)
