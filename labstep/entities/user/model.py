#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

import json
import urllib.parse
from labstep.generic.entity.model import Entity
from labstep.service.config import API_ROOT
from labstep.service.helpers import url_join, handleError, getHeaders
from labstep.service.request import requestService


class User(Entity):
    """
    Represents a Labstep User.

    To see all attributes of the user run
    ::
        print(user)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(user.name)
        print(user.id)
    """

    def __init__(self, user):
        if user["group"] is None:
            print(
                """Warning: No default workspace.
            Please set a workspace to continue."""
            )
            self.activeWorkspace = None
        else:
            self.activeWorkspace = user["group"]["id"]
        for key in user:
            setattr(self, key, user[key])

    def setWorkspace(self, workspace_id: int):
        """
        Set a Workspace as the active Workspace.

        Parameters
        ----------
        workspace_id (int)
            The id of the Workspace to set as active.

        Returns
        -------
        :class:`~labstep.entities.workspace.model.Workspace`
            An object representing a Workspace on Labstep.

        Example
        -------
        ::

            entity = user.getWorkspace(17000)
            user.setWorkspace(entity.id)
        """
        if isinstance(workspace_id, int) is False:
            raise TypeError("workspace_id must be an integer")

        self.activeWorkspace = workspace_id

    # getSingle()
    def getExperiment(self, experiment_id):
        """
        Retrieve a specific Labstep Experiment.

        Parameters
        ----------
        experiment_id (int)
            The id of the Experiment to retrieve.

        Returns
        -------
        :class:`~labstep.entities.experiment.model.Experiment`
            An object representing an Experiment on Labstep.

        Example
        -------
        ::

            entity = user.getExperiment(17000)
        """
        from labstep.entities.experiment.repository import experimentRepository

        return experimentRepository.getExperiment(self, experiment_id)

    def getProtocol(self, protocol_id):
        """
        Retrieve a specific Labstep Protocol.

        Parameters
        ----------
        protocol_id (int)
            The id of the Protocol to retrieve.

        Returns
        -------
        :class:`~labstep.entities.protocol.model.Protocol`
            An object representing a Protocol on Labstep.

        Example
        -------
        ::

            entity = user.getProtocol(17000)
        """
        from labstep.entities.protocol.repository import protocolRepository

        return protocolRepository.getProtocol(self, protocol_id)

    def getResource(self, resource_id):
        """
        Retrieve a specific Labstep Resource.

        Parameters
        ----------
        resource_id (int)
            The id of the Resource to retrieve.

        Returns
        -------
        :class:`~labstep.entities.resource.model.Resource`
            An object representing a Resource on Labstep.

        Example
        -------
        ::

            entity = user.getResource(17000)
        """
        from labstep.entities.resource.repository import resourceRepository

        return resourceRepository.getResource(self, resource_id)

    def getResourceItem(self, resource_item_id):
        """
        Retrieve a specific Labstep Resource Item.

        Parameters
        ----------
        resource_item_id (int)
            The id of the Resource Item to retrieve.

        Returns
        -------
        :class:`~labstep.entities.resourceItem.model.ResourceItem`
            An object representing a Resource Item on Labstep.

        Example
        -------
        ::

            entity = user.getResourceItem(17000)
        """
        from labstep.entities.resourceItem.repository import resourceItemRepository

        return resourceItemRepository.getResourceItem(self, resource_item_id)

    def getResourceCategory(self, resource_category_id):
        """
        Retrieve a specific Labstep ResourceCategory.

        Parameters
        ----------
        resource_category_id (int)
            The id of the ResourceCategory to retrieve.

        Returns
        -------
        :class:`~labstep.entities.resourceCategory.model.ResourceCategory`
            An object representing a ResourceCategory on Labstep.

        Example
        -------
        ::

            entity = user.getResourceCategory(17000)
        """
        from labstep.entities.resourceCategory.repository import resourceCategoryRepository

        return resourceCategoryRepository.getResourceCategory(
            self, resource_category_id
        )

    def getResourceLocation(self, resource_location_id):
        """
        Retrieve a specific Labstep ResourceLocation.

        Parameters
        ----------
        resource_location_id (int)
            The id of the ResourceLocation to retrieve.

        Returns
        -------
        :class:`~labstep.entities.resourceLocation.model.ResourceLocation`
            An object representing a ResourceLocation on Labstep.

        Example
        -------
        ::

            entity = user.getResourceLocation(17000)
        """
        from labstep.entities.resourceLocation.repository import resourceLocationRepository

        return resourceLocationRepository.getResourceLocation(
            self, resource_location_id
        )

    def getOrderRequest(self, order_request_id):
        """
        Retrieve a specific Labstep OrderRequest.

        Parameters
        ----------
        order_request_id (int)
            The id of the OrderRequest to retrieve.

        Returns
        -------
        :class:`~labstep.entities.orderRequest.model.OrderRequest`
            An object representing a OrderRequest on Labstep.

        Example
        -------
        ::

            entity = user.getOrderRequest(17000)
        """
        from labstep.entities.orderRequest.repository import orderRequestRepository

        return orderRequestRepository.getOrderRequest(self, order_request_id)

    def getWorkspace(self, workspace_id):
        """
        Retrieve a specific Labstep Workspace.

        Parameters
        ----------
        workspace_id (int)
            The id of the Workspace to retrieve.

        Returns
        -------
        :class:`~labstep.entities.workspace.model.Workspace`
            An object representing a Workspace on Labstep.

        Example
        -------
        ::

            entity = user.getWorkspace(17000)
        """
        from labstep.entities.workspace.repository import workspaceRepository

        return workspaceRepository.getWorkspace(self, workspace_id)

    def getFile(self, file_id):
        """
        Retrieve a specific Labstep File.

        Parameters
        ----------
        file_id (int)
            The id of the File to retrieve.

        Returns
        -------
        :class:`~labstep.entities.file.model.File`
            An object representing a File on Labstep.

        Example
        -------
        ::

            entity = user.getFile(17000)
        """
        from labstep.entities.file.repository import fileRepository

        return fileRepository.getFile(self, file_id)

    def getDevice(self, device_id):
        """
        Retrieve a specific Labstep Device.

        Parameters
        ----------
        device_id (int)
            The id of the Device to retrieve.

        Returns
        -------
        :class:`~labstep.entities.device.model.Device`
            An object representing a Device on Labstep.

        Example
        -------
        ::

            entity = user.getDevice(17000)
        """
        from labstep.entities.device.repository import deviceRepository

        return deviceRepository.getDevice(self, device_id)

    # getMany()
    def getExperiments(
        self,
        count=100,
        search_query=None,
        created_at_from=None,
        created_at_to=None,
        tag_id=None,
        collection_id=None,
        extraParams={},
    ):
        """
        Retrieve a list of a User's Experiments
        across all Workspaces on Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of Experiments to retrieve.
        search_query (str)
            Search for Experiments containing this string in the name or entry.
        created_at_from (str)
            The start date of the search range, must be
            in the format of 'YYYY-MM-DD'.
        created_at_to (str)
            The end date of the search range, must be
            in the format of 'YYYY-MM-DD'.
        tag_id (int)
            The id of a tag to filter by.
        collection_id (int)
            Get experiments in this collection.

        Returns
        -------
        List[:class:`~labstep.entities.experiment.model.Experiment`]
            A list of Labstep Experiments.

        Example
        -------
        ::

            entity = user.getExperiments(search_query='bacteria',
                                         created_at_from='2019-01-01',
                                         created_at_to='2019-01-31',
                                         tag_id=800)
        """
        from labstep.entities.experiment.repository import experimentRepository

        return experimentRepository.getExperiments(
            self,
            count=count,
            search_query=search_query,
            created_at_from=created_at_from,
            created_at_to=created_at_to,
            tag_id=tag_id,
            collection_id=collection_id,
            extraParams=extraParams,
        )

    def getProtocols(
        self,
        count=100,
        search_query=None,
        created_at_from=None,
        created_at_to=None,
        tag_id=None,
        collection_id=None,
        extraParams={},
    ):
        """
        Retrieve a list of a User's Protocols
        across all Workspaces on Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of Protocols to retrieve.
        search_query (str)
            Search for Protocols with this 'name'.
        created_at_from (str)
            The start date of the search range, must be
            in the format of 'YYYY-MM-DD'.
        created_at_to (str)
            The end date of the search range, must be
            in the format of 'YYYY-MM-DD'.
        tag_id (int)
            The id of a tag to filter by.
        collection_id (int)
            Get protocols in this collection.

        Returns
        -------
        List[:class:`~labstep.entities.protocol.model.Protocol`]
            A list of Labstep Protocols.

        Example
        -------
        ::

            entity = user.getProtocols(search_query='bacteria',
                                       created_at_from='2019-01-01',
                                       created_at_to='2019-01-31',
                                       tag_id=800)
        """
        from labstep.entities.protocol.repository import protocolRepository

        return protocolRepository.getProtocols(
            self,
            count=count,
            search_query=search_query,
            created_at_from=created_at_from,
            created_at_to=created_at_to,
            tag_id=tag_id,
            collection_id=collection_id,
            extraParams=extraParams,
        )

    def getResources(self, count=100, search_query=None, tag_id=None, extraParams={}):
        """
        Retrieve a list of a User's Resources
        across all Workspaces on Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of Resources to retrieve.
        search_query (str)
            Search for Resources with this 'name'.
        tag_id (int)
            The id of a tag to filter by.

        Returns
        -------
        List[:class:`~labstep.entities.resource.model.Resource`]
            A list of Labstep Resources.

        Example
        -------
        ::

            entity = user.getResources(search_query='bacteria',
                                       tag_id=800)
        """
        from labstep.entities.resource.repository import resourceRepository

        return resourceRepository.getResources(
            self,
            count=count,
            search_query=search_query,
            tag_id=tag_id,
            extraParams=extraParams,
        )

    def getResourceCategorys(
        self, count=100, search_query=None, tag_id=None, extraParams={}
    ):
        """
        Retrieve a list of a User's Resource Categorys
        across all Workspaces on Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of ResourceCategorys to retrieve.
        search_query (str)
            Search for ResourceCategorys with this 'name'.
        tag_id (int)
            The id of a tag to filter by.

        Returns
        -------
        List[:class:`~labstep.entities.resourceCategory.model.ResourceCategory`]
            A list of Labstep ResourceCategorys.

        Example
        -------
        ::

            entity = user.getResourceCategorys(search_query='properties',
                                               tag_id=800)
        """
        from labstep.entities.resourceCategory.repository import resourceCategoryRepository

        return resourceCategoryRepository.getResourceCategorys(
            self,
            count=count,
            search_query=search_query,
            tag_id=tag_id,
            extraParams=extraParams,
        )

    def getResourceLocations(self, count=100, search_query=None, extraParams={}):
        """
        Retrieve a list of a user's ResourceLocations on Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of ResourceLocations to retrieve.
        search_query (str)
            Search for ResourceLocations with this 'name'.

        Returns
        -------
        List[:class:`~labstep.entities.resourceLocation.model.ResourceLocation`]
            A list of ResourceLocation objects.

        Example
        -------
        ::

            entity = user.getResourceLocations(search_query='fridge')
        """
        from labstep.entities.resourceLocation.repository import resourceLocationRepository

        return resourceLocationRepository.getResourceLocations(
            self, count=count, search_query=search_query, extraParams=extraParams
        )

    def getOrderRequests(
        self, count=100, search_query=None, status=None, tag_id=None, extraParams={}
    ):
        """
        Retrieve a list of a user's OrderRequests on Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of OrderRequests to retrieve.
        search_query (str)
            Search query for OrderRequests with this 'name'.
        status (str)
            The status of the OrderRequest to filter by. Options are: "new",
            "approved", "ordered", "back_ordered", "received", and "cancelled".
        tag_id (int)
            The id of a tag to filter by.

        Returns
        -------

        List[:class:`~labstep.entities.orderRequest.model.OrderRequest`]
            A list of Labstep OrderRequests.

        Example
        -------
        ::

            entity = user.getOrderRequests(name='polymerase')
        """
        from labstep.entities.orderRequest.repository import orderRequestRepository

        return orderRequestRepository.getOrderRequests(
            self,
            count=count,
            search_query=search_query,
            status=status,
            tag_id=tag_id,
            extraParams=extraParams,
        )

    def getTags(self, count=1000, search_query=None, type=None, extraParams={}):
        """
        Retrieve a list of a User's Tags
        across all Workspaces on Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of Tags to retrieve.
        type (str)
            Return only tags of a certain type. Options are:
            'experiment_workflow', 'protocol_collection',
            'resource', 'order_request'.
        search_query (str)
            Search for Tags with this 'name'.

        Returns
        -------
        List[:class:`~labstep.entities.tag.model.Tag`]
            A list of Labstep Tags.

        Example
        -------
        ::

            entity = user.getTags(search_query='bacteria')
        """
        from labstep.entities.tag.repository import tagRepository

        return tagRepository.getTags(
            self,
            count=count,
            type=type,
            search_query=search_query,
            extraParams=extraParams,
        )

    def getWorkspaces(self, count=100, search_query=None, extraParams={}):
        """
        Retrieve a list of a user's Workspaces on Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of Workspaces to retrieve.
        search_query (str)
            Search for Workspaces with this 'name'.

        Returns
        -------

        List[:class:`~labstep.entities.workspace.model.Workspace`]
            A list of Labstep Workspaces.

        Example
        -------
        ::

            entity = user.getWorkspaces(name='bacteria')
        """
        from labstep.entities.workspace.repository import workspaceRepository

        return workspaceRepository.getWorkspaces(
            self, count=count, search_query=search_query, extraParams=extraParams
        )

    def getFiles(self, count=100, search_query=None, file_type=None, extraParams={}):
        """
        Retrieve a list of a User's Files
        across all Workspaces on Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of files to retrieve.
        file_type (str)
            Return only files of a certain type. Options are:
            'csv', 'doc',
            'docx', 'jpg', 'pdf','png','ppt','pptx','svg','xls','xlsx',
            'xml' or 'generic' for all others.
        search_query (str)
            Search for files with this name.

        Returns
        -------
        List[:class:`~labstep.entities.file.model.File`]
            A list of Labstep Files.

        Example
        -------
        ::

            entities = user.getFiles(search_query='bacteria')
        """
        from labstep.entities.file.repository import fileRepository

        return fileRepository.getFiles(
            self,
            count=count,
            search_query=search_query,
            file_type=file_type,
            extraParams=extraParams,
        )

    def getDevices(self, count=100, search_query=None, extraParams={}):
        """
        Retrieve a list of a User's Devices
        across all Workspaces on Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of Devices to retrieve.
        search_query (str)
            Search for Devices by name / metadata fields.

        Returns
        -------
        List[:class:`~labstep.entities.device.model.Device`]
            A list of Labstep Devices.

        Example
        -------
        ::

            entity = user.getDevices(search_query='microscope')
        """
        from labstep.entities.device.repository import deviceRepository

        return deviceRepository.getDevices(
            self, count=count, search_query=search_query, extraParams=extraParams
        )

    # newEntity()

    def newExperiment(self, name, entry=None, extraParams={}):
        """
        Create a new Labstep Experiment.

        Parameters
        ----------
        name (str)
            Give your Experiment a name.
        entry (obj)
            A JSON object representing the state of the Experiment Entry.

        Returns
        -------
        :class:`~labstep.entities.experiment.model.Experiment`
            An object representing an Experiment on Labstep.

        Example
        -------
        ::

            entity = user.newExperiment(name='The Synthesis of Aspirin')
        """
        from labstep.entities.experiment.repository import experimentRepository

        return experimentRepository.newExperiment(
            self, name, entry=entry, extraParams=extraParams
        )

    def newProtocol(self, name, extraParams={}):
        """
        Create a new Labstep Protocol.

        Parameters
        ----------
        name (str)
            Give your Protocol a name.

        Returns
        -------
        :class:`~labstep.entities.protocol.model.Protocol`
            An object representing a Protocol on Labstep.

        Example
        -------
        ::

            entity = user.newProtocol(name='Synthesising Aspirin')
        """
        from labstep.entities.protocol.repository import protocolRepository

        return protocolRepository.newProtocol(self, name, extraParams=extraParams)

    def newResource(self, name, extraParams={}):
        """
        Create a new Labstep Resource.

        Parameters
        ----------
        name (str)
            Give your Resource a name.

        Returns
        -------
        :class:`~labstep.entities.resource.model.Resource`
            An object representing a Resource on Labstep.

        Example
        -------
        ::

            entity = user.newResource(name='salicylic acid')
        """
        from labstep.entities.resource.repository import resourceRepository

        return resourceRepository.newResource(self, name, extraParams=extraParams)

    def newResourceCategory(self, name, extraParams={}):
        """
        Create a new Labstep ResourceCategory.

        Parameters
        ----------
        name (str)
            Give your ResourceCategory a name.

        Returns
        -------
        :class:`~labstep.entities.resourceCategory.model.ResourceCategory`
            An object representing the new Labstep ResourceCategory.

        Example
        -------
        ::

            entity = user.newResourceCategory(name='Chemical')
        """
        from labstep.entities.resourceCategory.repository import resourceCategoryRepository

        return resourceCategoryRepository.newResourceCategory(
            self, name, extraParams=extraParams
        )

    def newResourceLocation(self, name, outer_location_id=None, extraParams={}):
        """
        Create a new Labstep ResourceLocation.

        Parameters
        ----------
        name (str)
            Give your ResourceLocation a name.

        outer_location_id (int)
            The id of existing location to create the location within

        extraParams (dict)
            (Advanced) Dictionary of extra parameters to pass in the
            POST request

        Returns
        -------
        :class:`~labstep.entities.resourceLocation.model.ResourceLocation`
            An object representing the new Labstep ResourceLocation.

        Example
        -------
        ::

            entity = user.newResourceLocation(name='Fridge A')
        """
        from labstep.entities.resourceLocation.repository import resourceLocationRepository

        return resourceLocationRepository.newResourceLocation(
            self, name, outer_location_id=outer_location_id, extraParams=extraParams
        )

    def newOrderRequest(self, resource_id, quantity=1, extraParams={}):
        """
        Create a new Labstep OrderRequest.

        Parameters
        ----------
        resource_id (int)
            The id of the :class:`~labstep.entities.resource.model.Resource`
            to request more items of.
        quantity (int)
            The quantity of items requested.

        Returns
        -------
        :class:`~labstep.entities.orderRequest.model.OrderRequest`
            An object representing the an OrderRequest on Labstep.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            entity = user.newOrderRequest(my_resource.id, quantity=2)
        """
        from labstep.entities.orderRequest.repository import orderRequestRepository

        return orderRequestRepository.newOrderRequest(
            self, resource_id=resource_id, quantity=quantity, extraParams=extraParams
        )

    def newTag(self, name, type, extraParams={}):
        """
        Create a new Labstep Tag.

        Parameters
        ----------
        name (str)
            Give your Tag a name.
        type (str)
            Return only tags of a certain type. Options are:
            'experiment_workflow', 'protocol_collection',
            'resource', 'order_request'.

        Returns
        -------
        :class:`~labstep.entities.tag.model.Tag`
            An object representing a Tag on Labstep.

        Example
        -------
        ::

            entity = user.newTag(name='Aspirin')
        """
        from labstep.entities.tag.repository import tagRepository

        return tagRepository.newTag(self, name, type=type, extraParams=extraParams)

    def newWorkspace(self, name, extraParams={}):
        """
        Create a new Labstep Workspace.

        Parameters
        ----------
        name (str)
            Give your Workspace a name.

        Returns
        -------
        :class:`~labstep.entities.workspace.model.Workspace`
            An object representing a Workspace on Labstep.

        Example
        -------
        ::

            entity = user.newWorkspace(name='Aspirin Project')
        """
        from labstep.entities.workspace.repository import workspaceRepository

        return workspaceRepository.newWorkspace(self, name, extraParams=extraParams)

    def newFile(self, filepath, extraParams={}):
        """
        Upload a file to the Labstep entity Data.

        Parameters
        ----------
        filepath (str)
            The filepath to the file to attach.

        Example
        -------
        ::

            entity = user.newFile('./structure_of_aspirin.png')
        """
        from labstep.entities.file.repository import fileRepository

        return fileRepository.newFile(self, filepath, extraParams=extraParams)

    def newCollection(self, name, type="experiment"):
        """
        Create a new Collection for Experiments (or Protocols)

        Parameters
        ----------
        type (str)
            The filepath to the file to attach.
        """
        from labstep.entities.collection.repository import collectionRepository

        return collectionRepository.newCollection(self, name=name, type=type)

    def newDevice(self, name, extraParams={}):
        """
        Create a new Labstep Device.

        Parameters
        ----------
        name (str)
            Give your Device a name.

        Returns
        -------
        :class:`~labstep.entities.device.model.Device`
            An object representing a Device on Labstep.

        Example
        -------
        ::

            entity = user.newDevice(name='Microscope A')
        """
        from labstep.entities.device.repository import deviceRepository

        return deviceRepository.newDevice(self, name, extraParams)

    def acceptSharelink(self, token):
        """
        Accept a sharelink
        Parameters
        ----------
        token (class)
            The token of the sharelink.

        Returns
        -------
        None
        """
        # FIXME Refactor
        headers = getHeaders(self)
        url = url_join(API_ROOT, "/api/generic/",
                       "share-link", 'accept', token)
        requestService.post(url, headers=headers)
        return None
