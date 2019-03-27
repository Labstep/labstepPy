import requests
import json

def getProject(user,id):
  headers = {
    'apikey': user['api_key']
  }
  url = f"https://api.labstep.com/api/generic/group/{id}"
  r = requests.get(
      url,
      headers=headers,
  )
  return json.loads(r.content)


