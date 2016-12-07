.. highlight:: rst

Python Libraries Install
========================

Linux
-----
* Open a new terminal and install::

		apt-get install python3-pip
		pip3 install pymongo
		pip3 install elasticsearch
		pip3 install pytz
		pip3 install tzlocal
		pip3 install python-dateutil
		pip3 install ujson

Windows
-------
* Open a cmd window and install::

		pip install pymongo
		pip install elasticsearch
		pip install pytz
		pip install tzlocal
		pip install python-dateutil
		pip install ujson

If you have issues with ujson:

* If you get the error: Unable to find vcvarsall.bat error you will need to do some troubleshooting.  It needs to compile some stuff and it is missing Visual Studio’s C++ libraries.

* Option 1: So head on out to https://www.visualstudio.com/ and download Visual Studio.  Make sure you install Common Tools for Visual C++

	- If you are installing ujson for Python 3.5 this is all you need to do.
	- If you are installing ujson for Pythong 3.4 you’ll also need to run the following command
		set VS100COMNTOOLS=%VS140COMNTOOLS%

	- Now run the pip install ujson command again.

*	Option 2: You can also go try to find the precompiled binary version of ujson and install that instead of dealing with Visual Studio
