#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

user = LS.login('demo@labstep.com','demopassword')


# Get It
things = user.getExperiments(search_query='hello')

for i in range(len(things)):
    print('\n GETTING EXPERIMENTS[{}]\n'.format(i),things[i])



