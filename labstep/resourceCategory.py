#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylama:ignore=E501

from .entity import Entity, getEntity, getEntities, newEntity, editEntity
from .helpers import getTime
from .comment import addCommentWithFile, getComments
from .metadata import addMetadataTo, getMetadata
from .tag import tag, getAttachedTags


def getResourceCategory(user, resourceCategory_id):
    """
    Retrieve a specific Labstep ResourceCategory.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    resourceCategory_id (int)
        The id of the ResourceCategory to retrieve.

    Returns
    -------
    ResourceCategory
        An object representing a Labstep ResourceCategory.
    """
    return getEntity(user, ResourceCategory, id=resourceCategory_id)


def getResourceCategorys(user, count=100, search_query=None, tag_id=None,
                         extraParams={}):
    """
    Retrieve a list of a user's ResourceCategorys on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    count (int)
        The number of ResourceCategorys to retrieve.
    search_query (str)
        Search for ResourceCategorys with this 'name'.
    tag_id (int)
        The id of the Tag to retrieve.

    Returns
    -------
    ResourceCategorys
        A list of ResourceCategory objects.
    """
    filterParams = {'search_query': search_query,
                    'tag_id': tag_id}
    params = {**filterParams, **extraParams}
    return getEntities(user, ResourceCategory, count, params)


def newResourceCategory(user, name):
    """
    Create a new Labstep ResourceCategory.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the ResourceCategory.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your ResourceCategory a name.

    Returns
    -------
    ResourceCategory
        An object representing the new Labstep ResourceCategory.
    """
    metadata = {'name': name}
    return newEntity(user, ResourceCategory, metadata)


def editResourceCategory(resourceCategory, name=None, deleted_at=None):
    """
    Edit an existing ResourceCategory.

    Parameters
    ----------
    resourceCategory (obj)
        The ResourceCategory to edit.
    name (str)
        The new name of the ResourceCategory.
    deleted_at (str)
        The timestamp at which the ResourceCategory is deleted/archived.

    Returns
    -------
    ResourceCategory
        An object representing the edited ResourceCategory.
    """
    metadata = {'name': name,
                'deleted_at': deleted_at}
    return editEntity(resourceCategory, metadata)


class ResourceCategory(Entity):
    __entityName__ = 'resource-category'

    def edit(self, name):
        """
        Edit an existing ResourceCategory.

        Parameters
        ----------
        name (str)
            The new name of the ResourceCategory.

        Returns
        -------
        :class:`~labstep.resourceCategory.ResourceCategory`
            An object representing the edited ResourceCategory.

        Example
        -------
        ::

            my_resource_category = user.getResourceCategory(17000)
            my_resource_category.edit(name='A New ResourceCategory Name')
        """
        return editResourceCategory(self, name)

    def delete(self):
        """
        Delete an existing ResourceCategory.

        Example
        -------
        ::

            my_resource_category = user.getResourceCategory(17000)
            my_resource_category.delete()
        """
        return editResourceCategory(self, deleted_at=getTime())

    def addComment(self, body, filepath=None):
        """
        Add a comment and/or file to a Labstep ResourceCategory.

        Parameters
        ----------
        body (str)
            The body of the comment.
        filepath (str)
            A Labstep File entity to attach to the comment,
            including the filepath.

        Returns
        -------
        :class:`~labstep.comment.Comment`
            The comment added.

        Example
        -------
        ::

            my_resource_category = user.getResourceCategory(17000)
            my_resource_category.addComment(body='I am commenting!',
                                            filepath='pwd/file_to_upload.dat')
        """
        return addCommentWithFile(self, body, filepath)

    def getComments(self, count=100):
        """
        Gets the comments attached to this entity.

        Returns
        -------
        List[:class:`~labstep.comment.Comment`]
            List of the comments attached.

        Example
        -------
        ::

            entity = user.getResourceCategory(17000)
            comments = entity.getComments()
            comments[0].attributes()
        """
        return getComments(self, count)

    def addTag(self, name):
        """
        Add a tag to the ResourceCategory (creates a
        new tag if none exists).

        Parameters
        ----------
        name (str)
            The name of the tag to create.

        Returns
        -------
        :class:`~labstep.resourceCategory.ResourceCategory`
            The ResourceCategory that was tagged.

        Example
        -------
        ::

            my_resource_category = user.getResourceCategory(17000)
            my_resource_category.addTag(name='My Tag')
        """
        tag(self, name)
        return self

    def getTags(self):
        """
        Retrieve the Tags attached to a this Labstep Entity.

        Returns
        -------
        List[:class:`~labstep.tag.Tag`]
            List of the tags attached.

        Example
        -------
        ::

            entity = user.getResourceCategory(17000)
            tags = entity.getTags()
            tags[0].attributes()
        """
        return getAttachedTags(self)

    def addMetadata(self, fieldType="default", fieldName=None,
                    value=None, date=None,
                    quantity_amount=None, quantity_unit=None):
        """
        Add Metadata to a Resource Category.

        Parameters
        ----------
        fieldType (str)
            The Metadata field type. Options are: "default", "date",
            "quantity", or "number". The "default" type is "Text".
        fieldName (str)
            The name of the field.
        value (str)
            The value accompanying the fieldName entry.
        date (str)
            The date and time accompanying the fieldName entry. Must be
            in the format of "YYYY-MM-DD HH:MM".
        quantity_amount (float)
            The quantity.
        quantity_unit (str)
            The unit accompanying the quantity_amount entry.

        Returns
        -------
        :class:`~labstep.metadata.Metadata`
            An object representing the new Labstep Metadata.

        Example
        -------
        ::

            my_resource_category = user.getResourceCategory(17000)
            metadata = my_resource_category.addMetadata(fieldName="Refractive Index",
                                                        value="1.73")
        """
        return addMetadataTo(self, fieldType, fieldName, value, date,
                             quantity_amount, quantity_unit)

    def getMetadata(self):
        """
        Retrieve the Metadata of a Labstep Resource.

        Returns
        -------
        :class:`~labstep.metadata.Metadata`
            An array of Metadata objects for the Resource.

        Example
        -------
        ::

            entity = user.getResourceCategory(17000)
            metadatas = entity.getMetadata()
            metadatas[0].attributes()
        """
        return getMetadata(self)
