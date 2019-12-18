# labstepPy

Python wrapper around the Labstep API

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
my_experiment = user.getExperiment(23973)

# Get a specific protocol
my_protocol = user.getProtocol(4926)

# Attach the protocol to the experiment
result = my_experiment.addProtocol(my_protocol)
```

For full list of available methods see:

https://labsteppy.readthedocs.io/en/latest/