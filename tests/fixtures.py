import labstep
import os

TESTING_KEY = os.getenv('TESTING_KEY')

user = labstep.authenticate('apitest@labstep.com', TESTING_KEY)

tableData = {
    "rowCount": 6,
    "columnCount": 6,
    "colHeaderData": {},
    "data": {
        "dataTable": {
            0: {
                0: {
                    "value": 'Cell A1'
                },
                1: {
                    "value": 'Cell B1'
                }
            }
        }
    }
}

proseMirrorState = {
    "type": "doc",
    "content": [
        {
            "type": "paragraph",
            "attrs": {"align": None},
            "content": [
                {
                    "type": "text",
                            "text": "test"
                }
            ]
        },
        {
            "type": "paragraph",
            "attrs": {"align": None}
        }
    ]
}


def proseMirrorStateWithSteps(steps):
    return {
            "type": "doc",
            "content": [
                {
                    "type": "protocol_step",
                    "attrs": {"id": steps[0].id},
                    "content": [{
                            "type": "paragraph",
                            "attrs": {"align": None}
                    }]
                },
                {
                    "type": "protocol_step",
                    "attrs": {"id": steps[1].id},
                    "content": [{
                        "type": "paragraph",
                        "attrs": {"align": None}}
                    ]}
            ]
        }


testString = labstep.helpers.getTime()


def newString():
    return labstep.helpers.getTime()


def experiment(empty=False):
    entity = user.newExperiment(testString)
    if empty is True:
        return entity
    entity.addProtocol(user.newProtocol(testString))
    entity.addMaterial(testString)
    return entity.update()


def protocol(empty=False):
    entity = user.newProtocol(testString)
    if empty is True:
        return entity

    entity.addComment(testString)
    entity.addMaterial(testString, amount='0.1', units='ml')
    entity.addTimer(name=testString, hours=4, minutes=15)
    entity.addTable(name=testString, data=tableData)
    steps = entity.addSteps(2)
    entity.edit(body=proseMirrorStateWithSteps(steps))

    return entity.update()


def experimentProtocol():
    entity = user.newExperiment(testString)
    experiment_protocol = entity.addProtocol(protocol())
    return experiment_protocol


def resource():
    entity = user.newResource(testString)
    entity.addMetadata(fieldName='test', value=testString)
    entity.addComment(testString)
    return entity.update()


def resourceCategory():
    entity = user.newResourceCategory(testString)
    resourceTemplate = entity.getResourceTemplate()
    resourceTemplate.addMetadata(fieldName='test', value=testString)
    entity.addComment(testString)
    return entity.update()


def orderRequest():
    new_resource = resource()
    entity = new_resource.newOrderRequest()
    entity.addMetadata(fieldName='test', value=testString)
    entity.addComment(testString)
    return entity.update()


def resourceItem():
    entity = resource().newItem(name='Pytest Acetone')
    entity.addMetadata(fieldName='test', value=testString)
    entity.addComment(testString)
    return entity.update()


def resourceLocation():
    return user.newResourceLocation(testString)


def workspace():
    return user.newWorkspace(testString)


def protocolCollection():
    return user.newCollection(newString(), type="protocol")


def experimentCollection():
    return user.newCollection(newString())
