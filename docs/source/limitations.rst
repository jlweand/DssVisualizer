Limitations/Issues/Weirdness
============================

Limitations we've found with the application
--------------------------------------------

* Any future development on this application would best be done without the Webkit for debugging and inspecting JS purposes. The Webkit doesn’t have any of that functionality.  The most I’ve been able to get from it is console output on JS errors when debugging it in PyCharm.

* Mark has come across HTML5 functionally that works in Chrome, but not the Webkit.  I don’t remember the specifics of what though.

* window.open does not work with Webkit

* WebKit does not support 'includes' function, use 'indexOf' instead.

* You cannot change the Renderer plugins on the fly.  You must restart the application so the index.html can be recreated with the new plugin scripts.  You can, however, change the DB on the fly.

Things that may seem weird
--------------------------

* So for getting the list of distinct technician and event names, only certain classes have the methods to query the data source. This was done, because while, the logger generates up to 10 different data types, those comes in pairs (or a triad). There was no reason to select from all data types when the information is duplicated.  For example: TShark has two files, when importing the two files, they will have the same metadata. We only need to look at one of those data imports. So the five files that have the distinct methods are: KeyPress, MulitExcludeThroughput, MulitIncludeThroughput, TSharkThroughput, and ManualScreenshot.

Issues we know about
--------------------

* I think the plugin management should be more robust.  The Datasource plugin works fine because it's just a folder, but the renderers need more information.  So I'm rigging it together right now to work with specific files.  So if you add a new plugin you need to make sure the structure is the same as it is for the visjs plugin.  Meaning you need to have a /plugins/renderer/xxx/importScripts/ folder with a scripts.txt file that has all the scripts needed for that specific js. You also need keyloggerScript.txt, pcapScript.txt, and screenshotScript.txt files that have the JS script for that specific plugin.  Then all will work well.
