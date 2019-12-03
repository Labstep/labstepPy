#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from .config import API_ROOT
from .helpers import url_join, handleError, showAttributes
from .experiment import getExperiment, getExperiments, newExperiment
from .protocol import getProtocol, getProtocols, newProtocol
from .resource import getResource, getResources, newResource
from .resourceItem import getResourceItem, getResourceItems, newResourceItem
from .resourceCategory import (getResourceCategory, getResourceCategorys,
                               newResourceCategory)
from .resourceLocation import getResourceLocations, newResourceLocation
from .orderRequest import getOrderRequest, getOrderRequests, newOrderRequest
from .tag import getTags, newTag
from .workspace import getWorkspace, getWorkspaces, newWorkspace
from .file import newFile


def login(username, password):
    """
    Returns an authenticated Labstep User object to allow
    you to interact with the Labstep API.

    Parameters
    ----------
    username (str)
        Your Labstep username.
    password (obj)
        Your Labstep password.

    Returns
    -------
    :class:`~labstep.user.User`
        An object representing a user on Labstep.

    Example
    -------
    .. code-block::

        user = labstep.login('myaccount@labstep.com', 'mypassword')
    """
    fields = {'username': username,
              'password': password}
    url = url_join(API_ROOT, "/public-api/user/login")
    r = requests.post(url, json=fields, headers={})
    handleError(r)
    return User(json.loads(r.content))


class User:
    def __init__(self, user):
        self.activeWorkspace = user['group']['id']
        for key in user:
            setattr(self, key, user[key])

    def attributes(self):
        """
        Show all attributes of the User.

        Example
        -------
        .. code-block::

            user.attributes()

        The output should look something like this:

        .. program-output:: python ../labstep/attributes/user_attributes.py

        To inspect specific attributes of the user,
        for example, the user's 'username', 'activeWorkspace', etc.:

        .. code-block::

            print(user.username)
            print(user.activeWorkspace)
        """
        return showAttributes(self)

    def setWorkspace(self, workspace):
        """
        Set a Workspace as the active Workspace.

        Parameters
        ----------
        workspace (obj)
            The Workspace to set as active.

        Returns
        -------
        :class:`~labstep.workspace.Workspace`
            An object representing a Workspace on Labstep.

        Example
        -------
        .. code-block::

            entity = user.getWorkspace(17000)
            my_workspace = user.setWorkspace(entity)
        """
        self.activeWorkspace = workspace.id

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
        :class:`~labstep.experiment.Experiment`
            An object representing an Experiment on Labstep.

        Example
        -------
        .. code-block::

            entity = user.getExperiment(17000)
        """
        return getExperiment(self, experiment_id)

    def getProtocol(self, protocol_id):
        """
        Retrieve a specific Labstep Protocol.

        Parameters
        ----------
        protocol_id (int)
            The id of the Protocol to retrieve.

        Returns
        -------
        :class:`~labstep.protocol.Protocol`
            An object representing a Protocol on Labstep.

        Example
        -------
        .. code-block::

            entity = user.getProtocol(17000)
        """
        return getProtocol(self, protocol_id)

    def getResource(self, resource_id):
        """
        Retrieve a specific Labstep Resource.

        Parameters
        ----------
        resource_id (int)
            The id of the Resource to retrieve.

        Returns
        -------
        :class:`~labstep.resource.Resource`
            An object representing a Resource on Labstep.

        Example
        -------
        .. code-block::

            entity = user.getResource(17000)
        """
        return getResource(self, resource_id)

    def getResourceItem(self, resourceItem_id):
        """
        Retrieve a specific Labstep ResourceItem.

        Parameters
        ----------
        resourceItem_id (int)
            The id of the ResourceItem to retrieve.

        Returns
        -------
        :class:`~labstep.resourceItem.ResourceItem`
            An object representing a ResourceItem on Labstep.

        Example
        -------
        .. code-block::

            entity = user.getResourceItem(17000)
        """
        return getResourceItem(self, resourceItem_id)

    def getResourceCategory(self, resourceCategory_id):
        """
        Retrieve a specific Labstep ResourceCategory.

        Parameters
        ----------
        resourceCategory_id (int)
            The id of the ResourceCategory to retrieve.

        Returns
        -------
        :class:`~labstep.resourceCategory.ResourceCategory`
            An object representing a ResourceCategory on Labstep.

        Example
        -------
        .. code-block::

            entity = user.getResourceCategory(17000)
        """
        return getResourceCategory(self, resourceCategory_id)

    def getOrderRequest(self, order_request_id):
        """
        Retrieve a specific Labstep OrderRequest.

        Parameters
        ----------
        order_request_id (int)
            The id of the OrderRequest to retrieve.

        Returns
        -------
        :class:`~labstep.orderRequest.OrderRequest`
            An object representing a OrderRequest on Labstep.

        Example
        -------
        .. code-block::

            entity = user.getOrderRequest(17000)
        """
        return getOrderRequest(self, order_request_id)

    def getWorkspace(self, workspace_id):
        """
        Retrieve a specific Labstep Workspace.

        Parameters
        ----------
        workspace_id (int)
            The id of the Workspace to retrieve.

        Returns
        -------
        :class:`~labstep.workspace.Workspace`
            An object representing a Workspace on Labstep.

        Example
        -------
        .. code-block::

            entity = user.getWorkspace(17000)
        """
        return getWorkspace(self, workspace_id)

    # getMany()
    def getExperiments(self, count=100, search_query=None,
                       created_at_from=None, created_at_to=None, tag_id=None):
        """
        Retrieve a list of a User's Experiments
        across all Workspaces on Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of Experiments to retrieve.
        search_query (str)
            Search for Experiments with this 'name'.
        created_at_from (str)
            The start date of the search range, must be
            in the format of 'YYYY-MM-DD'.
        created_at_to (str)
            The end date of the search range, must be
            in the format of 'YYYY-MM-DD'.
        tag_id (int)
            The id of the Tag to retrieve.

        Returns
        -------
        List[:class:`~labstep.experiment.Experiment`]
            A list of Labstep Experiments.

        Example
        -------
        .. code-block::

            entity = user.getExperiments(search_query='bacteria',
                                         created_at_from='2019-01-01',
                                         created_at_to='2019-01-31',
                                         tag_id=800)
        """
        return getExperiments(self, count, search_query,
                              created_at_from, created_at_to, tag_id)

    def getProtocols(self, count=100, search_query=None,
                     created_at_from=None, created_at_to=None, tag_id=None):
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
            The id of the Tag to retrieve.

        Returns
        -------
        List[:class:`~labstep.protocol.Protocol`]
            A list of Labstep Protocols.

        Example
        -------
        .. code-block::

            entity = user.getProtocols(search_query='bacteria',
                                       created_at_from='2019-01-01',
                                       created_at_to='2019-01-31',
                                       tag_id=800)
        """
        return getProtocols(self, count, search_query, created_at_from,
                            created_at_to, tag_id)

    def getResources(self, count=100, search_query=None, tag_id=None):
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
            The id of the Tag to retrieve.

        Returns
        -------
        List[:class:`~labstep.resource.Resource`]
            A list of Labstep Resources.

        Example
        -------
        .. code-block::

            entity = user.getResources(search_query='bacteria',
                                       tag_id=800)
        """
        return getResources(self, count, search_query, tag_id)

    def getResourceItems(self, resource, count=100, search_query=None):
        """
        Retrieve a list of a User's ResourceItems
        across all Workspaces on Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        resource (obj)
            The Resource to retrieve the ResourceItems for.
        count (int)
            The number of ResourceItems to retrieve.
        search_query (str)
            Search for ResourceItems with this 'name'.

        Returns
        -------
        List[:class:`~labstep.resourceItems.ResourceItems`]
            A list of ResourceItem objects.

        Example
        -------
        .. code-block::

            entity = user.getResourceItems(search_query="acid")
        """
        return getResourceItems(self, resource, count, search_query)

    def getResourceCategorys(self, count=100, search_query=None, tag_id=None):
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
            The id of the Tag to retrieve.

        Returns
        -------
        List[:class:`~labstep.resourceCategory.ResourceCategory`]
            A list of Labstep ResourceCategorys.

        Example
        -------
        .. code-block::

            entity = user.getResourceCategorys(search_query='properties',
                                               tag_id=800)
        """
        return getResourceCategorys(self, count, search_query, tag_id)

    def getResourceLocations(self, count=100, search_query=None, tag_id=None):
        """
        Retrieve a list of a user's ResourceLocations on Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of ResourceLocations to retrieve.
        search_query (str)
            Search for ResourceLocations with this 'name'.
        tag_id (int)
            The id of the Tag to retrieve.

        Returns
        -------
        List[:class:`~labstep.resourceLocation.ResourceLocation`]
            A list of ResourceLocation objects.

        Example
        -------
        .. code-block::

            entity = user.getResourceLocations(search_query='properties',
                                               tag_id=800)
        """
        return getResourceLocations(self, count, search_query, tag_id)

    def getOrderRequests(self, count=100, name=None):
        """
        Retrieve a list of a user's OrderRequests on Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of OrderRequests to retrieve.
        name (str)
            Search for OrderRequests with this 'name'.

        Returns
        -------

        List[:class:`~labstep.orderRequest.OrderRequest`]
            A list of Labstep OrderRequests.

        Example
        -------
        .. code-block::

            entity = user.getOrderRequests(name='polymerase')
        """
        return getOrderRequests(self, count, name)

    def getTags(self, count=1000, search_query=None):
        """
        Retrieve a list of a User's Tags
        across all Workspaces on Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of Tags to retrieve.
        search_query (str)
            Search for Tags with this 'name'.

        Returns
        -------
        List[:class:`~labstep.tag.Tag`]
            A list of Labstep Tags.

        Example
        -------
        .. code-block::

            entity = user.getTags(search_query='bacteria')
        """
        return getTags(self, count, search_query)

    def getWorkspaces(self, count=100, name=None):
        """
        Retrieve a list of a user's Workspaces on Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of Workspaces to retrieve.
        name (str)
            Search for Workspaces with this 'name'.

        Returns
        -------

        List[:class:`~labstep.workspace.Workspace`]
            A list of Labstep Workspaces.

        Example
        -------
        .. code-block::

            entity = user.getWorkspaces(name='bacteria')
        """
        return getWorkspaces(self, count, name)

    # newEntity()
    def newExperiment(self, name, description=None):
        """
        Create a new Labstep Experiment.

        Parameters
        ----------
        name (str)
            Give your Experiment a name.
        description (str)
            Give your Experiment a description.

        Returns
        -------
        :class:`~labstep.experiment.Experiment`
            An object representing an Experiment on Labstep.

        Example
        -------
        .. code-block::

            entity = user.newExperiment(name='The Synthesis of Aspirin',
                                        description='Aspirin is an analgesic
                                        used to reduce pain.')
        """
        return newExperiment(self, name, description)

    def newProtocol(self, name):
        """
        Create a new Labstep Protocol.

        Parameters
        ----------
        name (str)
            Give your Protocol a name.

        Returns
        -------
        :class:`~labstep.protocol.Protocol`
            An object representing a Protocol on Labstep.

        Example
        -------
        .. code-block::

            entity = user.newProtocol(name='Synthesising Aspirin')
        """
        return newProtocol(self, name)

    def newResource(self, name):
        """
        Create a new Labstep Resource.

        Parameters
        ----------
        name (str)
            Give your Resource a name.

        Returns
        -------
        :class:`~labstep.resource.Resource`
            An object representing a Resource on Labstep.

        Example
        -------
        .. code-block::

            entity = user.newResource(name='salicylic acid')
        """
        return newResource(self, name)

    def newResourceItem(self, resource, name=None, availability=None,
                        quantity_amount=None, quantity_unit=None,
                        location=None):
        """
        Create a new Labstep ResourceItem.

        Parameters
        ----------
        resource (obj)
            The Resource to add a new ResourceItem to.
        name (str)
            The new name of the ResourceItem.
        availability (str)
            The status of the ResourceItem. Options are:
            "available" and "unavailable".
        quantity_amount (float)
            The quantity of the ResourceItem.
        quantity_unit (str)
            The unit of the quantity.
        location (obj)
            The ResourceLocation of the ResourceItem.

        Returns
        -------
        :class:`~labstep.resourceItem.ResourceItem`
            An object representing a ResourceItem on Labstep.

        Example
        -------
        .. code-block::

            # Get a Resource
            my_resource = user.getResource(17000)

            # Get a ResourceLocation
            my_location = user.getResourceLocations()[2]

            # Create a new ResourceItem for my_resource
            entity = user.newResourceItem(my_resource, name='Acetic Acid 10%',
                                          availability='unavailable',
                                          quantity_amount=250,
                                          quantity_unit='ml',
                                          location=my_location)
        """
        return newResourceItem(self, resource, name, availability,
                               quantity_amount, quantity_unit,
                               location)

    def newResourceCategory(self, name):
        """
        Create a new Labstep ResourceCategory.

        Parameters
        ----------
        name (str)
            Give your ResourceCategory a name.

        Returns
        -------
        :class:`~labstep.resourceCategory.ResourceCategory`
            An object representing the new Labstep ResourceCategory.
        """
        return newResourceCategory(self, name)

    def newResourceLocation(self, name):
        """
        Create a new Labstep ResourceLocation.

        Parameters
        ----------
        name (str)
            Give your ResourceLocation a name.

        Returns
        -------
        :class:`~labstep.resourceLocation.ResourceLocation`
            An object representing the new Labstep ResourceLocation.
        """
        return newResourceLocation(self, name)

    def newOrderRequest(self, resource, quantity=1):
        """
        Create a new Labstep OrderRequest.

        Parameters
        ----------
        resource (obj)
            The Labstep Resource.
        quantity (int)
            The quantity of the new OrderRequest.

        Returns
        -------
        :class:`~labstep.orderRequest.OrderRequest`
            An object representing the an OrderRequest on Labstep.

        Example
        -------
        .. code-block::

            my_resource = user.getResource(17000)
            entity = user.newOrderRequest(my_resource, quantity=2)
        """
        return newOrderRequest(self, resource, quantity)

    def newTag(self, name):
        """
        Create a new Labstep Tag.

        Parameters
        ----------
        name (str)
            Give your Tag a name.

        Returns
        -------
        :class:`~labstep.tag.Tag`
            An object representing a Tag on Labstep.

        Example
        -------
        .. code-block::

            entity = user.newTag(name='Aspirin')
        """
        return newTag(self, name)

    def newWorkspace(self, name):
        """
        Create a new Labstep Workspace.

        Parameters
        ----------
        name (str)
            Give your Workspace a name.

        Returns
        -------
        :class:`~labstep.workspace.Workspace`
            An object representing a Workspace on Labstep.

        Example
        -------
        .. code-block::

            entity = user.newWorkspace(name='Aspirin Project')
        """
        return newWorkspace(self, name)

    def newFile(self, filepath):
        """
        Upload a file to the Labstep entity Data.

        Parameters
        ----------
        filepath (str)
            The filepath to the file to attach.

        Example
        -------
        .. code-block::

            entity = user.newFile('./structure_of_aspirin.png')
        """
        return newFile(self, filepath)
