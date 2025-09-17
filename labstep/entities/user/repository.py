#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import json
from labstep.constants import UNSPECIFIED
from labstep.entities.user.model import User
from labstep.service.config import configService
from labstep.service.helpers import url_join
from labstep.service.request import requestService


def getUser(username, apikey):
    url = url_join(configService.getHost(), f"api/generic/user/{username}")
    response = requestService.get(url, headers={"apikey": apikey})
    user = json.loads(response.content)
    return User(user)


def newUser(
    first_name,
    last_name,
    email,
    password,
    share_link_token=UNSPECIFIED,
    extraParams={},
):
    url = url_join(configService.getHost(), "public-api/user")
    params = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "share_link_token": share_link_token,
        **extraParams,
    }

    params = dict(
        filter(lambda field: field[1] is not UNSPECIFIED, params.items()))

    response = requestService.post(url=url, json=params, headers=None)
    return User(json.loads(response.content))


def authenticate(username, apikey):
    url = url_join(configService.getHost(), "api/generic/user/info")
    response = requestService.get(url, headers={"apikey": apikey})
    user = json.loads(response.content)
    user["api_key"] = apikey
    return User(user)

def authenticateWithToken(token):
    url = url_join(configService.getHost(), "api/generic/user/info")
    response = requestService.get(url, headers={"Authorization": f"Bearer {token}"})
    user = json.loads(response.content)
    return User(user)


def login(username, password):
    raise Exception(
        'Login via password has been deprecated. Please use labstep.authenticate with an API key instead.')
    params = {"username": username, "password": password}
    url = url_join(configService.getHost(), "/public-api/user/login")
    response = requestService.post(url=url, json=params, headers={})
    return User(json.loads(response.content))


def impersonate(username, apikey):
    user = getUser(username, apikey)
    url = url_join(configService.getHost(), "api/generic/token/impersonate")
    response = requestService.post(
        url, json={'guid': user.guid}, headers={"apikey": apikey})
    token = json.loads(response.content)['uuid']
    user.api_key = token
    return user
