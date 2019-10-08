#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .config import API_ROOT
from .constants import commentEntityName, resourceEntityName, tagEntityName
from .helpers import url_join, getTime, handleStatus
from .core import (editEntity, editResource,
    newEntity, newFile, newTag,
    addComment, addTagTo, getTags)


class Resource:
    def __init__(self,resource,user):
        self.__user__ = user
        for key in resource:
            setattr(self, key, resource[key])


    ####################        functions()
    def edit(self,resource,name=None,status=None,deleted_at=None):
        metadata = {'name': name,
                    'status': handleStatus(status),
                    'deleted_at': deleted_at}
        resource = editEntity(self.__user__,resourceEntityName,resource['id'],metadata)
        return resource
    
    def delete(self,resource):
        resource = editResource(self.__user__,resource,deleted_at=getTime())
        return resource
    
    def addComment(self,entity,body,file=None):
        threadId = entity['thread']['id']
        if file != None:
            lsFile = [list(file.keys())[0]]
        else:
            lsFile = None
        data = {'body': body,
                'thread_id': threadId,
                'file_id': lsFile}
        return newEntity(self.__user__,commentEntityName,data)

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
        tag = editEntity(self.__user__,tagEntityName,(tag['id']),metadata)
        return tag
