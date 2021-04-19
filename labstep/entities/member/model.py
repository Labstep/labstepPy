#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.service.helpers import url_join, getHeaders
from labstep.service.config import API_ROOT
from labstep.service.request import requestService


class Member(Entity):
    """
    Represents a member of a Labstep Workspace.

    To see all attributes of the workspace run
    ::
        print(member)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(member.name)
    """

    __entityName__ = "user-group"

    def remove(self):
        """
        Remove this member from the workspace (requires owner permission)
        """
        url = url_join(API_ROOT, 'api/generic',
                       'user-group', str(self.id))
        headers = getHeaders(self.__user__)
        return requestService.delete(url, headers)
