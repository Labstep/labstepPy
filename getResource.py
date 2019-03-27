import requests
import json

def getResource(user,id):
  headers = {
    'apikey': user['api_key']
  }
  url = f"https://api.labstep.com/api/generic/resource/{id}"
  r = requests.get(
      url,
      headers=headers,
  )
  return json.loads(r.content)


