import requests
import json

def login(username,password):
  '''
  Returns an authenticated labstep User object to allow you to interact with the labstep API.
  
  Parameters
  ----------
  username : str
    You labstep username
  password : obj
    Your labstep password

  Returns
  -------
  user
    An object representing a user on labstep.
  '''
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