import pandas as pd
from datetime import datetime
import labstep
from labstep.generic.entityList.model import EntityList


## Authenticate user
user = labstep.authenticate()


workspace = user.getWorkspace(WORKSPACE_ID) ## Add ID of required workspace
print('Fetching devices')
devices = workspace.getDevices()

def export_devices(devices:EntityList, folder_target:str):
    df = pd.DataFrame()
    columns=['Labstep Device Category','Labstep Device ID','Device Name','QR Code URL']
    for device in devices:
        print(f'Exporting Device: {device.name}')
        row_json={}
        row_json['Labstep Device Category'] = None if device.getDeviceCategory() is None else device.getDeviceCategory().name
        row_json['Labstep Device ID']=device.id
        row_json['Device Name']=device.name
        row_json['QR Code URL']=f"https://app.labstep.com/perma-link/{device.guid}"

        metadatas = device.getMetadata()
        for metadata in metadatas:
            if metadata.label not in columns:columns.append(metadata.label)
        for column_name in columns:
            if column_name not in row_json:
                metadata_entity=device.getMetadata().get(column_name)
                row_json.update({column_name:metadata_entity.getValue() if metadata_entity is not None else None})
        row = pd.Series(row_json, name=device.id)  # create data frame row. indexed by labstep id. Keys must correspond to the columns defined above
        df_row = pd.DataFrame([row])
        df = pd.concat([df, df_row], axis=0, ignore_index=True)# add row to dataframe

      ## Get date and time of export
    now = datetime.now()

    # path / file name where csv will be saved.
    df.to_csv(f'{folder_target}/devices{now}.csv', index=False)


export_devices(devices=devices, folder_target='exported_devices')