#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep

# Login
user = labstep.login('myaccount@labstep.com', 'mypassword')


# Choose a Workspace
my_workspace = user.getWorkspaces(name='Structure of Protein A')[0]
user.setWorkspace(my_workspace.id)


# Delete a list of Tags for 'crystallisation'
# That are only in the Resource entity type
tags_to_delete = user.getTags(search_query='crystallisation', type='resource')
for i in range(len(tags_to_delete)):
    print('TAGS TO DELETE =', tags_to_delete[i].name)
    tags_to_delete[i].delete()


# Get the difference of two lists using set()
def diff(list1, list2):
    return (list(set(list1) - set(list2)))


# Only keep experiments that investigate the protein structure by 'NMR'
# And store the IDs in a list
keep_experiments = user.getExperiments(search_query='NMR')
keep_exp_ids = []
for i in range(len(keep_experiments)):
    print('EXPERIMENTS TO KEEP =', keep_experiments[i].name)
    print('EXPERIMENT IDS TO KEEP =', keep_experiments[i].id)
    keep_exp_ids.append(keep_experiments[i].id)


# Get all Experiment IDs
all_experiments = user.getExperiments()
all_exp_ids = []
for i in range(len(all_experiments)):
    all_exp_ids.append(all_experiments[i].id)


# Find the IDs of Experiments to delete, and delete them
for i in diff(all_exp_ids, keep_exp_ids):
    print('EXPERIMENT IDS TO DELETE =', i)
    exp_to_delete = user.getExperiment(i)
    exp_to_delete.delete()
