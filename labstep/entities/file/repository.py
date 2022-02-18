#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

import json
from labstep.service.config import configService
from labstep.service.helpers import url_join, getHeaders
from labstep.entities.file.model import File
from labstep.service.request import requestService
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def newFile(user, filepath=UNSPECIFIED, rawData=UNSPECIFIED, extraParams={}):
    if filepath is not UNSPECIFIED:
        rawData = open(filepath, 'rb')
    if rawData is UNSPECIFIED:
        raise Exception('Please specify filepath or raw data')

    files = {'file': rawData}
    params = {"group_id": user.activeWorkspace, **extraParams}
    headers = getHeaders(user=user)
    url = url_join(configService.getHost(), "/api/generic/file/upload")
    response = requestService.post(
        url, headers=headers, files=files, data=params)
    data = json.loads(response.content)
    return File(list(data.values())[0], user)


def getFile(user, fileId):
    return entityRepository.getEntity(user, File, fileId, isDeleted=UNSPECIFIED)


def getFileDownloadLink(user, fileId):
    headers = getHeaders(user=user)
    url = url_join(configService.getHost(),
                   "/api/generic/file/download", str(fileId))
    response = requestService.post(url, headers=headers)
    return json.loads(response.content)["signed_url"]


def downloadFile(user, fileId):
    downloadLink = getFileDownloadLink(user, fileId)
    response = requestService.get(downloadLink, headers=None)
    return response.content


def getFiles(
    user, count=100, search_query=UNSPECIFIED, file_type=UNSPECIFIED, extraParams={}
):
    params = {"search_query": search_query,
              "filetype": file_type, **extraParams}
    return entityRepository.getEntities(user, File, count, params)


def exportFile(file, root_path):

    fileDir = entityRepository.exportEntity(
        file, root_path, folderName=str(file.id))
    file.save(fileDir)
    if file.image_annotation is not None:
        annotatedFile = File(file.image_annotation, file.__user__)
        annotatedFile.export(root_path)
