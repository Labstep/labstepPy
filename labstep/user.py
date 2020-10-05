#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .file import newFile, getFile, getFiles
from .workspace import getWorkspace, getWorkspaces, newWorkspace
from .tag import getTags, newTag
from .orderRequest import getOrderRequest, getOrderRequests, newOrderRequest
import requests
import json
import urllib.parse

from .config import API_ROOT
from .entity import Entity
from .helpers import url_join, handleError, getHeaders
from .experiment import getExperiment, getExperiments, newExperiment
from .protocol import getProtocol, getProtocols, newProtocol
from .resource import getResource, getResources, newResource
from .resourceCategory import (getResourceCategory, getResourceCategorys,
                               newResourceCategory)
from .resourceLocation import (getResourceLocation, getResourceLocations,
                               newResourceLocation)
from .collection import newCollection


def newUser(first_name, last_name, email, password,
            share_link_token=None, extraParams={}):
    url = url_join(API_ROOT, "public-api/user")
    params = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "share_link_token": share_link_token,
        **extraParams
    }

    params = dict(
        filter(lambda field: field[1] is not None, params.items()))

    r = requests.post(url, json=params)
    handleError(r)
    return User(json.loads(r.content))


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
    params = {'username': username,
              'password': password}
    url = url_join(API_ROOT, "/public-api/user/login")
    r = requests.post(url, json=params, headers={})
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
        if user['group'] is None:
            print('Warning: No default workspace. Please set a workspace to continue.')
            self.activeWorkspace = None
        else: 
            self.activeWorkspace = user['group']['id']
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
        :class:`~labstep.workspace.Workspace`
            An object representing a Workspace on Labstep.

        Example
        -------
        ::

            entity = user.getWorkspace(17000)
            user.setWorkspace(entity.id)
        """
        if isinstance(workspace_id, int) is False:
            raise TypeError('workspace_id must be an integer')

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

    def getResourceCategory(self, resource_category_id):
        """
        Retrieve a specific Labstep ResourceCategory.

        Parameters
        ----------
        resource_category_id (int)
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
        return getResourceCategory(self, resource_category_id)

    def getResourceLocation(self, resource_location_id):
        """
        Retrieve a specific Labstep ResourceLocation.

        Parameters
        ----------
        resource_location_id (int)
            The id of the ResourceLocation to retrieve.

        Returns
        -------
        :class:`~labstep.resourceLocation.ResourceLocation`
            An object representing a ResourceLocation on Labstep.

        Example
        -------
        ::

            entity = user.getResourceLocation(17000)
        """
        return getResourceLocation(self, resource_location_id)

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

    def getFile(self, file_id):
        """
        Retrieve a specific Labstep File.

        Parameters
        ----------
        file_id (int)
            The id of the File to retrieve.

        Returns
        -------
        :class:`~labstep.file.File`
            An object representing a File on Labstep.

        Example
        -------
        ::

            entity = user.getFile(17000)
        """
        return getFile(self, file_id)

    # getMany()
    def getExperiments(self, count=100, search_query=None,
                       created_at_from=None, created_at_to=None, tag_id=None,
                       collection_id=None,
                       extraParams={}):
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
        return getExperiments(self,
                              count=count,
                              search_query=search_query,
                              created_at_from=created_at_from,
                              created_at_to=created_at_to,
                              tag_id=tag_id,
                              collection_id=collection_id,
                              extraParams=extraParams)

    def getProtocols(self, count=100, search_query=None,
                     created_at_from=None, created_at_to=None, tag_id=None,
                     collection_id=None,
                     extraParams={}):
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
        return getProtocols(self,
                            count=count,
                            search_query=search_query,
                            created_at_from=created_at_from,
                            created_at_to=created_at_to,
                            tag_id=tag_id,
                            collection_id=collection_id,
                            extraParams=extraParams)

    def getResources(self, count=100, search_query=None, tag_id=None,
                     extraParams={}):
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
        return getResources(self,
                            count=count,
                            search_query=search_query,
                            tag_id=tag_id,
                            extraParams=extraParams)

    def getResourceCategorys(self, count=100, search_query=None, tag_id=None,
                             extraParams={}):
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
        return getResourceCategorys(self,
                                    count=count,
                                    search_query=search_query,
                                    tag_id=tag_id,
                                    extraParams=extraParams)

    def getResourceLocations(self, count=100, search_query=None,
                             extraParams={}):
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
        return getResourceLocations(self,
                                    count=count,
                                    search_query=search_query,
                                    extraParams=extraParams)

    def getOrderRequests(self, count=100, search_query=None, status=None,
                         tag_id=None,
                         extraParams={}):
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

        List[:class:`~labstep.orderRequest.OrderRequest`]
            A list of Labstep OrderRequests.

        Example
        -------
        ::

            entity = user.getOrderRequests(name='polymerase')
        """
        return getOrderRequests(self,
                                count=count,
                                search_query=search_query,
                                status=status,
                                tag_id=tag_id,
                                extraParams=extraParams)

    def getTags(self, count=1000, search_query=None, type=None,
                extraParams={}):
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
        return getTags(self,
                       count=count,
                       type=type,
                       search_query=search_query,
                       extraParams=extraParams)

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

        List[:class:`~labstep.workspace.Workspace`]
            A list of Labstep Workspaces.

        Example
        -------
        ::

            entity = user.getWorkspaces(name='bacteria')
        """
        return getWorkspaces(self,
                             count=count,
                             search_query=search_query,
                             extraParams=extraParams)

    def getFiles(self, count=100, search_query=None, file_type=None,
                 extraParams={}):
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
        List[:class:`~labstep.file.File`]
            A list of Labstep Files.

        Example
        -------
        ::

            entities = user.getFiles(search_query='bacteria')
        """
        return getFiles(self,
                        count=count,
                        search_query=search_query,
                        file_type=file_type,
                        extraParams=extraParams)

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
        :class:`~labstep.experiment.Experiment`
            An object representing an Experiment on Labstep.

        Example
        -------
        ::

            entity = user.newExperiment(name='The Synthesis of Aspirin')
        """
        return newExperiment(self, name,
                             entry=entry,
                             extraParams=extraParams)

    def newProtocol(self, name, extraParams={}):
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
        return newProtocol(self, name, extraParams=extraParams)

    def newResource(self, name, extraParams={}):
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
        return newResource(self, name, extraParams=extraParams)

    def newResourceCategory(self, name, extraParams={}):
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
        return newResourceCategory(self, name, extraParams=extraParams)

    def newResourceLocation(self, name,
                            outer_location_id=None,
                            extraParams={}):
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
        :class:`~labstep.resourceLocation.ResourceLocation`
            An object representing the new Labstep ResourceLocation.

        Example
        -------
        ::

            entity = user.newResourceLocation(name='Fridge A')
        """
        return newResourceLocation(self,
                                   name,
                                   outer_location_id=outer_location_id,
                                   extraParams=extraParams)

    def newOrderRequest(self, resource_id, quantity=1, extraParams={}):
        """
        Create a new Labstep OrderRequest.

        Parameters
        ----------
        resource_id (int)
            The id of the :class:`~labstep.resource.Resource`
            to request more items of.
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
            entity = user.newOrderRequest(my_resource.id, quantity=2)
        """
        return newOrderRequest(self,
                               resource_id=resource_id,
                               quantity=quantity,
                               extraParams=extraParams)

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
        :class:`~labstep.tag.Tag`
            An object representing a Tag on Labstep.

        Example
        -------
        ::

            entity = user.newTag(name='Aspirin')
        """
        return newTag(self, name, type=type, extraParams=extraParams)

    def newWorkspace(self, name, extraParams={}):
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
        return newWorkspace(self, name, extraParams=extraParams)

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
        return newFile(self, filepath, extraParams=extraParams)

    def newCollection(self, name, type='experiment'):
        """
        Create a new Collection for Experiments (or Protocols)

        Parameters
        ----------
        type (str)
            The filepath to the file to attach.
        """
        return newCollection(self, name=name, type=type)

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
        headers = getHeaders(self)
        url = url_join(API_ROOT, "/api/generic/",
                       'share-link')
        params = {'token': token,
                  'get_single': 1}
        r = requests.get(url, headers=headers, params=params)
        handleError(r)
        return None
