.. highlight:: rst

MongoDB Installation
====================

Follow the below instructions to get started with MongoDB

Linux Instructions
------------------

Installing MongoDB, pymongo, ujson and other python dependencies

MongoDB Installation
#####################

* Open a new terminal.

* In the new terminal, remove any old “db” and “log” folders::

	rm –r /data/db/
	rm –r /data/log/

* Now create folders MongoDB need:  (These are the default in MongoDB.  You can customize them if you want, but I did not look too close into it.  The customer will be managing their own install.)::

	mkdir /data/db
	mkdir /data/log

* Start MongoDB up by entering the following command in the terminal::

	mongod –storageEngine=mmapv1



Windows Instructions
--------------------

Installing MongoDB, pymongo, ujson and other python dependencies

MongoDB Installation
#####################

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
