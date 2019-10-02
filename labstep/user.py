#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from .core import getWorkspaces


class User:
    def __init__(self,user):
        self.api_key = user['api_key']

    def getWorkspaces(self):
        return getWorkspaces(self)
    
    
