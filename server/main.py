import openai
import time
import os
from flask import Flask, request, jsonify, Response, render_template
from flask_cors import CORS

from pymongo import MongoClient
from bson.objectid import ObjectId

from flask_socketio import SocketIO, emit, send

from config import *

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)

#   MongoDB Connection
client = MongoClient(MONGODB_CONNECTION_STRING)
database = client[MONGODB_DATABASE_NAME]
items_collection = database[MONGODB_TODO_ITEMS_COLLECTION]



@app.get("/get_todo_items")
def get_todo_items():
    items_list = items_collection.find()
    items_list = [{"id": str(item["_id"]), "content": item["content"]} for item in items_list]

    return jsonify({
        "todoItems": items_list
    })

@app.post("/add_todo_item")
def add_todo_item():
    item_content = request.json["item_content"]
    _id = items_collection.insert_one({"content": item_content})

    return jsonify({
        "item_id": str(_id.inserted_id)
    })

@app.post("/delete_todo_item")
def delete_todo_item():
    item_id = request.json["item_id"]
    items_collection.delete_one({"_id": ObjectId(item_id)})
    return {}




#Call Assistant.py
@app.route('/display_code')
def display_code():
    with open('assistant.py', 'r') as file:
        code = file.read()
    return code

import subprocess

@app.route('/run_assistant')
def run_assistant():
    result = subprocess.run(['python', 'assistant.py'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/run_assistant')
# def run_assistant():
#     result = subprocess.run(['python', 'assistant.py'], stdout=subprocess.PIPE)
#     return result.stdout.decode('utf-8')


# OpenAI API
# def get_openai_response(message):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": message}
#         ]
#     )
#     return response.choices[0].message["content"]


# #hail mary

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/chat', methods=['GET'])
# def chat():
#     user_message = request.args.get('message', 'Hello')
#     print(f"Received message: {user_message}")
#     return Response(generate(user_message), mimetype='text/event-stream')

# def generate(user_message):
#     try:
#         openai.OpenAI(api_key=OPENAI_API_KEY)
#         stream = client.chat.completions.create(
#             model="gpt-4",
#             messages=[{"role": "user", "content": user_message}],
#             stream=True
#         )
#         full_response = ""
#         for chunk in stream:
#             if chunk.choices[0].delta.content:
#                 full_response += chunk.choices[0].delta.content
#                 if "\n" in chunk.choices[0].delta.content:
#                     yield f"data: {full_response}\n\n"
#                     full_response = ""  # Reset after sending
#     except Exception as e:
#         print(f"Error while generating chat completions: {e}")
#         yield f"data: Error while generating chat completions: {e}\n\n"

# @socketio.on('message')
# def handle_message(message):
#     print('received message: ' + message)
#     send(message, broadcast=True)

# if __name__ == '__main__':
#     socketio.run(app)
# @app.route('/')
# def index():
#     return render_template('index.html')

# @socketio.on('message')
# def handle_message(data):
#     print('Received message: ' + data)
#     response_message = get_openai_response(data)
#     emit('from_server', {'data': response_message})

# if __name__ == '__main__':
#     socketio.run(app, debug=True)


# @app.route('/')
# def index():
#     return render_template('index.html')

# @socketio.on('message')
# def handle_message(message):
#     print('Received message:', message)
#     socketio.emit('from_server', {'data': message})  # Echoes back the received message

# if __name__ == '__main__':
#     socketio.run(app, debug=True)

@app.route('/stream_response')
def stream_response():
    def generate():
        #client = openai.OpenAI(api_key='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')
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        stream = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": "This is a test"}],
            stream=True
        )
        
        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    return Response(generate(), mimetype="text/plain")

if __name__ == '__main__':
    app.run(debug=True) 


