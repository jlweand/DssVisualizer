.. DssVisualizer documentation master file, created by
   sphinx-quickstart on Sat Oct  1 12:48:21 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: ../../documents/coollogo_com-297791429.png

Welcome to the Decision Support System Visualizer
=================================================

DSS Visualizer is being developed for Dr. Jamie Acosta from the U.S. Army Research Laboratory.  It is a non-web based web based application that displays Key Logger, PCAP,
and screenshots gathered at various events. What do you mean by "non-web based web based application", you ask?  One of the requirements of this application was for it to
use a Webkit outside of a real web server.  So, while it has all the makeup of a real life web application, it does not need Apache, Tomcat, IIS, or any other web server.
This keeps it lightweight and portable.  It is written in Python and JavaScript with a MongoDB data source.

Its developers are:

* Jennifer Weand: In her free time, Jennifer spends her time playing with her four cats, officiating at local roller derby bouts, or (and this has been much too infrequent as of late) driving off into the sunset and camping.

* Juan Soto: One day Juan was looking for a proteomics class and accidently walked into the Advanced Object Oriented Programming class.  Now he's about to get a Master's in Software Engineering.  We turned another to the programming side!

* Mark Eby: Our GUI guru, we would be lost without him. He'll be changing his name to MarkEby.js after this semester. He spends his days deep in JavaScript to the delight of every other team member. When he's not cursing at JavaScript you might catch a glimpse of him flying down the highway to his next JavaScript adventure.

* Mark Smith: A chemist by trade, Mark decided that computers were much more fun to play with than measuring the effects of chemical compounds in the chemistry lab.  He was right, programmers are much more fun than chemicals!

* Andres Olivas: The enigma of the group, Andres saw the light and came to the programming side after realizing engineering electrons were not near as fun as engineering code.  When he's not stuck crossing the border, he enjoys long walks with MongoDB and working at HP.

DssVisualizer Code
==================

GitHub repo can be found at https://github.com/jlweand/DssVisualizer

Documentation
=============

At the moment we are still working on the documentation as we develop the visualizer.
But to not keep you hanging here are some things to get you started!

.. toctree::
   :maxdepth: 1

   pygobjectinstall
   mongodbinstall
   Datasource API <datasourceapi>
   Renderer API <rendererapi>
   Install a Plugin <plugininstall>


How to run the DssVisualizer
============================
* Copy your .json files into the dssvisualizer/app/json/<dataType> folders.  Check out the source code of :func:`DataImport <core.config.dataImport>` for where the application is looking for the json files.

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
