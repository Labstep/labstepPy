#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import inspect
import pprint
from labstep.service.helpers import getTime, update
from labstep.constants import UNSPECIFIED


class Entity:

    def __init__(self, data, user):
        self.id = None
        self.__user__ = user
        update(self, data)

    def __repr__(self):
        all_attributes = self.__dict__
        entity_attributes = {
            k: v for k, v in all_attributes.items() if not (k.startswith("__"))
        }
        pp = pprint.PrettyPrinter(indent=1)
        return pp.pformat(entity_attributes)

    def __getitem__(self, key):
        return getattr(self, key, None)

    def update(self):
        """
        Fetches the most up-to-date version of the entity from Labstep.
        """
        import labstep.generic.entity.repository as entityRepository
        identifier = 'guid' if getattr(
            type(self), "__hasGuid__", None) else 'id'

        data = entityRepository.getEntity(
            self.__user__, type(self), self[identifier]).__data__

        self.__init__(data, self.__user__)
        return self

    def export(self, rootPath, folderName=UNSPECIFIED):
        """
        Export the entity to the directory specified. 

        Parameters
        -------
        path (str)
            The path to the directory to save the experiment.

        Example
        -------
        ::

            experiment = user.getExperiment(17000)
            experiment.export('/my_folder')
        """
        import labstep.generic.entity.repository as entityRepository
        return entityRepository.exportEntity(self, rootPath, folderName=folderName)

    def delete(self):
        """
        Deletes the Labstep Entity (can be restored). 

        Example
        -------
        ::
            experiment = user.getExperiment(17000)
            experiment.delete()
        """
        from labstep.generic.entity.repository import editEntity

        return editEntity(self, {"deleted_at": getTime()})
