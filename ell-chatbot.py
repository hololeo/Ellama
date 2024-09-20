import ell
from openai import OpenAI

MODEL = "llama3.1:8b"
client = OpenAI(
	base_url = "http://localhost:11434/v1",
	api_key = "ollama",
)

#ell.config.verbose = True
ell.config.register_model(MODEL, client)


@ell.simple(model=MODEL, client=client)
def send_chat(user_message: str, context:str="You ate a banana this morning"):
    system_prompt = """You are Mr 3LL. You chat about AI and car mechanics
    You will be provided with a User message and relevant Context. Use this Context to inform your response, but also draw up on your general knowledge based on your background when appropriate."
    Respond in no more than 1 or 2 sentences."""

    user_prompt = f"""
Context:\n 

{context}\n

User: {user_message}\n

Reponse:
    """

    ell_sys_prompt = ell.system(system_prompt)
    ell_user_prompt = ell.user([user_prompt])
    message = [ell_sys_prompt, ell_user_prompt]
    return message

# context ('memory') starts clear
context = ""

if __name__ == "__main__":
    print("\x1b[2J\x1b[H", end="") # clear screen
    print ("> LOAD \"MR 3LL\",8,1")
    print ("==== 3LL Chatbot ====\n")

    while True:
        # Get input from the user
        user_input = input("You: ")
        # we add users message to the context
        context += f"User: {user_input}\n\n"
        print ("\n")
        
        # Exit the loop if the user types 'exit'
        if user_input.lower() == 'exit':
            print("Exiting... 3LL SHUTDOWN.")
            break

        # Send user input to the chat function and get response
        response = send_chat(user_input, context)
        # we add models response to the context
        context += f"Response: {response}\n"
        # Print the response from Mr. 3LL
        print(f"3LL: {response}\n")


