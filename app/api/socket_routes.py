from flask import Blueprint, jsonify, request
from flask_socketio import SocketIO, emit
from app.models import Message, db
from sqlalchemy.sql import or_

socketio = SocketIO(cors_allowed_origins="*")


socket_routes = Blueprint('socket', __name__)

@socket_routes.route("/http-call/<int:id>")
def http_call(id):
   messages = Message.query.filter(or_(Message.user_id_from == id,Message.user_id_to == id))
   print(f'\n\n Messages: {messages} \n\n')
   return {'messages': [message.to_dict() for message in messages]}

@socketio.on("connect")
def connected():
    """event listener when client connects to the server"""
    print(request.sid)
    print("client has connected")
    emit("connect",{"data":f"id: {request.sid} is connected"})

@socketio.on('data')
def handle_message(data):
    message_data = Message(
        user_id_from = data['user_id_from'],
        user_id_to = data['user_id_to'],
        message = data['msg']
    )
    db.session.add(message_data)
    db.session.commit()
    print(f'\n\ncommitting to database message instance {data} \n\n')
    """event listener when client types a message"""
    print("data from the front end: ",data)
    emit("data",{'data':data,'id':request.sid},broadcast=True)

@socketio.on("chat")
def handle_chat(data):
    emit("chat", data, broadcast=True)

@socketio.on("disconnect")
def disconnected():
    """event listener when client disconnects to the server"""
    print("user disconnected")
    emit("disconnect",f"user {request.sid} disconnected",broadcast=True)