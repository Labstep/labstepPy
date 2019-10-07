#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from .core import (getExperiment, getProtocol, getResource, getWorkspace,   # getSingle()
    getExperiments, getProtocols, getResources, getTags, getWorkspaces,     # getMany()
    newExperiment, newProtocol, newResource, newTag, newWorkspace,          # newEntity()
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
    def getExperiments(self,count=100,search_query=None,created_at_from=None,created_at_to=None,tag_id=None):
        return getExperiments(self,count,search_query,created_at_from,created_at_to,tag_id)

    def getProtocols(self,count=100,search_query=None,created_at_from=None,created_at_to=None,tag_id=None):
        return getProtocols(self,count,search_query,created_at_from,created_at_to,tag_id)
    
    def getResources(self,count=100,search_query=None,status=None,tag_id=None):
        return getResources(self,count,search_query,status,tag_id)
    
    def getTags(self,count=1000,search_query=None):
        return getTags(self,count,search_query)
    
    def getWorkspaces(self,count=100,name=None):
        return getWorkspaces(self,count,name)
    

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