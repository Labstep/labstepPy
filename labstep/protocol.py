#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .helpers import getTime, update
from .core import editProtocol, addCommentWithFile, tag
from .constants import protocolEntityName


class Protocol:
    def __init__(self, data, user):
        self.__user__ = user
        self.__entityName__ = protocolEntityName

        update(self, data)

    # functions()
    def edit(self, name=None):
        return editProtocol(self.__user__, self, name)

    def delete(self):
        return editProtocol(self.__user__, self, deleted_at=getTime())

    def comment(self, body, filepath=None):
        return addCommentWithFile(self.__user__, self, body, filepath)

    def addTag(self, name):
        return tag(self.__user__, self, name)
