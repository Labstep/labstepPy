#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from .core import (getExperiment, getProtocol, getResource, getWorkspace, 
    getExperiments, getProtocols, getResources, getTags, getWorkspaces,
    newExperiment, newProtocol, newResource, newTag, newWorkspace,
    uploadFile)


class User:
    def __init__(self,user):
        self.api_key = user['api_key']


    ####################        getSingle()
    def getExperiment(self,experiment_id):
        return getExperiments(self,experiment_id)

    def getProtocol(self,protocol_id):
        return getProtocols(self,protocol_id)
    
    def getResource(self,resource_id):
        return getResources(self,resource_id)

    def getWorkspace(self,workspace_id):
        return getWorkspace(self,workspace_id)


    ####################        getMany()
    def getExperiments(self):
        return getExperiments(self)

    def getProtocols(self):
        return getProtocols(self)
    
    def getResources(self):
        return getResources(self)
    
    def getTags(self):
        return getTags(self)
    
    def getWorkspaces(self):
        return getWorkspaces(self)
    

    ####################        newEntity()
    def newExperiment(self,name):
        return newExperiment(self,name)

    def newProtocol(self,name):
        return newProtocol(self,name)
    
    def newResource(self,name):
        return newResource(self,name)
    
    def newTag(self,name):
        return newTag(self,name)
    
    def newWorkspace(self,name):
        return newWorkspace(self,name)
    

    ####################        addEntity()
    def uploadFile(self,filepath):
        return uploadFile(self,filepath)