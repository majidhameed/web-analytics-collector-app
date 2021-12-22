'''
Created on Mar 26, 2014

@author: Majid Hameed
'''
import bottle, types, pymongo
from bottle import Bottle, request, response, static_file
from paste import httpserver
import datetime
import sys, traceback

DEFAULT_PORT = 80
APP_NAME = "Tracker"
HOST = '0.0.0.0'
DEV = False

connection = pymongo.Connection('mongodb://localhost', safe=True)
db = connection.web_analytics
app = Bottle()

@app.route('/t')
def serve_image():
    request_detail = {}
    
    try:
        for key, value in request.headers.items():
            request_detail[key] = value
        """    if key is 'HTTP_REFERER' and len(value)>7:
                request_detail['HTTP_REFERER_WEBSITE']=value[:value.find('/',7)]
        """
        for key in request.environ:
            if type(request.environ[key]) is types.StringType:
                value = request.environ[key]
                request_detail[key.replace('.','_')] = value
                if key.strip().find('HTTP_REFERER') is not -1:
                    request_detail['HTTP_REFERER_WEBSITE']=value[:value.find('/',7)]
        save_request_data(request_detail)
        today=datetime.datetime.utcnow()
        resp = static_file(filename='eh.gif', root='img', mimetype='auto', download=False)
        resp.set_header('Expires', 'Mon, 26 Jul 1997 05:00:00 GMT')
        resp.set_header('Last-Modified', today.strftime('%a, %d %b %Y %H:%M:%S GMT'))
        resp.set_header('cache-Control', 'no-store, no-cache, must-revalidate')
        resp.add_header('cache-Control', 'post-check=0, pre-check=0')
        resp.set_header('Pragma', 'no-cache')
    except:
        print sys.exc_info()
        print sys.exc_info()[0]
        print traceback.format_exc()
        
    return resp
    
def save_request_data(request_detail):
    request_detail['request_date'] = datetime.datetime.utcnow();
    print "request_detail:" + str(request_detail)
    db.request_detail.insert(request_detail)
    
bottle.debug(DEV)
app.run(server='paste', host=HOST, port=DEFAULT_PORT, reloader=DEV)