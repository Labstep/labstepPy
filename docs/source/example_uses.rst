.. _example-uses:

Workspace Setup
----------------------------------------------
To setup a Workspace on Labstep:

:download:`workspace_setup.py <../../examples/workspace_setup.py>`

.. literalinclude:: ../../examples/workspace_setup.py


Importing Resources
----------------------------------------------
To import a list of resources into Labstep
from a *resource_import.csv* file:

:download:`resource_import.csv <../../examples/resource_import.csv>`

:download:`resource_import.py <../../examples/resource_import.py>`

.. literalinclude:: ../../examples/resource_import.py


Deleting Multiple Entities
----------------------------------------------
You can use **labstep.entities.y.model** to easily delete
multiple different Entities on Labstep (a list
of Experiments, Protocols, or Tags, etc.),
either from within a specific Workspace or by
performing a global delete.

:download:`delete_multiple.py <../../examples/delete_multiple.py>`

.. literalinclude:: ../../examples/delete_multiple.py

Downloading Files
----------------------------------------------
You can use **labstep.entities.y.model** to download files uploaded directly to Labstep or
attached to different Labstep entities

:download:`download_file.py <../../examples/download_file.py>`

.. literalinclude:: ../../examples/download_file.py