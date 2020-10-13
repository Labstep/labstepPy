import requests
import json
from .helpers import handleError


def parseHTML(authenticatedUser, html):
    """
    Converts HTML into the JSON format used in protocols
    and experiment entries.

    Parameters
    ----------
    authenticatedUser (:)
        An authenticated Labstep :class:`~labstep.user.User`
        (see :func:`~labstep.user.authenticate`)
    html (str)
        HTML to be converted (as a string).
    """
    headers = {
        'Authorization': f'Bearer {authenticatedUser.token}'
    }

    body = {
      "html": html
    }

    url = "https://html-converter.labstep.com"
    r = requests.post(url, json=body, headers=headers)
    handleError(r)
    return json.loads(r.content)
