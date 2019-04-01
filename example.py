from labstep import login, createExperiment, addComment, attachFile

# Login to your Labstep account
user = login('demo@labstep.com','demopassword')

# Create an experiment
experiment = createExperiment(user,'My First Python Experiment','An experiment created using the labstep python package')

# Comment on an experiment
addComment(user,experiment,"It's working great!")

# Attach a file to an experiment
filepath = 'example.py'
attachFile(user,experiment,filepath,'This is the python script used in this experiment')

print(experiment)