from .entity import Entity, editEntity


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
