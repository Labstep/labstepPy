#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep
import pandas

# Login
user = labstep.login('myaccount@labstep.com', 'mypassword')


# Set to an existing workspace
my_workspace = user.newWorkspace('Shared Inventory')
user.setWorkspace(my_workspace.id)


# Read input data
# headers = ['ID', 'Name', 'Location', 'Amount / uL']
data = pandas.read_csv('./resource_import.csv')


# For each entry:
for counter, name in enumerate(data['Name']):

    # Create a new Resource for it
    new_resource = user.newResource(name)

    # Add a new Item and use the 'ID' as the Item name
    new_item = new_resource.newItem(name=data['ID'][counter])

    # Set the amount
    new_item.edit(quantity_amount=data['Amount / uL'][counter],
                  quantity_unit='uL')

    # Set the location
    location = my_workspace.getResourceLocations(
        search_query=data['Location'][counter])

    if len(location) == 0:
        location = user.newResourceLocation(data['Location'][counter])
    else:
        location = location[0]

    new_item.edit(resource_location_id=location.id)
