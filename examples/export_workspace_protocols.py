import labstep
import labstep.config.export as exportConfig

exportConfig.includePDF = True

user = labstep.authenticate(apikey='<your API key>') ## Enter your API key

workspace = user.getWorkspace(XXXX) ## Enter Workspace ID

protocols = workspace.getProtocols() ## Filter protocols using parameters such as tag_id, collection_id, created_at_from, created_at_to

for protocol in protocols:
    protocol.export('my/folder/path') ## Export all formats to a path called 'export'.