#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .config import API_ROOT
from .constants import commentEntityName, experimentEntityName, tagEntityName
from .helpers import url_join, getTime
from .core import editExperiment, tag, addCommentWithFile, addProtocolToExperiment


class Experiment:
    def __init__(self,experiment,user):
        self.__user__ = user
        for key in experiment:
            setattr(self, key, experiment[key])


    ####################        functions()
    def edit(self,experiment,name=None,description=None):
        return editExperiment(self.__user__,self,name,description)
    
    def delete(self):
        return editExperiment(self.__user__,self,deleted_at=getTime())
    
    def addProtocol(self,protocol):
        return addProtocolToExperiment(self.__user__,self,protocol)
    
    def comment(self,body,filepath=None):
        return addCommentWithFile(self.__user__,self,body,filepath)

    def addTag(self,name):
        return tag(self.__user__,self,name)
    
