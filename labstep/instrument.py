#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .primaryEntity import PrimaryEntity
from .entity import Entity, getEntity, getEntities, newEntity, editEntity
from .helpers import getTime
from .metadata import addMetadataTo, getMetadata
from .file import newFile

TYPE_DEFAULT = 'default'
TYPE_NUMERIC = 'numeric'
TYPE_FILE = 'file'

FIELDS = [
    TYPE_DEFAULT,
    TYPE_NUMERIC,
    TYPE_FILE,
]

ALLOWED_FIELDS = {
    TYPE_DEFAULT: [
        'value',
    ],
    TYPE_NUMERIC: [
        'number',
        'unit',
    ],
    TYPE_FILE: [
        'file_id',
    ]
}


def getInstrument(user, instrument_id):
    """
    Retrieve a specific Labstep Instrument.

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    instrument_id (int)
        The id of the Instrument to retrieve.

    Returns
    -------
    instrument
        An object representing a Labstep Instrument.
    """
    return getEntity(user, Instrument, id=instrument_id)


def getInstruments(user, count=100, search_query=None,
                   extraParams={}):
    """
    Retrieve a list of a user's Instruments on Labstep,
    which can be filtered using the parameters:

    Parameters
    ----------
    user (obj)
        The Labstep user. Must have property
        'api_key'. See 'login'.
    count (int)
        The number of Instruments to retrieve.
    search_query (str)
        Search for Instruments with this 'name'.
    extraParams (dict)
        Dictionary of extra filter parameters.

    Returns
    -------
    instruments
        A list of Instrument objects.
    """
    params = {'search_query': search_query,
              **extraParams}
    return getEntities(user, Instrument, count, params)


def newInstrument(user, name, extraParams={}):
    """
    Create a new Labstep Instrument.

    Parameters
    ----------
    user (obj)
        The Labstep user creating the Instrument.
        Must have property 'api_key'. See 'login'.
    name (str)
        Give your Instrument a name.

    Returns
    -------
    instrument
        An object representing the new Labstep Instrument.
    """
    params = {'name': name, **extraParams}
    return newEntity(user, Instrument, params)


def editInstrument(instrument, name=None, deleted_at=None,
                   extraParams={}):
    """
    Edit an existing Instrument.

    Parameters
    ----------
    instrument (obj)
        The Instrument to edit.
    name (str)
        The new name of the Experiment.
    deleted_at (str)
        The timestamp at which the Instrument is deleted/archived.
    instrument_category_id (obj)
        The id of the InstrumentCategory to add to a Instrument.

    Returns
    -------
    instrument
        An object representing the edited Instrument.
    """
    params = {'name': name,
              'deleted_at': deleted_at,
              **extraParams}
    return editEntity(instrument, params)


class Instrument(PrimaryEntity):
    """
    Represents a Instrument on Labstep.

    To see all attributes of the instrument run
    ::
        print(my_instrument)

    Specific attributes can be accessed via dot notation like so...
    ::
        print(my_instrument.name)
        print(my_instrument.id)
    """
    __entityName__ = 'instrument'

    def edit(self, name=None, extraParams={}):
        """
        Edit an existing Instrument.

        Parameters
        ----------
        name (str)
            The new name of the Instrument.

        Returns
        -------
        :class:`~labstep.instrument.Instrument`
            An object representing the edited Instrument.

        Example
        -------
        ::

            my_instrument = user.getInstrument(17000)
            my_instrument.edit(name='A New Instrument Name')
        """
        return editInstrument(self, name, extraParams=extraParams)

    def delete(self):
        """
        Delete an existing Instrument.

        Example
        -------
        ::

            my_instrument = user.getInstrument(17000)
            my_instrument.delete()
        """
        return editInstrument(self, deleted_at=getTime())

    def addMetadata(self, fieldName, fieldType="default",
                    value=None, date=None,
                    number=None, unit=None,
                    filepath=None,
                    extraParams={}):
        """
        Add Metadata to a Instrument.

        Parameters
        ----------
        fieldName (str)
            The name of the field.
        fieldType (str)
            The Metadata field type. Options are: "default", "date",
            "numeric", or "file". The "default" type is "Text".
        value (str)
            The value accompanying the fieldName entry.
        date (str)
            The date accompanying the fieldName entry. Must be
            in the format of "YYYY-MM-DD HH:MM".
        number (float)
            The numeric value.
        unit (str)
            The unit accompanying the number entry.
        filepath (str)
            Local path to the file to upload for type 'file'

        Returns
        -------
        :class:`~labstep.metadata.Metadata`
            An object representing the new Labstep Metadata.

        Example
        -------
        ::

            instrument = user.getInstrument(17000)
            metadata = instrument.addMetadata("Refractive Index",
                                               value="1.73")
        """
        return addMetadataTo(self,
                             fieldName=fieldName,
                             fieldType=fieldType,
                             value=value, date=date,
                             number=number, unit=unit,
                             filepath=filepath,
                             extraParams=extraParams)

    def getMetadata(self):
        """
        Retrieve the Metadata of a Labstep Instrument.

        Returns
        -------
        :class:`~labstep.metadata.Metadata`
            An array of Metadata objects for the Instrument.

        Example
        -------
        ::

            my_instrument = user.getInstrument(17000)
            metadatas = my_instrument.getMetadata()
            metadatas[0].attributes()
        """
        return getMetadata(self)

    def getData(self, count=100, search_query=None,
                extraParams={}):
        """
        Retrieve a list of the data sent by an instrument.

        Parameters
        ----------
        count (int)
            The total count of data points to return.
        search_query (str)
            Search for data points by name.
        extraParams (dict)
            Dictionary of extra filter parameters.

        Returns
        -------
        InstrumentData
            A list of InstrumentData objects.
        """
        params = {'search_query': search_query,
                  'instrument_id': self.id,
                  **extraParams}
        return getEntities(self.__user__, InstrumentData, count, params)

    def newData(self, fieldName, fieldType="text",
                text=None,
                number=None, unit=None,
                filepath=None,
                extraParams={}):
        """
        Send new data from the Instrument.

        Parameters
        ----------
        fieldName (str)
            The name of the data field being sent.
        fieldType (str)
            The type of data being sent. Options are: "text", "numeric",
            or "file".
        text (str)
            The text for a field of type 'text'.
        number (float)
            The number for a field of type 'numeric'.
        unit (str)
            The unit for a field of type 'numeric'.
        filepath (str)
            Local path to the file to upload for type 'file'.

        Returns
        -------
        :class:`~labstep.instrument.InstrumentData`
            An object representing the new Instrument Data.

        Example
        -------
        ::

            instrument = user.getInstrument(17000)
            data = instrument.newData("Temperature","numeric",
                                               number=173, unit='K')
        """
        if fieldType not in FIELDS:
            msg = "Not a supported data type '{}'".format(fieldType)
            raise ValueError(msg)

        if filepath is not None:
            file_id = newFile(self.__user__, filepath).id
        else:
            file_id = None

        allowedFieldsForType = set(ALLOWED_FIELDS[fieldType])
        fields = {
            'value': text,
            'number': number,
            'unit': unit,
            'file_id': file_id
        }
        fields = {k: v for k, v in fields.items() if v}
        fields = set(fields.keys())
        violations = fields - allowedFieldsForType
        if violations:
            msg = 'Unallowed fields [{}] for type {}'.format(
                ",".join(violations), fieldType)
            raise ValueError(msg)

        params = {'instrument_id': self.id,
                  'type': fieldType,
                  'name': fieldName,
                  'value': text,
                  'number': number,
                  'unit': unit,
                  'file_id': file_id,
                  **extraParams}

        return newEntity(self.__user__, InstrumentData, params)


class InstrumentData(Entity):
    __entityName__ = 'instrument-data'
