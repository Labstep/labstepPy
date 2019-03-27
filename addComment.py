import requests
import json

def addComment(user,entity,comment):
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


