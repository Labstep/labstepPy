from .entity import Entity, editEntity, newEntity
import requests
from .config import API_ROOT
from .helpers import url_join, handleError, getHeaders


def newSharelink(user, fields):
    return newEntity(user, Sharelink, fields)


class Sharelink(Entity):
    """
     Represents a Sharelink on Labstep.
    """
    __entityName__ = 'share-link'
    __isLegacy__ = True

    def edit(self, permission=None, extraParams={}):
        """
        Edit an existing ResourceLocation.

        Parameters
        ----------
        permission (str)
            Set the permission granted by the sharelink
            can be either 'view' or 'edit'

        Returns
        -------
        :class:`~labstep.sharelink.Sharelink`
            An object representing the edited Sharelink.

        Example
        -------
        ::

            # Get an experiment
            experiment = user.getExperiment(123)

            # Get the sharelink for the experiment
            sharelink = experiment.getSharelink()

            # Edit the sharelink
            sharelink.edit(type='view')
        """
        fields = {
            "type": permission,
            **extraParams,
        }
        return editEntity(self, fields=fields)

    def sendEmails(self, emails, message=None):
        """
        Send sharelinks to collaborators via email.

        Parameters
        ----------
        emails (list)
            A list of the emails to send the invite to.
        message (str)
            A message to send with the invite.

        Returns
        -------
        None

        Example
        -------
        ::

        sharelink.
        sendEmails(emails=['collegue1@labstep.com','collegue2@labstep.com'],
        message='Hi, please collaborate with me on Labstep!')
        """
        headers = getHeaders(self.__user__)

        url = url_join(API_ROOT, "api/generic/share-link/email")
        fields = {
            "emails": emails,
            "message": message,
            "id": self.id
        }
        r = requests.post(url, json=fields, headers=headers)
        handleError(r)