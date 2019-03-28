import requests
import json

def getResources(user,count=100):
  '''
  Retrieve a list of a users Resources on Labstep.
  
  Parameters
  ----------
  user : obj
    The Labstep user whose Resources you want to retrieve. Must have property 'api_key'. See 'login'. 
  count : int
    The number of Resources to retrieve. 

  Returns
  -------
  resources
    A list of resource objects.
  '''
  headers = {
    'apikey': user['api_key']
  }
  n = min(count,1000)
  playlist_id = user['resource_lists'][0]['id']
  url = f"https://api.labstep.com/api/generic/resource?search=1&cursor=-1&count={n}&resource_list_id={playlist_id}"
  r = requests.get(
      url,
      headers=headers,
  )

  resp = json.loads(r.content)
  items = resp['items']

  expected_results = min(resp['total'],count)

  while len(items)<expected_results:
    cursor = resp['next_cursor']
    url = f"https://api.labstep.com/api/generic/resource?search=1&cursor={cursor}&count={n}&resource_list_id={playlist_id}"
    r = requests.get(
        url,
        headers=headers,
    )

    resp = json.loads(r.content)
    items.extend(resp['items'])

  return items


