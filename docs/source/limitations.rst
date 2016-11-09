Limitations/Issues/Weirdness
============================

Limitations we've found with the application
--------------------------------------------

* Any future development on this application would best be done without the Webkit for debugging and inspecting JS purposes. The Webkit doesn’t have any of that functionality.  The most I’ve been able to get from it is console output on JS errors when debugging it in PyCharm.

* Mark has come across HTML5 functionally that works in Chrome, but not the Webkit.  I don’t remember the specifics of what though.

*window.open does not work with Webkit

Things that may seem weird
--------------------------

* So for getting the list of distinct technician and event names, only certain classes have the methods to query the data source. This was done, because while, the logger generates up to 10 different data types, those comes in pairs (or a triad). There was no reason to select from all data types when the information is duplicated.  For example: TShark has two files, when importing the two files, they will have the same metadata. We only need to look at one of those data imports. So the five files that have the distinct methods are: KeyPress, MulitExcludeThroughput, MulitIncludeThroughput, TSharkThroughput, and ManualScreenshot.

Issues we know about
--------------------
