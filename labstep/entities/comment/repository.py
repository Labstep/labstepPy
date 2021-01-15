#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.comment.model import Comment
from labstep.generic.entity.repository import entityRepository
from labstep.entities.file.repository import fileRepository
from labstep.service.helpers import handleString

class CommentRepository:
    def getComments(self, entity, count=100, extraParams={}):

        if entity.thread is None:
            return []

        params = {
            "parent_thread_id": entity.thread["id"],
            "search": None,
            **extraParams,
        }
        return entityRepository.getEntities(entity.__user__, Comment, count, params)

    def addComment(self, entity, body, fileId=None, extraParams={}):
        if entity.thread is None:
            raise Exception('You cannot add a comment to this entity')

        threadId = entity.thread["id"]

        params = {
            "body": handleString(body),
            "parent_thread_id": threadId,
            "file_id": [[fileId]] if fileId is not None else None,
            **extraParams,
        }

        return entityRepository.newEntity(entity.__user__, Comment, params)

    def addCommentWithFile(self, entity, body, filepath, extraParams={}):
        if filepath is not None:
            fileId = fileRepository.newFile(entity.__user__, filepath).id
        else:
            fileId = None
        return self.addComment(entity, body, fileId=fileId, extraParams=extraParams)

    def editComment(self, comment, body, extraParams={}):
        params = {"body": body, **extraParams}
        return entityRepository.editEntity(comment, params)

    def exportComment(self, comment, rootPath):
        commentDir = entityRepository.exportEntity(comment, rootPath)

        # export comment
        nestedCommentsDir = commentDir.joinpath('comments')
        nestedComments = comment.getComments(count=1000)

        for nestedComment in nestedComments:
            nestedComment.export(nestedCommentsDir)


commentRepository = CommentRepository()
