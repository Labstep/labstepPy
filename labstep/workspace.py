#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylama:ignore=E501

import requests
import json
from .entity import Entity, getEntity, getEntities, newEntity, editEntity
from .config import API_ROOT
from .helpers import getTime, getHeaders, url_join, handleError
from .experiment import getExperiments
from .protocol import getProtocols
from .resource import getResources
from .resourceCategory import getResourceCategorys
from .resourceLocation import getResourceLocations
from .orderRequest import getOrderRequests
from .tag import getTags
from .file import getFiles


def getWorkspace(user, workspace_id):
    """
    Retrieve a specific Labstep Workspace.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    workspace_id (int)
        The id of the Workspace to retrieve.

    Returns
    -------
    workspace
        An object representing a Labstep Workspace.
    """
    return getEntity(user, Workspace, id=workspace_id)


def getWorkspaces(user, count=100, name=None, extraParams={}):
    """
    Retrieve a list of a user's Workspaces on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user whose Workspaces you want to retrieve.
        Must have property 'api_key'. See 'login'.
    count (int)
        The number of Workspaces to retrieve.
    name (str)
        Search for Workspaces with this 'name'.
    extraParams (dict)
        Dictionary of extra filter parameters.

    Returns
    -------
    workspaces
        A list of Workspace objects.
    """
    filterParams = {'name': name}
    params = {**filterParams, **extraParams}
    return getEntities(user, Workspace, count, params)


def newWorkspace(user, name, extraParams={}):
    """
    Create a new Labstep Workspace.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the Workspace.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your Workspace a name.

    Returns
    -------
    workspace
        An object representing the new Labstep Workspace.
    """
    filterParams = {'name': name}
    params = {**filterParams, **extraParams}
    return newEntity(user, Workspace, params)


def editWorkspace(workspace, name=None, deleted_at=None, extraParams={}):
    """
    Edit an existing Workspace.

    Parameters
    ----------
    workspace (obj)
        The Workspace to edit.
    name (str)
        The new name of the Workspace.
    deleted_at (str)
        The timestamp at which the Workspace is deleted/archived.

    Returns
    -------
    workspace
        An object representing the Workspace to edit.
    """
    filterParams = {'name': name,
                    'deleted_at': deleted_at}
    params = {**filterParams, **extraParams}
    return editEntity(workspace, params)


class Workspace(Entity):
    """
    Represents a Labstep Workspace.

    To see all attributes of the workspace run
    ::
        print(my_workspace)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(my_workspace.name)
        print(my_workspace.id)
    """
    __entityName__ = 'group'

    share_link = None

    def edit(self, name, extraParams={}):
        """
        Edit an existing Workspace.

        Parameters
        ----------
        name (str)
            The new name of the Workspace.

        Returns
        -------
        :class:`~labstep.workspace.Workspace`
            An object representing the edited Workspace.

        Example
        -------
        ::

            my_workspace = user.getWorkspace(17000)
            my_workspace.edit(name='A New Workspace Name')
        """
        return editWorkspace(self, name, extraParams=extraParams)

    def delete(self):
        """
        Delete an existing Workspace.

        Example
        -------
        ::

            my_workspace = user.getWorkspace(17000)
            my_workspace.delete()
        """
        return editWorkspace(self, deleted_at=getTime())

    # getMany()
    def getExperiments(self, count=100, search_query=None,
                       created_at_from=None, created_at_to=None, tag_id=None,
                       extraParams={}):
        """
        Retrieve a list of Experiments within this specific Workspace,
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

            entity = workspace.getExperiments(search_query='bacteria',
                                              created_at_from='2019-01-01',
                                              created_at_to='2019-01-31',
                                              tag_id=800)
        """
        groupParams = {'group_id': self.id}
        extraParams = {**groupParams, **extraParams}
        return getExperiments(self.__user__, count, search_query,
                              created_at_from, created_at_to, tag_id,
                              extraParams=extraParams)

    def getProtocols(self, count=100, search_query=None,
                     created_at_from=None, created_at_to=None, tag_id=None,
                     extraParams={}):
        """
        Retrieve a list of Protocols within this specific Workspace,
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

            entity = workspace.getProtocols(search_query='bacteria',
                                            created_at_from='2019-01-01',
                                            created_at_to='2019-01-31',
                                            tag_id=800)
        """
        groupParams = {'group_id': self.id}
        extraParams = {**groupParams, **extraParams}
        return getProtocols(self.__user__, count, search_query,
                            created_at_from, created_at_to, tag_id,
                            extraParams=extraParams)

    def getResources(self, count=100, search_query=None, tag_id=None,
                     extraParams={}):
        """
        Retrieve a list of Resources within this specific Workspace,
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

            entity = workspace.getResources(search_query='bacteria',
                                            tag_id=800)
        """
        groupParams = {'group_id': self.id}
        extraParams = {**groupParams, **extraParams}
        return getResources(self.__user__, count, search_query,
                            tag_id, extraParams=extraParams)

    def getResourceCategorys(self, count=100, search_query=None, tag_id=None, extraParams={}):
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

            entity = workspace.getResourceCategorys(search_query='properties',
                                                    tag_id=800)
        """
        groupParams = {'group_id': self.id}
        extraParams = {**groupParams, **extraParams}
        return getResourceCategorys(self.__user__, count, search_query, tag_id,
                                    extraParams=extraParams)

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
        List[:class:`~labstep.resourceLocation.ResourceLocation`]
            A list of ResourceLocation objects.

        Example
        -------
        ::

            entity = workspace.getResourceLocations(search_query='properties',
                                                    tag_id=800)
        """
        groupParams = {'group_id': self.id}
        extraParams = {**groupParams, **extraParams}
        return getResourceLocations(self.__user__, count, search_query,
                                    extraParams=extraParams)

    def getOrderRequests(self, count=100, name=None, status=None, tag_id=None, extraParams={}):
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

            entity = workspace.getOrderRequests(name='polymerase')
        """
        groupParams = {'group_id': self.id}
        extraParams = {**groupParams, **extraParams}
        return getOrderRequests(self.__user__, count, name, status=status, tag_id=tag_id,
                                extraParams=extraParams=extraParams)

    def getTags(self, count=1000, search_query=None, type=None, extraParams={}):
        """
        Retrieve a list of Tags within this specific Workspace,
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

            entity = workspace.getTags(search_query='bacteria')
        """
        groupParams = {'group_id': self.id}
        extraParams = {**groupParams, **extraParams}
        return getTags(self.__user__, count, type, search_query,
                       extraParams=extraParams)

    def getFiles(self, count=100, search_query=None, file_type=None, extraParams={}):
        """
        Retrieve a list of Files in the Workspace on Labstep,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of files to retrieve.
        file_type (str)
            Return only files of a certain type. Options are:
            'csv', 'doc',
            'docx', 'jpg', 'pdf','png','ppt','pptx','svg','xls','xlsx','xml' or 'generic' for all others.
        search_query (str)
            Search for files with this name.

        Returns
        -------
        List[:class:`~labstep.file.File`]
            A list of Labstep Files.

        Example
        -------
        ::

            files = workspace.getFiles(search_query='bacteria')
        """
        groupParams = {'group_id': self.id}
        extraParams = {**groupParams, **extraParams}
        return getFiles(self.__user__, count, search_query, file_type, extraParams=extraParams)

    def sendInvites(self, emails, message):
        """
        Send invites to a Labstep Workspace via email.
        Parameters
        ----------
        emails (list)
            A list of the emails to send the invite to.
        message (str)
            A message to send with the invite.

        Returns
        -------
        None

        Example
        -------
        ::

        workspace.
        sendInvites(emails=['collegue1@labstep.com','collegue2@labstep.com'],message='Hi, please collaborate with me on Labstep!')
        """
        headers = getHeaders(self.__user__)
        sharelink = self.share_link

        if sharelink is None:
            url = url_join(API_ROOT, "api/generic/share-link")
            fields = {
                "group_id": self.id
            }
            r = requests.post(url, json=fields, headers=headers)
            handleError(r)
            sharelink = json.loads(r.content)

        url = url_join(API_ROOT, "api/generic/share-link/email")
        fields = {
            "emails": emails,
            "message": message,
            "id": sharelink['id']
        }
        r = requests.post(url, json=fields, headers=headers)
        handleError(r)
