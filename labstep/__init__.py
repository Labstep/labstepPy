#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylama:ignore=W0611

import requests
import json
from .config import API_ROOT
from .helpers import url_join, handleError
from .user import User
from .experiment import Experiment
from .protocol import Protocol
from .resource import Resource


# login()
def login(username, password):
    '''
    Returns an authenticated Labstep User object to allow
    you to interact with the Labstep API.

    Parameters
    ----------
    username (str)
        Your Labstep username.
    password (obj)
        Your Labstep password.

    Returns
    -------
    user
        An object representing a user on Labstep.
    '''
    data = {'username': username,
            'password': password}
    url = url_join(API_ROOT, "/public-api/user/login")
    r = requests.post(url, json=data, headers={})
    handleError(r)
    return User(json.loads(r.content))
