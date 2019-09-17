#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:48:20 2019

@author: Sze May YEE
"""

import labstep as LS

# Login to your Labstep account
user = LS.login('demo@labstep.com','demopassword')

# Create multiple protocols
quantity = 2

# Use the same tag for all
tagname = 'Protocol A'

for i in range(quantity):    
    # Start index from 1 instead of 0
    i = i+1
    
    # Create protocol(s)
    protocol = LS.createProtocol(user,'New protocol {}'.format(i))
    
    
    # Add comment
    LS.addComment(user,protocol,'Comment protocol {}'.format(i))

    # Attach file
    file = 'createMultiProtocol.py'
    comment = LS.attachFile(user,protocol,file,
                            'This python script was used in protocol {}'.format(i))

    # Add tag
    LS.tag(user,protocol,tagname)
       
    # Get updated info
    #updated = LS.getProtocol(user,protocol['id'])
    #print(updated)