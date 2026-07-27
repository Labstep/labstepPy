import labstep
import matplotlib.pyplot as plt

## Login to Labstep Workspace
user = labstep.authenticate()

## Get the id of the document (experiment or protocol) in which the Jupyter Notebook resides
document = labstep.jupyter.getParent()

## Plot some data
plt.plot([1, 2, 3, 4])

## Save the data
plt.savefig('plot.png')

## Get the data field to save the plot to
plotData = document.getDataFields().get('Plot')

## Set the value of the data field to be the generated plot.
plotData.setValue(user.newFile('plot.png'))