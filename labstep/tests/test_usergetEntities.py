#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep as LS

user = LS.login('demo@labstep.com','demopassword')


entity = user.newExperiment('A Labstep Experiment')
get = user.getExperiment(entity)
print(get)


# Get many
# for i in range(len(entity)):
#     print('\n GETTING EXPERIMENT[{}] \n'.format(i), entity[i])



