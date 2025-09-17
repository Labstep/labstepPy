Devices
----------------------------------------------

Sending Data from Devices
++++++++++++++++++++++++++++++++++++++++++++++


Sending Data from your devices is a simple 3 step process:

1. Authenticate and select the device you are sending data from.

You will need to create a representation for your device on Labstep. This can either be done on the web-app or by using the :func:`~labstep.entities.user.model.User.newDevice` method

2. Detect incoming data from the device.

How you do this will depend on the device and how it outputs data. See below for an example of how to work with simple numerical readings coming of an RS-232 device such as a balance or thermometer and another example for uploading data files being outputted by a more complex instrument such as a plate reader.

3. Once you have the data from the device, all that's left is to send it to Labstep with the :func:`~labstep.entities.device.model.Device.addData` method.



Examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here is an example of how to set up a script to read from an RS-232 device such as a balance.

This example requires the PySerial package which can be downloaded by running

.. code-block:: bash

    pip install PySerial

:download:`balance_integration_example.py <../../examples/balance_integration_example.py>`

.. literalinclude:: ../../examples/balance_integration_example.py


Here is an example of how to set up a script to watch a folder for data files saved by an instrument such as a plate reader.

This example requires the PySerial package which can be downloaded by running

.. code-block:: bash

    pip install watchdog

:download:`plate_reader_integration_example.py <../../examples/plate_reader_integration_example.py>`

.. literalinclude:: ../../examples/plate_reader_integration_example.py


Further Help
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For further help setting up integrations with instruments please contact **barney@labstep.com**


Importing devices
++++++++++++++++++++++++++++++++++++++++++++++

To import new devices to a specified device category from an xlsx file.

:download:`import_devices.py <../../examples/import_devices.py>`

:download:`devices.xlsx <../../examples/devices.xlsx>`

.. literalinclude:: ../../examples/import_devices.py


Exporting devices
++++++++++++++++++++++++++++++++++++++++++++++

To export all devices in a workspace including their categories, metadata and URLs.

:download:`export_devices.py <../../examples/export_devices.py>`

.. literalinclude:: ../../examples/export_devices.py