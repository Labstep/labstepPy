#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from .config import API_ROOT
from .helpers import url_join, handleError


def newFile(user, filepath):
    """
    Upload a file to the Labstep entity Data.
    Parameters
    ----------
    user (obj)
        The Labstep user uploading the file.
        Must have property 'api_key'. See 'login'.
    filepath (str)
        The filepath to the file to attach.
    Returns
    -------
    file
        An object to upload a file on Labstep.
    """
    files = {'file': open(filepath, 'rb')}
    headers = {'apikey': user.api_key}
    url = url_join(API_ROOT, "/api/generic/file/upload")
    r = requests.post(url, headers=headers, files=files)
    handleError(r)
    return json.loads(r.content)
