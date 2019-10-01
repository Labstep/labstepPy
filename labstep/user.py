#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from .core import *


class User:
    def __init__(self,user):
        self.api_key = user['api_key']

    def getWorkspace(self,id):
        return getWorkspace(self,id)
