import requests
import json

def attachFile(user,entity,filepath,caption):
  headers = {
    'apikey': user['api_key']
  }
  files = {'file': open(filepath, 'rb')}
  url = 'https://api.labstep.com/api/generic/file/upload'
  r = requests.post(
      url,
      headers=headers,
      files=files,
  )
  lsFile = json.loads(r.content)

  data = {
      'body': caption,
      'thread_id': entity['thread']['id'],
      'file_id': [list(lsFile.keys())[0]]
  }
  url = 'https://api.labstep.com/api/generic/comment'

  r = requests.post(
      url,
      json=data,
      headers=headers,
  )

  return json.loads(r.content)


