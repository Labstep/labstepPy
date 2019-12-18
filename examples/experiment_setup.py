#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import labstep

# Login
user = labstep.login('myaccount@labstep.com', 'mypassword')


# Create a new Workspace
workspace = user.newWorkspace(name='The Synthesis of Aspirin')
user.setWorkspace(workspace.id)


# Create an Experiment
my_experiment = workspace.newExperiment(name='Trial 1',
                                        description='Aspirin is a drug...')


# Upload the reaction scheme
workspace.newFile('./aspirin_reaction_scheme.png')


# Create a Protocol
my_protocol = workspace.newProtocol('Aspirin Synthesis')


# Add Resources
# 1. Salicylic Acid
salicylic_acid = workspace.newResource('Salicylic Acid')
salicylic_acid.addComment('Chemical structure', './salicylic_acid.png')

# Add general metadata
salicylic_acid.addMetadata(fieldName='Amount Required', value='2.0 g')

# Add metadata under specific Resource Categories
properties = workspace.newResourceCategory('Properties')
properties.addMetadata(fieldName='Molar mass', value='138.12 g mol-1')
properties.addMetadata(fieldName='Density', value='1.443 g cm-3')
properties.addMetadata(fieldName='Melting point', value='158.6 oC')

hazards = workspace.getResourceCategorys('Hazards')[0]
hazards.addMetadata(fieldName='Corrosive')
hazards.addMetadata(fieldName='Irritant')

# 2. Acetic Anhydride
acetic_anhydride = workspace.newResource('Acetic Anhydride')
acetic_anhydride.addComment('Chemical structure', './acetic_anhydride.png')

acetic_anhydride.addMetadata(fieldName='Amount Required', value='5 mL')

properties.addMetadata(fieldName='Molar mass', value='102.09 g mol-1')
properties.addMetadata(fieldName='Density', value='1.08 g cm-3')

hazards.addMetadata(fieldName='Flammable')
hazards.addMetadata(fieldName='Corrosive')

# etc...
