#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Labstep <dev@labstep.com>
import pandas
from datetime import datetime
from time import gmtime, strftime
from labstep.constants import UNSPECIFIED
from labstep.service.config import configService


def url_join(*args):
    """
    Join a set of args with a slash (/) between them. Instead of
    checking for the presence of a slash, the slashes from both sides
    of each arg will be .strip() and then args .join() together.

    Returns
    -------
        returns "/".join(arg.strip("/") for arg in args)

    """
    return "/".join(arg.strip("/") for arg in args)


def getTime():
    """
    Returns
    -------
    timestamp
        The datetime NOW in GMT in json serializable format.
    """
    return strftime(
        "%Y-%m-%d" + "T" + "%H:%M:%S" + "+00:00", gmtime())


def formatDate(date, time=True):
    if date is None:
        return None

    if date is UNSPECIFIED:
        return UNSPECIFIED

    format = '%Y-%m-%d %H:%M:%S' if time else '%Y-%m-%d'

    return datetime.strptime(date, '%Y-%m-%dT%H:%M:%S+00:00').strftime(format)


def handleDate(date):
    """
    Returns
    -------
        The datetime for in json serializable format.
    """
    if date is None:
        return None

    if date is UNSPECIFIED:
        return UNSPECIFIED

    for fmt in ('%Y-%m-%d', '%Y-%m-%d %H:%M', '%Y-%m-%d %H:%M:%S'):
        try:
            return datetime.strptime(date, fmt).strftime('%Y-%m-%dT%H:%M:%S+00:00')
        except ValueError:
            pass
    raise ValueError(
        'Please Specify date in format: YY-MM-DD or YY-MM-DD HH:MM:SS')


def handleString(string):
    """
    Casts to string or returns None
    """
    if string is None:
        return None
    if string is UNSPECIFIED:
        return UNSPECIFIED

    return str(string)


def handleKeyword(string):
    """
    Returns
    -------
    string
        The string in lowercase, and any whitespace replaced with '_'.
    """
    if string is None:
        return None
    if string is UNSPECIFIED:
        return UNSPECIFIED

    else:
        return string.lower().replace(" ", "_")


def update(entity, newData):
    """
    Returns
    -------
    the updated entity
    """
    entity.__data__ = newData
    for key in newData:
        try:
            setattr(entity, key, newData[key])
        except:
            pass
    return entity


def getHeaders(user=None):
    if user is None:
        return {
            "User-Agent": configService.getUserAgent()
        }
    elif hasattr(user,'api_key'):
        return {
            "apikey": user.api_key,
            "User-Agent": configService.getUserAgent()
        }
    else:
        return {
            "Authorization": "Bearer " + user.token,
            "User-Agent": configService.getUserAgent()
        }


def boolToString(kv):
    """ convert bool values to 'true'/'false' strings for json compat """
    def enc(x): return x if not isinstance(
        x, bool) else 'true' if x else 'false'

    return None if kv is None else {k: enc(v) for k, v in kv.items()}


def filterUnspecified(obj):
    return None if obj is None else {k: v for (k, v) in obj.items() if v is not UNSPECIFIED}


def getKeyValues(obj):
    return obj.items() if isinstance(obj, dict) else enumerate(obj)


def getCellValue(cell):
    if 'value' not in cell:
        return None
    if isinstance(cell['value'], str):
        return str(cell['value']).strip()

    return cell['value']


def dataTableToDataFrame(dataTable):

    values = {
        str(rowKey): {
            str(columnKey): getCellValue(cell)
            for (columnKey, cell) in getKeyValues(row)
        } for (rowKey, row) in getKeyValues(dataTable)
    }

    header = values.pop('0')

    df = pandas.DataFrame(values).T.rename(columns=header)

    df = df.reset_index(drop=True)

    return df


def dataFrameToDataTable(df):

    headers = {'0': {str(colInd): {'value': colName}
                     for colInd, colName in enumerate(df.columns)}}

    dataTable = {
        str(int(rowInd)+1): {str(colInd): {'value': row[colName]} for colInd, colName in enumerate(df.columns)} for rowInd, row in df.iterrows()
    }

    data = {"rowCount": int(df.index[-1]) + 2, "columnCount": len(
        df.columns), "colHeaderData": {}, "data": {"dataTable": {**headers, **dataTable}}}

    return data


def linearToCartesianCoordinates(position, number_of_columns):

    mod = position % number_of_columns
    floor = position // number_of_columns

    y = floor if mod != 0 else floor - 1
    x = mod - 1 if mod != 0 else number_of_columns

    return [x, y]


def alphanumericToCartesianCoordinates(position):
    from re import match as rematch

    position = position.lower()

    m = rematch('([a-z]+)([0-9]+)', position)

    if m is None:
        print('Invalid position: {}'.format(position))
    else:
        row = 0
        for ch in m.group(1):
            row += ord(ch) - 96
        col = int(m.group(2))

    return [col, row]
