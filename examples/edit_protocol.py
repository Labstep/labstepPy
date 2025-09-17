import os
import labstep

## Authenticate user
user = labstep.authenticate(USERNAME, APIKEY) # Replace with authenitcation credentials


## Set to the ID of the workspace to import into.
user.setWorkspace(WORKSPACE_ID) # Replace with workspace ID

## Create a protocol
protocol = user.newProtocol(name="API protocol")


## Add text to protocol body
body = {
    'type': 'doc',
    'content': [
        {
            'type': 'paragraph',
            'attrs': {
                'align': None
            }
        },
        {
            'type': 'paragraph',
            'attrs': {
                'align': None
            },
            'content': [
                {
                    'text': 'This is a new paragraph',
                    'type': 'text'
                }
            ]
        },
        {
            'type': 'paragraph',
            'attrs': {
                'align': None
            }
        }
    ]
}

protocol.edit(body=body)


## Adding a file / image to the body (images rendered automatically)

body = protocol.getBody()

file = experiment.addFile(os.path.abspath(__file__)) ## Replace with path to file

newContent = {
    "type": "paragraph",
    "attrs": {"align": None},
    "content": [
       {
        "type": "file", ## NOTE: this type of node MUST be embdedded in a paragraph node
        "attrs": {
            "id": file["id"],
            "fullWidth": False
            }
        }
    ]
}

body['content'].append(newContent)

protocol.edit(body=body)