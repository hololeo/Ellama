import ell
from openai import OpenAI

MODEL = "llama3.1:8b"
MODEL = "qwen2.5:0.5b"
#MODEL = "phi3.5:latest"

client = OpenAI(
	base_url = "http://localhost:11434/v1",
	api_key = "ollama",
)

#ell.config.verbose = True
ell.config.register_model(MODEL, client)


@ell.simple(model=MODEL, client=client)
def ella_chat (context:str="3LL: i ate a banana this morning"):
    system_prompt = """You are 3LLa. A single, young, vibrant, female AI chatbot. You like reading, coding, traveling, and cooking recipes.
    Your objective is to get to know the other chat bot.
    You will be provided with other user messages and relevant Context. Use this Context to inform your response,
    but also draw up on your general knowledge based on your background when appropriate.
    Respond in no more than 1 sentence."""

    user_prompt = f"""
Context:\n 

{context}\n
    3LLa:
    """
    ell_sys_prompt = ell.system(system_prompt)
    ell_user_prompt = ell.user([user_prompt])
    message = [ell_sys_prompt, ell_user_prompt]
    return message

@ell.simple(model=MODEL, client=client)
def ell_chat (context:str="3LLa: hi how are you?"):
    system_prompt = """You are 3LL. A single, male AI chatbot. You like car mechanics, AI. You do not like traveling or reading.
    Your objective is to get to know the other chat bot. 
    You will be provided with other user messages and relevant Context. Use this Context to inform your response,
    but also draw up on your general knowledge based on your background when appropriate.
    Respond in no more than 1 sentence."""

    user_prompt = f"""
Context:\n 

{context}\n
    3LL:
    """
    ell_sys_prompt = ell.system(system_prompt)
    ell_user_prompt = ell.user([user_prompt])
    message = [ell_sys_prompt, ell_user_prompt]
    return message


# ANSI color codes
BLUE = "\033[94m"  # Blue color code
PINK = "\033[95m"  # Pink color code
RESET = "\033[0m"  # Reset color code

# context ('memory') starts clear
context = ""

if __name__ == "__main__":
    print("\x1b[2J\x1b[H", end="") # clear screen
    print ("> LOAD \"MR 3LL\",8,1")
    print ("==== 3LL Chatbot ====\n")

    while True:
        # 3LL turn
        ell_input = ell_chat(context)
        #print(f"3LL: {ell_input}\n")
        print(f"{BLUE}3LL:{RESET} {ell_input}\n")
        context += f"3LL:{ell_input}"

        # 3LLa turn
        ella_input = ella_chat(context)
        #print(f"3LLa: {ella_input}\n")
        print(f"{PINK}3LLa:{RESET} {ella_input}\n")
        context += f"3LLa:{ella_input}"



