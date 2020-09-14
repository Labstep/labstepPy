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


contentStateEmpty = {
    "object": "value",
    "document": {
        "object": "document",
        "data": [],
        "nodes": [
                {
                    "object": "block",
                    "type": "paragraph",
                    "isVoid": False,
                    "data": [],
                    "nodes": [
                        {
                            "object": "text",
                            "leaves": [
                                {
                                    "object": "leaf",
                                    "text": " ",
                                    "marks": []
                                }
                            ]
                        }
                    ]
                },
        ]
    }
}


testString = labstep.helpers.getTime()


def newString():
    return labstep.helpers.getTime()


def contentStateWithSteps(steps):
    return {
        "object": "value",
        "document": {
            "object": "document",
            "data": [],
            "nodes": [
                {
                    "object": "block",
                    "type": "paragraph",
                    "isVoid": False,
                    "data": [],
                    "nodes": [
                        {
                            "object": "text",
                            "leaves": [
                                {
                                    "object": "leaf",
                                    "text": " ",
                                    "marks": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "object": "block",
                    "type": "protocol_step",
                    "isVoid": False,
                    "data": {"id": steps[0].id},
                    "nodes": [
                        {
                            "object": "text",
                            "leaves": [
                                {
                                    "object": "leaf",
                                    "text": " ",
                                    "marks": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "object": "block",
                    "type": "protocol_step",
                    "isVoid": False,
                    "data": {"id": steps[1].id},
                    "nodes": [
                        {
                            "object": "text",
                            "leaves": [
                                {
                                    "object": "leaf",
                                    "text": " ",
                                    "marks": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "isVoid": False,
                    "data": [],
                    "nodes": [
                        {
                            "object": "text",
                            "leaves": [
                                {
                                    "object": "leaf",
                                    "text": " ",
                                    "marks": []
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    }


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
    entity.edit(content_state=contentStateWithSteps(steps))

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
    entity.addMetadata(fieldName='test', value=testString)
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
