import labstep

user = labstep.login('demo@labstep.com','demopassword')
experiment = labstep.createExperiment(user,'Tagging Again')
taggedExperiment = labstep.tag(user,experiment,'NewTag')
print(taggedExperiment)