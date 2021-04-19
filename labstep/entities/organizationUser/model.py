#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Barney Walker <barney@labstep.com>

from labstep.generic.entity.model import Entity


class OrganizationUser(Entity):
    __entityName__ = "user-organization"

    def setAdmin(self):
        """
        Gives a user admin permission over the organization.


        Example
        -------
        ::

            users = my_organization.getUsers()
            user[0].setAdmin()
        """
        from labstep.entities.organizationUser.repository import organizationUserRepository

        return organizationUserRepository.promoteUser(self)

    def revokeAdmin(self):
        """
        Revokes admin permissions from a user.


        Example
        -------
        ::

            users = my_organization.getUsers()
            user[0].revokeAdmin()
        """
        from labstep.entities.organizationUser.repository import organizationUserRepository

        return organizationUserRepository.demoteUser(self)

    def disable(self):
        """
        Disables a user account.


        Example
        -------
        ::

            users = my_organization.getUsers()
            user[0].disable()
        """
        from labstep.entities.organizationUser.repository import organizationUserRepository

        return organizationUserRepository.disableUser(self)
