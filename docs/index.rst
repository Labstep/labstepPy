.. labstepPy documentation master file, created by
   sphinx-quickstart on Tue Oct 29 14:21:12 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



labstepPy
=====================================


Introduction
------------
`Labstep <https://www.labstep.com>`_ is a flexible research 
environment that connects `your electronic notebook
<https://app.labstep.com/login>`_, inventory, applications,
and data in one collaborative workspace.

**labstepPy is a Python package for working with the Labstep API.**
This guide is for anyone who wants to automatically attach analysis scripts
and data to your experiments on Labstep.

All the labstepPy code is available under open source licenses
from repositories at `github <https://github.com/Labstep/labstepPy>`_.


Installation
------------
The *labstep* package can be easily installed using ``pip``.

Open the ``Terminal``, and do:

.. code-block:: bash

    pip install labstep


.. Citations
   ---------
   When using labstepPy in published work, please cite the following:
   ...
   Thank you!


Quick Example
-------------
The quick example below shows you how to attach
a Labstep Protocol to a Labstep Experiment.

To see what else labstepPy can do,
see more :ref:`example uses <example-uses>`.

.. literalinclude:: ../examples/example.py


Learning labstepPy
------------------

To learn more about how to use **labstepPy**, the navigation below
should help you find the best use of the *labstep* package for your
own specific purposes.

.. toctree::
   :caption: Quick Start
   :maxdepth: 2

   source/installation_login.rst
   
.. toctree::
   :caption: Entity Classes
   :maxdepth: 2

   source/user.rst
   source/workspace.rst
   source/experiment.rst
   source/protocol.rst
   source/resource.rst
   source/orderRequest.rst
   source/metadata.rst
   source/comment.rst
   source/tag.rst
   source/file.rst

.. toctree::
   :caption: Examples
   :maxdepth: 2

   source/example_uses.rst


Getting Involved
----------------
Please report any bugs or provide any feedback to **barney@labstep.com**.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
