import labstep
import pandas as pd

user = labstep.authenticate(apikey="YOUR_API_KEY")  # replace with your API key

workspace = user.getWorkspace(WORKSPACE_ID)  # replace with your workspace ID

# Get Items in Workspace

resourceItems = workspace.getResourceItems()

# Initialise data frame to store data
df = pd.DataFrame()  # change the columns / names as you want

for item in resourceItems:

    resource_metadata = item.resource.getMetadata()
    item_metadata = item.getMetadata()

    row_json ={
        'Item ID': item.guid,
        'Item Name': item.name,
        'Resource Name': item.resource.name,
        'Resource ID': item.resource.guid,
        'Amount in Stock': f'{item.amount} {item.unit}',
        'Location': item.resource_location['location_path'] if item.resource_location else None,
        'QR Code URL': f"https://app.labstep.com/perma-link/{item.guid}"
    }

    for metadata in resource_metadata + item_metadata:

        value = metadata.getValue()

        ## If it's a file type metadata, save a local copy of the file and just return the file name in the csv
        if metadata.type == 'file':
            files = value if isinstance(value, list) else [value]
            value = ''
            for file in files:
                file.save()
                value += file.name

        row_json[metadata.label] = value

    row = pd.Series(row_json, name=item.id)
    df_row = pd.DataFrame([row])
    df = pd.concat([df, df_row], axis=0, ignore_index=True) # add row to dataframe

# path / file name where csv will be saved.
df.to_csv('inventory_export.csv', index=False)
