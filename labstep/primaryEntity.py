from .entity import Entity
from .comment import getComments, addCommentWithFile
from .tag import tag, getAttachedTags
from .permissions import getPermissions, newPermission, transferOwnership
from .sharelink import getSharelink


class ShareableEntity(Entity):
    __hasParentGroup__ = True

    def addComment(self, body, filepath=None, extraParams={}):
        """
        Add a comment and/or file to a Labstep Entity.

        Parameters
        ----------
        body (str)
            The body of the comment.
        filepath (str)
            A Labstep File entity to attach to the comment,
            including the filepath.

        Returns
        -------
        :class:`~labstep.comment.Comment`
            The comment added.

        Example
        -------
        ::

            my_experiment = user.getExperiment(17000)
            my_experiment.addComment(body='I am commenting!',
                                     filepath='pwd/file_to_upload.dat')
        """
        return addCommentWithFile(self, body=body,
                                  filepath=filepath,
                                  extraParams=extraParams)

    def getComments(self, count=100):
        """
        Retrieve the Comments attached to this Labstep Entity.

        Returns
        -------
        List[:class:`~labstep.comment.Comment`]
            List of the comments attached.

        Example
        -------
        ::

            entity = user.getExperiment(17000)
            comments = entity.getComments()
            comments[0].attributes()
        """
        return getComments(self, count)

    def getPermissions(self):
        """
        Returns the sharing permissions for the Entity.

        Returns
        -------
        List[:class:`~labstep.permissions.Permission`]
        """
        return getPermissions(self)

    def getSharelink(self):
        """
        Returns a sharelink for the Entity.

        Returns
        -------
        :class:`~labstep.sharelink.Sharelink`
            The sharelink for the entity
        """
        return getSharelink(self)

    def shareWith(self, workspace_id, permission='view'):
        """
        Shares the Entity with another Workspace.

        Parameters
        ----------
        workspace_id (int)
            The id of the workspace to share with

        permission (str)
            Permission to share with. Can be 'view' or 'edit'

        Returns
        -------
        None
        """
        return newPermission(self, workspace_id, permission)

    def transferOwnership(self, workspace_id):
        """
        Transfer ownership of the Entity to a different Workspace

        Parameters
        ----------
        workspace_id (int)
            The id of the workspace to transfer ownership to
        """
        return transferOwnership(self, workspace_id)


class PrimaryEntity(ShareableEntity):

    def addTag(self, name):
        """
        Add a tag to the Entity (creates a
        new tag if none exists).

        Parameters
        ----------
        name (str)
            The name of the tag to create.

        Returns
        -------
        :class:`~labstep.experiment.Experiment`
            The Experiment that was tagged.

        Example
        -------
        ::

            my_experiment = user.getExperiment(17000)
            my_experiment.addTag(name='My Tag')
        """
        tag(self, name)
        return self

    def getTags(self):
        """
        Retrieve the Tags attached to a this Labstep Entity.

        Returns
        -------
        List[:class:`~labstep.tag.Tag`]
            List of the tags attached.

        Example
        -------
        ::

            entity = user.getExperiment(17000)
            tags = entity.getTags()
            tags[0].attributes()
        """
        return getAttachedTags(self)
