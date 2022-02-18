#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.service.helpers import getTime
from labstep.constants import UNSPECIFIED


class Collection(Entity):
    """
    Represents a Collection on Labstep.

    To see all attributes of a collection run
    ::
        print(my_collection)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(my_collection.name)
        print(my_collection.id)
    """

    __entityName__ = "folder"
    __hasParentGroup__ = True

    def edit(self, name=UNSPECIFIED, extraParams={}):
        """
        Edit the name of an existing Collection.

        Parameters
        ----------
        name (str)
            The new name of the Collection.

        Returns
        -------
        :class:`~labstep.entities.collection.model.Collection`
            An object representing the edited Collection.

        Example
        -------
        ::

            # Get all collections, since there is no function
            # to get one collection.
            collections = user.getCollections()

            # Select the collection by using python index.
            collections[1].edit(name='A New Collection Name')
        """
        import labstep.entities.collection.repository as collectionRepository

        return collectionRepository.editCollection(self, name, extraParams=extraParams)

    def delete(self):
        """
        Delete an existing collection.

        Parameters
        ----------
        collection (obj)
            The collection to delete.

        Returns
        -------
        collection
            An object representing the collection to delete.
        """
        return self.edit(extraParams={"deleted_at": getTime()})

    def getSubCollections(self):
        """
        Get a list of the sub-collections within the collection.

        Returns
        -------
        List[:class:`~labstep.entities.collection.model.Collection`]
            A list of sub-collections

        """
        import labstep.entities.collection.repository as collectionRepository
        return collectionRepository.getCollections(self.__user__, extraParams={'outer_folder_id': self.id})

    def addSubCollections(self, names):
        """
        Add a sub-collection sub-collections to the collection.

        Parameters
        ----------
        name (List[str])
            List of names of sub-collections name of the new sub-collection.

        Returns
        -------
        :class:`~labstep.entities.collection.model.Collection`
            An object representing the collection created.
        """
        import labstep.entities.collection.repository as collectionRepository
        types = {"experiment_workflow": "experiment",
                 "protocol_collection": "protocol"}
        return collectionRepository.newCollections(self.__user__, names=names, type=types[self.type], extraParams={'outer_folder_id': self.id})
