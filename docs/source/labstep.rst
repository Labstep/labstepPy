.. sectnum::


Installation
==============================================
The *labstep* package can be easily installed using ``pip``.
Open the ``Terminal``, and do:

.. code-block:: bash

    pip install labstep



Setup
==============================================
Once installed, every session starts with importing
the *labstep* module and accessing your Labstep account
using either the :func:`~labstep.user.authenticate` or 
the :func:`~labstep.user.login` functions below:

Authenticate
----------------------------------------------

.. autofunction:: labstep.user.authenticate


Login
----------------------------------------------

.. autofunction:: labstep.user.login



Classes
==============================================

User
----------------------------------------------

.. autoclass:: labstep.user.User
   :members:
   :undoc-members:

Experiment
----------------------------------------------

.. autoclass:: labstep.experiment.Experiment
   :members:
   :undoc-members:

Protocol
----------------------------------------------

.. autoclass:: labstep.protocol.Protocol
   :members:
   :undoc-members:

Resource
----------------------------------------------

.. autoclass:: labstep.resource.Resource
   :members:
   :undoc-members:

Metadata
----------------------------------------------

.. autoclass:: labstep.metadata.Metadata
   :members:
   :undoc-members:

ResourceCategory
----------------------------------------------

.. autoclass:: labstep.resourceCategory.ResourceCategory
   :members:
   :undoc-members:

ResourceLocation
----------------------------------------------

.. autoclass:: labstep.resourceLocation.ResourceLocation
   :members:
   :undoc-members:

OrderRequest
----------------------------------------------

.. autoclass:: labstep.orderRequest.OrderRequest
   :members:
   :undoc-members:

Workspace
----------------------------------------------

.. autoclass:: labstep.workspace.Workspace
   :members:
   :undoc-members:

File
----------------------------------------------

.. autoclass:: labstep.file.File
   :members:
   :undoc-members:

Comment
----------------------------------------------

.. autoclass:: labstep.comment.Comment
   :members:
   :undoc-members:

Tag
----------------------------------------------

.. autoclass:: labstep.tag.Tag
   :members:
   :undoc-members:



.. _example-uses:

Example Uses
==============================================

Experiment Setup
----------------------------------------------
To setup an Experiment on Labstep:

:download:`experiment_setup.py <../../examples/experiment_setup.py>`

.. literalinclude:: ../../examples/experiment_setup.py


Importing Resources
----------------------------------------------
To import a list of resources into Labstep
from a *resource_import.csv* file:

:download:`resource_import.csv <../../examples/resource_import.csv>`

.. program-output:: python -c 'import pandas; print(pandas.read_csv("~/labstepPy/examples/resource_import.csv"))'

:download:`resource_import.py <../../examples/resource_import.py>`

.. literalinclude:: ../../examples/resource_import.py


Deleting Multiple Entities
----------------------------------------------
To delete a list of Entities from
a specific Workspace on Labstep:

:download:`delete_multiple.py <../../examples/delete_multiple.py>`

.. literalinclude:: ../../examples/delete_multiple.py



.. Acknowledgements
   ==============================================
   We acknowledge the use of the following resources:


