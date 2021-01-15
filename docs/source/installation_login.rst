Installation
==============================================
The *labstep* package can be easily installed using ``pip``.

Open the ``Terminal``, and do:

.. code-block:: bash

    pip install labstep



Setup
==============================================
Once installed, every session starts with
importing the *labstep* module and accessing
your Labstep account using either the
:func:`~labstep.authenticate` or 
the :func:`~labstep.login` functions below:


Authenticate
----------------------------------------------

Authenticating via an API key is the most secure method. 

For guidance on generating an API key to connect to your Labstep account see `this article <https://help.labstep.entities.com.model/en/articles/3636355-how-to-create-an-api-key-on-labstep>`_.

.. autofunction:: labstep.authenticate

Login
----------------------------------------------

You can also login using your username and password. 

NOTE: this method will not work for users who sign in via Google or via an Institution.

.. autofunction:: labstep.login
