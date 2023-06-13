#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.comment.model import Comment
from labstep.generic.entity.repository import getEntities, newEntity, editEntity, exportEntity
import labstep.entities.file.repository as fileRepository
from labstep.service.helpers import handleString
from labstep.constants import UNSPECIFIED


def getComments(entity, count=UNSPECIFIED, extraParams={}):

    if hasattr(entity, 'thread') is False:
        entity.update()

    if hasattr(entity, 'thread') is False:
        return []

    if entity.thread is None:
        return []

    if entity.thread['comment_count'] == 0:
        return []

    params = {
        "parent_thread_id": entity.thread["id"],
        "search": None,
        **extraParams,
    }
    return getEntities(entity.__user__, Comment, count, params)


def addComment(entity, body, fileId=UNSPECIFIED, extraParams={}):
    if hasattr(entity, 'thread') is False:
        raise Exception('You cannot add a comment to this entity')

    threadId = entity.thread["id"]

    params = {
        "body": handleString(body),
        "parent_thread_id": threadId,
        "file_id": [[fileId]] if fileId is not UNSPECIFIED else UNSPECIFIED,
        **extraParams,
    }

    entity.thread["comment_count"] += 1

    return newEntity(entity.__user__, Comment, params)


def addCommentWithFile(entity, body, filepath, extraParams={}):
    if filepath is not UNSPECIFIED:
        fileId = fileRepository.newFile(entity.__user__, filepath).id
    else:
        fileId = UNSPECIFIED
    return addComment(entity, body, fileId=fileId, extraParams=extraParams)


def editComment(comment, body=UNSPECIFIED, extraParams={}):
    params = {"body": body, **extraParams}
    return editEntity(comment, params)


def exportComment(comment, rootPath):
    commentDir = exportEntity(
        comment, rootPath)

    # export comment
    nestedCommentsDir = commentDir.joinpath('comments')
    nestedComments = comment.getComments()

    for nestedComment in nestedComments:
        nestedComment.export(
            nestedCommentsDir)
