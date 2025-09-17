import labstep
import pandas as pd

user = labstep.authenticate()

user.setWorkspace(WORKSPACE_ID) ## Enter Labstep target workspace ID

## Create device category and template
device_category = user.newDeviceCategory('My new device category')

device_template = device_category.getDeviceTemplate()

device_template.addMetadata(fieldName="Serial Number", fieldType="default")
device_template.addMetadata(fieldName="Manufacturer", fieldType="default")
device_template.addMetadata(fieldName="Service date", fieldType="date")

## Create devices
df = pd.read_excel('devices.xlsx')

for index, row in df.iterrows():
    newDevice = user.newDevice(name=row['Device name'], device_category_id=device_category.id)
    newDevice.addMetadata(fieldName='Serial Number', fieldType='default', value=row['Serial Number'])
    newDevice.addMetadata(fieldName='Manufacturer', fieldType='default', value=row['Manufacturer'])
    newDevice.addMetadata(fieldName='Service date', fieldType='date', date=str(row['Service date']))