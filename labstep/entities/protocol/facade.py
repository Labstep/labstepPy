#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.entities.protocol.repository import protocolRepository


def getProtocol(user, protocol_id):
    """
    Retrieve a specific Labstep Protocol.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    protocol_id (int)
        The id of the Protocol to retrieve.

    Returns
    -------
    protocol
        An object representing a Labstep Protocol.
    """
    return protocolRepository.getProtocol(user, protocol_id)


def getProtocols(
    user,
    count=100,
    search_query=None,
    created_at_from=None,
    created_at_to=None,
    tag_id=None,
    collection_id=None,
    extraParams={},
):
    """
    Retrieve a list of a user's Protocols on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    count (int)
        The number of Protocols to retrieve.
    search_query (str)
        Search for Protocols with this 'name'.
    created_at_from (str)
        The start date of the search range, must be
        in the format of 'YYYY-MM-DD'.
    created_at_to (str)
        The end date of the search range, must be
        in the format of 'YYYY-MM-DD'.
    tag_id (int)
        The id of the Tag to filter by.
    collection_id (int)
        Get experiments in this collection.
    extraParams (dict)
        Dictionary of extra filter parameters.

    Returns
    -------
    protocols
        A list of Protocol objects.
    """
    return protocolRepository.getProtocols(
        user,
        count,
        search_query,
        created_at_from,
        created_at_to,
        tag_id,
        collection_id,
        extraParams,
    )


def newProtocol(user, name, extraParams={}):
    """
    Create a new Labstep Protocol.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the Protocol.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your Protocol a name.

    Returns
    -------
    protocol
        An object representing the new Labstep Protocol.
    """
    return protocolRepository.newProtocol(user, name, extraParams)


def editProtocol(protocol, name=None, body=None, deleted_at=None, extraParams={}):
    """
    Edit an existing Protocol.

    Parameters
    ----------
    protocol (obj)
        The Protocol to edit.
    name (str)
        The new name of the Protocol.
    body (dict):
        JSON representing the the protocol document.
    deleted_at (str)
        The timestamp at which the Protocol is deleted/archived.

    Returns
    -------
    protocol
        An object representing the edited Protocol.
    """
    return protocolRepository.editProtocol(
        protocol, name, body, deleted_at, extraParams
    )
