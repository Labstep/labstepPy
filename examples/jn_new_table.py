import labstep
import pandas as pd
from labstep.service.helpers import dataFrameToDataTable


## Login to Labstep Workspace
user = labstep.authenticate()

## Get the id of the document (experiment or protocol) in which the Jupyter Notebook resides
document = labstep.jupyter.getParent()

## Get the datafields within the experiment
dataFields = document.getDataFields()

## Select the datafield of interest and get the data
example_data_file = dataFields.get('Example data').getValue()

## Save the file locally in the notebook
example_data_file.save()

## Convert the data to a dataframe
df = pd.read_csv(example_data_file.name)

## Make a Labstep data table from the DataFrame
data_table = dataFrameToDataTable(df)

## Get the table from the document
table = document.getTables().get('Output Table')

## Add data to Output Table
table.edit(data=data_table)