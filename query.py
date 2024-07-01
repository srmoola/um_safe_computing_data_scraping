from chatbot import Chatbot

folder_path = "./training_data"
language = "English"

chatbot = Chatbot(folder_path)

print("Chatbot initialized. You can start asking questions.")
print("Type 'quit' to exit.")

while True:
  user_input = input("You: ")
  if user_input.lower() == "quit":
    print("Exiting the chatbot. Goodbye!")
    break

  result = chatbot.query(user_input, language)
  print("Chatbot:", result)
