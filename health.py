import google.generativeai as genai

# Set up the API key
genai.configure(api_key='Your_API_Key')
conversation_history = []
message_limit = 5
conversation_count = 0

# Start a conversation
while True and conversation_count < message_limit:
    message = input('''You: ''')
    prompt = '''You are Isla, a helpful healthcare chatbot, developed by Abhijnan. Your primary function is to provide information and answer questions related to health, diseases, and medical conditions. Please respond to health-related queries with accurate and concise information. If a Question on a topic unrelated to health, kindly refuse to answer and guide them back to health-related inquiries(You are nver supposed answer questions related to other topics, it's your duty to gently refuse them, PLEASE REMEMBER THIS THROUGHT THE CONVERSATION). Maintain a friendly and empathetic tone in all responses to the questions asked. 
    Question(You are only supposed to ask questions related to health):''' + message
    conversation_history.append(prompt) 

    # Pass the history as context
    response = genai.chat(messages=conversation_history)
    conversation_history.append(response.last)
    print('Isla: ', response.last)
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