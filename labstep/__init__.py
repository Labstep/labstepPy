#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from .config import *
from .helpers import *


####################        login()
def login(username,password):
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
    url = url_join(API_ROOT,"/public-api/user/login")
    r = requests.post(url, json=data, headers={}) 
    return json.loads(r.content)
    #return User(json.loads(r.content))

