import requests
import json

def addComment(user,entity,comment):
  '''Add a comment to a labstep entity such as an experiment or resource
  Parameters
  ----------
  user : obj
    The labstep user to comment as. Must have property 'api_key'. See 'login'.
  entity : obj
    The labstep entity to comment on. Must have 'thread' property with property 'id'.
  comment : str
    The body of the comment

  Returns
  -------
  comment
    An object representing a comment on labstep.
  '''
  headers = {
    'apikey': user['api_key']
  }
  threadId = entity['thread']['id']
  data = {
      'body': comment,
      'thread_id': threadId,
  }
  url = 'https://api.labstep.com/api/generic/comment'
  r = requests.post(
      url,
      json=data,
      headers=headers,
  )
  return json.loads(r.content)


