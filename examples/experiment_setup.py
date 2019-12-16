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
# Salicylic Acid
salicylic_acid = workspace.newResource('Salicylic Acid')
salicylic_acid.addComment('Chemical structure', './salicylic_acid.png')

salicylic_acid.addMetadata(fieldName='Amount Required', value='2.0 g')

properties = workspace.newResourceCategory('Properties')
salicylic_acid.setResourceCategory(properties)
salicylic_acid.addMetadata(fieldName='Molar mass', value='138.12 g mol-1')
salicylic_acid.addMetadata(fieldName='Density', value='1.443 g cm-3')
salicylic_acid.addMetadata(fieldName='Melting point', value='158.6 oC')

hazards = workspace.newResourceCategory('Hazards')
salicylic_acid.setResourceCategory(hazards)
salicylic_acid.addMetadata(fieldName='Corrosive')
salicylic_acid.addMetadata(fieldName='Irritant')

# Acetic Anhydride
acetic_anhydride = workspace.newResource('Acetic Anhydride')
acetic_anhydride.addComment('Chemical structure', './acetic_anhydride.png')

acetic_anhydride.addMetadata(fieldName='Amount Required', value='5 mL')

acetic_anhydride.setResourceCategory(properties)
acetic_anhydride.addMetadata(fieldName='Molar mass', value='102.09 g mol-1')
acetic_anhydride.addMetadata(fieldName='Density', value='1.08 g cm-3')

acetic_anhydride.setResourceCategory(hazards)
acetic_anhydride.addMetadata(fieldName='Flammable')
acetic_anhydride.addMetadata(fieldName='Corrosive')
