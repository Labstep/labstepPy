#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .config import API_ROOT
from .constants import commentEntityName, resourceEntityName, tagEntityName
from .helpers import url_join, getTime, handleStatus
from .core import editResource, addCommentWithFile, tag


def update(entity,newData):
    for key in newData:
        setattr(entity, key, newData[key])
    return entity

class Experiment:
    def __init__(self,data,user):
        self.__user__ = user
        update(self,data)


    ####################        functions()
    def edit(self,name=None,status=None):
        return editResource(self.__user__,self,name,status)
    
    def delete(self):
        return editResource(self.__user__,self,deleted_at=getTime())
    
    def comment(self,body,filepath=None):
        return addCommentWithFile(self.__user__,self,body,filepath)

    def addTag(self,name):
        return tag(self.__user__,self,name)