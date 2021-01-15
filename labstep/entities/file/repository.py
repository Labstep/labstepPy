#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

import json
from labstep.service.config import API_ROOT
from labstep.service.helpers import url_join, getHeaders
from labstep.entities.file.model import File
from labstep.service.request import requestService
from labstep.generic.entity.repository import entityRepository


class FileRepository:
    def newFile(self, user, filepath, extraParams={}):
        files = {"file": open(filepath, "rb")}
        params = {"group_id": user.activeWorkspace, **extraParams}
        headers = getHeaders(user)
        url = url_join(API_ROOT, "/api/generic/file/upload")
        response = requestService.post(url, headers=headers, files=files, json=params)
        data = json.loads(response.content)
        return File(list(data.values())[0], user)

    def getFile(self, user, fileId):
        return entityRepository.getEntity(user, File, fileId, isDeleted=None)

    def downloadFile(self, user, fileId):
        headers = getHeaders(user)
        url = url_join(API_ROOT, "/api/generic/file/download", str(fileId))
        response = requestService.post(url, headers=headers)
        rawData = requestService.get(json.loads(response.content)["signed_url"],headers=None).content
        return rawData

    def getFiles(
        self, user, count=100, search_query=None, file_type=None, extraParams={}
    ):
        params = {"search_query": search_query, "filetype": file_type, **extraParams}
        return entityRepository.getEntities(user, File, count, params)


fileRepository = FileRepository()
