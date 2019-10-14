#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .helpers import getTime, update
from .core import editResource, addCommentWithFile, tag


class Resource:
    def __init__(self, data, user):
        self.__user__ = user
        update(self, data)

    # functions()
    def edit(self, name=None, status=None):
        return editResource(self.__user__, self, name, status)

    def delete(self):
        return editResource(self.__user__, self, deleted_at=getTime())

    def comment(self, body, filepath=None):
        return addCommentWithFile(self.__user__, self, body, filepath)

    def addTag(self, name):
        return tag(self.__user__, self, name)
