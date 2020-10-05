from .entity import Entity, editEntity


class Autoshare(Entity):
    """
    Represents an Autosharing rule on Labstep.
    """
    __entityName__ = 'security-policy'
    __isLegacy__ = True

    def edit(self,
             experiment_sharing=None,
             protocol_sharing=None,
             resource_sharing=None,
             extraParams={}):
        """
        Edit an autosharing policy.

        Parameters
        ----------
        experiment_sharing (str)
            Automatically share experiments
            you create and own with this workspace. Set to True or False

        protocol_sharing (str)
            Automatically share protocols
            you create and own with this workspace. Set to True or False

        resource_sharing (str)
            Automatically share resources
            you create and own with this workspace. Set to True or False


        Returns
        -------
        :class:`~labstep.autoshare.Autoshare`
            An object representing the Autosharing policy.

        Example
        -------
        ::

            # Get an workspace
            workspace = user.getWorkspace(123)

            # Set autosharing policy
            policy = workspace.setAutosharing(experiment_sharing=True)

            # Edit the policy
            policy.edit(protocol_sharing=True)
        """
        options = {
            True: 'edit',
            False: 'none',
            None: None
        }

        fields = {
            "experiment_workflow": options[experiment_sharing],
            "protocol_collection": options[protocol_sharing],
            "resource": options[resource_sharing],
            **extraParams,
        }
        return editEntity(self, fields=fields)
