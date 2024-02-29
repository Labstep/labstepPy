#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>

from labstep.generic.entityWithComments.model import EntityWithComments
from labstep.generic.entityWithSharing.model import EntityWithSharing
from labstep.generic.entityWithTags.model import EntityWithTags
from labstep.generic.entityWithAssign.model import EntityWithAssign


class EntityPrimary(EntityWithComments, EntityWithSharing, EntityWithTags, EntityWithAssign):
    pass
