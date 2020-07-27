#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep

# Login
user = labstep.login('myaccount@labstep.com', 'mypassword')


# Create a new Workspace
workspace = user.newWorkspace(name='The Synthesis of Aspirin')
user.setWorkspace(workspace.id)


# Create an Experiment
my_experiment = user.newExperiment(name='Trial 1')

# Upload the reaction scheme
user.newFile('./aspirin_reaction_scheme.png')

# Create a Protocol
my_protocol = user.newProtocol('Aspirin Synthesis')

# Create Resource Category
chemicalCategory = user.newResourceCategory('Chemical')
chemicalCategory.addMetadata(fieldName='Molar mass')
chemicalCategory.addMetadata(fieldName='Density')
chemicalCategory.addMetadata(fieldName='Melting point')

# Add Resources
salicylic_acid = user.newResource('Salicylic Acid')
salicylic_acid.addComment('Here is the chemical structure',
                          './salicylic_acid.png')
salicylic_acid.addMetadata(fieldName='Formula', value='C7H6O3')
salicylic_acid.addMetadata(fieldName='Hazards', value='Corrosive, irritant')


# etc...
