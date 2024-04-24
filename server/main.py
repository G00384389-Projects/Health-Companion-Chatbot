import openai
import time
import os
from flask import Flask, request, jsonify, Response
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



# OpenAI API

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

# @app.route('/medical_advice', methods=['POST'])
# def medical_advice():
#     ID = "asst_Z0g0wo4WWZBWljJbcvW7ekYa"
#     self.openAI = OpenAI(api_key=config.OPENAI_KEY)
    
#     symptoms = request.json.get('symptoms')

#     chat = client.beta.assistants.create(
#         name="Doctor",
#         instructions="You're a medical advisor, here to provide medical advice.",
#         content=symptoms,
#         model="gpt-4-turbo",
#     )

#     run = client.beta.threads.run.create(thread_id=chat.id, assistant_id=ID)
#     print(f"Run Created: {run.id}")

#     while run.status != "completed":
#         run = client.beta.threads.run.retrieve(thread_id=chat.id, run_id=run.id)
#         print(f"Run Status: {run.status}")
#         time.sleep(0.5)
#     else:
#         print(f"Run Completed: {run.id}")

#     message_response = client.beta.threads.messages.list(thread_id=chat.id)
#     messages = message_response.data

#     latest_message = messages[0]
#     return jsonify({"Response": latest_message.content[0].text.value})

# if __name__ == "__main__":
#     app.run(debug=True)



# @app.route('/answer', methods=['POST'])
# def answer():
#     try:
#         user_message = request.json["message"]
#         response = openai.Completion.create(
#           engine="text-davinci-002",
#           prompt=f"{user_message}\nAI:",
#           temperature=0.5,
#           max_tokens=100
#         )
#         return jsonify({
#             "response": response['choices'][0]['text']
#         })
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route("/answer", methods=["GET", "POST"])
# def answer():
#         data = request.get_json()
#         message = data["message"]

#         def generate():
#             stream = client.chat.completions.create(
#                 model="gpt-4",
#                 messages=[{"role": "user", "content": message}],
#                 stream=True
#             ) 

#             for chunk in stream:
#                 if chunk.choices[0].delta.content is not None:
#                     yield(chunk.choices[0].delta.content)

#         return generate(), {"Content-Type": "text/plain"}

# return app

# @app.get("/test_openai")
# def get_response(user_message, history):
#     # Append the user message to the conversation history
#     history.append({"role": "user", "content": user_message})

#     # Send the updated conversation to the API
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=history
#     )

#     # Extract the latest response from the model
#     ai_response = response['choices'][0]['message']['content']

#     # Optionally, update the history with the AI's response
#     history.append({"role": "ai", "content": ai_response})

#     return ai_response, history

# def respond(user_message, history=[]):
#     return get_response(user_message, history)

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



