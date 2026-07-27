Jupyter Notebooks
----------------------------------------------


Jupyter Notebooks Basics
++++++++++++++++++++++++++++++++++++++++++++++

Labstep Jupyter Notebooks have the following modules pre-installed:

* pandas
* scipy
* matplotlib
* openpyxl
* ipywidgets
* plotly
* pymatgen
* PyMassSpec
* Labstep SDK

These modules can be imported and used in Jupyter Notebook scripts in Labstep without being installed.


Read tables within a document and convert to a DataFrame
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This script allows you to take the data from within a Labstep table within your document and convert it to a Pandas DataFrame for further processing or analysis.



To execute this script in your Labstep experiment:

1. Create an interactive table within your experiment called "Experiment data table".
2. Enter some example data into the table.
3. Open a new instance of Jupyter Notebooks in your experiment.
4. Copy and paste the script below into the Jupyter Notebook editor, then run the script.


:download:`jn_table_to_df.py <../../examples/jn_table_to_df.py>`

.. literalinclude:: ../../examples/jn_table_to_df.py



Get data from a data field and convert to a DataFrame
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This script allows you to take the data from within a .csv file that you have added to your Labstep document and convert it to a Pandas DataFrame for further processing or analysis.

To execute this script in your Labstep experiment:

1. Create a data field in your Labstep experiment called "Example data".
2. Upload a .csv file containing some example data to the data field.
3. Open a new instance of Jupyter Notebooks in your experiment.
4. Copy and paste the script below into the Jupyter Notebook editor, then run the script.

:download:`jn_csv_to_df.py <../../examples/jn_csv_to_df.py>`

.. literalinclude:: ../../examples/jn_csv_to_df.py


Write a new data table for an experiment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This script allows you to take the data from within a .csv file that you have added to your Labstep experiment and write it to a table in your experiment for further interrogation or analysis.

To execute this script in your Labstep experiment:

1. Create a data field in your Labstep experiment called "Example data".
2. Upload a .csv file containing some example data to the data field.
3. Create an interactive called 'Output Table' to enter data into.
4. Open a new instance of Jupyter Notebooks in your experiment.
5. Copy and paste the script below into the Jupyter Notebook editor.
6. Save your script and exit the Jupyter Notebook editor.
7. Run your script from within the Labstep experiment.

:download:`jn_new_table.py <../../examples/jn_new_table.py>`

.. literalinclude:: ../../examples/jn_new_table.py


Save an image of a plot to a Labstep data field
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This script allows you to plot data in a graph which is then saved into your Labstep document (experiment or protocol) as a data field.

To execute this script in your Labstep experiment:

1. Create a data field in your Labstep experiment called "Plot".
2. Open a new instance of Jupyter Notebooks in your experiment.
3. Copy and paste the script below into the Jupyter Notebook editor.
4. Save your script and exit the Jupyter Notebook editor.
5. Run your script from within the Labstep experiment.

:download:`jn_plot_to_data_field.py <../../examples/jn_plot_to_data_field.py>`

.. literalinclude:: ../../examples/jn_plot_to_data_field.py