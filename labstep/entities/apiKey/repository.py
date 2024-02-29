from labstep.service.config import configService
from labstep.service.request import requestService
from labstep.entities.apiKey.model import APIKey
from labstep.generic.entity.repository import getEntities, newEntity, editEntity, getEntity
from labstep.constants import UNSPECIFIED
from labstep.service.helpers import url_join, getHeaders
import json



def newAPIKey(user, name, expires_at, extraParams):
    params = {
        "name": name,
        "expires_at": expires_at,
        **extraParams}
    return newEntity(user, APIKey, params)


def getAPIKey(user, APIKey_id,):


    params = {'id': APIKey_id, 'get_single': 1}

    headers = getHeaders(user=user)
    url = url_join(configService.getHost(), "/api/generic/",APIKey.__entityName__)
    response = requestService.get(url, headers=headers, params=params)
    return APIKey(json.loads(response.content), user)


def editAPIKey(APIKey,
                     name=UNSPECIFIED,
                     extraParams={}):

    params = {"name": name,
              **extraParams}

    return editEntity(APIKey, params)


def getAPIKeys(user,
               count=UNSPECIFIED,
               search_query=UNSPECIFIED,
               api_key=UNSPECIFIED,
               extraParams={},
                ):
    
    params = {
        "search_query": search_query,
        'uuid':api_key,
        **extraParams,
    }
    return getEntities(user, APIKey, count, params)