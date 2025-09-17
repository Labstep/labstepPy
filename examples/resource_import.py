import labstep
import pandas as pd
from labstep.service.helpers import linearToCartesianCoordinates


## Authenticate user
user = labstep.authenticate()


## Set to the ID of the workspace to import into.
user.setWorkspace(WORKSPACE_ID) ## Replace with ID of target workspace.


## Create templates for resources and items
resourceCategory = user.newResourceCategory('Plasmid Preps')
resourceTemplate = resourceCategory.getResourceTemplate()
itemTemplate = resourceCategory.getItemTemplate()

resourceTemplate.addMetadata(fieldName="Plasmid Backbone", fieldType="default")
itemTemplate.addMetadata(fieldName="Concentration", fieldType="numeric", unit="ng / µL")
itemTemplate.addMetadata(fieldName="Prep Date", fieldType="date")


## Import data from xlsx file to create locations, resources and items.
df = pd.read_excel('inventory.xlsx')

df_locations = df['Location'].unique()
locations = {}

for location in df_locations:
    newLocation = user.newResourceLocation(name=location)
    locations[newLocation.name] = newLocation.guid

for index, row in df.iterrows():
    newResource = user.newResource(name=row['Name'], resource_category_id=resourceCategory.id)
    newResource.addMetadata(fieldName='Plasmid Backbone', fieldType='default', value=row['Plasmid backbone'])
    newItem = newResource.newItem()
    newItem.addMetadata(fieldName='Concentration', fieldType="numeric", number=row['Concentration (ng / µl)'])
    newItem.addMetadata(fieldName='Prep Date', fieldType="date", date=str(row['Prep Date']))
    mapPosition = linearToCartesianCoordinates(position=row['Box Position'], number_of_columns=10)
    newItem.setLocation(locations[row['Location']], position=mapPosition)
