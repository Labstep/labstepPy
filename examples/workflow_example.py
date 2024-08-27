#Example script to create new entity states in a workflow and add role requirements to them
import labstep

#Authenticate user
user = labstep.authenticate('myAPIKey')


#Create a new entity state workflow
entity_state_workflow = user.newEntityStateWorkflow('First Workflow')
#Create a new experiment template
experiment_template = user.newExperimentTemplate(name='Template 1')



#Get workspace
workspace = user.getWorkspace(user.activeWorkspace)

#Create new collaborator role named 'Asignee'
collaborator_role_asignee = workspace.newCollaboratorRole(name='Asignee')
#Get entity state 'In Progress' from worflow 'First Workflow'
progress_state=entity_state_workflow.getEntityStates().get('In Progress')
#Add a role requirement to the entity state 'In Progress' to collaborate role 'Asignee' with number of signatures required 1
collaborator_role_requirement_progress_state = progress_state.addRoleRequirement(collaborator_role_asignee.id, number_required=1)
#Set a signature requirement to the role requirement
signature_requirement_progress_state=collaborator_role_requirement_progress_state.setSignatureRequirement()
#Edit the signature requirement statement and days to sign
signature_requirement_progress_state.edit(statement='I have carried out the experiment as described', days_to_sign=30)


#Create new entity state 'Review Needed' from workflow 'First Workflow'
completed_state = entity_state_workflow.newEntityState('Review Needed')
#Create new Collaborator Role named 'Reviewer'
collaborator_role_reviewer = workspace.newCollaboratorRole(name='Reviewer')
#Add a role requirement to the entity state 'Review Needed' to collaborate role 'Reviewer' with number of signatures required 1
collaborator_role_requirement_review_state = progress_state.addRoleRequirement(collaborator_role_reviewer.id, number_required=1)
#Set a signature requirement to the role requirement
signature_requirement_review_state=collaborator_role_requirement_review_state.setSignatureRequirement()
#Edit the signature requirement statement and days to sign, and set the reject entity state to 'In Progress'
signature_requirement_review_state.edit(statement='I have reviewed the experiment', days_to_sign=30, extraParams={'reject_entity_state_id':progress_state.id})


#Set the new workflow to the experiment template
experiment_template.edit(entity_state_workflow_id=entity_state_workflow.id)

#Create a new experiment from the template 'Experiment from Template' and set the entity state to 'In Progress'
new_experiment=user.newExperiment(name='Experiment from Template', template_id=experiment_template.id)
new_experiment.edit(extraParams={'entity_state_id':progress_state.id})