import os
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
import sys
import socketio
try:
	sio = socketio.Server(async_mode='gevent')
	app = socketio.WSGIApp(sio)
except AttributeError:
	os.system('pip uninstall socketio')
	os.system('pip install python-socketio')
	# even if you finsish the setup leave this here just incase rep.it acts weird and doesnt ignore installing

@sio.event
def connect(sid):
    print(f'{sid} has joined')


@sio.event
def disconnect(sid):
    print(f'{sid} left')


print('Server Online')
pywsgi.WSGIServer(('', 8080), app,
                  handler_class=WebSocketHandler).serve_forever()
