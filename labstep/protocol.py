#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .config import API_ROOT
from .constants import commentEntityName, protocolEntityName, tagEntityName
from .helpers import url_join, getTime
from .core import editProtocol, tag, addCommentWithFile


class Protocol:
    def __init__(self,protocol,user):
        self.__user__ = user
        for key in protocol:
            setattr(self, key, protocol[key])


    ####################        functions()
    def edit(self,name=None):
        return editProtocol(self.__user__,self,name)
    
    def delete(self):
        return editProtocol(self.__user__,self,deleted_at=getTime())
    
    def comment(self,body,filepath=None):
        return addCommentWithFile(self.__user__,self,body,filepath)

    def addTag(self,name):
        return tag(self.__user__,self,name)