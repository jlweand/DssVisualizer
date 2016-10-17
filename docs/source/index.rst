.. DssVisualizer documentation master file, created by
   sphinx-quickstart on Sat Oct  1 12:48:21 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to DssVisualizer's documentation!
=========================================

At the moment we are still working on the documentation as we develop the visualizer.
But to not keep you hanging here are some things to get you started!

* GitHub repo can be found at https://github.com/jlweand/DssVisualizer

.. toctree::
   :maxdepth: 1

   pygobjectinstall
   mongodbinstall
   Datasource API <datasourceapi>
   Renderer API <rendererapi>
   Install a Plugin <plugininstall>


How to run the DssVisualizer
----------------------------
* Copy your .json files into the dssvisualizer/app/json/<dataType> folders.  Check out the source code of :func:`DataImportConfig <core.config.dataImportConfig>` for where the application is looking for the json files.

* Until the UI is complete, in a `cmd` line, from within the `app` folder run the test_dataimport.py file::

    > python -m unittests.test_dataimport

* To start the app: in a `cmd` line, from within the `app` folder run::

    > python -m viewmanager.dssvisualizer




Indices and tables
==================

Check out all the code!  You can view everything by method (Index) or view it by module (Module Index).  You can search as well.

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
