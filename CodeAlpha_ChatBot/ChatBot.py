def chatbot():
    print("Chatbot:HELLO I AM BASIC CHATBOT.")
    print("Type 'bye' to exit.\n")

while True:
    msg = input("You: ").lower()
    
    if msg == "bye":
        print("Chabot: GoodBye!")
        break
        
    elif msg =="hello" or msg =="hi":
        print("Chabot: Hi How can I help you?")
        
    elif "name" in msg:
        print("Chatbot : My name is PyBot.")
        
    elif"how are you" in msg:
        print("Chatbot:  I am just a program ,but I am fine!")
        
    elif"help" in msg:
        print("Chatbot: You can ask about my name,greet me,or say exit.")
        
    else:
        print("Chatbot:Sorry, I didnt understand that.")
    
chatbot()