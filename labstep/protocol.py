#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .config import API_ROOT
from .constants import commentEntityName, protocolEntityName, tagEntityName
from .helpers import url_join, getTime
from .core import (editEntity, editProtocol,
    newEntity, newFile, newTag,
    addComment, addTagTo, getTags)


class Protocol:
    def __init__(self,protocol,user):
        self.__user__ = user
        for key in protocol:
            setattr(self, key, protocol[key])


    ####################        functions()
    def edit(self,protocol,name=None,deleted_at=None):
        metadata = {'name': name,
                    'deleted_at': deleted_at}
        protocol = editEntity(self.__user__,protocolEntityName,protocol['id'],metadata)
        return protocol
    
    def delete(self,protocol):
        protocol = editProtocol(self.__user__,protocol,deleted_at=getTime())
        return protocol
    
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
