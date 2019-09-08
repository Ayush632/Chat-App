import os

from flask import Flask
from flask_socketio import SocketIO, emit

from flask import jsonify, render_template, request
from selenium import webdriver

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template('main.html')
@socketio.on("send message")
def mess(data):
    print("in python")
    selection = data["selection"]
    us_name=data["user_name"]
    final=us_name+":"+selection
    chat_name=data["chat_name"]
    p={'final':final,'chat_name':chat_name}
    emit("recieve mesge",p, broadcast=True)
    
@socketio.on("create room")
def messa(data):
    print("in messa")
    room_name=data['room_name']
    emit("make room",room_name,broadcast=True)
    