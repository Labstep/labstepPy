import requests
import json

def getProtocols(user,count=100):
  headers = {
    'apikey': user['api_key']
  }
  n = min(count,1000)
  playlist_id = user['protocol_collection_playlists'][0]['id']
  url = f"https://api.labstep.com/api/generic/protocol-collection?search=1&cursor=-1&count={n}&protocol_collection_playlist_id={playlist_id}"
  r = requests.get(
      url,
      headers=headers,
  )

  resp = json.loads(r.content)
  items = resp['items']

  expected_results = min(resp['total'],count)

  while len(items)<expected_results:
    cursor = resp['next_cursor']
    url = f"https://api.labstep.com/api/generic/protocol-collection?search=1&cursor={cursor}&count={n}&protocol_collection_playlist_id={playlist_id}"
    r = requests.get(
        url,
        headers=headers,
    )

    resp = json.loads(r.content)
    items.extend(resp['items'])

  return items


