.. labstepPy documentation master file, created by
   sphinx-quickstart on Tue Oct 29 14:21:12 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to labstepPy's documentation!
=====================================

Introduction
------------
`Labstep <https://www.labstep.com>`_ is a flexible research 
environment that connects `your electronic notebook <https://app.labstep.com/login>`_,
inventory, applications and data in one collaborative workspace.

**labstepPy is a Python package for working with the Labstep API.**
This guide is for anyone who wants to automatically attach analysis scripts
and data to your experiments on Labstep.


Installation
------------
The *labstep* package can be easily installed using ``pip``.
Open the ``Terminal``, and do:

.. code-block:: bash

    pip install labstep


Open Source
-----------
All the labstepPy code is available under open source licenses
from repositories at `<github>`_.


Citations
---------
When using labstepPy in published work, please cite the following:

...

Thank you!


Basic Example
-------------
The simple example below shows how a user would attach a Labstep protocol
to a Labstep experiment:

.. literalinclude:: ../examples/example.py


Classes
-------
The main classes within the *labstep* module are:

- :class:`~labstep.user.User`
- :class:`~labstep.experiment.Experiment`
- :class:`~labstep.protocol.Protocol`
- :class:`~labstep.resource.Resource`
- :class:`~labstep.metadata.Metadata`
- :class:`~labstep.orderRequest.OrderRequest`
- :class:`~labstep.workspace.Workspace`
- :class:`~labstep.file.File`
- :class:`~labstep.comment.Comment`
- :class:`~labstep.tag.Tag`


Getting Involved
----------------
Please report any bugs or provide any feedback to ...


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
