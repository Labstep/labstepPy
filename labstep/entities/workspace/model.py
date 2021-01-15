#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.autoshare.model import Autoshare
from labstep.generic.entity.model import Entity
from labstep.entities.member.model import Member
from labstep.entities.sharelink.model import Sharelink
from labstep.service.helpers import getTime


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

    __entityName__ = "group"

    def edit(self, name=None, extraParams={}):
        """
        Edit an existing Workspace.

        Parameters
        ----------
        name (str)
            The new name of the Workspace.

        Returns
        -------
        :class:`~labstep.entities.workspace.model.Workspace`
            An object representing the edited Workspace.

        Example
        -------
        ::

            my_workspace = user.getWorkspace(17000)
            my_workspace.edit(name='A New Workspace Name')
        """
        from labstep.entities.workspace.repository import workspaceRepository

        return workspaceRepository.editWorkspace(self, name, extraParams=extraParams)

    def delete(self):
        """
        Delete an existing Workspace.

        Example
        -------
        ::

            my_workspace = user.getWorkspace(17000)
            my_workspace.delete()
        """
        from labstep.entities.workspace.repository import workspaceRepository

        return workspaceRepository.editWorkspace(self, deleted_at=getTime())

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
        Retrieve a list of Experiments within this specific Workspace,
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

            entity = workspace.getExperiments(search_query='bacteria',
                                              created_at_from='2019-01-01',
                                              created_at_to='2019-01-31',
                                              tag_id=800)
        """
        from labstep.entities.experiment.repository import experimentRepository

        extraParams = {"group_id": self.id, **extraParams}

        return experimentRepository.getExperiments(
            self.__user__,
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
        collection_id (int)
            Get protocols in this collection.

        Returns
        -------
        List[:class:`~labstep.entities.protocol.model.Protocol`]
            A list of Labstep Protocols.

        Example
        -------
        ::

            entity = workspace.getProtocols(search_query='bacteria',
                                            created_at_from='2019-01-01',
                                            created_at_to='2019-01-31',
                                            tag_id=800)
        """
        from labstep.entities.protocol.repository import protocolRepository

        extraParams = {"group_id": self.id, **extraParams}

        return protocolRepository.getProtocols(
            self.__user__,
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
        List[:class:`~labstep.entities.resource.model.Resource`]
            A list of Labstep Resources.

        Example
        -------
        ::

            entity = workspace.getResources(search_query='bacteria',
                                            tag_id=800)
        """
        from labstep.entities.resource.repository import resourceRepository

        extraParams = {"group_id": self.id, **extraParams}

        return resourceRepository.getResources(
            self.__user__, count, search_query, tag_id, extraParams=extraParams
        )

    def getResourceCategorys(
        self, count=100, search_query=None, tag_id=None, extraParams={}
    ):
        """
        Retrieve a list of Resource Categories within this specific Workspace,
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

            entity = workspace.getResourceCategorys(search_query='properties',
                                                    tag_id=800)
        """
        from labstep.entities.resourceCategory.repository import resourceCategoryRepository

        extraParams = {"group_id": self.id, **extraParams}

        return resourceCategoryRepository.getResourceCategorys(
            self.__user__, count, search_query, tag_id, extraParams=extraParams
        )

    def getResourceLocations(self, count=100, search_query=None, extraParams={}):
        """
        Retrieve a list of Resource Locations within this specific Workspace,
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

            entity = workspace.getResourceLocations(search_query='properties',
                                                    tag_id=800)
        """
        from labstep.entities.resourceLocation.repository import resourceLocationRepository

        extraParams = {"group_id": self.id, **extraParams}

        return resourceLocationRepository.getResourceLocations(
            self.__user__, count, search_query, extraParams=extraParams
        )

    def getOrderRequests(
        self, count=100, name=None, status=None, tag_id=None, extraParams={}
    ):
        """
        Retrieve a list of Order Requests within this specific Workspace,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of OrderRequests to retrieve.
        name (str)
            Search for OrderRequests with this 'name'.

        Returns
        -------

        List[:class:`~labstep.entities.orderRequest.model.OrderRequest`]
            A list of Labstep OrderRequests.

        Example
        -------
        ::

            entity = workspace.getOrderRequests(name='polymerase')
        """
        from labstep.entities.orderRequest.repository import orderRequestRepository

        extraParams = {"group_id": self.id, **extraParams}

        return orderRequestRepository.getOrderRequests(
            self.__user__,
            count=count,
            search_query=name,
            status=status,
            tag_id=tag_id,
            extraParams=extraParams,
        )

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
        List[:class:`~labstep.entities.tag.model.Tag`]
            A list of Labstep Tags.

        Example
        -------
        ::

            entity = workspace.getTags(search_query='bacteria')
        """
        from labstep.entities.tag.repository import tagRepository

        extraParams = {"group_id": self.id, **extraParams}

        return tagRepository.getTags(
            self.__user__, count, type, search_query, extraParams=extraParams
        )

    def getMembers(self, count=100, search_query=None, extraParams={}):
        """
        Retrieve a list of the members of the workspace.

        Parameters
        ----------
        count (int)
            The number of Members to retrieve.

        search_query (str)
            Search for members by name.

        Returns
        -------
        List[:class:`~labstep.entities.member.model.Member`]
            A list of the members of the workspace and their permissions.

        Example
        -------
        ::

            members = workspace.getMembers(search_query='john')
        """
        from labstep.generic.entity.repository import entityRepository

        params = {"group_id": self.id,
                  "search_query_user": search_query, **extraParams}

        return entityRepository.getEntities(self.__user__, Member, count, params)

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
        List[:class:`~labstep.entities.file.model.File`]
            A list of Labstep Files.

        Example
        -------
        ::

            files = workspace.getFiles(search_query='bacteria')
        """
        from labstep.entities.file.repository import fileRepository

        extraParams = {"group_id": self.id, **extraParams}

        return fileRepository.getFiles(
            self.__user__, count, search_query, file_type, extraParams=extraParams
        )

    def getDevices(self, count=100, search_query=None, extraParams={}):
        """
        Retrieve a list of Devices within this specific Workspace,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of Devices to retrieve.
        search_query (str)
            Search for Devices by name of metadata fields.

        Returns
        -------
        List[:class:`~labstep.entities.device.model.Device`]
            A list of Labstep Devices.

        Example
        -------
        ::

            devices = workspace.getDevices(search_query='microscope')
        """
        from labstep.entities.device.repository import deviceRepository

        extraParams = {"group_id": self.id, **extraParams}

        return deviceRepository.getDevices(
            self.__user__, count, search_query, extraParams=extraParams
        )

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

            workspace.sendInvites(
                emails=['collegue1@labstep.com','collegue2@labstep.com'],
                message='Hi, please collaborate with me on Labstep!')
        """
        self.getSharelink().sendEmails(emails=emails, message=message)

    def getSharelink(self):
        """
        Get the sharelink for the workspace.

        Returns
        -------
        :class:`~labstep.entities.sharelink.model.Sharelink`
            The sharelink for the workspace

        """

        from labstep.entities.sharelink.repository import shareLinkRepository
        return shareLinkRepository.getSharelink(self)

    def getCollections(
        self, count=1000, search_query=None, type="experiment", extraParams={}
    ):
        """
        Retrieve a list of Collections within this specific Workspace,
        which can be filtered using the parameters:

        Parameters
        ----------
        count (int)
            The number of Collection to retrieve.
        type (str)
            Return only Collections of a certain type. Options are:
           'experiment', 'protocol'.
        search_query (str)
            Search for Collections with this 'name'.

        Returns
        -------
        List[:class:`~labstep.entities.collection.model.Collection`]
            A list of Labstep Collections.

        Example
        -------
        ::

            entity = workspace.getCollections(search_query='bacteria')
        """
        extraParams = {"group_id": self.id, **extraParams}
        from labstep.entities.collection.repository import collectionRepository

        return collectionRepository.getCollections(
            self.__user__, count, type, search_query, extraParams=extraParams
        )

    def newCollection(self, name, type="experiment"):
        """
        Create a new Collection within the Workspace for Experiments or Protocols.

        Parameters
        ----------
        user (obj)
            The Labstep user creating the Collection.
            Must have property 'api_key'. See 'login'.
        name (str)
            Name of the new Collection.
        type (str)
            Return only collections of a certain type. Options are:
           'experiment', 'protocol'. Defaults to 'experiment'

        Returns
        -------
        collection
            An object representing the new Labstep Collection.
        """
        from labstep.entities.collection.repository import collectionRepository

        return collectionRepository.newCollection(
            self.__user__, name=name, type=type, extraParams={
                "group_id": self.id}
        )

    def setHome(self):
        """
        Sets this workspace as the default workspace for the active user.
        """
        member = Member(self.logged_user_user_group, self.__user__)
        from labstep.generic.entity.repository import entityRepository

        return entityRepository.editEntity(member, {"is_home": True})

    def setAutosharing(
        self, experiment_sharing=None, protocol_sharing=None, resource_sharing=None
    ):
        """
        Parameters
        ----------
        experiment_sharing (str)
            Automatically share experiments
            you create and own with this workspace. Set to True or False

        protocol_sharing (str)
            Automatically share protocols
            you create and own with this workspace. Set to True or False

        resource_sharing (str)
            Automatically share resources
            you create and own with this workspace. Set to True or False

        Returns
        -------
        :class:`~labstep.entities.autoshare.model.Autoshare`
            An object representing the Autosharing policy.

        Example
        -------
        ::

            # Get an workspace
            workspace = user.getWorkspaces(123)

            workspace.setAutosharing(experiment_sharing=True)
        """

        if self.security_policy is None:
            from labstep.generic.entity.repository import entityRepository

            policy = entityRepository.newEntity(
                self.__user__,
                Autoshare,
                {"user_group": self.logged_user_user_group["id"]},
            )
        else:
            policy = Autoshare(self.security_policy, self.__user__)

        return policy.edit(
            experiment_sharing=experiment_sharing,
            protocol_sharing=protocol_sharing,
            resource_sharing=resource_sharing,
        )
