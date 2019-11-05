#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from .config import API_ROOT
from .helpers import url_join, handleError
from .experiment import getExperiment, getExperiments, newExperiment
from .protocol import getProtocol, getProtocols, newProtocol
from .resource import getResource, getResources, newResource
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

        user = LS.login('myaccount@labstep.com', 'mypassword')

    """
    data = {'username': username,
            'password': password}
    url = url_join(API_ROOT, "/public-api/user/login")
    r = requests.post(url, json=data, headers={})
    handleError(r)
    return User(json.loads(r.content))


class User:
    def __init__(self, user):
        self.workspace = user['group']['id']
        for key in user:
            setattr(self, key, user[key])

    # getSingle()
    def getExperiment(self, experiment_id):
        """
        Retrieve a specific Labstep Experiment.

        Parameters
        ----------
        experiment_id (obj)
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
        protocol_id (obj)
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
        resource_id (obj)
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

    def getWorkspace(self, workspace_id):
        """
        Retrieve a specific Labstep Workspace.

        Parameters
        ----------
        workspace_id (obj)
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
        Retrieve a list of a user's Experiments on Labstep,
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
            List of Labstep Experiments

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
        Retrieve a list of a user's Protocols on Labstep,
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
            List of Labstep Protocols

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
        Retrieve a list of a user's Resources on Labstep,
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
            List of Labstep Resources

        Example
        -------
        .. code-block::

            entity = user.getResources(search_query='bacteria',
                                       tag_id=800)

        """
        return getResources(self, count, search_query, tag_id)

    def getTags(self, count=1000, search_query=None):
        """
        Retrieve a list of a user's Tags on Labstep,
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
            List of Labstep Tags

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
            List of Labstep Workspaces

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
            An object representing an Protocol on Labstep.

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
            An object representing an Resource on Labstep.

        Example
        -------
        .. code-block::

            entity = user.newResource(name='salicylic acid')

        """
        return newResource(self, name)

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
            An object representing an Tag on Labstep.

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
            An object representing an Workspace on Labstep.

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
