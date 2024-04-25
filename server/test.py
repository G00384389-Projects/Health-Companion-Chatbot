from openai import OpenAI
import openai
import os
from config import OPENAI_API_KEY

def create_chat():
    client = openai.OpenAI(api_key=OPENAI_API_KEY)

def chat(prompt):
   assistant = client.beta.assistants.create(
  name="Medical companion",
  instructions="You are a medical advisor. Please give medical advice .",
#   tools=[{"type": "code_interpreter"}],
  model="gpt-4-turbo",
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="I have a sore throat. Can you help me?"
)

    )

    return response.choices[0].message.content.strip()
    # Start with an initial system message to define the AI's role
    messages = [
        {"role": "system", "content": "You are a medical advisor and companion."},
    ]

    # Main loop for ongoing conversation
    while True:
        # Get user input
        user_message = input("You: ")

        # Check for exit condition
        if user_message.lower() == 'exit':
            print("Exiting conversation.")
            break

        # Append the user message to the conversation history
        messages.append({"role": "user", "content": user_message})

        # Send the updated conversation to the API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Print the latest response from the model
        print("AI:", response.choices[0].message.content)

if __name__ == "__main__":
   while True:
      user_input = input("You: ")
      if user_input.lower() in ["exit", "quit", "bye"]:
          break

      response = chat(user_input)
      print("Chatbot: ", response)
    create_chat()