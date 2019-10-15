#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .core import (getExperiment, getProtocol, getResource, getWorkspace,
                   getExperiments, getProtocols, getResources, getTags,
                   getWorkspaces,
                   newExperiment, newProtocol, newResource, newTag,
                   newWorkspace, newFile
                   )


class User:
    def __init__(self, user):
        self.workspace = user['group']['id']
        for key in user:
            setattr(self, key, user[key])

    # getSingle()
    def getExperiment(self, experiment_id):
        """
        Parameters
        ----------
        experiment_id (obj)
            The id of the Experiment to retrieve.
        """
        return getExperiment(self, experiment_id)

    def getProtocol(self, protocol_id):
        """
        Parameters
        ----------
        protocol_id (obj)
            The id of the Protocol to retrieve.
        """
        return getProtocol(self, protocol_id)

    def getResource(self, resource_id):
        """
        Parameters
        ----------
        resource_id (obj)
            The id of the Resource to retrieve.
        """
        return getResource(self, resource_id)

    def getWorkspace(self, workspace_id):
        """
        Parameters
        ----------
        workspace_id (obj)
            The id of the Workspace to retrieve.
        """
        return getWorkspace(self, workspace_id)

    # getMany()
    def getExperiments(self, count=100, search_query=None,
                       created_at_from=None, created_at_to=None, tag_id=None):
        """
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
        """
        return getExperiments(self, count, search_query,
                              created_at_from, created_at_to, tag_id)

    def getProtocols(self, count=100, search_query=None,
                     created_at_from=None, created_at_to=None, tag_id=None):
        """
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
        """
        return getProtocols(self, count, search_query, created_at_from,
                            created_at_to, tag_id)

    def getResources(self, count=100, search_query=None,
                     status=None, tag_id=None):
        """
        Parameters
        ----------
        count (int)
            The number of Resources to retrieve.
        search_query (str)
            Search for Resources with this 'name'.
        status (str)
            Current options to search the status of Resources are:
            'available', 'unavailable', 'requested', 'ordered'.
        tag_id (int)
            The id of the Tag to retrieve.
        """
        return getResources(self, count, search_query, status, tag_id)

    def getTags(self, count=1000, search_query=None):
        """
        Parameters
        ----------
        count (int)
            The number of Tags to retrieve.
        search_query (str)
            Search for Tags with this 'name'.
        """
        return getTags(self, count, search_query)

    def getWorkspaces(self, count=100, name=None):
        """
        Parameters
        ----------
        count (int)
            The number of Workspaces to retrieve.
        name (str)
            Search for Workspaces with this 'name'.
        """
        return getWorkspaces(self, count, name)

    # newEntity()
    def newExperiment(self, name, description=None):
        """
        Parameters
        ----------
        name (str)
            Give your Experiment a name.
        description (str)
            Give your Experiment a description.
        """
        return newExperiment(self, name, description)

    def newProtocol(self, name):
        """
        Parameters
        ----------
        name (str)
            Give your Protocol a name.
        """
        return newProtocol(self, name)

    def newResource(self, name, status=None):
        """
        Parameters
        ----------
        name (str)
            Give your Resource a name.
        status (str)
            Current options to set the status of Resources to are:
            'available', 'unavailable', 'requested', 'ordered'.
        """
        return newResource(self, name, status)

    def newTag(self, name):
        """
        Parameters
        ----------
        name (str)
            Give your Tag a name.
        """
        return newTag(self, name)

    def newWorkspace(self, name):
        """
        Parameters
        ----------
        name (str)
            Give your Workspace a name.
        """
        return newWorkspace(self, name)

    def newFile(self, filepath):
        """
        Parameters
        ----------
        filepath (str)
            The filepath to the file to attach.
        """
        return newFile(self, filepath)
