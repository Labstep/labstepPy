Advance filters in Labstep using Python
##########################
Index
****************
.. contents:: Table of contents
    :depth: 3

Overview of the filterEntities method
************************************************
**LabstepPy** has the capability to fetch entities based on their attributes and their values,
as well as associated attributes and values of associated entitites. :func:`~labstep.generic.entity.repository.filterEntities` allows a user
to fetch entities of a certain class filtering them using a json object that contains the filter query.

Parameters
****************
- ``user`` ( :class:`~labstep.generic.entity.user.model.User` )
    The user that is making the query.

- `entityClass` ( ``Entity class`` )
    The class of the entity that is being filtered.

- `filter` ( ``List`` [``Dict`` [``str``, ``Any``], ...] )
    List required on this parameter is an array of dictionaries, where each dictionary represents a filter condition.
    The dictionary representing a filter conditions can have the following keys and are described below:

    - ``path`` ( ``str`` ) specifies the name of the entity class associated to the entity that is being filtered, i.e. ``metadatas``, ``tags`` .
    The paths that can be used differ depending on the entitites class.

    - ``type`` ( ``str`` ) specifies the logical operator of the filter condition. It can be ``and`` or ``or``.

    - ``predicates`` ( ``List`` ) specifies the filter condition and can have the following keys:

        - ``attribute`` (``str``) specifies the name of attribute of the entity that is being filtered. i.e. ``name``, ``datetime``. The attributes that can be used differ depending on the entitites class.

        - ``value`` ( ``str``, ``int``, ``float`` )  specifies the value of the attribute that is being filtered.

        - ``comparison`` ( ``str`` ) specifies the comparison operator used in attribute values. It can be ``equal_to``, ``not_equal_to``, ``less_than``, ``less_than_or_equal_to``, ``greater_than``, ``greater_than_or_equal_to``, ``like``, ``notLike``, ``isNull``, ``isNotNull``.

        - ``predicates`` ( ``List`` ) nested filter condition.

- `count` (``int``)
    Optional. Number of entities to fetch.

- `pageSize` (``int``)
    Optional. Splits the total number of entities into pages of size `pageSize`. Its default value is 50.

Examples
****************

Return Resource Items that have not been assigned to a user
----------------------------

Python code
===========
.. code-block:: python

    import labstep
    # Import filterEntities method
    from labstep.generic.entity.repository import filterEntities
    # Import ResourceItem class model
    from labstep.entities.resourceItem.model import ResourceItem

    # Authenticate user
    user = labstep.authenticate()

    # Set workspace
    user.setWorkspace(1)

    # Define the filter
    filter = [
        {
        "type":"and",
        "predicates":
            [
                {
                "type":"and",
                "path":"assigned_to",
                "predicates":
                [
                    {
                    "attribute":"guid",
                    "comparison":"isNull",
                    }
                ]
                }
            ]
        }
    ]

    # Call filter method
    resource_items = filterEntities(user, ResourceItem, filter)

Return Resources that were created between two dates
----------------------------

Python code
===========
.. code-block:: python

    import labstep
    # Import filterEntities method
    from labstep.generic.entity.repository import filterEntities
    # Import Resource class model
    from labstep.entities.resource.model import Resource

    # Authenticate user
    user = labstep.authenticate()

    # Set workspace
    user.setWorkspace(1)

    # Define the filter
    filter = [
        {
        "type":"and",
        "predicates":
        [
            {
            "type":"and",
            "predicates":
            [
                {
                "attribute":"created_at",
                "comparison":"gte",
                "value":"2025-01-01"
                },
                {
                "attribute":"created_at",
                "comparison":"lte",
                "value":"2025-12-31"
                }
            ]
            }
        ]
        }
    ]
    # Call filter method
    resources = filterEntities(user, Resource, filter)


Return deleted and non-deleted Resource Items that are under a specific Resource Category and their parent resource metadatas and item metadatas have been updated after a specific date
----------------------------

Python code
===========
.. code-block:: python

    import labstep
    # Import filterEntities method
    from labstep.generic.entity.repository import filterEntities
    # Import ResourceItem class model
    from labstep.entities.resourceItem.model import ResourceItem

    # Authenticate user
    user = labstep.authenticate()

    # Set workspace
    user.setWorkspace(1)

    #Get the resource category
    reosurce_category= user.getResourceCategory(1)

    # Set the last export time
    LAST_EXPORT_TIME = "2025-02-07T11:50:19+00:00"

    # Define the filter
    filter = [
    {
        "type": "and",
        "predicates": [
            {
                "path": "resource.template",
                "type": "and",
                "predicates": [
                    {
                        "attribute": "guid",
                        "comparison": "eq",
                        "value": reosurce_category.guid
                    }
                ]
            }
        ]
    },
    {
        "type": "or",
        "predicates": [
            {
                'attribute': 'deletedAt',
                'comparison': 'not_null',
            }, {
                'attribute': 'deletedAt',
                'comparison': 'null',
            },
        ]
    },
    {
        "type": "or",
        "predicates": [
            {
                "type": "and",
                "predicates": [
                    {
                        'attribute': 'updated_at',
                        'comparison': 'greater_than',
                        'value': LAST_EXPORT_TIME,
                    },
                ]
            },
            {
                "type": "and",
                "path": "metadatas",
                "predicates": [
                    {
                        'attribute': 'updated_at',
                        'comparison': 'greater_than',
                        'value': LAST_EXPORT_TIME,
                    },
                ]
            },
            {
                "type": "and",
                "path": "resource.metadatas",
                "predicates": [
                    {
                        'attribute': 'updated_at',
                        'comparison': 'greater_than',
                        'value': LAST_EXPORT_TIME,
                    },
                ]
            },
            ]
    }]
    # Call filter method
    resources = filterEntities(user, ResourceItem, filter)


Supported Entities
****************
.. dropdown:: Resource
    :color:  dark

    .. dropdown:: `Supported Paths`
        :color:  primary
        :open:

        .. dropdown:: `default`
            :color:  info

            .. dropdown::  Supported Attributes
                :open:

                .. dropdown::  `name`
                    :color:  secondary

                    .. dropdown::  Supported value format
                        :open:

                        - ``str``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``

                .. dropdown::  `deletedAt`
                    :color:  secondary

                    .. dropdown::  Supported value format
                        :open:

                        - Date as ``str`` in format ``YYYY-MM-DDTHH:MM:SS+00:00``
                        - Date as ``str`` in format ``YYYY-MM-DD``

                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``not_exists`` or ``null`` or ``isNull``
                        - ``exists`` or ``not_null`` or ``isNotNull``
                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``
                        - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                        - ``less_than`` or ``lt``
                        - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                        - ``greater_than`` or ``gt``

                .. dropdown::  `template`
                    :color:  secondary

                    .. dropdown::  Supported value format
                        :open:

                        - ``str``

                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``not_exists`` or ``null`` or ``isNull``
                        - ``exists`` or ``not_null`` or ``isNotNull``
                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``
                        - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                        - ``less_than`` or ``lt``
                        - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                        - ``greater_than`` or ``gt``

                .. dropdown::  `available_resource_item_count`
                    :color:  secondary

                    .. dropdown::  Supported value format
                        :open:

                        - ``int``

                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``exists`` or ``not_null`` or ``isNotNull``
                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``
                        - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                        - ``less_than`` or ``lt``
                        - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                        - ``greater_than`` or ``gt`

                .. dropdown::  `created_at`
                    :color:  secondary

                    .. dropdown::  Supported value format
                        :open:

                        - Date as ``str`` in format ``YYYY-MM-DDTHH:MM:SS+00:00``
                        - Date as ``str`` in format ``YYYY-MM-DD``

                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``exists`` or ``not_null`` or ``isNotNull``
                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``
                        - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                        - ``less_than`` or ``lt``
                        - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                        - ``greater_than`` or ``gt`

        .. dropdown:: `author`
            :color:  info

            .. dropdown:: Supported Attributes
                :open:

                .. dropdown::  `guid`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - ``str``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``

                .. dropdown::  `email`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - ``str``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``

        .. dropdown:: `assigned_to`
            :color:  info

            .. dropdown:: Supported Attributes
                :open:

                .. dropdown::  `guid`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - ``str``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``

                .. dropdown::  `email`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - ``str``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``

        .. dropdown:: `entityUsers`
            :color:  info

            .. dropdown:: Supported Attributes
                :open:

                .. dropdown::  `is_assigned`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - ``boolean``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``

        .. dropdown:: `entityUsers.user`
            :color:  info

            .. dropdown:: Supported Attributes
                :open:

                .. dropdown::  `guid`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - ``str``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``

                .. dropdown::  `email`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - ``str``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``


        .. dropdown:: `metadatas`
            :color:  info

            .. dropdown:: Supported Attributes
                :open:

                .. dropdown::  `created_at`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - Date as ``str`` in format ``YYYY-MM-DDTHH:MM:SS+00:00``
                        - Date as ``str`` in format ``YYYY-MM-DD``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``not_exists`` or ``null`` or ``isNull``
                        - ``exists`` or ``not_null`` or ``isNotNull``
                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``
                        - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                        - ``less_than`` or ``lt``
                        - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                        - ``greater_than`` or ``gt``

                .. dropdown::  `updated_at`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - Date as ``str`` in format ``YYYY-MM-DDTHH:MM:SS+00:00``
                        - Date as ``str`` in format ``YYYY-MM-DD``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``not_exists`` or ``null`` or ``isNull``
                        - ``exists`` or ``not_null`` or ``isNotNull``
                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``
                        - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                        - ``less_than`` or ``lt``
                        - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                        - ``greater_than`` or ``gt``

                .. dropdown::  `deleted_at`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - Date as ``str`` in format ``YYYY-MM-DDTHH:MM:SS+00:00``
                        - Date as ``str`` in format ``YYYY-MM-DD``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``not_exists`` or ``null`` or ``isNull``
                        - ``exists`` or ``not_null`` or ``isNotNull``
                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``
                        - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                        - ``less_than`` or ``lt``
                        - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                        - ``greater_than`` or ``gt``

                .. dropdown::  `label`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - ``str``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``

                .. dropdown::  `value`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - ``str``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``

                .. dropdown::  `options`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - ``str``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``contains`` or ``includes`` or ``like``
                        - ``not_contains`` or ``excludes`` or ``notLike``

                .. dropdown::  `date`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - Date as ``str`` in format ``YYYY-MM-DD``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``exists`` or ``not_null`` or ``isNotNull``
                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``
                        - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                        - ``less_than`` or ``lt``
                        - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                        - ``greater_than`` or ``gt``

                .. dropdown::  `datetime`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - Date as ``str`` in format ``YYYY-MM-DDTHH:MM:SS+00:00``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``exists`` or ``not_null`` or ``isNotNull``
                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``
                        - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                        - ``less_than`` or ``lt``
                        - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                        - ``greater_than`` or ``gt``

                .. dropdown::  `number`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - ``int``
                        - ``float``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``exists`` or ``not_null`` or ``isNotNull``
                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``
                        - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                        - ``less_than`` or ``lt``
                        - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                        - ``greater_than`` or ``gt``

                .. dropdown::  `unit`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - ``str``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``exists`` or ``not_null`` or ``isNotNull``
                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``
                        - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                        - ``less_than`` or ``lt``
                        - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                        - ``greater_than`` or ``gt``

                .. dropdown::  `file`
                    :color:  secondary

                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``exists`` or ``not_null`` or ``isNotNull``
                        - ``not_exists`` or ``null`` or ``isNull``

        .. dropdown:: `metadatas.molecule`
            :color:  info

            .. dropdown:: Supported Attributes
                :open:

                .. dropdown::  `inchis`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - ``str``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``contains`` or ``includes`` or ``like``
                        - ``not_contains`` or ``excludes`` or ``notLike``

        .. dropdown:: `template`
            :color:  info

            .. dropdown:: Supported Attributes
                :open:

                .. dropdown::  `guid`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - ``str``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``
                        - ``contains`` or ``includes`` or ``like``
                        - ``not_contains`` or ``excludes`` or ``notLike``

        .. dropdown:: `tags`
            :color:  info

            .. dropdown:: Supported Attributes
                :open:

                .. dropdown::  `id`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - ``int``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``

                .. dropdown::  `guid`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - ``str``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``

                .. dropdown::  `name`
                    :color:  secondary

                    .. dropdown:: Supported value format
                        :open:

                        - ``int``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``




.. dropdown:: ResourceItem
    :color:  dark

    .. dropdown:: `Supported Paths`
        :color:  primary
        :open:

        .. dropdown:: `default`
            :color:  info

            .. dropdown::  Supported Attributes
                :open:

                .. dropdown::  `created_at`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - Date as ``str`` in format ``YYYY-MM-DDTHH:MM:SS+00:00``
                            - Date as ``str`` in format ``YYYY-MM-DD``

                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``
                            - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                            - ``less_than`` or ``lt``
                            - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                            - ``greater_than`` or ``gt`

                .. dropdown::  `updated_at`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - Date as ``str`` in format ``YYYY-MM-DDTHH:MM:SS+00:00``
                            - Date as ``str`` in format ``YYYY-MM-DD``

                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``exists`` or ``not_null`` or ``isNotNull``
                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``
                            - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                            - ``less_than`` or ``lt``
                            - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                            - ``greater_than`` or ``gt`

                .. dropdown::  `deletedAt`
                    :color:  secondary

                    .. dropdown::  Supported value format
                        :open:

                        - Date as ``str`` in format ``YYYY-MM-DDTHH:MM:SS+00:00``
                        - Date as ``str`` in format ``YYYY-MM-DD``

                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``not_exists`` or ``null`` or ``isNull``
                        - ``exists`` or ``not_null`` or ``isNotNull``
                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``
                        - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                        - ``less_than`` or ``lt``
                        - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                        - ``greater_than`` or ``gt``

                .. dropdown::  `status`
                    :color:  secondary

                    .. dropdown::  Supported value format
                        :open:

                        - ``str``
                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``equals`` or ``equal_to`` or ``eq``
                        - ``not_equals`` or ``not_equal_to`` or ``neq``

                .. dropdown::  `protocolValueOrigin`
                    :color:  secondary

                    .. dropdown::  Supported Operator Comparisons
                        :open:

                        - ``exists`` or ``not_null`` or ``isNotNull``
                        - ``not_exists`` or ``null`` or ``isNull``

        .. dropdown:: `author`
            :color:  info

            .. dropdown::  Supported Attributes
                :open:

                .. dropdown::  `guid`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - ``str``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``

                .. dropdown::  `email`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - ``str``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``

        .. dropdown:: `assigned_to`
            :color:  info

            .. dropdown::  Supported Attributes
                :open:

                .. dropdown::  `guid`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - ``str``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``

                .. dropdown::  `email`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - ``str``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``


        .. dropdown:: `entityUsers`
            :color:  info

            .. dropdown::  Supported Attributes
                :open:

                .. dropdown::  `is_assigned`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - ``boolean``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``

        .. dropdown:: `entityUsers.user`
            :color:  info

            .. dropdown::  Supported Attributes
                :open:

                .. dropdown::  `guid`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - ``str``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``

                .. dropdown::  `email`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - ``str``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``

        .. dropdown:: `metadatas`
            :color:  info

            .. dropdown::  Supported Attributes
                :open:

                .. dropdown::  `updated_at`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - Date as ``str`` in format ``YYYY-MM-DDTHH:MM:SS+00:00``
                            - Date as ``str`` in format ``YYYY-MM-DD``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``exists`` or ``not_null`` or ``isNotNull``
                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``
                            - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                            - ``less_than`` or ``lt``
                            - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                            - ``greater_than`` or ``gt``

                .. dropdown::  `label`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - ``str``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``

                .. dropdown::  `value`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - ``str``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``

                .. dropdown::  `options`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - ``str``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``contains`` or ``includes`` or ``like``
                            - ``not_contains`` or ``excludes`` or ``notLike``

                .. dropdown::  `date`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - Date as ``str`` in format ``YYYY-MM-DD``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``exists`` or ``not_null`` or ``isNotNull``
                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``
                            - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                            - ``less_than`` or ``lt``
                            - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                            - ``greater_than`` or ``gt``

                .. dropdown::  `datetime`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - Date as ``str`` in format ``YYYY-MM-DDTHH:MM:SS+00:00``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``exists`` or ``not_null`` or ``isNotNull``
                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``
                            - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                            - ``less_than`` or ``lt``
                            - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                            - ``greater_than`` or ``gt``

                .. dropdown::  `number`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - ``int``
                            - ``float``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``exists`` or ``not_null`` or ``isNotNull``
                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``
                            - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                            - ``less_than`` or ``lt``
                            - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                            - ``greater_than`` or ``gt``

                .. dropdown:: `unit`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - ``str``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``exists`` or ``not_null`` or ``isNotNull``
                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``
                            - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                            - ``less_than`` or ``lt``
                            - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                            - ``greater_than`` or ``gt``

                .. dropdown::  `file`
                        :color:  secondary

                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``exists`` or ``not_null`` or ``isNotNull``
                            - ``not_exists`` or ``null`` or ``isNull``

        .. dropdown:: `resource.metadatas`
            :color: info

            .. dropdown::  Supported Attributes
                :open:

                .. dropdown::  `updated_at`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - Date as ``str`` in format ``YYYY-MM-DDTHH:MM:SS+00:00``
                            - Date as ``str`` in format ``YYYY-MM-DD``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``exists`` or ``not_null`` or ``isNotNull``
                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``
                            - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                            - ``less_than`` or ``lt``
                            - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                            - ``greater_than`` or ``gt``

                .. dropdown::  `label`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - ``str``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``

                .. dropdown::  `value`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - ``str``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``

                .. dropdown::  `options`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - ``str``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``contains`` or ``includes`` or ``like``
                            - ``not_contains`` or ``excludes`` or ``notLike``

                .. dropdown::  `date`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - Date as ``str`` in format ``YYYY-MM-DD``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``exists`` or ``not_null`` or ``isNotNull``
                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``
                            - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                            - ``less_than`` or ``lt``
                            - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                            - ``greater_than`` or ``gt``

                .. dropdown::  `datetime`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - Date as ``str`` in format ``YYYY-MM-DDTHH:MM:SS+00:00``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``exists`` or ``not_null`` or ``isNotNull``
                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``
                            - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                            - ``less_than`` or ``lt``
                            - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                            - ``greater_than`` or ``gt``

                .. dropdown::  `number`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - ``int``
                            - ``float``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``exists`` or ``not_null`` or ``isNotNull``
                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``
                            - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                            - ``less_than`` or ``lt``
                            - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                            - ``greater_than`` or ``gt``

                .. dropdown:: `unit`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - ``str``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``exists`` or ``not_null`` or ``isNotNull``
                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``
                            - ``less_than_or_equals`` or ``less_than_or_equal_to`` or ``lte``
                            - ``less_than`` or ``lt``
                            - ``greater_than_or_equals`` or ``greater_than_or_equal_to`` or ``gte``
                            - ``greater_than`` or ``gt``

                .. dropdown::  `file`
                        :color:  secondary

                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``exists`` or ``not_null`` or ``isNotNull``
                            - ``not_exists`` or ``null`` or ``isNull``

        .. dropdown:: `resourceLocation`
            :color:  info

            .. dropdown::  Supported Attributes
                :open:

                .. dropdown::  `guid`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - ``str``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``

        .. dropdown:: `resource.template`
            :color:  info

            .. dropdown::  Supported Attributes
                :open:

                .. dropdown::  `guid`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - ``str``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``

        .. dropdown:: `resource`
            :color:  info

            .. dropdown::  Supported Attributes
                :open:

                .. dropdown::  `guid`
                        :color:  secondary

                        .. dropdown::  Supported value format
                            :open:

                            - ``str``
                        .. dropdown::  Supported Operator Comparisons
                            :open:

                            - ``equals`` or ``equal_to`` or ``eq``
                            - ``not_equals`` or ``not_equal_to`` or ``neq``




