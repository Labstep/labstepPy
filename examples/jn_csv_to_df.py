import labstep
import pandas as pd

## Login to Labstep Workspace
user = labstep.authenticate()

## Get the id of the document (experiment or protocol) in which the Jupyter Notebook resides
document = labstep.jupyter.getParent()

## Get the data fields within the experiment
dataFields = document.getDataFields()

## Select the data field of interest and get the file
example_data_file = dataFields.get('Example data').getValue()

## Save the file locally in the notebook
example_data_file.save()

## Read the file in as a DataFrame
df = pd.read_csv(example_data_file.name)

## print the DataFrame
print(df)