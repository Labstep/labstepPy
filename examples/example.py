import labstep as LS

# Login to your Labstep account
user = LS.login('myaccount@labstep.com', 'mypassword')

# Get a list of your experiments
experiments = user.getExperiments(count=10)

# Get a specific experiment
my_experiment = LS.Experiment(user.getExperiment(23973), user)

# Get a specific protocol
my_protocol = user.getProtocol(4926)

# Attach the protocol to the experiment
result = my_experiment.addProtocol(my_protocol)
