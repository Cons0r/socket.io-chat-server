# Socket.IO Python basics
### [Python-Socket.IO docs (more in depth)](https://python-socketio.readthedocs.io/en/latest/server.html#)
![python-socketio logo (i made it)](https://cdn-1.chadfreeman.repl.co/static/python-socket.IO-no-background.png)
There isnt much here as everything is pretty easy to do  
The way to assign events for this Library are:  
`@sio.event`  
#### --Or--
`@sio.on(event)`  
(In my Opinion @sio.on is better Because you can make an with event a function name without conflict):  
Example:
``` python
@sio.event
def print(sid, data):
	....
# you cant use that as there is already a function named print()
# what you can do is this
@sio.on('print')
def litteralyanything(sid, data):
	....
```
To send events to Clients:  
```python
from profanity_check import predict #Yes its a real library
@sio.on('format')
def msgformat(sid, data):
	profanity = bool(predict([data])) # use profanity_check.predict([]) wich returns a binary 1 or 0 and convert to bool
	if not profanity: # if the message doesnt contain profanity
		**sio.emit('message', data=data)**
	elif profanity:
		**sio.emit('profanityerror', data=data, to=sid)** # use sio.emit() to send messages to clients, to= is for sending a message to only specific clients

@sio.event
def connect(sid, environ):
	username = authenticate_user(environ)
  sio.save_session(sid, {'username': username})

@sio.on('message')
def getmessage(sid, data):
	with sio.session(sid) as session:
		username = session['username']
```
[NEXT: Build a Client](https://replit.com/@ChadFreeman/socketio-python-client-template)