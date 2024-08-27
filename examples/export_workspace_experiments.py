import labstep
import labstep.config.export as exportConfig

exportConfig.includePDF = True

user = labstep.authenticate(apikey='<your API key>') ## Enter your API key

workspace = user.getWorkspace(XXXX) ## Enter ID of workspace

experiments = workspace.getExperiments() ## Filter experiments using parameters such as tag_id, collection_id, created_at_from, created_at_to

for experiment in experiments:
    experiment.export('my/folder/path') ## Export all formats to a path called 'export'.