#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.autoshare.model import Autoshare
from labstep.generic.entityWithComments.model import EntityWithComments
from labstep.entities.workspaceMember.model import WorkspaceMember
from labstep.entities.sharelink.model import Sharelink
from labstep.service.helpers import getTime
from labstep.constants import UNSPECIFIED


class Workspace(EntityWithComments):
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

    def edit(self, name=UNSPECIFIED, extraParams={}):
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
        import labstep.entities.workspace.repository as workspaceRepository

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
        import labstep.entities.workspace.repository as workspaceRepository

        return workspaceRepository.editWorkspace(self, deleted_at=getTime())

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
        import labstep.entities.experiment.repository as experimentRepository

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
        count=UNSPECIFIED,
        search_query=UNSPECIFIED,
        created_at_from=UNSPECIFIED,
        created_at_to=UNSPECIFIED,
        tag_id=UNSPECIFIED,
        collection_id=UNSPECIFIED,
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
        import labstep.entities.protocol.repository as protocolRepository

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

    def getResources(self, count=UNSPECIFIED, search_query=UNSPECIFIED, resource_category_id=UNSPECIFIED, tag_id=UNSPECIFIED, extraParams={}):
        """
        Retrieve a list of Resources within this specific Workspace,
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

            entity = workspace.getResources(search_query='bacteria',
                                            tag_id=800)
        """
        import labstep.entities.resource.repository as resourceRepository

        extraParams = {"group_id": self.id, **extraParams}

        return resourceRepository.getResources(
            self.__user__, count=count, search_query=search_query, resource_category_id=resource_category_id, tag_id=tag_id, extraParams=extraParams
        )

    def getResourceCategorys(
        self, count=UNSPECIFIED, search_query=UNSPECIFIED, tag_id=UNSPECIFIED, extraParams={}
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
        import labstep.entities.resourceCategory.repository as resourceCategoryRepository

        extraParams = {"group_id": self.id, **extraParams}

        return resourceCategoryRepository.getResourceCategorys(
            self.__user__, count, search_query, tag_id, extraParams=extraParams
        )

    def getResourceLocations(self, count=UNSPECIFIED, search_query=UNSPECIFIED, extraParams={}):
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
        import labstep.entities.resourceLocation.repository as resourceLocationRepository

        extraParams = {"group_id": self.id, **extraParams}

        return resourceLocationRepository.getResourceLocations(
            self.__user__, count, search_query, extraParams=extraParams
        )

    def getResourceItems(self, count=UNSPECIFIED, search_query=UNSPECIFIED, extraParams={}):
        """
        Retrieve a list of ResourceItems in a workspace on Labstep.

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
        extraParams = {"group_id": self.id, **extraParams}

        return resourceItemRepository.getResourceItems(
            self.__user__, count=count, search_query=search_query, extraParams=extraParams
        )

    def getOrderRequests(
        self, count=UNSPECIFIED, name=UNSPECIFIED, status=UNSPECIFIED, tag_id=UNSPECIFIED, extraParams={}
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
        import labstep.entities.orderRequest.repository as orderRequestRepository

        extraParams = {"group_id": self.id, **extraParams}

        return orderRequestRepository.getOrderRequests(
            self.__user__,
            count=count,
            search_query=name,
            status=status,
            tag_id=tag_id,
            extraParams=extraParams,
        )

    def getTags(self, count=UNSPECIFIED, search_query=UNSPECIFIED, type=UNSPECIFIED, extraParams={}):
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
        import labstep.entities.tag.repository as tagRepository

        extraParams = {"group_id": self.id, **extraParams}

        return tagRepository.getTags(
            self.__user__, count, type, search_query, extraParams=extraParams
        )

    def newTag(self, name, type='experiment', extraParams={}):
        """
        Create a new tag within this specific Workspace.

        Parameters
        ----------
        name (int)
            The number of Tags to retrieve.
        type (str)
            Options are:
            'experiment', 'protocol',
            'resource', 'order_request'.

        Returns
        -------
        :class:`~labstep.entities.tag.model.Tag`
            An object representing a Labstep Tag.

        Example
        -------
        ::

            tag = workspace.newTag('bacteria')
        """
        import labstep.entities.tag.repository as tagRepository

        extraParams = {"group_id": self.id, **extraParams}

        return tagRepository.newTag(self.__user__, name=name, type=type, extraParams=extraParams)

    def addMember(self, user_id, workspace_role_name=UNSPECIFIED):
        """
        Add a new member to the workspace.

        Note: can only be used to add users from within the same Organization.

        Parameters
        ----------
        user_id (int)
            The id of the user to add as a member

        workspace_role_name (str)
            Name of the workspace role to assign to this member (defaults to 'editor')

        Returns
        -------
        :class:`~labstep.entities.workspaceMember.model.WorkspaceMember`
            An object representing the member of the workspace and their permissions within the workspace.

        Example
        -------
        ::

            newMember = workspace.addMember(user_id=123)
        """
        import labstep.entities.workspaceMember.repository as workspaceMemberRepository
        return workspaceMemberRepository.addMember(self.__user__, workspace_id=self.id, user_id=user_id, workspace_role_name=workspace_role_name)

    def getMembers(self, count=UNSPECIFIED, search_query=UNSPECIFIED, extraParams={}):
        """
        Retrieve a list of the members of the workspace.

        Parameters
        ----------
        count (int)
            The number of members to retrieve.

        search_query (str)
            Search for members by name.

        Returns
        -------
        List[:class:`~labstep.entities.workspaceMember.model.WorkspaceMember`]
            A list of the members of the workspace and their permissions.

        Example
        -------
        ::

            members = workspace.getMembers(search_query='john')
        """
        import labstep.entities.workspaceMember.repository as workspaceMemberRepository
        return workspaceMemberRepository.getMembers(self.__user__, workspace_id=self.id, search_query=search_query, extraParams=extraParams)

    def getFiles(self, count=UNSPECIFIED, search_query=UNSPECIFIED, file_type=UNSPECIFIED, extraParams={}):
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
        import labstep.entities.file.repository as fileRepository

        extraParams = {"group_id": self.id, **extraParams}

        return fileRepository.getFiles(
            self.__user__, count, search_query, file_type, extraParams=extraParams
        )

    def getDevices(self, count=UNSPECIFIED, search_query=UNSPECIFIED, extraParams={}):
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
        import labstep.entities.device.repository as deviceRepository

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

        import labstep.entities.sharelink.repository as shareLinkRepository
        return shareLinkRepository.getSharelink(self)

    def getCollections(
        self, count=UNSPECIFIED, search_query=UNSPECIFIED, type="experiment", extraParams={}
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
        import labstep.entities.collection.repository as collectionRepository

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
        import labstep.entities.collection.repository as collectionRepository

        return collectionRepository.newCollection(
            self.__user__, name=name, type=type, extraParams={
                "group_id": self.id}
        )

    def setHome(self):
        """
        Sets this workspace as the default workspace for the active user.
        """
        member = WorkspaceMember(self.logged_user_user_group, self.__user__)
        import labstep.generic.entity.repository as entityRepository

        return entityRepository.editEntity(member, {"is_home": True})

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

        extraParams = {"group_id": self.id, **extraParams}

        return deviceCategoryRepository.getDeviceCategorys(
            self.__user__,
            count=count,
            search_query=search_query,
            tag_id=tag_id,
            extraParams=extraParams,
        )

    def getJupyterNotebook(self, guid):
        """
        Retrieve an specific Jupyter Notebook attached to this Labstep Entity.

        Parameters
        ----------
        guid (str)
            The GUID of the Jupyter Notebook to retrieve.

        Returns
        -------
        List[:class:`~labstep.entities.jupyterNotebook.model.JupyterNotebook`]
            List of the Jupyter Notebooks attached.

        Example
        -------
        ::

            entity = user.getWorkspace(17000)
            jupyter_notebooks = entity.getJupyterNotebooks()
            print(jupyter_notebooks[0])
        """
        self.update()
        import labstep.entities.jupyterNotebook.repository as jupyterNotebookRepository

        return jupyterNotebookRepository.getJupyterNotebook(self.__user__, guid)

    def getJupyterNotebooks(self, count=UNSPECIFIED):
        """
        Retrieve the Jupyter Notebooks attached to this Labstep Entity.

        Parameters
        ----------
        count (int)
            The number of ResourceCategorys to retrieve.

        Returns
        -------
        List[:class:`~labstep.entities.jupyterNotebook.model.JupyterNotebook`]
            List of the Jupyter Notebooks attached.

        Example
        -------
        ::

            entity = user.getWorkspace(17000)
            jupyter_notebooks = entity.getJupyterNotebooks()
            print(jupyter_notebooks[0])
        """
        self.update()
        import labstep.entities.jupyterNotebook.repository as jupyterNotebookRepository

        return jupyterNotebookRepository.getJupyterNotebooks(self.__user__, count, extraParams={'group_id': self.id})

    def addJupyterNotebook(self, name=UNSPECIFIED, data=UNSPECIFIED):
        """
        Add a Jupyter Notebook to a workspace.

        Parameters
        ----------
        name (str)
            Name of Jupyter Notebook
        data (JSON)
            JSON Jupyter Notebook structure

        Returns
        -------
        :class:`~labstep.entities.jupyterNotebook.model.JupyterNotebook`
            The newly added file entity.

        Example
        -------
        ::

            workspace = user.getWorkspace(17000)
            workspace.addJupyterNotebook()
        """
        import labstep.entities.jupyterNotebook.repository as jupyterNotebookRepository

        return jupyterNotebookRepository.newJupyterNotebook(self.__user__, name, data, extraParams={'group_id': self.id})
