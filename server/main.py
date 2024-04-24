import openai
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

from pymongo import MongoClient
from bson.objectid import ObjectId

from config import *

app = Flask(__name__)
CORS(app)

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


# @app.post("/chatbot")
# def chatbot():
#     user_message = request.json["message"]
#     response = openai.ChatCompletion.create(
#       model="gpt-4.0-turbo",
#       messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": user_message}
#         ]
#     )
#     return jsonify({
#         "response": response['choices'][0]['message']['content']
#     })

# @app.post("/chatbot")
# def chatbot():
#     user_message = request.json["message"]
#     response = openai.Completion.create(
#       engine="text-davinci-002",
#       prompt=f"{user_message}\nAI:",
#       temperature=0.5,
#       max_tokens=100
#     )
#     return jsonify({
#         "response": response['choices'][0]['text']
#     })

# @app.get("/test_openai")
# def test_openai():
#     try:
#         response = openai.Completion.create(
#           engine="text-davinci-002",
#           prompt="Hello, world!\nAI:",
#           temperature=0.5,
#           max_tokens=100
#         )
#         return jsonify({
#             "response": response['choices'][0]['text']
#         })
#     except Exception as e:
#         return str(e), 500
    
@app.get("/test_openai")
def get_response(user_message, history):
    # Append the user message to the conversation history
    history.append({"role": "user", "content": user_message})

    # Send the updated conversation to the API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=history
    )

    # Extract the latest response from the model
    ai_response = response['choices'][0]['message']['content']

    # Optionally, update the history with the AI's response
    history.append({"role": "ai", "content": ai_response})

    return ai_response, history

def respond(user_message, history=[]):
    return get_response(user_message, history)
   
# @app.get("/test_openai1")
# def test_openai():
#     try:
#         message = {"role":"user", "content": input("This is the beginning of your chat with AI. [To exit, send \"###\".]\n\nYou:")};

#         conversation = [{"role": "system", "content": "DIRECTIVE_FOR_gpt-3.5-turbo"}]

#         while(message["content"]!="###"):
#             conversation.append(message)
#             completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation) 
#             message["content"] = input(f"Assistant: {completion.choices[0].message.content} \nYou:")
#             print()
#             conversation.append(completion.choices[0].message)
#     except Exception as e:
#          return str(e), 500



@app.route('/chat1', methods=['POST'])
def create_chat():
    client = openai.OpenAI()

    # Start with an initial system message to define the AI's role
    messages = [
        {"role": "system", "content": "You are a medical advisor and companion."},
    ]

    # Get user message from request data
    user_message = request.json.get('message')

    # Append the user message to the conversation history
    messages.append({"role": "user", "content": user_message})

    # Send the updated conversation to the API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Return the latest response from the model
    return {"AI": response.choices[0].message.content}

if __name__ == "__main__":
    app.run(debug=True)