import openai
from config import OPENAI_API_KEY

def create_chat():
    #client = openai.OpenAI()

    client = openai.OpenAI(api_key=OPENAI_API_KEY)
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
        print("MedBot:", response.choices[0].message.content+"\n")

if __name__ == "__main__":
    create_chat()
