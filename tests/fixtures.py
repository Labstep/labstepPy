import labstep


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


def protocolWithElements(user):

    testName = labstep.helpers.getTime()
    new_entity = user.newProtocol(testName)
    entity = user.getProtocol(new_entity.id)
    entity.addComment(testName)
    entity.addMaterial(testName, amount='0.1', units='ml')
    entity.addTimer(name=testName, hours=4, minutes=15)
    entity.addTable(name=testName, data=tableData)
    steps = entity.addSteps(2)
    entity.edit(content_state=contentStateWithSteps(steps))

    return user.getProtocol(entity.id)


def experimentProtocol(user):
    testName = labstep.helpers.getTime()
    entity = user.newExperiment(testName)
    protocol = protocolWithElements(user)
    experiment_protocol = entity.addProtocol(protocol)
    return experiment_protocol
