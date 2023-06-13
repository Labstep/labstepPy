#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import inspect
import pprint
from labstep.service.helpers import update
from labstep.constants import UNSPECIFIED


class Entity:

    def __init__(self, data, user):
        self.__user__ = user
        self.__data__ = data
        self.id = None
        update(self, data)

    def __repr__(self):
        all_attributes = inspect.getmembers(
            self, lambda a: not (inspect.isroutine(a)))
        entity_attributes = {
            k: v for k, v in all_attributes if not (k.startswith("__"))
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
