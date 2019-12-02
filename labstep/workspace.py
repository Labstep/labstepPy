#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylama:ignore=E501

from .entity import getEntity, getEntities, newEntity, editEntity
from .helpers import getTime, update, showAttributes
from .experiment import getExperiments
from .protocol import getProtocols
from .resource import getResources
from .tag import getTags


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


def getWorkspaces(user, count=100, name=None):
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

    Returns
    -------
    workspaces
        A list of Workspace objects.
    """
    fields = {'name': name}
    return getEntities(user, Workspace, count, fields)


def newWorkspace(user, name):
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
    fields = {'name': name}
    return newEntity(user, Workspace, fields)


def editWorkspace(workspace, name=None, deleted_at=None):
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
    fields = {'name': name,
              'deleted_at': deleted_at}
    return editEntity(workspace, fields)


class Workspace:
    __entityName__ = 'group'

    def __init__(self, fields, user):
        self.id = None
        self.__user__ = user
        update(self, fields)

    # functions()
    def attributes(self):
        """
        Show all attributes of a Workspace.

        Example
        -------
        .. code-block::

            my_workspace = user.getWorkspace(17000)
            my_workspace.attributes()

        The output should look something like this:

        .. program-output:: python ../labstep/attributes/workspace_attributes.py

        To inspect specific attributes of a workspace,
        for example, the workspace 'name', 'id', etc.:

        .. code-block::

            print(my_workspace.name)
            print(my_workspace.id)
        """
        return showAttributes(self)

    def edit(self, name):
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
        .. code-block::

            my_workspace = user.getWorkspace(17000)
            my_workspace.edit(name='A New Workspace Name')
        """
        return editWorkspace(self, name)

    def delete(self):
        """
        Delete an existing Workspace.

        Example
        -------
        .. code-block::

            my_workspace = user.getWorkspace(17000)
            my_workspace.delete()
        """
        return editWorkspace(self, deleted_at=getTime())

    # getMany()
    def getExperiments(self, count=100, search_query=None,
                       created_at_from=None, created_at_to=None, tag_id=None):
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
            The id of the Tag to retrieve.

        Returns
        -------
        List[:class:`~labstep.experiment.Experiment`]
            A list of Labstep Experiments.

        Example
        -------
        .. code-block::

            entity = workspace.getExperiments(search_query='bacteria',
                                              created_at_from='2019-01-01',
                                              created_at_to='2019-01-31',
                                              tag_id=800)
        """
        return getExperiments(self.__user__, count, search_query,
                              created_at_from, created_at_to, tag_id,
                              extraParams={'group_id': self.id})

    def getProtocols(self, count=100, search_query=None,
                     created_at_from=None, created_at_to=None, tag_id=None):
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
            The id of the Tag to retrieve.

        Returns
        -------
        List[:class:`~labstep.protocol.Protocol`]
            A list of Labstep Protocols.

        Example
        -------
        .. code-block::

            entity = workspace.getProtocols(search_query='bacteria',
                                            created_at_from='2019-01-01',
                                            created_at_to='2019-01-31',
                                            tag_id=800)
        """
        return getProtocols(self.__user__, count, search_query,
                            created_at_from, created_at_to, tag_id,
                            extraParams={'group_id': self.id})

    def getResources(self, count=100, search_query=None, tag_id=None):
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
            The id of the Tag to retrieve.

        Returns
        -------
        List[:class:`~labstep.resource.Resource`]
            A list of Labstep Resources.

        Example
        -------
        .. code-block::

            entity = workspace.getResources(search_query='bacteria',
                                            tag_id=800)
        """
        return getResources(self.__user__, count, search_query,
                            tag_id, extraParams={'group_id': self.id})

    def getTags(self, count=1000, search_query=None):
        """
        Retrieve a list of Tags within this specific Workspace,
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

            entity = workspace.getTags(search_query='bacteria')
        """
        return getTags(self.__user__, count, search_query,
                       extraParams={'group_id': self.id})
