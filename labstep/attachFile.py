import requests
import json

def attachFile(user,entity,filepath,caption):
  '''Attach a file to a labstep entity such as an experiment or resource. Optionally include a cpation describing the file.
  Parameters
  ----------
  user : obj
    The labstep user to attach as. Must have property 'api_key'. See 'login'.
  entity : obj
    The labstep entity to attach to. Must have 'thread' property with property 'id'.
  filepath : str
    The filepath to the file to attach
  caption : str
    An optional caption for the file.

  Returns
  -------
  comment
    An object representing a comment on labstep.
  '''
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


