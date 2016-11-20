UI Documentation
================
Versions:
---------
-> jquery - 3.1.0
-> sweetalert2 - 5.3.2
-> html - v5
-> Underscore.js - 1.8.3

External plugins
----------------
-> Chosen 1.6.2 - a Select Box Enhancer for jQuery and Prototype

Introduction
------------
This document describes the User Interface for the DSS Visualizer application.

Structure
---------
The application contains two primary elements visible to the user: the visualizer page, and the administrator page.

.. image:: UIelements.png

Access access to the administrator page is not resctricted and navigation to either page is performed via a link on the
top right corner labeled "Aministrator" or "Back to Visualizer".

Primary elements
----------------
Both the Administrator page and the Visualizer page are written with html and no other frameworks are beign used at the moment.

Visualizer elements (main page):
--------------------------------
At the top right corner is the link to the Administrator page.
Below that are the data visualization options. These include:
  * Data range (calendar selector)
  * Event name - Dropdown box displays available events NOTE: Must be selected before technician name. You can select more than 1.
  * Technician name - Dropdown box displays available technicians NOTE: You can select more than 1
  * Event/Technician names - Dropdown box. Pick a combination of technician and event depending on what data is available NOTE: You can select more than 1
  * Filter - You can enter a keyword to filter the data in the timelines. NOTE: It is case sensitive and needs to be spelled exactly the same.

Below the data visualization options are the "Go" button and the "Export Visible Data" button.
    * Go - Visualizes the data depending on the options selected
    * Export Visible Data- Allows you to select a destination to export the visible data

Datatype checkboxes:
  * Select what types of data you want to be visible.

Timeline Box:
  * Timelines are displayed at the bottom of the screen. When viewing multiple data sets they will be grouped depending on the technician/event.


Administrator elements:
-----------------------
At the top right you have the link to go back to the Visualizer.
Below, there are three tabs available:
  * Import Data - Allows the import of data from external sources. NOTE: For more detailed information about importing, refer to the Data Import README.
  * Active Plugins - Allows the selection of datasource and renderer plugins that will be used to visualize data.
  * Install Plugins - Allows the installation of new plugins. NOTE: For more detailed information about installing plugins, refer to the Plugin Install README.
