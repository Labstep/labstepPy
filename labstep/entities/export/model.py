#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity


class Export(Entity):
    """
    Represents an Export on Labstep.
    """

    __entityName__ = "entity-export"
    __unSearchable__ = True
