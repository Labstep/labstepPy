#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 12:29:49 2019

@author: Sze May YEE
"""

import labstep as LS

# Login to your Labstep account
user = LS.login('demo@labstep.com','demopassword')

# Create multiple experiments
quantity = 2

# Use the same tag for all
tagname = 'Spyder1'

for i in range(quantity):    
    # Start index from 1 instead of 0
    i = i+1
    
    # Create experiment(s)
    experiment = LS.createExperiment(user,'Test Python Experiment {}'.format(i),
                                     'Experiment {} created'.format(i))
    # Find Protocol
    
    protocols = LS.getProtocols(user)
    
    protocol = protocols[0]
    
    if protocol['name'] !== 'Test Protocol':
        throw Error('Wrong Protocol')
    
# %%    
    # Add protocol(s)
    LS.attachProtocol(user,experiment,protocol)
    
    # Add comment
    LS.addComment(user,experiment,'This is experiment {}'.format(i))

    # Attach file
    file = 'attachingDataToExperiment.py'
    comment = LS.attachFile(user,experiment,file,
                            'This python script was used in experiment {}'.format(i))

    # Add tag
    LS.tag(user,experiment,tagname)
       
    # Get updated info
    updated = LS.getExperiment(user,experiment['id'])
    print(updated)