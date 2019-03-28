import requests
import json

def getExperiments(user,count=100):
  '''
  Retrieve a list of a users Experiments on Labstep.
  
  Parameters
  ----------
  user : obj
    The Labstep user whose Experiments you want to retrieve. Must have property 'api_key'. See 'login'. 
  count : int
    The number of Experiments to retrieve. 

  Returns
  -------
  experiment
    A list of experiment objects.
  '''
  headers = {
    'apikey': user['api_key']
  }
  n = min(count,1000)
  url = f"https://api.labstep.com/api/generic/experiment-workflow?search=1&cursor=-1&count={n}"
  r = requests.get(
      url,
      headers=headers,
  )

  resp = json.loads(r.content)
  items = resp['items']

  expected_results = min(resp['total'],count)

  while len(items)<expected_results:
    cursor = resp['next_cursor']
    url = f"https://api.labstep.com/api/generic/experiment-workflow?search=1&cursor={cursor}&count={n}"
    r = requests.get(
        url,
        headers=headers,
    )

    resp = json.loads(r.content)
    items.extend(resp['items'])

  return items


