from .fixtures import testString, tableData


class SharedTests:
    def edit(self, entity):
        result = entity.edit(name='test')
        return result.name == 'test'

    def delete(self, entity):
        result = entity.delete()
        return result.deleted_at is not None

    def commenting(self, entity):
        commentFromAdd = entity.addComment(
            testString, './tests/data/sample.txt')
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
        file = entity.addFile('./tests/data/sample.txt')
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


sharedTests = SharedTests()
