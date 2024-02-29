#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.constants import UNSPECIFIED
from labstep.service.helpers import getTime

class APIKey(Entity):
    __entityName__='access-key'
    __unSearchable__=True

    """
    Represents an API key on Labstep.
    """

    def edit(self, name=UNSPECIFIED, 
                extraParams={}):
            """
            Edit an existing API Key.

            Parameters
            ----------
            name (str)
                The name of the API Key.

            Returns
            -------
            :class:`~labstep.entities.apiKey.model.ApiKey`
                An object representing the edited API Key.

            Example
            -------
            ::

                api_key = user.getAPIKey(1000000)
                api_key.edit(name='New name')
            """
            import labstep.entities.apiKey.repository as ApiKeyRepository

            return ApiKeyRepository.editAPIKey(
                self, name=name, extraParams=extraParams
            )
    
    def delete(self):
        """
        Delete an existing API Key.

        Example
        -------
        ::

            entity = user.getAPIKey(17000)
            entity.delete()
        """
        import labstep.entities.apiKey.repository as ApiKeyRepository

        return ApiKeyRepository.editAPIKey(self, deleted_at=getTime())
    