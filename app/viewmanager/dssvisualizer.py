import gi
import logging
import os
import ujson
from urllib.parse import parse_qs
from core.apis.renderer.annotations import Annotations

gi.require_version("Gtk", "3.0")
gi.require_version("WebKit", "3.0")
from gi.repository import Gtk
from gi.repository import WebKit


def handle(web_view,web_frame,web_resource,request,response):
	##'query' contains the data sent from the jquery.get method
	query = request.get_message().get_uri().get_query()

	if not query:
		return
	elif query == "keypressData":
		jsonFile = getJson("json/keypressData.json")
		jsonData = ujson.dumps(jsonFile)
		js = 'visData(%s);' % jsonData
		v.execute_script(js)
	else:
		queryDict = parse_qs(query)
		############################################################
		############## the annotation and data ID's ################
		############################################################
		print(queryDict['annotation'])
		print("\n")
		print(queryDict['dataID'])
		Annotations().addAnnotation(queryDict['dataID'][0], queryDict['annotation'][0])
	return

def getJson(file):
	with open(file) as json_data:
	    d = ujson.load(json_data)
	    return(d)

def handle_btn1():
	print ("button 1 pressed")
	return

def handle_btn2():
	print ("button 2 pressed")
	return

# def handle_url(request):
# 	print(request.get('annotation'))

w = Gtk.Window()
v = WebKit.WebView()
sw = Gtk.ScrolledWindow()
sw.add(v)
w.add(sw)

#w.set_size_request(100,100)

w.connect("delete-event", Gtk.main_quit)

uri = "file:///" + os.getcwd() + "/viewmanager/index.html"
v.load_uri(uri)
v.connect("resource-request-starting", handle)



w.show_all()
Gtk.main()
