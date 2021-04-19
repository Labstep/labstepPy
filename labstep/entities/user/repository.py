#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

import json
import urllib.parse
from labstep.entities.user.model import User
from labstep.service.config import API_ROOT
from labstep.service.helpers import url_join
from labstep.service.request import requestService


class UserRepository:
    def getUser(self, username, apikey):
        url = url_join(API_ROOT, f"api/generic/user/{username}")
        response = requestService.get(url, headers={"apikey": apikey})
        user = json.loads(response.content)
        return User(user)

    def newUser(
        self,
        first_name,
        last_name,
        email,
        password,
        share_link_token=None,
        extraParams={},
    ):
        url = url_join(API_ROOT, "public-api/user")
        params = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "share_link_token": share_link_token,
            **extraParams,
        }

        params = dict(
            filter(lambda field: field[1] is not None, params.items()))

        response = requestService.post(url=url, json=params, headers=None)
        return User(json.loads(response.content))

    def authenticate(self, username, apikey):
        url = url_join(API_ROOT, "api/generic/user/info")
        response = requestService.get(url, headers={"apikey": apikey})
        user = json.loads(response.content)
        user["api_key"] = apikey
        return User(user)

    def login(self, username, password):
        params = {"username": username, "password": password}
        url = url_join(API_ROOT, "/public-api/user/login")
        response = requestService.post(url=url, json=params, headers={})
        return User(json.loads(response.content))

    def impersonate(self, username, apikey):
        user = self.getUser(username, apikey)
        url = url_join(API_ROOT, "api/generic/token/impersonate")
        response = requestService.post(
            url, json={'guid': user.guid}, headers={"apikey": apikey})
        token = json.loads(response.content)['uuid']
        user.api_key = token
        return user


userRepository = UserRepository()
