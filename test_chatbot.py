import openai

# Directly set your OpenAI API key
api_key = "sk-proj-aZfIiwp1glz4GTTHlSRlT3BlbkFJeFwN7yjKxq6rhq3v3BVN"

openai.api_key = api_key

def get_chatbot_response(user_message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        bot_message = response.choices[0].message['content'].strip()
        return bot_message
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Chatbot Console Test")
    print("Type 'exit' to quit the chat.")
    while True:
        user_message = input("You: ")
        if user_message.lower() == 'exit':
            print("Exiting chat.")
            break
        bot_response = get_chatbot_response(user_message)
        print(f"Bot: {bot_response}")

if __name__ == "__main__":
    main()