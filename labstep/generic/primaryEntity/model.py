#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.shareableEntity.model import ShareableEntity


class PrimaryEntity(ShareableEntity):
    def addTag(self, name):
        """
        Add a tag to the Entity (creates a
        new tag if none exists).

        Parameters
        ----------
        name (str)
            The name of the tag to create.

        Returns
        -------
        :class:`~labstep.entities.experiment.model.Experiment`
            The Experiment that was tagged.

        Example
        -------
        ::

            my_experiment = user.getExperiment(17000)
            my_experiment.addTag(name='My Tag')
        """
        from labstep.entities.tag.repository import tagRepository

        tagRepository.tag(self, name)
        return self

    def getTags(self):
        """
        Retrieve the Tags attached to a this Labstep Entity.

        Returns
        -------
        List[:class:`~labstep.entities.tag.model.Tag`]
            List of the tags attached.

        Example
        -------
        ::

            entity = user.getExperiment(17000)
            tags = entity.getTags()
            tags[0].attributes()
        """
        from labstep.entities.tag.repository import tagRepository

        return tagRepository.getAttachedTags(self)
