Installation
==============================================
The *labstep* package can be easily installed using ``pip``.

Open the ``Terminal``, and do:

.. code-block:: bash

    pip install labstep



Authentication
==============================================

Every session starts with importing the *labstep* module and accessing
your Labstep account using the
:func:`~labstep.authenticate` method and an API key.

For guidance on generating an API key to connect to your Labstep account see `this article <https://help.labstep.entities.com.model/en/articles/3636355-how-to-create-an-api-key-on-labstep>`_.

.. autofunction:: labstep.authenticate

