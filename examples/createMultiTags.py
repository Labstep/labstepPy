#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:42:30 2019

@author: Sze May YEE
"""

import labstep as LS

# Login to your Labstep account
user = LS.login('demo@labstep.com','demopassword')

# List of tag names
tagname = ['MultiTag1', 'MultiTag2', 'MultiTag3']

for i in tagname:
    # Create tags
    LS.createTag(user,i)