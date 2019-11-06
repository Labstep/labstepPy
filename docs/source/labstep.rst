*labstep* package
==============================================

Installation
----------------------------------------------

The *labstep* package can be easily installed using ``pip``.
Open the ``Terminal``, and do:

.. code-block:: bash

    pip install labstep


Setup
----------------------------------------------
Once installed, every session starts with importing
the *labstep* module and logging into your Labstep account:

.. code-block::

    import labstep

    user = labstep.login('myaccount@labstep.com', 'mypassword')


Login
----------------------------------------------

.. autofunction:: labstep.user.login

Classes
----------------------------------------------

User
++++++++++++++++++++++++++++++++++++++++++++++

.. autoclass:: labstep.user.User
   :members:
   :undoc-members:

Experiment
++++++++++++++++++++++++++++++++++++++++++++++

.. autoclass:: labstep.experiment.Experiment
   :members:
   :undoc-members:

Protocol
++++++++++++++++++++++++++++++++++++++++++++++

.. autoclass:: labstep.protocol.Protocol
   :members:
   :undoc-members:

Resource
++++++++++++++++++++++++++++++++++++++++++++++

.. autoclass:: labstep.resource.Resource
   :members:
   :undoc-members:

Workspace
++++++++++++++++++++++++++++++++++++++++++++++

.. autoclass:: labstep.workspace.Workspace
   :members:
   :undoc-members:

File
++++++++++++++++++++++++++++++++++++++++++++++

.. autoclass:: labstep.file.File
   :members:
   :undoc-members:

Comment
++++++++++++++++++++++++++++++++++++++++++++++

.. autoclass:: labstep.comment.Comment
   :members:
   :undoc-members:

Tag
++++++++++++++++++++++++++++++++++++++++++++++

.. autoclass:: labstep.tag.Tag
   :members:
   :undoc-members:


Acknowledgements
----------------------------------------------

We acknowledge the use of the following resources:


