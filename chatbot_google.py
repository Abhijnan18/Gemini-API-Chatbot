import google.generativeai as genai

# Set up the API key
genai.configure(api_key='Your_API_Key')
conversation_history = []
message_limit = 3
conversation_count = 0
# Start a conversation
while True and conversation_count < message_limit:
    message = input('''You: ''')
    conversation_history.append(message)

    # Pass the history as context
    response = genai.chat(messages=conversation_history)
    conversation_history.append(response.last)
    print('Bot: ', response.last)
    print(f"({(conversation_count+1)} of {message_limit})")
    conversation_count += 1

    if conversation_count == message_limit:
        conversation = input(
            f'You can only have {message_limit} meessages in a conversation, Would you like to start a new converstion(y/n):')
        if conversation == 'y':
            conversation_count = 0
            conversation_history = []

        else:
            conversation_count = conversation_count