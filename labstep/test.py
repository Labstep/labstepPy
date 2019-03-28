from login import login
from createExperiment import createExperiment
from createResource import createResource
from createProtocol import createProtocol
from createProject import createProject
from addComment import addComment
from attachFile import attachFile
from getExperiment import getExperiment
from getExperiments import getExperiments
from getProtocols import getProtocols
from getResources import getResources

user = login('test@labstep.com','testpass')

resources = getResources(user,100)
""" resource = createResource(user,'My Resource')
experiment = createExperiment(user,'My Experiment','Test')
experiments = getExperiments(user,2000)
protocols = getProtocols(user,100)

exp = getExperiment(user,experiment['id'])
protocol = createProtocol(user,'My Protocol')
project = createProject(user,'My Project')
comment = addComment(user,experiment,'Test Comment')
fileComment = attachFile(user,experiment,'test.py','hellllo?') """
print(len(resources))