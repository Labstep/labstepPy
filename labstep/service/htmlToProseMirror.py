#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

import json
from labstep.service.request import requestService


class HTMLToProseMirrorService:
    def parseHTML(self, authenticatedUser, html):
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

        url = "https://html-converter.labstep.com"
        response = requestService.post(url, json=body, headers=headers)
        return json.loads(response.content)


htmlToProseMirrorService = HTMLToProseMirrorService()
