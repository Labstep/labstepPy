import requests
import json

def getProtocol(user,id):
  headers = {
    'apikey': user['api_key']
  }
  url = f"https://api.labstep.com/api/generic/protocol/{id}"
  r = requests.get(
      url,
      headers=headers,
  )
  return json.loads(r.content)


