import gi
import logging
import os
import ujson
from urllib.parse import parse_qs
# from core.apis.renderer.annotations import Annotations
from core.apis.renderer.generateHtml import GenerateHtml
from plugins.datasource.mongodb.pyKeyLogger import PyKeyLogger
from core.apis.renderer.importRenderer import ImportRenderer

gi.require_version("Gtk", "3.0")
gi.require_version("WebKit", "3.0")
from gi.repository import Gtk
from gi.repository import WebKit



def handle(web_view,web_frame,web_resource,request,response):
	##'query' contains the data sent from the jquery.get method

	query = request.get_message().get_uri().get_query()
	uri = request.get_uri()

	if('installRends' in uri or 'adminset' in uri):
		load_uninstalled_renderers(query)
	if not query:
		return
	else:

		queryDict = parse_qs(query)
		if('request' in queryDict):
			if(queryDict['request'][0] == 'keypressData'):
				# jsonFile = getJson("json/keypressData.json")
				# jsonData = ujson.dumps(jsonFile)
				startDate = queryDict['startDate'][0]
				endDate = queryDict['endDate'][0]
				keyData = PyKeyLogger().selectKeyPressData(startDate, endDate)
				clickData = PyKeyLogger().selectClickData(startDate, endDate)
				timedData = PyKeyLogger().selectTimedData(startDate, endDate)
				js = "visData(%s, %s, %s);" % (keyData, clickData, timedData)
				webKitWebView.execute_script(js)
		elif('submission' in queryDict):
			if(queryDict['submission'][0] == 'annotation'):
				itemID = queryDict['itemID'][0]
				itemType = queryDict['type'][0]
				annotation = queryDict['annotation'][0]
				if(itemType == 'keypress'):
					PyKeyLogger().addAnnotationKeyPress(itemID, annotation)
				elif(itemType == 'click'):
					PyKeyLogger().addAnnotationClick(itemID, annotation)
				elif(itemType == 'timed'):
					PyKeyLogger().addAnnotationTimed(itemID, annotation)

	# elif query == "keypressData":
	# 	jsonData = PyKeyLogger().selectKeyPressData('2016-08-01 00:00:00', '2016-08-20 00:00:00')
	# 	# jsonData = ujson.dumps(jsonFile)
	# 	print(jsonData)
	# 	js = 'visData(%s);' % jsonData
	# 	webKitWebView.execute_script(js)
	# else:
	# 	queryDict = parse_qs(query)
	# 	############################################################
	# 	############## the annotation and data ID's ################
	# 	############################################################
	# 	print(queryDict['annotation'])
	# 	print("\n")
	# 	print(queryDict['dataID'])
	# 	# Annotations().addAnnotation(queryDict['dataID'][0], queryDict['annotation'][0])
	return

def getJson(file):
	with open(file) as json_data:
	    d = ujson.load(json_data)
	    return(d)


def load_uninstalled_renderers(query):

	importer = ImportRenderer()
	newPlugins = importer.getUninstalledPlugins()
	if not query:
		for plugin in newPlugins:
			modify_uninstalled_renderers(plugin)
	else:
		importer.importPlugin(query)
		script = 'document.getElementById("installRends").innerHTML = "";'
		webKitWebView.execute_script(script)
		load_uninstalled_renderers(None)

	print (importer.getUninstalledPlugins())

def modify_uninstalled_renderers(plugin):
	if plugin:
		script = 'var element = document.createElement("option");'
		script = script + 'element.innerHTML = "' + plugin + '";'
		script = script + 'document.getElementById("installRends").appendChild(element);'
	else:
		script = 'document.getElementById("installRends").innerHTML = "";'
	webKitWebView.execute_script(script)



# def handle_url(request):
# 	print(request.get('annotation'))

gtkWindow = Gtk.Window()
webKitWebView = WebKit.WebView()
gtkScrolledWindow = Gtk.ScrolledWindow()
gtkScrolledWindow.add(webKitWebView)
gtkWindow.add(gtkScrolledWindow)
gtkWindow.connect("delete-event", Gtk.main_quit)

#gtkWindow.set_size_request(100,100)

# generate the index.html page based on the renderer plugin
GenerateHtml().generatHtml()
uri = "file:///" + os.getcwd() + "/viewmanager/index.html"

webKitWebView.load_uri(uri)
webKitWebView.connect("resource-request-starting", handle)


gtkWindow.show_all()
Gtk.main()
