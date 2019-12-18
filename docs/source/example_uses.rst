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
You can use **labstepPy** to easily delete
multiple different Entities on Labstep (a list
of Experiments, Protocols, or Tags, etc.),
either from within a specific Workspace or by
performing a global delete.

:download:`delete_multiple.py <../../examples/delete_multiple.py>`

.. literalinclude:: ../../examples/delete_multiple.py
