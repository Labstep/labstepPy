from labstep import login, getExperiment, addComment, attachFile

# Login to your Labstep account
user = login('demo@labstep.com','demopassword')

# Get a particular experiment
experiment = getExperiment(user,19125)

# Get first step of experiment
step = experiment['experiments'][0]['experiment_steps'][0]

# Comment on the step
addComment(user,step,"Test Comment")

# Attach a file to an experiment
filepath = 'examples/attachingDataToStep.py'
attachFile(user,step,filepath,'This is the python script used in this experiment')

print(experiment)