.. highlight:: rst

Installation and setup for MongoDB and Python libraries
=========================================

Follow the below instructions to get started with MongoDB

Windows Instructions
==================

Installing MongoDB, pymongo, ujson (for Windows. Mac OS and Linux may vary)

MongoDBo installation
---------------------
* Download the version of MongoDB Community Server you need: https://www.mongodb.com/download-center#community

* Choose Custom Install and change the install path to C:\mongodb. Accept all other defaults.  The rest of these instructions assume that’s where you’ve installed it.

* Create folders MongoDB need:  (These are the default in MongoDB.  You can customize them if you want, but I did not look too close into it.  The customer will be managing their own install.)::

	mkdir c:\data\db
	mkdir c:\data\log


* Start MongoDB up:  You must use a command window with Administrative rights. And this must be done before you try to use our app or Mongo isn’t started and the app can’t use it!::

	C:\MongoDB\Server\3.2\bin\mongod.exe

You’ll get a lot of text scrolling.  As long as it ends in ‘waiting for connections’ you’re good.

* Connect to MongoDB to test that it's all working in another cmd window (doesn’t need to be run with admin rights)::

	C:\MongoDB\Server\3.2\bin\mongo.exe

Ctrl+C to close connection.

* If you want to walk through their tutorial for python, you can check it out here: https://docs.mongodb.com/getting-started/python/  I’ll leave that up to the reader.

pymongo installation
--------------------
* Open a cmd window and install it::

	python -m pip install pymongo

* That’s it.

ujson installation
------------------
* Open a cmd window and try to install it::

	python -m pip install ujson

* If you get the error: Unable to find vcvarsall.bat error you will need to do some troubleshooting.  It needs to compile some stuff and it is missing Visual Studio’s C++ libraries.

* Option 1: So head on out to https://www.visualstudio.com/ and download Visual Studio.  Make sure you install Common Tools for Visual C++

	- If you are installing ujson for Python 3.5 this is all you need to do.
	- If you are installing ujson for Pythong 3.4 you’ll also need to run the following command
		set VS100COMNTOOLS=%VS140COMNTOOLS%

	- Now run the pip install ujson command again.

*	Option 2: You can also go try to find the precompiled binary version of ujson and install that instead of dealing with Visual Studio
