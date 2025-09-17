#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
from labstep.generic.entity.model import Entity
from labstep.constants import UNSPECIFIED


class CustomIdentifierSet(Entity):
    """
    Represents a set of custom identifiers for an entity.

    """

    __entityName__='custom-identifier-set'
    __hasParentGroup__ = True