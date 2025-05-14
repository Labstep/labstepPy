from labstep.entities.collection.model import Collection
from labstep.entities.device.model import Device
from labstep.entities.experiment.model import Experiment
from labstep.entities.orderRequest.model import OrderRequest
from labstep.entities.protocol.model import Protocol
from labstep.entities.resource.model import Resource
from labstep.entities.resourceCategory.model import ResourceCategory
from labstep.entities.resourceItem.model import ResourceItem
from labstep.entities.resourceLocation.model import ResourceLocation
from labstep.entities.tag.model import Tag
from labstep.entities.workspace.model import Workspace
from labstep.generic.entity.repository import newEntity
from labstep.service.request import RequestException

from .fixtures import fixtures, tableData, testString


class SharedTests:
    def edit(self, entity):
        result = entity.edit(name='test')
        return result.name == 'test'

    def delete(self, entity):
        result = entity.delete()
        return result.deleted_at is not None

    def commenting(self, entity):
        commentFromAdd = entity.addComment(
            testString, __file__)
        commentFromGet = entity.getComments()[0]
        return commentFromAdd.id == commentFromGet.id

    def tagging(self, entity):
        entity.addTag(testString)
        tagFromGet = entity.getTags().get(testString)
        return tagFromGet.name == testString

    def metadata(self, entity):
        metadataFromAdd = entity.addMetadata(
            fieldName=testString, value=testString)
        entity.update()
        metadataFromGet = entity.getMetadata().get(testString)
        return metadataFromAdd.id == metadataFromGet.id \
            and metadataFromGet.label == testString

    def sharelink(self, entity):
        sharelink = entity.getSharelink()
        return sharelink is not None

    def sharing(self, entity, workspaceToShare):
        entity.shareWith(workspaceToShare.guid, 'view')
        permission = entity.getPermissions()[0]
        assert permission.type == 'view'
        permission.set('edit')
        newPermission = entity.getPermissions()[0]
        assert newPermission.type == 'edit'
        newPermission.revoke()
        finalPermissions = entity.getPermissions()
        return len(finalPermissions) == 0

    def collections(self, entity, collection):
        entity.addToCollection(collection.id)
        collectionsAfterAdding = entity.getCollections()
        entity.removeFromCollection(collection.id)
        collectionsAfterRemoving = entity.getCollections()
        return collectionsAfterAdding[0].id == collection.id \
            and len(collectionsAfterRemoving) == 0

    def files(self, entity):
        file = entity.addFile(__file__)
        files = entity.getFiles()
        return files[-1].id == file.id

    def steps(self, entity):
        entity.addSteps(2)
        steps = entity.getSteps()
        return len(steps) >= 2

    def inventoryFields(self, entity):
        inventoryFieldFromAdd = entity.addInventoryField(
            name=testString, amount='2.0', units='ml')
        inventoryFieldFromGet = entity.getInventoryFields().get(testString)
        inventoryFieldEdited = inventoryFieldFromGet.edit(
            name='New Sample Name')
        return inventoryFieldFromGet.id == inventoryFieldFromAdd.id \
            and inventoryFieldEdited.name == 'New Sample Name'

    def timers(self, entity):
        timerFromAdd = entity.addTimer(name=testString, minutes=20, seconds=30)
        timerFromGet = entity.getTimers().get(testString)
        timerEdited = timerFromGet.edit(minutes=17)
        return timerFromAdd.id == timerFromGet.id \
            and timerEdited.minutes == 17

    def tables(self, entity):
        tableFromAdd = entity.addTable(name=testString, data=tableData)
        tableEdited = tableFromAdd.edit(name='Edited')
        tableFromGet = entity.getTables().get('Edited')
        return tableFromAdd.guid == tableFromGet.guid \
            and tableEdited.name == 'Edited'

    def dataFields(self, entity):
        dataFromAdd = entity.addDataField(
            fieldType="default", fieldName="test")
        dataFromAdd.edit(fieldName=testString)
        dataFromGet = entity.getDataFields()
        dataField = dataFromGet.get(testString)
        return dataField.id == dataFromAdd.id \
            and dataField.label == testString

    def jupyterNotebooks(self, entity):
        jupyter_notebook = entity.addJupyterNotebook(name="test")
        jupyter_notebooks = entity.getJupyterNotebooks()
        jupyter_notebook_entity = jupyter_notebooks.get("test")
        return jupyter_notebook_entity.id == jupyter_notebook.id \
            and jupyter_notebook_entity.name == "test"

    def protocolConditions(self, entity):
        user = fixtures.defaultUser()
        test_resource = user.newResource(name='Test')
        output_data_field = entity.addDataField(
            'Test', extraParams={'is_variable': True, 'is_output': True})
        output_inventory_field = entity.addInventoryField('Test',
                                                          resource_id=test_resource.id,
                                                          extraParams={'is_variable': True, 'is_output': True})

        condition = entity.addConditions(1)
        condition_entity = condition[0]

        condition_from_get = entity.getConditions()[0]

        input_data_field_from_get = condition_entity.getDataFields()
        input_inventory_field_from_get = condition_entity.getInventoryFields()

        return condition_entity.guid == condition_from_get.guid \
            and condition_entity.guid == input_data_field_from_get[0].protocol_condition_guid \
            and condition_entity.guid == input_inventory_field_from_get[0].protocol_condition_guid

    def experimentConditions(self, entity):
        user = fixtures.defaultUser()
        test_resource = user.newResource(name='Test')
        output_data_field = entity.addDataField(
            'Test', extraParams={'is_variable': True, 'is_output': True})
        output_inventory_field = entity.addInventoryField('Test',
                                                          resource_id=test_resource.id,
                                                          extraParams={'is_variable': True, 'is_output': True})

        condition = entity.addConditions(1)
        condition_entity = condition[0]

        condition_from_get = entity.getConditions()[1]

        input_data_field_from_get = condition_entity.getDataFields()
        input_inventory_field_from_get = condition_entity.getInventoryFields()

        return condition_entity.guid == condition_from_get.guid \
            and condition_entity.guid == input_data_field_from_get[0].protocol_condition_guid \
            and condition_entity.guid == input_inventory_field_from_get[0].protocol_condition_guid

    def assign(self, entity):
        user = entity.__user__
        workspace_id=entity['owner']['id'] if entity.__entityName__ != 'resource-item' else entity['resource']['owner']['id']
        workspace = user.getWorkspace(workspace_id)
        # add second_user to workspace
        sharelink = workspace.getSharelink()
        second_user = fixtures.new_user(sharelink.token)

        collab = entity.assign(second_user.id)
        collabs_from_get = entity.getCollaborators()
        return collab.id == collabs_from_get[0].id


sharedTests = SharedTests()


class HelperMethods:
    def doesSystemAllowAction(self, action):
        try:
            action()
            return True
        except RequestException as e:
            # Check if the status code is 403 (Forbidden)
            if e.status_code == 403:
                return e.message
            else:
                raise Exception(e)

    def newWorkspaceRole(self, org, roleName, defaultPermission='none'):
        workspace_role = org.newWorkspaceRole(
            f'{roleName}-{defaultPermission}')
        workspace_role.setPermission(Experiment, 'create', defaultPermission)
        workspace_role.setPermission(Experiment, 'edit', defaultPermission)
        workspace_role.setPermission(Experiment, 'assign', defaultPermission)
        workspace_role.setPermission(Experiment, 'delete', defaultPermission)
        workspace_role.setPermission(Experiment, 'share', defaultPermission)
        workspace_role.setPermission(Experiment, 'lock', defaultPermission)
        workspace_role.setPermission(Experiment, 'unlock', defaultPermission)
        workspace_role.setPermission(Experiment, 'comment', defaultPermission)
        workspace_role.setPermission(Experiment, 'sign', defaultPermission)
        workspace_role.setPermission(
            Experiment, 'tag:add_remove', defaultPermission)
        workspace_role.setPermission(
            Experiment, 'folder:add_remove', defaultPermission)

        workspace_role.setPermission(Protocol, 'create', defaultPermission)
        workspace_role.setPermission(Protocol, 'edit', defaultPermission)
        workspace_role.setPermission(Protocol, 'assign', defaultPermission)
        workspace_role.setPermission(Protocol, 'delete', defaultPermission)
        workspace_role.setPermission(Protocol, 'share', defaultPermission)
        workspace_role.setPermission(Protocol, 'comment', defaultPermission)
        workspace_role.setPermission(
            Protocol, 'tag:add_remove', defaultPermission)
        workspace_role.setPermission(
            Protocol, 'folder:add_remove', defaultPermission)

        workspace_role.setPermission(Resource, 'create', defaultPermission)
        workspace_role.setPermission(Resource, 'edit', defaultPermission)
        workspace_role.setPermission(Resource, 'assign', defaultPermission)
        workspace_role.setPermission(Resource, 'delete', defaultPermission)
        workspace_role.setPermission(Resource, 'share', defaultPermission)
        workspace_role.setPermission(Resource, 'comment', defaultPermission)
        workspace_role.setPermission(
            Resource, 'resource_item:create', defaultPermission)
        workspace_role.setPermission(
            Resource, 'tag:add_remove', defaultPermission)

        workspace_role.setPermission(
            ResourceCategory, 'create', defaultPermission)
        workspace_role.setPermission(
            ResourceCategory, 'edit', defaultPermission)
        workspace_role.setPermission(
            ResourceCategory, 'assign', defaultPermission)
        workspace_role.setPermission(
            ResourceCategory, 'delete', defaultPermission)
        workspace_role.setPermission(
            ResourceCategory, 'comment', defaultPermission)

        workspace_role.setPermission(ResourceItem, 'edit', defaultPermission)
        workspace_role.setPermission(ResourceItem, 'assign', defaultPermission)
        workspace_role.setPermission(ResourceItem, 'delete', defaultPermission)
        workspace_role.setPermission(
            ResourceItem, 'comment', defaultPermission)

        workspace_role.setPermission(
            ResourceLocation, 'create', defaultPermission)
        workspace_role.setPermission(
            ResourceLocation, 'edit', defaultPermission)
        workspace_role.setPermission(
            ResourceLocation, 'assign', defaultPermission)
        workspace_role.setPermission(
            ResourceLocation, 'delete', defaultPermission)
        workspace_role.setPermission(
            ResourceLocation, 'comment', defaultPermission)

        workspace_role.setPermission(OrderRequest, 'create', defaultPermission)
        workspace_role.setPermission(OrderRequest, 'edit', defaultPermission)
        workspace_role.setPermission(OrderRequest, 'assign', defaultPermission)
        workspace_role.setPermission(OrderRequest, 'delete', defaultPermission)
        workspace_role.setPermission(OrderRequest, 'share', defaultPermission)
        workspace_role.setPermission(
            OrderRequest, 'comment', defaultPermission)

        workspace_role.setPermission(Device, 'create', defaultPermission)
        workspace_role.setPermission(Device, 'edit', defaultPermission)
        workspace_role.setPermission(Device, 'assign', defaultPermission)
        workspace_role.setPermission(Device, 'delete', defaultPermission)
        workspace_role.setPermission(Device, 'share', defaultPermission)
        workspace_role.setPermission(Device, 'comment', defaultPermission)
        workspace_role.setPermission(Device, 'send_data', defaultPermission)
        workspace_role.setPermission(
            Device, 'create_bookings', defaultPermission)
        workspace_role.setPermission(
            Device, 'tag:add_remove', defaultPermission)

        workspace_role.setPermission(Collection, 'create', defaultPermission)
        workspace_role.setPermission(Collection, 'edit', defaultPermission)
        workspace_role.setPermission(Collection, 'delete', defaultPermission)

        workspace_role.setPermission(Tag, 'create', defaultPermission)
        workspace_role.setPermission(Tag, 'edit', defaultPermission)
        workspace_role.setPermission(Tag, 'delete', defaultPermission)

        workspace_role.setPermission(Workspace, 'comment', defaultPermission)

        return workspace_role

    def setupWorkspace(self, admin, org, user, entityClass, actionName, permission_setting, defaultPermission='none'):

        workspace = admin.newWorkspace(
            f'{permission_setting}-{defaultPermission}')
        workspace_role = self.newWorkspaceRole(
            org, permission_setting, defaultPermission)

        if actionName == 'create' and permission_setting is not 'none':
            workspace_role.setPermission(
                entityClass, 'edit', permission_setting=permission_setting)

        workspace_role.setPermission(
            entityClass, actionName, permission_setting=permission_setting)

        workspace.addMember(
            user_id=user.id, workspace_role_name=workspace_role.name)

        return workspace

    def setupEntity(self, admin, user, workspace, entityClass, entityParams):

        entity = newEntity(admin, entityClass, {
            **entityParams, 'group_id': workspace.id})

        entity.__user__ = user

        return entity

    def setupAssignedEntities(self, admin, user, workspace, entityClass, entityParams):

        entity_assigned = newEntity(admin, entityClass, {
            **entityParams, 'group_id': workspace.id})

        entity_assigned.assign(user.id)
        entity_assigned.__user__ = user

        entity_unassigned = newEntity(admin, entityClass, {
            **entityParams, 'group_id': workspace.id})
        entity_unassigned.__user__ = user

        return [entity_assigned, entity_unassigned]

    def testCreateAction(self, admin, user, org, entityClass, entityParams):

        tests = []

        def create_in_workspace(id): return newEntity(
            user, entityClass, {**entityParams, 'group_id': id})

        # Test With All Permissions
        workspace = self.setupWorkspace(
            admin, org, user, entityClass, 'create', 'all')

        tests.append({
            'entity_name': entityClass.__name__,
            'background_permissions': 'none',
            'workspace_role_permission': 'all',
            'action': 'create',
            'expected_result': True,
            'actual_result': self.doesSystemAllowAction(lambda: create_in_workspace(workspace.id))
        })

        # Test With None Permissions
        workspace = self.setupWorkspace(
            admin, org, user, entityClass, 'create', 'none')

        tests.append({
            'entity_name': entityClass.__name__,
            'background_permissions': 'none',
            'workspace_role_permission': 'none',
            'action': 'create',
            'expected_result': False,
            'actual_result': self.doesSystemAllowAction(lambda: create_in_workspace(workspace.id))
        })

        # Test None With Background All Permissions
        workspace = self.setupWorkspace(
            admin, org, user, entityClass, 'create', 'none', defaultPermission='all')

        tests.append({
            'entity_name': entityClass.__name__,
            'background_permissions': 'all',
            'workspace_role_permission': 'none',
            'action': 'create',
            'expected_result': False,
            'actual_result': self.doesSystemAllowAction(lambda: create_in_workspace(workspace.id))
        })

        return self.checkResults(tests)

    def testEntityActionNoAssign(self, admin, user, org, entityClass, entityParams, actionName, actionTest):
        tests = []
        # Test With All Permissions
        workspace = self.setupWorkspace(
            admin, org, user, entityClass, actionName, 'all')

        entity = self.setupEntity(
            admin, user, workspace, entityClass, entityParams)

        # Can do action for assigned and unassigned entities
        tests.extend([
            {
                'entity_name': entityClass.__name__,
                'background_permissions': 'none',
                'workspace_role_permission': 'all',
                'action': actionName,
                'expected_result': True,
                'actual_result': self.doesSystemAllowAction(lambda: actionTest(entity))
            },
        ])

        # Test With None Permissions
        workspace = self.setupWorkspace(
            admin, org, user, entityClass, actionName, 'none', defaultPermission='all')

        entity = self.setupEntity(
            admin, user, workspace, entityClass, entityParams)

        tests.extend([
            {
                'entity_name': entityClass.__name__,
                'background_permissions': 'all',
                'workspace_role_permission': 'none',
                'action': actionName,
                'expected_result': False,
                'actual_result': self.doesSystemAllowAction(lambda: actionTest(entity))
            }
        ])

    def testEntityAction(self, admin, user, org, entityClass, entityParams, actionName, actionTest):

        tests = []
        # Test With All Permissions
        workspace = self.setupWorkspace(
            admin, org, user, entityClass, actionName, 'all')
        [entity_assigned, entity_unassigned] = self.setupAssignedEntities(
            admin, user, workspace, entityClass, entityParams)

        # Can do action for assigned and unassigned entities
        tests.extend([
            {
                'entity_name': entityClass.__name__,
                'background_permissions': 'none',
                'workspace_role_permission': 'all',
                'collaborator_role': 'assigned',
                'action': actionName,
                'expected_result': True,
                'actual_result': self.doesSystemAllowAction(lambda: actionTest(entity_assigned))
            },
            {
                'entity_name': entityClass.__name__,
                'background_permissions': 'none',
                'workspace_role_permission': 'all',
                'collaborator_role': 'unassigned',
                'action': actionName,
                'expected_result': True,
                'actual_result': self.doesSystemAllowAction(lambda: actionTest(entity_unassigned))
            },
        ])

        # Test With None Permissions
        workspace = self.setupWorkspace(
            admin, org, user, entityClass, actionName, 'none', defaultPermission='all')
        [entity_assigned, entity_unassigned] = self.setupAssignedEntities(
            admin, user, workspace, entityClass, entityParams)

        tests.extend([
            {
                'entity_name': entityClass.__name__,
                'background_permissions': 'all',
                'workspace_role_permission': 'none',
                'collaborator_role': 'assigned',
                'action': actionName,
                'expected_result': False,
                'actual_result': self.doesSystemAllowAction(lambda: actionTest(entity_assigned))
            }
        ])

        # Test With If Assigned Permissions
        workspace = self.setupWorkspace(
            admin, org, user, entityClass, actionName, 'if_assigned')
        [entity_assigned, entity_unassigned] = self.setupAssignedEntities(
            admin, user, workspace, entityClass, entityParams)

        tests.extend([
            {
                'entity_name': entityClass.__name__,
                'background_permissions': 'none',
                'workspace_role_permission': 'if_assigned',
                'collaborator_role': 'assigned',
                'action': actionName,
                'expected_result': True,
                'actual_result': self.doesSystemAllowAction(lambda: actionTest(entity_assigned))
            },
            {
                'entity_name': entityClass.__name__,
                'background_permissions': 'none',
                'workspace_role_permission': 'if_assigned',
                'collaborator_role': 'unassigned',
                'action': actionName,
                'expected_result': False,
                'actual_result': self.doesSystemAllowAction(lambda: actionTest(entity_unassigned))
            },
        ])

        return self.checkResults(tests)

    def checkResults(self, tests):
        for test in tests:
            if test['expected_result'] is False and test['actual_result'] is not True:
                continue

            if test['actual_result'] != test['expected_result']:
                raise Exception(f'Failing Test: {test}')


helperMethods = HelperMethods()
