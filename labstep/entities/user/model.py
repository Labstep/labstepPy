#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from deprecated import deprecated
from labstep.generic.entity.model import Entity
from labstep.service.config import configService
from labstep.service.helpers import url_join, getHeaders
from labstep.service.request import requestService
from labstep.constants import UNSPECIFIED


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
    __entityName__ = "user"

    def __init__(self, data, adminUser=UNSPECIFIED):
        super().__init__(data, self)
        self.__user__ = adminUser if adminUser is not UNSPECIFIED else self
        self._activeWorkspace = getattr(self.__data__, 'group', None)

    @property
    def activeWorkspace(self):

        if self._activeWorkspace is not None:
            return self._activeWorkspace

        if 'group' not in self.__data__ or self.__data__["group"] is None:
            raise Exception(
                "No workspace specified. Please set a workspace to continue.")
        else:
            self._activeWorkspace = self.__data__["group"]["id"]

        return self._activeWorkspace

    def update(self):
        import json
        from labstep.service.helpers import url_join, update
        from labstep.service.config import configService
        from labstep.service.request import requestService

        apikey = self.__user__['api_key']
        url = url_join(configService.getHost(), "api/generic/user/info")
        response = requestService.get(url, headers={"apikey": apikey})
        data = json.loads(response.content)
        update(self, data)
        return self

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

        self._activeWorkspace = workspace_id

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
        import labstep.entities.experiment.repository as experimentRepository

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
        import labstep.entities.protocol.repository as protocolRepository

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
        import labstep.entities.resource.repository as resourceRepository

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
        import labstep.entities.resourceItem.repository as resourceItemRepository

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
        import labstep.entities.resourceCategory.repository as resourceCategoryRepository

        return resourceCategoryRepository.getResourceCategory(
            self, resource_category_id
        )

    def getResourceLocation(self, resource_location_guid):
        """
        Retrieve a specific Labstep ResourceLocation.

        Parameters
        ----------
        resource_location_guid (guid)
            The guid of the ResourceLocation to retrieve.

        Returns
        -------
        :class:`~labstep.entities.resourceLocation.model.ResourceLocation`
            An object representing a ResourceLocation on Labstep.

        Example
        -------
        ::

            entity = user.getResourceLocation(17000)
        """
        import labstep.entities.resourceLocation.repository as resourceLocationRepository

        return resourceLocationRepository.getResourceLocation(
            self, resource_location_guid
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
        import labstep.entities.orderRequest.repository as orderRequestRepository

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
        import labstep.entities.workspace.repository as workspaceRepository

        return workspaceRepository.getWorkspace(self, workspace_id)

    def getOrganization(self):
        """
        Returns the organization the user is part of.

        Returns
        -------
        :class:`~labstep.entities.organization.model.Organization`
            An object representing an Organization on Labstep.

        Example
        -------
        ::

            organization = user.getOrganization()
        """
        import labstep.entities.organization.repository as organizationRepository

        self.update()

        if len(self.user_organizations) > 0:

            organizationId = self.user_organizations[0]['organization']['id']

            return organizationRepository.getOrganization(self, organizationId)

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
        import labstep.entities.file.repository as fileRepository

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
        import labstep.entities.device.repository as deviceRepository

        return deviceRepository.getDevice(self, device_id)

    # getMany()

    def getExperiments(
        self,
        count=UNSPECIFIED,
        search_query=UNSPECIFIED,
        created_at_from=UNSPECIFIED,
        created_at_to=UNSPECIFIED,
        tag_id=UNSPECIFIED,
        collection_id=UNSPECIFIED,
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
        import labstep.entities.experiment.repository as experimentRepository

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
        count=UNSPECIFIED,
        search_query=UNSPECIFIED,
        created_at_from=UNSPECIFIED,
        created_at_to=UNSPECIFIED,
        tag_id=UNSPECIFIED,
        collection_id=UNSPECIFIED,
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
        import labstep.entities.protocol.repository as protocolRepository

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

    def getResources(self, count=UNSPECIFIED, search_query=UNSPECIFIED, resource_category_id=UNSPECIFIED, tag_id=UNSPECIFIED, extraParams={}):
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
        resource_category_id (int)
            Search for Resources in a particular category.
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
                                       resource_category_id=123,
                                       tag_id=800)
        """
        import labstep.entities.resource.repository as resourceRepository

        return resourceRepository.getResources(
            self,
            count=count,
            search_query=search_query,
            tag_id=tag_id,
            resource_category_id=resource_category_id,
            extraParams=extraParams,
        )

    def getResourceCategorys(
        self, count=UNSPECIFIED, search_query=UNSPECIFIED, tag_id=UNSPECIFIED, extraParams={}
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
        import labstep.entities.resourceCategory.repository as resourceCategoryRepository

        return resourceCategoryRepository.getResourceCategorys(
            self,
            count=count,
            search_query=search_query,
            tag_id=tag_id,
            extraParams=extraParams,
        )

    def getResourceLocations(self, count=UNSPECIFIED, search_query=UNSPECIFIED, extraParams={}):
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
        import labstep.entities.resourceLocation.repository as resourceLocationRepository

        return resourceLocationRepository.getResourceLocations(
            self, count=count, search_query=search_query, extraParams=extraParams
        )

    def getResourceItems(self, count=UNSPECIFIED, search_query=UNSPECIFIED, extraParams={}):
        """
        Retrieve a list of a user's ResourceItems on Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of ResourceItems to retrieve.
        search_query (str)
            Search for ResourceItems with this 'name'.

        Returns
        -------
        List[:class:`~labstep.entities.resourceItem.model.ResourceItem`]
            A list of ResourceItem objects.

        Example
        -------
        ::

            entity = user.getResourceItems(search_query='batch #5')
        """
        import labstep.entities.resourceItem.repository as resourceItemRepository

        return resourceItemRepository.getResourceItems(
            self, count=count, search_query=search_query, extraParams=extraParams
        )

    def getOrderRequests(
        self, count=UNSPECIFIED, search_query=UNSPECIFIED, status=UNSPECIFIED, tag_id=UNSPECIFIED, extraParams={}
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
        import labstep.entities.orderRequest.repository as orderRequestRepository

        return orderRequestRepository.getOrderRequests(
            self,
            count=count,
            search_query=search_query,
            status=status,
            tag_id=tag_id,
            extraParams=extraParams,
        )

    def getTags(self, count=UNSPECIFIED, search_query=UNSPECIFIED, type=UNSPECIFIED, extraParams={}):
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
        import labstep.entities.tag.repository as tagRepository

        return tagRepository.getTags(
            self,
            count=count,
            type=type,
            search_query=search_query,
            extraParams=extraParams,
        )

    def getWorkspaces(self, count=UNSPECIFIED, search_query=UNSPECIFIED, extraParams={}):
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
        import labstep.entities.workspace.repository as workspaceRepository

        return workspaceRepository.getWorkspaces(
            self, count=count, search_query=search_query, extraParams=extraParams
        )

    @deprecated(version='3.0.3', reason="You should use workspace.getFiles instead")
    def getFiles(self, count=UNSPECIFIED, search_query=UNSPECIFIED, file_type=UNSPECIFIED, extraParams={}):
        return []

    def getDevices(self, count=UNSPECIFIED, search_query=UNSPECIFIED, extraParams={}):
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
        import labstep.entities.device.repository as deviceRepository

        return deviceRepository.getDevices(
            self, count=count, search_query=search_query, extraParams=extraParams
        )

    # newEntity()

    def newExperiment(self, name, entry=UNSPECIFIED, template_id=UNSPECIFIED,extraParams={}):
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
        import labstep.entities.experiment.repository as experimentRepository
        extraParams={'source_id': template_id,
                     **extraParams}
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
        import labstep.entities.protocol.repository as protocolRepository

        return protocolRepository.newProtocol(self, name, extraParams=extraParams)

    def newResource(self, name, resource_category_id=UNSPECIFIED, extraParams={}):
        """
        Create a new Labstep Resource.

        Parameters
        ----------
        name (str)
            Give your Resource a name.

        resource_category_id (int)
            ID of the resource category of the new resource

        Returns
        -------
        :class:`~labstep.entities.resource.model.Resource`
            An object representing a Resource on Labstep.

        Example
        -------
        ::

            entity = user.newResource(name='salicylic acid')
        """
        import labstep.entities.resource.repository as resourceRepository

        return resourceRepository.newResource(self, name, resource_category_id=resource_category_id, extraParams=extraParams)

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
        import labstep.entities.resourceCategory.repository as resourceCategoryRepository

        return resourceCategoryRepository.newResourceCategory(
            self, name, extraParams=extraParams
        )

    def newResourceLocation(self, name, outer_location_guid=UNSPECIFIED, extraParams={}):
        """
        Create a new Labstep ResourceLocation.

        Parameters
        ----------
        name (str)
            Give your ResourceLocation a name.

        outer_location_guid (str)
            The guid of existing location to create the location within

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
        import labstep.entities.resourceLocation.repository as resourceLocationRepository

        return resourceLocationRepository.newResourceLocation(
            self, name, outer_location_guid=outer_location_guid, extraParams=extraParams
        )

    def newOrderRequest(self, resource_id, purchase_order_id=UNSPECIFIED, quantity=1, extraParams={}):
        """
        Create a new Labstep OrderRequest.

        Parameters
        ----------
        resource_id (int)
            The id of the :class:`~labstep.entities.resource.model.Resource`
            to request more items of.

        purchase_order_id (int)
            The id of the :class:`~labstep.entities.purchaseOrder.model.PurchaseOrder`

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
        import labstep.entities.orderRequest.repository as orderRequestRepository

        return orderRequestRepository.newOrderRequest(
            self, resource_id=resource_id, purchase_order_id=purchase_order_id, quantity=quantity, extraParams=extraParams
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
        import labstep.entities.tag.repository as tagRepository

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
        import labstep.entities.workspace.repository as workspaceRepository

        return workspaceRepository.newWorkspace(self, name, extraParams=extraParams)

    def newFile(self, filepath=UNSPECIFIED, rawData=UNSPECIFIED, extraParams={}):
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
        import labstep.entities.file.repository as fileRepository

        return fileRepository.newFile(self, filepath, rawData=rawData, extraParams=extraParams)

    def newCollection(self, name, type="experiment", extraParams={}):
        """
        Create a new Collection for Experiments (or Protocols)

        Parameters
        ----------
        type (str)
            The type of collection to create ("experiment" or "protocol")
        """
        import labstep.entities.collection.repository as collectionRepository

        return collectionRepository.newCollection(self, name=name, type=type, extraParams=extraParams)

    def newDevice(self, name, extraParams={}, device_category_id=UNSPECIFIED):
        """
        Create a new Labstep Device.

        Parameters
        ----------
        name (str)
            Give your Device a name.

        device_category_id (int)
            The ID of a device category.

        Returns
        -------
        :class:`~labstep.entities.device.model.Device`
            An object representing a Device on Labstep.

        Example
        -------
        ::

            entity = user.newDevice(name='Microscope A')
        """
        import labstep.entities.device.repository as deviceRepository

        return deviceRepository.newDevice(self, name, extraParams, device_category_id=device_category_id)

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
        url = url_join(configService.getHost(), "/api/generic/",
                       "share-link", 'accept', token)
        requestService.post(url, headers=headers)
        return None

    def getJupyterInstance(self, jupyterInstanceGuid):
        """
        Retrieve a specific Labstep Jupyter Instance.

        Parameters
        ----------
        jupyterInstanceGuid (string)
            The JupyterInstance guid.

        Returns
        -------
        :class:`~labstep.entities.jupyterInstance.model.JupyterInstance`
            An object representing a JupyterInstance on Labstep.

        Example
        -------
        ::

            entity = user.getJupyterInstance("872b3e7e-e21f-4403-9ef3-3650fe0d86ba")
        """
        import labstep.entities.jupyterInstance.repository as jupyterInstanceRepository

        return jupyterInstanceRepository.getJupyterInstance(self, jupyterInstanceGuid)

    def getJupyterNotebook(self, jupyterNotebookGuid):
        """
        Retrieve a specific Labstep Jupyter Notebook.

        Parameters
        ----------
        jupyterNotebookGuid (string)
            The JupyterNotebook guid.

        Returns
        -------
        :class:`~labstep.entities.jupyterNotebook.model.JupyterNotebook`
            An object representing a JupyterNotebook on Labstep.

        Example
        -------
        ::

            entity = user.getJupyterNotebook("872b3e7e-e21f-4403-9ef3-3650fe0d86ba")
        """
        import labstep.entities.jupyterNotebook.repository as jupyterNotebookRepository

        return jupyterNotebookRepository.getJupyterNotebook(self, jupyterNotebookGuid)

    def newDeviceCategory(self, name, extraParams={}):
        """
        Create a new Labstep DeviceCategory.

        Parameters
        ----------
        name (str)
            Give your DeviceCategory a name.

        Returns
        -------
        :class:`~labstep.entities.resourceCategory.model.DeviceCategory`
            An object representing the new Labstep DeviceCategory.

        Example
        -------
        ::

            entity = user.newDeviceCategory(name='Printer')
        """
        import labstep.entities.deviceCategory.repository as deviceCategoryRepository

        return deviceCategoryRepository.newDeviceCategory(
            self, name, extraParams=extraParams
        )

    def getDeviceCategorys(
        self, count=UNSPECIFIED, search_query=UNSPECIFIED, tag_id=UNSPECIFIED, extraParams={}
    ):
        """
        Retrieve a list of a User's Device Categorys
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
        List[:class:`~labstep.entities.resourceCategory.model.DeviceCategory`]
            A list of Labstep DeviceCategorys.

        Example
        -------
        ::

            entity = user.getDeviceCategorys(search_query='properties',
                                               tag_id=800)
        """
        import labstep.entities.deviceCategory.repository as deviceCategoryRepository

        return deviceCategoryRepository.getDeviceCategorys(
            self,
            count=count,
            search_query=search_query,
            tag_id=tag_id,
            extraParams=extraParams,
        )

    def getDeviceCategory(self, device_category_id):
        """
        Retrieve a specific Labstep DeviceCategory.

        Parameters
        ----------
        device_category_id (int)
            The id of the DeviceCategory to retrieve.

        Returns
        -------
        :class:`~labstep.entities.deviceCategory.model.DeviceCategory`
            An object representing a DeviceCategory on Labstep.

        Example
        -------
        ::

            entity = user.getDeviceCategory(17000)
        """
        import labstep.entities.deviceCategory.repository as deviceCategoryRepository

        return deviceCategoryRepository.getDeviceCategory(
            self, device_category_id
        )

    def newAPIKey(self, name, expires_at=UNSPECIFIED, extraParams={}):
        """
        Create a new API Key.

        Parameters
        ----------
        name (str)
            Name of the new API Key.

        Returns
        -------
        :class:`~labstep.entities.apiKey.model.ApiKey`
            An object representing the new Labstep ApiKey.

        Example
        -------
        ::

            entity = user.newAPIKey(name='Access Key')
        """
        import labstep.entities.apiKey.repository as apiKeyRepository

        return apiKeyRepository.newAPIKey(
            self, name, expires_at, extraParams=extraParams
        )

    def getAPIKey(self, APIKey_id, extraParams={}):
        """
        Create a new API Key.

        Parameters
        ----------
        APIKey_id (int)
            ID of the API Key.

        Returns
        -------
        :class:`~labstep.entities.apiKey.model.ApiKey`
            An object representing the new Labstep ApiKey.

        Example
        -------
        ::

            entity = user.getAPIKey(100000000)
        """
        import labstep.entities.apiKey.repository as apiKeyRepository

        return apiKeyRepository.getAPIKey(
            self, APIKey_id
        )

    def getAPIKeys(
        self, count=UNSPECIFIED, api_key=UNSPECIFIED, search_query=UNSPECIFIED, extraParams={}
    ):
        """
        Retrieve a list of a User's API keys.

        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of API keys to retrieve.
        search_query (str)
            Search for API keys with this 'name'.
        api_key (str)
            Search for API keys with this 'api_key'.

        Returns
        -------
        List[:class:`~labstep.entities.apiKey.model.apiKey`]
            A list of Labstep API keys.

        Example
        -------
        ::

            entity = user.getAPIKeys(api_key='111f321dafd0d0sa')
        """
        import labstep.entities.apiKey.repository as ApiKeyRepository

        return ApiKeyRepository.getAPIKeys(
            self,
            count=count,
            api_key=api_key,
            search_query=search_query,
            extraParams=extraParams,
        )

    def getNotifications(self, count=UNSPECIFIED, notification_type=UNSPECIFIED):
        """
        Retrieve a list of the User's notifications which can be filtered using the parameters

        Parameters
        ----------
        count(int)
            The number of Notifications to retrieve.

        type (str)
            The type of the Notifications to retrieve. Notification type can be of 'Workspace', 'Experiment',
            'Protocol', 'Jupyter Instance', 'Device', 'Order request', 'Order', 'Resource', 'Item resource',
            or 'Resource Location'.

        Returns
        -------
        List[:class:`~labstep.entities.workspace.model.Workspace`]
            A list of Notification entities in Labstep.

        Example
        -------
        ::

            entities = user.getNotifications()
        """
        import labstep.entities.notification.repository as notificationRepository

        return notificationRepository.getNotifications(self, count=count, notification_type=notification_type)

    def getNotification(self, id):
        """
        Retrieve a Notification entity in Labstep.

        Parameters
        ----------
        guid (str)
            Guid of the comment entity to retrieve.

        Returns
        -------
        :class:`~labstep.entities.notificaction.model.Notification`
            An object representing a Notification on Labstep.

        Example
        -------
        ::

            entity = user.getNotification(guid='100000')
        """
        import labstep.entities.notification.repository as notificationRepository

        return notificationRepository.getNotification(self, id=id)

    def newPurchaseOrder(self ,name=UNSPECIFIED, status=UNSPECIFIED, currency='USD', extraParams={}):
        """
        Create a new Labstep Purchase Order.

        Parameters
        ----------
        name (str)
            The name of the Purchase Order.
        status (str)
            The status of the Purchase Order. Options are: "open", "pending",
            and "completed".
        currency (str)
            The currency of the price in the format of the 3-letter
            currency code by country. For example, "EUR" for Euro, "GBP" for
            British Pound Sterling, "USD" for US Dollar, etc.

        Returns
        -------
        :class:`~labstep.entities.purchaseOrder.model.PurchaseOrder`
            An object representing the an PurchaseOrder on Labstep.

        Example
        -------
        ::

            my_purchase_order = user.newPurchaseOrder()

        """
        import labstep.entities.purchaseOrder.repository as PurchaseOrderRepository

        return PurchaseOrderRepository.newPurchaseOrder(
            self, name=name, status=status, currency=currency, extraParams=extraParams
        )

    def getPurchaseOrder(self ,purchase_order_id, extraParams={}):
        """
        Get an existing Labstep Purchase Order.

        Parameters
        ----------
        purchase_order_id (int)
            The ID of the Purchase Order.


        Returns
        -------
        :class:`~labstep.entities.purchaseOrder.model.PurchaseOrder`
            An object representing the an PurchaseOrder on Labstep.

        Example
        -------
        ::

            my_purchase_order = user.getPurchaseOrder(17000)
        """
        import labstep.entities.purchaseOrder.repository as PurchaseOrderRepository

        return PurchaseOrderRepository.getPurchaseOrder(
            self, purchase_order_id=purchase_order_id,extraParams=extraParams)

    def getPurchaseOrders(self ,
                        count=UNSPECIFIED,
                        status=UNSPECIFIED,
                        extraParams={}):
        """
        Get an existing Labstep Purchase Order.

        Parameters
        ----------
        count(int)
            The number of Purchase Order entities to retrieve.

        status (str)
            The status of the Purchase Order. Options are: "open", "pending",
            and "completed".


        Returns
        -------
        :class:`~labstep.entities.purchaseOrder.model.PurchaseOrder`
            An object representing the an PurchaseOrder on Labstep.

        Example
        -------
        ::

            my_purchase_order = user.getPurchaseOrders()
        """
        import labstep.entities.purchaseOrder.repository as PurchaseOrderRepository

        return PurchaseOrderRepository.getPurchaseOrders(
            self, count=count,status=status, extraParams=extraParams)

    def newExperimentTemplate(self, name,entry=UNSPECIFIED, entity_state_workflow_id=UNSPECIFIED, extraParams={}):
        """
        Create a new Labstep Experiment Template.

        Parameters
        ----------
        name (str)
            Give your Experiment Template a name.

        entry (obj)
            A JSON object representing the state of the Experiment Entry.

        entity_state_workflow_id (int)
            The ID of the EntityStateWorkflow to associate with the Experiment Template.

        Returns
        -------
        :class:`~labstep.entities.experimentTemplate.model.ExperimentTemplate`
            An object representing an Experiment Template on Labstep.

        Example
        -------
        ::

            entity = user.newExperimentTemplate(name='The Synthesis of Aspirin')
        """
        import labstep.entities.experimentTemplate.repository as experimentTemplateRepository

        return experimentTemplateRepository.newExperimentTemplate(
            self, name,entry=entry, entity_state_workflow_id=entity_state_workflow_id, extraParams=extraParams
        )

    def getExperimentTemplate(self, experiment_template_id):
        """
        Retrieve a specific Labstep Experiment Template.

        Parameters
        ----------
        experiment_template_id (int)
            The id of the Experiment Template to retrieve.

        Returns
        -------
        :class:`~labstep.entities.experimentTemplate.model.ExperimentTemplate`
            An object representing an Experiment Template on Labstep.

        Example
        -------
        ::

            entity = user.getExperimentTemplate(17000)
        """
        import labstep.entities.experimentTemplate.repository as experimentTemplateRepository

        return experimentTemplateRepository.getExperimentTemplate(self, experiment_template_id)

    def getExperimentTemplates(
        self,
        count=UNSPECIFIED,
        search_query=UNSPECIFIED,
        extraParams={},
    ):
        """
        Retrieve a list of a User's Experiment Templates
        across different Workspaces on Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of Experiment Templates to retrieve.
        search_query (str)
            Search for Experiment Templates containing this string in the name.

        Returns
        -------
        List[:class:`~labstep.entities.experimentTemplate.model.ExperimentTemplate`]
            A list of Labstep Experiment Templates.

        Example
        -------
        ::

            entity = user.getExperimentTemplates(search_query='bacteria')
        """
        import labstep.entities.experimentTemplate.repository as experimentTemplateRepository

        return experimentTemplateRepository.getExperimentTemplates(
            self,
            count=count,
            search_query=search_query,
            extraParams=extraParams,
        )

    def newEntityStateWorkflow(self, name, extraParams={}):
        """
        Create a new Labstep Entity State Workflow.

        Parameters
        ----------
        name (str)
            Give your Entity State Workflow a name.

        Returns
        -------
        :class:`~labstep.entities.entityStateWorkflow.model.EntityStateWorkflow`
            An object representing an Entity State Workflow on Labstep.

        Example
        -------
        ::

            entity = user.newEntityStateWorkflow(name='The Synthesis of Aspirin')
        """
        import labstep.entities.entityStateWorkflow.repository as entityStateWorkflowRepository

        return entityStateWorkflowRepository.newEntityStateWorkflow(
            self, name, group_id=self.activeWorkspace, extraParams=extraParams
        )

    def getEntityStateWorkflow(self, entity_state_workflow_id):
        """
        Retrieve a specific Labstep Entity State Workflow.

        Parameters
        ----------
        entity_state_workflow_id (int)
            The id of the Entity State Workflow to retrieve.

        Returns
        -------
        :class:`~labstep.entities.entityStateWorkflow.model.EntityStateWorkflow`
            An object representing an Entity State Workflow on Labstep.

        Example
        -------
        ::

            entity = user.getEntityStateWorkflow(17000)
        """
        import labstep.entities.entityStateWorkflow.repository as entityStateWorkflowRepository

        return entityStateWorkflowRepository.getEntityStateWorkflow(self, entity_state_workflow_id)

    def getEntityStateWorkflows(
        self,
        count=UNSPECIFIED,
        search_query=UNSPECIFIED,
        extraParams={},
    ):
        """
        Retrieve a list of a User's Entity State Workflows
        across different Workspaces on Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of Entity State Workflows to retrieve.
        search_query (str)
            Search for Entity State Workflows containing this string in the name.

        Returns
        -------
        List[:class:`~labstep.entities.entityStateWorkflow.model.EntityStateWorkflow`]
            A list of Labstep Entity State Workflows.

        Example
        -------
        ::

            entity = user.getEntityStateWorkflows(search_query='bacteria')
        """
        import labstep.entities.entityStateWorkflow.repository as entityStateWorkflowRepository

        return entityStateWorkflowRepository.getEntityStateWorkflows(
            self,
            count=count,
            search_query=search_query,
            extraParams=extraParams,
        )