import requests
import json

def createProtocol(user,name):
  data = {
    'name':name,
  }
  headers = {
    'apikey': user['api_key']
  }
  url = 'https://api.labstep.com/api/generic/protocol'
  r = requests.post(
      url,
      json=data,
      headers=headers,
  )
  return json.loads(r.content)