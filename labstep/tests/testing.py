#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS
import json

user = LS.login('demo@labstep.com','demopassword')



dictOfNames = {
   7 : 'None',
   8 : 'john',
   9 : 'mathew',
   10: 'None',
   11: 'aadi',
   12: 'sachin'
}

newDict = dict(filter(lambda elem: elem[1] != 'None', dictOfNames.items()))
 
print('Filtered Dictionary : ')
print(newDict)