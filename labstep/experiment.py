#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .helpers import getTime, update
from .core import (editExperiment, addProtocolToExperiment,
                   addCommentWithFile, tag)
from .constants import experimentEntityName


class Experiment:
    def __init__(self, data, user):
        self.__user__ = user
        self.__entityName__ = experimentEntityName
        update(self, data)

    # functions()
    def edit(self, name=None, description=None):
        newData = editExperiment(self.__user__, self, name, description)
        return update(self, newData)

    def delete(self):
        return editExperiment(self.__user__, self, deleted_at=getTime())

    def addProtocol(self, protocol):
        return addProtocolToExperiment(self.__user__, self, protocol)

    def comment(self, body, filepath=None):
        return addCommentWithFile(self.__user__, self, body, filepath)

    def addTag(self, name):
        return tag(self.__user__, self, name)
