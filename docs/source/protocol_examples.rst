Protocols
----------------------------------------------

Creating protocols
++++++++++++++++++++++++++++++++++++++++++++++

Create a protocol and edit the body
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The body of protocols can be edited like the entries of experiments. The below shows how to add text
and files to the protocol body. For further examples, see those listed under creating experiments.

:download:`edit_protocol.py <../../examples/edit_protocol.py>`

.. literalinclude:: ../../examples/edit_protocol.py


Exporting protocols
++++++++++++++++++++++++++++++++++++++++++++++

The following example scripts will export experiments in PDF, HTML and JSON formats.

Export a specific protocol
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The protocol ID can be found in the URL of the protocol in the web app.

:download:`export_protocol.py <../../examples/export_protocol.py>`

.. literalinclude:: ../../examples/export_protocol.py


Export protocols by workspace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Export the protocols by their workspace. The ID of the workspace, collections and tags can be found in their URLs in the web app.

:download:`export__workspace_protocol.py <../../examples/export_workspace_protocols.py>`

.. literalinclude:: ../../examples/export_workspace_protocols.py


Export protocols by user
^^^^^^^^^^^^^^^^^^^^^^^^

Export the protocols of a user across multiple workspaces.

:download:`export__workspace_protocol.py <../../examples/export_user_protocols.py>`

.. literalinclude:: ../../examples/export_user_protocols.py