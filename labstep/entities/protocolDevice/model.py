#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entity.model import Entity
from labstep.constants import UNSPECIFIED


class ProtocolDevice(Entity):
    __entityName__ = "protocol-device"
    __hasGuid__ = True

