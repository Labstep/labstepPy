Experiments
----------------------------------------------

Creating experiments
++++++++++++++++++++++++++++++++++++++++++++++

Create an experiment and edit the entry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The below example shows how to create an experiment and add to the experiment entry:

* Files
* Data fields
* Inventory fields
* Inline spreadsheets
* Protocols
* Basic tables

For other elements or formatting options please use the web app to produce the desired result and
inspect the network request sent to see the shape of the JSON document object.

:download:`editing_entry.py <../../examples/editing_entry.py>`

.. literalinclude:: ../../examples/editing_entry.py


Exporting experiments
++++++++++++++++++++++++++++++++++++++++++++++

The following example scripts will export experiments in PDF, HTML and JSON formats.

Export a specific experiment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ID of the experiment can be found in the URL for the experiment in the web app.

:download:`export_experiment.py <../../examples/export_experiment.py>`

.. literalinclude:: ../../examples/export_experiment.py


Export experiments by workspace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Export the experiments by their workspace. The ID of the workspace, collections and tags can be found in their URLs in the web app.

:download:`export__workspace_experiments.py <../../examples/export_workspace_experiments.py>`

.. literalinclude:: ../../examples/export_workspace_experiments.py


Export experiments by user
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Export the experiments of a user across multiple workspaces.

:download:`export__workspace_experiments.py <../../examples/export_user_experiments.py>`

.. literalinclude:: ../../examples/export_user_experiments.py