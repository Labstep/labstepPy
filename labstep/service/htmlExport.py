#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import json
import glob
from bs4 import BeautifulSoup
from labstep.service.request import requestService
from labstep.service.config import configService
from labstep.service.helpers import (
    url_join,
    getHeaders,
)


class HTMLExportService:
    def getHTML(self, entity, withImages=False):
        """
        Gets HTML summary of experiments / protocols.

        """
        headers = getHeaders(entity.__user__)

        body = {
            "group_id": entity.__user__.activeWorkspace,
            "query_entity_name": entity.__entityName__.replace("-", "_"),
            "query_parameters": {
                "id": entity.id
            },
            "type": "html_file" if withImages else "html"
        }

        url = url_join(configService.getHost(), 'api/generic', 'entity-export')
        response = requestService.post(url, json=body, headers=headers)

        return json.loads(response.content)['html']

    def insertFilepaths(self, rootDir, html):

        soup = BeautifulSoup(html, 'html.parser')

        for img in soup.find_all('img', {'data-file-id': True, 'data-file-is-link': False}):
            file_id = img['data-file-id']
            file_name = glob.escape(img['data-file-name'])
            path = list(rootDir.glob(f'**/files/{file_id}*/{file_name}'))
            img['src'] = str(path[0].relative_to(rootDir))

        for a in soup.find_all('a', {'data-file-id': True, 'data-file-is-link': False}):
            file_id = a['data-file-id']
            file_name = glob.escape(a['data-file-name'])
            path = list(rootDir.glob(f'**/files/{file_id}*/{file_name}'))
            a['href'] = str(path[0].relative_to(rootDir))

        return str(soup)


htmlExportService = HTMLExportService()
