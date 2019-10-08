#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .config import API_ROOT
from .constants import commentEntityName, resourceEntityName, tagEntityName
from .helpers import url_join, getTime, handleStatus
from .core import editResource, addCommentWithFile, tag


class Resource:
    def __init__(self,resource,user):
        self.__user__ = user
        for key in resource:
            setattr(self, key, resource[key])


    ####################        functions()
    def edit(self,resource,name=None,status=None):
        return editResource(self.__user__,self,name,status)
    
    def delete(self):
        return editResource(self.__user__,self,deleted_at=getTime())
    
    def comment(self,body,filepath=None):
        return addCommentWithFile(self.__user__,self,body,filepath)

    def addTag(self,name):
        return tag(self.__user__,self,name)