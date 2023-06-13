#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.constants import UNSPECIFIED
from labstep.service.helpers import getTime


class Molecule(Entity):
    __entityName__ = "molecule"
    __hasGuid__ = True

    def edit(self, name=UNSPECIFIED, data=UNSPECIFIED, inchis=UNSPECIFIED, extraParams={}):
        """
        Edit an existing Molecule.

        Parameters
        ----------
        name (str)
            Molecule name
        data (str)
            The JSON data for the molecule
        inchis (array)
            List of inchis codes

        Returns
        -------
        :class:`~labstep.entities.molecule.model.Molecule`
            An object representing the edited Molecule.
        """
        import labstep.generic.entity.repository as entityRepository

        params = {
            "name": name,
            "data": data,
            "inchis": inchis,
            **extraParams
        }
        return entityRepository.editEntity(self, params)

    def delete(self):
        """
        Delete an existing Molecule.

        Example
        -------
        ::

            my_molecule = user.getMolecule(17000)
            my_molecule.delete()
        """
        import labstep.entities.molecule.repository as moleculeRepository

        return moleculeRepository.editMolecule(self, deleted_at=getTime())
