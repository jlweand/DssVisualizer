.. highlight:: rst
.. DssVisualizer documentation master file, created by
   sphinx-quickstart on Sat Oct  1 12:48:21 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: ../../documents/coollogo_com-297791429.png

Welcome to the Decision Support System Visualizer
=================================================

DSS Visualizer is being developed by Interrupt 0x22 for Dr. Jamie Acosta from the U.S. Army Research Laboratory.  It is a non-web based web based application that displays Key Logger, PCAP,
and screenshots gathered at various events. What do you mean by "non-web based web based application", you ask?  One of the requirements of this application was for it to
use a Webkit outside of a real web server.  So, while it has all the makeup of a real life web application, it does not need Apache, Tomcat, IIS, or any other web server.
This keeps it lightweight and portable.  It is written in Python and JavaScript with your choice of a MongoDB or ElasticSearch data source.

The Interrupt 0x22 developers are:

* **Jennifer Weand**: In her free time, Jennifer spends her time playing with her four cats, officiating at local roller derby bouts, or (and this has been much too infrequent as of late) driving off into the sunset and camping.

* **Juan Soto**: One day Juan was looking for a proteomics class and accidently walked into the Advanced Object Oriented Programming class.  Now he's about to get a Master's in Software Engineering.  We turned another to the programming side!

* **Mark Eby**: Our GUI guru, we would be lost without him. He'll be changing his name to MarkEby.js after this semester. He spends his days deep in JavaScript to the delight of every other team member. When he's not cursing at JavaScript you might catch a glimpse of him flying down the highway to his next JavaScript adventure.

* **Mark Smith**: A chemist by trade, Mark decided that computers were much more fun to play with than measuring the effects of chemical compounds in the chemistry lab.  He was right, programmers are much more fun than chemicals!

* **Andres Olivas**: The enigma of the group, Andres saw the light and came to the programming side after realizing engineering electrons were not near as fun as engineering code.  When he's not stuck crossing the border, he enjoys long walks with MongoDB and working at HP.

DssVisualizer Code
==================

GitHub repo can be found at https://github.com/jlweand/DssVisualizer

Documentation
=============

Here is all the hand written documentation we have.  There is more documentation in the code about individual
methods.  Check out the list of `modules <py-modindex.html>`_ for more information.

.. toctree::
   :maxdepth: 1

   pygobjectinstall
   pythonlibraries
   mongodbinstall
   elasticsearchinstall
   datasourceapi
   /viewmanager/js Package <viewmanager.js>
   Add a New Data Type <addnewdatatype>
   Install a Plugin <plugininstall>
   dataimport
   testcases
   UIdocumentation
   limitations
   incomplete
   datacreator
   Browse the Code! <modules>


How to run the DssVisualizer
============================
We now have command line functionality for DssVisualizer! Once you have the latest version of DssVisualizer from GitHub navigate to the `app` folder and run::

    > python3 dssviz.py -h

To start the app in a `cmd` line, from within the `app` folder run either::

    > python3 dssviz.py
    > python3 dssviz.py start

To import data, you can use the `user interface <dataimport.html>`_, run the
`setup test case <testcases.html>`_, or use the command line::

    usage: dssviz.py import [-h] [-dir DIRECTORY] [-e EVENTNAME] [-t TECHNAME]
                            [-c COMMENTS] [-id IMPORTDATE] [-cp]
    arguments:
      -h, --help      Show this help message and exit
      -dir DIRECTORY  The top level directory to search and import JSON files.
      -e EVENTNAME    Name of the event to add as metadata to imported data.
      -t TECHNAME     Name of the technician to add as metadata to imported
                      data.
      -c COMMENTS     Comments about data to add as metadata to imported data.
      -id IMPORTDATE	Datetime the data was imported. If not specified,
                      current datetime will be used.
      -cp             Flag to copy the images on import. Images will be copied
                      into DssVisualizers file structure

To export data, you can use the `user interface <dataimport.html#export-data>`_, or use the command line::

    usage: dssviz.py export [-h] [-dir DIRECTORY] [-sd STARTDATE] [-ed ENDDATE]
                            [-e EVENTNAME] [-t TECHNAME] [-cp]
    optional arguments:
      -h, --help      Show this help message and exit
      -dir DIRECTORY  The destination for the exported data.
      -sd STARTDATE   The start datetime to search on and return data to export.
      -ed ENDDATE     The end datetime to search on and return data to export.
      -e EVENTNAME    Name of the event to search on and return data to export.
      -t TECHNAME     Name of the technician to search on and return data to
                      export.
      -cp             Flag to copy the images on export. Images will be copied
                      to the export directory.

Indices and tables
==================

Check out all the code!  You can view everything by method (Index) or view it by module (Module Index).  You can search as well.

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

This documentation was last updated |today|.
