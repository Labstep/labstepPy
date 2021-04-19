#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.user.repository import userRepository


def newUser(
    first_name, last_name, email, password, share_link_token=None, extraParams={}
):
    """
    TODO
    """
    return userRepository.newUser(
        first_name, last_name, email, password, share_link_token, extraParams
    )


def authenticate(username, apikey):
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
