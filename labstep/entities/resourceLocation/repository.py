#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.entities.resourceLocation.model import ResourceLocation
import labstep.generic.entity.repository as entityRepository
from labstep.constants import UNSPECIFIED


def getResourceLocation(user, resource_location_guid):
    return entityRepository.getEntity(
        user, ResourceLocation, id=resource_location_guid
    )


def getResourceLocations(
    user, count=UNSPECIFIED, search_query=UNSPECIFIED, extraParams={}
):
    params = {
        "group_id": user.activeWorkspace,
        "search_query": search_query,
        **extraParams,
    }
    return entityRepository.getEntities(user, ResourceLocation, count, params)


def newResourceLocation(user, name, outer_location_guid=UNSPECIFIED, extraParams={}):
    params = {
        "group_id": user.activeWorkspace,
        "name": name,
        "outer_location_guid": outer_location_guid,
        **extraParams
    }
    return entityRepository.newEntity(user, ResourceLocation, params)


def editResourceLocation(resourceLocation, name, extraParams={}):
    params = {"name": name, **extraParams}
    return entityRepository.editEntity(resourceLocation, params)


def setPosition(entity, location, position, size=[1, 1]):
    """
    Set the position of an entity within the location (Must have location set already)

    Parameters
    ----------
    position ([x: int,y: int])
        Position coordinates as a [x,y]
    size ([w: int,h: int])
        Optional: Specify the width / height the entity takes up in the location (defaults to [1,1])


    Example
    -------
    ::

        item = user.getResourceItem(17000)
        location = user.getResourceItem(17000)
        setPosition(location,item,position=[1,2],size=[1,1])
    """
    location.update()
    # Create a reference to the item being mapped
    map_key = f'{entity.__entityName__.replace("-","_")}-{entity.id}'

    # Get the most up to date map data or create map data if there is none
    mapData = location.map_data

    if mapData is None:
        # Default to a 10x10 grid unless position of item is greater
        mapData = {
            'rowCount': max(10, position[1]+size[1]),
            'columnCount': max(10, position[0]+size[0]),
            'data': {}
        }

    if position[0] > mapData['columnCount']:
        raise Exception('X position exceeds number of columns')

    if position[1] > mapData['rowCount']:
        raise Exception('Y position exceeds number of rows')

    # Create updated map data with item positions
    updatedMapData = {
        **mapData,
        'data': {
            map_key: {
                "name": entity.name,
                "item": {"w": size[0], "h": size[1], "x": position[0], "y": position[1], "i":
                         map_key, "moved": False, "static": False, "isDraggable": True}
            },
            **mapData['data']
        }
    }

    # Edit the item on labstep with the new map data
    location.edit(extraParams={'map_data': updatedMapData})


def getPosition(entity, location):

    mapData = location.update().map_data

    if mapData is None:
        return None

    map_key = f'{entity.__entityName__.replace("-","_")}-{entity.id}'

    if map_key in mapData['data']:

        item = mapData['data'][map_key]['item']
        return {
            'w':  item['w'],
            'h':  item['h'],
            'x':  item['x'],
            'y':  item['y']
        }

    return None
