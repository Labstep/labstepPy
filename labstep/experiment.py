#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from .config import API_ROOT
from .helpers import url_join, handleError, getTime, createdAtFrom, createdAtTo, handleStatus
from .core import (editEntity, editExperiment,
    newEntity, newFile, newTag,
    addComment, addTagTo, getTags)
import requests
import json


class Experiment:
    def __init__(self,experiment,user):
        self.__user__ = user
        for key in experiment:
            setattr(self, key, experiment[key])


    ####################        functions()
    def edit(self,experiment,name=None,description=None,deleted_at=None):
        metadata = {'name': name,
                    'description': description,
                    'deleted_at': deleted_at}
        experiment = editEntity(self.__user__,'experiment-workflow',experiment['id'],metadata)
        return experiment
    
    def delete(self,experiment):
        experiment = editExperiment(self.__user__,experiment,deleted_at=getTime())
        return experiment
    
    def addProtocol(self,experiment,protocol):
        data = {'experiment_workflow_id':experiment['id'],
                'protocol_id': protocol['last_version']['id']}  
        return newEntity(self.__user__,'experiment',data)
    
    def addComment(self,entity,body,file=None):
        threadId = entity['thread']['id']
        if file != None:
            lsFile = [list(file.keys())[0]]
        else:
            lsFile = None
        data = {'body': body,
                'thread_id': threadId,
                'file_id': lsFile}
        return newEntity(self.__user__,'comment',data)

    def addFile(self,entity,filepath,caption):
        lsFile = newFile(self.__user__,filepath)
        caption = addComment(self.__user__,caption,lsFile)  
        return caption

    def tag(self,entity,name):
        tags = getTags(self.__user__,name)
        matchingTags = list(filter(lambda x: x['name']==name,tags))

        if len(matchingTags)== 0:
            tag = newTag(self.__user__,name)
        else: 
            tag = matchingTags[0]

        entity = addTagTo(self.__user__,entity,tag)
        return entity
    
    def editTag(self,tag,name):
        metadata = {'name': name}
        tag = editEntity(self.__user__,'tag',(tag['id']),metadata)
        return tag
