import labstep

# Creating entities

user = labstep.login('demo@labstep.com','demopassword')
print(user)
experiment = labstep.createExperiment(user,'My First Python Experiment','An experiment created using the labstep python package')
print(experiment)
protocol = labstep.createProtocol(user,'test')
print(protocol)
resource = labstep.createResource(user,'test')
print(resource)
project = labstep.createProject(user,'test')

# Get individual entities
experiment = labstep.getExperiment(user,experiment['id'])
print(experiment)
protocol = labstep.getProtocol(user,protocol['id'])
print(protocol)
resource = labstep.getResource(user,resource['id'])
print(resource)
project = labstep.getProject(user,project['id'])
print(project)

# Get lists of entities
experiments = labstep.getExperiments(user,200)
print(experiments)
protocols = labstep.getProtocols(user,200)
print(protocols)
resources = labstep.getResources(user,200)
print(resources)

# Adding to entities
comment = labstep.addComment(user,experiment,"It's working great!")
print(comment)
lsFile = labstep.attachFile(user,experiment,'example.py','This is the python script used in this experiment')
print(lsFile)
exp = labstep.attachProtocol(user,experiment,protocol)
print(exp)

taggedExperiment = labstep.tag(user,experiment,'NewTag')
print(taggedExperiment)