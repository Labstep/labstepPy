import labstep
import labstep.config.export as exportConfig

exportConfig.includePDF = True

user = labstep.authenticate(apikey='<your API key>') ## Enter your API key

experiment = user.getExperiment(XXXX) ## Enter ID of experiment

experiment.export('my/folder/path') ## Export all formats to a path called 'export'.