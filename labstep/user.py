#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import urllib.parse

from .config import API_ROOT
from .entity import Entity
from .helpers import url_join, handleError
from .experiment import getExperiment, getExperiments, newExperiment
from .protocol import getProtocol, getProtocols, newProtocol
from .resource import getResource, getResources, newResource
from .resourceCategory import (getResourceCategory, getResourceCategorys,
                               newResourceCategory)
from .resourceLocation import getResourceLocations, newResourceLocation
from .orderRequest import getOrderRequest, getOrderRequests, newOrderRequest
from .tag import getTags, newTag
from .workspace import getWorkspace, getWorkspaces, newWorkspace
from .file import newFile


def authenticate(username, apikey):
    """
    Returns an authenticated Labstep User object to allow
    you to interact with the Labstep API.

    Parameters
    ----------
    username (str)
        Your Labstep username.
    apikey (str)
        An apikey for the user.

    Returns
    -------
    :class:`~labstep.user.User`
        An object representing a user on Labstep.

    Example
    -------
    ::

        import labstep

        user = labstep.authenticate('myaccount@labstep.com', 'MY_API_KEY')
    """
    url = url_join(API_ROOT, "api/generic/user", urllib.parse.quote(username))
    r = requests.get(url, headers={'apikey': apikey})
    handleError(r)
    user = json.loads(r.content)
    user['api_key'] = apikey
    return User(user)


def login(username, password):
    """
    Returns an authenticated Labstep User object to allow
    you to interact with the Labstep API.

    Parameters
    ----------
    username (str)
        Your Labstep username.
    password (str)
        Your Labstep password.

    Returns
    -------
    :class:`~labstep.user.User`
        An object representing a user on Labstep.

    Example
    -------
    ::

        import labstep

        user = labstep.login('myaccount@labstep.com', 'mypassword')
    """
    fields = {'username': username,
              'password': password}
    url = url_join(API_ROOT, "/public-api/user/login")
    r = requests.post(url, json=fields, headers={})
    handleError(r)
    return User(json.loads(r.content))


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
        self.activeWorkspace = user['group']['id']
        for key in user:
            setattr(self, key, user[key])

    def setWorkspace(self, workspace_id):
        """
        Set a Workspace as the active Workspace.

        Parameters
        ----------
        workspace_id (int)
            The id of the Workspace to set as active.

        Returns
        -------
        :class:`~labstep.workspace.Workspace`
            An object representing a Workspace on Labstep.

        Example
        -------
        ::

            entity = user.getWorkspace(17000)
            user.setWorkspace(entity.id)
        """
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
        :class:`~labstep.experiment.Experiment`
            An object representing an Experiment on Labstep.

        Example
        -------
        ::

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
        ::

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
        ::

            entity = user.getResource(17000)
        """
        return getResource(self, resource_id)

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
        ::

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
        ::

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
        ::

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
            The id of a tag to filter by.

        Returns
        -------
        List[:class:`~labstep.experiment.Experiment`]
            A list of Labstep Experiments.

        Example
        -------
        ::

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
            The id of a tag to filter by.

        Returns
        -------
        List[:class:`~labstep.protocol.Protocol`]
            A list of Labstep Protocols.

        Example
        -------
        ::

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
            The id of a tag to filter by.

        Returns
        -------
        List[:class:`~labstep.resource.Resource`]
            A list of Labstep Resources.

        Example
        -------
        ::

            entity = user.getResources(search_query='bacteria',
                                       tag_id=800)
        """
        return getResources(self, count, search_query, tag_id)

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
            The id of a tag to filter by.

        Returns
        -------
        List[:class:`~labstep.resourceCategory.ResourceCategory`]
            A list of Labstep ResourceCategorys.

        Example
        -------
        ::

            entity = user.getResourceCategorys(search_query='properties',
                                               tag_id=800)
        """
        return getResourceCategorys(self, count, search_query, tag_id)

    def getResourceLocations(self, count=100, search_query=None):
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
        List[:class:`~labstep.resourceLocation.ResourceLocation`]
            A list of ResourceLocation objects.

        Example
        -------
        ::

            entity = user.getResourceLocations(search_query='fridge')
        """
        return getResourceLocations(self, count, search_query)

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
        ::

            entity = user.getOrderRequests(name='polymerase')
        """
        return getOrderRequests(self, count, name)

    def getTags(self, count=1000, search_query=None, type=None):
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
        List[:class:`~labstep.tag.Tag`]
            A list of Labstep Tags.

        Example
        -------
        ::

            entity = user.getTags(search_query='bacteria')
        """
        return getTags(self, count, type, search_query)

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
        ::

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
        ::

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
        ::

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
        ::

            entity = user.newResource(name='salicylic acid')
        """
        return newResource(self, name)

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

        Example
        -------
        ::

            entity = user.newResourceCategory(name='Chemical')
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

        Example
        -------
        ::

            entity = user.newResourceLocation(name='Fridge A')
        """
        return newResourceLocation(self, name)

    def newOrderRequest(self, resource, quantity=1):
        """
        Create a new Labstep OrderRequest.

        Parameters
        ----------
        resource (Resource)
            The :class:`~labstep.resource.Resource` to request more items of.
        quantity (int)
            The quantity of items requested.

        Returns
        -------
        :class:`~labstep.orderRequest.OrderRequest`
            An object representing the an OrderRequest on Labstep.

        Example
        -------
        ::

            my_resource = user.getResource(17000)
            entity = user.newOrderRequest(my_resource, quantity=2)
        """
        return newOrderRequest(self, resource, quantity)

    def newTag(self, name, type):
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
        :class:`~labstep.tag.Tag`
            An object representing a Tag on Labstep.

        Example
        -------
        ::

            entity = user.newTag(name='Aspirin')
        """
        return newTag(self, name, type)

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
        ::

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
        ::

            entity = user.newFile('./structure_of_aspirin.png')
        """
        return newFile(self, filepath)
