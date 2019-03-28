import requests
import json

def createProject(user,name):
  data = {
    'name':name,
  }
  headers = {
    'apikey': user['api_key']
  }
  url = 'https://api.labstep.com/api/generic/group'
  r = requests.post(
      url,
      json=data,
      headers=headers,
  )
  return json.loads(r.content)