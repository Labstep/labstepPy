#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity


class EntityImport(Entity):
    """
    Represents an EntityImport on Labstep.
    """

    __entityName__ = "entity-import"
    __hasGuid__ = True

    def edit(self, name=None):
        """
        Edit an existing EntityImport.

        Parameters
        ----------
        name (str)
            Custom name given by the user for the import.

        Returns
        -------
        :class:`~labstep.entities.entityImport.model.EntityImport`
            An object representing the edited EntityImport.

        Example
        -------
        ::

            entityImport = user.getEntityImport("872b3e7e-e21f-4403-9ef3-3650fe0d86ba")
            entityImport.edit(name='My first import')
        """
        import labstep.entities.entityImport.repository as entityImportRepository

        return entityImportRepository.editEntityImport(
            self, name=name
        )
