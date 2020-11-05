import labstep

user = labstep.login('username', 'password')

user.setWorkspace()

protocol = user.newProtocol('Labstep Protocol Guide')
protocol_steps = protocol.addSteps(7)
image = user.newFile(filepath="./protocol_image.png")
sample1 = user.newResource(name="Sample 1")
sample_resource = protocol.addMaterial(name="Sample Resource", amount="12", units="mL", resource_id=sample1.id)
unspecified_resource = protocol.addMaterial(name="Unspecified Resource", amount="12", units="mL")
data_numeric = protocol.addDataElement(fieldName="Melting Temperature", fieldType="default")
data_file = protocol.addDataElement(fieldName="Raw Data", fieldType="file")
data_reaction = protocol.addDataElement(fieldName="Reaction Scheme", fieldType="default")
data_plasmid = protocol.addDataElement(fieldName="Plasmid map", fieldType="default")
timer = protocol.addTimer(name="Timer", minutes=2)


body = {
    "type":"doc","content":[
        {"type":"heading","attrs":{"level":3},"content":[{"type":"text","text":"Introduction"}]},{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"Labstep Protocols make it "},{"type":"text","marks":[{"type":"strong"}],"text":"quick"},{"type":"text","text":" and "},{"type":"text","marks":[{"type":"strong"}],"text":"easy"},{"type":"text","text":" to keep an accurate record of your experimental work."}]},{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"Each time you "},{"type":"text","marks":[{"type":"strong"}],"text":"'Start'"},{"type":"text","text":" a Labstep Protocol you can capture:"}]},{"type":"bullet_list","content":[{"type":"list_item","content":[{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"The experimental / analytical methods performed"}]}]},{"type":"list_item","content":[{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"The materials used."}]}]},{"type":"list_item","content":[{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"Variable parameters or conditions"}]}]},{"type":"list_item","content":[{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"Data files produced. "}]}]}]},{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"Along with any miscellaneous notes and observations you make along the way! For more information about Labstep Protocols, click "},{"type":"text","marks":[{"type":"link","attrs":{"href":"https://help.labstep.com/en/articles/3142376-creating-importing-and-editing-protocols","title":"here"}}],"text":"here"},{"type":"text","text":"."}]},{"type":"heading","attrs":{"level":3},"content":[{"type":"text","text":"Tracking Methods"}]},{"type":"protocol_step","attrs":{"id":protocol_steps[0].id},"content":[{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"Use "},{"type":"text","marks":[{"type":"strong"}],"text":"Steps "},{"type":"text","text":"to indicate actions to be performed. Each time you run a Protocol you can mark the steps as complete to track progress."}]},{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"Try now by click the 'tick' icon on the left of the step card."}]}]},{"type":"paragraph","attrs":{"align":None}},{"type":"protocol_step","attrs":{"id":protocol_steps[1].id},"content":[{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"Add notes and observations to steps by clicking the 'comment' icon in the bottom right of each step."}]}]},{"type":"paragraph","attrs":{"align":None}},{"type":"heading","attrs":{"level":3},"content":[{"type":"text","text":"Tracking Materials"}]},{"type":"protocol_step","attrs":{"id":protocol_steps[2].id},"content":[{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"Match materials listed in the protocol to "},{"type":"text","marks":[{"type":"strong"}],"text":"resources "},{"type":"text","text":"from your inventory to quickly pull up more information and track which item / batch in each run."}]},{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"Click "},{"type":"protocol_value","attrs":{"id":sample_resource.id}},{"type":"text","text":"  to see more information and select the specific item used."}]}]},{"type":"paragraph","attrs":{"align":None}},{"type":"protocol_step","attrs":{"id":protocol_steps[3].id},"content":[{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"You can also leave the amount or resource unspecified if it will be different each time the protocol is run."}]},{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"For example, click "},{"type":"protocol_value","attrs":{"id":unspecified_resource.id}},{"type":"text","text":" to specify the sample and amount used."}]}]},{"type":"paragraph","attrs":{"align":None}},{"type":"heading","attrs":{"level":3},"content":[{"type":"text","text":"Capturing Data"}]},{"type":"protocol_step","attrs":{"id":protocol_steps[4].id},"content":[{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"You can use Data elements as a quick way to capture variable parameters involved in your method."}]},{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"For example, click 'Add default' below to specify the temperature."}]},{"type":"metadata","attrs":{"id":data_numeric.id}}]},{"type":"paragraph","attrs":{"align":None}},{"type":"protocol_step","attrs":{"id":protocol_steps[5].id},"content":[{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"Data Elements can also be used to help you capture your Data in a consistent fashion."}]},{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"For example, click 'Add default' to upload a data file."}]},{"type":"metadata","attrs":{"id":data_file.id}},{"type":"paragraph","attrs":{"align":None}},{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"For chemistry protocols you can use Data Elements to insert molecular structures or reaction schemes into your Protocol such as the one below."}]},{"type":"metadata","attrs":{"id":data_reaction.id}},{"type":"paragraph","attrs":{"align":None}},{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"For molecular biology protocols you can insert interactive plasmid maps."}]},{"type":"metadata","attrs":{"id":data_plasmid.id}}]},{"type":"paragraph","attrs":{"align":None}},{"type":"heading","attrs":{"level":3},"content":[{"type":"text","text":"Tracking Time"}]},{"type":"protocol_step","attrs":{"id":protocol_steps[6].id},"content":[{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"Use timers to track time sensitive steps."}]},{"type":"paragraph","attrs":{"align":None},"content":[{"type":"text","text":"Click the interactive element to test it out -> "},{"type":"text","text":" "},{"type":"protocol_timer","attrs":{"id":timer.id}}]}]},{"type":"paragraph","attrs":{"align":None}},{"type":"paragraph","attrs":{"align":None}},{"type":"paragraph","attrs":{"align":None}},{"type":"paragraph","attrs":{"align":None}}
    ]
}

protocol.edit(body=body)