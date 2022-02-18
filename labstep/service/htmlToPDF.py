#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.service.request import requestService
import base64


def htmlToPDF(authenticatedUser, html):
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

    body = {"html": html}

    url = "https://pdf-generator.labstep.com"
    response = requestService.post(url, json=body, headers=headers)

    return base64.b64decode(response.content)
