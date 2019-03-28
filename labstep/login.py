import requests
import json

def login(username,password):
  data = {
      'username': username,
      'password': password,
  }
  url = 'https://api.labstep.com/public-api/user/login'
  r = requests.post(
      url,
      json=data,
      headers={},
  )
  return json.loads(r.content)