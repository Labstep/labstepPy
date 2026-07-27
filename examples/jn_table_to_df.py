import labstep

## Login to Labstep Workspace
user = labstep.authenticate()

## Get the id of the document (experiment or protocol) in which the Jupyter Notebook resides
document = labstep.jupyter.getParent()

## Get the tables within the experiment
tables = document.getTables()

## Select the table of interest and convert to a DataFrame.
df = tables.get('Experiment data table').getDataFrame()

## Print the DataFrame.
print(df)