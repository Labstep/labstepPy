#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.constants import UNSPECIFIED


class Tag(Entity):
    """
    Represents a Tag on Labstep.

    To see all attributes of a tag run
    ::
        print(my_tag)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(my_tag.name)
        print(my_tag.id)
    """

    __entityName__ = "tag"
    __hasParentGroup__ = True

    def edit(self, name=UNSPECIFIED, extraParams={}):
        """
        Edit the name of an existing Tag.

        Parameters
        ----------
        name (str)
            The new name of the Tag.

        Returns
        -------
        :class:`~labstep.entities.tag.model.Tag`
            An object representing the edited Tag.

        Example
        -------
        ::

            # Get all tags, since there is no function
            # to get one tag.
            tags = user.getTags()

            # Select the tag by using python index.
            tags[1].edit(name='A New Tag Name')
        """
        import labstep.entities.tag.repository as tagRepository

        return tagRepository.editTag(self, name, extraParams=extraParams)

    def delete(self):
        """
        Delete an existing tag.

        Parameters
        ----------
        tag (obj)
            The tag to delete.

        Returns
        -------
        tag
            An object representing the tag to delete.
        """
        import labstep.entities.tag.repository as tagRepository

        return tagRepository.deleteTag(self)
