import labstep

user = labstep.login('username', 'password')

user.setWorkspace()

experiment = user.newExperiment('Your First Experiment')

tableData = {
  'rowCount': 12,
  'columnCount': 12,
  'colHeaderData': [],
  'rowHeaderData': [],
  'columns': [{"size": 266}],
  "data":{"dataTable":{"0":{"0":{"value":"A"},"1":{"value":1}},"1":{"0":{"value":"B"},"1":{"value":2}},"2":{"0":{"value":"C"},"1":{"value":3}},"3":{"0":{"value":"Average"},"1":{"value":2,"formula":"AVERAGE(B1:B3)"}},"4":{"0":{"value":"Stdev"},"1":{"value":1,"formula":"STDEV(B1:B3)"}}}},"rows":[{"size":21},{"size":21},{"size":21},{"size":21},{"size":21}],"leftCellIndex":0,"topCellIndex":0
}

table = experiment.addTable('Table',data=tableData)

dataElement = experiment.addDataElement("Refractive Index",
                                   value="1.73")

body = {
    "type":"doc","content":[{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","marks":[{"type":"backgroundColor","attrs":{"backgroundColor":"#ffffff"}},{"type":"color","attrs":{"color":"#565867"}}],"text":"The experiment entry allows you to format your experiment report, add results, and create shortcuts to Protocols, Materials or Data elements all in a single document. To get started, simply doubled click anywhere on the entry page or click the pen icon to the bottom left of the page if you're on mobile."}]},{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"For more information about Labstep Experiments, visit "},{"type":"text","marks":[{"type":"link","attrs":{"href":"https://help.labstep.com/en/collections/2302419-notebook#experiments","title":"here"}}],"text":"here"},{"type":"text","text":"."}]},{"type":"heading","attrs":{"level":3},"content":[{"type":"text","text":"Introduction"}]},{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"Describe the purpose of the experiment here. "}]},{"type":"paragraph","attrs":{"align":None}},{"type":"heading","attrs":{"level":3},"content":[{"type":"text","text":"Materials"}]},{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"Click the (+) icon to add Materials to capture the inventory items and amounts used/created in the experiment."}]},{"type":"paragraph","attrs":{"align":None}},{"type":"heading","attrs":{"level":3},"content":[{"type":"text","text":"Methods"}]},{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"Describe your experiment workflow here, and simply drag & drop to add images or files."}]},{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"Click the (+) icon to link Protocols and formula-embedded Tables for capturing your methods:"}]},
    {"type":"experiment_table","attrs":{"id":table.id}},{"type":"paragraph","attrs":{"align":None}},{"type":"heading","attrs":{"level":3},"content":[{"type":"text","text":"Results"}]},{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"Add Data Elements to capture your results in a consistent format:"}]},{"type":"metadata","attrs":{"id":dataElement.id}},{"type":"paragraph","attrs":{"align":None}}]
}

experiment.edit(entry=body)