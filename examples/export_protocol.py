import labstep
import labstep.config.export as exportConfig

exportConfig.includePDF = True

user = labstep.authenticate(apikey='<your API key>') ## Enter your API key.

protocol = user.getProtocol(XXXX) ## Enter protocol ID.

protocol.export('my/folder/path') ## Export all formats to a path called 'export'.