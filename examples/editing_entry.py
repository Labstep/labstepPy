import labstep
import os
import pandas as pd
from labstep.service.helpers import dataFrameToDataTable

user = labstep.authenticate()

initialEntry = {
  "type": "doc",
  "content": []
}

experiment = user.newExperiment('API Experiment',entry=initialEntry)

# Adding text to the entry

entry = experiment.getEntry()

newContent = {
    "type": "paragraph",
    "attrs": {"align": None},
    "content": [
        {
            "type": "text", ## NOTE: this type of node MUST be embdedded in a paragraph node
            "text": "This is a new paragraph"
        }
    ]
}

entry['content'].append(newContent)

experiment.edit(entry=entry)

## Adding a file / image to the entry (images rendered automatically)

entry = experiment.getEntry()

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

entry['content'].append(newContent)

experiment.edit(entry=entry)

## Adding a data field to the entry

dataField = experiment.addDataField('My Data Field',fieldType='file')

file = user.newFile(os.path.abspath(__file__)) ## Replace with path to file

dataField.setValue(file)

newContent = {"type": "metadata", "attrs": {"id": dataField["id"]}}

entry['content'].append(newContent)

experiment.edit(entry=entry)


## Adding an inventory field to the entry

inventoryField = experiment.addInventoryField('Sample')

newContent = {
    "type": "paragraph",
    "attrs": {"align": None},
    "content": [
        {
           "type": "protocol_value", ## NOTE: this type of node MUST be embdedded in a paragraph node
           "attrs": {"id": inventoryField["id"]}
        }
    ]
}

entry['content'].append(newContent)

experiment.edit(entry=entry)


## Adding an inline spreadsheet to the entry

df = pd.read_excel('spreadsheet.xlsx')

dataTable = dataFrameToDataTable(df)

table = experiment.addTable('Spreadsheet 1',data=dataTable)

newContent = {"type": "protocol_table", "attrs": {"id": table["id"]}}

entry['content'].append(newContent)

experiment.edit(entry=entry)

## Adding a protocol to the entry

protocol = user.newProtocol('My Protocol')

experiment_protocol = experiment.addProtocol(protocol)

newContent = {
    "type": "paragraph",
    "attrs": {"align": None},
    "content": [
        {
           "type": "experiment", ## NOTE: this type of node MUST be embdedded in a paragraph node
           "attrs": {"id": experiment_protocol["id"]}
        }
    ]
}

entry['content'].append(newContent)

experiment.edit(entry=entry)


## Adding a basic table to the entry

newContent = {
  "type": "table",
  "content": [
    {
      "type": "table_row",
      "content": [
        {
          "type": "table_cell",
          "attrs": {
            "colspan": 1,
            "rowspan": 1,
            "colwidth": None,
            "background": None
          },
          "content": [
            {
              "type": "paragraph",
              "attrs": {
                "align": None
              },
              "content": [
                {
                  "type": "text",
                  "text": "Column 1"
                }
              ]
            }
          ]
        },
        {
          "type": "table_cell",
          "attrs": {
            "colspan": 1,
            "rowspan": 1,
            "colwidth": None,
            "background": None
          },
          "content": [
            {
              "type": "paragraph",
              "attrs": {
                "align": None
              },
              "content": [
                {
                  "type": "text",
                  "text": "Column 2"
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "table_row",
      "content": [
        {
          "type": "table_cell",
          "attrs": {
            "colspan": 1,
            "rowspan": 1,
            "colwidth": None,
            "background": None
          },
          "content": [
            {
              "type": "paragraph",
              "attrs": {
                "align": None
              }
            }
          ]
        },
        {
          "type": "table_cell",
          "attrs": {
            "colspan": 1,
            "rowspan": 1,
            "colwidth": None,
            "background": None
          },
          "content": [
            {
              "type": "paragraph",
              "attrs": {
                "align": None
              }
            }
          ]
        }
      ]
    }
  ]
}

entry['content'].append(newContent)

experiment.edit(entry=entry)

'''
For other elements or formatting options...
Please use the web app to produce the desired result and
inspect the network request sent to see the shape of the JSON document object
'''
