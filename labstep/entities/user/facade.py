#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

import os
import labstep.entities.user.repository as userRepository
from labstep.constants import UNSPECIFIED


def newUser(
    first_name, last_name, email, password, share_link_token=UNSPECIFIED, extraParams={}
):
    """
    TODO
    """
    return userRepository.newUser(
        first_name, last_name, email, password, share_link_token, extraParams
    )


def authenticate(username=UNSPECIFIED, apikey=UNSPECIFIED):
    """
    Returns an authenticated Labstep User object to allow
    you to interact with the Labstep API.

    Parameters
    ----------
    username (str)
        Your Labstep username.
    apikey (str)
        An apikey for the user.

    Returns
    -------
    :class:`~labstep.entities.user.model.User`
        An object representing a user on Labstep.

    Example
    -------
    ::

        import labstep

        user = labstep.authenticate('myaccount@labstep.com', 'MY_API_KEY')
    """
    if (apikey is UNSPECIFIED):
        apikey = os.environ['LABSTEP_API_KEY']

    return userRepository.authenticate(username, apikey)


def login(username, password):
    """
    Returns an authenticated Labstep User object to allow
    you to interact with the Labstep API.

    Parameters
    ----------
    username (str)
        Your Labstep username.
    password (str)
        Your Labstep password.

    Returns
    -------
    :class:`~labstep.entities.user.model.User`
        An object representing a user on Labstep.

    Example
    -------
    ::

        import labstep

        user = labstep.login('myaccount@labstep.com', 'mypassword')
    """
    return userRepository.login(username, password)


def impersonate(username, apikey):
    return userRepository.impersonate(username, apikey)
