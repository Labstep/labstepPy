
from .entity import Entity, editEntity


def editMolecule(molecule,
                 data=None, svg=None, table_data=None, extraParams={}):
    """
    Edit the value of an existing Molecule.

    Parameters
    ----------
    molecule (obj)
        The Molecule to edit.
    data (str)
        The MOL data in MOL V2000 format.
    svg (str)
        An svg preview of the molecular structure.

    Returns
    -------
    molecule
        An object representing the edited Molecule.
    """
    filterParams = {'datat': data,
                    'svg': svg,
                    'table_data': table_data
                    }
    params = {**filterParams, **extraParams}
    return editEntity(molecule, params)


class Molecule(Entity):
    """
    Represents a Molecule entity that may be attached to a metadata field, data element or note.

    To see the attributes of the molecule field run
    ::
        print(my_molecule)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(my_molecule.data)
        print(my_molecule.id)
    """
    __entityName__ = 'comment-molecule'

    def edit(self, data=None, svg=None, table_data=None, extraParams={}):
        """
        Edit the value of an existing Metadata.

        Parameters
        ----------
        fieldName (str)
            The new name of the field.
        value (str)
            The new value of the Metadata.

        Returns
        -------
        :class:`~labstep.metadata.Metadata`
            An object representing the edited Metadata.

        Example
        -------
        ::

            metadata.edit(value='2.50')
        """
        return editMolecule(self,
                            data=data,
                            svg=svg,
                            table_data=table_data,
                            extraParams=extraParams)
