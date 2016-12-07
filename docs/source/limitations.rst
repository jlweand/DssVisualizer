.. highlight:: py

Limitations/Issues/Weirdness
============================

Limitations we've found with the application
--------------------------------------------

* Any future development on this application would best be done without the Webkit for debugging and inspecting JS purposes. The Webkit doesn’t have any of that functionality.
  The most I’ve been able to get from it is console output on JS errors when debugging it in PyCharm.

* Mark has come across HTML5 functionally that works in Chrome, but not the Webkit.  I don’t remember the specifics of what though.

* window.open does not work with Webkit

* WebKit does not support 'includes' function, use 'indexOf' instead.

* You cannot change the Renderer plugins on the fly.  You must restart the application so the index.html can be recreated with the new plugin scripts.  You can, however, change the DB on the fly.

* It might not be a good idea without a lot more research to use ElasticSearch for the visualizer.

    1. When researching on how to get the distinct event/tech names I tried
    `aggregation <https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-terms-aggregation.html>`_ and then ran into `fielddata
    is disabled on text fields by default <https://www.elastic.co/guide/en/elasticsearch/reference/current/fielddata.html>`_

    2. The annotation queries are weird. Maybe there's a way to do everything in one query but I couldn't figure out how to only add an annotation if the exact
    same annotation did not exist.  Mongo does it automatically, and to keep the same functionality in ES I had to select the object, check that the annotation
    does not already exist, update the object, and then resave it.

Things that may seem weird
--------------------------

* So for getting the list of **distinct technician and event names**, only certain classes have the methods to query the data source. This was done, because while,
  the logger generates up to 10 different data types, those comes in pairs (or a triad). There was no reason to select from all data types when the information
  is duplicated.  For example: TShark has two files, when importing the two files, they will have the same metadata. We only need to look at one of those data
  imports. So the five files that have the distinct methods are: KeyPress, MulitExcludeThroughput, MulitIncludeThroughput, TSharkThroughput, and ManualScreenshot.

* **Annotations:**  The UI only allows for one annotation per item.  It calls the back end method to add/edit an 'annotation' attribute.  The back end (both MongoDB
  and ElasticSearch) both have the capability to add multiple annotations ('annotations' attribute) as well, with the edit and delete methods.  So there are three
  annotation methods that aren't currently used. I left them there for future work.

Issues we know about
--------------------

* I think the plugin management should be more robust.  The Datasource plugin works fine because it's just a folder, but the renderers need more information.
  So I'm rigging it together right now to work with specific files.  So if you add a new plugin you need to make sure the structure is the same as it is for the
  visjs plugin.  Meaning you need to have a /plugins/renderer/xxx/importScripts/ folder with a scripts.txt file that has all the scripts needed for that specific
  js. You also need keyloggerScript.txt, pcapScript.txt, and screenshotScript.txt files that have the JS script for that specific plugin.  Then all will work well.

* I think there's a way in MongoDB to return the date/times to the original local time instead of your current local time.  I don't have time to test it out
  before Wednesday, but check this `link <https://docs.mongodb.com/v3.2/tutorial/model-time-data/>`_ out.

* Here are some ideas to help speed up the Mongo back end.  Right now we pull the data from Mongo and clean up the dates, and remap the '_id' to 'id'.

  1. I think you can format the date on the way out of MongoDB and get rid of a bunch of datetime conversions to help speed things up.  Look `here <https://docs.mongodb.com/v3.2/reference/operator/aggregation/dateToString/>`_.

  2. But you'll still have the Mongo '_id' issue that the JS won't pick up as the id of the data point.  Maybe there is someway to tell JS that the id of the object is '_id' and not 'id'.

* Sphinx documentation will complain about not being able to find index.html.template when trying to document dssvisualizer.py.  Just change::

    GenerateHtml().generateHtml()
    uri = "file:///" + os.getcwd() + "/viewmanager/index.html"

  to::

      #GenerateHtml().generateHtml()
      uri = "file:///" #+ os.getcwd() + "/viewmanager/index.html"

  and run the::

      make html

  command again.  Check `this <http://www.sphinx-doc.org/en/1.4.9/tutorial.html#autodoc>`_ out for more information.

Issues you may be facing with Linux
-----------------------------------
This is verbatim from Dr. Acosta when he first tried to install and run DssVizualizer:

1. Tried running on my kali Linux 2016.1 and I get this error when I try running python3::

    Traceback (most recent call last):
      File "/usr/lib/python3.5/runpy.py", line 193, in _run_module_as_main
        "__main__", mod_spec)
      File "/usr/lib/python3.5/runpy.py", line 85, in _run_code
        exec(code, run_globals)
      File "/root/install/viz/DssVisualizer-master/app/viewmanager/dssvisualizer.py", line 36, in <module>
        from viewmanager.exportPopup import ExportPopup
      File "/root/install/viz/DssVisualizer-master/app/viewmanager/exportPopup.py", line 6, in <module>
        gi.require_version("WebKit", "3.0")
      File "/usr/lib/python3/dist-packages/gi/__init__.py", line 102, in require_version
        raise ValueError('Namespace %s not available' % namespace)
    ValueError: Namespace WebKit not available

2. Read your documentation stating that python 3.4 (windows) works, not 3.5

3. Turns out that the fix for Linux (probably windows too) is to

  3a. install: gir1.2-webkit-3.0 I used apt-get on Linux Solution was found `here <http://stackoverflow.com/questions/25037006/error-could-not-find-any-typelib-for-gtk-with-python3-and-gtk3>`_

  3b. I also had to change the theme or else I didn't see some of the widgets. I still get your warnings related to the theme (deprecated calls).
