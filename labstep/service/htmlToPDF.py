#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.service.request import requestService
from labstep.constants import UNSPECIFIED
import json


def htmlToPDF(authenticatedUser, html=UNSPECIFIED,file_id=UNSPECIFIED,returnFile=False):
    """
    Converts HTML into the JSON format used in protocols
    and experiment entries.

    Parameters
    ----------
    authenticatedUser (:)
        An authenticated Labstep :class:`~labstep.entities.user.model.User`
        (see :func:`~labstep.authenticate`)
    html (str)
        HTML to be converted (as a string).
    """
    headers = {"Authorization": f"Bearer {authenticatedUser.token}"}

    if html is UNSPECIFIED and file_id is UNSPECIFIED:
        raise ValueError("html or file_id must be provided")

    body = {"group_id": authenticatedUser.activeWorkspace}

    if html is not UNSPECIFIED:
        body["html"] = html

    if file_id is not UNSPECIFIED:
        body["file_id"] = file_id

    url = "https://pdf-generator.labstep.com"
    response = requestService.post(url, json=body, headers=headers)

    fileID = json.loads(response.content)["file_id"]
    file = authenticatedUser.getFile(fileID)

    file.save()


    if returnFile:
        return file
    else:
        data = file.getData()
        return data
