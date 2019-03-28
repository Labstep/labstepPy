from labstep import login, createResource, getResources

user = login('demo@labstep.com','demopassword')

resource = createResource(user,'My Resource')
resources = getResources(user)
#experiment = createExperiment(user,'My Experiment','Test')
#experiments = getExperiments(user)
#protocols = getProtocols(user)
#experiment = getExperiment(user,experiment['id'])
#protocol = createProtocol(user,'My Protocol')
#project = createProject(user,'My Project')
#comment = addComment(user,experiment,'Test Comment')
#fileComment = attachFile(user,experiment,'test.py','hellllo?')
print(len(resources))