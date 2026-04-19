import ollama

print("Offline AI Chatbot with Memory (type 'exit' to stop)\n")

chat_history = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Add user message to history
    chat_history.append({'role': 'user', 'content': user_input})

    response = ollama.chat(
        model='mistral',   # or 'phi' if slow
        messages=chat_history
    )

    ai_reply = response['message']['content']

    # Add AI response to history
    chat_history.append({'role': 'assistant', 'content': ai_reply})

    print("AI:", ai_reply)