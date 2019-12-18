# labstepPy

Python SDK for working with the Labstep API

## Installation

```
pip install labstep
```

## Usage

```
import labstep

# Login to your Labstep account
user = labstep.login('myaccount@labstep.com', 'mypassword')

# Get a list of your experiments
experiments = user.getExperiments(count=10)

# Get a specific experiment
my_experiment = experiments[0]

# Get a specific protocol
protocols = user.getProtocols()
my_protocol = protocols[0]

# Attach the protocol to the experiment
result = my_experiment.addProtocol(my_protocol)
```

For full list of available methods see:

https://labsteppy.readthedocs.io/en/latest/