import labstep as LS


# Login to your Labstep account
user = LS.login('demo@labstep.com','demopassword')

# Create an experiment
experiment = LS.createExperiment(user,'Add file no caption')

# Attach a file
filename = 'attachingDataToExperiment.py'
comment = LS.attachFile(user,experiment,filename)

updatedExperiment = LS.getExperiment(user,experiment['id'])
print(updatedExperiment)